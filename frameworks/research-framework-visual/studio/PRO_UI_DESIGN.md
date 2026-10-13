# Mathematical Visual Design Studio — Professional UI System V0.4

## Design objective

The desktop application should communicate that it is a mathematical visual-engineering environment, not a generic code editor and not a decorative 3D viewer.

The interface is organized around the operational chain:

`mathematics -> computation -> geometry -> visual encoding -> rendering -> validation -> governed output`

The professional shell must expose power without overstating integration. Every visible capability is classified as one of:

- `BUILT-IN` — available directly in the application;
- `COMPUTE LAB` — executable through the native local-runtime bridge or managed Python environment;
- `ADAPTER` — governed architecture exists, but the one-click end-to-end adapter is not yet complete.

## Workspace architecture

### Activity rail

Four first-class workspaces:

1. **Studio** — mathematical scene, live WebGL canvas, geometry inspector, generated code, provenance and validation.
2. **Compute** — native Python/JavaScript/Julia execution, package profiles, output console and generated-artifact preview.
3. **Engines** — engine architecture, capability states and runtime-management surface.
4. **Quality** — mathematical validation, scientific QA, provenance and non-compensatory evidence controls.

### Studio workspace

The Studio workspace uses a professional engineering layout:

`activity rail | scene explorer | live mathematical viewport | precision inspector`

with a bottom source dock generated from the canonical Visual IR.

The live viewport is not an isolated image. It remains connected to:

- the canonical mathematical object ID;
- parameter values;
- equations;
- mesh resolution;
- camera state;
- provenance engine;
- deterministic seed;
- epistemic status;
- validation gates.

## Visual hierarchy

The interface deliberately uses restrained dark neutral surfaces, low-saturation cyan for active mathematical/compute states, green only for passing runtime/validation conditions, amber for warnings, and red only for failures.

No decorative gradients may imply scientific meaning. Color used in scientific views remains separate from application-chrome color.

Typography hierarchy:

- product title: compact system sans-serif;
- metadata/status: small uppercase labels;
- source/equations/IDs: monospace;
- mathematical viewport: content-controlled scientific rendering.

## Power demonstration

The UI demonstrates the intended multi-engine architecture through a visible chain:

`SymPy -> NumPy/JAX -> PyVista/VTK -> WebGL -> SVG/PDF -> Manim/Blender`

This chain is architectural, not a claim that every adapter is currently one-click executable.

The capability deck makes that distinction explicit.

## Professional UX principles

1. Dense but readable desktop information architecture.
2. No hidden scientific state: object status, provenance and QA stay visible.
3. No fake success state for missing engines.
4. No unrestricted shell box in the normal GUI.
5. Local-runtime execution reports executable path, stdout, stderr and exit state.
6. Generated artifacts remain attached to the governed application workspace.
7. The same mathematical object should be inspectable as geometry, equation, code, render and validation state.
8. Visual polish never overrides scientific correctness or epistemic classification.

## Next professional UX milestones

- editable equation surface with parsing and symbolic validation;
- visual node graph: Domain -> Equation -> Differential Operator -> Geometry -> Encoding -> Renderer;
- project Open/Save/Save As and deterministic project manifests;
- object outliner with multiple scenes and reusable components;
- render queue with SVG/PNG/PDF/MP4 outputs;
- adapter-specific inspectors for PyVista, Manim, Blender, Tectonic/TikZ, Asymptote and Makie;
- command palette and keyboard-shortcut system;
- reproducibility/provenance report view;
- signed/notarized production macOS distribution.

## Acceptance rule

A professional-looking GUI is not sufficient for release. UI release acceptance requires:

`functional build + native macOS package + mathematical tests + runtime bridge checks + provenance integrity + repository manifest synchronization`.
