#!/usr/bin/env python3
"""Compare detuned detector susceptibility with the half-chain formula.

Run with python verification/check_detuned_response.py. Use --output PATH
to retain the tested parameters and results as JSON.
"""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy import sparse
from scipy.integrate import quad, simpson
from scipy.linalg import eigh_tridiagonal
from scipy.sparse.linalg import expm_multiply
from scipy.special import expit


INVERSE_TEMPERATURES = (0.5, 1.0, 2.0, 4.0)
ELAPSED_TIME = 80.0
BATH_SITES = 245


def thermal_response(energy: np.ndarray | float, b: float):
    """Negative derivative in b of the Fermi occupation."""
    return energy * expit(-b * energy) * expit(b * energy)


def finite_slopes(nu: float, detuning: float, kappa: float) -> list[float]:
    """Integrate the susceptibility of the actual vacuum-sensor preparation."""
    sites = BATH_SITES + 1
    diagonal = np.full(sites, 1j * nu, dtype=complex)
    diagonal[0] += 1j * detuning - kappa / 2
    hopping = np.full(sites - 1, -1j)
    adjoint_generator = sparse.diags(
        (hopping, diagonal, hopping), (-1, 0, 1), format="csr"
    )
    endpoint = np.zeros(sites, dtype=complex)
    endpoint[0] = 1
    grid = np.linspace(0.0, ELAPSED_TIME, 801)
    states = expm_multiply(
        adjoint_generator, endpoint, start=0.0, stop=ELAPSED_TIME,
        num=len(grid), endpoint=True
    )
    energies, modes = eigh_tridiagonal(
        np.full(BATH_SITES, nu), np.full(BATH_SITES - 1, -1.0)
    )
    instantaneous_weights = np.abs(states[:, 1:] @ modes) ** 2
    mean_weights = kappa * simpson(
        instantaneous_weights, x=grid, axis=0
    ) / ELAPSED_TIME
    return [
        float(mean_weights @ thermal_response(energies, b))
        for b in INVERSE_TEMPERATURES
    ]


def continuum_slope(nu: float, detuning: float, kappa: float, b: float) -> float:
    """Integrate the exact spectral weight by E = nu - 2 cos(q)."""
    def integrand(q: float) -> float:
        sine = np.sin(q)
        centered_energy = -2 * np.cos(q)
        denominator = (
            1 + detuning**2 + kappa**2 / 4
            - detuning * centered_energy + kappa * sine
        )
        return (
            (2 / np.pi) * sine**2 * thermal_response(nu + centered_energy, b)
            / denominator
        )

    integral, _ = quad(integrand, 0.0, np.pi, epsabs=1e-13)
    return kappa * integral


def verify() -> dict:
    cases = (
        (0.0, 0.0, 0.5),
        (0.0, 0.5, 0.5),
        (0.0, 0.5, 2.0),
        (0.25, 0.5, 0.5),
        (-0.25, -0.5, 0.5),
        (2.0, 0.5, 0.5),
        (-2.0, -0.5, 0.5),
    )
    rows = []
    for nu, detuning, kappa in cases:
        finite = np.asarray(finite_slopes(nu, detuning, kappa))
        spectral = np.asarray([
            continuum_slope(nu, detuning, kappa, b)
            for b in INVERSE_TEMPERATURES
        ])
        comparison = {"absolute_max_error": float(np.max(abs(finite - spectral)))}
        if detuning == 0:
            assert np.max(abs(finite)) < 1e-11
            assert np.max(abs(spectral)) < 1e-13
        else:
            sign = np.sign(detuning)
            assert np.all(sign * finite > 0)
            assert np.all(sign * spectral > 0)
            relative_error = float(np.max(abs((finite - spectral) / spectral)))
            assert relative_error < 0.05
            comparison["relative_max_error"] = relative_error
        rows.append({
            "nu": nu,
            "detuning": detuning,
            "kappa": kappa,
            "finite_susceptibility_per_time": finite.tolist(),
            "continuum_susceptibility_per_time": spectral.tolist(),
            **comparison,
        })
    return {
        "check": "detuned_boundary_count_response",
        "status": "passed",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "scope": (
            "Temperature derivatives of the mean count from one finite bath, "
            "compared at a fixed elapsed time to half-chain spectral quadrature."
        ),
        "bath_sites": BATH_SITES,
        "elapsed_time": ELAPSED_TIME,
        "inverse_temperatures": INVERSE_TEMPERATURES,
        "cases": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also save the JSON report.")
    arguments = parser.parse_args()
    encoded = json.dumps(verify(), indent=2)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)


if __name__ == "__main__":
    main()
