# MSR Research-Platform Architecture

- Architecture ID: `MSR-RA-001`
- Version: `0.4.0`
- Date: 2026-08-22
- Status: `ACTIVE_FOUNDATION`
- Application decision: `NOT_SELECTED`

## 1. Purpose

This architecture converts the repository from a literature-review package into a traceable research system for mathematics, computation, mathematical art, and scholarly publication. It preserves the existing evidence base and adds the minimum executable infrastructure needed to test future claims.

The governing rule is:

> Every substantive claim connects to evidence; every mathematical object connects to a specification; every computation connects to tests; every figure connects to reproducible data and declared visual encodings.

Traceability establishes provenance. It does not transform an inference, proposal, or analogy into an observation or validation result.

## 2. Scope boundary

The architecture is domain-neutral. The following remain `NOT_SELECTED`:

- application domain;
- system boundary;
- hazard or stressor;
- sustainability outcome;
- resilience outcome;
- spatial and temporal scale;
- geography;
- demonstrator.

No software namespace, model contract, example, or figure may silently privilege the former coupled P-W-T-SW urban-flooding candidate. Neutral mathematical fixtures are permitted. Domain adapters require a future evidence-led selection decision.

## 3. Responsibility layers

| Layer | Authoritative location | Core object | Principal verification |
|---|---|---|---|
| Literature and evidence | `literature_review/` | Claim and evidence record | Citation and provenance audit |
| Mathematical specification | `mathematics/` | Definition, assumption, proposition, model contract | Mathematical review and schema validation |
| Executable model | `src/msr/` | Versioned implementation | Unit and property tests |
| Experiment | `experiments/` | Immutable configuration and result summary | Reproduction and numerical checks |
| Data | `data/` | Versioned dataset reference | Lineage, license, privacy, and checksum audit |
| Figure and mathematical art | `figures/`, `art/` | Visual source and encoding record | Mathematical, provenance, and accessibility review |
| Publication | `docs/`, `papers/` | Quarto or LaTeX source | Citation, cross-reference, render, and limitation audit |
| Governance | root documents, `.github/` | Policy, decision, release | Pull-request checks and recorded review |

## 4. Language policy

The repository uses the smallest polyglot stack that gives each language a distinct responsibility.

| Technology | Governing role | Entry condition |
|---|---|---|
| Python | Reference computation, schemas, data, tests, and experiments | Active |
| Markdown and LaTeX | Mathematical specification and scholarly writing | Active |
| Quarto and Pandoc | Reproducible HTML and PDF publication | Active |
| SVG and CSS | Exact diagrams and vector mathematical art | Active |
| YAML, JSON Schema, and TOML | Protocols, records, validation, and environments | Active |
| TypeScript, D3, and Three.js | Interactive two- and three-dimensional mathematical artifacts | Add with first reviewed interactive artifact |
| Julia, Manifolds.jl, Manopt.jl, SciML, and JuMP | High-performance geometry, dynamics, and optimization | Add after a benchmark against the Python reference |
| JAX | Automatic differentiation and sensitivity analysis | Add only when derivatives are operationally required |
| Lean | Formal proof of a bounded theorem or safety property | Add with a named formalization target |
| Rust or C++ | Performance-critical kernels | Add after profiling identifies a justified bottleneck |
| Blender or GLSL | High-fidelity or shader-based interpretive art | Add with provenance and non-empirical labeling |

Adding a language requires an architectural decision record stating its non-overlapping role, environment, interface, shared fixtures, tests, and removal criteria.

## 5. Repository topology

```text
literature_review/   evidence synthesis and application selection
mathematics/         definitions, derivations, propositions, and contracts
src/msr/             domain-neutral reference implementations
tests/               unit, property, numerical, regression, cross-language
experiments/         registered configurations and benchmarks
schemas/             model and experiment validation schemas
data/                data policy and controlled local data locations
art/                 visual encoding standard and mathematical-art sources
figures/             source, generated, and publication-ready figures
notebooks/           exploration and teaching, not production logic
docs/                Quarto documentation and decision records
papers/              publication manuscripts and generated-output rules
reproducibility/     environments, containers, and manifests
.github/              automated checks and collaboration controls
```

Folders without a research object contain a README stating their admission rules rather than placeholder claims or unvalidated examples.

## 6. Stable identifiers

| Object | Pattern | Example |
|---|---|---|
| Chain architecture | `MSR-CA-NNN` | `MSR-CA-001` |
| Research architecture | `MSR-RA-NNN` | `MSR-RA-001` |
| Literature case study | `MSR-CS-NNN` | `MSR-CS-001` |
| Model contract | `MSR-MOD-NNNN` | `MSR-MOD-0001` |
| Experiment | `MSR-EXP-NNNN` | `MSR-EXP-0001` |
| Dataset | `MSR-DATA-NNNN` | `MSR-DATA-0001` |
| Figure or art object | `MSR-FIG-NNNN` | `MSR-FIG-0001` |
| Architectural decision | `ADR-NNNN` | `ADR-0001` |

Identifiers are never recycled. Corrections increment an object version and identify the superseded version.

## 7. Mathematical model contract

Every implemented model has a machine-readable contract conforming to `schemas/model-contract.schema.json`. The contract contains at least:

1. model identifier, title, version, authorship, date, and status;
2. application state and scientific purpose;
3. mathematical state space or manifold;
4. domain and codomain of every material map;
5. metric, topology, connection, measure, or other geometric structure;
6. symbols, parameters, dimensions, units, and admissible ranges;
7. assumptions, boundary conditions, and applicability limits;
8. governing equations and referenced derivation;
9. invariants, constraints, and expected limiting behavior;
10. numerical representation, solver, precision, and tolerances;
11. uncertainty representation and sensitivity requirements;
12. verification tests, benchmark cases, and validation status;
13. author–date source keys and secondary audit identifiers;
14. links to implementations, experiments, data, and figures.

An equation in code without a contract is an implementation candidate, not an accepted project model.

## 8. Experiment contract

Every experiment record conforming to `schemas/experiment.schema.json` identifies:

- immutable experiment ID and version;
- model contract and code release;
- research question and predeclared acceptance rule;
- input references and checksums;
- parameter values, units, precision, and tolerances;
- random-number generator and seed, or an explicit deterministic declaration;
- software environment and dependency lock reference;
- command or entry point;
- output locations and checksums;
- verification, validation, and review status;
- known limitations and failure conditions.

Exploratory runs may be labeled `EXPLORATORY`. They cannot be cited as confirmatory tests unless preregistered and rerun under a new confirmatory experiment identifier.

## 9. Computational verification

Verification is layered:

| Test class | Question |
|---|---|
| Unit | Does one function meet its local contract? |
| Property | Do mathematical invariants hold across generated admissible inputs? |
| Numerical | Are residuals, tolerances, convergence, and limiting cases acceptable? |
| Regression | Did a reviewed result or repository invariant change unexpectedly? |
| Cross-language | Do independent implementations agree on shared fixtures and tolerances? |
| Validation | Does the model adequately represent checked external observations for its declared purpose? |

Verification of code is not validation of the represented system. Tests must state numerical tolerances rather than using unspecified approximate equality.

## 10. Mathematical-art contract

Every figure or artwork declares:

- object ID, source, version, author, and generation method;
- mathematical model, experiment, or evidence records encoded;
- mappings from mathematical or data variables to shape, position, color, line, opacity, motion, and texture;
- artifact class: `ANALYTICAL`, `EXPLANATORY`, `PARTICIPATORY`, or `INTERPRETIVE`;
- mathematical-validity status;
- communication-impact status;
- accessibility provisions, including text alternatives and non-color cues;
- known perceptual, projection, interpolation, or rendering limitations.

The two validation tracks remain separate:

1. **Mathematical validity:** whether the artifact accurately encodes its declared mathematics or data.
2. **Communication impact:** whether comprehension, participation, behavior, or decision influence has been evaluated.

Visual elegance, engagement, or realism is not evidence of physical-system accuracy or decision impact.

## 11. Writing and citation system

Quarto and LaTeX sources generate publications. The following are mandatory:

- author–date citations for substantive scholarly claims;
- one traceable bibliography record for each citation key;
- DOI and stable URL when available and verified;
- numbered equations, tables, figures, and cross-references;
- separate methods, results, interpretation, and limitations;
- explicit evidence-state language;
- audit identifiers only as secondary traceability metadata;
- no unsupported combined citation ranges;
- generated HTML and PDF treated as outputs, not hand-edited sources.

## 12. One-command verification

`make verify` is the portable verification entry point. It checks:

1. required architecture and policy files;
2. Python syntax and importability;
3. unit, property, numerical, and regression tests;
4. JSON records and schema conformance;
5. application and chain-architecture boundaries;
6. bibliography keys and internal document links;
7. figure identifiers, provenance, and accessibility metadata;
8. reference experiment reproducibility;
9. integrity-manifest checksums;
10. Quarto rendering when available, with a Pandoc source-validation fallback.

`make verify-ci` additionally runs Ruff, mypy, pytest, and strict tool availability in the controlled continuous-integration environment.

## 13. Merge gates

A pull request cannot be described as verified unless all applicable gates pass:

- no unsupported or uncited substantive claim;
- no undocumented equation, model, parameter, unit, or tolerance;
- mathematical properties tested across admissible cases;
- no selection-state change outside the selection protocol;
- no generated figure without provenance and alternative text;
- no silently changed experiment input, seed, threshold, or output;
- documentation renders without errors;
- dependencies and secrets pass automated checks;
- limitations and unresolved uncertainty remain visible.

Passing automated checks is necessary but not sufficient for scholarly acceptance.

## 14. Environments and reproducibility

The reference environment uses Python with version constraints in `pyproject.toml`. A development container specifies the operating-system layer. Future TypeScript and Julia environments require lockfiles. Release manifests record content checksums.

Large data, source PDFs, private information, generated caches, and unrestricted experiment outputs are not committed. Their lineage, access conditions, and checksums are documented instead.

## 15. Automation policy

GitHub Actions provide:

- pull-request continuous integration;
- documentation rendering and Pages deployment;
- scheduled and manual reproducibility checks;
- citation and link audits;
- tagged release artifacts;
- dependency and code-security analysis.

Workflow permissions follow least privilege. Deploy and release permissions are granted only to the jobs that require them.

## 16. Foundation acceptance criteria

Release `0.4.0` is accepted when:

1. the directory architecture and governance documents exist;
2. the two schemas validate their reference records;
3. the two-sphere implementation passes unit, property, and numerical tests;
4. the reference experiment reproduces its declared tolerance;
5. the exact SVG has a validated provenance record;
6. documentation sources render;
7. application status remains `NOT_SELECTED`;
8. all tracked-file checksums match `MANIFEST.sha256`;
9. GitHub pull-request checks complete successfully.

These criteria validate the repository foundation. They do not validate a sustainable-resilience application or establish the completeness of `MSR-CA-001`.
