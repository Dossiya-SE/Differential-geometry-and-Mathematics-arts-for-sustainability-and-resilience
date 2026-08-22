# Application-Domain Exploration and Selection Protocol

## 1. Purpose

This protocol prevents premature commitment to a system, hazard, geography, mathematical formalism, or demonstrator. Its purpose is to identify the application domain in which differential geometry and mathematical art can make the most rigorous, useful, and verifiable contribution to sustainability and resilience.

The protocol governs project-level selection. It does not alter the classification of individual reviewed papers.

## 2. Current decision state

`NOT_SELECTED` - No application domain, focal system, hazard or stressor, spatial scale, temporal scale, geography, or demonstrator is frozen.

Coupled Power-Water-Transportation-Solid-Waste infrastructure under urban flooding is one incomplete, unscreened `CANDIDATE`. It must be evaluated under the same rules as every other candidate.

## 3. Candidate-generation scope

Candidate generation must remain broad enough to test the project's central intersection. Candidate families may include, without presuming selection:

1. coupled critical-infrastructure systems;
2. climate-adaptive buildings, structures, and materials;
3. energy systems, microgrids, and storage networks;
4. water, drainage, coastal, and blue-green systems;
5. transportation, mobility, and evacuation networks;
6. circular material, waste, and industrial-ecology systems;
7. ecological, landscape, and restoration systems;
8. food, agriculture, or coupled human-natural systems;
9. community service, health, or humanitarian logistics systems;
10. multiscale geometric design problems connecting form, function, resources, and recovery.
11. Earth and climate-system dynamics, extremes, tipping, and projection manifolds;
12. urban morphology, spatial planning, heat, accessibility, and land-use resilience.

New families may be added when supported by evidence. This list is a search frame, not a ranking.

The Phase-0 landscape review supporting this expansion is [`../application_selection/scope_review_01/SCOPE_REVIEW_01.md`](../application_selection/scope_review_01/SCOPE_REVIEW_01.md). It classifies digital twins and sensing; inverse problems and uncertainty; mathematical art and visualization; and equity, finance, governance, and implementation as cross-cutting enabling or decision layers rather than standalone application families unless a bounded system and outcome justify otherwise.

## 4. Unit of comparison

The unit is a fully specified candidate application tuple

$$
A_i=(S_i,H_i,O_i,L_i,G_i,D_i,V_i),
$$

where:

- $S_i$ is the system and boundary;
- $H_i$ is the hazard, stressor, disturbance, or transition;
- $O_i$ is the sustainability-resilience outcome;
- $L_i$ is the spatial and temporal scale;
- $G_i$ is the proposed geometric or mathematical role;
- $D_i$ is the data and validation pathway;
- $V_i$ is the mathematical-art function and its encoding rules.

A broad label such as "urban resilience" is not a valid candidate until these fields are specified.

## 5. Evidence requirements

Each candidate requires an evidence dossier containing:

- direct application studies with quantified sustainability or resilience outcomes;
- mathematical-method studies supporting the proposed formalism;
- data and measurement sources;
- validation or falsification pathways;
- existing reviews and competing approaches;
- known limitations, negative evidence, and unresolved assumptions;
- a claim-level evidence matrix using the repository evidence statuses.

At least two reviewers or two independent verification passes should check eligibility and scoring before final selection. Exact corpus-size and reviewer-agreement thresholds will be preregistered after the exploratory search establishes the available evidence base; they must not be chosen retrospectively to favor a candidate.

## 6. Stage I: non-compensatory eligibility gates

A candidate advances only if every gate passes. A high score elsewhere cannot compensate for a failed gate.

| Gate | Pass question |
|---|---|
| G1 Scientific fit | Is there a precisely defined problem for which geometry, dynamics, or topology is mathematically material rather than decorative? |
| G2 Sustainability substance | Is at least one environmental, economic, social, or integrated sustainability outcome explicit and measurable? |
| G3 Resilience substance | Are disturbance, degradation or failure, response, recovery or adaptation, and a performance or viability outcome defined? |
| G4 Differential-geometric necessity | Is there a defensible role for manifolds, metrics, curvature, geodesics, connections, geometric flows, shape spaces, stratified spaces, or closely related geometry? |
| G5 Mathematical-art integrity | Can visual or generative form be mapped to defined variables without being treated as validation? |
| G6 Data and observability | Is there a credible path to data, simulation outputs, experiments, or benchmark instances? |
| G7 Validation and falsifiability | Can central claims be tested against a comparator, held-out evidence, physical constraints, or empirical observations? |
| G8 Feasibility | Can a meaningful contribution be completed with available time, computation, expertise, permissions, and data? |
| G9 Ethics and equity | Are affected populations, distributional effects, safety, and misuse risks identifiable and governable? |
| G10 Contribution potential | Is there a demonstrable gap that is neither a renaming exercise nor already resolved by standard methods? |

Gate decisions are `PASS`, `FAIL`, or `UNCERTAIN`, each with citations and a rationale. `UNCERTAIN` does not advance without a dated resolution plan.

## 7. Stage II: comparative assessment

Candidates passing all gates are compared on a common 0-4 anchored scale.

| Score | Interpretation |
|---:|---|
| 0 | No credible evidence |
| 1 | Weak or mostly conceptual evidence |
| 2 | Partial evidence with material gaps |
| 3 | Strong evidence with manageable limitations |
| 4 | Multiple direct, validated, and mutually supporting evidence sources |

The comparison dimensions are:

1. mathematical depth and necessity;
2. strength of direct sustainability evidence;
3. strength of direct resilience evidence;
4. relevance of differential geometry;
5. meaningful role for mathematical art;
6. data availability and measurement quality;
7. model identifiability and uncertainty treatment;
8. validation strength and benchmark availability;
9. real-world usefulness and stakeholder relevance;
10. feasibility within the research horizon;
11. originality and defensible contribution;
12. transferability beyond one case;
13. ethical, safety, and equity governability;
14. reproducibility and open-science potential.

Weights, if used, must be declared before final scoring. Sensitivity analysis must test plausible alternative weights and rating uncertainty. A candidate should not be called robustly preferred if small defensible changes reverse the ranking.

## 8. Decision rule

Selection requires all of the following:

1. every Stage I gate is `PASS`;
2. the candidate has a complete, traceable evidence dossier;
3. comparative scores have been independently checked;
4. uncertainty and weight-sensitivity analyses do not reveal an unstable preference, or the instability is explicitly resolved;
5. a feasibility test or minimal prototype demonstrates that the proposed mathematics can be implemented and evaluated;
6. the selection memo documents alternatives rejected, reasons, limitations, and residual risks.

If no candidate meets these conditions, the correct result is `NO_SELECTION`; the search or project scope must be revised.

## 9. Anti-bias controls

- Do not privilege a candidate because it appeared first, matches prior work, has attractive visuals, or has more popular literature.
- Do not infer direct sustainability or resilience relevance from keywords such as *geometry*, *topology*, *optimization*, *adaptive*, or *green*.
- Do not reuse the same evidence as independent support for multiple criteria without declaring dependence.
- Record negative and null evidence.
- Separate source findings from reviewer inference and project proposals.
- Freeze criteria and weights before final comparative scoring.
- Preserve all candidate records, including rejected candidates.

## 10. Required decision artifacts

Before an application is frozen, the repository must contain:

- `CANDIDATE_REGISTER.csv`;
- one evidence dossier per candidate;
- `ELIGIBILITY_GATES.csv`;
- `COMPARATIVE_SCORECARD.csv`;
- sensitivity and uncertainty analysis code and outputs;
- `APPLICATION_SELECTION_MEMO.md`;
- an updated validation log and versioned decision record.

Until these artifacts exist and the decision rule is satisfied, all named applications remain candidates.
