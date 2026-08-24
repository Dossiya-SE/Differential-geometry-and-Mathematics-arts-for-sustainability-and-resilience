# Research Framework Visual — V4 Governed Renderer

This module implements a fail-closed scientific-rendering controller.

Governing chain:

`request -> research specification -> mathematical objects -> computation -> verification -> rendering -> audit -> editable release`

An accepted render produces:

- `poster_EDITABLE.svg` — canonical visual master
- `poster_EDITABLE.pptx` — convenience-editable derivative
- `poster.png`
- `poster.pdf`
- `render_request.yaml`
- `equations.tex`
- `research_data.json`
- `manifest.json`
- `qa_report.json`
- `SOURCE_BUNDLE.zip`

## Standard run

```bash
python -m pip install -e .[dev]
python -m framework doctor --strict
python -m framework render --request render_requests/Research_Framework_V4.yaml
python -m framework reproduce --bundle exports/SOURCE_BUNDLE.zip
python -m framework audit --outdir exports
```

## MacBook / Apple Silicon notebook environment

The local target includes macOS on Apple Silicon with Python 3.13. The important rule is that creating a `.venv` is not sufficient by itself: the Jupyter process must also come from that same environment.

Use the deterministic bootstrap:

```bash
./scripts/bootstrap_macos.sh
```

Then launch Jupyter with:

```bash
./scripts/launch_jupyter_macos.sh
```

The launcher executes `.venv/bin/python -m notebook` directly. This prevents an existing Conda/base installation, shell alias, or cached `jupyter` command from silently starting a different Python environment.

Before any notebook or render, the environment can be audited with:

```bash
.venv/bin/python -m framework doctor --strict --notebook
```

The doctor checks:

- Python version and machine architecture;
- active interpreter versus `VIRTUAL_ENV`;
- Conda/venv overlap warnings;
- CairoSVG import and a real SVG-to-PNG conversion;
- PPTX creation;
- Jupyter executable provenance;
- NumPy and Matplotlib availability;
- Matplotlib-bundled DejaVu font availability and Pillow loading.

If native Cairo is missing on macOS, install it with Homebrew and rerun the doctor:

```bash
brew install cairo libffi
```

## Notebook dependency profile

Notebook work is intentionally optional for the deterministic renderer:

```bash
python -m pip install -e '.[dev,notebook]'
```

The notebook extra currently constrains the tested major-version families for Jupyter, Notebook, IPython kernel, NumPy, and Matplotlib while keeping the core renderer smaller.

## Fail-closed status

`RENDER_PASS` is prohibited if a required artifact, scientific/mathematical/visual gate, provenance gate, or source-only reproduction gate fails.

The current research data are explicitly `ILLUSTRATIVE`; they are not observational evidence.
