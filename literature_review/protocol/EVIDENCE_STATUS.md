# Evidence Status Protocol

## Purpose

This protocol prevents statements made by source authors, reviewer interpretations, external corroboration, and new project proposals from being blended into one apparent evidence class.

## Status vocabulary

| Status | Meaning | Permitted use |
|---|---|---|
| `OBSERVED` | Explicitly verified in the reviewed full text, table, figure, equation, or supplement | May support a source-level finding with a page or section locator |
| `INFERRED` | A reasoned interpretation derived from observed evidence but not stated by the source authors | Must be identified as interpretation and accompanied by its reasoning |
| `EXTERNAL` | Supported by an independently verified source or dataset | Must cite the independent evidence directly |
| `PROPOSED` | A new construct, mapping, hypothesis, model, or demonstrator introduced by this project | Is not evidence and cannot be attributed to the reviewed source |
| `NOT_OBSERVED` | A searched-for concept or result was not found in the reviewed material | Applies only to the reviewed material; it is not a global absence claim |
| `NOT_VERIFIED` | The source states that an artifact or result exists, but it has not been independently inspected or executed | Cannot support a reproducibility claim |

## Directness rules

1. A paper is not a differential-geometry application merely because it uses the words *geometry*, *shape space*, *distance*, or *topology*.
2. Topology optimization is not automatically algebraic topology, topological data analysis, or differential geometry.
3. A material-weight objective is not a quantified sustainability assessment unless environmental, resource, economic, social, or integrated sustainability outcomes are calculated.
4. Repairability of a computational representation is not proof of physical recovery or dynamic reachability.
5. Visual attractiveness is not evidence of scientific accuracy or decision value.
6. A numerical example alone is insufficient for field validation.

## Required traceability

Every substantive case-study claim should contain:

- evidence status;
- page, section, equation, table, or figure locator;
- direct or transferable relationship to the review question;
- limitation or boundary condition;
- source identifier.

