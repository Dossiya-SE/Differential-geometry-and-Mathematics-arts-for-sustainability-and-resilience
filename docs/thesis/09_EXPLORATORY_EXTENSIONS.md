# Exploratory Extensions: Information Geometry, Tensor Methods, and Quantum-Inspired Ideas

Status: `FUTURE / EXPLORATORY`

These directions arose during thesis exploration. They are intentionally separated from the current core so that mathematical inspiration is not confused with evidence-backed infrastructure physics.

# 1. Information geometry

If the uncertain infrastructure state is represented as a probability distribution

$$
Y\sim p(Y;\theta),
$$

then the family

$$
\mathcal P=\{p(Y;\theta):\theta\in\Theta\}
$$

may be treated as a statistical manifold.

A Fisher information metric is

$$
(g_F)_{ij}(\theta)
=
\mathbb E\left[
\frac{\partial\log p}{\partial\theta_i}
\frac{\partial\log p}{\partial\theta_j}
\right].
$$

Potential long-term question:

> Can geometric distances between uncertain infrastructure-state distributions provide meaningful resilience information beyond state-space geometry alone?

This is a promising PhD extension, but it requires clear answers to:

- what probability family is physically justified;
- what variables are observed or latent;
- whether Fisher distance has a demonstrable engineering interpretation;
- what constitutes viability in distribution space.

# 2. Tensor methods for scalable viability computation

The curse of dimensionality is a fundamental limitation of viability and reachability algorithms.

A high-dimensional viability indicator or value function may admit low-rank approximation, for example through tensor-train, hierarchical, sparse-grid, or reduced-basis structures.

A generic approximation target is

$$
V(Y_P,Y_W,Y_T,Z)
\approx
\widetilde V_r(Y)
$$

with rank/complexity \(r\) controlled and error verified.

Potential research question:

> Can low-rank structure preserve viability-boundary geometry while reducing computational cost enough for larger infrastructure systems?

Do not write

$$
Y=Y_P\otimes Y_W\otimes Y_T
$$

unless a genuine tensor-product state structure is mathematically defined. Classical infrastructure coupling does not automatically imply such a product.

# 3. Quantum-mechanics inspiration: what is useful

The useful lesson from Bloch-sphere-style quantum-state visualization is the general principle:

$$
\boxed{
\text{complex system}
\rightarrow
\text{structured state space}
\rightarrow
\text{geometry}
\rightarrow
\text{dynamics}
\rightarrow
\text{measurement/decision}
}
$$

For infrastructure, this motivates physically meaningful state-space geometry. It does **not** justify claiming that classical infrastructure states are quantum superpositions.

# 4. Interdependency versus "entanglement"

Infrastructure systems are classically dependent, not quantum entangled.

A defensible statistical statement is

$$
P(Y_P,Y_W,Y_T)
\neq
P(Y_P)P(Y_W)P(Y_T).
$$

Useful mathematics includes:

- mutual information;
- conditional mutual information;
- graphical models;
- copulas;
- dependence measures.

Avoid using `entanglement` as infrastructure terminology unless a genuinely quantum subsystem is present.

# 5. Quantum walks

Quantum walks may be mathematically interesting for network analysis, but they should not be introduced into infrastructure-failure propagation without a clear physical or computational justification.

Classical spectral, diffusion, flow, percolation, and random-walk benchmarks are sufficient for the present thesis.

# 6. Quantum-inspired or quantum optimization

Future infrastructure redesign may contain binary topology decisions

$$
x_e\in\{0,1\}
$$

and potentially QUBO-like formulations.

Quantum annealing, QAOA, or quantum-inspired optimization are implementation options only after the resilience/viability objective has been validated. The primary scientific problem is defining and validating

$$
R_{\rm sus}(G)
$$

rather than changing the solver technology.

# 7. Hybrid classical–quantum infrastructure resilience

A separate future research direction could ask when quantum communication resources materially change critical-infrastructure viability.

Possible hybrid map:

$$
\Psi_H:\mathscr G_H\rightarrow\mathscr V_H.
$$

Potential question:

> Under what conditions does selective quantum-secure communication augmentation enlarge the sustainable viable region relative to conventional secure communication and post-quantum alternatives under equal lifecycle resources?

A practical state should normally use engineering-relevant quantum-network variables such as key rate, QBER, link availability, loss, latency, trusted-node state, and classical fallback. A quantum density operator \(\rho_Q\) should be used only if the quantum state itself materially enters the infrastructure-level resilience model.

Any quantum augmentation must be allowed to worsen viability because it can add powered equipment, optical dependencies, maintenance, trusted nodes, geographic constraints, and new failure modes:

$$
\Delta\mathcal V_H
\gtrless
0.
$$

Potential comparison:

- classical secure architecture;
- post-quantum cryptography;
- selective QKD;
- QKD with redundant quantum paths;
- viability-optimized hybrid architecture.

This is a future research programme, not part of the current thesis kernel.

# Priority order

For the current research programme, the preferred order is:

1. physical-state differential/nonsmooth geometry;
2. probabilistic/stochastic viability;
3. information geometry;
4. scalable tensor/reduced-order methods;
5. inverse geometric design;
6. advanced solver technologies, including quantum-inspired methods where justified.

