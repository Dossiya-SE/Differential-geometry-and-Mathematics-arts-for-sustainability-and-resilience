# MVS v0.1.1 executable vertical slice

## Status

`PROPOSED_IMPLEMENTATION` until all repository CI checks and all six MVS release gates pass.

## Frozen invariant

```text
LLM intent -> formal constraints -> validated computation -> Visual IR -> renderer
```

Visual IR is the mathematical authority. Renderer state is never accepted as mathematical truth.

## Implemented slice

The first benchmark is the unit two-sphere with deterministic sample points and tangent vectors:

- points satisfy `||x_i|| = 1`;
- tangent vectors satisfy `x_i^T v_i = 0` within numerical tolerance;
- pairwise geodesic distances satisfy the configured minimum separation;
- the validated scene is serialized into immutable `VisualIR` objects;
- the Spline adapter exports renderer payloads while preserving semantic IDs and locked geometry;
- style edits are allowed without mutating the mathematical snapshot.

The adapter currently provides a deterministic renderer-neutral payload for the Spline boundary. It does **not** claim live Spline MCP connectivity. That external integration remains outside the v0.1.1 mathematical proof obligation.

## Registry contract

The vertical slice exposes the frozen sequence:

```text
search -> describe -> execute -> task_status
```

Capabilities and task execution are distinct from mathematical validation.

## Strict release gate

The release is admissible only when all six conditions pass:

1. mathematical validity;
2. constraint preservation;
3. determinism;
4. editability;
5. round-trip semantic identity;
6. safety: style mutation cannot alter locked mathematical state.

Formally, `Release(0.1.1) = AND(T_1, ..., T_6)`. Five of six is a failure.

## Scope boundary

No persistent homology, vector-field expansion, infrastructure digital twin, additional renderer, or additional mathematical engine is admitted before this vertical slice passes its complete release gate.
