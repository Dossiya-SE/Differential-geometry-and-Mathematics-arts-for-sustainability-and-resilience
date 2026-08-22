---
review_id: MSR-SR-001
version: 0.3.1
date: 2026-08-22
status: Phase-0 landscape scoping review
decision: application NOT_SELECTED
---

# Application-Scope Landscape Review

## Differential geometry and mathematical art for sustainability and resilience

## Abstract

### Background

The project seeks an application in which differential geometry and mathematical art make scientifically defensible contributions to sustainability and resilience. Its initial ten-family search frame was intentionally broad, but it had not been tested against a cross-domain literature map.

### Objective

This Phase-0 scoping review identifies the application-scope universe, distinguishes differential geometry from adjacent geometric methods, maps direct and missing outcome evidence, and defines what must be verified before any domain is selected.

### Methods

Sixty-four targeted discovery queries were executed across methodology, ten initial application families, Earth/climate dynamics, urban morphology, digital twins, finance/governance, and mathematical art. Forty-two anchor records were charted after publisher, DOI, national-academy, government-laboratory, or institutional verification. Sources were coded separately for differential geometry, sustainability, resilience, and mathematical-art/visualization evidence. The method is aligned with JBI guidance and PRISMA-ScR reporting principles (Peters et al., 2020; Tricco et al., 2018), but it is explicitly not a completed systematic scoping review: it has no enumerated database corpus, dual independent screening, full-text exclusion flow, or risk-of-bias appraisal.

### Results

The search frame expands from ten to twelve primary families by adding (11) Earth/climate-system dynamics, extremes, tipping, and projection manifolds and (12) urban morphology, spatial planning, heat, accessibility, and land-use resilience. Digital twins, mathematical art, and finance/governance are better treated as cross-cutting layers than primary application domains. Explicit differential geometry is strongest in power-flow manifolds, architectural geometry and shape design, climate attractor manifolds, and biological shape formation (Falasca & Bracco, 2022; Goodwin et al., 2026; Huang et al., 2018; Kodnongbua et al., 2025; Pottmann et al., 2015; Wolter & Berger, 2019). Direct sustainability or resilience evidence is often supplied by adjacent fields—network science, topological data analysis, optimal transport, shape calculus, dynamical systems, and geometric morphometrics—without establishing differential-geometric necessity (Ibrahim et al., 2022; Larson et al., 2023; Schlegel & Schulz, 2021; Selicato et al., 2025). Empirical climate-art studies support communication and engagement functions but not physical-system validation (Li et al., 2023; Lindborg et al., 2023; Metze, 2020).

### Conclusion

No single curated anchor jointly operationalizes explicit differential geometry, quantified sustainability, quantified resilience, and a validated mathematical-art function. This provisional bridge deficit defines the research opportunity and the principal risk. The review expands candidate generation but does not rank families or select an application.

## 1. Decision boundary

The application remains `NOT_SELECTED`. This review asks where a defensible project *could* be constructed; it does not ask which broad sector is most attractive. A search family is not a scientific problem, and a paper is not an application decision.

The eventual unit of comparison remains

$$
A_i=(S_i,H_i,O_i,L_i,G_i,D_i,V_i),
$$

where $S$ is the bounded system, $H$ the disturbance or transition, $O$ a measurable sustainability-resilience outcome, $L$ the spatial-temporal scale, $G$ the geometric role, $D$ the data and validation pathway, and $V$ the mathematical-art function. None of the family labels below satisfies this specification by itself.

## 2. Review method and evidentiary limits

The protocol, exact queries, source-level coding, and machine-readable record are provided in [`REVIEW_PROTOCOL.md`](REVIEW_PROTOCOL.md), [`SEARCH_LOG.csv`](SEARCH_LOG.csv), [`ANCHOR_EVIDENCE_MATRIX.csv`](ANCHOR_EVIDENCE_MATRIX.csv), and [`SCOPE_REVIEW_RECORD.yaml`](SCOPE_REVIEW_RECORD.yaml).

The method is a landscape scoping review, not an effect review or meta-analysis. The evidence map is designed to prevent three category errors:

1. **Mathematical error:** treating every use of topology, optimal transport, networks, or manifold learning as differential geometry.
2. **Outcome error:** treating sector relevance, efficiency, accuracy, or robustness as demonstrated sustainability or resilience.
3. **Art-validation error:** treating an expressive visualization as evidence that a physical, ecological, or operational claim is true.

The synthesis uses conventional author–date citations. Audit identifiers are retained only in the reference list and evidence matrix, where each anchor establishes only the fields coded for it. `NOT_OBSERVED` means not observed in the checked source record, and absence from the map means not yet identified in this phase.

## 3. Mathematical ontology for candidate generation

### 3.1 Explicit differential geometry

The central class includes smooth or stratified manifolds, tangent and normal spaces, Riemannian metrics, curvature, geodesics, connections, differential forms, geometric flows, and shape spaces. Power-flow geometry provides an unusually explicit engineering instance: the feasible solution set is treated as a smooth manifold and analyzed through induced metrics, geodesics, curvature tensors, scalar curvature, and second fundamental forms (Goodwin et al., 2026; Maack et al., 2024; Wolter & Berger, 2019). Climate attractor geometry and biological shape formation provide other explicit state-space or form-space instances (Falasca & Bracco, 2022; Ghil, 2017; Huang et al., 2018).

### 3.2 Adjacent geometric mathematics

Topological data analysis, network topology, optimal transport, geometric morphometrics, shape calculus, and geometric optimization are relevant but must be named precisely. Persistent homology can quantify water-network resilience and ecosystem-state transitions (Larson et al., 2023; Selicato et al., 2025). Optimal transport can route flows across transport or supply networks while representing structural mismatch (Ibrahim et al., 2022; Seyedi et al., 2026). These are strong application bridges, but they do not automatically pass the project's differential-geometric-necessity gate.

### 3.3 Learned manifolds and reduced state spaces

Manifold learning can expose low-dimensional organization in high-dimensional climate, health, or infrastructure data. Its scientific value depends on stability, interpretability, out-of-sample behavior, and a validation target. Calling an embedding a manifold does not establish that intrinsic metric, curvature, or geodesic structure is meaningful.

### 3.4 Dynamics, viability, and recovery

Resilience is inherently temporal. Attractors, bifurcations, reachability, viability kernels, recovery trajectories, and control laws can define persistence and adaptation more rigorously than a static score. Dynamical-systems climate studies establish the relevance of attractors and bifurcations (Falasca & Bracco, 2022; Ghil, 2017), while interdependent-infrastructure studies show why cascading failure and coupled recovery must be represented (Buldyrev et al., 2010; Danziger & Barabási, 2022; Ouyang, 2014; Ouyang & Wang, 2015).

### 3.5 Mathematical art and visual encoding

Mathematical art is scientifically admissible when its mapping is explicit: state to color or form, uncertainty to texture or transparency, curvature to surface or line behavior, recovery trajectory to animation, distribution to sound, or feasible set to spatial composition. Empirical studies indicate that artistic representations can alter emotion and perceived climate relevance without necessarily improving credibility or learning (Li et al., 2023), and that climate sonification/visualization is a substantial design practice with heterogeneous aims (Lindborg et al., 2023). Therefore art can support exploration, participation, memory, and communication, but cannot replace validation.

## 4. Expanded application-scope universe

The original ten-family frame is retained and expanded by two distinct system classes. The table reports evidence patterns, not rankings.

| ID | Primary family | Illustrative subscopes | Strongest observed mathematical role | Direct outcome evidence in anchors | Principal gap before candidacy |
|---|---|---|---|---|---|
| SF-001 | Coupled critical infrastructure | Interdependent lifelines; cascading failure; restoration; interface control; cross-sector investment | Multilayer networks, percolation, coupled recovery dynamics | Resilience is direct in infrastructure studies (Buldyrev et al., 2010; Danziger & Barabási, 2022; Ouyang, 2014; Ouyang & Wang, 2015) | Explicit differential geometry and sustainability accounting are usually absent; boundary and dependency data are difficult |
| SF-002 | Climate-adaptive buildings, structures, and materials | Passive envelopes; low-carbon members; shells; architected materials; damage-aware retrofit | Architectural/discrete geometry, shape and topology optimization, geometric mechanics | Carbon and mechanical resilience appear in separate studies (Bai et al., 2025; Meza et al., 2015; Pottmann et al., 2015) | A single formulation must connect embodied/operational impacts to hazard response and recovery |
| SF-003 | Energy systems, microgrids, and storage | AC power flow; optimal power flow; microgrid islanding; storage state spaces; restoration | Smooth power-flow manifolds, Riemannian optimization, and curvature (Goodwin et al., 2026; Maack et al., 2024; Roslan et al., 2019; Wolter & Berger, 2019) | Operational/energy-management outcomes exist; direct joint sustainability-resilience evidence is incomplete | Convert elegant manifold structure into measurable emissions, service continuity, recovery, and uncertainty benefits |
| SF-004 | Water, drainage, coastal, and blue-green systems | Distribution; sewer flooding; coastal erosion; nature-based drainage; drought allocation | Persistent homology, shape calculus, and multiobjective optimization (Bakhshipour et al., 2021; Schlegel & Schulz, 2021; Selicato et al., 2025; Yazdi, 2018) | Direct resilience metrics, flood/erosion reduction, and cost outcomes occur | Classical differential-geometric necessity and ecological co-benefit validation remain weak |
| SF-005 | Transportation, mobility, and evacuation | Multimodal routing; carbon-aware transport; disruption recovery; accessibility; evacuation | Optimal transport, multilayer networks, and network topology (Ganin et al., 2017; Ibrahim et al., 2022; Zhang et al., 2015) | Emissions, congestion, efficiency, and resilience are directly evaluated in separate studies | Equity, recovery dynamics, and an intrinsic geometric model must be joined without conflating network topology with DG |
| SF-006 | Circular materials, waste, and industrial ecology | Industrial symbiosis; closed-loop supply; material flows; collection; sorting and disassembly | Network analysis, Gromov–Wasserstein transport, and mathematical optimization (Chopra & Khanna, 2014; Sandoval-Reyes et al., 2024; Seyedi et al., 2026) | Resource-flow sustainability and network resilience are explicit in parts of the literature | Physical recovery, uncertainty, and necessity of differential geometry are not yet established |
| SF-007 | Ecology, landscape, biodiversity, and restoration | Niche geometry; ecosystem states; connectivity; habitat restoration; disturbance recovery | Niche geometry, TDA, landscape graphs, and state-space dynamics (Goyal et al., 2025; Larson et al., 2023; Mitchell et al., 2013) | Perturbation response, state transitions, restoration relevance, and ecosystem services are direct or strongly contextual | Link mathematical invariants to intervention outcomes, uncertainty, and multiple sustainability values |
| SF-008 | Food, agriculture, and coupled human-natural systems | Plant form; phenotyping; agroecosystems; food networks; land-water-food coupling | Geometric morphometrics, TDA, growth geometry, and network resilience (Huang et al., 2018; Karan et al., 2023; Noshita et al., 2022) | Morphology and food-system resilience are observed in separate strands | Bridge organism-scale form to system-scale resource use, climate adaptation, and recovery |
| SF-009 | Community services, public health, and humanitarian logistics | Emergency services; health access; relief distribution; community recovery; service restoration | Hyperbolic embeddings, network design, optimization, and coupled restoration (Anjomshoae et al., 2025; Karakoc et al., 2019; Wen et al., 2025) | Resilience, logistics sustainability, and service recovery are present | Distributional validity, causal evidence, privacy, and differential-geometric necessity require strong safeguards |
| SF-010 | Multiscale geometric design | Shape grammars; inverse design; form-performance co-design; fabrication; recovery-aware generative design | Shape spaces, differentiable grammar, geometric optimization, and visualization (Bai et al., 2025; Kodnongbua et al., 2025; Meza et al., 2015; Pottmann et al., 2015) | Manufacturability and optimization are direct; sustainability/resilience are mostly not jointly evaluated | Add life-cycle and disturbance-response objectives plus physical validation; art cannot stand in for performance |
| SF-011 | Earth and climate-system dynamics | Attractors; extremes; tipping; atmospheric rivers; model projection manifolds | Attractor manifolds, TDA, dynamical systems, and manifold learning (Falasca & Bracco, 2022; Ghil, 2017; Muszynski et al., 2019) | Climate-pattern recognition and dynamical structure are direct; adaptation outcomes are not | Translate planetary-state geometry to actionable, falsifiable resilience decisions across scales |
| SF-012 | Urban morphology, spatial planning, heat, accessibility, and land use | Street networks; heat form; compactness; access; land-use transition | Spatial morphology, graph metrics, and geometric/spatial optimization (Sharifi, 2019; Zhang et al., 2023) | Reviews connect form to multiple sustainability/resilience outcomes | Metric proliferation, causal identification, Global South coverage, and explicit DG remain unresolved |

The full 60-row decomposition is in [`SCOPE_TAXONOMY.csv`](SCOPE_TAXONOMY.csv).

## 5. Family syntheses

### 5.1 Coupled critical infrastructure

Interdependency is scientifically substantive: failures and recoveries can propagate across physical, informational, geographic, and organizational couplings (Buldyrev et al., 2010; Danziger & Barabási, 2022; Ouyang, 2014; Ouyang & Wang, 2015). The literature supplies strong network and restoration formulations, making this family a legitimate resilience search space. It does not, by itself, justify a particular four-sector P-W-T-SW boundary, urban flooding, or differential geometry. A candidate must prove that a manifold, hybrid state space, geometric control formulation, or other geometric structure improves a defined decision over established multilayer-network and optimization baselines. Sustainability must be measured rather than attached as a contextual label.

### 5.2 Buildings, structures, and materials

This family has natural geometric design variables and physical validation routes. Architected metamaterials show how hierarchical geometry can produce recoverable mechanical behavior (Meza et al., 2015). Architectural geometry and form-finding expose differential- and discrete-geometric constraints (Pottmann et al., 2015). Low-carbon structural studies show how material capacity and carbon can enter design decisions (Bai et al., 2025). The missing bridge is consequential: low carbon, hazard resistance, repairability, and recovery time are commonly optimized in separate frameworks. A strong candidate would define life-cycle emissions and a disturbance-response trajectory on the same admissible design space.

### 5.3 Energy systems

Power systems currently provide the clearest direct evidence that classical differential geometry is operational rather than decorative. Power-flow solution sets are treated as smooth manifolds; Riemannian metrics, geodesics, intrinsic and extrinsic curvature, and Riemannian optimization have computational roles (Goodwin et al., 2026; Maack et al., 2024; Wolter & Berger, 2019). Microgrid control literature supplies sustainability and operational context (Roslan et al., 2019). The opportunity is not to rebrand optimal power flow as resilience. It is to test whether geometric structure improves continuation, stability-boundary detection, restoration, uncertainty propagation, or control while emissions, resource use, unserved energy, and recovery are measured.

### 5.4 Water, drainage, coastal, and blue-green systems

This family has several outcome-grounded adjacent-geometric anchors. Persistent homology has been used to construct resilience information for water distribution networks (Selicato et al., 2025). Drainage optimization and rehabilitation work directly evaluates flood, service, and investment outcomes (Bakhshipour et al., 2021; Yazdi, 2018). Shape calculus has been applied to erosion-mitigation geometry under shallow-water equations (Schlegel & Schulz, 2021). A defensible candidate could couple hydraulic state-space geometry with topological redundancy or shape design, but should not label persistent homology or multiobjective optimization as differential geometry. Blue-green ecological co-benefits and distributional effects require separate measurement.

### 5.5 Transportation, mobility, and evacuation

Optimal transport and multilayer-network methods support carbon-aware routing, congestion distribution, and structural analysis (Ibrahim et al., 2022). Transportation-resilience studies define efficiency and topology-dependent disruption behavior (Ganin et al., 2017; Zhang et al., 2015). The family therefore has measurable operational baselines. Its central risk is method substitution: an optimal-transport or graph-theoretic project may be valuable while failing the stated differential-geometry gate. Equity in access and evacuation, behavioral adaptation, and recovery over time also need to be explicit.

### 5.6 Circular materials, waste, and industrial ecology

Industrial-symbiosis networks directly connect resource exchange to resilience questions (Chopra & Khanna, 2014). Geometric optimal transport has been proposed for structural and attribute mismatch in closed-loop supply networks (Seyedi et al., 2026), and waste-system optimization supplies decision context (Sandoval-Reyes et al., 2024). This family is promising for flow geometry and structural comparison, but current anchors do not show that differential geometry is necessary or that post-disruption recovery is validated. Material quality degradation, reverse-logistics uncertainty, and rebound effects must be included.

### 5.7 Ecology, landscape, biodiversity, and restoration

Ecosystem evidence offers unusually meaningful state-space interpretations. Niche geometry has been related to response under environmental perturbations (Goyal et al., 2025). Persistent homology has identified ecosystem states and transitions in long-running river data, with rehabilitation relevance (Larson et al., 2023). Landscape connectivity literature connects spatial structure to ecosystem-service provision while recording research gaps (Mitchell et al., 2013). The challenge is to validate that a geometric invariant predicts or improves intervention outcomes beyond standard ecological models and to represent multiple values without reducing resilience to one scalar.

### 5.8 Food, agriculture, and coupled human-natural systems

Plant geometry and morphometrics provide fine-scale, observable shape data (Huang et al., 2018; Noshita et al., 2022), while food-system studies provide network-level resilience outcomes (Karan et al., 2023). The evidence currently spans different scales rather than forming a single bridge. Candidate generation should therefore distinguish plant or canopy form, agroecosystem resource dynamics, and regional food-network recovery. A multiscale candidate must specify how shape information propagates to water, carbon, yield stability, accessibility, or recovery rather than assuming that better phenotyping produces sustainability.

### 5.9 Community service, health, and humanitarian logistics

Humanitarian supply reviews show that sustainability and resilience can be joint planning concerns (Anjomshoae et al., 2025). Hyperbolic embeddings have been applied to hierarchical community public-health resilience assessment (Wen et al., 2025), while restoration models examine community effects of interdependent services (Karakoc et al., 2019). These scopes are high-stakes. Predictive accuracy is insufficient: calibration, causal validity, missingness, distributional impact, privacy, and meaningful community participation are eligibility issues. Mathematical art may support participatory sense-making only if encodings and interpretive risks are tested.

### 5.10 Multiscale geometric design

Shape grammars, differentiable representations, and inverse design make geometry a direct design object (Kodnongbua et al., 2025). This family can connect mathematical art and engineering unusually well, because a visual form may also be a parameterized feasible design. However, the focal *Design for Descent* case study demonstrates optimization and fabrication rather than sustainability or resilience outcomes (Kodnongbua et al., 2025). The next bridge must introduce life-cycle, resource, service, and recovery objectives plus physical or simulation validation. Visual elegance is not a substitute for those additions.

### 5.11 Earth and climate-system dynamics

Climate dynamics warrants a distinct family because the system object is a planetary, multiscale dynamical state rather than a local infrastructure or ecological asset. Low-dimensional attractor geometry, TDA of atmospheric patterns, and bifurcation analysis provide direct mathematical roles (Falasca & Bracco, 2022; Ghil, 2017; Muszynski et al., 2019). The difficult translation is from recognizable manifold or topological structure to an actionable adaptation, early-warning, or model-selection decision with uncertainty and false-alarm costs. Climate prediction skill is not identical to community resilience.

### 5.12 Urban morphology and spatial planning

Street networks, built form, land use, heat, and accessibility combine geometry with many sustainability and resilience outcomes (Sharifi, 2019; Zhang et al., 2023). The literature also reveals a methodological problem: hundreds of spatial measures coexist, with uneven links to outcomes and geographic bias (Zhang et al., 2023). This is a valid domain for geometric causal and optimization research, but a candidate must identify a specific intervention and disturbance, show why the chosen representation is identifiable and transferable, and avoid treating visual urban form as an outcome.

## 6. Cross-cutting enabling layers

Some discovered areas should not become standalone application families because they do not define the affected system and outcome.

| Layer | Function | Why it is cross-cutting |
|---|---|---|
| Differential geometry and shape spaces | Formal state/design representation; intrinsic metrics; curvature; geodesics; geometric flows | Supplies mathematics across sectors but does not define a sustainability problem |
| Topology, networks, optimal transport, and TDA | Connectivity, persistence, structural comparison, and flow allocation | Often provides strong direct evidence, but is adjacent to rather than synonymous with DG |
| Dynamics, viability, control, and optimization | Disturbance, recovery, admissibility, and intervention | Defines temporal performance across all families |
| Inverse problems, sensing, uncertainty, and digital twins | State estimation, calibration, scenario updating, and human-in-the-loop decisions | A digital twin is an architecture around a chosen system, not an application outcome (National Academies of Sciences, Engineering, and Medicine, 2024) |
| Mathematical art, visualization, sonification, and participation | Exploration, explanation, memory, deliberation, and design generation | Functions across domains and requires an explicit encoding and evaluation target (Li et al., 2023; Lindborg et al., 2023; Metze, 2020) |
| Equity, ethics, finance, governance, and implementation | Distribution, legitimacy, investment, safety, and institutional feasibility | Constrains every application but does not establish geometric necessity by itself |

Climate-risk finance is therefore retained as a decision layer unless a bounded financial-system resilience question demonstrates an operational geometric role. Digital twins are retained as a data-model-decision architecture. Mathematical art is retained as a cross-cutting function unless communication or participation is itself the focal measurable outcome.

## 7. The four-way bridge deficit

The mapped literature is fragmented along four axes:

- **Geometry-rich sources** often optimize or characterize form and state without measuring sustainability or recovery.
- **Sustainability sources** often measure carbon, resources, ecosystem services, or equity without explicit differential geometry.
- **Resilience sources** often use networks, simulation, optimization, or topology rather than classical differential geometry.
- **Mathematical-art sources** often evaluate attention, emotion, engagement, or interpretation without linking those effects to validated physical-system outcomes.

Within the 42-anchor map, no single source jointly provides all four. This is not evidence that no such paper exists. It is evidence that the project cannot assume a ready-made unified literature and must construct and validate explicit bridges.

The strongest partial bridges are:

1. **Power:** explicit differential geometry plus operational computation (Goodwin et al., 2026; Maack et al., 2024; Wolter & Berger, 2019); sustainability and resilience outcomes require integration.
2. **Ecology:** geometry or topology plus perturbation/state transition (Goyal et al., 2025; Larson et al., 2023); intervention and sustainability valuation require integration.
3. **Water:** topology or shape calculus plus direct resilience/mitigation (Schlegel & Schulz, 2021; Selicato et al., 2025; Yazdi, 2018); classical DG and multi-benefit sustainability require integration.
4. **Transport/circularity:** optimal-transport geometry plus emissions, congestion, or structural sustainability (Ibrahim et al., 2022; Seyedi et al., 2026); recovery and classical DG require integration.
5. **Geometric design:** parameterized form plus differentiability and fabrication (Bai et al., 2025; Kodnongbua et al., 2025; Meza et al., 2015; Pottmann et al., 2015); life-cycle and recovery validation require integration.
6. **Climate communication:** empirical art/visualization effects (Li et al., 2023; Lindborg et al., 2023; Metze, 2020); these validate communication functions, not physical resilience.

## 8. Search-scope specifications for future candidate generation

The following are *problem forms*, not nominated candidates. Each must be narrowed to a system, stressor, outcome, scale, data path, and validation design.

| Family | Candidate-generating problem form |
|---|---|
| Critical infrastructure | Geometry of viable service states and coupled recovery trajectories under multi-network disruption |
| Buildings/materials | Shape-space optimization of carbon, hazard damage, reparability, and recovery time |
| Energy | Riemannian power-flow or storage-state methods for low-carbon service continuity and restoration |
| Water/coastal | Geometry/topology of hydraulic viability and adaptive intervention under flood, drought, or erosion |
| Transportation | Carbon-, access-, and recovery-aware flow geometry under disruption and behavioral adaptation |
| Circular systems | Geometric comparison and control of closed-loop material flows under supplier, quality, or logistics shocks |
| Ecology/restoration | State-space or niche geometry as a predictor and design variable for restoration under disturbance |
| Food/agriculture | Multiscale geometry linking biological form and landscape organization to resource use and yield recovery |
| Community/health/logistics | Geometry of equitable service accessibility and restoration under emergencies, with participatory validation |
| Multiscale design | Differentiable form generation constrained by life-cycle resources, physical performance, repair, and recovery |
| Earth/climate | Geometric early-warning or model-evaluation methods tied to explicit adaptation decisions and uncertainty costs |
| Urban morphology | Causally validated morphology interventions for heat, access, resource demand, and post-disturbance recovery |

These forms become candidates only after complete tuples are entered into the candidate register. They carry no priority and no score.

## 9. Evidence gaps that apply across families

### 9.1 Outcome coupling

Sustainability and resilience must be co-defined. Lower nominal resource use can reduce redundancy; greater robustness can increase embodied material; rapid recovery can shift burdens to vulnerable groups. A candidate should expose these trade-offs rather than merge them into an unvalidated composite score.

### 9.2 Geometric necessity

Every candidate needs a baseline test: what decision or prediction fails, degrades, or becomes less interpretable without the proposed geometric structure? Euclidean, graph, standard optimization, and non-geometric machine-learning comparators should be specified before the geometric method is treated as necessary.

### 9.3 Temporal semantics

Resilience requires a declared disturbance and trajectory: performance loss, response, recovery, adaptation, transformation, or viability. Static robustness, centrality, classification accuracy, or visual complexity alone is insufficient.

### 9.4 Scale and boundary

Form-to-system and local-to-regional translations require conservation laws, aggregation rules, or causal models. A multiscale label does not supply them. System boundaries must include displaced carbon, resource, risk, and labor burdens where material.

### 9.5 Validation and uncertainty

Candidates require benchmark data or simulations, held-out or prospective tests where appropriate, sensitivity and uncertainty analysis, physical constraints, and falsification criteria. Learned manifolds and digital twins additionally require drift, observability, calibration, and update rules.

### 9.6 Art evaluation

The visual or generative mapping must be reproducible. Evaluation should match function: task accuracy for analytical visualization; comprehension and calibrated trust for communication; option diversity and constraint satisfaction for generative design; deliberative quality and accessibility for participation. Aesthetic preference alone does not establish scientific value.

### 9.7 Ethics and distribution

Aggregate efficiency or recovery can conceal unequal exposure, access, displacement, and benefit. Distributional metrics, affected-population participation, privacy, safety, and governance are non-compensatory eligibility concerns.

## 10. Implications for application selection

This review changes the selection process in five ways:

1. the candidate-generation frame is expanded to twelve families;
2. digital twins, mathematical art, and finance/governance are classified as enabling or decision layers, preventing category inflation;
3. adjacent geometric methods are preserved as evidence without being mislabeled as differential geometry;
4. the four-way bridge deficit becomes an explicit research and validation risk;
5. no family advances to eligibility screening until it is converted into one or more complete application tuples with evidence dossiers.

The prior P-W-T-SW urban-flooding concept remains one incomplete, unscreened candidate. Nothing in this review privileges it.

## 11. Limitations

The map is preliminary. It uses targeted web discovery rather than a reproducible export from multiple scholarly databases; retains no stable hit counts; relies mainly on publisher or institutional metadata and abstracts; does not include formal dual screening or quality appraisal; and is biased toward English-language terminology. The 42 anchors demonstrate scope structure and evidence patterns, not corpus prevalence. New families or subscopes may be added when verified evidence shows that they are distinct and materially relevant.

## 12. Conclusion

The credible application universe is broader than the initial list but can remain scientifically controlled. Twelve primary application families cover engineered, ecological, climatic, spatial, and social-service systems; six cross-cutting layers organize mathematics, dynamics, data, art, and implementation. The literature contains strong partial bridges, but the complete intersection of differential geometry, quantified sustainability, quantified resilience, and validated mathematical art is not yet established in this corpus. The rigorous next move is deeper, candidate-specific evidence synthesis—not premature selection.

## References

References are listed alphabetically in author–date format. The `Audit ID` attached to each entry is a secondary crosswalk to [`ANCHOR_EVIDENCE_MATRIX.csv`](ANCHOR_EVIDENCE_MATRIX.csv); it is not the scholarly citation.

Anjomshoae, A., Banomyong, R., Hossein Azadnia, A., Kunz, N., & Blome, C. (2025). Sustainable humanitarian supply chains: A systematic literature review and research propositions. *Production Planning & Control, 36*(3), 357–377. https://doi.org/10.1080/09537287.2023.2273451. Audit ID A030.

Bai, J., Yang, K., Chen, Z., Liang, J., Zhang, S., & Diao, Y. (2025). Geometry and material criteria for low-carbon design of I/H-beams in sustainable steel structures considering both mechanical properties and carbon emissions. *Materials, 18*(21), 4930. https://doi.org/10.3390/ma18214930. Audit ID A009.

Bakhshipour, A. E., Hespen, J., Haghighi, A., Dittmer, U., & Nowak, W. (2021). Integrating structural resilience in the design of urban drainage networks in flat areas using a simplified multi-objective optimization framework. *Water, 13*(3), 269. https://doi.org/10.3390/w13030269. Audit ID A014.

Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., & Havlin, S. (2010). Catastrophic cascade of failures in interdependent networks. *Nature, 464*(7291), 1025–1028. https://doi.org/10.1038/nature08932. Audit ID A004.

Chopra, S. S., & Khanna, V. (2014). Understanding resilience in industrial symbiosis networks: Insights from network analysis. *Journal of Environmental Management, 141*, 86–94. https://doi.org/10.1016/j.jenvman.2013.12.038. Audit ID A021.

Danziger, M. M., & Barabási, A.-L. (2022). Recovery coupling in multilayer networks. *Nature Communications, 13*, 955. https://doi.org/10.1038/s41467-022-28379-5. Audit ID A006.

Falasca, F., & Bracco, A. (2022). Exploring the tropical Pacific manifold in models and observations. *Physical Review X, 12*, 021054. https://doi.org/10.1103/PhysRevX.12.021054. Audit ID A037.

Ganin, A. A., Kitsak, M., Marchese, D., Keisler, J. M., Seager, T., & Linkov, I. (2017). Resilience and efficiency in transportation networks. *Science Advances, 3*(12), e1701079. https://doi.org/10.1126/sciadv.1701079. Audit ID A019.

Ghil, M. (2017). The wind-driven ocean circulation: Applying dynamical systems theory to a climate problem. *Discrete and Continuous Dynamical Systems, 37*(1), 189–228. https://doi.org/10.3934/dcds.2017008. Audit ID A039.

Goodwin, A., Maack, J., & Sigler, D. (2026). Power flow geometry and approximation. *IEEE Transactions on Power Systems, 41*(2), 982–993. https://doi.org/10.1109/TPWRS.2025.3612220. Audit ID A010.

Goyal, A., Rocks, J. W., & Mehta, P. (2025). Universal niche geometry governs the response of ecosystems to environmental perturbations. *PRX Life, 3*, 013010. https://doi.org/10.1103/PRXLife.3.013010. Audit ID A024.

Huang, C., Wang, Z., Quinn, D., Suresh, S., & Hsia, K. J. (2018). Differential growth and shape formation in plant organs. *Proceedings of the National Academy of Sciences, 115*(49), 12359–12364. https://doi.org/10.1073/pnas.1811296115. Audit ID A028.

Ibrahim, A. A., Leite, D., & De Bacco, C. (2022). Sustainable optimal transport in multilayer networks. *Physical Review E, 105*, 064302. https://doi.org/10.1103/PhysRevE.105.064302. Audit ID A018.

Karakoc, D. B., Almoghathawi, Y., Barker, K., González, A. D., & Mohebbi, S. (2019). Community resilience-driven restoration model for interdependent infrastructure networks. *International Journal of Disaster Risk Reduction, 38*, 101228. https://doi.org/10.1016/j.ijdrr.2019.101228. Audit ID A032.

Karan, E. P., Asgari, S., & Asadi, S. (2023). Resilience assessment of centralized and distributed food systems. *Food Security, 15*(1), 59–75. https://doi.org/10.1007/s12571-022-01321-9. Audit ID A029.

Kodnongbua, M., Zhang, Z. J., Sharp, N., & Schulz, A. (2025). Design for descent: What makes a shape grammar easy to optimize? In *SIGGRAPH Asia 2025 Conference Papers*. Association for Computing Machinery. https://doi.org/10.1145/3757377.3764004. Audit ID A033.

Larson, D. M., Bungula, W., McKean, C., Stockdill, A., Lee, A., Miller, F. F., & Davis, K. (2023). Quantifying ecosystem states and state transitions of the Upper Mississippi River System using topological data analysis. *PLOS Computational Biology, 19*(6), e1011147. https://doi.org/10.1371/journal.pcbi.1011147. Audit ID A025.

Li, N., Villanueva, I. I., Jilk, T., Van Matre, B. R., & Brossard, D. (2023). Artistic representations of data can help bridge the US political divide over climate change. *Communications Earth & Environment, 4*, 195. https://doi.org/10.1038/s43247-023-00856-9. Audit ID A034.

Lindborg, P., Lenzi, S., & Chen, M. (2023). Climate data sonification and visualization: An analysis of topics, aesthetics, and characteristics in 32 recent projects. *Frontiers in Psychology, 13*, 1020102. https://doi.org/10.3389/fpsyg.2022.1020102. Audit ID A035.

Maack, J., Sigler, D., & Goodwin, A. (2024). Riemannian optimization applied to AC optimal power flow: Preprint. Paper presented at the *2024 IEEE Power & Energy Society General Meeting*, Seattle, WA. National Laboratory of the Rockies, NREL/CP-2C00-88090. https://research-hub.nlr.gov/en/publications/riemannian-optimization-applied-to-ac-optimal-power-flow-preprint/. Audit ID A011.

Metze, T. (2020). Visualization in environmental policy and planning: A systematic review and research agenda. *Journal of Environmental Policy & Planning, 22*(5), 745–760. https://doi.org/10.1080/1523908X.2020.1798751. Audit ID A036.

Meza, L. R., Zelhofer, A. J., Clarke, N., Mateos, A. J., Kochmann, D. M., & Greer, J. R. (2015). Resilient 3D hierarchical architected metamaterials. *Proceedings of the National Academy of Sciences, 112*(37), 11502–11507. https://doi.org/10.1073/pnas.1509120112. Audit ID A007.

Mitchell, M. G. E., Bennett, E. M., & Gonzalez, A. (2013). Linking landscape connectivity and ecosystem service provision: Current knowledge and research gaps. *Ecosystems, 16*(5), 894–908. https://doi.org/10.1007/s10021-013-9647-2. Audit ID A026.

Muszynski, G., Kashinath, K., Kurlin, V., Wehner, M., & Prabhat. (2019). Topological data analysis and machine learning for recognizing atmospheric river patterns in large climate datasets. *Geoscientific Model Development, 12*, 613–628. https://doi.org/10.5194/gmd-12-613-2019. Audit ID A038.

National Academies of Sciences, Engineering, and Medicine. (2024). *Foundational research gaps and future directions for digital twins*. National Academies Press. https://doi.org/10.17226/26894. Audit ID A042.

Noshita, K., Murata, H., & Kirie, S. (2022). Model-based plant phenomics on morphological traits using morphometric descriptors. *Breeding Science, 72*(1), 19–30. https://doi.org/10.1270/jsbbs.21078. Audit ID A027.

Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040. Audit ID A003.

Ouyang, M., & Wang, Z. (2015). Resilience assessment of interdependent infrastructure systems: With a focus on joint restoration modeling and analysis. *Reliability Engineering & System Safety, 141*, 74–82. https://doi.org/10.1016/j.ress.2015.03.011. Audit ID A005.

Peters, M. D. J., Marnie, C., Tricco, A. C., Pollock, D., Munn, Z., Alexander, L., McInerney, P., Godfrey, C. M., & Khalil, H. (2020). Updated methodological guidance for the conduct of scoping reviews. *JBI Evidence Synthesis, 18*(10), 2119–2126. https://doi.org/10.11124/JBIES-20-00167. Audit ID A002.

Pottmann, H., Eigensatz, M., Vaxman, A., & Wallner, J. (2015). Architectural geometry. *Computers & Graphics, 47*, 145–164. https://doi.org/10.1016/j.cag.2014.11.002. Audit ID A008.

Roslan, M. F., Hannan, M. A., Ker, P. J., & Uddin, M. N. (2019). Microgrid control methods toward achieving sustainable energy management: A bibliometric analysis for future directions. *Applied Energy, 240*, 583–607. https://doi.org/10.1016/j.apenergy.2019.02.070. Audit ID A013.

Sandoval-Reyes, M., He, R., Semeano, R., & Ferrão, P. (2024). Mathematical optimization of waste management systems: Methodological review and perspectives for application. *Waste Management, 174*, 630–645. https://doi.org/10.1016/j.wasman.2023.10.006. Audit ID A023.

Schlegel, L., & Schulz, V. (2021). Shape optimization for the mitigation of coastal erosion via shallow water equations. *arXiv*. https://doi.org/10.48550/arXiv.2107.09464. Audit ID A016.

Selicato, L., Pagano, A., Esposito, F., & Icardi, M. (2025). Topological data analysis for resilience assessment of water distribution networks. *Mathematics and Computers in Simulation, 231*, 62–70. https://doi.org/10.1016/j.matcom.2024.12.001. Audit ID A015.

Seyedi, I., Candelieri, A., & Archetti, F. (2026). Geometric optimal transport for sustainable closed-loop supply chain: A fused Gromov–Wasserstein framework for structural and attribute inefficiency diagnosis. *Sustainability, 18*(13), 6906. https://doi.org/10.3390/su18136906. Audit ID A022.

Sharifi, A. (2019). Resilient urban forms: A review of literature on streets and street networks. *Building and Environment, 147*, 171–187. https://doi.org/10.1016/j.buildenv.2018.09.040. Audit ID A040.

Tricco, A. C., Lillie, E., Zarin, W., O'Brien, K. K., Colquhoun, H., Levac, D., Moher, D., Peters, M. D. J., Horsley, T., Weeks, L., Hempel, S., Akl, E. A., Chang, C., McGowan, J., Stewart, L., Hartling, L., Aldcroft, A., Wilson, M. G., Garritty, C., Lewin, S., Godfrey, C. M., Macdonald, M. T., Langlois, E. V., Soares-Weiser, K., Moriarty, J., Clifford, T., Tunçalp, Ö., & Straus, S. E. (2018). PRISMA extension for scoping reviews (PRISMA-ScR): Checklist and explanation. *Annals of Internal Medicine, 169*(7), 467–473. https://doi.org/10.7326/M18-0850. Audit ID A001.

Wen, Q., Ismail, M., & Abdul Nasir, M. H. (2025). A community public health emergency resilience assessment framework based on contrastive learning and hyperbolic embedding. *Frontiers in Public Health, 13*, 1651331. https://doi.org/10.3389/fpubh.2025.1651331. A correction was published in 2026: https://doi.org/10.3389/fpubh.2026.1805132. Audit ID A031.

Wolter, F.-E., & Berger, B. (2019). Differential geometric foundations for power flow computations. *arXiv*. https://doi.org/10.48550/arXiv.1903.11131. Audit ID A012.

Yazdi, J. (2018). Rehabilitation of urban drainage systems using a resilience-based approach. *Water Resources Management, 32*(2), 721–734. https://doi.org/10.1007/s11269-017-1835-y. Audit ID A017.

Zhang, P., Ghosh, D., & Park, S. (2023). Spatial measures and methods in sustainable urban morphology: A systematic review. *Landscape and Urban Planning, 237*, 104776. https://doi.org/10.1016/j.landurbplan.2023.104776. Audit ID A041.

Zhang, X., Miller-Hooks, E., & Denny, K. (2015). Assessing the role of network topology in transportation network resilience. *Journal of Transport Geography, 46*, 35–45. https://doi.org/10.1016/j.jtrangeo.2015.05.006. Audit ID A020.

## Data availability and audit trail

All source-level codes, search strings, scope records, and limitations are contained in this directory. The machine-readable bibliography is in [`scope_review_01.bib`](scope_review_01.bib); audit metadata and persistent links are in [`ANCHOR_EVIDENCE_MATRIX.csv`](ANCHOR_EVIDENCE_MATRIX.csv). The live application decision remains controlled by [`../DECISION_STATUS.yaml`](../DECISION_STATUS.yaml).
