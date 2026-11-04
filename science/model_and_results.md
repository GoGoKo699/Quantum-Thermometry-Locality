# Local thermometry with a complete measurement record

A thermometer that contacts the first $`r`$ sites of a spin reservoir can use the thermal information initially present there and the information transported to that region during the experiment. For the reservoir and controls specified below, these two resources give the exact minimax order

```math
\mathcal R(r,\tau)=\Theta\!\left(\frac{1}{r+\tau}\right),
\qquad \tau=\frac{Jt}{\hbar}.
```

Here $`\mathcal R`$ is the worst-case mean squared error in **logarithmic temperature**, minimized over all allowed protocols and estimators. The lower bound includes arbitrary ancillas, adaptive measurements, feedback, resets, strong control inside the contacted region, and the complete retained measurement record. A single counted sensor attains the time dependence. Direct measurement of the initially accessible bath block supplies the spatial dependence.

The [locality converse](locality_converse.md) proves the lower bound with explicit constants. The [counted sensor construction](counted_sensor.md) proves the matching upper bound. [Physical consequences](physical_consequences.md) discusses the meaning of the result for local sensing and reduced dynamical descriptions.

## Reservoir and temperature parameter

The bath is a semi-infinite chain of spin-$`1/2`$ sites with a known Hamiltonian

```math
\begin{aligned}
H_B
&=J\left[
\nu\sum_{j\ge1}n_j
-\sum_{j\ge1}
\left(\sigma_j^+\sigma_{j+1}^-+\sigma_j^-\sigma_{j+1}^+\right)
\right],\\
n_j&=\sigma_j^+\sigma_j^-,
\qquad J>0,\quad \nu>2.
\end{aligned}
```

The unknown physical temperature $`T`$ enters only through the initial Gibbs state. Define

```math
\begin{aligned}
b&=\beta J=\frac{J}{k_BT},\\
I&=[b_-,b_+],
\qquad
0\lt b_-\lt b_+\lt\infty.
\end{aligned}
```

The interval $`I`$, the hopping energy $`J`$, and the band position $`\nu`$ are known. The interval is fixed as the time and contact resources increase. Except when restoring physical units, use $`\hbar=k_B=1`$ and dimensionless time $`\tau=Jt`$.

The infinite reservoir is specified by its compatible local states; a normalized density matrix on the entire half-chain is unnecessary. With the Jordan–Wigner ordering beginning at the physical endpoint, the one-particle Hamiltonian and thermal covariance are

```math
\begin{aligned}
h_B&=\nu I-S-S^\dagger,\\
\mathrm{spec}(h_B)&=[\nu-2,\nu+2],\\
C_b&=f_b(h_B),\\
f_b(E)&=\frac{1}{1+e^{bE}},
\end{aligned}
```

where $`S|j\rangle=|j+1\rangle`$ on $`\ell^2(\mathbb N)`$. In the convention $`(C_b)_{jk}=\langle c_k^\dagger c_j\rangle_b`$, the sine transform gives

```math
(C_b)_{jk}
=\frac{2}{\pi}\int_0^\pi
\sin(jq)\sin(kq)\,
f_b(\nu-2\cos q)\,dq.
```

Let $`\rho_{b,R}`$ denote the actual reduced initial state of the first $`R`$ physical spins. It is a gauge-invariant fermionic Gaussian state with covariance

```math
C_{b,R}=P_R f_b(h_B)P_R,
```

where the compression is regarded as an operator on the first $`R`$ one-particle modes. The endpoint Jordan–Wigner transformation identifies their algebra with that of the first $`R`$ physical spins. This covariance description of the reduced density matrix follows from the Gaussian reconstruction formula [1], also derived in the [converse](locality_converse.md#thermal-distinguishability-of-the-actual-marginal).

In general, $`\rho_{b,R}`$ differs from the Gibbs state of an isolated $`R`$-site Hamiltonian. Correlations with the rest of the initial bath are retained in $`C_{b,R}`$.

## Operational resources

An experiment has two charged resources: an integer contact footprint $`r\ge1`$ and a hard elapsed-time budget $`\tau\ge0`$.

Every bath contact is confined to the fixed set of sites $`1,\ldots,r`$. Arbitrary controls may act jointly on those sites and on attached apparatus. All Hamiltonian terms whose bath support extends outside this set remain the specified bath terms. In particular, the bond between sites $`r`$ and $`r+1`$ has its fixed exchange strength $`J`$ throughout the experiment.

The apparatus can contain any finite number of sensors, quantum memories, control registers, and ancillary systems of any finite dimension. Its initial state is independent of $`b`$ and uncorrelated with the bath. Entanglement within the apparatus is allowed. Every operation is specified without knowledge of the true $`b`$; the protocol can depend on the known interval and model.

Within the contacted region, protocols can use time-dependent Hamiltonians of arbitrary strength, instantaneous gates and local instruments, resets into parameter-independent states, and feedback conditioned on earlier outcomes. In particular, an instantaneous measurement of the first $`r`$ bath sites is allowed at $`\tau=0`$; this convention makes the initial-block contribution to the all-time theorem explicit. Intervention times and a stopping time can depend on the record, provided elapsed time never exceeds $`\tau`$. A stopped protocol can preserve its output in isolated memory until the end of the budget.

The final data may include all classical outcomes, the entire time record, and an arbitrary joint measurement of the remaining accessible quantum systems. Keeping otherwise discarded environments only strengthens an experiment for the lower bound. Every outcome, including any outcome labelled unsuccessful, contributes to the risk.

Begin with finite experiments and include their operational limits: a limiting experiment is admissible when each finite final decision can be approximated by finite experiments with the same contact and time budgets, with the decision probabilities converging at each $`b`$. This gives a precise meaning to continuous monitoring and ideal arbitrarily fast local control. The converse is uniform in the approximating apparatus dimensions and intervention rates and passes directly to such limits. No continuity assumption about Fisher information is used.

There is one initially thermal reservoir. Sensor resets and additional apparatus do not supply fresh thermal samples. The contact footprint counts bath sites made directly accessible, rather than the number of probes attached to them.

## Loss, units, and minimax risk

Use the dimensionless log-temperature coordinate

```math
\begin{aligned}
\theta&=\log\!\left(\frac{k_BT}{J}\right)=-\log b,\\
\Theta&=[-\log b_+,-\log b_-].
\end{aligned}
```

All logarithms are natural. If $`\widehat b\in I`$ and $`\widehat T=J/(k_B\widehat b)`$, the loss is

```math
\ell(\widehat b,b)
=(\log\widehat b-\log b)^2
=\left[\log\!\left(\frac{\widehat T}{T}\right)\right]^2.
```

It is dimensionless and invariant under a change of temperature units. For small errors it equals squared relative temperature error to leading order. The reported resource law is a law for this mean squared loss; its square root is the corresponding root mean squared log-temperature error.

Write $`\mathfrak P(r,\tau)`$ for the allowed protocols, with every final measurement included in the protocol. The global minimax risk is

```math
\mathcal R(r,\tau)
=\inf_{\mathcal P\in\mathfrak P(r,\tau),\,\widehat b}
\ \sup_{b\in I}
\mathbb E_b^{\mathcal P}
\left[(\log\widehat b-\log b)^2\right].
```

Estimators can be clipped to $`I`$ without increasing this loss. The expectation includes the complete distribution of outcomes and any classical randomization used by the estimator. There is no unbiasedness or local estimation assumption.

It is convenient to prove intermediate bounds for

```math
\mathcal R_b(r,\tau)
=\inf_{\mathcal P,\,\widehat b\in I}
\ \sup_{b\in I}\mathbb E_b^{\mathcal P}
\left[(\widehat b-b)^2\right].
```

The mean-value theorem gives, pointwise on $`I`$,

```math
\frac{|\widehat b-b|}{b_+}
\le |\log\widehat b-\log b|
\le\frac{|\widehat b-b|}{b_-}.
```

Consequently,

```math
\frac{\mathcal R_b(r,\tau)}{b_+^2}
\le\mathcal R(r,\tau)
\le\frac{\mathcal R_b(r,\tau)}{b_-^2}.
```

## Theorem: optimal contact and time scaling

**Theorem.** Fix $`\nu>2`$ and $`0\lt b_-\lt b_+\lt\infty`$. Under the reservoir, control, and initial-state assumptions above, there are constants $`0\lt c\le C\lt\infty`$, depending only on $`\nu`$ and $`I`$, such that for every integer $`r\ge1`$ and every $`\tau\ge0`$,

```math
\boxed{
\frac{c}{r+\tau}
\le\mathcal R(r,\tau)
\le\frac{C}{r+\tau}.
}
```

The lower bound is uniform in the apparatus dimension, sensor number, number of interventions, and strength of all controls supported inside the accessible region. It applies to the complete output of every allowed protocol. The upper bound uses a measurement of total occupation in the accessible initial block or a single sensor with a fixed local counted reset, chosen according to the resource budget.

In physical units the denominator is $`r+Jt/\hbar`$. For a fixed footprint, the optimal mean squared log-temperature error is of order $`\hbar/(Jt)`$ at long times. The optimal root mean squared log-temperature error is of order $`\sqrt{\hbar/(Jt)}`$.

### Why the converse holds

Retain all records and dilate every intervention into a parameter-independent unitary. Combine the apparatus and the first $`r`$ bath spins into one boundary vertex. An interaction picture removes all dynamics internal to that vertex. The only remaining connection to the rest of the bath is a chain of exchange bonds with dimensionless norm one, regardless of internal control strength.

Deleting the bath bond beyond site $`R`$ then changes the complete accessible output by trace distance at most

```math
\exp\!\left[6e\tau-(R-r)\right].
```

Under the cut dynamics, the output is a parameter-independent channel of $`\rho_{b,R}`$. The actual local thermal states satisfy

```math
\begin{aligned}
D(\rho_{b,R}\Vert\rho_{b',R})
&\le K R(b-b')^2,\\
K&=\frac{(\nu+2)^2}{32\eta(1-\eta)},\\
\eta&=\frac{1}{1+e^{b_+(\nu+2)}}.
\end{aligned}
```

Choosing $`R=r+\lceil6e\tau+\log16\rceil`$ leaves a constant testing error between temperatures separated by order $`R^{-1/2}`$. A two-point decision argument yields the stated global minimax lower bound. The [complete proof](locality_converse.md) includes the locality estimate, the noncommuting covariance calculation, the thermodynamic and continuous-record limits, and an explicit value of $`c`$.

### Why the order is attainable

The [counted sensor construction](counted_sensor.md) couples one sensor to the endpoint and records local loss events. Its count has a mean whose inverse-temperature derivative grows linearly in $`\tau`$ and a variance bounded by a constant times $`\tau`$. Inverting the calibrated mean, with clipping to the known interval, gives worst-case mean squared error of order $`1/\tau`$ without preparing replacement bath states.

For short times relative to $`r`$, a measurement of total occupation of the first $`r`$ bath sites gives worst-case error of order $`1/r`$. Choosing the better of these two experiments gives the uniform $`1/(r+\tau)`$ bound. No assumption of independence between samples drawn at different times is required.

## Scope of the theorem

The positive one-particle band, $`\nu>2`$, makes occupation uniformly monotone in inverse temperature on the fixed compact interval. It is used by the explicit upper construction. The constants can deteriorate as the interval approaches zero temperature or as model parameters approach a limiting regime. The theorem makes no uniform claim in such limits.

The half-chain supplies an indefinitely growing spatial region. A reservoir of fixed finite length cannot support the same long-time upper law indefinitely. Moving a contact beyond the first $`r`$ sites, changing the bond that leaves the contacted region, or introducing temperature-dependent ancillary inputs changes the operational resources and falls outside the statement.

The result concerns global estimation risk. It does not assert a pointwise quantum Fisher-information bound obtained by differentiating a locality approximation.

## Reference

1. I. Peschel, “Calculation of reduced density matrices from correlation functions,” *Journal of Physics A: Mathematical and General* **36**, L205–L208 (2003). [DOI](https://doi.org/10.1088/0305-4470/36/14/101); [primary preprint](https://arxiv.org/abs/cond-mat/0212631). The covariance reconstruction applies to finite-temperature Gaussian states as well as their restrictions.
