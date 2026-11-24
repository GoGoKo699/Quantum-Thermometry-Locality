# The low-temperature scale for local thermometry

A cold gapless chain carries temperature information in a narrow band around the Fermi energy. A spatial thermometer can resolve the band by measuring a large enough region. With one fixed contact, an auxiliary chain can collect energy-selective wave packets over time.

## Uniform minimax law

Use the [XX half-chain and operational resources](model_and_results.md), with fixed known field $`|\nu|<2`$, dimensionless inverse temperature $`b=J/(k_{\mathrm B}T)`$ and elapsed time $`\tau=Jt/\hbar`$. The bath is prepared once at an unknown $`b\in[B,2B]`$, with $`B`$ known to the experimenter. The risk is the worst-case mean squared error for $`\log b`$, minimized over all allowed fixed-contact protocols and estimators.

**Theorem.** For each fixed $`|\nu|<2`$ there are positive constants $`B_0,c,C`$ depending only on the field. For $`B\ge B_0`$, integer $`r\ge1`$ and $`\tau\ge0`$,

```math
\begin{aligned}
c\min\{1,B/(r+\tau)\}
&\le \mathcal R_{[B,2B]}(r,\tau)\\
&\le C\min\{1,B/(r+\tau)\}.
\end{aligned}
```

The inequalities hold when the temperature, footprint and time vary together. The lower bound covers the complete output of arbitrary admissible adaptive experiments. The upper bound uses an immediate spatial readout or an auxiliary XX lead connected to one bath site. The lead is initially in vacuum and its length scales with the time budget. Its terminal mode measurement uses the instantaneous internal readout permitted in the model.

At one fixed contact, attaining a fixed sufficiently small relative error takes time of order $`\hbar/(k_{\mathrm B}T)`$. With spatial access alone, the footprint instead has order $`J/(k_{\mathrm B}T)`$. Clipping estimates to the known octave makes squared relative error comparable to squared log error.

## Converse

### Temperature information in the initial marginal

Write $`C_{b,R}=P_R f_b(h_B)P_R`$ for the covariance of the actual initial marginal on the first $`R`$ sites, with $`f_b(E)=(1+e^{bE})^{-1}`$. Let $`A_E\,dE=P_R\,d\Pi_E\,P_R`$ be the compressed spectral measure of the one-particle bath Hamiltonian. The sine transform gives $`\int A_E\,dE=I_R`$ and

```math
\begin{aligned}
C_{b,R}&=\int f_b(E)A_E\,dE,\\
I_R-C_{b,R}&=\int [1-f_b(E)]A_E\,dE,\\
\mathrm{Tr}A_E
&\le \frac{2R}{\pi\sqrt{4-(E-\nu)^2}},\qquad |E-\nu|<2.
\end{aligned}
```

The last line follows by bounding each squared sine by one. The compressed covariances at two temperatures can fail to commute. To handle them, use the [Gaussian relative entropy identity](locality_converse.md#gaussian-logarithms-and-relative-entropy) and the generalized matrix relative entropy

```math
\mathfrak D(X\Vert Y)=
\mathrm{Tr}[X(\log X-\log Y)-X+Y].
```

The trace terms cancel across the two complementary covariance blocks. The functional is jointly convex and homogeneous. On the common support of positive scalar multiples of a matrix $`A`$ it satisfies $`\mathfrak D(aA\Vert a'A)=\mathrm{Tr}(A)[a\log(a/a')-a+a']`$. Applying these facts to the two spectral integrals yields

```math
D(\rho_{b,R}\Vert \rho_{b',R})
\le \int \mathrm{Tr}(A_E)
\,D_{\rm Ber}\big(f_b(E)\Vert f_{b'}(E)\big)\,dE .
```

One can apply the inequality first to positive spectral bins and take their mesh to zero. For finite $`b,b'`$ the limiting covariances and their complements are positive definite.

The Bernoulli log-partition function $`g(u)=\log(1+e^u)`$ has second derivative at most $`e^{-|u|}`$. The natural parameters $`-bE`$ and $`-b'E`$ have the same sign and magnitude at least $`B|E|`$ throughout their connecting segment. Taylor's integral remainder and $`|b-b'|\le 2B|\log(b/b')|`$ give

```math
D_{\rm Ber}\big(f_b(E)\Vert f_{b'}(E)\big)
\le 2(BE)^2e^{-B|E|}\,|\log(b/b')|^2.
```

In a neighborhood of zero strictly inside the band, the spectral density is bounded by a field-dependent constant times $`R`$. The integral of the thermal factor there is $`O(1/B)`$ by rescaling $`E`$. On the rest of the band that factor is exponentially small, while the spectral density has total mass $`R`$. Thus

```math
D(\rho_{b,R}\Vert \rho_{b',R})
\le C_\nu\frac{R}{B}|\log(b/b')|^2.
```

### From the marginal to the complete experiment

Use the [complete-record truncation](locality_converse.md#truncating-the-complete-output) with $`R=r+\lceil 6e\tau+\log 16\rceil`$. Cutting the far bond changes the output of either hypothesis by trace distance at most $`1/16`$. The cut output is a parameter-independent channel of the actual initial marginal. Data processing and Pinsker's inequality bound the distance of the two cut outputs by $`\sqrt{D(\rho_{b,R}\Vert \rho_{b',R})/2}`$.

Take $`b=B`$ and $`b'=Be^\delta`$, with $`\delta=a\min\{1,\sqrt{B/R}\}`$ and a sufficiently small fixed $`a\le\log 2`$. The two complete outputs have trace distance at most $`1/2`$. An estimator induces a test by choosing the nearest log temperature. A wrong decision incurs squared error at least $`\delta^2/4`$, and at least one hypothesis has error probability at least $`1/4`$. Thus the risk is at least $`\delta^2/16`$. Since $`R`$ is comparable to $`r+\tau`$ for $`r\ge1`$, this proves the lower bound for every budget, including operational limits of finite experiments.

## Attaining receiver

### Energy-selective packets

On the full line, the one-particle dispersion and group velocity are $`E(k)=\nu-2\cos k`$ and $`v(k)=2\sin k`$. For sufficiently large $`B`$, choose the left-moving carrier $`k_*`$ with $`E(k_*)=1/B`$. Its velocity $`v_*=v(k_*)<0`$ has magnitude bounded below by a positive field-dependent constant. Use the packet

```math
\psi(j)=
\sqrt{\frac{2}{L+1}}\sin\!\left(\frac{\pi(j-a)}{L+1}\right)
e^{ik_*j},\qquad a\lt j\le a+L ,
```
zero elsewhere, with $`L=\lceil KB\rceil`$. The first difference of the zero-padded normalized envelope has norm $`2\sin(\pi/(2(L+1)))`$. Applying the shift and its adjoint gives

```math
\begin{aligned}
\Vert(h-1/B)\psi\Vert &\le \frac{2\pi}{L+1},\\
\Vert(v-v_*)\psi\Vert &\le \frac{2\pi}{L+1},
\end{aligned}
```
where $`h`$ is the full-line Hamiltonian and $`v`$ acts by multiplication in Fourier coordinates. For $`\mathcal I_B=[1/(2B),3/(2B)]`$, the norm outside the band is at most $`4\pi B/(L+1)`$.

For a packet supported in the bath, use the odd extension $`Uq=(q-\mathscr Rq)/\sqrt 2`$, where $`\mathscr R`$ reflects about site zero and the initial $`q`$ is extended by zero. This is the isometry from the half-line to the odd subspace of the full-line chain. It intertwines the half-line Hamiltonian and the full-line Hamiltonian on that subspace. Since reflection commutes with energy projections, the half-line off-band norm is at most $`\sqrt 2`$ times the full-line off-band norm of the zero-extended packet.

### One-site temporal readout

Attach an auxiliary XX lead on sites $`0,-1,\ldots`$ with the bath field and hopping, prepare it in vacuum, and switch on the matched exchange bond between sites zero and one. First calculate with an infinite lead. At time $`\tau`$, select disjoint output packets with centers $`x`$ in the interval $`[v_*\tau/2,v_*\tau/4]`$. For $`\tau`$ at least a sufficiently large field-dependent multiple of $`L`$, there are at least a constant times $`\tau/L`$ packets, wholly within the lead.

The backward evolution $`\phi=e^{ih\tau}\psi`$ obeys the exact Fourier position identity

```math
\Vert(X-x+\tau v_*)\phi\Vert
\le L+\frac{2\pi\tau}{L+1},
```
where $`X`$ is position. In Fourier coordinates, differentiation of $`e^{ih\tau}`$ contributes $`-\tau v(k)`$ to $`X`$. The backward packet center $`x-\tau v_*`$ is at least $`|v_*|\tau/2`$. For $`q=P_{j\ge1}\phi`$, the norm lost outside the bath is at most $`2(L+2\pi\tau/(L+1))/(|v_*|\tau)`$. Full-line evolution preserves the energy concentration. The half-line energy bound follows after compression by reflecting the bath component:

```math
\Vert\Pi_{\rm out}Uq\Vert
\le\sqrt 2\big(\Vert\Pi_{\rm out}\phi\Vert+\Vert\phi-q\Vert\big),
```
where $`\Pi_{\rm out}`$ projects onto full-line energies outside $`\mathcal I_B`$. This uses the bath's original half-line spectrum, where its initial covariance is defined.

A finite lead suffices. Place the remote boundary at hopping distance $`d\ge16e\tau`$ from every packet support, using a lead of length $`O_\nu(\tau)`$ in this regime. Embed the cut evolution into the full line. After factoring out the uniform field, powers of the two hopping operators coincide on each packet up to order $`d-1`$, and their norms are at most two. The norm error is bounded by $`2\sum_{m\ge d}(2\tau)^m/m!`$, exponentially small in $`\tau`$. The projections add at most this norm error to the bounds above. Choose $`K`$, the ratio $`\tau/L`$ and $`B_0`$ large enough that the actual bath component has weight at least $`0.9`$ and arbitrarily small off-band weight.

### Estimate from a single count

For immediate spatial readout, pack $`M=\lfloor r/L\rfloor`$ packets entirely within the contacted region. For temporal readout, use the $`M`$ packed modes on the finite lead. In both cases each occupation mean is $`\langle q,f_b(h_B)q\rangle`$, with $`q`$ the spatial packet or the bath component of the backward-evolved temporal packet. In a left-to-right Jordan–Wigner ordering the initial covariance is the vacuum block plus the bath covariance. Both initial states are gauge invariant, and the final lead occupation measurement acts on the apparatus spins alone.

On $`\mathcal I_B`$ and for $`b\in[B,2B]`$, one has $`bE\in[1/2,3]`$, so

```math
-\partial_{\log b}f_b(E)=bE f_b(E)(1-f_b(E))
```
is bounded below by a positive constant. Its absolute value is bounded by one at every energy. With the stated concentration, each occupation mean decreases with slope bounded away from zero in $`\log b`$, uniformly on the octave. Its functional dependence is determined by the known model and receiver.

An internal number-preserving mode rotation followed by occupation readout measures the commuting mode occupations. Wick's identity gives the total count $`N`$ variance $`\mathrm{Var}(N)=\mathrm{Tr}[C_M(I-C_M)]\le M/4`$, where $`C_M`$ is the compressed covariance. This bound includes correlations between modes. Clip $`N`$ to the known range of its mean and invert that mean as a function of $`\log b`$. The mean has slope of magnitude at least a constant times $`M`$, so the estimate has squared log error bounded in expectation by a constant times $`\mathrm{Var}(N)/M^2=O(1/M)`$.

Choose the receiver according to the larger of $`r`$ and $`\tau`$. Above a field-dependent constant times $`B`$, this supplies $`M`$ proportional to $`\max\{r,\tau\}/B`$. Below that threshold, the midpoint of the known log-temperature interval gives constant risk. Since $`r+\tau`$ and $`\max\{r,\tau\}`$ are within a factor of two, this proves the upper bound.

## Interpretation and boundaries

The time dependence comes from ballistic transport at nonzero Fermi velocity. The temperature dependence comes from resolving modes within an energy of order $`1/B`$ of the Fermi level. The finite packet proof turns this phase-space count into an estimator for the one-bath experiment.

At a band edge the Fermi velocity vanishes and a different analysis is needed. The [fixed-interval theorem](model_and_results.md) continues to apply at every known field. Attainment with a fixed-size detector and the exact minimax coefficient remain open. See the [literature comparison](../references/RELATED_WORK.md#low-temperature-resource-scaling) and the [finite checks](../verification/README.md).
