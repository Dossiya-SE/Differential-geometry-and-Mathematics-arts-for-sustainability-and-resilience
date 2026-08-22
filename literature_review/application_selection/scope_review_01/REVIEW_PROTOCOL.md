# Phase-0 Application-Scope Review Protocol

## 1. Record and purpose

- Review ID: `MSR-SR-001`
- Version: `0.3.1`
- Search date: `2026-08-22`
- Review type: landscape scoping review and evidence map
- Decision effect: candidate generation only; application remains `NOT_SELECTED`

The purpose is to identify the breadth and structure of application domains in which differential geometry or closely related geometric mathematics could make a non-decorative contribution to sustainability and resilience, and in which mathematical art could support analysis, design, or communication through an explicit encoding.

The review follows the problem-framing, transparent eligibility, charting, and reporting principles of JBI scoping-review guidance and PRISMA-ScR (Peters et al., 2020; Tricco et al., 2018). It is not represented as a completed PRISMA-ScR review: this phase does not include subscription-database exports, deduplication counts, dual independent title/abstract screening, full-text screening of an enumerated corpus, risk-of-bias appraisal, or a PRISMA flow diagram.

## 2. Review questions

1. Which application families and subscopes should remain in the project's candidate-generation universe?
2. In which scopes is differential geometry explicit and operational, rather than metaphorical or merely visual?
3. Where are sustainability and resilience outcomes directly defined and measured?
4. Which adjacent geometric methods—topological data analysis, network geometry, optimal transport, shape calculus, manifold learning, and geometric optimization—supply transferable evidence without being mislabeled as differential geometry?
5. What scientifically valid roles can mathematical art, visualization, data physicalization, or sonification play?
6. Which evidence and validation gaps must be resolved before any scope becomes a fully specified application candidate?

## 3. PCC eligibility frame

| Element | Operational scope |
|---|---|
| Population | Engineered, ecological, climatic, urban, material, logistical, public-service, and coupled human-natural systems at any spatial or temporal scale |
| Concept | Operational differential geometry or adjacent geometric mathematics; measurable sustainability and/or resilience; mathematical-art or visualization roles with explicit encodings |
| Context | Any geography, sector, governance setting, hazard, stressor, transition, or recovery regime |

The unit charted in the taxonomy is a `SEARCH_SCOPE`, not a candidate application. A valid application candidate must later instantiate the tuple defined in the governing selection protocol: system, stressor, outcome, scale, mathematical role, data/validation pathway, and mathematical-art function.

## 4. Discovery strategy

Sixty-four targeted web-discovery queries were executed in 16 thematic batches. Searches combined mathematical terms with application, sustainability, resilience, and artistic-communication terms. Candidate sources were then checked against publisher, DOI, government-laboratory, academy, or institutional records. The exact strings are preserved in `SEARCH_LOG.csv`.

The query design intentionally included:

- the original ten search families;
- general mathematical-intersection searches;
- scoping-review methodology;
- Earth/climate dynamics and urban morphology as possible missing families;
- digital twins and sensing as cross-cutting architectures;
- finance and governance as possible cross-cutting decision layers;
- mathematical art, visualization, and sonification.

Discovery was iterative rather than database-exhaustive. Total result counts were not retained because web-search counts are unstable and were not used as inferential data.

## 5. Inclusion criteria

A source could enter the curated anchor matrix when all applicable criteria were met:

1. a traceable primary paper, authoritative review, or official methodological source was identifiable;
2. the mathematical object or method was explicit enough to classify;
3. the work addressed a system application, a direct sustainability/resilience outcome, or an empirically assessed mathematical-art/visualization function;
4. metadata could be checked through a DOI resolver, publisher, scholarly index, national academy, government laboratory, or institutional repository;
5. the source contributed to scope identification, method transfer, outcome definition, validation design, or a documented limitation.

Authoritative reviews were retained to delimit domains and terminology. They do not substitute for direct application evidence.

## 6. Exclusion and caution rules

The following were excluded from direct-evidence status or coded cautiously:

- uses of *geometry*, *topology*, *resilience*, *adaptive*, or *green* as keywords without an operational definition;
- purely aesthetic images without a declared data-to-form mapping;
- art or communication effects treated as proof of physical, ecological, or operational performance;
- generic optimization papers with no application or transferable geometric content;
- secondary summaries used as though they were primary evidence;
- sources whose bibliographic identity could not be verified;
- sustainability inferred solely from sector membership;
- resilience inferred from robustness, accuracy, or efficiency alone;
- topological data analysis, optimal transport, network science, or manifold learning mislabeled as classical differential geometry.

## 7. Mathematical classification

| Code | Class | Required evidence |
|---|---|---|
| `DG_EXPLICIT` | Differential geometry | Explicit manifolds, metrics, curvature, geodesics, connections, shape spaces, geometric flows, or differential-geometric operators |
| `GEOM_ADJACENT` | Adjacent geometric mathematics | Operational TDA, network geometry, optimal transport, geometric morphometrics, shape calculus, or geometric optimization |
| `MANIFOLD_EMPIRICAL` | Manifold learning/reduction | A learned or inferred low-dimensional state space with a defined analytical purpose |
| `DYNAMICAL` | Dynamical systems/control | Attractors, bifurcations, reachability, viability, recovery dynamics, or geometric control |
| `VISUAL_ENCODING` | Mathematical art/visualization | A defined mapping from data, state, uncertainty, or design variable to visual, material, generative, or sonic form |
| `NOT_OBSERVED` | No operational geometric content observed | Relevant to the application or outcome, but not direct support for the central geometric intersection |

`GEOM_ADJACENT` and `MANIFOLD_EMPIRICAL` are not automatically evidence for the differential-geometric necessity gate.

## 8. Outcome coding

Each anchor is coded separately for differential geometry, sustainability, resilience, and mathematical art/visualization:

- `DIRECT_QUANTIFIED`: an explicit outcome is measured or computationally evaluated;
- `DIRECT_QUALITATIVE`: the outcome is explicit but not quantitatively tested;
- `CONTEXTUAL`: the relation is plausible or motivating, but not evaluated as an outcome;
- `NOT_OBSERVED`: the source does not provide the outcome;
- `NOT_VERIFIED`: available metadata did not permit a reliable determination.

Bibliographic verification uses:

- `PUBLISHER_METADATA_VERIFIED`;
- `OFFICIAL_INSTITUTION_METADATA_VERIFIED`;
- `PRIMARY_PAPER_REVIEWED`;
- `DISCOVERY_METADATA_ONLY`.

The last status does not support strong claim extraction and is retained only when it helps identify a search gap.

## 9. Synthesis method

Evidence was charted by application family, system object, disturbance or transition, outcome, geometric role, art role, and validation gap. Constant comparison was used to decide whether a discovered topic was:

1. a primary application family;
2. a searchable subscope within an existing family;
3. a cross-cutting enabling layer;
4. a decision/governance layer; or
5. outside the present intersection.

A family was added only when it represented a distinct system class and could not be adequately represented as a subscope or enabling method. This rule produced two additions to the original ten families: Earth/climate-system dynamics and urban morphology/spatial planning.

## 10. Interpretation rule

This review maps possibility and evidence structure. It does not estimate effects, pool outcomes, score candidate quality, or select a domain. Absence from the curated anchor matrix means `NOT_YET_IDENTIFIED_IN_THIS_PHASE`, not global nonexistence.

The central four-way bridge is considered observed only if one source or a declared evidence chain supplies:

1. operational differential geometry;
2. an explicit sustainability outcome;
3. an explicit disturbance-response-recovery or adaptation outcome; and
4. an empirically or analytically justified mathematical-art/visualization function.

No single anchor in this Phase-0 map satisfies all four conditions. This is a corpus-limited bridge deficit, not a universal absence claim.

## 11. Required next review phase

Before comparative candidate assessment, the project should preregister database coverage and dates; export records from at least two multidisciplinary and relevant domain databases; retain deduplication and exclusion counts; conduct two independent screening or verification passes; retrieve full texts; complete claim-level extraction; and register explicit rules for converting search scopes into application candidates.

## Methodological references

- Peters, M. D. J., Marnie, C., Tricco, A. C., Pollock, D., Munn, Z., Alexander, L., McInerney, P., Godfrey, C. M., & Khalil, H. (2020). Updated methodological guidance for the conduct of scoping reviews. *JBI Evidence Synthesis, 18*(10), 2119–2126. https://doi.org/10.11124/JBIES-20-00167
- Tricco, A. C., Lillie, E., Zarin, W., O'Brien, K. K., Colquhoun, H., Levac, D., Moher, D., Peters, M. D. J., Horsley, T., Weeks, L., Hempel, S., Akl, E. A., Chang, C., McGowan, J., Stewart, L., Hartling, L., Aldcroft, A., Wilson, M. G., Garritty, C., Lewin, S., Godfrey, C. M., Macdonald, M. T., Langlois, E. V., Soares-Weiser, K., Moriarty, J., Clifford, T., Tunçalp, Ö., & Straus, S. E. (2018). PRISMA extension for scoping reviews (PRISMA-ScR): Checklist and explanation. *Annals of Internal Medicine, 169*(7), 467–473. https://doi.org/10.7326/M18-0850

The complete scope-review bibliography is maintained in [`SCOPE_REVIEW_01.md`](SCOPE_REVIEW_01.md) and [`scope_review_01.bib`](scope_review_01.bib).
