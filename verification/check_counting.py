#!/usr/bin/env python3
"""Compare the full count law with an independent number-resolved spin solver.

Run from any working directory:
    python verification/check_counting.py
    python verification/check_counting.py --output /tmp/counting.json

The dynamical side uses tensor products of physical spin matrices, a many-body
Gibbs density matrix, and a number-resolved Lindblad equation. Only the separate
prediction uses a one-particle covariance and determinant/Poisson-binomial law.
Small finite baths make the entire count distribution accessible without a
Monte Carlo error or a Gaussian assumption in the spin calculation.
"""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy import sparse
from scipy.linalg import eigh, expm
from scipy.sparse.linalg import expm_multiply
from scipy.special import expit


def spin_site(operator: np.ndarray, site: int, sites: int) -> sparse.csr_matrix:
    result = sparse.csr_matrix([[1.0 + 0.0j]])
    for position in range(sites):
        factor = operator if position == site else np.eye(2)
        result = sparse.kron(result, factor, format="csr")
    return result


def spin_chain(sites: int, nu: float):
    lowering = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    minus = [spin_site(lowering, position, sites) for position in range(sites)]
    number = [operator.getH() @ operator for operator in minus]
    dimension = 2**sites
    hamiltonian = sparse.csr_matrix((dimension, dimension), dtype=complex)
    for occupation in number:
        hamiltonian += nu * occupation
    for position in range(sites - 1):
        exchange = minus[position].getH() @ minus[position + 1]
        hamiltonian -= exchange + exchange.getH()
    return hamiltonian.tocsr(), minus, number


def spin_count_distribution(bath_sites: int, nu: float, b: float,
                            kappa: float, tau: float):
    bath_hamiltonian, _, _ = spin_chain(bath_sites, nu)
    thermal = expm(-b * bath_hamiltonian.toarray())
    thermal /= np.trace(thermal)
    initial = np.kron(np.diag([1.0, 0.0]), thermal)

    hamiltonian, minus, number = spin_chain(bath_sites + 1, nu)
    dimension = hamiltonian.shape[0]
    identity = sparse.eye(dimension, format="csr", dtype=complex)
    n0 = number[0]
    # Column-major vectorization: vec(A rho B) = (B.T tensor A) vec(rho).
    no_jump = (
        -1j * (sparse.kron(identity, hamiltonian)
               - sparse.kron(hamiltonian.T, identity))
        - 0.5 * kappa * (sparse.kron(identity, n0)
                         + sparse.kron(n0.T, identity))
    ).tocsr()
    jump = kappa * sparse.kron(minus[0].conjugate(), minus[0], format="csr")

    # Sensor starts empty; no excitation is created, so counts 0,...,bath_sites
    # are the exact complete support, not a count-space approximation.
    count_dimension = bath_sites + 1
    forward_count = sparse.diags(
        [np.ones(count_dimension - 1)], [-1],
        shape=(count_dimension, count_dimension), format="csr"
    )
    generator = (
        sparse.kron(sparse.eye(count_dimension), no_jump, format="csr")
        + sparse.kron(forward_count, jump, format="csr")
    )
    vector = np.zeros(count_dimension * dimension**2, dtype=complex)
    vector[:dimension**2] = initial.reshape(-1, order="F")
    final = expm_multiply(tau * generator, vector)
    blocks = [
        final[index * dimension**2:(index + 1) * dimension**2]
        .reshape((dimension, dimension), order="F")
        for index in range(count_dimension)
    ]
    probabilities_complex = np.array([np.trace(block) for block in blocks])
    probabilities = probabilities_complex.real
    density = sum(blocks)
    total_number = sum(number).toarray()
    excitation_lost = np.trace(total_number @ (initial - density)).real
    return probabilities, {
        "normalization_error": float(abs(probabilities.sum() - 1.0)),
        "imaginary_probability_error": float(np.max(np.abs(
            probabilities_complex.imag))),
        "minimum_probability": float(probabilities.min()),
        "minimum_density_eigenvalue": float(np.linalg.eigvalsh(
            (density + density.conj().T) / 2).min()),
        "excitation_lost": float(excitation_lost),
    }


def gaussian_prediction(bath_sites: int, nu: float, b: float,
                        kappa: float, tau: float):
    h_bath = (
        nu * np.eye(bath_sites)
        - np.eye(bath_sites, k=1) - np.eye(bath_sites, k=-1)
    )
    energies, modes = eigh(h_bath)
    root_covariance = (modes * np.sqrt(expit(-b * energies))) @ modes.T
    total_sites = bath_sites + 1
    h_extended = (
        nu * np.eye(total_sites)
        - np.eye(total_sites, k=1) - np.eye(total_sites, k=-1)
    )
    generator = -1j * h_extended
    generator[0, 0] -= kappa / 2
    propagator = expm(tau * generator)
    loss = np.eye(total_sites) - propagator.conj().T @ propagator
    q = root_covariance @ loss[1:, 1:] @ root_covariance
    q = (q + q.conj().T) / 2
    occupations = np.linalg.eigvalsh(q)
    if occupations.min() < -2e-12 or occupations.max() > 1 + 2e-12:
        raise AssertionError("The prediction is not a positive contraction.")
    occupations = np.clip(occupations, 0.0, 1.0)
    probabilities = np.array([1.0])
    for value in occupations:
        probabilities = np.convolve(probabilities, [1.0 - value, value])
    return probabilities, q


def verify_case(bath_sites: int, nu: float, b: float,
                kappa: float, tau: float) -> dict:
    actual, diagnostics = spin_count_distribution(
        bath_sites, nu, b, kappa, tau
    )
    predicted, q = gaussian_prediction(bath_sites, nu, b, kappa, tau)
    count = np.arange(bath_sites + 1)
    mean = float(count @ actual)
    variance = float((count - mean)**2 @ actual)
    trace_mean = float(np.trace(q).real)
    trace_variance = float(np.trace(q - q @ q).real)
    distribution_error = float(np.max(np.abs(actual - predicted)))
    phases = np.array([0.37, 1.2, 2.5])
    characteristic_error = float(max(
        abs(np.exp(1j * phase * count) @ actual
            - np.linalg.det(np.eye(bath_sites)
                            + (np.exp(1j * phase) - 1.0) * q))
        for phase in phases
    ))
    tolerance = 2e-10
    assert diagnostics["normalization_error"] < tolerance
    assert diagnostics["imaginary_probability_error"] < tolerance
    assert diagnostics["minimum_probability"] > -tolerance
    assert diagnostics["minimum_density_eigenvalue"] > -tolerance
    assert distribution_error < tolerance
    assert characteristic_error < tolerance
    assert abs(mean - trace_mean) < tolerance
    assert abs(variance - trace_variance) < tolerance
    assert abs(mean - diagnostics["excitation_lost"]) < tolerance
    return {
        "bath_sites": bath_sites,
        "nu": nu,
        "b": b,
        "kappa": kappa,
        "tau": tau,
        "full_pmf_max_error": distribution_error,
        "characteristic_max_error": characteristic_error,
        "mean": mean,
        "variance": variance,
        "mean_formula_error": abs(mean - trace_mean),
        "variance_formula_error": abs(variance - trace_variance),
        "excitation_balance_error": abs(mean - diagnostics["excitation_lost"]),
        **diagnostics,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also save the JSON report.")
    arguments = parser.parse_args()
    # Includes vacuum-at-zero-time, weak initial exposure, and several
    # nontrivial interacting spin evolutions. Fixed kappa=1/2 is the protocol.
    cases = [
        (2, 3.0, 0.7, 0.5, 0.0),
        (2, 2.2, 0.3, 0.5, 0.1),
        (1, 3.0, 0.7, 0.5, 2.3),
        (3, 3.0, 1.2, 0.5, 4.0),
        (4, 2.4, 0.4, 0.5, 2.3),
    ]
    results = [verify_case(*case) for case in cases]
    report = {
        "check": "independent_number_resolved_spin_counting",
        "status": "passed",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "scope": (
            "Exact finite spin baths; full probability laws. This verifies "
            "the spin-to-determinant identification at these instances, "
            "not the infinite-volume theorem."
        ),
        "maximum_full_pmf_error": max(
            result["full_pmf_max_error"] for result in results
        ),
        "cases": results,
    }
    encoded = json.dumps(report, indent=2)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)


if __name__ == "__main__":
    main()
