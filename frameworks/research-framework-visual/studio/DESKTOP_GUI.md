# Desktop GUI Architecture

## Decision

The Mathematical Visual Design Studio uses **Tauri 2** as its native graphical user interface framework.

Tauri is the desktop shell; it does not replace the scientific or mathematical engines.

## Separation of responsibilities

```text
Native OS window / menus / packaging     -> Tauri + Rust
Interactive application interface        -> React + TypeScript
2D/3D live rendering                     -> SVG / Canvas / Three.js / WebGL
Canonical mathematical object model      -> Visual IR
Scientific and symbolic computation      -> Python / NumPy / SymPy / SciPy
Publication mathematics                  -> LaTeX
Future high-end renderers                 -> PyVista / Manim / Blender / WebGPU
```

## Why this architecture

1. The existing React/Three.js studio can be reused directly.
2. The installed application runs in a dedicated native window rather than a browser tab.
3. Rust provides a controlled boundary for future filesystem, process, export and local scientific-engine integration.
4. Tauri uses the operating system webview instead of bundling a complete browser runtime.
5. Browser development remains available without making it the final user experience.

## Security boundary

The native shell currently grants only `core:default` capability. Native filesystem/process permissions are intentionally not enabled until a concrete feature requires them.

The CSP is explicit and restrictive. Future adapters must request the minimum Tauri capability required and add tests for that capability.

## Installation state

V0.2 is a development desktop application. GitHub Actions produces an unsigned macOS DMG artifact.

A public production release still requires:

- Apple Developer signing
- notarization
- release identity/version policy
- update-signing strategy if auto-update is enabled
- repository-wide manifest synchronization
