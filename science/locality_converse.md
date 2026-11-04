# A complete-record locality converse

For the [model and operational resources](model_and_results.md), every thermometer confined to the first $`r`$ bath sites obeys a global minimax lower bound of order $`1/(r+\tau)`$. The proof bounds distinguishability of the entire accessible output, including all measurement records. It allows arbitrary apparatus dimension and arbitrary control strength within the contacted region.

Throughout, time is dimensionless, $`\tau=Jt/\hbar`$, inverse temperature is $`b=J/(k_BT)\in I=[b_-,b_+]`$, and logarithms are natural. Write

```math
\begin{aligned}
T(\rho,\sigma)&=\frac12\|\rho-\sigma\|_1,\\
D(\rho\Vert\sigma)&=\mathrm{tr}\,\rho(\log\rho-\log\sigma).
\end{aligned}
```

For classical outputs, $`T`$ is total variation distance. Operationally, it is the largest difference in probability of a binary output event. The same testing definition applies to limiting output records.

## Explicit lower-bound theorem

Define the positive constants

```math
\begin{aligned}
E_{\max}&=\nu+2,\\
\eta&=(1+e^{b_+E_{\max}})^{-1},\\
K&=\frac{E_{\max}^2}{32\eta(1-\eta)},\\
W&=b_+-b_-,\\
a&=\min\!\left\{\frac W2,\frac{1}{\sqrt{8K}}\right\},\\
v&=6e,\\
A&=v+\log16+1,\\
c_b&=\frac{5a^2}{64A},\\
c&=\frac{c_b}{b_+^2}.
\end{aligned}
```

**Theorem.** For every allowed protocol with contact footprint $`r\ge1`$, elapsed time at most $`\tau\ge0`$, and any estimator, the worst-case risks satisfy

```math
\begin{aligned}
\mathcal R_b(r,\tau)&\ge\frac{c_b}{r+\tau},\\
\mathcal R(r,\tau)&\ge\frac{c}{r+\tau}.
\end{aligned}
```

These constants are independent of apparatus dimension, number of probes, internal control strengths, intervention rates, and retained record size. They are deliberately conservative. The proof has three parts: a uniform truncation of the complete output, an extensive relative-entropy bound for the actual initial marginal, and a two-point testing reduction.

## Compressing an arbitrary adaptive experiment

Start with a bath of finite length $`L`$ and an experiment with a finite apparatus and finitely many interventions. Dilate each measurement and reset to a unitary on the accessible systems and an initially parameter-independent ancillary register. Retain every outcome register and every environment that would otherwise be discarded. A feedback operation becomes a fixed controlled unitary on these registers. Although the outcome probabilities depend on $`b`$, the controlled unitary itself does not.

All ancillary registers can be present at time zero and left inactive until needed. Enlarge the final accessible output to include the whole apparatus and the first $`r`$ bath spins. This can only improve the observer's ability to distinguish temperatures. Combine these systems into a single vertex $`0`$; vertex $`j\ge1`$ is physical bath site $`r+j`$.

Go to the interaction picture of the complete Hamiltonian internal to vertex $`0`$ and of the on-site bath terms at the other vertices. Instantaneous boundary gates are incorporated piecewise into the same local change of picture. The remaining Hamiltonian has the form

```math
\begin{aligned}
H(s)&=\sum_{j\ge0}v_j(s),\\
\mathrm{supp}\,v_j(s)&\subseteq\{j,j+1\},\\
\|v_j(s)\|&\le1.
\end{aligned}
```

The dimension of vertex $`0`$ may be arbitrarily large. Its internal Hamiltonian may be arbitrarily strong. Neither changes the displayed bound: the outgoing bath bond is conjugated by a local unitary, which preserves its norm and support. This is where the restriction to fixed bath contacts enters the proof.

For a Heisenberg propagator $`\alpha_{s,t}`$, define the local generators

```math
\begin{aligned}
\mathcal L_j(s)(O)&=i[v_j(s),O],\\
\|\mathcal L_j(s)\|_{\infty\to\infty}&\le2.
\end{aligned}
```

Each edge overlaps at most three edges, counting itself. The estimates below therefore depend only on these two numbers, and have no Hilbert-space dimension factor.

## A dimension-independent path estimate

This is a specialization of the time-dependent Lieb–Robinson argument. The original propagation principle is due to Lieb and Robinson [1]; an explicit time-dependent formulation and path proof appear in Barthel and Kliesch [2, Theorem 1 and Section V]. The short proof here states the precise estimate needed for the compressed boundary. It applies to the joint unitary dilation; no approximation of the bath by memoryless dynamics is involved.

Let $`O`$ be supported on vertex $`0`$. For an edge support $`X`$, let

```math
F_X(s)
=\sup_{\mathcal K_X\ne0}
\frac{\|\mathcal K_X\alpha_{s,t}(O)\|}
{\|\mathcal K_X\|},
```

where the supremum is over linear maps supported on $`X`$ that annihilate the identity, with their induced operator norm on the full finite system. In particular, local commutators and the generators $`\mathcal L_j(s)`$ belong to this class. Always $`F_X(s)\le\|O\|`$.

Split the generator into terms disjoint from $`X`$ and terms touching $`X`$. A map supported on $`X`$ commutes with the former terms. Variation of constants, followed by norm preservation of unitary Heisenberg evolution, gives

Equation (1).

```math
\begin{aligned}
F_X(s)
&\le F_X(t)\\
&\quad+\sum_{Y:\,Y\cap X\ne\varnothing}
\int_s^t\|\mathcal L_Y(u)\|\,F_Y(u)\,du.
\end{aligned}
```

For completeness, apply this to $`G(s)=\mathcal K_X\alpha_{s,t}(O)`$. Its differential equation contains the homogeneous term $`-\mathcal L_{\mathrm{disjoint}\,X}(s)G(s)`$ and the inhomogeneous terms $`-\mathcal K_X\mathcal L_Y(s)\alpha_{s,t}(O)`$ for edges touching $`X`$. The propagator of the homogeneous term has norm one. Dividing its integral equation by $`\|\mathcal K_X\|`$ and taking the supremum yields (1).

Now take $`X=\{d,d+1\}`$ with $`d\ge1`$. Iterating (1) produces paths of overlapping edges. A nonzero terminal term must meet vertex $`0`$, so it requires at least $`d`$ steps. There are at most $`3^n`$ paths of length $`n`$, each contributes at most $`2^n`$ from the generator norms, and its ordered time integrals have volume $`(t-s)^n/n!`$. The remainder vanishes because $`F_Y\le\|O\|`$ and this factorial dominates the bounded branching. Thus

Equation (2).

```math
\begin{aligned}
F_X(s)
&\le\|O\|\sum_{n\ge d}\frac{[6(t-s)]^n}{n!}\\
&\le\|O\|e^{6e(t-s)-d}.
\end{aligned}
```

The last inequality follows from $`1\le e^{n-d}`$ for $`n\ge d`$. It holds as well when an edge has been removed. For any Hermitian $`V_X`$ of norm at most one,

Equation (3).

```math
\begin{aligned}
\|[V_X,\alpha_{s,t}(O)]\|
&\le2\|O\|e^{v(t-s)-d},\\
v&=6e.
\end{aligned}
```

Only operator norms and the edge adjacency graph entered this derivation. Increasing the boundary Hilbert space, adding record registers, or increasing the removed internal Hamiltonian cannot increase $`v`$.

## Truncating the complete output

Choose an integer $`R\ge r+1`$ and delete only the bath bond between physical sites $`R`$ and $`R+1`$. Its compressed support is $`\{d,d+1\}`$, where $`d=R-r`$. Keep the initial bath state and every control operation unchanged. Denote the full and cut Heisenberg propagators by $`\alpha^{\mathrm f}`$ and $`\alpha^{\mathrm c}`$.

For any final boundary observable $`O`$, Duhamel's identity and (3) imply

Equation (4).

```math
\begin{aligned}
&\|\alpha^{\mathrm f}_{0,\tau}(O)
-\alpha^{\mathrm c}_{0,\tau}(O)\|\\
&\quad\le\int_0^\tau
\|[v_d(s),\alpha^{\mathrm c}_{s,\tau}(O)]\|\,ds\\
&\quad\le\frac{2}{v}(e^{v\tau}-1)e^{-(R-r)}\|O\|.
\end{aligned}
```

The same local interaction picture is used for both experiments, so the comparison is also valid in the physical picture. Let $`\sigma_b`$ and $`\sigma_{b,R}`$ be their complete final accessible states. Taking the supremum over all Hermitian boundary observables with norm at most one gives

Equation (5).

```math
\begin{aligned}
T(\sigma_b,\sigma_{b,R})
&\le\frac{e^{v\tau}-1}{v}\,e^{-(R-r)}\\
&\le e^{v\tau-(R-r)}.
\end{aligned}
```

This is a bound on the entire output state. It controls every joint measurement of the sensor, quantum memory, and full retained record, rather than one preselected observable. There is no record-size factor.

The initial Gibbs state generally has correlations across the deleted bond. Equation (4) is an operator-norm estimate and holds for that correlated state. In the cut experiment, all subsequent evolution on sites beyond $`R`$ is separate from the accessible part. Tracing out that tail therefore shows that

Equation (6).

```math
\sigma_{b,R}=\Lambda_R(\rho_{b,R}),
```

where $`\Lambda_R`$ is a channel independent of $`b`$ and includes the fixed initial apparatus state. Crucially, $`\rho_{b,R}`$ is the actual marginal of the initial bath, not the Gibbs state of the cut Hamiltonian.

### Infinite bath and continuous records

The finite-volume estimates are uniform in $`L`$. For the open finite chains, functional calculus gives convergence of every fixed compressed thermal covariance to $`P_R f_b(h_B)P_R`$. Wick's rule then gives convergence of each fixed finite spin density matrix. Applying the same distant-cut estimate to the finite-volume dynamics gives their norm limit on each fixed accessible observable. These two limits establish (5)–(6) for the half-chain.

For a continuous record or other operational limit, fix a finite final decision. By the definition of admissible limits in the [model](model_and_results.md#operational-resources), its outcome probabilities are limits of those from finite experiments with the same budgets. Every pairwise testing inequality below is uniform over those finite experiments and therefore passes to the limit. Taking the supremum over binary decisions gives the complete-record testing bound. This argument does not differentiate a small trace-distance error or invoke continuity of Fisher information.

## Thermal distinguishability of the actual marginal

The following estimate is the second load-bearing ingredient:

Equation (7).

```math
\begin{aligned}
D(\rho_{b,R}\Vert\rho_{b',R})
&\le K R(b-b')^2,\\
b,b'&\in I.
\end{aligned}
```

Although $`f_b(h_B)`$ and $`f_{b'}(h_B)`$ commute, their compressions need not commute. The proof of (7) keeps this distinction.

### Gaussian logarithms and relative entropy

For a gauge-invariant Gaussian state with covariance $`0\lt C\lt I`$, the density matrix is

Equation (8).

```math
\rho_C
=\det(I-C)\,
\exp\!\left[c^\dagger\log\!\big(C(I-C)^{-1}\big)c\right].
```

Here $`C_{ij}=\mathrm{tr}(\rho_C c_j^\dagger c_i)`$ and $`c^\dagger A c=\sum_{ij}c_i^\dagger A_{ij}c_j`$. Diagonalizing $`C`$ proves (8): in its natural mode basis the state is a product of occupations with probabilities equal to the eigenvalues of $`C`$. The same reconstruction follows from Wick's rule for a restricted Gaussian state [3].

Using $`\mathrm{tr}(\rho_C c^\dagger A c)=\mathrm{Tr}(AC)`$ in the difference of the two quadratic logarithms gives

Equation (9).

```math
\begin{aligned}
D(\rho_C\Vert\rho_D)
&=\mathrm{Tr}\!\Bigl[
C(\log C-\log D)\\
&\qquad+(I-C)(\log(I-C)-\log(I-D))
\Bigr].
\end{aligned}
```

Lowercase $`\mathrm{tr}`$ denotes the many-body trace and uppercase $`\mathrm{Tr}`$ the one-particle trace. Equation (9) does not assume that $`C`$ and $`D`$ commute.

Let $`g(x)=x\log x+(1-x)\log(1-x)`$ and $`\Phi(C)=\mathrm{Tr}\,g(C)`$. The right side of (9) is

Equation (10).

```math
\Phi(C)-\Phi(D)-\mathrm{Tr}[g'(D)(C-D)].
```

Suppose both covariances have spectrum in $`[\eta,1-\eta]`$. For a Hermitian perturbation $`X`$, diagonalize an intermediate covariance $`A`$ with eigenvalues $`\lambda_i`$. Differentiating the spectral function gives

```math
\mathrm D^2\Phi(A)[X,X]
=\sum_{i,j}g'^{[1]}(\lambda_i,\lambda_j)|X_{ij}|^2,
```

where the divided difference is $`[g'(x)-g'(y)]/(x-y)`$ for distinct arguments and $`g''(x)`$ on the diagonal. This formula also follows by differentiating $`\mathrm D\Phi(A)[X]=\mathrm{Tr}[g'(A)X]`$ in the eigenbasis of $`A`$. Because

```math
\begin{aligned}
g''(x)&=\frac{1}{x(1-x)}
\le\frac{1}{\eta(1-\eta)},\\
\eta&\le x\le1-\eta,
\end{aligned}
```

the scalar mean-value theorem bounds each divided difference by the same constant. Integrating the Hessian along $`D+s(C-D)`$ yields

Equation (11).

```math
D(\rho_C\Vert\rho_D)
\le\frac{\|C-D\|_F^2}{2\eta(1-\eta)}.
```

The factor $`1/2`$ is the integral of $`1-s`$ from zero to one. This establishes the needed noncommutative estimate directly.

### Applying the estimate to thermal covariances

Positivity of the band and the parameter interval give

```math
\begin{aligned}
\eta I&\le C_{b,R}\le\frac12 I\le(1-\eta)I,\\
\eta&=(1+e^{b_+(\nu+2)})^{-1}.
\end{aligned}
```

These inequalities follow first for $`f_b(h_B)`$ and then survive compression. On the full one-particle space,

```math
\begin{aligned}
\partial_b f_b(h_B)
&=-h_B f_b(h_B)[I-f_b(h_B)],\\
\|\partial_b f_b(h_B)\|&\le\frac{E_{\max}}4.
\end{aligned}
```

Compression is contractive in operator norm, so integration in $`b`$ gives

```math
\begin{aligned}
\|C_{b,R}-C_{b',R}\|
&\le\frac{E_{\max}}4|b-b'|,\\
\|C_{b,R}-C_{b',R}\|_F^2
&\le\frac{R E_{\max}^2}{16}(b-b')^2.
\end{aligned}
```

Combining this with (11) proves (7) with

```math
K=\frac{E_{\max}^2}{32\eta(1-\eta)}.
```

The entire calculation concerns the compressed covariance of the actual half-chain state. No approximation by a block Gibbs state has been made.

## Global minimax reduction

Fix the budget and choose

Equation (12).

```math
R=r+\left\lceil v\tau+\log16\right\rceil.
```

Equation (5) then gives a truncation error at most $`1/16`$ for each temperature. Let $`b_*=(b_-+b_+)/2`$ and choose

```math
\begin{aligned}
\delta&=\frac{a}{\sqrt R},\\
b_0&=b_*-\frac\delta2,\\
b_1&=b_*+\frac\delta2.
\end{aligned}
```

The choice $`a\le W/2`$ ensures that both points lie in $`I`$. Their separation depends on the resource budget and known model, and is the same for every controller. By (6), data processing, quantum Pinsker's inequality with natural logarithms, and (7),

```math
\begin{aligned}
T(\sigma_{b_0,R},\sigma_{b_1,R})
&\le T(\rho_{b_0,R},\rho_{b_1,R})\\
&\le\sqrt{\frac12D(\rho_{b_0,R}\Vert\rho_{b_1,R})}\\
&\le\sqrt{\frac{Ka^2}{2}}
\le\frac14.
\end{aligned}
```

Adding the two truncation errors gives the complete-output bound

Equation (13).

```math
\begin{aligned}
T(\sigma_{b_0},\sigma_{b_1})
&\le\frac14+\frac1{16}+\frac1{16}\\
&=\frac38.
\end{aligned}
```

To convert this to a risk bound, classify an estimate according to the nearer of $`b_0`$ and $`b_1`$. A wrong classification entails squared error at least $`\delta^2/4`$. The sum of error probabilities of any binary test is at least $`1-T(\sigma_{b_0},\sigma_{b_1})`$. Therefore every estimator satisfies

Equation (14).

```math
\begin{aligned}
&\max_{i=0,1}\mathbb E_{b_i}(\widehat b-b_i)^2\\
&\quad\ge\frac{\delta^2}{8}
\left[1-T(\sigma_{b_0},\sigma_{b_1})\right]\\
&\quad\ge\frac{5a^2}{64R}.
\end{aligned}
```

For clarity, the testing identity follows by writing the two errors of a test effect $`0\le M\le I`$ as $`\mathrm{tr}(\sigma_{b_0}M)+\mathrm{tr}(\sigma_{b_1}(I-M))`$ and using the variational characterization of trace distance. Thus no estimator regularity, local unbiasedness, or asymptotic normality is required.

Since $`r\ge1`$, (12) implies

```math
\begin{aligned}
R&\le r+v\tau+\log16+1\\
&\le A(r+\tau),\\
A&=v+\log16+1.
\end{aligned}
```

Taking the supremum over $`I`$ and then the infimum over protocols and estimators proves

```math
\mathcal R_b(r,\tau)
\ge\frac{5a^2}{64A(r+\tau)}.
```

After clipping an estimator to $`I`$, the pointwise inequality

```math
(\log\widehat b-\log b)^2
\ge\frac{(\widehat b-b)^2}{b_+^2}
```

gives the stated log-temperature lower bound. All unfavorable records are included in the expectation. Adaptivity and postselection cannot remove their contribution.

## What the proof establishes

The locality step limits the temperature information that can reach the complete accessible output during the elapsed time. The thermal step bounds distinguishability in the initial region of size $`R=O(r+\tau)`$. Their combination yields a global minimax statement even when the controller is large, fast, adaptive, and fully monitored.

The argument requires fixed bath bonds outside the contacted region and an initially parameter-independent apparatus. It also uses a fixed compact positive inverse-temperature interval to keep the covariance spectra away from zero and one. It makes no claim about a pointwise Fisher-information derivative of the full output. The [counted sensor construction](counted_sensor.md) establishes attainability for the positive-band model and completes the matching resource law.

## Primary references

1. E. H. Lieb and D. W. Robinson, “The finite group velocity of quantum spin systems,” *Communications in Mathematical Physics* **28**, 251–257 (1972). [DOI](https://doi.org/10.1007/BF01645779). Original finite-propagation estimate for local spin dynamics.
2. T. Barthel and M. Kliesch, “Quasi-locality and efficient simulation of Markovian quantum dynamics,” *Physical Review Letters* **108**, 230504 (2012). [DOI](https://doi.org/10.1103/PhysRevLett.108.230504); [primary preprint](https://arxiv.org/abs/1111.4210). Theorem 1 and Section V provide the time-dependent, operator-norm path framework. Its unitary specialization is sufficient here.
3. I. Peschel, “Calculation of reduced density matrices from correlation functions,” *Journal of Physics A: Mathematical and General* **36**, L205–L208 (2003). [DOI](https://doi.org/10.1088/0305-4470/36/14/101); [primary preprint](https://arxiv.org/abs/cond-mat/0212631). Gaussian density matrices are reconstructed from their restricted correlation matrices; equations (8)–(11) above give the relative-entropy calculation used here.
