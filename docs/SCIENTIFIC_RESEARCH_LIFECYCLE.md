# MSR Scientific Research Lifecycle

- Architecture ID: `MSR-RA-002`
- Version: `0.1.0`
- Date: 2026-08-22
- Status: `PROPOSED_ACTIVE_REVIEW`
- Parent architecture: [`MSR-RA-001`](REPOSITORY_ARCHITECTURE.md)
- Application decision: `NOT_SELECTED`

## 1. Purpose

`MSR-RA-002` expands the repository's six-node executive architecture into the full scientific lifecycle used for focal-paper review, mathematical reconstruction, computational reproduction, cross-paper synthesis, sustainable-resilience transfer, mathematical visualization, and publication.

The lifecycle is deliberately **not a one-way pipeline**. It contains explicit gates, failure loops, transfer falsification, and a final return from released results to new questions and evidence.

The governing distinctions are:

- evidence acquisition is not evidence interpretation;
- author mathematics is not project mathematics;
- code availability is not execution;
- execution is not reproduction;
- reproduction is not independent validation;
- mathematical relevance is not sustainable-resilience relevance;
- mathematical art is not empirical validation;
- publication is not the endpoint of inquiry.

## 2. Authoritative Mermaid diagram

```mermaid
flowchart TD

%% =========================================================
%% PHASE I — QUESTION, CORPUS, AND PRIMARY EVIDENCE
%% =========================================================

subgraph P1["I · RESEARCH QUESTION AND PRIMARY EVIDENCE"]
    Q["Research question, scope and scientific boundaries"]
    S["Literature discovery and corpus registration"]
    A["Primary-source resolution"]
    B["Primary evidence bundle"]

    B1["Main paper / PDF"]
    B2["Supplement and appendices"]
    B3["Official code"]
    B4["Data / meshes / point clouds / inputs"]
    B5["Models / checkpoints / parameters"]
    B6["Environment / dependencies / hardware"]
    B7["DOI, project page, version, license, hashes"]

    G1{"Artifact inventory closed?"}
    U1["Document unresolved, restricted or unavailable artifacts"]

    Q --> S
    S --> A
    A --> B

    B --> B1
    B --> B2
    B --> B3
    B --> B4
    B --> B5
    B --> B6
    B --> B7

    B1 --> G1
    B2 --> G1
    B3 --> G1
    B4 --> G1
    B5 --> G1
    B6 --> G1
    B7 --> G1

    G1 -- "No" --> U1
    U1 --> A
end

%% =========================================================
%% PHASE II — INDEPENDENT PAPER CASE STUDY
%% =========================================================

subgraph P2["II · INDEPENDENT PAPER CASE STUDY"]
    R["Independent focal-paper review"]

    R1["Scientific problem and research question"]
    R2["Claims and evidence extraction"]
    R3["Definitions, notation and assumptions"]
    R4["Mathematical objects and spaces"]
    R5["Equations, propositions and derivations"]
    R6["Physical laws and boundary conditions"]
    R7["Algorithms and discretization"]
    R8["Experiments, metrics and reported results"]
    R9["Limitations and failure conditions"]

    ES["Evidence-state adjudication<br/>OBSERVED · INFERRED · EXTERNAL · PROPOSED · NOT OBSERVED · NOT VERIFIED"]
    G2{"Paper mathematically reconstructed?"}

    R --> R1
    R --> R2
    R --> R3
    R --> R4
    R --> R5
    R --> R6
    R --> R7
    R --> R8
    R --> R9

    R1 --> ES
    R2 --> ES
    R3 --> ES
    R4 --> ES
    R5 --> ES
    R6 --> ES
    R7 --> ES
    R8 --> ES
    R9 --> ES

    ES --> G2
    G2 -- "No" --> R
end

%% =========================================================
%% PHASE III — MATHEMATICS → IMPLEMENTATION
%% =========================================================

subgraph P3["III · MATHEMATICAL AND COMPUTATIONAL RECONSTRUCTION"]
    M["Formal mathematical specification"]

    M1["State space / manifold / topology"]
    M2["Metrics, operators and measures"]
    M3["Parameters, units and admissible ranges"]
    M4["Governing equations"]
    M5["Objectives and constraints"]
    M6["Invariants and limiting cases"]

    XW["Equation → algorithm → code crosswalk"]
    C["Executable reference model"]

    T1["Unit tests"]
    T2["Property and invariant tests"]
    T3["Numerical convergence tests"]
    T4["Regression tests"]
    T5["Cross-implementation checks"]

    M --> M1
    M --> M2
    M --> M3
    M --> M4
    M --> M5
    M --> M6

    M1 --> XW
    M2 --> XW
    M3 --> XW
    M4 --> XW
    M5 --> XW
    M6 --> XW

    XW --> C

    C --> T1
    C --> T2
    C --> T3
    C --> T4
    C --> T5
end

%% =========================================================
%% PHASE IV — REPRODUCTION AND VALIDATION
%% =========================================================

subgraph P4["IV · REPRODUCTION, STRESS TESTING AND VALIDATION"]
    E["Preregistered reproduction experiment"]

    E1["Immutable inputs and checksums"]
    E2["Exact environment"]
    E3["Parameters, tolerances and random seeds"]
    E4["Exact execution command"]
    E5["Expected source result"]

    RUN["Execute"]
    G3{"Reported result reproduced?"}

    F["Failure diagnosis"]
    F1["Source ambiguity"]
    F2["Environment or dependency"]
    F3["Implementation discrepancy"]
    F4["Data discrepancy"]
    F5["Numerical sensitivity"]
    F6["Unreported assumption"]

    PR["Partial reproduction<br/>with explicit limitations"]
    REP["Reproduced source result"]
    ST["Independent stress tests"]

    ST1["Resolution / discretization"]
    ST2["Parameter sensitivity"]
    ST3["Noise and perturbations"]
    ST4["Boundary and initial conditions"]
    ST5["Random-seed robustness"]
    ST6["Computational scaling"]
    ST7["Failure and edge cases"]
    ST8["Uncertainty analysis"]

    G4{"Independent validation adequate?"}
    LIM["Bounded conclusion and limitations"]
    VM["Validated mathematical mechanism"]

    E --> E1
    E --> E2
    E --> E3
    E --> E4
    E --> E5

    E1 --> RUN
    E2 --> RUN
    E3 --> RUN
    E4 --> RUN
    E5 --> RUN

    RUN --> G3

    G3 -- "No" --> F
    F --> F1
    F --> F2
    F --> F3
    F --> F4
    F --> F5
    F --> F6
    F --> E

    G3 -- "Partly" --> PR
    G3 -- "Yes" --> REP

    PR --> ST
    REP --> ST

    ST --> ST1
    ST --> ST2
    ST --> ST3
    ST --> ST4
    ST --> ST5
    ST --> ST6
    ST --> ST7
    ST --> ST8

    ST1 --> G4
    ST2 --> G4
    ST3 --> G4
    ST4 --> G4
    ST5 --> G4
    ST6 --> G4
    ST7 --> G4
    ST8 --> G4

    G4 -- "No" --> LIM
    G4 -- "Yes" --> VM
end

%% =========================================================
%% PHASE V — CROSS-PAPER MATHEMATICAL SYNTHESIS
%% =========================================================

subgraph P5["V · CROSS-PAPER MATHEMATICS EXPLORATION"]
    SYN["Cross-paper synthesis"]

    K1["Mathematical object registry"]
    K2["Equation and operator ontology"]
    K3["Method and algorithm relations"]
    K4["Common assumptions"]
    K5["Contradictions and limitations"]
    K6["Numerical evidence comparison"]

    KG["Mathematical knowledge graph"]

    SYN --> K1
    SYN --> K2
    SYN --> K3
    SYN --> K4
    SYN --> K5
    SYN --> K6

    K1 --> KG
    K2 --> KG
    K3 --> KG
    K4 --> KG
    K5 --> KG
    K6 --> KG
end

%% =========================================================
%% PHASE VI — TRANSFER TO SUSTAINABLE RESILIENCE
%% =========================================================

subgraph P6["VI · TRANSFER TO SUSTAINABLE RESILIENCE"]
    TH["Candidate transfer hypothesis"]

    SR1["Domain and physical-system evidence"]
    SR2["Sustainability evidence"]
    SR3["Resilience evidence"]
    SR4["Hazard and stressor evidence"]
    SR5["Service and population evidence"]
    SR6["Equity and distributional evidence"]
    SR7["Governance and implementation evidence"]

    G5{"Transfer scientifically justified?"}
    RJ["Reject, revise or retain only as analogy"]
    SRM["Sustainable-resilience mathematical model"]
    SRV["Verification, calibration and validation"]

    TH --> SR1
    TH --> SR2
    TH --> SR3
    TH --> SR4
    TH --> SR5
    TH --> SR6
    TH --> SR7

    SR1 --> G5
    SR2 --> G5
    SR3 --> G5
    SR4 --> G5
    SR5 --> G5
    SR6 --> G5
    SR7 --> G5

    G5 -- "No" --> RJ
    G5 -- "Yes" --> SRM

    SRM --> SRV
end

%% =========================================================
%% PHASE VII — FIGURES, MATHEMATICAL ART AND PUBLICATION
%% =========================================================

subgraph P7["VII · MATHEMATICAL ART, COMMUNICATION AND PUBLICATION"]
    VIS["Reproducible mathematical visualization"]

    VA["Mathematical validity audit"]
    VB["Data and provenance audit"]
    VC["Visual-encoding audit"]
    VD["Accessibility audit"]

    ART["Mathematical art"]
    CI["Communication-impact evaluation<br/>when claimed"]
    PUB["Papers, documentation and decisions"]
    REL["Versioned release and reproducibility record"]

    VIS --> VA
    VIS --> VB
    VIS --> VC
    VIS --> VD

    VA --> ART
    VB --> ART
    VC --> ART
    VD --> ART

    ART --> CI
    CI --> PUB
    PUB --> REL
end

%% =========================================================
%% MASTER CONNECTIONS
%% =========================================================

G1 -- "Yes" --> R
G2 -- "Yes" --> M

T1 --> E
T2 --> E
T3 --> E
T4 --> E
T5 --> E

LIM --> SYN
VM --> SYN

KG --> TH

SRV --> VIS
RJ --> SYN

REL -. "new questions, gaps and falsification" .-> Q
```

The standalone Mermaid source is maintained at [`diagrams/MSR_RA_002_SCIENTIFIC_RESEARCH_LIFECYCLE.mmd`](diagrams/MSR_RA_002_SCIENTIFIC_RESEARCH_LIFECYCLE.mmd).

## 3. Lifecycle phases

| Phase | Scientific purpose | Principal gate |
|---|---|---|
| I | Resolve corpus and all claim-critical primary artifacts | `Artifact inventory closed?` |
| II | Reconstruct each focal publication independently | `Paper mathematically reconstructed?` |
| III | Translate accepted mathematics into explicit specifications and code | Tests and equation-to-code traceability |
| IV | Reproduce source results, diagnose failures, stress-test, and independently validate | `Reported result reproduced?` and `Independent validation adequate?` |
| V | Link independently reviewed papers through mathematical objects, equations, methods, assumptions, contradictions, and numerical evidence | Knowledge-graph traceability |
| VI | Test whether mathematical mechanisms can be transferred to sustainable resilience using independent domain evidence | `Transfer scientifically justified?` |
| VII | Produce mathematically valid, provenance-controlled visualization and publication artifacts | Visual and publication audits |

## 4. Case-study rule

For every focal paper `MSR-CS-NNN`, the default path is:

$$
\text{source acquisition}
\rightarrow
\text{independent reconstruction}
\rightarrow
\text{equation-to-code traceability}
\rightarrow
\text{registered reproduction}
\rightarrow
\text{stress test}
\rightarrow
\text{bounded conclusion}.
$$

Cross-paper synthesis is downstream of individual judgement. A paper is not interpreted as a sustainable-resilience contribution merely because its mathematics appears transferable.

## 5. Primary-evidence dependency

Phase I is governed by [`PRIMARY_EVIDENCE_BUNDLE.md`](../literature_review/protocol/PRIMARY_EVIDENCE_BUNDLE.md). Required artifact classes are resolved per claim and experiment, including where applicable:

- main paper;
- supplementary material and appendices;
- official code;
- datasets, meshes, point clouds, simulation inputs, or procedural generators;
- models and checkpoints;
- environment and dependency information;
- DOI, project page, immutable version, license, and hashes.

A missing artifact does not automatically fail the review. It must receive an admissible documented lifecycle state and its effect on attainable reproduction status must remain explicit.

## 6. Evidence-state firewall

Scientific evidence status and artifact/reproduction status remain orthogonal. In particular:

$$
\texttt{REPRODUCED}
\not\Rightarrow
\texttt{VALIDATED},
$$

and

$$
\texttt{PROPOSED}
\not\Rightarrow
\texttt{OBSERVED}
$$

merely because a proposed extension has been implemented in code.

## 7. Cross-paper synthesis contract

Only reviewed case studies enter Phase V. Cross-paper edges must identify the relation type and source evidence. Typical relation classes include:

- shared mathematical object;
- operator dependence;
- discretization or approximation relation;
- algorithmic extension;
- shared assumption;
- contradictory result or boundary condition;
- common benchmark;
- implementation dependence;
- validated transfer candidate.

The knowledge graph must preserve directionality and must not treat co-citation, topical similarity, or visual resemblance as mathematical dependence.

## 8. Sustainable-resilience transfer firewall

A mathematical mechanism moves from Phase V to a sustainable-resilience model only after independent evidence supports the intended physical and decision interpretation. Candidate transfer requires, as applicable, domain evidence, physical-system evidence, sustainability evidence, resilience evidence, hazard/stressor evidence, service/population evidence, equity evidence, and implementation/governance evidence.

Failed transfer is a scientific result. It returns to cross-paper synthesis as a rejected, revised, or analogy-only relation rather than being silently removed.

## 9. Mathematical-art firewall

A figure or artwork is downstream of a declared mathematical object, dataset, experiment, or evidence record. Four audits are explicit before publication:

1. mathematical validity;
2. data and provenance;
3. visual encoding;
4. accessibility.

Communication impact is assessed separately and only when such an effect is claimed.

## 10. Feedback and falsification loop

The release node returns to the research-question node because every completed study may create:

- new falsification tests;
- unresolved mathematical questions;
- missing evidence requirements;
- contradictory cases;
- domain-transfer failures;
- new candidate methods;
- revisions to assumptions, tolerances, or model boundaries.

The authoritative conceptual loop is therefore

$$
\mathcal E
\rightarrow
\mathcal M
\rightarrow
\mathcal C
\rightarrow
\mathcal R
\rightarrow
\mathcal S
\rightarrow
\mathcal T
\rightarrow
\mathcal P
\circlearrowleft,
$$

where evidence, mathematics, computation, reproduction, synthesis, transfer, and publication remain separately auditable stages.