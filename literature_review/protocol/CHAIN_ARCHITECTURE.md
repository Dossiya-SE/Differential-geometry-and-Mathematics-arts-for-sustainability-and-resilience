---
architecture_id: MSR-CA-001
version: 0.1.0
date: 2026-08-22
status: PROPOSED_NON_EXHAUSTIVE
application_decision: NOT_SELECTED
---

# Provisional Ten-Chain Architecture for Sustainable Resilience

## 1. Status and purpose

The earlier six-chain architecture was a provisional extraction scaffold for the first paper case study. It was not a complete ontology of sustainable resilience, and the number six had no special mathematical justification. The scaffold was useful because it separated physical mechanisms, observation and inference, disturbance and consequences, resilience-state mathematics, intervention and adaptation, and service distribution and equity. That separation remains scientifically valuable, but the formulation was incomplete and some sequences mixed causal stages, mathematical properties, analytical methods, and outcomes.

This document replaces the six-chain label with a stronger domain-neutral architecture of ten provisional chains. It is a research construct, not a literature-validated final ontology. It must be tested against the project's [12 application families](../application_selection/scope_review_01/SCOPE_REVIEW_01.md#4-expanded-application-scope-universe) before being frozen. The application remains `NOT_SELECTED`.

## 2. Audit of the earlier scaffold

| Earlier chain | Assessment and required correction |
|---|---|
| Physics → Structure → Interfaces → Dynamics | Important, but physical forcing, state evolution, structure, and interface coupling require clearer separation. |
| Observe → Identify → Estimate → Predict | Valid epistemic sequence, but uncertainty, calibration, validation, and falsification were missing. |
| Hazard → Failure → Service loss → Consequences | Valid causal core, but exposure, vulnerability, cascade propagation, and common-cause disturbances were missing. |
| Recovery → Resilience → Reachability → Viability | The order was problematic. Viability and reachability characterize admissible possibilities before recovery trajectories and resilience outcomes are evaluated. |
| Decision → Control → Optimization → Adaptation | Optimization is a method for selecting controls or designs, not necessarily a temporal stage after control. Implementation, monitoring, and learning were missing. |
| Service → Population → Equity → Critical-service continuity | Service availability and continuity should normally be measured before population access and distributional consequences are evaluated. |

## 3. Ten provisional chains

The chains are ordered mechanisms or reasoning paths. They do not imply that every real system is acyclic; feedback, iteration, and cross-chain coupling are expected.

| ID | Chain class | Ordered chain | Governing question |
|---|---|---|---|
| C01 | Physical-causal | **Forcing → Physical laws → States and flows → Dynamics** | What drives the system, which conservation or constitutive laws apply, and how do states and flows evolve? |
| C02 | Structural-interface | **Structure → Interfaces → Coupling → Feedback and cascade propagation** | How does organization create dependencies, transmissions, feedbacks, and cascades? |
| C03 | Epistemic-inference | **Sensing → Data → Identification → Estimation → Uncertainty → Prediction → Validation** | What is observed, what can be identified, how uncertain are estimates and forecasts, and how are they tested? |
| C04 | Disturbance-consequence | **Hazard or stressor → Exposure → Vulnerability → Failure or degradation → Service loss → Consequences** | How does a disturbance become functional loss and material, ecological, social, or economic harm? |
| C05 | Viability-resilience | **Constraints → Admissible states → Viability kernel → Reachability → Response and recovery → Resilience → Adaptation or transformation** | Which states and trajectories remain acceptable, which can be reached, and how does the system persist, recover, adapt, or transform? |
| C06 | Decision-action-learning | **Objectives and trade-offs → Decision → Intervention design → Control or optimization → Implementation → Monitoring → Learning** | How are competing objectives converted into implementable and revisable actions? |
| C07 | Service-equity | **Service capacity → Availability and continuity → Population access → Critical needs → Distributional effects → Equity and well-being** | Who receives which service, when, at what reliability, and with what distribution of benefits and burdens? |
| C08 | Sustainability-metabolism | **Resource extraction → Transformation → Stocks and flows → Emissions and waste → Life-cycle burdens → Circularity or regeneration → Sustainability** | How do resources and burdens move across the life cycle, boundaries, generations, and affected systems? |
| C09 | Institutional-implementation | **Ownership and institutions → Governance → Incentives and finance → Coordination → Operations and maintenance → Adoption and legitimacy** | Which actors can authorize, finance, coordinate, maintain, and legitimately sustain an intervention? |
| C10 | Mathematical-art impact | **Mathematical encoding → Visual, sonic, or material form → Interpretation → Comprehension and participation → Decision influence → Evaluated impact** | How is mathematical structure mapped into an expressive form, and what analytical, participatory, behavioral, or design effect is actually validated? |

## 4. Cross-cutting axes

The following axes must not be forced into artificial linear chains. They qualify multiple chains simultaneously.

| ID | Axis | Required control |
|---|---|---|
| A01 | Differential geometry, topology, and state-space representation | Name the mathematical structure precisely and test whether it is operationally necessary. |
| A02 | Spatial and temporal scale | Declare resolution, horizon, aggregation, timescale asymmetry, and cross-scale translation rules. |
| A03 | System boundaries and displaced burdens | Track boundary choices, externalized risks, leakage, rebound, and burden shifting. |
| A04 | Uncertainty, verification, and evidence provenance | Separate observation, inference, assumptions, sensitivity, validation, and falsification. |
| A05 | Ethics, justice, privacy, and safety | Treat non-compensatory harms and distributional safeguards explicitly. |
| A06 | Data availability and computational reproducibility | Record data lineage, code, parameters, environments, benchmarks, and reproducibility status. |

## 5. Non-conflation rules

Every extraction and synthesis must preserve these distinctions:

1. physical forcing is not an observation or a prediction;
2. structural coupling is not identical to statistical association;
3. hazard, component failure, system-function loss, service loss, and human consequence are different variables;
4. a recovery trajectory is not itself a resilience property;
5. viability and reachability are mathematical properties or sets, not synonyms for successful recovery;
6. optimization is a method, not evidence that a decision is implementable or beneficial;
7. sector relevance, efficiency, or lower mass is not a sustainability assessment;
8. aggregate service performance is not evidence of equitable population outcomes;
9. governance or finance feasibility cannot be inferred from technical feasibility;
10. visual elegance or engagement is not physical-system validation or demonstrated decision impact.

## 6. Evidence use

For each source, reviewers must assign evidence separately to C01–C10 and A01–A06 using the repository evidence states. A chain may be `OBSERVED`, `OBSERVED_PARTIAL`, `INFERRED`, `PROPOSED`, `NOT_OBSERVED`, `NOT_VERIFIED`, or `NOT_APPLICABLE`. `NOT_APPLICABLE` requires a source- or candidate-specific rationale. Coverage of one link does not establish the entire chain. A paper cannot be credited with an endpoint unless that endpoint is explicitly defined and supported by the checked evidence.

The architecture is extensible. A new chain may be added when verified evidence identifies a distinct ordered mechanism that cannot be represented faithfully as a link, feedback, or cross-cutting axis. Chains must not be added merely because a topic is important.

## 7. Selection boundary

The architecture organizes evidence across candidate domains; it does not rank or select those domains. Coupled Power-Water-Transportation-Solid-Waste infrastructure under urban flooding remains one incomplete candidate with no privileged status. Any future application must still pass the repository's [application-domain selection protocol](APPLICATION_DOMAIN_SELECTION.md).
