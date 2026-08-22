# Primary Evidence Bundle and Reproduction-Gate Protocol

## 1. Purpose

This protocol defines the minimum provenance, artifact, execution, and reproduction controls for an individual paper case study. It prevents a reviewed PDF, an identified code link, or a successful program launch from being reported as a reproduced scientific result.

It applies to every study class (`D`, `M`, `G`, `V`, and `C`). The required artifacts are determined per claim and per experiment; they are not assumed to be identical for every paper.

## 2. Bundle model

For study (i), record

$$
\mathcal{B}_i=(\mathcal{I}_i,\mathcal{A}_i,\mathcal{E}_i,\mathcal{X}_i,\mathcal{P}_i),
$$

where:

- $\mathcal{I}_i$ is source identity: title, authors, venue, DOI, version, correction or retraction state, and official landing pages;
- $\mathcal{A}_i$ is the artifact inventory: main text, supplement, code, data, model weights, configurations, and any additional claim-critical artifact;
- $\mathcal{E}_i$ is the execution specification: operating system, runtime, dependency lock, hardware, random seeds, external services, and licenses;
- $\mathcal{X}_i$ is the experiment register: source claim, equation, algorithm, command, inputs, expected output, metric, tolerance, and stress test;
- $\mathcal{P}_i$ is audit provenance: retrieval dates, immutable identifiers, hashes, search paths, logs, deviations, and reviewer decisions.

`ENV` is therefore an execution specification, not merely another downloadable artifact. A model checkpoint may be required for one experiment and not applicable to another. Applicability must be decided at experiment level.

## 3. Two status systems that must not be conflated

### 3.1 Scientific-evidence status

`OBSERVED`, `INFERRED`, `EXTERNAL`, `PROPOSED`, `NOT_OBSERVED`, and `NOT_VERIFIED` classify statements and are governed by [the evidence-status protocol](EVIDENCE_STATUS.md).

### 3.2 Artifact lifecycle

| Status | Meaning |
|---|---|
| `UNASSESSED` | No documented search or inspection has begun. |
| `IDENTIFIED` | An authoritative or candidate location is known, but the artifact has not been acquired. |
| `OBTAINED` | The artifact has been acquired and identified, but substantive inspection is incomplete. |
| `INSPECTED` | Identity, scope, integrity, licensing, and claim relevance have been inspected and recorded. The inspection scope must be stated. |
| `NOT_APPLICABLE` | The artifact is not required for the named claim or experiment; a rationale is mandatory. |
| `NOT_FOUND_AFTER_SEARCH` | A documented search of named sources found no artifact. This does not mean the artifact is non-public. |
| `ACCESS_RESTRICTED` | The artifact is identified, but authentication, payment, embargo, or permission prevents access. |
| `LICENSE_RESTRICTED` | The artifact is accessible but cannot be copied, executed, or redistributed for the intended audit under the recorded license. |

`CODE_NOT_PUBLIC` is not an admissible default. Use `ACCESS_RESTRICTED` only when a repository or author statement establishes restricted access; otherwise use `NOT_FOUND_AFTER_SEARCH` after documenting the search. Replace `DATA_NOT_REQUIRED` with `NOT_APPLICABLE` plus a claim-specific rationale.

### 3.3 Execution and reproduction lifecycle

| Status | Meaning |
|---|---|
| `NOT_STARTED` | No environment build or run has been attempted. |
| `ENVIRONMENT_BUILT` | Dependencies and required services resolve, but a target experiment has not completed. |
| `EXECUTED` | A named command completed and produced auditable output. This does not establish agreement with the paper. |
| `PARTIALLY_REPRODUCED` | At least one registered target result agrees within a predeclared tolerance, but the reproduction target is incomplete. |
| `REPRODUCED` | All preregistered target results agree within their tolerances under the recorded conditions. |
| `FAILED` | A named build, execution, or comparison failed; logs and the failure stage are recorded. |

Independent validation is a later stage: it requires a new dataset, stress condition, perturbation, implementation, or real-world comparison that was not merely used to reproduce the source result.

## 4. Inventory-closure gate

Let $A_i^*$ be the set of artifacts required by the registered claims and experiments. Define

$$
R_{\mathrm{inv}}(s)=1
\quad\text{iff}\quad
s\in\mathcal S_{\mathrm{terminal}}.
$$

Here $\mathcal S_{\mathrm{terminal}}$ denotes exactly the artifact states `INSPECTED`, `NOT_APPLICABLE`, `NOT_FOUND_AFTER_SEARCH`, `ACCESS_RESTRICTED`, and `LICENSE_RESTRICTED`.

The inventory is closed only when

```math
G_i^{\mathrm{inventory}}
=
\bigwedge_{a\in A_i^*}R_{\mathrm{inv}}(s_{i,a})=1.
```

This is an **inventory-closure gate**, not a reproduction gate. A terminal absence or restriction can close the inventory while preventing reproduction. `IDENTIFIED` and `OBTAINED` remain open because inspection is incomplete.

## 5. Reproduction-grade gates

Case-study completion must be reported with explicit stages:

| Stage | Minimum condition |
|---|---|
| `MAIN_PAPER_REVIEWED` | Main text inspected; claim-level locators and evidence statuses recorded. |
| `ARTIFACT_INVENTORY_CLOSED` | The inventory-closure gate passes for the registered target claims. |
| `EXECUTION_COMPLETE` | The registered commands complete with logs and outputs. |
| `PARTIALLY_REPRODUCED` | Some target comparisons pass their declared tolerances. |
| `REPRODUCED` | All registered target comparisons pass their declared tolerances. |
| `INDEPENDENTLY_VALIDATED` | A distinct validation or stress-test protocol passes. |

Do not use `fully reviewed`, `verified study`, or `reproducible` without naming the attained stage. Missing or restricted claim-critical artifacts must cap the attainable result and be reported as limitations.

## 6. Required source-resolution path

Search and record, as applicable:

1. author publication page;
2. official project page;
3. DOI and publisher record;
4. main paper and correction or retraction notices;
5. publisher-hosted or author-hosted supplement;
6. official code repository linked by the paper or project page;
7. archived releases and immutable commits;
8. data repositories, model registries, and configuration files;
9. dependency locks, container files, and hardware notes;
10. author contact only when a material unresolved artifact justifies it.

Every negative result must record where and when the search occurred. Absence from one web page is not evidence of nonexistence.

## 7. Equation-to-implementation traceability

Each reproduction target must provide the following crosswalk:

| Field | Required content |
|---|---|
| Source claim | Exact claim with page, section, figure, table, or equation locator |
| Mathematical object | Symbols, domains, assumptions, constraints, and objective |
| Algorithm | Paper algorithm or a transparent derivation when no pseudocode is supplied |
| Implementation | Repository path, symbol or function, and immutable commit |
| Inputs | Dataset/model/configuration identifiers and hashes where feasible |
| Run | Exact command, seed policy, runtime, hardware, and log location |
| Comparison | Metric, expected value or range, tolerance, and pass/fail rule |
| Deviation | Every departure from the source configuration and its likely consequence |

For numerical claims, the reviewer must distinguish transcription checks, unit tests, smoke tests, benchmark reproduction, ablation reproduction, robustness tests, and external validation.

## 8. Repository and copyright rule

The review repository stores provenance manifests, lawful links, hashes, metadata, reviewer-authored scripts, environment specifications, logs, and derived results. It does not mirror third-party PDFs, code, data, or model weights unless the license permits redistribution and the reason for mirroring is documented. Access and redistribution rights must be assessed separately.

## 9. Minimum per-case files

Each computational or data-dependent case study should contain:

- a critical literature review with author-date citations;
- a machine-readable evidence record;
- a claim-level evidence matrix;
- `SOURCE_MANIFEST.yaml` implementing this protocol;
- a validation and provenance log;
- an experiment register before execution begins;
- environment, run, comparison, and stress-test records as the audit advances.

Until these stages are complete, status language must state exactly what is reviewed, identified, inspected, executed, reproduced, or still open.
