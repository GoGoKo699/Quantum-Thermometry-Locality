# The 30-milestone understanding map

**Map revision 1 — settled 4 November 2026.** This map follows the [canonical scientific account](../science/README.md) from a single thermal occupation to the optimal precision of a complete controlled experiment. Its 30 understanding targets describe the project itself. The exact assumptions and theorem remain in [Model and results](../science/model_and_results.md); the proof pages own the specialist derivations.

The allocation is **14 background/preliminary milestones and 16 narrative/innovation milestones**. The background connects local states and exchange links to measurement records, distinguishability, and the complete estimation problem. The narrative develops two complementary arguments: the converse limits every accessible output, while the construction extracts a useful count with one fixed sensor. They meet at the joint spatial and temporal law; the last milestones interpret its Markov comparison, scope, and significance. Each phase ends by integrating its components. The map covers the load-bearing ideas without treating every proof calculation or neighboring subject as a separate milestone.

## Selected educational anchor

**WM** denotes Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control*, Cambridge University Press, **first edition, first published 2010**, ISBN 9780521804424; [book DOI](https://doi.org/10.1017/CBO9780511813948). The [publisher's front matter](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf) identifies this edition, and its [table of contents](https://assets.cambridge.org/97805218/04424/toc/9780521804424_toc.pdf) verifies the following section numbers and printed starting pages.

| WM pointer | Printed start | Role in this map |
| --- | ---: | --- |
| Appendix A.1 | 398 | States, operators, and evolution |
| Appendix A.2 | 404 | Composite systems and correlations |
| §1.4 | 32 | General measurement instruments |
| §2.2 | 54 | Fisher information and local optimality |
| §2.7 | 85 | Distinguishing quantum states |
| §3.2 | 99 | The Born–Markov approximation |
| §3.5 | 113 | Fermionic reservoir occupations |
| §3.6 | 119 | Positive Lindblad evolution |
| §3.11 | 141 | Evolution of observables |
| §4.2 | 149 | Monitored jump dynamics |
| §4.3 | 154 | Detection events and their interpretation |
| §5.4 | 237 | Feedback from a monitored system |
| Chapter 6 | 269 | State-conditioned feedback |

These are targeted entry points within **one educational anchor**. The XX-chain reduction, correlated thermal marginals, dimension-independent locality argument, count determinant, and global minimax proof are supplied by the linked project science. The primary literature cited there provides research attribution and proof dependencies. The WM pointers do not attribute those project results to the textbook.

## Phase I — Background and preliminaries, M01–M14

The progression is from one occupation and one bond to an entire temperature-estimation experiment.

| Milestone | Place in the argument |
| --- | --- |
| [M01](#m01-thermal-information-in-one-occupation) | Locate the unknown parameter in a thermal population. |
| [M02](#m02-a-bounded-exchange-link-and-its-time-scale) | Identify the microscopic coupling and time resource. |
| [M03](#m03-from-the-endpoint-spin-chain-to-thermal-modes) | Represent the thermal chain by its covariance. |
| [M04](#m04-the-state-of-an-accessible-block) | Preserve the actual correlated marginal. |
| [M05](#m05-a-positive-band-and-a-fixed-temperature-interval) | Identify the assumptions behind uniform response. |
| [M06](#m06-a-microscopic-bath-and-a-reduced-generator) | Separate the two roles of reduced dynamics. |
| [M07](#m07-a-loss-event-and-its-measurement-record) | Relate detection, disturbance, and sensor reset. |
| [M08](#m08-instruments-and-the-complete-output) | Include every accessible record and memory. |
| [M09](#m09-adaptive-control-with-a-parameter-independent-apparatus) | Track how feedback uses existing information. |
| [M10](#m10-distinguishing-two-temperatures) | Give information an operational testing meaning. |
| [M11](#m11-relative-entropy-and-information-in-a-finite-region) | Quantify distinguishability in correlated states. |
| [M12](#m12-propagation-under-bounded-bath-couplings) | Understand what local control cannot accelerate. |
| [M13](#m13-global-error-and-the-choice-of-loss) | Specify the risk that the theorem bounds. |
| [M14](#m14-the-complete-thermometry-experiment) | Assemble the full problem and its two proof tasks. |

### M01. Thermal information in one occupation

**Central question.** How can the population of one known energy level carry information about an unknown temperature?

**Understanding target.** Explain a two-level occupation, its probability, and its mean. Interpret $`f_b(E)=(1+e^{bE})^{-1}`$ for a thermal mode with known dimensionless energy $`E`$, and identify $`b=J/(k_BT)`$ as the unknown parameter. A thermal preparation is a parameter-bearing state.

**Dependencies and story role.** None. This is the local statistical object from which both the reservoir covariance and the observed counts will be built.

**Conceptual connection.** A temperature-dependent distribution provides information before any sensor or controller is introduced; later operations determine which part becomes accessible.

**Sources.** Anchor: WM Appendix A.1, p. 398, and §3.5, p. 113. Science: [reservoir and parameter](../science/model_and_results.md#reservoir-and-temperature-parameter).

### M02. A bounded exchange link and its time scale

**Central question.** What can one nearest-neighbor exchange bond do, and which physical scale limits its action?

**Understanding target.** Distinguish local occupation from exchange of an excitation between adjacent spins. Identify the hopping energy $`J`$, dimensionless time $`\tau=Jt/\hbar`$, and the finite-dimensional local spin space. Explain why an operation inside a contacted region and the bond leaving that region are different resources.

**Dependencies and story role.** M01. Add dynamics to the local thermal object and establish the link that later carries information toward a sensor.

**Conceptual connection.** The bath's fixed exchange scale connects elapsed time to spatial influence even when apparatus operations are arbitrarily fast.

**Sources.** Anchor: WM Appendix A.1, p. 398, and §3.2, p. 99, for Hamiltonians and microscopic coupling. Science: [reservoir Hamiltonian](../science/model_and_results.md#reservoir-and-temperature-parameter); [operational resources](../science/model_and_results.md#operational-resources).

### M03. From the endpoint spin chain to thermal modes

**Central question.** How does this many-spin thermal state admit a one-particle description?

**Understanding target.** Explain the endpoint Jordan–Wigner ordering, the number-conserving quadratic Hamiltonian, and the covariance $`C_b=f_b(h_B)`$. Distinguish physical spins, spatial sites, and natural occupation modes. Understand that Gaussian structure determines higher correlations from the covariance; it does not make spatial sites independent.

**Dependencies and story role.** M01, M02. Extend the local occupation picture to a correlated chain with a known spectral band.

**Conceptual connection.** The same covariance description will support a finite-region distinguishability bound and the count statistics of the sensor.

**Sources.** Anchor: WM §3.5, p. 113; the spin-chain reduction is supplied locally. Science: [thermal covariance and sine transform](../science/model_and_results.md#reservoir-and-temperature-parameter); [one-particle sensor description](../science/counted_sensor.md#1-apparatus-and-one-particle-description).

### M04. The state of an accessible block

**Central question.** Which state is available when only the first few spins of a thermal chain can be accessed?

**Understanding target.** Interpret a partial trace and the compressed covariance $`P_RC_bP_R`$. Explain why the actual reduced state generally differs from a Gibbs state prepared on an isolated block. Recognize that compressions at different temperatures need not commute even though the full thermal covariances do.

**Dependencies and story role.** M03. Identify the correct finite input state for any locally confined experiment.

**Conceptual connection.** Restricting access preserves the consequences of initial correlations; deleting a dynamical bond does not retrospectively change the initial preparation.

**Sources.** Anchor: WM Appendix A.2, p. 404. Science: [actual local thermal states](../science/model_and_results.md#reservoir-and-temperature-parameter); [thermal distinguishability of the actual marginal](../science/locality_converse.md#thermal-distinguishability-of-the-actual-marginal).

### M05. A positive band and a fixed temperature interval

**Central question.** Which assumptions keep thermal occupation uniformly responsive to the parameter?

**Understanding target.** Explain the roles of $`\nu>2`$ and a fixed compact interval $`0\lt b_-\lt b_+\lt\infty`$. The covariance eigenvalues stay away from zero and one, and every positive-energy occupation decreases with $`b`$. Distinguish a strictly positive response on a fixed interval from a response bound uniform down to zero temperature.

**Dependencies and story role.** M01, M03, M04. Identify the quantitative assumptions shared by the information bound and the explicit estimator.

**Conceptual connection.** Spectral control supplies both an entropy constant and an inverse-mean stability constant; their physical roles are different.

**Sources.** Anchor: WM §3.5, p. 113. Science: [thermal covariance bounds](../science/locality_converse.md#applying-the-estimate-to-thermal-covariances); [uniform susceptibility](../science/counted_sensor.md#4-a-global-estimator-including-biased-outcomes); [scope](../science/model_and_results.md#scope-of-the-theorem).

### M06. A microscopic bath and a reduced generator

**Central question.** What is assumed when a bath is replaced by a temperature-dependent Markov generator?

**Understanding target.** Distinguish the chain's explicit microscopic dynamics from a reduced Markov description derived in an approximation regime. A generator's Lindblad form guarantees legitimate reduced evolution, not accuracy for every microscopic coupling or control. Separately identify the known vacuum loss channel used as a sensor-reset resource.

**Dependencies and story role.** M02, M03. Introduce the two dynamical descriptions whose operational predictions will later be compared.

**Conceptual connection.** The unknown temperature enters the chain's initial state; the apparatus reset is parameter independent, while the reference thermal Markov rates depend on temperature.

**Sources.** Anchor: WM §§3.2 and 3.6, pp. 99 and 119. Science: [sensor reset and microscopic bath](../science/counted_sensor.md#1-apparatus-and-one-particle-description); [formal weak-coupling rates](../science/physical_consequences.md#microscopic-interaction-and-formal-weak-coupling-rates).

### M07. A loss event and its measurement record

**Central question.** What information is retained by detecting a sensor's loss events?

**Understanding target.** Distinguish a conditioned trajectory, its jump record, and the unconditional state obtained by averaging over records. Explain how a counted loss returns the sensor to its empty state while the bath continues to evolve. Resetting the sensor does not prepare another independent thermal bath sample.

**Dependencies and story role.** M01, M06. Introduce the observed data used by the attaining experiment and the resource meaning of repeated detection.

**Conceptual connection.** The detector can accumulate information across time even when the sensor has little information in its final state.

**Sources.** Anchor: WM §§4.2–4.3, pp. 149 and 154. Science: [counted sensor instrument](../science/counted_sensor.md#1-apparatus-and-one-particle-description); [one initial thermal reservoir](../science/model_and_results.md#operational-resources).

### M08. Instruments and the complete output

**Central question.** What is the output of an experiment that measures, stores, and continues interacting?

**Understanding target.** Describe a measurement instrument as producing both an outcome and a conditional state. Include classical outcomes, their timing, retained quantum memory, and any final joint measurement in the accessible output. Explain why a statement about the sensor's final reduced state alone need not constrain this complete experiment.

**Dependencies and story role.** M04, M07. Enlarge the description from one detected event to the full data-bearing system.

**Conceptual connection.** A universal precision limit must survive every allowed processing and joint measurement of the accumulated output.

**Sources.** Anchor: WM §1.4, p. 32, and §4.2, p. 149. Science: [complete operational output](../science/model_and_results.md#operational-resources); [whole-output truncation](../science/locality_converse.md#truncating-the-complete-output).

### M09. Adaptive control with a parameter-independent apparatus

**Central question.** How can feedback depend on temperature-bearing observations while its implementation remains parameter independent?

**Understanding target.** Distinguish a fixed rule controlled by an outcome register from a device supplied with the unknown parameter. Explain why apparatus entanglement, memory, resets, and record-dependent intervention times are allowed, while free initial bath–apparatus correlations or thermal replacement inputs change the resources.

**Dependencies and story role.** M07, M08. Extend the complete-output picture to the arbitrary adaptive protocols covered by the theorem.

**Conceptual connection.** Feedback can rearrange and process information already obtained from the bath; it is not an additional temperature-bearing input.

**Sources.** Anchor: WM §5.4, p. 237, and Chapter 6, p. 269. Science: [allowed apparatus and controls](../science/model_and_results.md#operational-resources); [dilation of an adaptive experiment](../science/locality_converse.md#compressing-an-arbitrary-adaptive-experiment).

### M10. Distinguishing two temperatures

**Central question.** How does distinguishability of two output states constrain a temperature measurement?

**Understanding target.** Interpret trace distance as the largest difference in the probability of a binary measurement event, and total variation as its classical counterpart. Relate it to the unavoidable error in discriminating two equally likely states. Explain why a common parameter-independent channel cannot improve distinguishability.

**Dependencies and story role.** M08, M09. Give the information available to a controlled experiment an operational definition.

**Conceptual connection.** A temperature estimator induces a two-temperature decision rule, allowing a testing limit to constrain estimation.

**Sources.** Anchor: WM §2.7, p. 85. Science: [testing and minimax reduction](../science/locality_converse.md#global-minimax-reduction); [meaning of complete-output distance](../science/locality_converse.md#truncating-the-complete-output).

### M11. Relative entropy and information in a finite region

**Central question.** How can nearby correlated thermal states have a useful quantitative distinguishability bound?

**Understanding target.** Interpret quantum relative entropy as a comparison of entire states, connect it to trace distance through Pinsker's inequality, and recognize the role of a bound proportional to region size times squared parameter separation. Spatial correlations prevent an assumption of independent site samples.

**Dependencies and story role.** M04, M05, M10. Supply the statistical tool for limiting information in the initial region that can influence the output.

**Conceptual connection.** Finite information density here means a relative-entropy estimate. An energy or entropy current bound alone does not establish it for arbitrary invasive controls.

**Sources.** Anchor: WM §2.7, p. 85, for the discrimination perspective; the entropy estimate is supplied by the project. Science: [Gaussian relative entropy](../science/locality_converse.md#gaussian-logarithms-and-relative-entropy); [global testing use](../science/locality_converse.md#global-minimax-reduction).

### M12. Propagation under bounded bath couplings

**Central question.** Why does strong control at one end leave a finite rate for influence across untouched bath bonds?

**Understanding target.** Connect support of an observable, a local Hamiltonian term, and a commutator to propagation. Interpret a Lieb–Robinson estimate as a small tail outside an effective influence region, not a strictly sharp light cone. Identify which coupling norms and graph connections determine the estimate.

**Dependencies and story role.** M02, M08, M09. Connect local dynamics to the spatial extent of the initial thermal state relevant at a given time.

**Conceptual connection.** Large apparatus dimension and fast internal operations must be separated from the fixed boundary bond before drawing an information-supply conclusion.

**Sources.** Anchor: WM §3.11, p. 141, for observable evolution; locality is a project proof dependency. Science: [compressed boundary dynamics](../science/locality_converse.md#compressing-an-arbitrary-adaptive-experiment); [dimension-independent path estimate](../science/locality_converse.md#a-dimension-independent-path-estimate).

### M13. Global error and the choice of loss

**Central question.** Which precision claim remains meaningful for every parameter and every outcome of the experiment?

**Understanding target.** Interpret the infimum over protocols and estimators, supremum over a fixed parameter interval, and expectation over all records. Explain squared log-temperature loss, its compact-interval comparison with $`b`$-MSE, and the distinction between MSE and root mean squared error. Identify the extra assumptions that prevent a local Fisher-information statement from automatically giving this global claim.

**Dependencies and story role.** M05, M08, M10, M11. Specify the common statistical objective for the lower and upper bounds.

**Conceptual connection.** Clipping, biased estimates, and unfavorable outcomes belong to the global risk calculation; a two-point argument does not require local unbiasedness.

**Sources.** Anchor: WM §§2.2 and 2.7, pp. 54 and 85. Science: [loss and minimax risk](../science/model_and_results.md#loss-units-and-minimax-risk); [testing lower bound](../science/locality_converse.md#global-minimax-reduction).

### M14. The complete thermometry experiment

**Central question.** How do the state, dynamics, access, record, and loss define one precise research problem?

**Understanding target.** Trace the unknown parameter from one initial thermal half-chain through fixed spatial contact, permitted controls, the complete output, and an estimator. Identify $`r`$ and $`\tau`$ as the charged resources; sensor number is different from contacted bath volume. State the two required tasks: constrain every allowed experiment and exhibit one attaining construction in that same model.

**Dependencies and story role.** M03–M13. Synthesize the background into the full operational framework and orient the two proof branches.

**Conceptual connection.** Both branches must include the same initial correlations, reset rules, hard time budget, instantaneous block-access convention, and operational limits for continuous records.

**Sources.** Anchor: WM §§1.4, 2.7, and 5.4, pp. 32, 85, and 237. Science: [operational model](../science/model_and_results.md#operational-resources); [theorem](../science/model_and_results.md#theorem-optimal-contact-and-time-scaling); [connected scientific argument](../science/README.md#the-connected-argument).

## Phase II — Narrative and innovation, M15–M30

The converse starts at the controlled boundary and reaches a statement about every complete output. The construction starts at one sensor and reaches a global estimator. Their combination supports the final resource interpretation and the controlled Markov comparison.

| Milestone | Place in the argument |
| --- | --- |
| [M15](#m15-put-the-adaptive-experiment-into-one-boundary-vertex) | Retain and dilate the complete experiment. |
| [M16](#m16-remove-internal-control-without-strengthening-the-bath-bond) | Isolate the fixed outgoing coupling. |
| [M17](#m17-bound-influence-along-the-remaining-chain) | Obtain a uniform propagation estimate. |
| [M18](#m18-cut-the-dynamics-while-keeping-the-true-initial-state) | Reduce the output to a finite initial marginal. |
| [M19](#m19-bound-distinguishability-of-the-correlated-thermal-block) | Bound that marginal's thermal information. |
| [M20](#m20-convert-locality-into-a-global-risk-lower-bound) | Complete the all-control converse. |
| [M21](#m21-build-the-fixed-counted-sensor) | Specify the attaining physical instrument. |
| [M22](#m22-identify-the-physical-spin-count-distribution) | Derive the observed count law. |
| [M23](#m23-prove-a-continuing-supply-of-detectable-modes) | Prove linear extraction from one bath. |
| [M24](#m24-define-the-infinite-bath-count-and-its-finite-size-limits) | Control the infinite-volume and count limits. |
| [M25](#m25-estimate-temperature-from-every-possible-count) | Obtain a uniform global upper bound. |
| [M26](#m26-join-spatial-access-and-elapsed-time) | Establish the matching joint resource law. |
| [M27](#m27-construct-the-collective-markov-comparison-record) | Define an attainable comparison experiment. |
| [M28](#m28-test-uniform-accuracy-of-the-controlled-markov-model) | Derive an obstruction at the level of records. |
| [M29](#m29-delimit-the-claim-and-account-for-its-ingredients) | Place assumptions, attribution, and evidence. |
| [M30](#m30-synthesize-the-resource-law-and-its-physical-meaning) | Integrate the complete scientific contribution. |

### M15. Put the adaptive experiment into one boundary vertex

**Central question.** How can one proof encompass arbitrary measurements, resets, feedback, and retained memory?

**Understanding target.** Explain the parameter-independent unitary dilation of finite interventions and the retention of their registers and discarded environments. Group the entire apparatus with the first $`r`$ bath spins. Understand why enlarging this boundary output strengthens the observer for a converse and why record-dependent operations remain fixed controlled operations.

**Dependencies and story role.** M08, M09, M14. Begin the converse by representing all permitted local complexity in one object.

**Conceptual connection.** The measurement-and-control language becomes a boundary geometry suitable for an estimate that is uniform over apparatus size.

**Sources.** Anchor: WM §1.4, p. 32, §5.4, p. 237, and Chapter 6, p. 269. Science: [compressing the adaptive experiment](../science/locality_converse.md#compressing-an-arbitrary-adaptive-experiment).

### M16. Remove internal control without strengthening the bath bond

**Central question.** Why does arbitrary control strength within the boundary fail to increase the remaining bond norms?

**Understanding target.** Explain the local interaction picture that removes dynamics internal to the enlarged boundary and the bath on-site terms. Track the outgoing exchange bond under unitary conjugation: its norm and support remain bounded. Recognize that the resulting chain geometry is independent of the boundary Hilbert-space dimension.

**Dependencies and story role.** M02, M12, M15. Expose the fixed microscopic connection after accounting for all controller freedom.

**Conceptual connection.** The relevant speed limit comes from untouched links, even when the contacted region contains very large collective matrix elements.

**Sources.** Anchor: WM §3.11, p. 141, and §5.4, p. 237, for changes of dynamical description and control. Science: [interaction-picture reduction](../science/locality_converse.md#compressing-an-arbitrary-adaptive-experiment).

### M17. Bound influence along the remaining chain

**Central question.** Which features of the chain determine a propagation bound uniform over every boundary controller?

**Understanding target.** Explain why influence across distant edges requires paths of overlapping local terms. Relate bounded generator norms, bounded edge adjacency, and ordered time integrals to the exponential tail. Identify the absence of factors depending on apparatus dimension, record size, or internal control strength; the explicit velocity is a conservative bound.

**Dependencies and story role.** M12, M16. Turn the reduced boundary geometry into the quantitative locality ingredient.

**Conceptual connection.** Operator-norm control applies before choosing an initial state or a final observable, which is essential for a complete-output statement.

**Sources.** Anchor: WM §3.11, p. 141, as observable-evolution background; the path estimate is supplied in the project. Science: [dimension-independent path estimate](../science/locality_converse.md#a-dimension-independent-path-estimate).

### M18. Cut the dynamics while keeping the true initial state

**Central question.** How does deleting one distant bath bond reduce the whole experiment to a finite input state?

**Understanding target.** Follow Duhamel's comparison and operator-norm duality from the path estimate to trace distance of the complete output. Keep the same correlated initial bath in the full and cut experiments. Explain why the cut output is a parameter-independent channel of the actual marginal $`\rho_{b,R}`$ despite correlations across the cut.

**Dependencies and story role.** M04, M10, M15, M17. Connect spatial locality to an explicit statistical input of finite size.

**Conceptual connection.** The bound controls all joint measurements of records and memory. It neither discards initial correlations nor substitutes the equilibrium state of a cut Hamiltonian.

**Sources.** Anchor: WM Appendix A.2, p. 404, and §2.7, p. 85. Science: [complete-output truncation](../science/locality_converse.md#truncating-the-complete-output); [infinite bath and continuous records](../science/locality_converse.md#infinite-bath-and-continuous-records).

### M19. Bound distinguishability of the correlated thermal block

**Central question.** Why is the block's relative entropy at most proportional to its size and squared temperature-parameter separation?

**Understanding target.** Explain how Gaussian density-matrix logarithms reduce relative entropy to a one-particle matrix expression. Identify why compressed covariances cannot be treated as simultaneously diagonal, and how the matrix-entropy Hessian and the spectral floor handle this. Connect the covariance derivative bound to $`D(\rho_{b,R}\Vert\rho_{b',R})\le KR(b-b')^2`$.

**Dependencies and story role.** M03, M04, M05, M11, M18. Supply the information-density estimate for the finite input isolated by locality.

**Conceptual connection.** Correlations and noncommutativity are retained while the information bound remains extensive in $`R`$.

**Sources.** Anchor: WM §2.7, p. 85, and §3.5, p. 113, as statistical and reservoir background. Science: [Gaussian relative entropy](../science/locality_converse.md#gaussian-logarithms-and-relative-entropy); [application to thermal covariances](../science/locality_converse.md#applying-the-estimate-to-thermal-covariances).

### M20. Convert locality into a global risk lower bound

**Central question.** How do a constant truncation error and a finite-region information bound constrain every estimator?

**Understanding target.** Choose $`R=O(r+\tau)`$ and two parameters separated by order $`R^{-1/2}`$, with the same pair usable for every controller. Combine data processing, Pinsker's inequality, and the two truncation errors. Explain why a decision error forces estimation error and yields the global lower bound, including biased estimates and unfavorable records.

**Dependencies and story role.** M10, M13, M18, M19. Complete the first proof branch and its uniformity over protocols.

**Conceptual connection.** Constant-error binary testing suffices; no derivative of an approximate channel or continuity of Fisher information is needed. The testing inequalities also pass to admissible continuous-record limits.

**Sources.** Anchor: WM §§2.2 and 2.7, pp. 54 and 85. Science: [global minimax reduction](../science/locality_converse.md#global-minimax-reduction); [operational limits](../science/locality_converse.md#infinite-bath-and-continuous-records); [explicit lower bound](../science/locality_converse.md#explicit-lower-bound-theorem).

### M21. Build the fixed counted sensor

**Central question.** Which fixed local apparatus converts the chain's existing excitations into an accessible record?

**Understanding target.** Specify one initially empty sensor, exchange coupling $`J`$, matching on-site energy, and counted loss at physical rate $`J/(2\hbar)`$. Identify the detector and its classical count as apparatus resources. The reset channel is temperature independent, and the same thermal chain evolves throughout. Ideal continuous monitoring is an admissible instrument limit.

**Dependencies and story role.** M02, M03, M06, M07, M14. Start the separate attaining branch with a concrete physical experiment.

**Conceptual connection.** A lower bound on all controllers becomes useful only when a permitted controller extracts information at the same order without replacing the bath.

**Sources.** Anchor: WM §§3.6 and 4.2, pp. 119 and 149. Science: [apparatus and one-particle description](../science/counted_sensor.md#1-apparatus-and-one-particle-description); [admissible resources](../science/model_and_results.md#operational-resources).

### M22. Identify the physical spin count distribution

**Central question.** Why does the observed spin-reset count obey a fermionic determinant identity?

**Understanding target.** Relate each counted jump to one lost excitation, use endpoint ordering to identify the physical jump with $`c_0`$, and explain Gaussian evolution in the even sector. Interpret the determinant through Bernoulli occupation modes and its variance bound. Independence in this representation does not imply independent jump times or fermionic detector photons.

**Dependencies and story role.** M03, M07, M08, M21. Establish the law of the actually measured statistic before estimating temperature.

**Conceptual connection.** The spin instrument and excitation accounting justify the count law; an imagined output-particle statistics assumption is unnecessary.

**Sources.** Anchor: WM §§4.2–4.3, pp. 149 and 154. Science: [Gaussian even-sector evolution](../science/counted_sensor.md#gaussian-evolution-in-the-even-sector); [jumps and lost excitations](../science/counted_sensor.md#relate-counted-jumps-to-lost-excitations); [count determinant](../science/counted_sensor.md#2-the-actual-spin-count-has-a-determinant-law).

### M23. Prove a continuing supply of detectable modes

**Central question.** Why can a single boundary sensor keep extracting information from one unreprepared half-chain?

**Understanding target.** Connect the loss trace to a boundary survival probability. Explain the roles of the semicircle spectral density, the finite squared return-amplitude integral, and the dissipative rank-one resolvent bound. Interpret $`\operatorname{Tr}M_\tau\ge\kappa q\tau-1`$ with fixed $`\kappa=1/2`$ and $`q=1-4/(3\pi)>0`$: the linear term supplies growing loss channels, and the subtraction removes the initially empty sensor mode.

**Dependencies and story role.** M02, M03, M21, M22. Establish the dynamical supply needed for an inverse-time upper bound.

**Conceptual connection.** The available modes grow because excitations propagate from an extended initial bath, not because the detector creates new thermal samples.

**Sources.** Anchor: WM §3.5, p. 113, and §4.2, p. 149; the return-amplitude estimate is supplied by the project. Science: [linear extraction](../science/counted_sensor.md#3-linear-extraction-from-the-initially-thermal-half-chain); [free boundary return](../science/counted_sensor.md#the-free-boundary-return-has-finite-squared-integral); [dissipative bound](../science/counted_sensor.md#dissipation-cannot-increase-that-squared-integral).

### M24. Define the infinite-bath count and its finite-size limits

**Central question.** In what sense is the half-chain count a well-defined finite-time probability law?

**Understanding target.** Explain why the loss operator is trace class at every fixed time, how finite-chain operators and count laws converge, and how bounded jump intensity controls moments. Distinguish this limit from assuming a global thermal density matrix or an infinite total-excitation observable. A fixed finite bath ultimately depletes and cannot sustain the same all-time extraction law.

**Dependencies and story role.** M04, M12, M21, M22, M23. Establish the meaning and limits of the construction's infinite reservoir.

**Conceptual connection.** Finite calculations can verify the physical count law and pre-reflection behavior; the trace-class and spectral arguments establish the infinite-volume claims.

**Sources.** Anchor: WM §§3.5 and 4.2, pp. 113 and 149, for reservoir and jump concepts. Science: [infinite-volume count and moments](../science/counted_sensor.md#infinite-volume-count-and-moments); [verification scope](../science/counted_sensor.md#6-what-the-verification-does-and-does-not-establish).

### M25. Estimate temperature from every possible count

**Central question.** How can the count produce a global error bound without local unbiasedness or asymptotic normality?

**Understanding target.** Use the positive-band susceptibility to bound the slope of the calibrated mean, and the count law to bound its variance. Explain clipping to the mean range and inversion, including counts outside that range. Combine the resulting error bound with a midpoint estimate at short times, then convert to squared log-temperature loss on the fixed interval.

**Dependencies and story role.** M05, M13, M22, M23, M24. Complete the temporal attaining construction with an estimator defined for every outcome.

**Conceptual connection.** Linear signal response and at-most-linear noise give a uniform inverse-time risk once the nonlinear inverse is controlled globally.

**Sources.** Anchor: WM §2.2, p. 54, as the local-estimation comparison, and §4.2, p. 149. Science: [global count estimator](../science/counted_sensor.md#4-a-global-estimator-including-biased-outcomes); [loss-coordinate comparison](../science/model_and_results.md#loss-units-and-minimax-risk).

### M26. Join spatial access and elapsed time

**Central question.** How do the converse and two simple measurements establish the full $`1/(r+\tau)`$ law?

**Understanding target.** Explain the initial block-occupation measurement, its true marginal covariance, variance of order $`r`$, and susceptibility of order $`r`$. Use the permitted instantaneous instrument when $`r\ge\tau`$ and the counted-sensor construction otherwise. Combine this all-time upper bound with the converse, without assuming independence between block and temporal samples.

**Dependencies and story role.** M04, M13, M14, M20, M25. Join the two proof branches into the exact minimax order for every $`r\ge1`$ and $`\tau\ge0`$.

**Conceptual connection.** Initially accessible thermal volume and elapsed propagation time supply alternative routes to the same order; auxiliary probe number changes neither charged quantity.

**Sources.** Anchor: WM §§1.4 and 2.7, pp. 32 and 85. Science: [spatial access and the joint law](../science/counted_sensor.md#5-spatial-access-and-the-joint-law); [canonical matching theorem](../science/model_and_results.md#theorem-optimal-contact-and-time-scaling).

### M27. Construct the collective Markov comparison record

**Central question.** Which operationally accessible record displays the collective enhancement predicted by the reference Markov model?

**Understanding target.** Explain the central Dicke-state preparation, frequent probe-population measurements, recorded transition direction, and restoration. Identify the enhanced, temperature-independent total rate $`\Lambda_N=a_N\Gamma`$ and the temperature-dependent labels of the marked Poisson record. Interpret its global risk of order $`(1+\Lambda_N\tau)^{-1}`$ as an attainable property of this record, not an assertion about every possible Markov protocol.

**Dependencies and story role.** M06, M07, M09, M13, M26. Define a concrete statistical experiment against which microscopic locality can be compared.

**Conceptual connection.** The record comes from probe measurements rather than assumed access to microscopic bath jumps. The same rapid controls can have different microscopic backaction, including Zeno suppression.

**Sources.** Anchor: WM §3.2, p. 99, and §5.4, p. 237. Science: [formal collective rates](../science/physical_consequences.md#microscopic-interaction-and-formal-weak-coupling-rates); [accessible probe record](../science/physical_consequences.md#a-record-obtainable-from-probe-measurements); [global record precision](../science/physical_consequences.md#global-minimax-precision-of-this-record).

### M28. Test uniform accuracy of the controlled Markov model

**Central question.** Why must a Markov model with an unbounded collective rate fail to approximate some controlled records uniformly?

**Understanding target.** Compare the same finite-cadence probe protocols at a fixed microscopic contact and elapsed time. The microscopic two-temperature distinguishability stays bounded below perfect discrimination, while the reference Markov record approaches perfect discrimination as its rate grows. Use the triangle inequality to obtain a nonzero approximation error for at least one temperature.

**Dependencies and story role.** M10, M13, M20, M27. Turn the matched theorem into an operational consequence for reduced dynamics.

**Conceptual connection.** This is an obstruction to uniform accuracy across controlled experiments. It does not locate a sharp crossover, establish accuracy below one, or determine the error of an uncontrolled probe.

**Sources.** Anchor: WM §2.7, p. 85, §3.2, p. 99, and Chapter 6, p. 269. Science: [uniform Markov-accuracy obstruction](../science/physical_consequences.md#an-operational-obstruction-to-uniform-markov-accuracy); [controller-independent two-point bound](../science/locality_converse.md#global-minimax-reduction).

### M29. Delimit the claim and account for its ingredients

**Central question.** What is established, what is inherited, and which changes would require a new theorem?

**Understanding target.** State the roles of a positive band, fixed compact interval, one initially thermal half-chain, fixed contacts, and bounded outgoing bonds. Explain how a moving contact, fresh thermal inputs, a temperature-bearing actuator, or an unbounded local bosonic degree of freedom changes the model. Separate the matched complete-experiment result from its established locality, Gaussian, counting, and statistical ingredients.

**Dependencies and story role.** M05, M14, M24, M26, M28. Delimit the interpretation before the final synthesis.

**Conceptual connection.** Finite numerical checks support specific identifications and approximations; they do not certify universal scaling or priority. No pointwise QFI bound, uniform zero-temperature law, or sharp finite-coupling crossover follows from the theorem.

**Sources.** Anchor: WM §§2.2 and 3.2, pp. 54 and 99, for estimation and approximation distinctions. Science: [theorem scope](../science/model_and_results.md#scope-of-the-theorem); [changed resources](../science/physical_consequences.md#which-resources-would-change-the-conclusion); [verification limits](../science/counted_sensor.md#6-what-the-verification-does-and-does-not-establish); [attribution and contribution](../references/RELATED_WORK.md#mathematical-and-physical-contribution).

### M30. Synthesize the resource law and its physical meaning

**Central question.** Why does $`r+Jt/\hbar`$ control optimal thermometric precision in this model?

**Understanding target.** Give a connected account: the unknown temperature is initially encoded in the bath; bounded links limit which initial region can influence every accessible record; that region has bounded thermal distinguishability; a fixed counted sensor and initial block readout attain the resulting order. Interpret the mean squared log-temperature law and its square root, with constants and scope intact.

**Dependencies and story role.** M14, M20, M26, M28, M29. Complete the narrative by joining mechanisms, global statistics, and physical implications.

**Conceptual connection.** The result identifies a resource limit on acquiring initially encoded information. Arbitrary apparatus at a fixed contact may improve constants or implementation, while the controlled Markov comparison exposes the cost of treating thermal information supply as unrestricted.

**Sources.** Anchor: WM §§2.2, 2.7, 3.2, and 4.2, pp. 54, 85, 99, and 149. Science: [canonical theorem](../science/model_and_results.md#theorem-optimal-contact-and-time-scaling); [converse meaning](../science/locality_converse.md#what-the-proof-establishes); [matching construction](../science/counted_sensor.md#5-spatial-access-and-the-joint-law); [physical interpretation](../science/physical_consequences.md#what-the-precision-law-says); [operational Markov consequence](../science/physical_consequences.md#an-operational-obstruction-to-uniform-markov-accuracy).
