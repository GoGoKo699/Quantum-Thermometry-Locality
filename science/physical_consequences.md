# Physical consequences and a controlled Markov comparison

## What the precision law says

The [model and theorem](model_and_results.md) concern one initially thermal XX half-chain with positive one-particle band. Write $`b=\beta J`$ and $`\tau=Jt`$, using $`\hbar=k_{\mathrm B}=1`$. The parameter interval $`[b_-,b_+]`$ is fixed and contained in $`(0,\infty)`$. For all allowed experiments supported on the first $`r`$ bath sites,

```math
\mathcal R_b(r,\tau)
=\inf_{\mathcal P,\widehat b}\sup_{b\in[b_-,b_+]}
  \mathbb E_b[(\widehat b-b)^2]
=\Theta\!\left(\frac{1}{r+\tau}\right).
```

The constants depend on the known band and parameter interval, but not on thermometer size, retained memory, entanglement, or the strength of controls inside the contacted region.

This identifies two ways to improve the order of the precision. One can initially access more thermal sites, or allow more time for the chain to bring initially encoded information into reach. Adding arbitrarily many auxiliary probes at a fixed contact supplies neither resource. Such probes can still improve constants, implement convenient readout, or operate efficiently in restricted regimes.

The [counted-sensor construction](counted_sensor.md) shows that the bound is attainable. For $`\tau>r`$, one fixed two-level sensor with fixed hopping and fixed counted loss suffices. Its detector resets the sensor into a known state; the thermal chain evolves throughout and is never re-prepared. For $`r\geq\tau`$, a measurement of the initial contacted block's occupation supplies the matching order.

The theorem applies to squared log-temperature error as well: on the fixed interval, the dimensionless coordinate $`\theta=\log(k_{\mathrm B}T/J)=-\log b`$ is bi-Lipschitz in $`b`$. Squared error in physical inverse temperature carries the dimensional factor $`J^{-2}`$. None of these comparisons has constants uniform as $`b_+\to\infty`$ or as the positive band gap closes.

## A collective Markov experiment

Collective thermometry within a prescribed Markov generator can have a quadratic enhancement in the number of probes. The central-state measurement and preparation construction below follows [Sekatski and Perarnau-Llobet, §4.2](https://arxiv.org/html/2107.04425v2). We specialize its rates to the endpoint spectrum of this chain and state the resulting **global** estimation performance.

### Microscopic interaction and formal weak-coupling rates

Take an even number $`N`$ of probe spins in the symmetric sector of spin $`s=N/2`$. Let their known level spacing in units of $`J`$ be $`\Delta\in(\nu-2,\nu+2)`$, and use collective operators $`S_z,S_\pm`$. Couple them to the first bath spin through

```math
\frac{H_I}{J}
=\lambda\bigl(S_-\sigma_1^+ + S_+\sigma_1^-\bigr),
\qquad \lambda=\frac{g}{J}.
```

For the free half-chain, the endpoint density of one-particle states is

```math
w_\nu(E)=\frac{\sqrt{4-(E-\nu)^2}}{2\pi},
\qquad \nu-2<E<\nu+2.
```

The ordinary weak-coupling endpoint rates, expressed per unit $`\tau`$, are

```math
\gamma_+(b)=\Gamma f_b(\Delta),\qquad
\gamma_-(b)=\Gamma[1-f_b(\Delta)],
\qquad
\Gamma=2\pi\lambda^2w_\nu(\Delta),\qquad
f_b(E)=\frac{1}{1+e^{bE}}.
```

These Fermi occupation factors belong to this spin chain at its Jordan–Wigner endpoint. They are not rates asserted for every thermal environment. They define the reference Markov generator

```math
\mathcal L_b(\rho)
=-i[\Delta S_z+H_{\rm LS}(b),\rho]
 +\gamma_-(b)\mathcal D[S_-]\rho
 +\gamma_+(b)\mathcal D[S_+]\rho,
\qquad
\mathcal D[A]\rho=A\rho A^\dagger-\tfrac12\{A^\dagger A,\rho\}.
```

The secular Lamb shift is diagonal in the collective-spin population basis, so it does not affect the population experiment below. Using these rates for increasing collective strength is a proposed extension of a weak-coupling description whose uniform validity is being tested, not an assumption that the approximation remains accurate.

### A record obtainable from probe measurements

Prepare the central Dicke state $`|s,0\rangle`$. Measure $`S_z`$ frequently; after an upward or downward transition, record its direction and restore $`|s,0\rangle`$. In the ideal rapid-measurement limit of the Markov model,

```math
|\langle s,\pm1|S_\pm|s,0\rangle|^2
=a_N=s(s+1)=\frac{N(N+2)}4.
```

The total departure rate is

```math
\Lambda_N=a_N(\gamma_++\gamma_-)=a_N\Gamma.
```

It is independent of $`b`$. Restoring the same state after every departure therefore produces a Poisson event process of rate $`\Lambda_N`$, with independent labels that are upward with probability $`p_b=f_b(\Delta)`$. Equivalently, the two observed counts are independent variables

```math
X_+\sim{\rm Poisson}(\Lambda_N\tau p_b),\qquad
X_-\sim{\rm Poisson}(\Lambda_N\tau[1-p_b]).
```

No access to an unobserved microscopic bath jump channel is assumed. The record is obtained by measurements on the probe itself. For each finite $`N`$, finite measurement cadences approach this Markov counting experiment. Since the largest population transition rate is of order $`\Lambda_N`$, taking a mesh $`\delta_N`$ with $`\tau\Lambda_N^2\delta_N\to0`$ controls the total probability of multiple unresolved events and delayed restoration. Thus a sequence of finite, parameter-independent control protocols also realizes its limiting distinguishability.

The same rapid measurements have their actual microscopic backaction when applied to the chain. They can produce Zeno suppression; their effect cannot be inferred by retaining a Markov jump rate outside its regime of validity.

### Global minimax precision of this record

Set $`q=\Lambda_N\tau`$. For $`q\geq1`$, let

```math
\widehat p
=\Pi_{[p_{b_+},p_{b_-}]}\!\left(\frac{X_+}{q}\right),
\qquad
\widehat b=f^{-1}_{(\cdot)}(\widehat p;\Delta).
```

Here $`\Pi`$ is Euclidean clipping and the inverse solves $`f_b(\Delta)=\widehat p`$. On the fixed parameter interval,

```math
d_*=\min_{b\in[b_-,b_+]}
      \Delta f_b(\Delta)[1-f_b(\Delta)]>0.
```

The inverse has Lipschitz constant at most $`d_*^{-1}`$. Since $`X_+/q`$ is unbiased for $`p_b`$ with variance $`p_b/q`$, clipping cannot increase its error and

```math
\sup_b\mathbb E_b[(\widehat b-b)^2]
\leq \frac{1}{d_*^2q}.
```

For $`q<1`$, a fixed midpoint estimate gives a constant bound. This proves an upper bound of order $`(1+q)^{-1}`$.

For the reverse bound, the complete marked Poisson record has relative entropy

```math
D(P_b^{\rm M}\Vert P_{b'}^{\rm M})
=q\,D\bigl({\rm Bern}(p_b)\Vert{\rm Bern}(p_{b'})\bigr).
```

Waiting times carry no additional parameter dependence. The Bernoulli probabilities stay in a compact subinterval of $`(0,1)`$, so the last divergence is at most $`C(b-b')^2`$. Two interior parameters separated by $`a/\sqrt{1+q}`$ have bounded distinguishability for sufficiently small fixed $`a`$. Two-point testing then gives

```math
\inf_{\widehat b}\sup_b
\mathbb E_b^{\rm M}[(\widehat b-b)^2]
=\Theta\!\left(\frac{1}{1+\Lambda_N\tau}\right).
```

This is the minimax risk of this particular controlled Markov record. It is not asserted to be the optimum over every Markov protocol, including coherent Lamb-shift schemes. Its attainable rate alone is sufficient for the comparison.

## An operational obstruction to uniform Markov accuracy

The microscopic one-port theorem gives

```math
\mathcal R_b(1,\tau)\geq\frac{c}{1+\tau}
```

uniformly over $`N`$, $`\lambda`$, the probe preparation and all subsequent controls. Comparing this bound only with a Markov Fisher information would leave questions about local estimation and attainability. The preceding global estimator removes that ambiguity. A direct statement about records is stronger still.

Fix $`\tau>0`$. The [two-point converse](locality_converse.md) supplies distinct parameters $`b_0,b_1`$ in the interval, separated by a constant times $`(1+\tau)^{-1/2}`$, such that

```math
\|P^{\rm mic}_{b_0,N}-P^{\rm mic}_{b_1,N}\|_{\rm TV}
\leq q_0<1
```

for every allowed microscopic protocol, with $`q_0`$ independent of $`N`$ and its control strength. The explicit constants in that proof allow $`q_0=3/8`$. This applies in particular to the finite-cadence Dicke preparation and measurement protocols just described.

Suppose $`\Lambda_N\to\infty`$ at this fixed time. Under the Markov model, the normalized upward count consistently estimates $`p_b`$, and $`p_{b_0}\ne p_{b_1}`$. Thresholding that estimate distinguishes the two parameters with error tending to zero. Choosing a sufficiently fine finite cadence therefore yields

```math
\|P^{\rm M}_{b_0,N}-P^{\rm M}_{b_1,N}\|_{\rm TV}\longrightarrow1.
```

The microscopic and Markov distributions here refer to the same probe-measurement record for each $`N`$. If

```math
\epsilon_N=
\max_{j\in\{0,1\}}
\|P^{\rm mic}_{b_j,N}-P^{\rm M}_{b_j,N}\|_{\rm TV},
```

the triangle inequality gives

```math
2\epsilon_N\geq
\|P^{\rm M}_{b_0,N}-P^{\rm M}_{b_1,N}\|_{\rm TV}-q_0,
\qquad
\liminf_{N\to\infty}\epsilon_N\geq\frac{1-q_0}{2}>0.
```

In particular, the displayed choice gives $`\liminf_N\epsilon_N\geq5/16`$. Thus the formal collective Markov model cannot approximate all controlled experiments uniformly over the temperature interval when it predicts an unbounded rate at a fixed microscopic contact and bandwidth. With physical units restored, the comparison is between $`\Lambda_N^{\rm phys}=(J/\hbar)\Lambda_N`$ and the chain rate $`J/\hbar`$.

This is a necessary obstruction. It does not establish validity below a sharp crossover, compute the microscopic error for an uncontrolled probe, or prove an optimal finite-coupling rate of $`\min\{g^2N^2/J,J\}`$. Qualitative requirements that collective relaxation be slower than bath correlation and propagation times are already part of the established analysis; see [Mok et al., Supplement B.5](https://arxiv.org/html/2406.00722v3). The statement here concerns a complete controlled statistical experiment in a specified thermal model.

## Which resources would change the conclusion?

| Change to the experiment | Consequence for the theorem |
| --- | --- |
| Enlarge the contacted interval | Already quantified by the $`r`$ term. More initially accessible thermal sites increase the available information. |
| Replace the thermal bath between trials | Supplies new parameter-bearing states. The theorem assumes one initial bath and does not cover repeated replacements. |
| Supply a thermal actuator or nonlocal thermal observable | Changes where temperature information enters. The global magnetization actuator in [Tumbiolo et al., Supplement Eqs. (S32)–(S39)](https://arxiv.org/html/2511.19631v3) is an example outside fixed local access. |
| Encode the unknown parameter in a Hamiltonian acting throughout the experiment | Changes the statistical model. Here the parameter occurs only in the initial state. |
| Use an unbounded local bosonic Hilbert space, a moving contact or a different bath geometry | Requires a separate locality and information-density analysis. No universal extension is asserted. |
| Use a finite bath | The infinite-chain scaling describes the interval before finite-size boundaries affect extraction. It cannot provide an indefinitely decreasing risk from a fixed finite initial information supply. |

Finally, positivity of the band is doing observable work in the attaining protocol. It makes the mean total extraction count uniformly monotone in $`b`$. At particle–hole symmetry the same unweighted count can lose its temperature response. A different statistic or sensor would then be needed, and no matching theorem for that regime is established here.
