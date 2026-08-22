# Experiments

An experiment is a versioned execution record, not an informal notebook run. Registered experiments must conform to `schemas/experiment.schema.json`, name a model contract, predeclare an acceptance rule, identify inputs and environment, and preserve limitations.

| Status | Meaning |
|---|---|
| `PREREGISTERED` | Configuration and decision rule fixed before execution |
| `EXPLORATORY` | Used for discovery; not confirmatory evidence |
| `REFERENCE_VERIFIED` | Reproduced the declared internal mathematical or computational fixture |
| `FAILED` | Did not meet the predeclared rule or could not complete |
| `SUPERSEDED` | Replaced by a linked later version |

Experiment outputs are not automatically validation results. Validation requires a declared real-world or external reference appropriate to the model purpose.
