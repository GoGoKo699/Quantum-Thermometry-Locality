# From measurement and control to local thermometry

A thermometer touches a sample, changes as a result of that interaction, and produces a reading. Repeating the readout, resetting the sensor, or attaching more sensors gives more opportunities to observe the sample. The question here is how much temperature information those operations can acquire when they all use the same small contact with one microscopic reservoir.

The reservoir is a chain of two-state spins, prepared thermally once. Its nearest-neighbor couplings transport excitations toward the contacted region. The project proves a limit for every permitted controller. On a fixed temperature interval, a block-energy measurement attains the spatial rate and a fixed boundary sensor attains the temporal rate. At zero bath field, the undetuned sensor's mean count is independent of temperature. A known shift of the sensor's own energy restores its response. A low-temperature law for an interior band crossing gives the dependence on temperature itself. Wiseman and Milburn supply the language of states, instruments, trajectories, and feedback used to describe the experiment.

## Anchor and route

The selected educational anchor is **Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control*, Cambridge University Press, first edition, first published 2010**, ISBN 9780521804424; [book DOI](https://doi.org/10.1017/CBO9780511813948). The publisher's [front matter](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf) identifies the edition, and its [contents](https://assets.cambridge.org/97805218/04424/toc/9780521804424_toc.pdf) verify the section numbers below. “WM” refers to this one book.

The [30-milestone map](MILESTONES.md) gives the complete understanding targets. This bridge connects them through the following parts of WM; the explanations and examples below supply the additional links.

| WM starting point | Connection developed here | Milestones |
| --- | --- | --- |
| Appendices A.1–A.2; §3.5 | States and occupations become a correlated thermal chain with restricted access. | [M01–M05](MILESTONES.md#m01-thermal-information-in-one-occupation) |
| §1.4; §§3.2, 3.6; §§4.2–4.3; §5.4 and Chapter 6 | Instruments and feedback become a complete record obtained from one initial bath. | [M06–M09](MILESTONES.md#m06-a-microscopic-bath-and-a-reduced-generator) |
| §§2.2, 2.7 and 3.11 | Estimation, discrimination, and observable evolution become a locality-based global converse. | [M10–M20](MILESTONES.md#m10-distinguishing-two-temperatures) |
| §§3.5, 4.2–4.3 | A physical loss record becomes a computable count law and a uniform estimator. | [M21–M26](MILESTONES.md#m21-build-the-fixed-counted-sensor) |
| §3.2; §5.4 and Chapter 6 | A controlled Markov experiment is compared with the microscopic resource limit. | [M27–M30](MILESTONES.md#m27-construct-the-collective-markov-comparison-record) |
| §§2.7, 3.5 and 3.11 | Discrimination, thermal occupations, and time evolution combine to give the low-temperature dependence. | [M19](MILESTONES.md#m19-bound-distinguishability-of-the-correlated-thermal-block), [M26](MILESTONES.md#m26-join-spatial-access-and-elapsed-time), [M30](MILESTONES.md#m30-synthesize-the-resource-law-and-its-physical-meaning) |

The canonical statements are in [Model and results](../science/model_and_results.md). The [converse](../science/locality_converse.md), [sensor construction](../science/counted_sensor.md), and [physical consequences](../science/physical_consequences.md) develop the fixed-interval result. The [low-temperature proof](../science/low_temperature.md#uniform-minimax-law) gives the uniform rate and the apparatus resources for attaining it.

## 1. Locate the parameter and the resources

**Connections:** [M01–M05](MILESTONES.md#m01-thermal-information-in-one-occupation), [M13–M14](MILESTONES.md#m13-global-error-and-the-choice-of-loss).

A spin has an empty state and an occupied state. Its occupation observable has possible readings zero and one. Exchange coupling moves an excitation between neighboring spins while preserving their total number. The known energy scale of that coupling is $`J`$.

For one isolated two-state system whose occupied state has energy $`JE`$ relative to the empty state, thermal preparation gives the occupied-state probability

```math
p_b=f_b(E)=\frac{1}{1+e^{bE}},
\qquad b=\frac{J}{k_BT}.
```

Here $`T`$ is absolute temperature and $`k_B`$ converts temperature to energy. For a positive gap, increasing $`b`$ means cooling the system and reducing its occupation. The same function determines the occupations of the chain's one-particle energy modes. A site and an energy mode are different: a mode can extend across many sites.

The following notation translates the book's general measurement-and-control setting into this particular experiment.

| Quantity | Meaning in this project |
| --- | --- |
| $`b=J/(k_BT)`$ | The unknown dimensionless inverse temperature. It labels the **initial bath state**. |
| $`\tau=Jt/\hbar`$ | The available physical time $`t`$ measured in units set by the bath coupling. |
| $`r`$ | The number of bath sites in the fixed contacted interval, sites $`1,\ldots,r`$. |
| Apparatus | Sensors, ancillary systems, control registers, detector, and retained memory. Their initial state is independent of $`b`$ and uncorrelated with the bath. |
| $`Y`$ | A complete classical record, potentially including outcomes and their times. Quantum memory may also be retained. |
| $`N_\tau`$ | The total detected loss count in the particular attaining experiment. It uses only part of the allowed output. |
| $`R`$ | A bath cutoff introduced in the converse. It is an analysis variable, not an enlargement of the permitted contact $`r`$. |

The chain's one-particle energies lie in $`[\nu-2,\nu+2]`$ in units of $`J`$. The field $`\nu`$ is fixed and known. If the band crosses zero, occupations at its positive and negative energies respond to cooling in opposite directions. At zero field, energies occur in particle–hole pairs. The fixed known interval $`I=[b_-,b_+]`$ with $`0\lt b_-\lt b_+\lt \infty`$ keeps all thermal occupations bounded away from zero and one. Every protocol has the hard elapsed-time budget $`\tau`$, including branches chosen adaptively from earlier outcomes.

The loss measures error in logarithmic temperature. A hat denotes a reported estimate:

```math
\begin{aligned}
\theta
&=\log\!\left(\frac{k_BT}{J}\right)=-\log b,\\
(\widehat\theta-\theta)^2
&=(\log\widehat b-\log b)^2\\
&=\left[\log\!\left(\frac{\widehat T}{T}\right)\right]^2.
\end{aligned}
```

It assigns the same loss to overestimating an absolute temperature by a factor of two and underestimating it by that factor. Estimates can be clipped to the known interval without worsening this loss. The global minimax risk $`\mathcal R(r,\tau)`$ first averages this loss over every possible record, takes the worst value over $`I`$, and then minimizes over allowed experiments and estimators. A biased estimator is allowed. A rare unfavorable record still contributes.

The result is

```math
\mathcal R(r,\tau)=\Theta\!\left(\frac{1}{r+\tau}\right).
```

This notation means that fixed positive multiples of $`1/(r+\tau)`$ bound the optimal risk from below and above. Those constants depend on the known band and interval. The **root** mean squared log-temperature error therefore has order $`(r+\tau)^{-1/2}`$.

## 2. Keep the measurement record when the sensor is reset

**Connections:** [M06–M09](MILESTONES.md#m06-a-microscopic-bath-and-a-reduced-generator), [M15](MILESTONES.md#m15-put-the-adaptive-experiment-into-one-boundary-vertex). WM §1.4, §§4.2–4.3, §5.4, and Chapter 6 provide the relevant framework.

A density operator $`\rho`$ describes a quantum state, including both probabilities and coherences. A measurement instrument specifies two things together: how likely each outcome is, and which state remains after that outcome. For an instrument branch $`\mathcal I_y`$,

```math
p(y)=\mathrm{tr}\,\mathcal I_y(\rho),
\qquad
\rho_y=\frac{\mathcal I_y(\rho)}{p(y)}
\quad\text{when }p(y)\gt 0.
```

The trace extracts the probability weight; division normalizes the conditional state. Averaging these conditional states while forgetting $`y`$ gives the unconditional state. Keeping $`y`$ in a register preserves information that this average can lose.

### Worked example: one thermal source, two readouts

Take a toy bath consisting of one isolated two-state system, occupied with probability $`p_b`$. Prepare an empty sensor. A known SWAP operation exchanges their states, so the bath becomes empty and the sensor acquires the bath's initial occupation. Measure that occupation and store the result $`Y_1`$. Reset the sensor to empty, perform the same SWAP again, and record $`Y_2`$.

The entire outcome law is

| Stored pair $`(Y_1,Y_2)`$ | Probability |
| --- | ---: |
| $`(0,0)`$ | $`1-p_b`$ |
| $`(1,0)`$ | $`p_b`$ |

After the first SWAP, the same toy bath is already empty. Resetting the sensor therefore does not provide a second thermal draw. At the end, the sensor is empty for every temperature, while the stored first outcome still has a temperature-dependent distribution.

This example identifies the output that a precision bound must cover. In the actual half-chain, transport from more distant sites can replenish the contacted region. The proof must determine how quickly that can happen, while retaining the effects of all earlier operations on the bath.

Feedback fits this accounting. A rule such as “apply operation $`A_y`$ after outcome $`y`$” is fixed before the unknown temperature is known. Its outcome probabilities depend on temperature because the input bath does; the rule itself remains parameter independent. Choosing a later operation using an estimate computed from the record is also permitted. Supplying a separate device whose initial state already depends on the true temperature would add another information source.

## 3. Replace a many-spin description by the correct covariance

**Connections:** [M03–M05](MILESTONES.md#m03-from-the-endpoint-spin-chain-to-thermal-modes), [M11](MILESTONES.md#m11-relative-entropy-and-information-in-a-finite-region), [M19](MILESTONES.md#m19-bound-distinguishability-of-the-correlated-thermal-block). WM §3.5 and Appendix A.2 are the starting points; the XX-chain reduction is supplied locally.

For this chain, the Jordan–Wigner transformation rewrites the spin-exchange Hamiltonian in terms of fermionic creation and annihilation operators. The one-particle Hamiltonian is

```math
\begin{aligned}
h_B&=\nu I-S-S^\dagger,\\
C_b&=f_b(h_B),\\
(C_b)_{jk}&=\langle c_k^\dagger c_j\rangle_b.
\end{aligned}
```

In these matrix formulas, $`I`$ denotes the identity operator; the parameter interval uses the same letter in expressions such as $`b\in I`$. The shift $`S`$ moves a one-particle amplitude by one site. The matrix $`C_b`$ records occupations on its diagonal and two-site coherences off the diagonal. It is the fermionic covariance used here, rather than a table of independent site probabilities.

The thermal state is Gaussian: higher correlations follow from this two-point matrix by Wick's rule. “Gaussian” describes this reconstruction property; it does not assert a bell-shaped distribution for the measured count. For example, distinct sites satisfy

```math
\langle n_jn_k\rangle_b
=(C_b)_{jj}(C_b)_{kk}-|(C_b)_{jk}|^2,
\qquad j\ne k.
```

Nonzero coherences therefore create correlations between site occupations. Diagonalizing a covariance identifies independent **natural occupation modes**, which generally differ from the spatial sites.

When only the first $`R`$ spins are retained, the actual reduced state has covariance

```math
C_{b,R}=P_R f_b(h_B)P_R.
```

Here $`P_R`$ projects onto those one-particle sites. Taking a partial trace means retaining the statistics of all measurements on this block and ignoring the rest. It preserves the consequences of the original coupling to the surrounding bath. Consequently, applying the thermal function after cutting the Hamiltonian generally gives a different matrix:

```math
P_R f_b(h_B)P_R
\ne f_b(P_Rh_BP_R).
```

The right side describes a different preparation: an isolated block thermalized on its own. The distinction is essential when the converse later deletes a bond in the dynamics.

Gaussian reconstruction is an established method; see [Peschel](https://doi.org/10.1088/0305-4470/36/14/101). The project's [relative-entropy calculation](../science/locality_converse.md#gaussian-logarithms-and-relative-entropy) supplies the additional matrix estimate needed here. In particular, covariances compressed at different temperatures need not commute. Their information cannot be calculated by assuming a common independent-site basis.

## 4. From state discrimination to a bound on every controller

**Connections:** [M10–M14](MILESTONES.md#m10-distinguishing-two-temperatures), [M15–M20](MILESTONES.md#m15-put-the-adaptive-experiment-into-one-boundary-vertex). WM §2.7 supplies the decision perspective, §2.2 provides the local-estimation comparison, and §3.11 supplies observable evolution.

Suppose an experiment must distinguish two possible inverse temperatures $`b_0`$ and $`b_1`$. Trace distance between its two possible quantum outputs is the largest difference in probability of a binary measurement event. Once the outputs are classical records, the same quantity is total variation distance. Processing both outputs by the same parameter-independent channel cannot increase this distinguishability.

This principle turns a statement about the initially accessible bath into a statement about any sensor and controller. Three additional steps make it work for a time-dependent experiment.

### First, isolate the fixed outgoing bath bond

Retain every measurement register and the environments used to implement resets. A measurement with feedback can then be represented by a larger unitary experiment followed by readout. Group this enlarged apparatus and the first $`r`$ bath spins into one boundary vertex.

A change of dynamical picture removes all operations internal to that vertex. The outgoing bath bond is only conjugated by local unitaries: its norm remains the fixed exchange norm. Large apparatus dimension, strong internal control, and many stored outcomes do not strengthen that bond.

The remaining chain admits a Lieb–Robinson estimate. An observable at the boundary can become sensitive to a distant site only through a sequence of overlapping local interactions. Bounded interaction norms control the sum of these paths. The result has exponentially small tails outside an effective influence region; it is not a strictly sharp causal boundary. The [path argument](../science/locality_converse.md#a-dimension-independent-path-estimate) specializes the framework of [Barthel and Kliesch](https://doi.org/10.1103/PhysRevLett.108.230504) and tracks the absence of apparatus-dimension factors.

### Next, identify the finite initial input

Delete a sufficiently distant bond after bath site $`R`$, keeping the original initial state and all controller operations unchanged. With $`R`$ of order $`r+\tau`$, this changes the **complete accessible output** by at most a chosen small constant in trace distance.

In the cut experiment, the distant tail has no further interaction with the accessible region. Tracing it out leaves a parameter-independent channel $`\Lambda_R`$ acting on the actual initial marginal:

```math
\sigma_{b,R}=\Lambda_R(\rho_{b,R}).
```

The initial correlations across the cut were never removed or replaced. This is precisely why the covariance in the preceding section must be $`P_Rf_b(h_B)P_R`$. The [complete-output truncation](../science/locality_converse.md#truncating-the-complete-output) controls every final joint measurement of the sensor, memories, and accumulated record.

### Finally, turn finite-region information into estimation error

Relative entropy compares the whole thermal states. The Gaussian calculation and the fixed spectral floor give

```math
D(\rho_{b,R}\Vert\rho_{b',R})
\le K R(b-b')^2,
```

where $`K`$ depends only on the known band and parameter interval. The estimate retains correlations. Its factor $`R`$ comes from a bound on the matrix covariance variation, not from assuming $`R`$ independent site measurements.

Pinsker's inequality converts this relative-entropy bound into a trace-distance bound. Choose two parameters separated by a sufficiently small constant times $`R^{-1/2}`$. Their initial marginals remain hard to distinguish; data processing and the two truncation errors preserve a nonzero testing error for every controller.

Any numerical estimate also defines a test: choose whichever of $`b_0,b_1`$ is nearer. If this decision is wrong, the estimation error is at least half their separation. A testing error bounded away from zero therefore forces mean squared error of order $`1/R`$, hence $`1/(r+\tau)`$. On the fixed interval, errors in $`b`$ and in $`\log b`$ differ only by bounded factors.

This is the bridge from WM's discrimination framework to the project's global converse. The [two-point proof](../science/locality_converse.md#global-minimax-reduction) works for biased estimators and all records. It needs only a constant truncation accuracy; it never differentiates the small error of an approximate channel to infer a Fisher-information bound.

## 5. From a quantum jump record to an attaining thermometer

**Connections:** [M21–M25](MILESTONES.md#m21-build-the-fixed-counted-sensor). WM §§4.2–4.3 explain conditioned detection records, and §3.5 supplies reservoir background. The project relates the physical count law to the spectral response and uses it for global estimation.

Attach one initially empty sensor at site zero using the chain's exchange coupling $`J`$. Its on-site energy is $`J(\nu+d)`$, where the fixed, known detuning $`d`$ is positive for $`\nu\ge 0`$ and negative for $`\nu\lt 0`$. Count its loss events through the known jump operator

```math
\ell=\sqrt{\kappa}\,\sigma_0^-,
\qquad \kappa=\frac12.
```

The rate is measured in units of $`J/\hbar`$, so the physical loss rate is $`J/(2\hbar)`$. Conditional on the existing record, an event in a small interval $`d\tau`$ has probability

```math
\Pr(dN_\tau=1\mid\text{record})
=\kappa\,\langle n_0\rangle_{\rm cond}\,d\tau
+o(d\tau).
```

A jump removes a sensor excitation and changes the conditional state. The record includes both the events and the waiting periods. Averaging over records produces the unconditional evolution used in part of the calculation.

There are two different environments in this description. The **thermal chain** remains explicit in the microscopic dynamics. The **known vacuum detector** provides a temperature-independent reset instrument, idealized as continuously monitored loss. Its fresh vacuum ancillary inputs contain no information about the unknown bath temperature. This ideal detector model is an allowed apparatus resource; it does not assume a temperature-dependent Markov generator for the thermal chain.

### From the spin instrument to counting statistics

Endpoint ordering makes the physical spin loss exactly $`\sigma_0^-=c_0`$, with no Jordan–Wigner string. The unconditional Gaussian covariance can therefore be propagated with a one-particle contraction:

```math
\begin{aligned}
K_\tau&=e^{(-ih-\kappa P_0/2)\tau},\\
M_\tau&=P_B(I-K_\tau^\dagger K_\tau)P_B.
\end{aligned}
```

Here $`h`$ is the sensor-plus-chain one-particle Hamiltonian, $`P_0`$ selects the sensor, and $`P_B`$ selects the initial bath modes. The last expression is restricted to the bath one-particle space. The positive matrix $`M_\tau`$ measures how much of each initial bath amplitude can be lost by time $`\tau`$. It is independent of $`b`$.

Each physical spin jump lowers the total excitation number by one. A generating function packages count probabilities as $`G(z)=\sum_n\Pr(N_\tau=n)z^n`$; $`z`$ is a bookkeeping variable. Combining excitation accounting with Gaussian trace formulas gives

```math
\begin{aligned}
Q_\tau(b)&=C_b^{1/2}M_\tau C_b^{1/2},\\
\mathbb E_b z^{N_\tau}
&=\det[I+(z-1)Q_\tau(b)]\\
&=\prod_j(1-q_j+q_jz).
\end{aligned}
```

The $`q_j`$ are eigenvalues of $`Q_\tau(b)`$, between zero and one. A Bernoulli variable is zero with probability $`1-q_j`$ and one with probability $`q_j`$; its generating function is exactly the corresponding factor. Multiplying the factors gives the distribution of their independent sum. Thus the count has an independent occupation-mode representation while the actual jump times can remain correlated. The detector's emitted quanta need no assigned fermionic statistics: the identity follows from the spin instrument and excitation accounting.

The trace-to-determinant method and generalized-binomial structure are inherited from [Klich](https://doi.org/10.1007/978-94-010-0089-5_19) and [Abanov–Ivanov](https://doi.org/10.1103/PhysRevB.79.205315). The [sensor proof](../science/counted_sensor.md#2-the-actual-spin-count-has-a-determinant-law) supplies the connection to this particular physical record. It also treats Gaussian evolution in the even sector, without an assumption about the evolution of odd fermionic operators.

Two consequences of the count law are enough for estimation:

```math
\begin{aligned}
\mu_\tau(b)
&=\mathbb E_bN_\tau
=\mathrm{Tr}(C_bM_\tau),\\
\mathrm{Var}_b(N_\tau)
&=\sum_jq_j(1-q_j)
\le\mu_\tau(b)\le \kappa\tau.
\end{aligned}
```

For every fixed time the loss operator has finite trace, which makes the infinite-mode determinant and count moments well defined. The [finite-volume limit](../science/counted_sensor.md#infinite-volume-count-and-moments) connects them to actual finite spin instruments. A fixed finite chain eventually exhausts its supply.

### Make the count sensitive to temperature

At $`\nu=0`$, consider energies $`E`$ and $`-E`$. Their total occupation is $`f_b(E)+f_b(-E)=1`$ at every temperature. The undetuned sensor weights the two signs equally, and the temperature derivatives cancel in the total mean at every time. This statement concerns the mean count. The other count statistics and the event times are separate observables.

For the detuned sensor, the long-time count susceptibility is a spectral average. Each energy contributes $`g_b(E)=E f_b(E)[1-f_b(E)]`$ to the negative derivative of the occupation, with a detector weight determined by the boundary dynamics. With positive detuning at zero field, the larger weight at $`E\gt0`$ leaves a positive contribution after pairing it with $`-E`$. The same sign choice works when the band shifts to a nonnegative field. Reversing the sign of both the field and the detuning reverses the slope. The [spectral proof](../science/counted_sensor.md#3-linear-extraction-from-the-initially-thermal-half-chain) derives the weight from the damped boundary return, then uses the fixed temperature interval to bound the susceptibility away from zero uniformly. Thus at sufficiently long times the mean has a fixed direction of change and $`|\mu_\tau'(b)|\ge m\tau`$ for some $`m\gt0`$ independent of $`b`$.

### Invert a mean, with every outcome included

At sufficiently long times, the estimator clips the observed count into the calibrated mean range and inverts the mean function. For a decreasing mean with range from 4 to 10, a recorded count of 12 would be clipped to 10 and assigned to the warm endpoint $`b_-`$. A count of 2 would be clipped to 4 and assigned to the cold endpoint $`b_+`$. The assignments reverse for an increasing mean. These fluctuations contribute to the risk.

Clipping cannot increase distance from the true mean. The uniform slope then converts count fluctuations into parameter error:

```math
\mathbb E_b(\widehat b-b)^2
\le\frac{\mathrm{Var}_b(N_\tau)}
{m^2\tau^2}
\le\frac{\kappa}{m^2\tau}.
```

A midpoint estimate covers short times, and the fixed interval converts the result to log-temperature loss. The [global estimator proof](../science/counted_sensor.md#4-a-global-estimator-including-biased-outcomes) uses the variance and the mean slope directly, so correlated fluctuations in the record are included.

## 6. Join the two resources and interpret the Markov comparison

**Connections:** [M26–M30](MILESTONES.md#m26-join-spatial-access-and-elapsed-time).

Direct access to $`r`$ initial bath sites provides a second attaining experiment. Measure the block Hamiltonian, which includes on-site energies and the exchange terms inside the block. Weighting occupations by energy changes the paired derivative to $`E^2 f_b(E)[1-f_b(E)]`$ in the bulk trace, so both energy signs add. The [block proof](../science/counted_sensor.md#5-spatial-access-and-the-joint-law) accounts for the bond leaving the block and uses the actual reduced thermal state. The variance is at most a constant times $`r`$ and the slope magnitude is at least a positive multiple of $`r`$ at sufficiently large $`r`$. Inversion gives risk of order $`1/r`$, with a midpoint estimate for small blocks.

Choose this initial-block experiment when $`r\ge\tau`$ and the counted sensor when $`\tau\gt r`$. The larger of $`r`$ and $`\tau`$ is at least $`(r+\tau)/2`$. This gives the matching upper bound without combining two potentially correlated data streams. The ideal instantaneous block access, including at zero elapsed time, is part of the [operational model](../science/model_and_results.md#operational-resources).

WM's distinction between a microscopic derivation and a reduced master equation matters again for the [collective Markov comparison](../science/physical_consequences.md#a-collective-markov-experiment). A Lindblad generator defines legitimate state evolution, but its form alone does not guarantee approximation accuracy for every microscopic coupling and controller.

In the reference Markov model, choose a positive probe spacing in the interior of the bath band. An even number $`N`$ of probe spins can be prepared in a central collective state, measured frequently, and restored after detected population changes. The preparation-and-measurement mechanism is due to [Sekatski and Perarnau-Llobet, §4.2](https://arxiv.org/html/2107.04425v2). For the chain's formal weak-coupling rates, the total event rate $`\Lambda_N`$ grows as $`N(N+2)`$ and the event directions retain temperature information. That controlled record has global risk of order $`(1+\Lambda_N\tau)^{-1}`$.

The microscopic one-contact theorem remains uniform in probe number and control strength. At fixed time, it supplies a pair of temperatures whose complete microscopic outputs remain imperfectly distinguishable. If the formal Markov rate $`\Lambda_N`$ grows without bound, its records distinguish that same pair with error tending to zero. The triangle inequality forces a nonvanishing difference between the two models' predicted records for at least one temperature.

The compared records can be obtained by probe measurements; no free access to bath jumps is added. The same rapid measurements retain their actual microscopic backaction and may cause Zeno suppression. The conclusion concerns uniform accuracy over controlled experiments. It neither computes an uncontrolled probe's error nor establishes a sharp crossover or validity below one. The [operational comparison](../science/physical_consequences.md#an-operational-obstruction-to-uniform-markov-accuracy) gives the precise statement.

The matched theorem therefore concerns acquiring **initially encoded** information. Locality limits the initial thermal region that can influence the complete output; the covariance estimate limits that region's distinguishability; the counted sensor and initial block measurement attain the resulting order. Arbitrary apparatus at a fixed contact can improve constants or implementation while leaving these charged resources unchanged.

The minimax law uses an XX half-chain with a fixed known field, fixed compact temperature interval, one initial thermal preparation, fixed contacted sites, and unchanged outgoing bath bonds. The counted construction uses ideal efficient monitoring. Moving contacts, additional temperature-bearing inputs, unbounded local bosonic systems, and detector imperfections raise separate questions. The next section gives the low-temperature result for an interior band crossing. The analytic proofs establish the scaling, and finite checks test the count law and spectral response. [Verification](../verification/README.md) · [Scope and attribution](../references/RELATED_WORK.md#mathematical-and-physical-contribution)

## 7. Resolve the thermal energy window

**Connections.** [M05](MILESTONES.md#m05-energy-signs-and-a-fixed-temperature-interval), [M19–M20](MILESTONES.md#m19-bound-distinguishability-of-the-correlated-thermal-block), [M25–M26](MILESTONES.md#m25-estimate-temperature-from-every-possible-count), [M29–M30](MILESTONES.md#m29-delimit-the-claim-and-account-for-its-ingredients).

Now let the known interval be $`b\in[B,2B]`$ and let $`B`$ grow, with the field fixed at $`|\nu|\lt 2`$. The one-particle band crosses zero with nonzero group velocity. For an energy near $`1/B`$, changing the temperature by a fixed factor changes its Fermi occupation by a constant amount. In particular, the magnitude of the derivative with respect to $`\log b`$ is $`bE f_b(E)[1-f_b(E)]`$ at positive energy $`E`$. It stays bounded below on the interval $`E\in[1/(2B),3/(2B)]`$. Well outside an energy window of order $`1/B`$ around zero, the occupations respond much less.

### Count the available information

The fixed-interval entropy estimate uses a spectral floor that decreases with $`B`$. The [uniform converse](../science/low_temperature.md#converse) first expresses the compressed covariances as averages over a common positive operator-valued spectral measure. Joint convexity bounds the block's relative entropy by the integral of classical Bernoulli divergences against that measure's trace. At large $`B`$, the integral is concentrated near zero energy, where the density of states is bounded. The resulting factor is $`R/B`$, so the two temperatures in the testing reduction are separated in $`\log b`$ by a small multiple of $`\min\{1,\sqrt{B/R}\}`$. Locality still gives $`R=O(r+\tau)`$.

### Resolve and read out the occupied modes

A packet of length proportional to $`B`$ can resolve the positive thermal energy band. With initial block access, measure the occupations of disjoint packets in the contacted spins. For time access, attach a finite, initially empty XX lead at one bath site. The packet calculation traces each selected lead mode backward into the initially thermal bath. Its carrier has nonzero velocity, so the usable lead interval grows linearly in $`\tau`$. The coherent lead uses order $`\tau`$ ancillary spins, and the bath is prepared once.

Each mode contributes a slope bounded below by a positive constant to the mean total count as a function of log temperature. Gaussian occupation statistics bound the variance by the number of measured modes, even when their outcomes are correlated. The same clipping-and-inversion idea from Section 5 bounds squared error by a constant times $`1/M`$ for $`M`$ such modes. Choosing the spatial or temporal measurement gives the [matching receiver](../science/low_temperature.md#attaining-receiver).

The uniform law is $`\Theta_\nu(\min\{1,B/(r+\tau)\})`$. At a fixed contact, reaching a fixed small relative error takes time of order $`\hbar/(k_BT)`$. This extension assumes an interior band crossing and a known temperature interval within a factor of two. A matching construction with a fixed-size detector remains open. [Full theorem](../science/low_temperature.md#uniform-minimax-law) · [Finite checks](../verification/README.md)
