# Mathematical-Art Visual Encoding Standard

- Standard ID: `MSR-VIS-001`
- Version: `1.0.0`
- Date: 2026-08-22
- Status: `ACTIVE_FOUNDATION`

## 1. Two independent validation tracks

1. **Mathematical validity:** Does the artifact accurately encode its declared mathematical object, data, transformations, approximations, and uncertainty?
2. **Communication impact:** Has comprehension, interpretation, participation, behavior, or decision influence been evaluated with a declared method?

An artifact may pass mathematical validation while communication impact remains `NOT_EVALUATED`. Aesthetic preference cannot replace either track.

## 2. Artifact classes

| Class | Permitted purpose | Minimum evidence |
|---|---|---|
| `ANALYTICAL` | Read values, relationships, residuals, or uncertainty | Validated encoding, scale, units, provenance, and tolerances |
| `EXPLANATORY` | Explain a mathematical or causal structure | Accurate source mapping and comprehension limitations |
| `PARTICIPATORY` | Support elicitation, exploration, or co-design | Interaction protocol, participant safeguards, and evaluated use |
| `INTERPRETIVE` | Express analogy, atmosphere, or conceptual meaning | Explicit non-empirical label and source attribution |

## 3. Encoding ontology

| Visual property | Default scientific meaning | Required control |
|---|---|---|
| Shape and geometry | Mathematical object or state-space structure | Declare projection, parameterization, and approximation |
| Position | State, parameter, spatial relation, or ordered step | Declare coordinate system and scale |
| Color | Chain class, subsystem, or conceptual family | Repeat meaning with labels, shapes, or line patterns |
| Line style | Evidence state or relationship status | Use machine-readable dash tokens |
| Opacity | Uncertainty, confidence, or evidential strength | State mapping and avoid implying probability without calibration |
| Motion | Time, disturbance, recovery, or iterative learning | Declare time scale and interpolation |
| Texture | Material, environmental, or institutional category | Provide legend and non-texture fallback |

No visual variable receives a new meaning inside an artifact without an explicit local legend.

## 4. Evidence-state line convention

| Evidence state | Stroke convention | Interpretation |
|---|---|---|
| `OBSERVED` | solid | Direct support in the checked evidence boundary |
| `OBSERVED_PARTIAL` | long dash | Only named parts are directly supported |
| `INFERRED` | short dash | Reasoned interpretation |
| `PROPOSED` | dash-dot | Project hypothesis or design |
| `VALIDATED` | double-emphasis solid | Passed a declared bounded validation procedure |
| `REJECTED` | crossed or red dotted | Failed a declared test or contradicted by controlling evidence |
| `NOT_VERIFIED` | dotted | Relevant but not independently checked |
| `NOT_APPLICABLE` | omitted from causal path and stated in text | Outside the bounded object with rationale |

Color is never the only evidence-state carrier.

## 5. Chain colors

`design_tokens.json` assigns stable hues to C01–C10. Labels always include the chain identifier because ten distinct categories cannot be made universally distinguishable by color alone. Cross-cutting axes use neutral patterns rather than additional competing hues.

## 6. Exactness and provenance

Analytical and explanatory artifacts originate from SVG or code. Each generated artifact has a provenance JSON containing:

- stable figure ID and version;
- source script and source checksum;
- model, experiment, data, and citation links;
- mathematical-to-visual mapping;
- precision, projection, and rendering assumptions;
- mathematical-validity and communication-impact statuses;
- alternative text and accessibility review;
- generation command and environment.

Manual post-processing of a generated result creates a new source version and must be declared.

## 7. Accessibility

- Provide concise alternative text plus a longer description for complex artifacts.
- Do not rely on red–green contrast or color alone.
- Maintain readable type and stroke sizes at the declared output dimensions.
- Label axes, scales, units, and uncertainty.
- Respect reduced-motion preferences in interactive artifacts.
- Provide a static equivalent for essential interactive information.

## 8. Generative and AI-created imagery

Generated imagery may be used for clearly labeled interpretive art. It is prohibited for exact diagrams, empirical outputs, spatially precise maps, measured geometry, or any artifact whose pixels must correspond to declared data. Prompts, source assets, model/tool identity, and edits are recorded when they materially affect interpretation.

## 9. Admission checklist

An artifact enters `figures/publication/` only after its identity, source, model/data links, encoding map, uncertainty, mathematical review, accessibility, communication-impact status, limitations, and generation command are complete.
