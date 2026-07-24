# I027 — Hunter Cloudflare worker

Status: candidate record — paired private module evidence complete

Primary Archivist: `AF08-P10`
Independent Verifier: `AF08-V10`
Inspected: 2026-07-23

## Canonical source identity
- private parent source: `jaydumisuni/hunter`;
- branch: `master`;
- exact repository pin: `0c1e9154367e48afb807d4cf5ec6713df94c9ff0`;
- role: Hunter online API/auth/storage/WhatsApp and provider-routing worker;
- private THETECHGUY source and deployment configuration.

## Evidence and boundary
The module supplies online-first availability, auth/session, D1/KV/R2 and provider-routing requirements. The verifier confirmed that Cloudflare bindings, secrets, accounts, models and external APIs are replaceable hosted surfaces and must not become Ptah identity or private-source leakage.

## Bounded outcome
`accepted_for_archive_private_hunter_cloud_worker_requirements_with_hosted_binding_secret_provider_and_fallback_boundaries`

Restrictions: keep code, bindings, secrets and user data private; retain provider/service revisions and degraded/fallback states; do not block unrelated work when optional services fail; do not make Cloudflare or Hunter worker IDs canonical Ptah identities or authority.

This outcome does not authorize implementation.