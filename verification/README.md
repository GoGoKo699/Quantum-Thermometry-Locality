# Verification

The analytical theorem combines an all-control locality converse with an infinite-chain attaining construction. The programs here check finite implementations of its thermal-state, counting, and extraction ingredients through independent calculations. They use deterministic matrix evolution, not Monte Carlo sampling.

## Run the checks

The reference outputs were produced with Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

Expected summary:

```text
PASS: restricted_gaussian_relative_entropy
PASS: independent_number_resolved_spin_counting
PASS: finite_chain_extraction_and_global_estimator
PASS: detuned_boundary_count_response
PASS: low_temperature_packets_and_entropy
All finite checks passed. Analytical and infinite-volume claims require the written proofs.
```

The programs require no network access. To retain fresh reports in a separate directory:

```bash
python3 verification/run_all.py --output-dir /tmp/thermometry-checks
```

Each check can also run separately, with an optional `--output PATH` argument. The runner leaves the committed reference reports unchanged unless an output directory is explicitly supplied. Floating-point residuals can vary with BLAS and platform; the programs use numerical tolerances rather than byte-for-byte output comparisons. Setting `OPENBLAS_NUM_THREADS=1` can reduce overhead on machines with many cores.

## What is checked

| Program | Independent calculations | Scientific issue tested |
|---|---|---|
| [check_relative_entropy.py](check_relative_entropy.py) | Full Fock-space density matrices versus one-particle covariance logarithms for nine pairs of restricted thermal states. | The relative-entropy formula remains correct when compressed covariances do not commute. The actual restricted state differs from the Gibbs state of a cut Hamiltonian. |
| [check_counting.py](check_counting.py) | A number-resolved Lindblad equation built from physical spin matrices and the many-body Gibbs state versus the Gaussian determinant prediction. | The complete probability law, mean, variance and excitation balance describe the physical counted spin-reset instrument, including with sensor detuning. |
| [check_extraction.py](check_extraction.py) | Dense loss matrices versus independently propagated boundary vectors and integrated detector current at two bath lengths, with exact finite count distributions and clipped estimators. | For the matched sensor in a positive band, checks the extraction and variance inequalities, thermal response, estimator bounds and onset of finite-volume exhaustion. |
| [check_detuned_response.py](check_detuned_response.py) | Finite-chain susceptibility from sparse adjoint propagation versus quadrature of the half-chain spectral weight. | Tests cancellation in the undetuned half-filled count mean, its restoration by detuning, and the sign response across fields and reset rates. |
| [check_low_temperature.py](check_low_temperature.py) | Exact finite-chain propagation, bath-mode occupations, finite-difference response, and total count moments. Direct reduced Fock-state entropy versus the spectral Bernoulli bound. | Tests energy selection, transport into one vacuum lead, monotone packet occupations, correlated count variance, and the compression bound for noncommuting covariances. |

The entropy cases restrict a 19-site one-particle thermal covariance to two, three and four sites, then reconstruct and compare the full 4-, 8- and 16-dimensional density matrices. The test explicitly records nonzero covariance commutators and the difference from rethermalizing an isolated block.

The counting cases use one to four bath spins and cover zero time, short exposure, and interacting evolution. They include detuning at half filling and on both sides of that field. Excitation conservation makes counts from zero through the bath length the exact support. The dynamical side evolves the full spin density matrices.

The extraction cases compare baths of 48 and 80 sites through dimensionless time 12, well before appreciable reflection in these instances. A separate three-site bath at time 200 saturates near three extracted one-particle modes. This demonstrates the failure of extending the half-chain's indefinite linear lower bound to a fixed finite bath. The reported finite estimator diagnostics distinguish the inverse-count estimator from the midpoint/count choice used by the uniform theorem.

The detuned response calculation uses one vacuum sensor and a bath of 245 sites at dimensionless time 80. It checks four inverse temperatures at half filling, on both sides of half filling, and at the two band-touching fields. It also tests two positive reset rates at half filling. The comparison measures the finite-time response per unit time against the analytical long-time coefficient.

The low-temperature calculation tests both receivers at four field and temperature-band pairs. It uses disjoint packets of widths 64 to 192 sites, with between four and six packets in each receiver. The smallest transported bath weight was 0.99997 and the smallest selected-band weight exceeded 0.82. At the sampled inverse temperatures each packet's negative log-inverse-temperature derivative exceeded 0.18, and the largest count variance per packet was below 0.20. Three independent Fock-state calculations check the spectral bound with nonzero covariance commutators. The [uniform law and its proofs](../science/low_temperature.md) give the continuous parameter and asymptotic guarantees.

## Reference results

The committed [entropy](results/relative_entropy.json), [counting](results/counting.json), [extraction](results/extraction.json) and [detuned response](results/detuned_response.json) reports record the parameters, software versions and residuals. In the reference runs:

- The full density-matrix relative entropy and covariance formula agreed within $`1.2\times10^{-15}`$.
- The physical spin and determinant count probabilities agreed within $`7\times10^{-16}`$.
- The two finite-chain extraction traces agreed within $`1.5\times10^{-13}`$ at the tested times.
- The count mean and integrated detector current agreed within $`2\times10^{-11}`$.
- The undetuned half-filled slope per unit time was below $`6\times10^{-18}`$ in magnitude. The tested detuned slopes agreed with the spectral formula to within 1.8% relative error.

These values describe the recorded run; the acceptance tolerances in the scripts are larger to accommodate floating-point variation.

## Analytical scope

Finite calculations cannot establish the universal quantifiers over controllers, arbitrarily large apparatus, continuous records, or infinite elapsed time. Those statements rely on the [locality proof](../science/locality_converse.md), the noncommuting matrix-entropy estimate on that page, and the [trace-class limit and boundary-resolvent argument](../science/counted_sensor.md).

The global minimax proof uses two-point distinguishability and a clipped inverse estimator. The verification does not infer this result from a local Fisher information or from a fit to numerical scaling. The collective Markov comparison is an analytical comparison of complete controlled records, with its own approximation caveats in [physical consequences](../science/physical_consequences.md).

## Hosted mathematical display

The separate [hosted Markdown check](hosted/README.md) compares the actual GitHub mathematics against exact commit-pinned source at wide and narrow viewport widths. It records screenshots and structural evidence for visual review. The workflow has read-only repository permissions. Its success concerns the observed rendering and is independent of the scientific checks above.
