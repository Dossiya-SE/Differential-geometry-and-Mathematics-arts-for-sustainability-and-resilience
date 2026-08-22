# Governance

## 1. Scope

This policy governs literature evidence, mathematical specifications, software, experiments, mathematical art, documentation, and releases in this repository.

## 2. Decision roles

| Role | Responsibility |
|---|---|
| Project steward | Maintains scope, approves releases, and protects the application-selection boundary |
| Evidence reviewer | Checks source attribution, evidence status, and claim-level traceability |
| Mathematical reviewer | Checks definitions, assumptions, derivations, invariants, and numerical interpretation |
| Computational reviewer | Checks implementation, tests, environments, security, and reproducibility |
| Visual-communication reviewer | Checks encoding validity, accessibility, provenance, and impact claims |

One person may occupy multiple roles during the foundation stage, but each review perspective must be explicitly recorded. A second independent pass is required for domain selection, major mathematical claims, and release-critical numerical results.

## 3. Decision hierarchy

1. Verified source evidence and binding research protocols.
2. Versioned mathematical and data contracts.
3. Reproducible experiment records and tests.
4. Architectural decision records.
5. Working interpretations and proposals.

A lower level cannot silently override a higher level.

## 4. Protected decisions

The following changes require a dedicated pull request and explicit rationale:

- selection of an application, system boundary, hazard, geography, or demonstrator;
- freezing or replacing the ten-chain architecture;
- modification of evidence-state definitions;
- relaxation of validation gates or numerical tolerances;
- retroactive alteration of a released evidence or experiment record;
- licensing decisions affecting code, writing, data, or art.

## 5. Releases and corrections

Releases are tagged only after required checks pass. Corrections preserve history: a released record is superseded by a new version rather than silently rewritten. Retractions or rejected claims must remain discoverable with a reason and replacement reference when applicable.

## 6. Conflicts and limitations

Contributors disclose material conflicts, unavailable evidence, failed replications, and computational limitations. Uncertainty or disagreement is recorded; it is not resolved by increasing a score or changing a threshold after seeing results.
