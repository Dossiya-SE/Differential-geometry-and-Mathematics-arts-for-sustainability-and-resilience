# Security Policy

## Supported versions

Security fixes are applied to the latest release and the active development branch.

## Reporting a vulnerability

Do not publish credentials, personal data, exploitable details, or restricted datasets in a public issue. Use GitHub private vulnerability reporting when enabled, or contact the repository owner through a private channel listed on the owner's GitHub profile.

Include the affected path and version, impact, minimal reproduction, and any safe mitigation. Reports should not contain real participant data.

## Research-data safeguards

- Commit only public, synthetic, anonymized, or explicitly redistributable data.
- Store access-controlled or sensitive data outside the repository.
- Never commit API keys, tokens, private URLs, or credentials.
- Treat geospatial, demographic, health, and infrastructure-location data as potentially sensitive even when technically public.
- Document aggregation, privacy, and threat-model assumptions in model and experiment records.

Automated dependency and secret checks supplement review; they do not establish that a model, dataset, or visual product is ethically safe.
