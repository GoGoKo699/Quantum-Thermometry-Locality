# Quantum Thermometry Locality

**How accurately can a thermometer learn a bath's initial temperature when all of its access is confined to one fixed region?** For a semi-infinite XX spin chain, this project establishes an attained precision law that charges the spatial contact and the time available for thermal information to reach it.

The bath is prepared once. Its known hopping scale is $`J`$, its known one-particle band is strictly positive, and its unknown inverse temperature lies in a fixed positive compact interval. The apparatus may use arbitrary finite quantum memory, entanglement, temperature-independent controls, adaptive measurements, and retained classical records. Every contact remains within the first $`r\ge1`$ bath sites, and the bath bonds outside that region retain their fixed strength.

The optimal worst-case squared log-temperature error is

```math
\boxed{\qquad
\mathcal R(r,Jt/\hbar)=\Theta\!\left(\frac{1}{r+Jt/\hbar}\right).
\qquad}
```

The constants depend on the fixed band position and temperature interval, but not on the number of probes, the size of the memory, or the strength and speed of controls within the contacted region. The corresponding root-mean-square log-temperature error scales as $`(r+Jt/\hbar)^{-1/2}`$.

## What establishes the law

| Result | Physical content | Authoritative account |
|---|---|---|
| Complete-output converse | Even the full adaptive record and final quantum memory cannot distinguish nearby temperatures faster than information propagates from the initially thermal bath. | [Locality and statistical distinguishability](science/locality_converse.md) |
| Attaining fixed-contact sensor | One boundary spin with fixed exchange and counted vacuum reset reaches squared error of order $`(1+Jt/\hbar)^{-1}`$, without re-preparing the bath. | [Counted boundary sensor](science/counted_sensor.md) |
| Spatial access | An occupation measurement of the initial contacted block gives squared error of order $`r^{-1}`$. Choosing the better spatial or temporal protocol attains the joint law. | [Construction and estimator](science/counted_sensor.md#5-spatial-access-and-the-joint-law) |
| Resource consequence | Increasing apparatus size alone cannot produce an unbounded precision gain at fixed contact and elapsed time in this microscopic model. | [Physical consequences](science/physical_consequences.md) |

The lower bound follows from locality of the entire controlled experiment, a relative-entropy estimate for actual restricted thermal states, and a two-temperature testing argument. It is a global risk statement and allows biased estimators. The upper bound uses the exact spin jump-count distribution, a positive long-time extraction rate, and inversion of a uniformly monotone calibrated mean.

The mathematical ingredients have established precedents. The [related-work account](references/RELATED_WORK.md) distinguishes those ingredients from the matched local-access estimation problem and explains the relation to all-control Markov thermometry.

## Read the science

Start with the [model and exact statements](science/model_and_results.md). The [science guide](science/README.md) connects the converse, attaining apparatus, and physical interpretation. Each result has one authoritative proof page.

| Reader's question | Route |
|---|---|
| What is estimated, and which resources are available? | [Model and results](science/model_and_results.md) |
| Why do strong control and large quantum memory not enter the lower-bound constant? | [Boundary compression and locality](science/locality_converse.md) |
| Why does the count formula describe a spin detector? | [Exact counted-spin experiment](science/counted_sensor.md#2-the-actual-spin-count-has-a-determinant-law) |
| How can one sensor keep learning without resetting the bath? | [Linear extraction](science/counted_sensor.md#3-linear-extraction-from-the-initially-thermal-half-chain) |
| What does this imply for collective Markov models? | [Physical consequences](science/physical_consequences.md) |
| Which results are inherited, and what do the closest models assume? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| How are finite implementations checked? | [Verification](verification/README.md) |

[The LLM reading guide](llms.txt) maps scientific questions to these same authoritative files.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The checks compare a direct number-resolved spin evolution with the one-particle counting determinant, examine finite-chain extraction before boundary reflections, and verify the restricted-state relative-entropy calculation. They test implementations and finite examples. The universal converse and infinite-time attainment follow from the written proofs.

## Scope

The theorem concerns the initial temperature of a known, one-dimensional, finite-bandwidth bath with fixed spatial access. The initial apparatus is independent of the bath and of its temperature. The attaining apparatus uses an ideal counted, temperature-independent vacuum reset channel. Temperature-dependent external actuators, fresh thermal samples, moving contact, and an unknown parameter acting throughout an external Hamiltonian change the estimation model.

The bath is infinite for the all-time attainment statement. A finite bath has a finite initial information supply. The constants are not uniform as the positive band gap closes, the temperature interval reaches zero temperature, or the interval becomes unbounded. This result does not assert a pointwise quantum Fisher information bound.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
