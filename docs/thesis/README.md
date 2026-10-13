# Thesis Research Consolidation

Status: `PROPOSED / EVIDENCE-BOUND`

This folder consolidates the thesis research developed in the 2026-08-31 working session. It is deliberately structured so that **established mathematics**, **candidate gaps**, **hypotheses**, **engineering translations**, and **future extensions** remain distinct.

The repository-level domain-neutral architecture remains unchanged. This package records two application-specific thesis trajectories for coupled Power–Water–Transportation (P–W–T) infrastructure.

## Thesis trajectories

### Thesis 1 — Graph-to-Viability Geometry of Sustainable and Resilient Power–Water–Transportation Systems

Core identity:

$$
\mathfrak G_{\rm PWT}
\rightarrow F_{\mathfrak G}
\rightarrow K_{\rm sus}
\rightarrow \mathcal V_{\rm sus}
\rightarrow \text{geometry}
\rightarrow \text{criticality}
\rightarrow \text{intervention}.
$$

Main question:

> How do infrastructure architecture and dynamic cross-sector interfaces change sustainable viable futures, and can that information improve adaptation and mitigation decisions?

Primary signature map:

$$
\Psi:(\mathscr G_{\rm PWT},d_{\mathscr G})\rightarrow(\mathscr V,D_{\mathcal V}),
\qquad
\Psi(\mathfrak G)=\mathcal V_{\rm sus}(\mathfrak G).
$$

### Thesis 2 — Differential and Nonsmooth Geometry of Sustainable Infrastructure Viability

Core identity:

$$
F
\rightarrow K_{\rm sus}
\rightarrow \mathcal V_{\rm sus}\subset(\mathcal M,g_\psi)
\rightarrow \partial\mathcal V_{\rm sus}
\rightarrow \rho_g
\rightarrow \text{deformation}
\rightarrow \text{decision}.
$$

Main question:

> What is the intrinsic smooth and nonsmooth geometry of sustainable infrastructure viability, how does that geometry deform under stress, and can it improve resilience diagnosis and intervention?

Primary geometric object:

$$
\mathcal V_{\rm sus}\subset(\mathcal M,g_\psi),
\qquad
\rho_g(Y,t)=d_{g_\psi}(Y,\partial\mathcal V_{\rm sus}(t)).
$$

## Current interpretation

- **Thesis 1** is architecture-centred: `architecture → dynamics → viability → geometry → redesign`.
- **Thesis 2** is geometry-centred: `dynamics → viability → differential/nonsmooth geometry → diagnosis → intervention`.
- Thesis 2 is the stronger route if the long-term objective is deeper specialization in applied mathematics, differential geometry, variational analysis, geometric control, Hamilton–Jacobi reachability, stochastic differential geometry, and information geometry.
- Thesis 1 remains stronger for direct infrastructure architecture redesign, network criticality, and system-of-systems engineering.

## Research-integrity rules

1. Candidate gaps are not declared novelty until systematic-review validation closes.
2. Viability theory, Riemannian viability, tangent/normal conditions, graph resilience, topology optimization, stochastic viability, and Digital Twins are established fields and must not be claimed as newly invented here.
3. A proposed Riemannian metric must be physically calibrated, symmetric positive definite, dimensionally interpretable or explicitly normalized, and compared with Euclidean baselines.
4. Geodesic proximity is not equivalent to dynamic feasibility.
5. Smooth manifold structure does not imply a smooth viability boundary.
6. Curvature is used only where regularity supports it and where it has a defensible engineering interpretation.
7. Uncertainty, numerical tolerance, model reduction, and discretization error must be separated from physical effects.
8. Engineering value must be tested against conventional baselines under equal or explicitly normalized resources.
9. Digital Twins, GIS, co-simulation and forecasting platforms are support/implementation layers, not the mathematical novelty by themselves.
10. Negative results remain scientifically valid outcomes.

## Contents

- [01 — Graph-to-Viability thesis](01_GRAPH_TO_VIABILITY_GEOMETRY.md)
- [02 — Differential/nonsmooth geometry thesis](02_DIFFERENTIAL_NONSMOOTH_GEOMETRY.md)
- [03 — Scientific and industrial gaps, RQs, hypotheses](03_GAPS_RQS_HYPOTHESES.md)
- [04 — Physics, mathematics, engineering concept stack](04_CONCEPT_STACK.md)
- [05 — Mathematical architecture and computation](05_MATHEMATICAL_AND_COMPUTATIONAL_ARCHITECTURE.md)
- [06 — Industrial translation and platform fit](06_INDUSTRIAL_TRANSLATION.md)
- [07 — MSc-to-PhD research trajectory](07_MSC_TO_PHD_TRAJECTORY.md)
- [08 — Six-slide proposal content and visual specification](08_SIX_SLIDE_PROPOSAL_SPEC.md)
- [09 — Exploratory extensions: information geometry, tensors, quantum-inspired ideas](09_EXPLORATORY_EXTENSIONS.md)
- [10 — Synthetic 2D viability demonstrator](10_2D_VIABILITY_DEMONSTRATOR.md)
- [11 — Known prior art and novelty claim boundaries](11_KNOWN_PRIOR_ART_AND_CLAIM_BOUNDARIES.md)

