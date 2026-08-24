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

Run:

```bash
python -m pip install -e .[dev]
python -m framework render --request render_requests/Research_Framework_V4.yaml
python -m framework reproduce --bundle exports/SOURCE_BUNDLE.zip
python -m framework audit --outdir exports
```

`RENDER_PASS` is prohibited if a required artifact, scientific/mathematical/visual gate, provenance gate, or source-only reproduction gate fails.

The current research data are explicitly `ILLUSTRATIVE`; they are not observational evidence.
