# Mathematical specification layer

This directory is authoritative for the mathematical meaning of implemented models. Code may realize a specification; it may not silently redefine it.

## Contents

| Directory | Research object |
|---|---|
| `notation/` | Project-wide symbols, domains, codomains, units, and collision controls |
| `definitions/` | Definitions used by more than one derivation or model |
| `assumptions/` | Versioned assumption register and applicability conditions |
| `propositions/` | Propositions, proof status, and computational consequences |
| `derivations/` | Stepwise derivations and numerical forms |
| `model_contracts/` | Machine-readable contracts linking mathematics to code and tests |

## Admission rule

A mathematical object enters the executable platform only when its notation, assumptions, singularities, numerical tolerance, supporting source, implementation path, and verification tests can be named. Domain-specific mathematics remains proposed until an application is selected.
