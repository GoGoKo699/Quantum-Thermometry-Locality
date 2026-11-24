#!/usr/bin/env python3
"""Check finite low-temperature packets and the spectral entropy bound."""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.fft import dst
from scipy.special import expit

from check_relative_entropy import fock_state, relative_entropy


def chain_energies(sites: int, field: float) -> np.ndarray:
    momenta = np.pi * np.arange(1, sites + 1) / (sites + 1)
    return field - 2 * np.cos(momenta)


def packets(sites: int, starts: np.ndarray, width: int, carrier: float) -> np.ndarray:
    offsets = np.arange(width)
    envelope = np.sqrt(2 / (width + 1)) * np.sin(np.pi * (offsets + 1) / (width + 1))
    states = np.zeros((len(starts), sites), dtype=complex)
    states[np.arange(len(starts))[:, None], starts[:, None] + offsets] = (
        envelope * np.exp(1j * carrier * offsets)
    )
    return states


def packet_measurements(spectral: np.ndarray, energies: np.ndarray, base: int) -> dict:
    size = len(spectral)
    weights = np.abs(spectral) ** 2
    band = (energies >= 0.5 / base) & (energies <= 1.5 / base)
    band_mass = weights[:, band].sum(axis=1)
    assert np.min(band_mass) > 0.75
    slopes, variances = [], []
    for b in np.geomspace(base, 2 * base, 5):
        occupations = expit(-b * energies)
        slope = weights @ (b * energies * occupations * expit(b * energies))
        assert np.min(slope) > 0.15

        step = 1e-5
        colder = weights @ expit(-b * np.exp(step) * energies)
        warmer = weights @ expit(-b * np.exp(-step) * energies)
        np.testing.assert_allclose(slope, (warmer - colder) / (2 * step), atol=1e-9)

        covariance = (spectral * occupations) @ spectral.conj().T
        eigenvalues = np.linalg.eigvalsh(covariance)
        assert np.min(eigenvalues) >= -1e-12 and np.max(eigenvalues) <= 1 + 1e-12
        distribution = np.ones(1)
        for occupation in eigenvalues:
            distribution = np.convolve(distribution, [1 - occupation, occupation])
        count = np.arange(size + 1)
        mean = float(distribution @ count)
        variance = float(distribution @ (count - mean) ** 2)
        np.testing.assert_allclose(distribution.sum(), 1, atol=1e-12)
        np.testing.assert_allclose(mean, np.trace(covariance).real, atol=1e-12)
        np.testing.assert_allclose(
            variance, np.trace(covariance - covariance @ covariance).real, atol=1e-12
        )
        assert variance <= size / 4 + 1e-12
        slopes.append(float(np.min(slope)))
        variances.append(variance / size)
    return {
        "packets": size,
        "minimum_band_weight": float(np.min(band_mass)),
        "minimum_negative_log_b_slope": min(slopes),
        "maximum_count_variance_per_packet": max(variances),
    }


def packet_case(field: float, base: int) -> dict:
    width = 16 * base
    time = 14 * width
    lead_sites = bath_sites = 4 * time
    carrier = -np.arccos((field - 1 / base) / 2)
    velocity = 2 * np.sin(carrier)
    start, stop = int(velocity * time / 2), int(velocity * time / 4)
    starts = np.arange(start, stop - width + 1, width)
    assert len(starts) >= 2

    # The same open-chain transform first evolves the finite combined chain and
    # then resolves the initial finite bath's energies in its own mode basis.
    output = packets(lead_sites + bath_sites, lead_sites + starts, width, carrier)
    np.testing.assert_allclose(output @ output.conj().T, np.eye(len(starts)), atol=1e-12)
    phase = np.exp(1j * time * chain_energies(lead_sites + bath_sites, field))
    backward = dst(dst(output, type=1, norm="ortho") * phase, type=1, norm="ortho")
    initial_bath = backward[:, lead_sites:]
    bath_weight = np.sum(np.abs(initial_bath) ** 2, axis=1)
    assert np.min(bath_weight) > 0.99
    bath_energies = chain_energies(bath_sites, field)
    temporal = packet_measurements(dst(initial_bath, type=1, norm="ortho"), bath_energies, base)
    spatial = packets(bath_sites, np.arange(len(starts)) * width, width, carrier)
    spatial = packet_measurements(dst(spatial, type=1, norm="ortho"), bath_energies, base)
    return {
        "field": field,
        "inverse_temperature_band": [base, 2 * base],
        "packet_width": width,
        "elapsed_time": time,
        "lead_sites": lead_sites,
        "bath_sites": bath_sites,
        "minimum_temporal_bath_weight": float(np.min(bath_weight)),
        "spatial": spatial,
        "temporal": temporal,
    }


def entropy_case(field: float, base: int, retained_sites: int) -> dict:
    sites = 49
    energies = chain_energies(sites, field)
    momenta = np.pi * np.arange(1, sites + 1) / (sites + 1)
    modes = np.sqrt(2 / (sites + 1)) * np.sin(
        np.outer(np.arange(1, retained_sites + 1), momenta)
    )
    # Independently reconstruct both reduced many-body states. The spectral
    # upper bound uses only the one-mode binary relative entropies and weights.
    logits, other_logits = -base * energies, -1.7 * base * energies
    occupations, other_occupations = expit(logits), expit(other_logits)
    c = (modes * occupations) @ modes.T
    d = (modes * other_occupations) @ modes.T
    commutator = float(np.linalg.norm(c @ d - d @ c, "fro"))
    binary_entropy = (
        occupations * (logits - other_logits)
        + np.logaddexp(0, other_logits) - np.logaddexp(0, logits)
    )
    bound = float(np.sum(modes**2, axis=0) @ binary_entropy)
    actual = relative_entropy(fock_state(c), fock_state(d))
    assert commutator > 1e-6
    assert 0 < actual <= bound + 1e-12
    return {
        "field": field,
        "inverse_temperatures": [base, 1.7 * base],
        "full_chain_sites": sites,
        "retained_sites": retained_sites,
        "covariance_commutator_frobenius": commutator,
        "fock_relative_entropy": actual,
        "spectral_bernoulli_bound": bound,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also save the JSON report.")
    arguments = parser.parse_args()
    report = {
        "check": "low_temperature_packets_and_entropy",
        "status": "passed",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "scope": "Four finite receiver instances and three finite entropy comparisons.",
        "packet_cases": [packet_case(field, base) for field, base in (
            (0.0, 4), (0.8, 8), (-1.0, 12), (1.6, 12)
        )],
        "entropy_cases": [entropy_case(field, base, retained) for field, base, retained in (
            (0.0, 4, 3), (0.7, 8, 4), (-1.0, 12, 4)
        )],
    }
    encoded = json.dumps(report, indent=2)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)


if __name__ == "__main__":
    main()
