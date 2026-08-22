# Contributing

Contributions are welcome when they preserve evidence traceability, mathematical precision, reproducibility, and the current application-selection boundary.

## Required workflow

1. Create a focused branch from the current `main` branch.
2. Open or reference an issue describing the research or engineering question.
3. Make the smallest coherent change that answers that question.
4. Run `make verify` before opening a pull request.
5. Complete every applicable section of the pull-request template.
6. Obtain review before merge. Direct changes to `main` are reserved for documented emergencies.

## Evidence requirements

Every substantive literature claim must include an author–date citation and a bibliography record. Evidence-matrix identifiers may be added as secondary audit links. They do not replace citations.

Use only the controlled evidence states:

`OBSERVED`, `OBSERVED_PARTIAL`, `INFERRED`, `PROPOSED`, `VALIDATED`, `REJECTED`, `NOT_OBSERVED`, `NOT_VERIFIED`, and `NOT_APPLICABLE`.

`NOT_APPLICABLE` requires a written rationale. Evidence for one step cannot be promoted to evidence for a complete chain or endpoint.

## Mathematical requirements

New models or material changes to models require a versioned contract under `mathematics/model_contracts/`. The contract must define:

- state space, domain, codomain, and geometric structure;
- symbols, parameters, dimensions, and units;
- assumptions, boundary conditions, invariants, and applicability limits;
- numerical representation, solver, precision, and tolerances;
- uncertainty representation and validation evidence;
- citations, tests, and benchmark identifiers.

Public functions must document the mathematical operation, assumptions, failure modes, and associated model identifier.

## Computational requirements

- Pin or constrain dependencies through the appropriate environment file.
- Record random seeds and numerical precision.
- Test invariants and limiting cases, not only example outputs.
- Separate exploratory notebooks from reusable package code.
- Store large or restricted data outside Git; document acquisition, checksums, and access constraints in `data/README.md`.
- Generated figures must contain or reference a provenance record.

## Mathematical-art requirements

Every mathematical artwork or scientific visualization must state:

1. the mathematical object encoded;
2. the mapping from data or mathematics to visual properties;
3. whether the artifact is analytical, explanatory, participatory, or interpretive;
4. its validation status;
5. accessibility provisions and known perceptual limitations.

Interpretive imagery must never be labeled as a simulation, measurement, or validation result.

## Application-selection control

A contribution must not silently select a domain, hazard, geography, system boundary, or demonstrator. Any proposed selection change must follow `literature_review/protocol/APPLICATION_DOMAIN_SELECTION.md` and modify the authoritative decision record through a separately reviewed pull request.
