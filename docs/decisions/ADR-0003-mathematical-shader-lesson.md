# ADR-0003: Introduce a shader as a bounded mathematical learning artifact

- Status: Proposed, pending review and shader-device verification
- Date: 2026-10-09
- Domain: `NOT_SELECTED`

## Decision

Allow one self-contained WebGL2 fragment shader and minimal browser JavaScript within `art/shaders/inversion_lab/`. Keep Python/NumPy as the mathematical reference implementation of `MSR-MOD-0002`. Use a dependency-free ECMAScript module for pointwise coordinate diagnostics and Node.js 22's built-in test runner for a numerically independent browser-kernel check. Node.js is an explicitly pinned CI verification tool, not a frontend build dependency. Use no new build-time frontend dependencies. The browser presentation has a static SVG reference and supports reduced motion. No unrelated interface or package dependencies are introduced.

## Justification for GLSL

A fragment shader performs parallel per-pixel evaluation of a mathematical mapping with interactive parameters, which cannot be taught equally well by static SVG alone. GLSL is a **rendering language only**, not a second scientific model authority. It follows existing ADR-0002's staged language policy.

## Verification interface and gate

Python reference tests check the inversion, involution, Jacobian and singularities. The shader must be compared with the same benchmark points and inspected on actual WebGL2 implementations prior to accepted gallery/publication status. WebGL `highp` is not automatically equivalent to binary64. Frame-rate and pixel derivatives affect appearance but do not validate the map.

## Removal or promotion criteria

Remove the experiment if it cannot be maintained or reproducibly rendered. Promote it only after browser screenshot testing, accessible fallback validation, documented device constraints, and independent review. If multiple interactive artifacts are admitted, migrate to a small TypeScript build with a pinned lockfile, shared fixtures, and cross-language tests.

## Nonclaims

This geometry fixture does not represent infrastructure state, network propagation, resilience, sustainability improvement, or an empirically validated scientific result. It does not select any application domain.
