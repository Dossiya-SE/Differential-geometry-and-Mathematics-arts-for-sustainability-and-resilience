# Mathematical and Computational Architecture

Status: `PROPOSED IMPLEMENTATION ARCHITECTURE`

A mathematically honest visualization or simulation of the thesis requires four distinct computational layers. Skipping one risks producing a figure that resembles the theory without actually computing the map under study.

# Layer 1 — Infrastructure graph / structural representation

For Thesis 1, the structural object is

$$
\mathfrak G_{\rm PWT}
=
\{G_P,G_W,G_T,E_{PW},E_{PT},E_{WT}\}.
$$

Visual coordinates may be:

- real geospatial coordinates, preferred when representing physical infrastructure;
- force-directed layouts for structure-first diagrams;
- spectral embeddings based on graph Laplacian eigenvectors;
- multilayer/multiplex layouts with separated P/W/T layers and explicit cross-sector couplings.

The graph layer visualizes architecture only. It does not by itself compute dynamics or viability.

# Layer 2 — Reduced physical dynamics

Use a physically justified reduced state \(Y\) with approximately 2–4 effective continuous dimensions for initial viability computation and visualization.

The governing model is

$$
\dot Y=F_{\mathfrak G}(Y,u,\eta;\theta)
$$

or, for the geometry-centred trajectory,

$$
\dot Y=F(Y,u,\eta;\theta).
$$

Numerical integration candidates:

- Runge–Kutta methods for deterministic ODEs;
- Euler–Maruyama or stronger SDE solvers for explicitly stochastic dynamics;
- event-aware integration where breakers, capacity switches, or discrete failures are modeled.

High-dimensional infrastructure models should be reduced using physically justified methods rather than arbitrary plotting projection. Candidate approaches include balanced truncation, proper orthogonal decomposition, nonlinear manifold reduction, or other verified reduced-order modeling techniques.

# Layer 3 — Sustainable viability computation

Construct each admissibility component explicitly in the same state coordinates:

$$
K_{\rm sus}
=
K_{\rm phys}
\cap K_{\rm serv}
\cap K_{\rm env}
\cap K_{\rm resource}
\cap K_{\rm econ}.
$$

The viable set is

$$
\mathcal V_{\rm sus}
=
\operatorname{Viab}_{F}(K_{\rm sus}).
$$

For low-dimensional systems, candidate algorithms include:

## Grid-based viability / Saint-Pierre-style iteration

Initialize the admissible grid and iteratively remove states for which no admissible control keeps the next state inside the current approximation. This is transparent and suitable for an initial 2D–4D demonstrator.

## Hamilton–Jacobi reachability

Represent the safe/viable set through a value function and solve the corresponding HJ PDE. A level-set representation can provide a continuous boundary approximation and can support distance-like calculations.

The numerical method must report:

- grid/domain bounds;
- time step or PDE discretization;
- convergence/fixed-point tolerance;
- control discretization;
- numerical error estimates;
- sensitivity to state normalization;
- computational cost.

# Layer 4 — Geometric analysis

Once \(\mathcal V_{\rm sus}\) exists as a numerical set, compute geometric diagnostics.

## Boundary extraction

- marching squares in 2D;
- marching cubes in 3D;
- slicing/projection only with explicit documentation in 4D+.

## Euclidean baseline

First compute

$$
\rho_E(Y)=d_E(Y,\partial\mathcal V_{\rm sus}).
$$

A Euclidean signed-distance transform is a mandatory baseline before introducing a nontrivial metric.

## Riemannian metric

Candidate metric:

$$
g_\psi(Y)
=
J_{\tilde h}(Y)^\top W_\psi J_{\tilde h}(Y)+\lambda I.
$$

The corresponding intrinsic viability margin is

$$
\rho_g(Y)
=
d_{g_\psi}(Y,\partial\mathcal V_{\rm sus}).
$$

For nontrivial metrics, numerical methods may require an eikonal solver or fast marching / geodesic-distance computation adapted to spatially varying anisotropic metrics.

## Smooth and nonsmooth boundary analysis

At smooth points, use gradients, tangent spaces, and normals. At intersections and corners, use

$$
T_{\mathcal V}(Y),\qquad N_{\mathcal V}(Y),
$$

with generalized gradients or normal-cone calculus if deeper regularity analysis is required.

## Set deformation

Given baseline \(\mathcal V_0\) and perturbed \(\mathcal V_\delta\), quantify

$$
D_{\mathcal V}[\mathcal V_\delta,\mathcal V_0].
$$

Candidate metrics:

- Hausdorff distance;
- symmetric-difference measure;
- boundary displacement statistics;
- application-specific weighted set distances.

No set-distance metric should be treated as automatically superior or coordinate invariant without analysis.

For interface/parameter sensitivity,

$$
S_e^{\mathcal V}(\delta)
=
\frac{D_{\mathcal V}[\mathcal V(\theta+\delta e),\mathcal V(\theta)]}{|\delta|}.
$$

# Dynamic intervention layer

Geometry does not replace dynamics. A geometrically favorable direction is only actionable if it is dynamically feasible.

At the viability boundary, a necessary viability-style condition is expressed through the tangent cone:

$$
F(Y,u,\eta)\in T_{\mathcal V}(Y).
$$

A possible intervention objective is

$$
u^\star
=
\arg\max_{u\in U}\dot\rho_g(Y;u)
$$

subject to physical equations, control bounds, and sustainability constraints.

# Recommended MSc-scale computational scope

$$
\boxed{
3\text{ systems}
+3\text{ cross-sector interfaces}
+1\text{ hazard}
+1\text{ case study}
+2\text{--}4\text{ effective viability dimensions}
}
$$

Avoid in one MSc implementation:

- citywide full-dimensional viability;
- unrestricted topology optimization;
- many hazards and cities;
- full industrial Digital Twin deployment;
- deep learning plus TDA plus Ricci plus differential geometry simultaneously;
- universal graph-to-manifold theorems.

# Verification and validation sequence

1. Verify physical equations and units.
2. Verify reduced-order model against the higher-fidelity model.
3. Verify viability implementation on benchmark systems with known behavior.
4. Verify Euclidean distance and set-distance computations.
5. Verify \(g_\psi\) SPD and coordinate/scaling behavior.
6. Compare \(\rho_g\) against \(\rho_E\).
7. Propagate parameter/hazard uncertainty.
8. Compare geometry-guided diagnosis/intervention with conventional baselines under equal resources.

