# Mathematical Visual Design Studio — V0.2 Desktop GUI

A governed mathematical/scientific visual engineering application built around a common Visual IR.

The application now has two presentation modes:

- **Native desktop GUI** — Tauri 2 + Rust system shell around the React/TypeScript/Three.js studio.
- **Web preview** — Vite development server for browser-only iteration.

The native application opens in its own operating-system window. It does not require the user to work inside a browser once the desktop bundle is installed.

## Implemented

- React + TypeScript GUI
- Tauri 2 native desktop shell
- common Visual IR 0.1.0
- Three.js/WebGL differential-geometry live canvas
- generated Python / TypeScript / GLSL / LaTeX source views from the same object
- scientific validation gates for a curvature-coded torus
- Python adapter for downstream scientific computation
- epistemic status preserved in the object model
- macOS `.dmg` build path
- GitHub Actions native macOS build and artifact upload

The demonstrator uses the regular torus

`X(u,v)=((R+r cos v) cos u,(R+r cos v) sin u,r sin v)`

with analytic Gaussian curvature

`K(v)=cos(v)/(r(R+r cos(v)))`.

Validation checks `R > r > 0`, finite sampled curvature, and metric regularity `EG-F^2 > 0`. The object remains explicitly `ILLUSTRATIVE`; rendering quality does not convert it into empirical evidence.

## macOS: first-time setup

Requirements:

- macOS
- Node.js 22+
- Rust stable (`rustc` + `cargo`)
- Xcode Command Line Tools

Run:

```bash
bash scripts/bootstrap_macos_gui.sh
```

## Open the native GUI during development

```bash
npm run gui
```

Tauri starts the Vite frontend and opens **Mathematical Visual Design Studio** in its own native application window.

## Build an installable macOS application

```bash
npm run gui:build -- --bundles dmg
```

The installer is generated under:

```text
src-tauri/target/release/bundle/dmg/
```

Open the `.dmg`, then drag **Mathematical Visual Design Studio** into Applications.

Unsigned development builds can trigger macOS Gatekeeper warnings. Production distribution should add Apple Developer signing and notarization rather than bypassing Gatekeeper.

## Browser-only development

```bash
npm install
npm run check
npm run dev
```

## Quality commands

```bash
npm run test
npm run build:web
npm run desktop:check
npm run check
```

## Architecture

```text
React / TypeScript GUI
        |
        v
Common Visual IR
        |
   +----+-------------------+
   |                        |
Three.js/WebGL          Python adapter
   |                        |
Live geometry           scientific compute
   |
Tauri 2 / Rust
   |
Native macOS window + installable bundle
```

Tauri is only the desktop application shell. Mathematical meaning remains in the Visual IR and scientific engines, keeping rendering, computation, and GUI concerns separated.

Future adapters remain: PyVista/VTK, Manim, Blender, TikZ/Asymptote, WGSL/WebGPU, Julia/Makie, and Rust/WASM.
