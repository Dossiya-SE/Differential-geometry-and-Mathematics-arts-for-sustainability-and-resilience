# ADR-0002: Adopt a staged language policy

- Status: Accepted
- Date: 2026-08-22

## Decision

Python is the reference computational language. Markdown, LaTeX, Quarto, SVG, YAML, JSON Schema, and TOML support mathematical specification, publishing, art, and machine-readable records. TypeScript is reserved for interactive web artifacts. Julia is added only after a documented benchmark shows that manifold optimization, differential-equation simulation, or constrained optimization materially benefits from it.

## Rationale

Multiple languages increase environment, interface, and verification costs. A language enters the repository only when it has a distinct responsibility and can share contracts, fixtures, tolerances, and provenance with the reference implementation.

## Consequences

- Rust, C++, Lean, Blender, and GLSL remain optional specialized tools.
- A future Julia implementation must pass cross-language fixtures against the reference model.
