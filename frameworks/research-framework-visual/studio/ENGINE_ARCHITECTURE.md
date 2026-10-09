# Mathematical Visual Design Studio — Engine Architecture V0.3

The installed desktop application is the control surface for a governed collection of mathematical, scientific-computing, geometry, rendering and publication engines.

## Principle

One mathematical object should be reusable across specialized engines instead of being rewritten separately for each language.

`Visual IR -> computation adapters -> geometry adapters -> rendering adapters -> validation -> export`

## Executable languages available from the native Compute Lab

The desktop application can execute reviewed local code through explicit native commands for:

- Python — primary scientific-computing language.
- JavaScript / Node.js — application-side numerical logic and tooling.
- Julia — high-performance numerical mathematics when installed.

The application deliberately does **not** provide an unrestricted shell box. Local code execution is a trusted-workstation capability and runs with the permissions of the current macOS user.

## Python scientific profiles

The GUI can create and manage an application-owned Python virtual environment under the user's macOS Application Support directory.

### Core Scientific

- NumPy
- SciPy
- SymPy
- Matplotlib
- Pillow
- NetworkX
- pandas
- Plotly

### Geometry / VTK

Core Scientific plus:

- PyVista
- VTK

### Advanced / JAX

Geometry / VTK plus:

- JAX

### Animation / Manim

Core Scientific plus:

- Manim Python package

Manim may additionally require native system dependencies such as FFmpeg and Cairo/Pango components depending on the local macOS configuration.

### Full Python Lab

Geometry / VTK + JAX + Manim.

## External engine discovery

The Runtime Manager detects and reports readiness for:

- Blender — cinematic 3D, Geometry Nodes and Python-driven rendering.
- Manim — mathematical animation.
- Tectonic — reproducible LaTeX/PDF compilation.
- FFmpeg — animation/video encoding.
- Graphviz — graph and dependency-layout rendering.
- Asymptote — precise mathematical vector/3D diagrams.
- Julia — future Makie adapter target.

## In-application render engines

Already embedded in the application:

- React + TypeScript — GUI and interaction layer.
- Three.js + WebGL — live differential-geometry renderer.
- GLSL — GPU visual encoding/shaders.
- KaTeX — live mathematical typography.
- Visual IR — canonical mathematical-object boundary.

## Planned adapters

The architecture keeps extension points for:

- Manim renderer adapter
- Blender scene/Geometry Nodes adapter
- PyVista/VTK scene adapter
- TikZ/Tectonic publication adapter
- Asymptote adapter
- Julia/Makie adapter
- WGSL/WebGPU compute/render adapter
- Rust/WebAssembly kernels
- JAX automatic-differentiation backend

## Security boundary

The native application can execute user-authored Python, JavaScript and Julia. Those languages are powerful enough to read or modify files and access network resources available to the macOS user account. The runtime lab therefore:

1. exposes only explicit language executors rather than arbitrary shell commands;
2. shows the exact executable path being used;
3. reports stdout, stderr and exit status;
4. separates browser preview from native execution;
5. keeps scientific evidence classification independent from execution success.

A future high-assurance mode should add process timeouts, per-project working directories, filesystem/network policy controls, and optional sandbox/container execution for untrusted code.

## Scientific rule

Successful execution or visually impressive output does not establish empirical validity. Every visual object retains its epistemic status and remains subject to mathematical, scientific, provenance and rendering QA.
