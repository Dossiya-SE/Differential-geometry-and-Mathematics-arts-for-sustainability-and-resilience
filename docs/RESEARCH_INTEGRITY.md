# Research Integrity Standard

- Standard ID: `MSR-RI-001`
- Version: `1.0.0`
- Status: `ACTIVE`

## Evidence language

| State | Permitted meaning |
|---|---|
| `OBSERVED` | Directly supported by the checked source, data, or execution record |
| `OBSERVED_PARTIAL` | Direct support exists for named elements but not the full construct or endpoint |
| `INFERRED` | Reasoned interpretation derived from identified observations |
| `PROPOSED` | Project design, hypothesis, transfer, or future method |
| `VALIDATED` | Passed a declared validation procedure for a bounded purpose |
| `REJECTED` | Failed a declared test or was contradicted by controlling evidence |
| `NOT_OBSERVED` | Absent from the checked source or record |
| `NOT_VERIFIED` | Relevant but not independently checked |
| `NOT_APPLICABLE` | Outside the bounded object, with a written rationale |

The state is attached to a specific claim and evidence boundary. It is not inherited by neighboring claims.

## Attribution

Scholarly claims use conventional author–date citations and complete bibliography records. Evidence-matrix IDs support internal traceability only. A citation must support the exact claim near which it appears; a source relevant to the general topic is insufficient.

## Mathematical integrity

Mathematical statements distinguish definitions, assumptions, lemmas, propositions, conjectures, approximations, and empirical findings. Symbols have declared domains, codomains, dimensions, and units. Numerical implementations state discretization, precision, tolerances, singularities, and failure behavior.

## Computational integrity

Results identify code version, environment, inputs, parameter values, seeds, checksums, and output provenance. Exploratory, calibration, verification, validation, and confirmatory runs remain distinct. Thresholds are not changed after observing results without a new record and rationale.

## Visual integrity

Analytical figures encode declared variables and transformations. Interpretive art is labeled as such. Cropping, interpolation, projection, smoothing, color scales, animation, and generative processing are documented when they could affect interpretation. Accessibility is part of validity, not a decorative afterthought.

## Correction policy

Errors are corrected transparently through versioned commits and changelog entries. Released records are superseded rather than silently overwritten. Negative results and failed reproductions remain visible when material to the research conclusion.
