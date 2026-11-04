# Scientific reading guide

The central resource is access to temperature information already present in a bath at the beginning of an experiment. A larger contact contains more of that information immediately. Additional elapsed time allows more distant bath degrees of freedom to influence the contact. The question is whether arbitrary quantum apparatus can improve on that spatial and temporal supply.

## The connected argument

1. **[Model and exact results](model_and_results.md).** Define the initially thermal half-chain, fixed contact, permitted adaptive protocols, complete output, and minimax squared log-temperature risk. This page owns the theorem's quantifiers and assumptions.
2. **[Locality converse](locality_converse.md).** Group the entire apparatus and contacted region into a single boundary block. Locality then limits the temperature distinguishability available to the complete experiment. A relative-entropy estimate for restricted Gaussian thermal states and a two-point testing argument turn this into a global estimation lower bound.
3. **[Counted sensor and attainment](counted_sensor.md).** Derive the physical spin count distribution, prove a linear supply of one-particle loss channels, and construct a globally calibrated estimator. Combine this temporal protocol with an initial block-occupation measurement to attain the joint spatial and temporal order.
4. **[Physical consequences](physical_consequences.md).** Interpret the result as a limit on information acquisition from a fixed bath contact. Compare the microscopic experiment with controlled Markov models, and identify the assumptions that change the conclusion.

## Proof dependencies and attribution

The converse and the construction share the [model](model_and_results.md) but have separate mathematical mechanisms. The converse uses finite-range locality, matrix relative entropy, and binary decision theory. The construction uses the XX-chain one-particle representation, exact loss counting, a boundary resolvent estimate, and a monotone inverse estimator. Neither part assumes the desired conclusion from the other.

The [related-work account](../references/RELATED_WORK.md) identifies imported ingredients and the closest thermometry models. Primary source identities are collected in the [bibliography](../references/references.bib). The [verification guide](../verification/README.md) describes the finite calculations and their limits.

For a quick result-first route, read the model, then the physical consequences. To audit the theorem, read both proof pages in full, including the continuous-instrument and infinite-volume limits.

## Learning route

The [Wiseman–Milburn bridge](../learning/ANCHOR_BRIDGE.md) connects the measurement and control foundations to this argument. Use it alongside the [30-milestone map](../learning/MILESTONES.md), whose two phases develop the prerequisites and then assemble the complete result. The specialist proof route above remains authoritative for exact statements and technical detail.
