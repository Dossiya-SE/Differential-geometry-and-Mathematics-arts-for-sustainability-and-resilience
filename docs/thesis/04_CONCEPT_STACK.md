# Physics–Mathematics–Engineering Concept Stack

Status: `PROPOSED TAXONOMY`

The project draws from three domains. The concepts should not be treated as an undifferentiated list; they are assigned roles as `CORE`, `SUPPORT`, `VALIDATION`, `CONDITIONAL`, or `FUTURE`.

# A. Physics

| Concept | Role | Thesis use |
|---|---|---|
| Conservation laws | CORE | Enforce physically admissible P–W–T flows and balances |
| Transport phenomena | CORE | Represent transfer of energy, water, mobility, and service |
| Network physics | CORE | Couple structure to flow, propagation, and cascading behavior |
| Failure/degradation physics | CORE | Model capacity loss and interface deterioration |
| Climate/hazard physics | CORE | External forcing \(\eta(x,t)\) |
| Physical thresholds | CORE | Define \(K_{\rm phys}\) and active constraints |
| Complex systems | SUPPORT | Emergent behavior and interdependency |
| Stochastic physics | SUPPORT | Random disturbances and degradation |
| Multiscale physics | SUPPORT | Different spatial and temporal scales |
| Thermodynamics | CONDITIONAL | Energy/resource admissibility where physically relevant |
| Entropy/irreversibility | CONDITIONAL | Degradation/efficiency interpretation when justified |
| Exergy | CONDITIONAL | Energy/resource-quality constraints where justified |

Physics spine:

$$
\boxed{
\text{Conservation}
\rightarrow
\text{Flows}
\rightarrow
\text{Interdependency}
\rightarrow
\text{Degradation}
\rightarrow
\text{Hazard}
\rightarrow
\text{Physical limits}
}
$$

# B. Mathematics

| Concept | Role | Thesis use |
|---|---|---|
| Graph/network theory | CORE in Thesis 1; SUPPORT in Thesis 2 | Structural representation \(\mathfrak G_{\rm PWT}\) |
| Nonlinear dynamical systems | CORE | Define \(F\) or \(F_{\mathfrak G}\) |
| Viability theory | CORE | Compute/characterize \(\mathcal V_{\rm sus}\) |
| Differential geometry | CORE/CENTRAL | State manifold and intrinsic geometry |
| Riemannian geometry | CENTRAL in Thesis 2 | Metric, distance, geodesics, local geometry |
| Nonsmooth/variational analysis | CORE/CENTRAL | Tangent/normal cones and active-constraint intersections |
| Differential topology | SUPPORT/DEEPENING | Local/global manifold structure when needed |
| Set-valued analysis | CORE/DEEPENING | Viability maps and set deformation |
| Probability | CORE/SUPPORT | Hazard, parameter, state uncertainty |
| Uncertainty quantification | CORE | Ranking confidence and robustness |
| Reachability | SUPPORT | Recovery and safe reachable sets |
| Reliability mathematics | SUPPORT/BASELINE | Conventional benchmark |
| Optimization | VALIDATION | Intervention selection and design |
| Control theory | VALIDATION | Adaptation and dynamically feasible action |
| Geometric control | DEEPENING | Control on manifolds and viability-preserving motion |
| Decision mathematics | VALIDATION | Equal-resource comparison and decision value |
| Hamilton–Jacobi methods | DEEPENING | Reachability/viability computation and PDE formulation |
| Information geometry | FUTURE | Geometry of uncertain state distributions |
| Tensor methods | FUTURE | Scalable approximation of high-dimensional viability/value functions |

Mathematical spine for Thesis 1:

$$
\boxed{
\text{Graphs}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Viability}
\rightarrow
\text{Geometry}
\rightarrow
\text{UQ}
\rightarrow
\text{Optimization/Control}
}
$$

Mathematical spine for Thesis 2:

$$
\boxed{
\text{Dynamics}
\rightarrow
\text{Viability}
\rightarrow
\text{Riemannian Geometry}
\rightarrow
\text{Nonsmooth Geometry}
\rightarrow
\text{Deformation}
\rightarrow
\text{Geometric Control}
}
$$

# C. Engineering

| Concept | Role | Thesis use |
|---|---|---|
| Systems-of-systems engineering | CORE | Coupled P–W–T architecture and interfaces |
| Sustainable engineering | CORE | Define non-compensatory sustainability conditions |
| Resilience engineering | CORE | Disturbance, survival, adaptation, recovery |
| Critical-service engineering | CORE | Map system states to essential service continuity |
| Robust/adaptive design | CORE | Strengthening and operational response |
| Climate adaptation/mitigation | CORE | Structural and operational interventions |
| Reliability engineering | SUPPORT/BASELINE | Compare geometry/viability against conventional margins |
| Human-centred infrastructure | SUPPORT | Service-to-population interpretation when data support it |
| Asset management | SUPPORT | Maintenance and recovery actions |
| Life-cycle engineering | SUPPORT | Long-term intervention consequences |
| Smart infrastructure | FUTURE/SUPPORT | Online state estimation and operational analytics |
| Digital Twins | FUTURE/SUPPORT | Operationalization of viability geometry, not the mathematical core |
| Circular engineering | CONDITIONAL | Resource/material loops if included in the case study |

Engineering chain:

$$
\boxed{
\text{SoS architecture}
\rightarrow
\text{sustainability requirements}
\rightarrow
\text{resilience}
\rightarrow
\text{critical services}
\rightarrow
\text{adaptation/mitigation}
\rightarrow
\text{validation}
}
$$

# Shared high-priority core

The smallest common concept set capable of supporting both thesis trajectories is:

1. conservation laws;
2. network physics;
3. failure/degradation physics;
4. climate/hazard physics;
5. nonlinear dynamical systems;
6. viability theory;
7. differential/Riemannian geometry;
8. nonsmooth/variational analysis;
9. probability/UQ;
10. systems-of-systems engineering;
11. sustainable engineering;
12. resilience engineering;
13. critical-service engineering;
14. optimization/control;
15. adaptation/mitigation.

The difference between Thesis 1 and Thesis 2 is therefore primarily **hierarchy**, not a completely different toolbox.

