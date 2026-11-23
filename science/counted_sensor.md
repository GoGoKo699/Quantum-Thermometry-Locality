# A counted boundary sensor attains the locality rate

One detuned sensor spin coupled to the bath endpoint and reset at the fixed rate $`J/(2\hbar)`$ attains worst-case squared log-temperature error of order $`(1+Jt/\hbar)^{-1}`$. The initially thermal bath is prepared once. Sections 2–4 derive the physical count law, prove a nonzero long-time thermal response, and construct the global estimator. The [model and theorem](model_and_results.md) specify the controls. The [locality converse](locality_converse.md) bounds the complete record of every thermometer at the same contact.

The bath is a semi-infinite XX chain with any fixed known field $`\nu\in\mathbb R`$. The inverse temperature $`b=\beta J`$ lies in a known compact interval $`B=[b_-,b_+]\subset(0,\infty)`$. Constants below depend on the interval and known model parameters.

## 1. Apparatus and one-particle description

Use $`\hbar=k_B=1`$, dimensionless time $`\tau=Jt`$, and

```math
H_B/J=\nu\sum_{x\ge1}n_x
-\sum_{x\ge1}\bigl(\sigma_x^+\sigma_{x+1}^-+
\sigma_{x+1}^+\sigma_x^-\bigr),\qquad \nu\in\mathbb R.
```

The one-particle bath Hamiltonian and thermal covariance are

```math
\begin{aligned}
h_B&=\nu I-S-S^*,\\
\mathrm{spec}(h_B)&=[\nu-2,\nu+2],\\
C_b&=f_b(h_B),\quad f_b(E)=\frac1{1+e^{bE}}.
\end{aligned}
```

The covariance convention is $`(C_b)_{xy}=\langle c_y^*c_x\rangle_b`$. The infinite-volume state is the gauge-invariant quasifree state specified by this covariance. Its local spin marginals are well defined by the Jordan–Wigner transformation starting at the physical endpoint.

Add a sensor spin at site $`0`$ in $`|0\rangle`$. Use exchange coupling $`J`$ on the sensor bond and detune the sensor energy from $`\nu J`$ to $`(\nu+d)J`$. The fixed choice $`d=1/2`$ for $`\nu\ge0`$ and $`d=-1/2`$ for $`\nu\lt 0`$ suffices. Continuously count the sensor loss channel

```math
\ell=\sqrt\kappa\,\sigma_0^-,\qquad \kappa=\frac12,
```

Here $`\kappa`$ is dimensionless. The argument works for any fixed $`\kappa>0`$ and the displayed choice gives physical reset rate $`J/(2\hbar)`$. The master equation for sensor and bath is

```math
\frac{d\rho}{d\tau}
=-i[H/J,\rho]
\,+\,\ell\rho\ell^*-\frac12\{\ell^*\ell,\rho\}.
```

Every jump of this monitored channel is counted. The count through time $`\tau`$ is $`N_\tau`$. The channel is a known, temperature-independent vacuum reset resource belonging to the apparatus. No temperature-dependent Markov generator is assumed for the bath, which remains part of the microscopic evolution. No bath site is reset or replaced.

This continuous instrument is allowed in the operational closure of finite local instruments: successive vacuum ancillas can interact with the sensor and be measured, with the collision step tending to zero. It is an ideal continuous-monitoring statement. A claim about a particular nonzero detector cadence or an inefficient detector would require a further error analysis.

Let $`h_0=\nu I-S-S^*`$ denote the matched one-particle half-chain Hamiltonian on sites $`0,1,\ldots`$. Write $`P_0=|0\rangle\langle0|`$, $`P_B=I-P_0`$, and

```math
\begin{aligned}
h_d&=h_0+dP_0,\\
K_\tau&=e^{(-ih_d-\kappa P_0/2)\tau},\\
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

For every field, $`0\le C_b\le I`$, which gives

```math
\mathrm{Var}_b(N_\tau)
\le\mu_\tau(b)\le\mathrm{Tr}\,M_\tau\le\kappa\tau.
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

There is also a direct limit from finite spin experiments. Truncate the bath after site $`n`$ and embed its one-particle vectors into the half-chain. Bounded finite-range generators imply $`K_{n,s}^*|0\rangle\to K_s^*|0\rangle`$, uniformly on a fixed compact time interval. Polynomial approximation of the exponentials proves this assertion directly. The rank-one integral above then gives $`L_{n,\tau}\to L_\tau`$ in trace norm. Finite-volume thermal covariances, extended by zero, converge strongly to $`C_b`$, by continuous functional calculus for the bounded one-particle Hamiltonians. Their norms are at most $`1`$. Strong convergence of their square roots, together with the trace-norm convergence of $`M_{n,\tau}`$, gives

```math
\|Q_{n,\tau}(b)-Q_\tau(b)\|_1\longrightarrow0.
```

Fredholm determinant continuity proves convergence of the count generating functions on the unit circle. Traces of $`Q`$ and $`Q^2`$ also converge. To identify this with the actual infinite spin experiment, construct its local dynamics as the thermodynamic limit of the finite spin channels. Each number-resolved Dyson term contains finitely many local jump insertions; the term with $`k`$ insertions is bounded by $`(\kappa\tau)^k/k!`$, so the finite-volume limit passes through the sum. At all times, the conditional jump intensity is at most $`\|\ell^*\ell\|=\kappa`$. A Poisson process of rate $`\kappa`$ therefore dominates the count, uniformly in bath length, giving convergence of all fixed count moments along with the local instrument limit. In particular, the displayed mean and variance are the physical infinite-volume moments. No infinite total bath-excitation observable or global thermal density matrix is required.

## 3. Linear extraction from the initially thermal half-chain

The useful quantity is the **temperature response** of the mean count. A linear number of detected excitations gives a linear variance budget, while a linear derivative of the mean lets us make that count into a thermometer.

Write $`g_b(E)=E f_b(E)[1-f_b(E)]`$. The initial sensor is vacuum, so the derivative of the mean uses the operator $`G_b=0\oplus g_b(h_B)`$. The loss integral gives

```math
-\mu_\tau'(b)
=\mathrm{Tr}(L_\tau G_b)
=\kappa\int_0^\tau \langle u_s,G_bu_s\rangle\,ds,
\qquad u_s=K_s^*|0\rangle.
```

Differentiation is legitimate because the functional-calculus derivative of $`f_b(h_B)`$ is uniformly bounded on $`B`$, and $`L_\tau`$ is trace class.

### The undetuned count at zero field

For $`\nu=d=0`$, let $`\Theta`$ conjugate the site amplitudes and multiply the amplitude at site $`j`$ by $`(-1)^j`$. This antiunitary fixes the sensor endpoint, reverses $`h_0`$, and leaves $`P_0`$ fixed. Conjugating $`i`$ contributes a second minus sign, so $`\Theta`$ commutes with $`K_s^*`$ and fixes $`u_s`$. Since $`g_b`$ is odd, $`\Theta G_b\Theta^{-1}=-G_b`$. The integrand above is real and equals its own negative, so $`\mu_\tau'(b)=0`$ at every elapsed time. This is a statement about the mean of the cumulative count. Higher moments and the jump times are separate statistics.

### Detuned thermal response at any known field

**Separate the vacuum preparation from the spectral calculation.** The operator $`h_{\mathrm{cut}}=\nu P_0\oplus h_B`$ differs from $`h_0`$ by the rank-two coupling across the sensor bond. Take a contour enclosing both real spectra with imaginary parts of magnitude strictly less than $`\pi/b_+`$. Let $`\ell_{\mathrm c}`$ be its length, $`M_g`$ a uniform bound on the analytic functions $`g_b(z)`$ there for $`b\in B`$, and $`M_R`$ a common bound on the two resolvent norms. The resolvent identity gives

```math
\sup_{b\in B}\|g_b(h_0)-g_b(h_{\mathrm{cut}})\|_1
\le\frac{\ell_{\mathrm c}}{2\pi}\,
\|h_0-h_{\mathrm{cut}}\|_1 M_g M_R^2
\lt\infty.
```

Removing the single entry $`g_b(\nu)P_0`$ from $`g_b(h_{\mathrm{cut}})`$ gives $`G_b`$. Therefore replacing $`G_b`$ by $`g_b(h_0)`$ in $`\mathrm{Tr}(L_\tau G_b)`$ changes the result by at most a constant independent of $`\tau`$ and $`b`$. This estimate uses $`0\le L_\tau\le I`$ and keeps the actual vacuum-sensor preparation in the experiment.

**Compute the continuum response.** Let $`c=d+i\kappa/2`$. Then $`u_s=e^{i(h_0+cP_0)s}|0\rangle`$. The boundary amplitude $`a(s)=\langle0|u_s\rangle`$ satisfies

```math
\frac{d}{ds}\|u_s\|^2=-\kappa |a(s)|^2,
\qquad \int_0^\infty |a(s)|^2\,ds\le\kappa^{-1}.
```

The free half-chain sine transform gives the endpoint spectral density

```math
w_\nu(E)=\frac{\sqrt{4-(E-\nu)^2}}{2\pi},
\qquad E\in[\nu-2,\nu+2],
```

with zero weight outside the band. In the spectral representation of $`h_0`$ with cyclic vector $`|0\rangle`$, that vector is the constant function $`1`$. Duhamel's formula represents $`e^{-ih_0s}u_s`$ by

```math
v_s(E)=1+ic\int_0^s e^{-iEu}a(u)\,du.
```

The integral is the Fourier transform of a truncated square-integrable function. Plancherel's identity gives convergence as $`s\to\infty`$ in ordinary $`L^2`$ for this integral and then in $`L^2(w_\nu(E)\,dE)`$ because $`w_\nu`$ is bounded. Replacing the sharp time cutoff by multiplication by $`e^{-\epsilon u}`$ produces the same limit in the two norms as $`\epsilon\downarrow0`$.

Define $`m_0(z)=\langle0|(z-h_0)^{-1}|0\rangle`$. For $`z=E-i\epsilon`$, the Abel-regularized integral above is $`-i\langle0|(z-h_0-cP_0)^{-1}|0\rangle`$, by the Laplace integral of the contraction semigroup. The rank-one resolvent identity gives $`m_0(z)/(1-cm_0(z))`$ for the matrix element. Thus the Abel-regularized version of $`v_s`$ is $`1/(1-cm_0(E-i\epsilon))`$. Cutting the free chain after site 0 gives $`m_0(z)=[z-\nu-m_0(z)]^{-1}`$, where the branch is fixed by $`m_0(z)\sim 1/z`$ at infinity. Inside the band,

```math
m_0(E-i0)=\frac{x+iy}{2},
\qquad x=E-\nu,\quad y=\sqrt{4-x^2}.
```

In particular $`|m_0(E-i0)|=1`$, and

```math
\begin{aligned}
D(E)&=|1-cm_0(E-i0)|^2\\
&=1+d^2+\kappa^2/4-dx+(\kappa/2)y.
\end{aligned}
```

The denominator is strictly positive since $`1+d^2-dx\ge(1-|d|)^2`$ and $`\kappa\gt 0`$. Pointwise Abel limits therefore identify the $`L^2(w_\nu\,dE)`$ limit $`v_\infty`$ by the same boundary formula. As $`g_b(h_0)`$ commutes with the free evolution,

```math
\langle u_s,g_b(h_0)u_s\rangle
=\int g_b(E)|v_s(E)|^2w_\nu(E)\,dE
\longrightarrow
\int g_b(E)\frac{w_\nu(E)}{D(E)}\,dE
```

uniformly in $`b`$. Indeed $`\|v_s\|_{L^2(w_\nu)}\le1`$ by contractivity, and the difference of the quadratic forms is bounded by
$`\sup_{b\in B}\|g_b(h_0)\|\,\|v_s-v_\infty\|_{L^2(w_\nu)}(\|v_s\|_{L^2(w_\nu)}+\|v_\infty\|_{L^2(w_\nu)})`$. Averaging in time and using the preparation bound gives the uniform limiting count slope

```math
\boxed{
\lim_{\tau\to\infty}\frac{-\mu_\tau'(b)}{\tau}
=\kappa\int_{\nu-2}^{\nu+2}
g_b(E)\frac{w_\nu(E)}{D(E)}\,dE.
}
```

### Strict temperature response

For $`\nu\ge0`$, choose $`d\gt 0`$. The weight $`w_\nu(E)/D(E)`$ inside the band is proportional to $`y/(A-dx+(\kappa/2)y)`$, with $`A=1+d^2+\kappa^2/4`$. It increases in $`x`$ and in $`y`$ separately for $`|x|\le2`$ and $`y\ge0`$, using $`A-dx\gt 0`$. If $`E\gt 0`$ and both $`E`$ and $`-E`$ are in the band, then $`x(E)\gt x(-E)`$ and $`y(E)\ge y(-E)`$. The weight at $`E`$ is strictly larger in the interior. This remains true for a pair with only its positive member in the band, and a pair with only its negative member in the band cannot occur. Since $`g_b`$ is odd and positive for $`E\gt 0`$, the limiting slope is strictly positive. For $`\nu\lt 0`$ and $`d\lt 0`$, reflecting $`E,\nu,d`$ reverses the slope. The conclusion holds for every fixed positive reset rate. Continuity on $`B`$ and uniform convergence give constants $`s_*\gt 0`$ and finite $`\tau_0`$, determined by the known model, such that $`|\mu_\tau'(b)|\ge s_*\tau`$ with a fixed sign for all $`b\in B`$ and $`\tau\ge\tau_0`$.

## 4. A global estimator, including biased outcomes

For $`\tau\ge\tau_0`$ the mean $`\mu_\tau`$ is strictly monotone on $`B`$. Project the observed count to the interval $`\mu_\tau(B)`$ and invert the calibrated mean:

```math
\widehat b_\tau
=\mu_\tau^{-1}\!\left(\Pi_{\mu_\tau(B)}N_\tau\right).
```

Projection cannot increase the distance to $`\mu_\tau(b)`$. The inverse mean has Lipschitz constant at most $`(s_*\tau)^{-1}`$, and the count variance is at most $`\kappa\tau`$ by Section 2. Hence

```math
\sup_{b\in B}\mathbb E_b(\widehat b_\tau-b)^2
\le\frac{\kappa}{s_*^2\tau}.
```

At shorter times use the midpoint of $`B`$, with squared error at most $`(b_+-b_-)^2/4`$. The resulting worst-case squared inverse-temperature error is bounded by $`C_{\mathrm{inv}}/(1+\tau)`$ for a finite constant $`C_{\mathrm{inv}}`$. Since $`|\log\widehat b-\log b|\le b_-^{-1}|\widehat b-b|`$ for estimates in $`B`$, the same order holds in log temperature. The estimate accounts for every outcome. The model determines the calibration curve, and this proof places no computational bound on its evaluation.

## 5. Spatial access and the joint law

For the spatial branch, measure the dimensionless block energy $`\mathrm d\Gamma(A_r)=\sum_{jk}(A_r)_{jk} c_j^\dagger c_k`$, where $`A_r=P_r h_B P_r`$ acts on the first $`r`$ sites. This is a physical observable on the contacted block, with its onsite terms and its internal exchange bonds. The initial block state has the actual compressed covariance $`C_{b,r}=P_r f_b(h_B)P_r`$. By the Gaussian two- and four-point formulas, the mean $`e_r(b)`$ and variance obey

```math
\begin{aligned}
e_r(b)&=\mathrm{Tr}(A_r C_{b,r}),\\
\mathrm{Var}_b(\mathrm d\Gamma(A_r))
&=\mathrm{Tr}\!\big[C_{b,r} A_r(I-C_{b,r})A_r\big]
\le \mathrm{Tr}(A_r^2)\le r(|\nu|+2)^2.
\end{aligned}
```

The trace formula for the variance follows by Wick contraction. Its first inequality follows by writing the trace as the squared Hilbert–Schmidt norm of $`(I-C_{b,r})^{1/2}A_r C_{b,r}^{1/2}`$ and using that both covariance factors are contractions.

To bound the slope, let $`m_*=\min_{b\in B,\ E\in[\nu-2,\nu+2]} f_b(E)[1-f_b(E)]\gt 0`$. Then $`h_Bg_b(h_B)\ge m_*h_B^2`$. Inserting $`P_r+(I-P_r)`$ between $`h_B`$ and $`g_b(h_B)`$ gives

```math
\begin{aligned}
-e_r'(b)
&=\mathrm{Tr}(A_r P_r g_b(h_B)P_r)\\
&\ge m_*\mathrm{Tr}(P_r h_B^2 P_r)
-\big|\mathrm{Tr}\big(P_r h_B(I-P_r)g_b(h_B)P_r\big)\big|\\
&\ge m_*[r(\nu^2+2)-1]-\|g_b(h_B)\|.
\end{aligned}
```

The omitted trace crosses only the rank-one bond term $`P_r h_B(I-P_r)=-|r\rangle\langle r+1|`$, of trace norm one. The diagonal of $`h_B^2`$ counts one hopping neighbor at the physical endpoint and two elsewhere. Thus for all sufficiently large $`r`$, the derivative magnitude is bounded below by a positive constant times $`r`$, uniformly in $`b`$. The same clipped inverse-mean estimator gives worst-case squared error at most $`C_{\rm sp}/r`$ in $`b`$. A midpoint estimate covers the bounded set of smaller blocks, including a single site at zero field.

Choose the block measurement for $`r\ge\tau`$, or the one-sensor count when $`\tau\gt r`$. Each branch depends only on the known budget. Converting to log temperature gives the joint risk bound

```math
\frac{C}{r+\tau},
\qquad C=\frac{2}{b_-^2}\max\{C_{\rm sp},C_{\rm inv}\}.
```

The spatial branch uses the model's allowance for an instantaneous joint operation within the contacted block. A separate time charge for the block measurement would define a different access model.

## 6. What the verification does and does not establish

[`check_counting.py`](../verification/check_counting.py) builds the finite spin Hamiltonian directly from Pauli raising and lowering matrices, prepares its exact many-body thermal density matrix, and solves the number-resolved spin Lindblad equation. It compares the complete count probability distribution with the one-particle determinant prediction. Its dynamical calculation never assumes Gaussian evolution or a fermionic output detector.

[`check_detuned_response.py`](../verification/check_detuned_response.py) compares finite-chain evolution with the continuum count slope over several fields, temperatures, and reset rates. It checks the zero-field cancellation and the sign of the restored response. [`check_extraction.py`](../verification/check_extraction.py) retains the original positive-band benchmark, including a finite bath that exhausts its initial supply. These calculations check signs, normalization, and the finite-volume implementation. The analytic spectral and trace-class arguments above establish the infinite-volume statements.

### Primary references for inherited ingredients

1. T. Barthel and Y. Zhang, *Solving quasi-free and quadratic Lindblad master equations for open fermionic and bosonic systems*, J. Stat. Mech. **2022**, 113101, [DOI](https://doi.org/10.1088/1742-5468/ac8e5c), [arXiv:2112.08344](https://arxiv.org/abs/2112.08344).
2. I. Klich, *Full Counting Statistics: An elementary derivation of Levitov's formula*, in *Quantum Noise in Mesoscopic Physics* (Kluwer, 2003), [published chapter](https://doi.org/10.1007/978-94-010-0089-5_19), [arXiv:cond-mat/0209642](https://arxiv.org/abs/cond-mat/0209642).
3. A. G. Abanov and D. A. Ivanov, *Factorization of quantum charge transport for non-interacting fermions*, Phys. Rev. B **79**, 205315 (2009), [DOI](https://doi.org/10.1103/PhysRevB.79.205315), [arXiv:0902.4151](https://arxiv.org/abs/0902.4151).
