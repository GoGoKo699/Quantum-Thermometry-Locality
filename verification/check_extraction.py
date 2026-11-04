#!/usr/bin/env python3
"""Finite-chain verification of extraction, susceptibility, and estimation.

Run from any working directory:
    python verification/check_extraction.py
    python verification/check_extraction.py --output /tmp/extraction.json

Two long finite chains are compared at fixed times before far-boundary
reflections. Boundary-vector propagation and integrated detector current
provide an independent check of dense one-particle loss matrices. A separate
short, exhausted bath documents that indefinite linear extraction is an
infinite-volume statement. No finite computation proves that limit.
"""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy import sparse
from scipy.integrate import simpson
from scipy.linalg import eigh, expm
from scipy.optimize import brentq
from scipy.sparse.linalg import expm_multiply
from scipy.special import expit, j1


NU = 3.0
KAPPA = 0.5
B_INTERVAL = (0.3, 1.2)
TIMES = (0.5, 4.0, 12.0)
Q_LOWER = 1.0 - 8.0 * KAPPA / (3.0 * np.pi)


def hamiltonian(sites: int) -> np.ndarray:
    return NU * np.eye(sites) - np.eye(sites, k=1) - np.eye(sites, k=-1)


def probability_vector(eigenvalues: np.ndarray) -> np.ndarray:
    probabilities = np.array([1.0])
    for occupation in np.clip(eigenvalues, 0.0, 1.0):
        probabilities = np.convolve(
            probabilities, [1.0 - occupation, occupation]
        )
    return probabilities


def inverse_mean_estimator(loss_in_energy_basis: np.ndarray,
                           energies: np.ndarray) -> np.ndarray:
    """Return the clipped estimate for every possible finite-bath count."""
    weights = np.diag(loss_in_energy_basis).real

    def mean(b):
        return float(weights @ expit(-b * energies))

    b_min, b_max = B_INTERVAL
    lower_mean, upper_mean = mean(b_max), mean(b_min)
    estimates = []
    for count in range(len(energies) + 1):
        if count <= lower_mean:
            estimate = b_max
        elif count >= upper_mean:
            estimate = b_min
        else:
            estimate = brentq(lambda b: mean(b) - count, b_min, b_max,
                             xtol=1e-13)
        estimates.append(estimate)
    return np.array(estimates)


def finite_chain(bath_sites: int):
    sites = bath_sites + 1
    h = hamiltonian(sites)
    generator = -1j * h
    generator[0, 0] -= KAPPA / 2.0
    initial_boundary = np.zeros(sites, dtype=complex)
    initial_boundary[0] = 1.0
    # Sparse propagation of just one vector does not construct the dense
    # propagator used independently below. The 0.01 grid resolves current
    # integration much more finely than the hopping time.
    grid = np.linspace(0.0, max(TIMES), 1201)
    boundary_vectors = expm_multiply(
        sparse.csr_matrix(generator), initial_boundary,
        start=grid[0], stop=grid[-1], num=len(grid), endpoint=True
    )
    survival = np.sum(abs(boundary_vectors)**2, axis=1)
    free_vectors = expm_multiply(
        sparse.csr_matrix(-1j * h), initial_boundary,
        start=grid[0], stop=grid[-1], num=len(grid), endpoint=True
    )
    exact_free_return = np.ones(len(grid), dtype=complex)
    exact_free_return[1:] = (
        np.exp(-1j * NU * grid[1:]) * j1(2 * grid[1:]) / grid[1:]
    )
    free_return_error = float(np.max(abs(
        free_vectors[:, 0] - exact_free_return
    )))
    assert free_return_error < 2e-10
    assert survival.min() > Q_LOWER - 2e-10

    energies, modes = eigh(hamiltonian(bath_sites))
    covariance_data = {}
    for b in B_INTERVAL[:1] + (0.7,) + B_INTERVAL[1:]:
        occupations = expit(-b * energies)
        covariance = (modes * occupations) @ modes.T
        current = KAPPA * np.einsum(
            "ti,ij,tj->t", boundary_vectors[:, 1:],
            covariance, boundary_vectors[:, 1:].conj(),
            optimize=True
        ).real
        covariance_data[b] = (occupations, covariance, current)

    eta = expit(-B_INTERVAL[1] * (NU + 2))
    m_conservative = (NU - 2) * eta * (1.0 - eta)
    rows = []
    summaries = {}
    for tau in TIMES:
        propagator = expm(tau * generator)
        loss = np.eye(sites) - propagator.conj().T @ propagator
        loss = (loss + loss.conj().T) / 2
        bath_loss = loss[1:, 1:]
        trace_loss = float(np.trace(loss).real)
        trace_bath_loss = float(np.trace(bath_loss).real)
        eig_loss = np.linalg.eigvalsh(loss)
        assert eig_loss.min() > -2e-11
        assert eig_loss.max() < 1.0 + 2e-11
        assert trace_bath_loss >= KAPPA * Q_LOWER * tau - 1.0 - 2e-10
        assert trace_bath_loss <= KAPPA * tau + 2e-10
        last = int(round(tau / (grid[1] - grid[0])))
        integration_grid = grid[:last + 1]
        trace_by_boundary = float(KAPPA * simpson(
            survival[:last + 1], x=integration_grid
        ))
        boundary_trace_error = abs(trace_loss - trace_by_boundary)
        assert boundary_trace_error < 2e-8
        loss_energy = modes.T @ bath_loss @ modes
        weights = np.diag(loss_energy).real
        estimates = inverse_mean_estimator(loss_energy, energies)

        for b, (occupations, covariance, current) in covariance_data.items():
            mean = float(np.trace(covariance @ bath_loss).real)
            mean_by_current = float(simpson(
                current[:last + 1], x=integration_grid
            ))
            root_covariance = (
                modes * np.sqrt(occupations)
            ) @ modes.T
            q = root_covariance @ bath_loss @ root_covariance
            q = (q + q.conj().T) / 2
            q_eigenvalues = np.linalg.eigvalsh(q)
            variance = float(np.trace(q - q @ q).real)
            susceptibility = float(
                weights @ (energies * occupations * (1 - occupations))
            )
            delta = 1e-5
            derivative_by_difference = float(
                weights @ (expit(-(b - delta) * energies)
                           - expit(-(b + delta) * energies)) / (2 * delta)
            )
            probabilities = probability_vector(q_eigenvalues)
            b_risk = float(probabilities @ (estimates - b)**2)
            log_risk = float(
                probabilities @ (np.log(estimates) - np.log(b))**2
            )
            extraction_threshold = 2.0 / (KAPPA * Q_LOWER)
            if tau < extraction_threshold:
                protocol_estimator = "interval_midpoint"
                midpoint = sum(B_INTERVAL) / 2.0
                protocol_b_risk = (midpoint - b)**2
                protocol_log_risk = (np.log(midpoint) - np.log(b))**2
            else:
                protocol_estimator = "clipped_inverse_mean"
                protocol_b_risk = b_risk
                protocol_log_risk = log_risk
            risk_bound = variance / (m_conservative * trace_bath_loss)**2
            assert abs(mean - mean_by_current) < 2e-8
            assert abs(susceptibility - derivative_by_difference) < 2e-8
            assert susceptibility >= m_conservative * trace_bath_loss - 2e-10
            assert variance <= mean + 2e-10
            assert mean <= 0.5 * trace_bath_loss + 2e-10
            assert b_risk <= risk_bound + 2e-10
            assert log_risk <= risk_bound / B_INTERVAL[0]**2 + 2e-10
            assert abs(probabilities.sum() - 1.0) < 2e-11
            rows.append({
                "tau": tau,
                "b": b,
                "trace_bath_loss": trace_bath_loss,
                "mean": mean,
                "variance": variance,
                "susceptibility": susceptibility,
                "integrated_current_error": abs(mean - mean_by_current),
                "susceptibility_finite_difference_error": abs(
                    susceptibility - derivative_by_difference
                ),
                "clipped_inverse_b_mse": b_risk,
                "clipped_inverse_log_temperature_mse": log_risk,
                "protocol_estimator": protocol_estimator,
                "protocol_b_mse": protocol_b_risk,
                "protocol_log_temperature_mse": protocol_log_risk,
            })
        summaries[tau] = {
            "trace_bath_loss": trace_bath_loss,
            "boundary_trace_integration_error": boundary_trace_error,
            "survival": float(survival[last]),
            "means": [row["mean"] for row in rows if row["tau"] == tau],
        }
    return {
        "bath_sites": bath_sites,
        "free_boundary_return_max_error": free_return_error,
        "minimum_boundary_survival": float(survival.min()),
        "survival_lower_bound": Q_LOWER,
        "rows": rows,
    }, summaries


def exhausted_finite_bath() -> dict:
    # In a chain of three bath spins, trace M <= 3 for all times. By tau=200,
    # this system is essentially empty. Applying the infinite-chain linear
    # bound here would be a clear, reproducible error.
    bath_sites = 3
    tau = 200.0
    generator = -1j * hamiltonian(bath_sites + 1)
    generator[0, 0] -= KAPPA / 2
    propagator = expm(tau * generator)
    loss = np.eye(bath_sites + 1) - propagator.conj().T @ propagator
    trace_bath_loss = float(np.trace(loss[1:, 1:]).real)
    purported_lower = KAPPA * Q_LOWER * tau - 1.0
    assert trace_bath_loss <= bath_sites + 1e-10
    assert trace_bath_loss > bath_sites - 1e-5
    assert purported_lower > trace_bath_loss + 1.0
    return {
        "bath_sites": bath_sites,
        "tau": tau,
        "trace_bath_loss": trace_bath_loss,
        "infinite_chain_lower_bound_inapplicable_here": purported_lower,
        "meaning": (
            "The finite bath saturates at its finite number of initial modes. "
            "This intentionally violates an invalid finite-volume extension "
            "of the infinite-chain linear bound."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also save the JSON report.")
    arguments = parser.parse_args()
    reports = []
    summaries = []
    for bath_sites in (48, 80):
        report, summary = finite_chain(bath_sites)
        reports.append(report)
        summaries.append(summary)
    length_comparison = []
    for tau in TIMES:
        first, second = summaries[0][tau], summaries[1][tau]
        trace_difference = abs(
            first["trace_bath_loss"] - second["trace_bath_loss"]
        )
        mean_difference = float(np.max(abs(
            np.array(first["means"]) - np.array(second["means"])
        )))
        assert trace_difference < 2e-9
        assert mean_difference < 2e-9
        length_comparison.append({
            "tau": tau,
            "trace_difference_between_lengths": trace_difference,
            "maximum_mean_difference_between_lengths": mean_difference,
            "maximum_boundary_trace_integration_error": max(
                first["boundary_trace_integration_error"],
                second["boundary_trace_integration_error"]
            ),
        })
    result = {
        "check": "finite_chain_extraction_and_global_estimator",
        "status": "passed",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "nu": NU,
        "kappa": KAPPA,
        "inverse_temperature_interval": B_INTERVAL,
        "scope": (
            "Bath lengths 48 and 80 at tau <= 12, checked against each other "
            "and the exact free half-chain return. This is finite-time "
            "numerical evidence; the infinite-volume proof is analytic."
        ),
        "length_comparison": length_comparison,
        "finite_bath_limitation": exhausted_finite_bath(),
        "chains": reports,
    }
    encoded = json.dumps(result, indent=2)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)


if __name__ == "__main__":
    main()
