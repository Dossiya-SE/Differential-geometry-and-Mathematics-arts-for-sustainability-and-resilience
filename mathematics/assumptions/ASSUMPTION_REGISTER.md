# Assumption register

| ID | Scope | Statement | Status | Failure consequence |
|---|---|---|---|---|
| `A-001` | `MSR-MOD-0001` | Input points are finite nonzero vectors normalized to the unit sphere. | `OBSERVED` | Geometry functions reject the input. |
| `A-002` | `MSR-MOD-0001` | The principal logarithm is evaluated away from the antipode of its base point. | `OBSERVED` | The principal direction is non-unique and the implementation raises an error. |
| `A-003` | `MSR-MOD-0001` | Reference calculations use IEEE 754 binary64 arithmetic. | `OBSERVED` | Declared tolerances require re-evaluation. |
| `A-004` | Platform | The sphere fixture is domain-neutral and carries no sustainability or resilience semantics. | `PROPOSED` | Any domain interpretation must be removed or separately justified. |

Assumptions are not evidence of real-system behavior. Application-specific assumptions may be added only after application selection or within clearly labeled candidate feasibility work.
