# Quantum Thermometry Locality

**How accurately can a thermometer learn a bath's initial temperature when all of its access is confined to one fixed region?** For a semi-infinite XX spin chain, this project establishes an attained precision law that charges the spatial contact and the time available for thermal information to reach it.

The bath is prepared once. Its known hopping scale is $`J`$, its known field may give a gapped or gapless spectrum, and its unknown inverse temperature lies in a fixed positive compact interval. The apparatus may use arbitrary finite quantum memory, entanglement, temperature-independent controls, adaptive measurements, and retained classical records. Every contact remains within the first $`r\ge1`$ bath sites, and the bath bonds outside that region retain their fixed strength.

On any fixed temperature interval, the optimal worst-case squared log-temperature error is

```math
\boxed{\qquad
\mathcal R(r,Jt/\hbar)=\Theta\!\left(\frac{1}{r+Jt/\hbar}\right).
\qquad}
```

The constants depend on the known field and temperature interval and are uniform over probe number, memory size, and the strength and speed of controls within the contacted region. The corresponding root-mean-square log-temperature error scales as $`(r+Jt/\hbar)^{-1/2}`$.

## How the budget changes at low temperature

For a fixed gapless field in the interior of the XX band, take the dimensionless inverse temperature $`b=J/(k_{\mathrm B}T)`$ in a known octave $`[B,2B]`$. As $`B`$ grows, the [uniform low-temperature theorem](science/low_temperature.md#uniform-minimax-law) gives

```math
\mathcal R_{[B,2B]}(r,\tau)
=\Theta_\nu\!\left(\min\left\{1,\frac{B}{r+\tau}\right\}\right),
\qquad \tau=Jt/\hbar.
```

At one fixed contact, a fixed relative precision takes time of order $`\hbar/(k_{\mathrm B}T)`$. The converse covers every allowed adaptive experiment. A finite auxiliary spin chain attains the rate by collecting energy-selective wave packets through that contact from the same bath preparation. The chain length grows with the allotted time.

## What establishes the law

| Result | Physical content | Authoritative account |
|---|---|---|
| Complete-output converse | Even the full adaptive record and final quantum memory cannot distinguish nearby temperatures faster than information propagates from the initially thermal bath. | [Locality and statistical distinguishability](science/locality_converse.md) |
| Attaining fixed-contact sensor | One detuned boundary spin with fixed exchange and counted vacuum reset reaches squared error of order $`(1+Jt/\hbar)^{-1}`$, without re-preparing the bath. | [Counted boundary sensor](science/counted_sensor.md) |
| Spatial access | An energy measurement of the initial contacted block gives squared error of order $`r^{-1}`$. Choosing the better spatial or temporal protocol attains the joint law. | [Construction and estimator](science/counted_sensor.md#5-spatial-access-and-the-joint-law) |
| Resource consequence | Increasing apparatus size alone cannot produce an unbounded precision gain at fixed contact and elapsed time in this microscopic model. | [Physical consequences](science/physical_consequences.md) |

The lower bound follows from locality of the entire controlled experiment, a relative-entropy estimate for actual restricted thermal states, and a two-temperature testing argument. It is a global risk statement and allows biased estimators. At zero field, particle–hole symmetry makes the undetuned sensor’s mean count independent of temperature. A fixed local detuning weights the two sides of the spectrum differently. The exact spin jump-count law and a uniformly monotone long-time mean then give a calibrated estimator from one bath preparation.

The mathematical ingredients have established precedents. The [related-work account](references/RELATED_WORK.md) distinguishes those ingredients from the matched local-access estimation problem and explains the relation to all-control Markov thermometry.

## Read the science

Start with the [model and exact statements](science/model_and_results.md). The [science guide](science/README.md) connects the converse, attaining apparatus, and physical interpretation. Each result has one authoritative proof page.

| Reader's question | Route |
|---|---|
| What is estimated, and which resources are available? | [Model and results](science/model_and_results.md) |
| How do the space and time budgets scale as the bath gets colder? | [Uniform low-temperature law](science/low_temperature.md) |
| Why do strong control and large quantum memory not enter the lower-bound constant? | [Boundary compression and locality](science/locality_converse.md) |
| Why does the count formula describe a spin detector? | [Exact counted-spin experiment](science/counted_sensor.md#2-the-actual-spin-count-has-a-determinant-law) |
| How does a detuned sensor acquire temperature information at zero field? | [Thermal response](science/counted_sensor.md#3-linear-extraction-from-the-initially-thermal-half-chain) |
| What does this imply for collective Markov models? | [Physical consequences](science/physical_consequences.md) |
| Which results are inherited, and what do the closest models assume? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| How are finite implementations checked? | [Verification](verification/README.md) |

[The LLM reading guide](llms.txt) maps scientific questions to these same authoritative files.

## Learn the project

The single educational anchor is **Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control* (Cambridge University Press, first edition, 2010)**. The [anchor bridge](learning/ANCHOR_BRIDGE.md) selects the relevant sections, translates the notation, and connects measurements, counting records and feedback to the microscopic thermometry problem.

The [30-milestone map](learning/MILESTONES.md) gives a common route through the project. Its 14 background milestones build the operational and mathematical foundations; its 16 narrative milestones connect the locality converse, attaining sensor and physical consequences. Each milestone states an understanding target, dependencies, conceptual connections and source pointers. The map is defined by the science and can be used alongside the bridge for self-directed study.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The checks compare the spin counting model with its one-particle formulas and test the reduced-state entropy estimates, packet transport, occupation slopes and count variance. The analytic proofs give the all-budget guarantees.

## Scope

Both theorems concern the initial temperature of a known, one-dimensional, finite-bandwidth bath with fixed spatial access. The initial apparatus is independent of the bath and of its temperature. The fixed-interval sensor uses an ideal counted vacuum reset channel. The low-temperature temporal receiver uses a finite vacuum lead and an ideal terminal mode readout.

The bath is infinite for the all-time attainment statements. A finite bath has a finite initial information supply. The uniform low-temperature law concerns a fixed interior gapless field. The band edges and attainment with a fixed-size detector are open in this limit.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
