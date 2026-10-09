# Six-Slide Proposal Content and Visual Specification

Status: `PROPOSED COMMUNICATION ARTIFACT`

The presentation must separate established mathematics, candidate gaps, hypotheses, and potential contributions. Visuals should be mathematically informative rather than decorative.

# Slide 1 — Research Background & Motivation

## Title

**Differential Geometry of Sustainable Infrastructure Viability**

## Core equations

$$
\dot Y=F(Y,u,\eta;\theta)
$$

and

$$
K_{\rm sus}
=
K_{\rm phys}
\cap K_{\rm serv}
\cap K_{\rm env}
\cap K_{\rm resource}
\cap K_{\rm econ}.
$$

Central idea:

$$
\mathcal V_{\rm sus}
=
\operatorname{Viab}_{F}(K_{\rm sus})
\subset(\mathcal M,g_\psi).
$$

## Visual design

- Left: compact P–W–T coupled-system diagram.
- Center: dynamics equation feeding a constraint-intersection graphic.
- Right: a smooth state manifold containing a highlighted viable region.
- Show one point \(Y\) inside \(\mathcal V_{\rm sus}\) and the boundary \(\partial\mathcal V_{\rm sus}\).
- Minimal text.

Key message:

> Resilience is treated as a property of a dynamically generated feasible region, not only as a scalar score.

# Slide 2 — Candidate Scientific & Industrial Gaps

## Scientific gaps

1. physically calibrated metric geometry;
2. sustainable viability geometry;
3. smooth/nonsmooth boundary transitions;
4. geometric deformation under hazard/degradation;
5. decision value of geometry.

## Industrial gaps

Core contrast:

$$
\boxed{\text{Monitoring}\neq\text{Viability intelligence}}
$$

Show five compact industrial statements:

- acceptable now versus viable future;
- heterogeneous P–W–T indicators;
- state prediction without explicit viable-region geometry;
- multi-constraint critical states;
- limited validated chain from state → margin → feasible intervention.

## Visual design

Split slide vertically:

- left: five scientific-gap mini-visuals;
- right: industrial state-monitoring pipeline ending before viability;
- one bottom caution band: `Candidate gaps until systematic-review closure`.

# Slide 3 — Research Questions, Objective & Hypotheses

## Main objective

> Develop and validate a physically calibrated smooth/nonsmooth geometric framework for sustainable infrastructure viability and determine whether its geometric information improves resilience diagnosis and intervention.

## RQs

### RQ1 — Metric

$$
Y\in(\mathcal M,g_\psi)
$$

### RQ2 — Boundary geometry

$$
\mathcal V_{\rm sus},\quad
\partial\mathcal V_{\rm sus},\quad
T_{\mathcal V},\quad
N_{\mathcal V}
$$

### RQ3 — Deformation

$$
\Delta\eta,\Delta\theta
\rightarrow
\Delta\mathcal V_{\rm sus}
\rightarrow
\Delta\rho_g
$$

### RQ4 — Decision value

Geometry versus Euclidean, reliability, and conventional resilience baselines.

## Hypotheses

$$
H_1:\quad \mathcal P(g_\psi)\stackrel{?}{>}\mathcal P(g_E)
$$

$$
H_2:\quad
\mathcal P(T_{\mathcal V},N_{\mathcal V})
\stackrel{?}{>}
\mathcal P(\text{smooth-only})
$$

$$
H_3:\quad
D_{\mathcal V}[\mathcal V(\theta+\delta),\mathcal V(\theta)]
\stackrel{?}{>}
\varepsilon_{\rm num}+\varepsilon_{\rm UQ}
$$

$$
H_4:\quad
\eta_{\rm geometry}
\stackrel{?}{>}
\eta_{\rm conventional}
$$

## Visual design

Use four aligned RQ cards, each connected to one mathematical object and one hypothesis. Keep \(H_4\) visibly falsifiable with a question mark.

# Slide 4 — Mathematical Research Framework

This is the central visual slide.

$$
\boxed{
\begin{array}{c}
\textbf{P-W-T PHYSICAL DYNAMICS}\\
\dot Y=F(Y,u,\eta;\theta)\\
\downarrow\\
\textbf{SUSTAINABLE CONSTRAINTS}\\
K_{\rm sus}\\
\downarrow\\
\textbf{SUSTAINABLE VIABILITY}\\
\mathcal V_{\rm sus}=\operatorname{Viab}_{F}(K_{\rm sus})\\
\downarrow\\
\textbf{INTRINSIC STATE-SPACE GEOMETRY}\\
Y\in(\mathcal M,g_\psi)\\
\downarrow\\
\textbf{VIABILITY-BOUNDARY GEOMETRY}\\
\partial\mathcal V_{\rm sus},\rho_g,T_{\mathcal V},N_{\mathcal V}\\
\downarrow\\
\textbf{DEFORMATION UNDER STRESS}\\
\Delta\eta,\Delta\theta\rightarrow\Delta\mathcal V_{\rm sus}\\
\downarrow\\
\textbf{RESILIENCE DIAGNOSIS}\\
\downarrow\\
\textbf{DYNAMICALLY FEASIBLE INTERVENTION}
\end{array}}
$$

Principal diagnostic:

$$
\boxed{
\rho_g(Y,t)
=
d_{g_\psi}(Y,\partial\mathcal V_{\rm sus}(t))
}
$$

## Visual design

- Left: vertical causal chain.
- Right: one large mathematical manifold visual with \(\mathcal V_{\rm sus}\), boundary, point \(Y\), and a geodesic-distance marker \(\rho_g\).
- Add a small inset showing a nonsmooth corner with tangent/normal cones.
- No decorative photography.

# Slide 5 — Candidate Contributions to Be Tested

## C1 — Physical metric

$$
g_\psi(Y)
$$

with engineering interpretation beyond coordinate-normalized Euclidean distance.

## C2 — Sustainable viability geometry

$$
\mathcal V_{\rm sus}\subset(\mathcal M,g_\psi).
$$

## C3 — Smooth/nonsmooth framework

$$
\text{Riemannian boundary geometry}
+
T_{\mathcal V}
+
N_{\mathcal V}.
$$

## C4 — Geometric deformation

$$
\text{hazard/degradation}
\rightarrow
\Delta\mathcal V_{\rm sus}
\rightarrow
\Delta\rho_g.
$$

## C5 — Engineering validation

Compare geometry, Euclidean, reliability, and conventional resilience using common disturbances and equal resources.

Critical principle:

> Beautiful geometry is insufficient; it must demonstrate added explanatory or decision value.

## Visual design

Use a five-row matrix. Each row contains:

`candidate contribution → mathematical object → validation target`.

# Slide 6 — Engineering Translation & Long-Term Research Vision

## Operational translation

$$
\boxed{
\text{Sensors/Data}
\rightarrow
\hat Y
\rightarrow
\hat{\mathcal V}_{\rm sus}
\rightarrow
\rho_g
\rightarrow
\text{active constraints}
\rightarrow
\text{feasible intervention}
}
$$

Potential applications:

- climate adaptation;
- critical-service continuity;
- infrastructure operations;
- resilience planning;
- Digital Twin analytics;
- asset/intervention prioritization.

## PhD research trajectory

$$
\boxed{
\begin{array}{c}
\text{Differential Geometry}\\
\downarrow\\
\text{Nonsmooth / Variational Geometry}\\
\downarrow\\
\text{Geometric Dynamical Systems}\\
\downarrow\\
\text{Geometric Control}\\
\downarrow\\
\text{Hamilton--Jacobi / Reachability}\\
\downarrow\\
\text{Stochastic Differential Geometry}\\
\downarrow\\
\text{Information Geometry}\\
\downarrow\\
\text{Inverse Sustainable Infrastructure Design}
\end{array}}
$$

Long-term vision:

> A geometric theory of sustainable infrastructure viability connecting physical dynamics, viable futures, geometric resilience, and engineering decisions.

## Visual design

- Top: operational pipeline.
- Bottom-left: mathematical PhD trajectory.
- Bottom-right: compact long-term loop `physical dynamics → viable futures → geometric resilience → engineering decisions`.

# Visual integrity standard

Every figure must distinguish:

- analytical variables actually computed;
- schematic conceptual relationships;
- proposed future operational layers;
- unvalidated candidate contributions.

No visual should imply that a candidate gap or proposed metric has already been validated.

