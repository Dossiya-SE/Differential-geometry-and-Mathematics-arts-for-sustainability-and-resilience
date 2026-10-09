# MVS Scientific Core Engine v0.1

Status: **experimental engine pack, governed by Visual IR and the MVS Engine Protocol**.

This engine begins the free/open mathematical capability layer described by the studio architecture. It is intentionally small enough to audit and test before larger engine packs are admitted.

## Included engines

| Engine | Frozen version | Role |
|---|---:|---|
| NumPy | 2.3.5 | numerical array kernel; compatibility-pinned for Geomstats 2.8.0 |
| SciPy | 1.18.0 | scientific algorithms |
| SymPy | 1.14.0 | exact symbolic mathematics |
| Geomstats | 2.8.0 | differential/Riemannian geometry |
| NetworkX | 3.6.1 | graph algorithms |
| Google OR-Tools | 9.15.6755 | network and combinatorial optimization |

The development engine baseline is **CPython 3.12**. Release Engine Packs will be built and content-addressed per supported target architecture rather than pretending one binary payload is portable everywhere.

### Compatibility decision

The first cross-platform CI run intentionally used NumPy 2.5.2 and exposed a real upstream compatibility break: Geomstats 2.8.0 imports `numpy.trapz`, while NumPy removed that deprecated API in 2.4.0. The engine therefore pins NumPy 2.3.5, the latest 2.3.x release, until a released Geomstats version no longer depends on `numpy.trapz`. This is a compatibility constraint, not an attempt to silently patch third-party code.

## Governing rule

The worker is not an unrestricted Python console. Requests use protocol `mvs.engine/1.0` and can invoke only registered operations:

- `system.capabilities`
- `symbolic.simplify`
- `geometry.sphere_geodesic`
- `graph.shortest_path`
- `optimization.min_cost_flow`

No operation exposes shell execution, arbitrary Python evaluation, arbitrary imports, filesystem I/O, process spawning, or network access.

The AI layer must eventually call these typed operations. It must not receive direct authority over Python, Bash, package installation, or the project filesystem.

## Scientific contracts

### Symbolic mathematics

The first symbolic operation uses a bounded AST parser. Only arithmetic, declared symbols, and a small allow-list of mathematical functions are accepted. Python attribute access, imports, comprehensions, indexing, arbitrary function calls, and other executable syntax are rejected.

### Riemannian geometry

The first geometry operation computes a shortest geodesic on the unit sphere `S²` through Geomstats. Inputs must already lie on the manifold. The worker does **not** silently normalize invalid points. Antipodal endpoints are rejected because the shortest geodesic is not unique. Returned samples are checked against the unit-sphere invariant.

### Graph analysis

The first graph operation computes a weighted Dijkstra shortest path with NetworkX. Node identity is explicit, edges may not reference unregistered nodes, and negative weights are rejected for this operation.

### Network optimization

The first optimization operation uses OR-Tools `SimpleMinCostFlow`. Capacities, costs, and supplies are integral. Supplies must sum to zero. Solver status is preserved explicitly; a result is marked `verifiedOptimal` only when OR-Tools returns `OPTIMAL`.

## Provenance and determinism

Every successful response records:

- engine ID and engine version;
- protocol version;
- exact installed dependency versions;
- canonical request SHA-256;
- canonical result SHA-256;
- explicit `networkUsed: false`.

The source worker and frozen dependency requirements are themselves content-addressed by `engine-packs/scientific-core/manifest.json`.

## Verification gates

CI runs the worker on both Linux and Apple Silicon macOS with CPython 3.12 and checks:

1. exact dependency identities;
2. engine permission declarations;
3. worker and dependency-lock content hashes;
4. bounded symbolic parsing and rejection of executable syntax;
5. geodesic distance on `S²`;
6. manifold residuals for sampled geodesic points;
7. deterministic NetworkX shortest-path behavior;
8. OR-Tools optimal min-cost-flow result;
9. byte-for-byte deterministic protocol output for repeated requests;
10. fail-closed handling of unknown fields and operations;
11. manifest JSON Schema validity.

These are **software verification tests**. They do not establish empirical validity for a scientific model or dataset.

## Next engine admissions

After this pack remains green across the supported platforms:

1. Penrose mathematical constraint-diagram adapter;
2. PyVista/VTK scientific 3D pack;
3. GUDHI topology pack with dependency-level license audit;
4. Geometry Central native discrete-differential-geometry pack;
5. Manim animation pack;
6. external Blender bridge.

Each must enter through the same typed protocol, provenance, validation, licensing, and content-addressing gates.
