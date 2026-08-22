# Model contracts

Model contracts are the binding interface between mathematical writing, code, tests, experiments, and figures. Every JSON record must validate against `schemas/model-contract.schema.json`.

A contract may have the status `PROPOSED`, `REFERENCE_VERIFIED`, `VALIDATED`, `REJECTED`, or `SUPERSEDED`. `REFERENCE_VERIFIED` means that the mathematical fixture and implementation passed the declared internal tests; it does not mean that an application has been empirically validated.
