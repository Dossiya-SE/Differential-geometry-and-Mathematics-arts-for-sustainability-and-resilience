# ADR-0001: Keep the research core domain-neutral

- Status: Accepted
- Date: 2026-08-22

## Context

The project is evaluating 12 application families. Earlier work used coupled P-W-T-SW infrastructure under urban flooding as a working demonstrator, but the selection protocol has not been completed.

## Decision

Core mathematics, schemas, software, tests, and visual encodings will not depend on a selected sector, hazard, geography, or demonstrator. Domain adapters may be created only after an application passes the governing selection protocol.

## Consequences

- The reference experiment uses the unit two-sphere as a neutral mathematical fixture.
- Application-specific assumptions cannot enter shared interfaces without an explicit architectural review.
- `DECISION_STATUS.yaml` remains authoritative for selection state.
