#!/usr/bin/env python3
"""Check restricted Gaussian relative entropy against a full Fock calculation.

The local covariance is compressed from a longer thermal chain. It is not
replaced by the thermal covariance of the isolated local Hamiltonian. The
two compressed covariances generally do not commute. A separate many-body
matrix calculation checks the relative-entropy identity and its uniform
quadratic bound on these finite instances.
"""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigh, expm
from scipy.special import expit


def matrix_function(matrix, function):
    eigenvalues, modes = eigh(matrix)
    return (modes * function(eigenvalues)) @ modes.conj().T


def annihilators(sites):
    lowering = np.array([[0.0, 1.0], [0.0, 0.0]])
    parity = np.diag([1.0, -1.0])
    operators = []
    for site in range(sites):
        operator = np.array([[1.0]])
        for position in range(sites):
            factor = parity if position < site else (
                lowering if position == site else np.eye(2)
            )
            operator = np.kron(operator, factor)
        operators.append(operator)
    return operators


def fock_state(covariance):
    sites = covariance.shape[0]
    single_particle = matrix_function(
        covariance, lambda x: np.log1p(-x) - np.log(x)
    )
    operators = annihilators(sites)
    generator = np.zeros((2**sites, 2**sites), dtype=complex)
    for i in range(sites):
        for j in range(sites):
            generator += single_particle[i, j] * (
                operators[i].conj().T @ operators[j]
            )
    state = expm(-generator)
    state /= np.trace(state)
    recovered = np.array([
        [np.trace(state @ operators[j].conj().T @ operators[i])
         for j in range(sites)] for i in range(sites)
    ])
    assert np.max(np.abs(recovered - covariance)) < 2e-12
    return state


def relative_entropy(state, reference):
    return float(np.trace(state @ (
        matrix_function(state, np.log) - matrix_function(reference, np.log)
    )).real)


def covariance_relative_entropy(c, d):
    identity = np.eye(c.shape[0])
    return float(np.trace(
        c @ (matrix_function(c, np.log) - matrix_function(d, np.log))
        + (identity - c) @ (
            matrix_function(identity - c, np.log)
            - matrix_function(identity - d, np.log)
        )
    ).real)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also save the JSON report.")
    arguments = parser.parse_args()
    nu = 3.2
    full_sites = 19
    b_interval = (0.2, 1.2)
    hamiltonian = (
        nu * np.eye(full_sites)
        - np.eye(full_sites, k=1) - np.eye(full_sites, k=-1)
    )
    energies, modes = eigh(hamiltonian)
    eta = float(expit(-b_interval[1] * (nu + 2)))
    coefficient = (nu + 2)**2 / (32 * eta * (1 - eta))
    results = []
    for sites in (2, 3, 4):
        for b, other_b in ((0.2, 0.8), (0.55, 1.1), (0.7, 0.701)):
            c = ((modes * expit(-b * energies)) @ modes.T)[:sites, :sites]
            d = ((modes * expit(-other_b * energies)) @ modes.T)[:sites, :sites]
            rho, sigma = fock_state(c), fock_state(d)
            actual = relative_entropy(rho, sigma)
            predicted = covariance_relative_entropy(c, d)
            difference_squared = float(np.linalg.norm(c - d, "fro")**2)
            hessian_bound = difference_squared / (2 * eta * (1 - eta))
            temperature_bound = coefficient * sites * (b - other_b)**2
            trace_distance = float(np.sum(np.abs(eigh(
                rho - sigma, eigvals_only=True
            ))) / 2)
            assert actual >= -2e-12
            assert abs(actual - predicted) < 3e-11
            assert actual <= hessian_bound + 3e-11
            assert hessian_bound <= temperature_bound + 3e-11
            assert trace_distance**2 <= actual / 2 + 3e-11

            # Quantify the distinction between restriction and rethermalizing
            # a cut Hamiltonian; the converse uses the former throughout.
            cut_hamiltonian = hamiltonian[:sites, :sites]
            cut_covariance = matrix_function(
                cut_hamiltonian, lambda energy: expit(-b * energy)
            )
            results.append({
                "restricted_sites": sites,
                "b": b,
                "other_b": other_b,
                "covariance_commutator_frobenius": float(np.linalg.norm(
                    c @ d - d @ c, "fro"
                )),
                "restriction_vs_cut_gibbs_frobenius": float(np.linalg.norm(
                    c - cut_covariance, "fro"
                )),
                "fock_relative_entropy": actual,
                "covariance_formula_error": abs(actual - predicted),
                "hessian_bound": hessian_bound,
                "uniform_temperature_bound": temperature_bound,
                "trace_distance": trace_distance,
            })
    assert max(row["covariance_commutator_frobenius"] for row in results) > 1e-5
    assert max(row["restriction_vs_cut_gibbs_frobenius"] for row in results) > 1e-3
    report = {
        "check": "restricted_gaussian_relative_entropy",
        "status": "passed",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "scope": (
            "Nine finite restricted thermal-state pairs; direct 4-, 8-, "
            "and 16-dimensional Fock density matrices. The general "
            "matrix bound and complete-output locality are analytical."
        ),
        "full_chain_sites": full_sites,
        "nu": nu,
        "b_interval": list(b_interval),
        "eta": eta,
        "quadratic_coefficient": coefficient,
        "maximum_covariance_formula_error": max(
            row["covariance_formula_error"] for row in results
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
