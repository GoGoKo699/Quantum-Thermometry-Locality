# A counted boundary sensor attains the locality rate

One sensor spin, coupled with the bath hopping strength and reset at the fixed rate $`J/2`$, attains a worst-case squared log-temperature error of order $`(1+Jt)^{-1}`$. The bath is prepared thermally once. Only the sensor is reset. This page proves the count law, the continuing supply of detectable excitations, and the global estimator bound. The [model and theorem](model_and_results.md) specify the available controls; the [locality converse](locality_converse.md) proves that arbitrary apparatus at the same contact cannot improve the order.

The assumptions matter: the bath is a semi-infinite XX chain with known positive one-particle band, and $`b=\beta J`$ lies in a fixed compact interval $`B=[b_-,b_+]\subset(0,\infty)`$. Constants below depend on this interval and on the known band position. The proof does not give a uniform zero-temperature or gap-closing limit.

## 1. Apparatus and one-particle description

Use $`\hbar=k_B=1`$, dimensionless time $`\tau=Jt`$, and

```math
H_B/J=\nu\sum_{x\ge1}n_x
-\sum_{x\ge1}\bigl(\sigma_x^+\sigma_{x+1}^-+
\sigma_{x+1}^+\sigma_x^-\bigr),\qquad \nu\gt 2.
```

The one-particle bath Hamiltonian and thermal covariance are

```math
\begin{aligned}
h_B&=\nu I-S-S^*,\\
E_-&=\nu-2\gt 0,\quad E_+=\nu+2,\\
C_b&=f_b(h_B),\quad f_b(E)=\frac1{1+e^{bE}}.
\end{aligned}
```

The covariance convention is $`(C_b)_{xy}=\langle c_y^*c_x\rangle_b`$. The infinite-volume state is the gauge-invariant quasifree state specified by this covariance. Its local spin marginals are well defined by the Jordan–Wigner transformation starting at the physical endpoint.

Add a sensor spin at site $`0`$ in $`|0\rangle`$, with the same on-site energy and exchange coupling as the bath. Continuously count the sensor loss channel

```math
\ell=\sqrt\kappa\,\sigma_0^-,\qquad \kappa=\frac12,
```

where $`\kappa`$ is dimensionless; the physical reset rate is $`J/2`$. The master equation for sensor and bath is

```math
\frac{d\rho}{d\tau}
=-i[H/J,\rho]
\,+\,\ell\rho\ell^*-\frac12\{\ell^*\ell,\rho\}.
```

Every jump of this monitored channel is counted. The count through time $`\tau`$ is $`N_\tau`$. The channel is a known, temperature-independent vacuum reset resource belonging to the apparatus. No temperature-dependent Markov generator is assumed for the bath, which remains part of the microscopic evolution. No bath site is reset or replaced.

This continuous instrument is allowed in the operational closure of finite local instruments: successive vacuum ancillas can interact with the sensor and be measured, with the collision step tending to zero. It is an ideal continuous-monitoring statement. A claim about a particular nonzero detector cadence or an inefficient detector would require a further error analysis.

Let $`h`$ be the one-particle half-chain Hamiltonian on sites $`0,1,\ldots`$. Write $`P_0=|0\rangle\langle0|`$, $`P_B=I-P_0`$, and

```math
\begin{aligned}
K_\tau&=e^{(-ih-\kappa P_0/2)\tau},\\
L_\tau&=I-K_\tau^*K_\tau,\\
M_\tau&=P_B L_\tau P_B\big|_{\ell^2(\mathbb N)}.
\end{aligned}
```

Here $`L_\tau`$ denotes a one-particle loss operator, not the Lindblad generator or the jump operator. Contractivity gives $`0\le L_\tau\le I`$ and $`0\le M_\tau\le I`$. The initial combined covariance is $`C_b^{(0)}=0\oplus C_b`$.

## 2. The actual spin count has a determinant law

### Gaussian evolution in the even sector

Begin with a finite bath. Jordan–Wigner ordering starts at the sensor, so the physical spin jump is exactly $`\sigma_0^-=c_0`$, without a string. Nearest-neighbor exchange is a number-conserving quadratic fermion Hamiltonian. The unconditional channel preserves gauge-invariant Gaussian states and sends their covariance to

```math
C\longmapsto K_\tau C K_\tau^*.
```

One elementary way to check preservation is to split the evolution into quadratic Hamiltonian steps and pure sensor-loss steps. A sensor-loss step multiplies a normally ordered even correlation by $`e^{-\kappa s/2}`$ for each occurrence of the sensor index. Wick determinants therefore transform by the corresponding row and column factors. Hamiltonian steps rotate the one-particle covariance. The finite-dimensional Trotter limit preserves Wick's rule and gives the displayed covariance evolution. Thus no assertion about the Heisenberg evolution of odd fermion operators is needed. This is the quasi-free Lindblad structure treated more generally by [Barthel and Zhang](https://doi.org/10.1088/1742-5468/ac8e5c).

### Relate counted jumps to lost excitations

Let $`\widehat N`$ be total sensor-plus-bath excitation number and $`\mathcal E_\tau`$ the unconditional channel. The Hamiltonian and the no-jump evolution preserve $`\widehat N`$; each counted jump lowers it by one. Since the initial Gaussian state $`\rho(C)`$ commutes with $`\widehat N`$, trajectory expansion gives, for real $`z\gt 0`$,

```math
\mathbb E_C z^{N_\tau}
=\mathrm{Tr}\!\left[
z^{-\widehat N}\,
\mathcal E_\tau\!\left(z^{\widehat N}\rho(C)\right)
\right].
```

In an initial excitation sector $`n`$, a trajectory with $`k`$ jumps ends in sector $`n-k`$, and its weight on the right is $`z^n z^{-(n-k)}=z^k`$. This identity refers to the physical spin instrument. It does not posit a fermionic statistics law for the detector's emitted quanta.

Set

```math
D_z=I+(z-1)C,\qquad
C_z=zC D_z^{-1}.
```

The positive operator $`z^{\widehat N}\rho(C)`$ has trace $`\det D_z`$ and, after normalization, Gaussian covariance $`C_z`$. These identities follow by diagonalizing $`C`$ into independent occupation modes. The same diagonalization gives $`\mathrm{Tr}(u^{\widehat N}\rho(C'))=\det[I+(u-1)C']`$. Consequently,

```math
\begin{aligned}
\mathbb E_C z^{N_\tau}
&=\det D_z\,
\det\!\left[I+(z^{-1}-1)K_\tau C_z K_\tau^*\right]\\
&=\det\!\left[I+(z-1)(I-K_\tau^*K_\tau)C\right].
\end{aligned}
```

The last step uses $`\det(I+AB)=\det(I+BA)`$ and multiplication by $`D_z`$; it does not assume that $`C`$ commutes with $`K_\tau^*K_\tau`$. Both sides are finite polynomials, so the identity extends to all complex $`z`$. This trace-to-determinant method is part of the established fermionic counting formalism; see [Klich](https://arxiv.org/abs/cond-mat/0209642). Generalized-binomial counting is likewise established, for example in [Abanov and Ivanov](https://doi.org/10.1103/PhysRevB.79.205315). The specialization to the counted spin-reset protocol has been derived here.

For $`C=C_b^{(0)}`$, remove the initially empty sensor mode and symmetrize the determinant:

```math
\boxed{\begin{aligned}
\mathbb E_b z^{N_\tau}
&=\det\!\left[I+(z-1)Q_\tau(b)\right],\\
Q_\tau(b)&=C_b^{1/2}M_\tau C_b^{1/2}.
\end{aligned}}
```

The eigenvalues of $`Q_\tau(b)`$ are in $`[0,1]`$. The total count therefore has the law of a sum of Bernoulli variables with those eigenvalues as success probabilities. This is an auxiliary representation in occupation modes; the measured jump times need not be independent.

In particular,

```math
\begin{aligned}
\mu_\tau(b)&:=\mathbb E_bN_\tau=\mathrm{Tr}(C_bM_\tau),\\
\mathrm{Var}_b(N_\tau)
&=\mathrm{Tr}\bigl[Q_\tau(b)(I-Q_\tau(b))\bigr].
\end{aligned}
```

The positive band implies $`0\le C_b\le I/2`$, and hence

```math
\mathrm{Var}_b(N_\tau)
\le\mu_\tau(b)\le\frac12\mathrm{Tr}\,M_\tau.
```

### Infinite-volume count and moments

For every fixed $`\tau`$,

```math
\begin{aligned}
L_\tau&=\kappa\int_0^\tau
|K_s^*0\rangle\langle K_s^*0|\,ds,\\
\mathrm{Tr}\,L_\tau&\le\kappa\tau.
\end{aligned}
```

This is a positive trace-class operator: differentiate $`K_s^*K_s`$ and use $`\|K_s\|\le1`$. Thus $`M_\tau`$ and $`Q_\tau(b)`$ are trace class, and the infinite determinant is a well-defined Fredholm determinant.

There is also a direct limit from finite spin experiments. Truncate the bath after site $`n`$ and embed its one-particle vectors into the half-chain. Bounded finite-range generators imply $`K_{n,s}^*|0\rangle\to K_s^*|0\rangle`$, uniformly on a fixed compact time interval. Polynomial approximation of the exponentials proves this assertion directly. The rank-one integral above then gives $`L_{n,\tau}\to L_\tau`$ in trace norm. Finite-volume thermal covariances, extended by zero, converge strongly to $`C_b`$, by continuous functional calculus for the bounded one-particle Hamiltonians. Their norms are at most $`1/2`$. Strong convergence of their square roots, together with the trace-norm convergence of $`M_{n,\tau}`$, gives

```math
\|Q_{n,\tau}(b)-Q_\tau(b)\|_1\longrightarrow0.
```

Fredholm determinant continuity proves convergence of the count generating functions on the unit circle. Traces of $`Q`$ and $`Q^2`$ also converge. To identify this with the actual infinite spin experiment, construct its local dynamics as the thermodynamic limit of the finite spin channels. Each number-resolved Dyson term contains finitely many local jump insertions; the term with $`k`$ insertions is bounded by $`(\kappa\tau)^k/k!`$, so the finite-volume limit passes through the sum. At all times, the conditional jump intensity is at most $`\|\ell^*\ell\|=\kappa`$. A Poisson process of rate $`\kappa`$ therefore dominates the count, uniformly in bath length, giving convergence of all fixed count moments along with the local instrument limit. In particular, the displayed mean and variance are the physical infinite-volume moments. No infinite total bath-excitation observable or global thermal density matrix is required.

## 3. Linear extraction from the initially thermal half-chain

The required lower bound concerns how many independent one-particle loss channels become available, measured by $`\mathrm{Tr}\,M_\tau`$. It is independent of the unknown temperature.

Define the boundary amplitude and one-particle survival probability

```math
a_\kappa(s)=\langle0|K_s|0\rangle,
\qquad S_\kappa(s)=\|K_s|0\rangle\|^2.
```

Differentiating the norm gives

```math
S_\kappa(s)=1-\kappa\int_0^s|a_\kappa(u)|^2\,du.
```

The matrix $`h`$ is real symmetric and $`P_0`$ is diagonal. Hence $`K_s`$ is complex symmetric in the site basis, so its boundary row and column have equal squared norms. The loss trace is therefore

```math
\begin{aligned}
\mathrm{Tr}\,L_\tau
&=\kappa\int_0^\tau\|K_s^*|0\rangle\|^2ds\\
&=\kappa\int_0^\tau S_\kappa(s)\,ds.
\end{aligned}
```

### The free boundary return has finite squared integral

The sine transform diagonalizes the free half-chain. Its boundary spectral density is

```math
w(E)=\frac{\sqrt{4-(E-\nu)^2}}{2\pi}
\,\mathbf 1_{[\nu-2,\nu+2]}(E).
```

Indeed, the generalized eigenvectors at sites $`x=0,1,\ldots`$ are $`\sqrt{2/\pi}\sin((x+1)k)`$, with $`E=\nu-2\cos k`$, $`0\lt k\lt\pi`$. Changing variables in the boundary weight $`(2/\pi)\sin^2k\,dk`$ gives the stated density. Thus

```math
\begin{aligned}
a_0(s)&=\int w(E)e^{-iEs}\,dE,\\
\int_0^\infty|a_0(s)|^2ds
&=\pi\int w(E)^2dE
=\frac8{3\pi}.
\end{aligned}
```

The factor $`\pi`$ follows from full-line Fourier Plancherel and $`|a_0(-s)|=|a_0(s)|`$.

### Dissipation cannot increase that squared integral

For $`\Re\,z\gt 0`$, let $`A_\kappa(z)`$ be the Laplace transform of $`a_\kappa`$. The rank-one resolvent identity gives

```math
\begin{aligned}
A_\kappa(z)&=\frac{A_0(z)}{1+(\kappa/2)A_0(z)},\\
A_0(z)&=\int\frac{w(E)}{z+iE}\,dE.
\end{aligned}
```

Since $`\Re\,A_0(z)\ge0`$, the denominator has modulus at least one. Apply Fourier Plancherel on each vertical line $`z=x+iy`$, $`x\gt 0`$:

```math
\int_0^\infty e^{-2xs}|a_\kappa(s)|^2ds
\le\int_0^\infty e^{-2xs}|a_0(s)|^2ds.
```

Monotone convergence as $`x\downarrow0`$ yields

```math
\begin{aligned}
\int_0^\infty|a_\kappa(s)|^2ds&\le\frac8{3\pi},\\
S_\kappa(s)&\ge q_\kappa:=1-\frac{8\kappa}{3\pi}.
\end{aligned}
```

Fixing $`\kappa=1/2`$ gives $`q:=q_{1/2}=1-4/(3\pi)\gt 0`$. Finally, removing the initially vacuum sensor can reduce the loss trace by at most one:

```math
\boxed{\qquad
\kappa q\tau-1
\le\mathrm{Tr}\,M_\tau\le\kappa\tau,
\qquad \kappa=\frac12.
\qquad}
```

The lower bound can be negative at short times, when it is simply uninformative. At long times it proves a continuing linear supply from the same initially thermal half-chain. The proof uses the absolutely continuous half-chain spectral measure; it makes no corresponding all-time assertion for a fixed finite chain.

## 4. A global estimator, including biased outcomes

The positive band and compact temperature interval give a strictly positive susceptibility constant

```math
m:=\min_{\substack{b\in B\\E\in[E_-,E_+]}}
E f_b(E)(1-f_b(E))\gt 0.
```

For example, with $`\eta=f_{b_+}(E_+)`$, the explicit conservative choice $`m_0=E_-\eta(1-\eta)`$ also works in every bound below. Since

```math
-\partial_b C_b=h_BC_b(I-C_b)\ge mI,
```

and $`M_\tau`$ is positive, temperature independent, and trace class,

```math
\begin{aligned}
-\mu_\tau'(b)
&=\mathrm{Tr}\bigl[h_BC_b(I-C_b)M_\tau\bigr]\\
&\ge m\mathrm{Tr}\,M_\tau.
\end{aligned}
```

Differentiation under this trace is legitimate because the functional-calculus derivative is bounded uniformly on $`B`$. Neither $`C_b`$ nor its derivative needs to commute with $`M_\tau`$ for the inequality: the trace of the product of two positive operators is nonnegative.

Whenever $`\mathrm{Tr}\,M_\tau\gt 0`$, the calibrated mean $`\mu_\tau`$ is continuous and strictly decreasing. Define

```math
\widehat b_\tau
=\mu_\tau^{-1}\!\left(
\Pi_{[\mu_\tau(b_+),\,\mu_\tau(b_-)]}N_\tau
\right),
```

where $`\Pi`$ is projection onto the indicated interval. This assigns a valid estimate to every count, including those beyond the physically possible mean range. Projection cannot increase distance from the true mean, and the inverse mean is Lipschitz with constant $`(m\mathrm{Tr}\,M_\tau)^{-1}`$. Thus, for every $`b\in B`$,

```math
\begin{aligned}
\mathbb E_b(\widehat b_\tau-b)^2
&\le\frac{\mathbb E_b(N_\tau-\mu_\tau(b))^2}
{m^2(\mathrm{Tr}\,M_\tau)^2}\\
&\le\frac1{2m^2\mathrm{Tr}\,M_\tau}.
\end{aligned}
```

For $`\tau\ge\tau_0:=2/(\kappa q)`$, the trace lower bound gives

```math
\sup_{b\in B}\mathbb E_b(\widehat b_\tau-b)^2
\le\frac1{m^2\kappa q\tau}.
```

For $`0\le\tau\lt\tau_0`$, use the interval midpoint, whose squared error is at most $`(b_+-b_-)^2/4`$. This produces a single budget-dependent protocol and estimator with

```math
\sup_{b\in B}\mathbb E_b(\widehat b_\tau-b)^2
\le\frac{C_{\mathrm{inv}}}{1+\tau}
```

For example, one may choose

```math
C_{\mathrm{inv}}
=\max\!\left\{
\frac{(b_+-b_-)^2(1+\tau_0)}4,\,
\frac{1+\tau_0^{-1}}{m^2\kappa q}
\right\}.
```

This is finite and depends only on $`\nu`$ and $`B`$.

For the stated dimensionless temperature loss, set $`\theta=\log(T/J)=-\log b`$ and $`\widehat\theta=-\log\widehat b`$ in the chosen units $`k_B=1`$. Both inverse-temperature values belong to $`B`$, so

```math
\begin{aligned}
|\widehat\theta-\theta|
&\le b_-^{-1}|\widehat b-b|,\\
\sup_{b\in B}\mathbb E_b(\widehat\theta-\theta)^2
&\le\frac{C_{\mathrm{inv}}/b_-^2}{1+\tau}.
\end{aligned}
```

This is a finite-time worst-case risk bound. It requires no locally unbiased estimator, asymptotic normality, or quantum Fisher-information continuity. Calibration of $`\mu_\tau`$ uses only the known model; no claim of a particular computational cost for that calibration is made.

## 5. Spatial access and the joint law

The allowed model grants an ideal instantaneous instrument within the fixed initial block of $`r\ge1`$ bath spins. At time zero measure its occupation

```math
N_r=\sum_{x=1}^r n_x.
```

Its marginal covariance is $`C_{b,r}=P_rC_bP_r`$, the restriction of the actual initial half-chain state, rather than the Gibbs covariance of a chain cut after $`r`$. Its number statistics obey

```math
\begin{aligned}
\nu_r(b)&=\mathbb E_bN_r=\mathrm{Tr}(P_rC_bP_r),\\
\mathrm{Var}_b(N_r)
&=\mathrm{Tr}[C_{b,r}(I-C_{b,r})]\le\frac r4,
\end{aligned}
```

and

```math
-\nu_r'(b)
=\mathrm{Tr}[P_rh_BC_b(I-C_b)P_r]\ge mr.
```

The same clipped inverse-mean estimator has

```math
\sup_{b\in B}\mathbb E_b(\widehat b_r-b)^2
\le\frac1{4m^2r}.
```

Choose the initial block measurement when $`r\ge\tau`$ and the one-sensor count protocol when $`\tau\gt r`$. This decision depends only on the known budget. Since the larger of $`r`$ and $`\tau`$ is at least $`(r+\tau)/2`$, the resulting squared log-temperature risk is at most

```math
\frac{C}{r+\tau},\qquad
C=\frac{2}{b_-^2}
\max\!\left\{\frac1{4m^2},\,C_{\mathrm{inv}}\right\}.
```

There is no need to combine correlated block and count records. The spatial branch uses the model's permission to perform arbitrary operations on its contacted block. If block readout or moving probes carries an additional time cost, that is a different access model and this branch must be charged accordingly.

## 6. What the verification does and does not establish

[`check_counting.py`](../verification/check_counting.py) builds the finite spin Hamiltonian directly from Pauli raising and lowering matrices, prepares its exact many-body thermal density matrix, and solves the number-resolved spin Lindblad equation. It compares the complete count probability distribution with the one-particle determinant prediction. Its dynamical calculation never assumes Gaussian evolution or a fermionic output detector.

[`check_extraction.py`](../verification/check_extraction.py) compares boundary propagation at two bath lengths before reflections, verifies the mean susceptibility by finite differences, and checks the extraction and variance inequalities. It also includes a deliberately exhausted finite bath to show why the all-time linear extraction bound belongs to the half-chain. These reproducible numerical checks can catch sign, normalization, and finite-volume mistakes. The analytic spectral and trace-class arguments above establish the infinite-volume claims.

### Primary references for inherited ingredients

1. T. Barthel and Y. Zhang, *Solving quasi-free and quadratic Lindblad master equations for open fermionic and bosonic systems*, J. Stat. Mech. **2022**, 113101, [DOI](https://doi.org/10.1088/1742-5468/ac8e5c), [arXiv:2112.08344](https://arxiv.org/abs/2112.08344).
2. I. Klich, *Full Counting Statistics: An elementary derivation of Levitov's formula*, in *Quantum Noise in Mesoscopic Physics* (Kluwer, 2003), [published chapter](https://doi.org/10.1007/978-94-010-0089-5_19), [arXiv:cond-mat/0209642](https://arxiv.org/abs/cond-mat/0209642).
3. A. G. Abanov and D. A. Ivanov, *Factorization of quantum charge transport for non-interacting fermions*, Phys. Rev. B **79**, 205315 (2009), [DOI](https://doi.org/10.1103/PhysRevB.79.205315), [arXiv:0902.4151](https://arxiv.org/abs/0902.4151).
