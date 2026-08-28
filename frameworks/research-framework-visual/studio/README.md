# Mathematical Visual Design Studio — V0.3 Native Compute GUI

A governed mathematical/scientific visual engineering application built around a common Visual IR.

The installed macOS application is designed for normal desktop use: open it from Applications, create or inspect mathematical visuals, run supported mathematical code, inspect runtime readiness, and use managed scientific Python profiles without working in Terminal during ordinary use.

## Native application architecture

- **Tauri 2 + Rust** — native macOS GUI shell and controlled local-runtime bridge.
- **React + TypeScript** — interactive studio interface.
- **Three.js + WebGL + GLSL** — live mathematical geometry/rendering.
- **KaTeX** — mathematical typography.
- **Visual IR 0.1.0** — canonical mathematical-object boundary.

## Native Compute Lab

The installed GUI now includes a runtime manager and code console.

Executable directly in the native application:

- Python
- JavaScript / Node.js
- Julia, when installed

Runtime discovery also reports:

- Blender
- Manim
- Tectonic
- FFmpeg
- Graphviz
- Asymptote

The studio shows the executable path, version, stdout, stderr and exit status instead of hiding which runtime produced a result.

## One-click scientific Python profiles

The GUI can create an application-owned Python environment under macOS Application Support and install profiles without requiring normal Terminal use.

- **Core Scientific** — NumPy, SciPy, SymPy, Matplotlib, Pillow, NetworkX, pandas, Plotly.
- **Geometry / VTK** — Core + PyVista + VTK.
- **Advanced / JAX** — Geometry + JAX.
- **Animation / Manim** — Core + Manim Python package.
- **Full Python Lab** — Geometry + JAX + Manim.

Some animation/cinematic engines can still require native external components such as FFmpeg, Cairo/Pango, Blender, Julia or Asymptote. The Runtime Manager marks those dependencies READY or NOT FOUND. They are adapter targets rather than silently assumed dependencies.

See `ENGINE_ARCHITECTURE.md` for the full toolchain and security boundary.

## Current mathematical demonstrator

The application currently renders the regular torus

`X(u,v)=((R+r cos v) cos u,(R+r cos v) sin u,r sin v)`

with analytic Gaussian curvature

`K(v)=cos(v)/(r(R+r cos(v)))`.

Validation checks `R > r > 0`, finite sampled curvature, and metric regularity `EG-F^2 > 0`. The object remains explicitly `ILLUSTRATIVE`; execution or rendering quality does not convert it into empirical evidence.

## macOS development setup

Requirements for source development:

- macOS
- Node.js 22+
- Rust stable (`rustc` + `cargo`)
- Xcode Command Line Tools

Run:

```bash
bash scripts/bootstrap_macos_gui.sh
npm run gui
```

## Build the installable macOS application

```bash
npm run gui:build -- --bundles dmg
```

The installer is generated under:

```text
src-tauri/target/release/bundle/dmg/
```

Open the `.dmg`, drag **Mathematical Visual Design Studio** into Applications, then use it as a normal Mac application.

Unsigned development builds can trigger macOS Gatekeeper warnings. Production distribution should add Apple Developer signing and notarization.

## Browser-only development

```bash
npm install
npm run check
npm run dev
```

Native code execution is deliberately unavailable in browser preview mode.

## Quality commands

```bash
npm run test
npm run build:web
npm run desktop:check
npm run check
```

## Architecture

```text
Native macOS Application
        |
        v
Tauri 2 / Rust runtime bridge
        |
        +----------------------+---------------------+
        |                      |                     |
React / TypeScript         Local runtimes       Managed Python
        |                  Python/Node/Julia     scientific env
        v                      |                     |
Common Visual IR -------------+---------------------+
        |
        +----------------------+---------------------+
        |                      |                     |
Three.js/WebGL/GLSL       Scientific Python      External adapters
live geometry             NumPy/SciPy/SymPy      Blender/Manim/etc.
        |
        v
Validation + governed export
```

The next adapter layer is designed for PyVista/VTK scene exchange, Manim animation generation, Blender/Geometry Nodes, TikZ/Tectonic, Asymptote, Julia/Makie, WGSL/WebGPU and Rust/WASM while preserving one canonical Visual IR.
