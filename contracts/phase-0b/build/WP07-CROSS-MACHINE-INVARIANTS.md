# WP07 Cross-Machine Invariants

**Status:** CANDIDATE  
**Date:** 2026-07-19

These invariants connect the individual WP07 lifecycle machines without collapsing them into one generic status.

1. Recipe proposal, acceptance, readiness, backend compatibility, compilation, execution and verification remain separate records and projections.
2. A Recipe Revision cannot execute without exact acceptance authority and non-expired target readiness/compatibility evidence.
3. Build Run and Step Run project execution; WP02 Activity, Operation and Attempt remain canonical work identities.
4. Every physical retry creates a new Attempt ID/nonce and rebinds exact Provider generation and connection epoch.
5. A cache hit may satisfy an Operation only after an immutable Cache Use Decision; it is never evidence of newly executed work.
6. Output declaration, produced Object, Artifact promotion, Location materialization and Artifact Release remain separate.
7. `build.run.succeeded` cannot imply export, SBOM completeness, attestation verification, signature validity, reproduction, review or release acceptance.
8. SBOM existence cannot imply completeness, vulnerability absence, licence acceptability or runtime use.
9. Attestation creation, signature creation, trust verification, transparency inclusion and release approval remain separate.
10. A valid signature proves only the policy-bounded signer/subject/digest claim; it does not prove functional correctness.
11. Offline verification may pass only under an exact trust-policy revision that allows the supplied bundle and freshness limits.
12. Independent reproduction must satisfy its declared separation conditions; same-provider same-cache reruns are classified as repeated execution, not independent reproduction.
13. Build success with failed export/proof/signing preserves immutable outputs and honest partial state.
14. Late, duplicate, stale-generation and contradictory evidence is retained and reconciled explicitly rather than silently overwriting current truth.
15. Backend replacement creates new compatibility assessments, compiled plans, runs and attempts while preserving stable Recipe, Object, Artifact and provenance identity.
16. Raw credential values are forbidden from ordinary entities, logs, caches, outputs, SBOMs, attestations and public bundles; only references, scoped grants and cleanup evidence are recorded.
