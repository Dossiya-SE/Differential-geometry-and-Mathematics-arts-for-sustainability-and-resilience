# Thesis 2 — Differential and Nonsmooth Geometry of Sustainable Infrastructure Viability

Status: `PROPOSED / DEEP-MATHEMATICS TRAJECTORY`

## Central scientific identity

$$
\boxed{
F
\rightarrow
K_{\rm sus}
\rightarrow
\mathcal V_{\rm sus}\subset(\mathcal M,g_\psi)
\rightarrow
\partial\mathcal V_{\rm sus}
\rightarrow
\rho_g
\rightarrow
\text{deformation}
\rightarrow
\text{decision}
}
$$

Main question:

> What is the intrinsic smooth and nonsmooth geometry of sustainable infrastructure viability, how does that geometry deform under stress, and can it improve resilience diagnosis and intervention?

This thesis is geometry-centred. Network structure remains relevant because it helps generate the physical dynamics, but the main mathematical object is the sustainable viable region itself.

## Physical system and dynamics

A reduced P–W–T state evolves according to

$$
\dot Y=F(Y,u,\eta;\theta),
$$

where \(Y\) contains physically interpretable reduced states, \(u\) denotes admissible control, \(\eta\) external forcing/hazard, and \(\theta\) system/interface parameters.

Conservation laws, network physics, transport phenomena, degradation physics, and engineering constraints define \(F\) and the admissible domain. They do **not** automatically define the manifold curvature or topology.

## Sustainable admissibility

$$
K_{\rm sus}
=
K_{\rm phys}
\cap K_{\rm serv}
\cap K_{\rm env}
\cap K_{\rm resource}
\cap K_{\rm econ}.
$$

The sustainable viable set is

$$
\boxed{
\mathcal V_{\rm sus}
=
\operatorname{Viab}_{F}(K_{\rm sus})
}
$$

and is interpreted as the set of states from which at least one admissible future control/trajectory keeps the system within the sustainability constraints for the declared horizon.

## Intrinsic state-space geometry

Represent the reduced state as

$$
Y\in(\mathcal M,g_\psi).
$$

The metric \(g_\psi\) must be constructed so that intrinsic distance reflects meaningful physical, service, sustainability, and/or intervention consequences rather than arbitrary coordinate scaling.

A candidate construction is

$$
\boxed{
g_\psi(Y)
=
J_{\tilde h}(Y)^\top W_\psi J_{\tilde h}(Y)+\lambda I
}
$$

where \(\tilde h\) is a normalized consequence map and \(W_\psi\) a declared weighting/calibration operator.

Required validation:

- symmetry and positive definiteness;
- dimensional or normalization consistency;
- coordinate/scaling sensitivity;
- physical calibration;
- stability under parameter uncertainty;
- comparison with Euclidean baseline \(g_E=I\).

## Geometric viability margin

Define

$$
\boxed{
\rho_g(Y,t)
=
d_{g_\psi}(Y,\partial\mathcal V_{\rm sus}(t))
}
$$

and call it an **intrinsic sustainable-viability margin**.

It must not be described as a universal distance to collapse. Crossing \(\partial\mathcal V_{\rm sus}\) means loss of modeled sustainable viability, not necessarily physical system collapse.

## Smooth and nonsmooth boundary geometry

At regular boundary points, if

$$
\partial\mathcal V=\{Y:h(Y)=0\}
$$

with sufficient regularity, differential/Riemannian geometry may characterize tangent directions, normals, geodesic distance, and—where justified—curvature-like quantities.

At intersections of multiple active constraints, ordinary smooth geometry may fail. Use

$$
\boxed{
T_{\mathcal V}(Y),\qquad N_{\mathcal V}(Y)
}
$$

and, in deeper work, generalized gradients, proximal/Clarke normals, coderivatives, and set-valued sensitivity.

## Deformation under hazard and degradation

The research treats resilience as a geometric deformation problem:

$$
\theta,\eta
\mapsto
\mathcal V_{\rm sus}(\theta,\eta)
$$

and studies

$$
\Delta\eta,\Delta\theta
\rightarrow
\Delta\mathcal V_{\rm sus}
\rightarrow
\Delta\rho_g,
$$

with additional changes in boundary structure, tangent/normal cones, active constraints, and set distances.

Set deformation can be quantified using declared metrics such as Hausdorff distance, symmetric-difference measure, or application-specific distances. No single set metric is assumed universal.

## Geometric control and intervention

A normal direction is only local geometric information; it is not automatically a feasible control direction.

Dynamic feasibility requires

$$
\dot Y=F(Y,u,\eta)
$$

with viability conditions such as

$$
F(Y,u,\eta)\in T_{\mathcal V}(Y)
$$

at the boundary.

A possible control objective is

$$
u^\star
=
\arg\max_{u\in U}\dot\rho_g(Y;u)
$$

subject to the physical dynamics and all constraints.

Likewise, a shortest geodesic is not automatically a reachable or dynamically feasible recovery path.

## Scientific identity

This thesis is not "apply differential geometry to infrastructure". Its stronger research identity is:

> Develop and validate a physically calibrated smooth/nonsmooth geometric description of dynamically generated sustainable infrastructure viability, quantify how that geometry deforms under stress, and test whether the geometric information adds predictive or intervention value beyond simpler baselines.

## Why this trajectory is attractive for deeper mathematics

The MSc/early thesis core can remain bounded to:

$$
F\rightarrow K_{\rm sus}\rightarrow\mathcal V_{\rm sus}\rightarrow g_\psi\rightarrow\rho_g\rightarrow T_{\mathcal V},N_{\mathcal V}.
$$

A PhD can deepen naturally into:

1. Riemannian geometry and geodesic structure;
2. variational and nonsmooth geometry;
3. geometric dynamical systems;
4. geometric control;
5. Hamilton–Jacobi reachability;
6. stochastic differential geometry;
7. information geometry;
8. inverse geometric infrastructure design.

