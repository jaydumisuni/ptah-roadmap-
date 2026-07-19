# Phase 0B WP07 — Recipe, Build, Provenance, SBOM, Signature and Verification

**Status:** CANDIDATE COMPLETE — DOWNSTREAM CONTRACT USE APPROVED; IMPLEMENTATION FREEZE DEFERRED  
**Date:** 2026-07-19  
**Runtime implementation:** NOT STARTED  
**Dependency/backend selection:** NOT STARTED

## Purpose

Turn the frozen Build/Artifact/Provenance architecture into exact candidate identities, schemas, lifecycles, migration rules and conformance expectations without selecting BuildKit, Dagger, ORAS, Syft, Witness, in-toto, Sigstore or one native platform backend.

WP07 closes the boundary from project/Recipe detection through accepted immutable Recipe Revision, backend compilation, Build execution, output registration, SBOM, attestation, signature, verification and independent reproduction without allowing any stage to impersonate release acceptance.

## Normative records

- `contracts/phase-0b/build/BUILD-RECIPE-PROVENANCE-CONVENTIONS.md`
- `contracts/phase-0b/build/BUILD-RECIPE-PROVENANCE-CONVENTIONS.v0.1.1.md`
- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP07-SUPPLEMENT.md`
- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP07-CORRECTION-0.1.1.md`
- `schemas/phase-0b/build/schema-catalog.v0.1.1.json`
- `migrations/phase-0b/WP07-BUILD-PROVENANCE-MIGRATION-COMPATIBILITY.md`
- `conformance/PHASE-0B-WP07-BUILD-PROVENANCE-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp07/build-provenance-cases.v0.1.0.json`
- `conformance/fixtures/phase-0b/wp07/build-provenance-cases.v0.1.1.json`

Catalog `0.1.1` supersedes catalog `0.1.0` without mutating candidate history. ADR-0024A records the final corrected schema/lifecycle selection and conventions/fixture additions.

## Candidate schema set

The corrected Build catalog contains 30 active schemas:

1. shared Build/provenance definitions;
2. Build Recipe;
3. immutable Build Recipe Revision;
4. Recipe Proposal;
5. Recipe Acceptance;
6. Backend Compatibility;
7. Build Readiness;
8. Compiled Plan;
9. Build Run;
10. Build Step;
11. Output Declaration;
12. Build Output Record;
13. Cache Record;
14. Cache Use;
15. Secret Access;
16. Package Observation;
17. SBOM Coverage;
18. SBOM Document;
19. Trust Policy;
20. Transparency Evidence;
21. Attestation;
22. Attestation Verification;
23. Signature;
24. Signature Verification;
25. Proof Bundle;
26. Verification Run;
27. Reproduction Request;
28. Reproduction Run;
29. Reproduction Comparison;
30. Provenance Graph Revision.

Dependencies:

- `ptah.common` `0.1.0`;
- `ptah.activity` `0.1.1`;
- `ptah.object` `0.1.0`;
- `ptah.runtime` `0.1.2`;
- `ptah.workspace` `0.1.0`;
- `ptah.transfer` `0.1.0`.

### Final active corrections

Catalog `0.1.1` selects:

- Build Recipe Revision `0.1.1`;
- Build Readiness `0.1.1`;
- Build Run `0.1.1`;
- Backend Compatibility `0.1.0`;
- Build Output Record `0.1.0`;
- Transparency Evidence `0.1.0`;
- the remaining active schemas at the versions listed in the catalog.

Superseded candidate records remain preserved:

- Build Recipe Revision `0.1.0`, because acceptance state was embedded inside an immutable Revision;
- Build Readiness `0.1.0`, because it did not bind one exact locality/generation context;
- Build Run `0.1.0`, because compatibility, Dispatch Eligibility and connection-epoch evidence were incomplete;
- Secret Access lifecycle `0.1.0`, because terminal expiry conflicted with later cleanup failure.

## Lifecycle machines

Nine namespaced lifecycles are included:

- `build.recipe.lifecycle` `0.1.0`;
- `build.run.lifecycle` `0.1.0`;
- `build.step.lifecycle` `0.1.0`;
- `build.cache_record.lifecycle` `0.1.0`;
- `build.secret_access.lifecycle` `0.1.1`;
- `provenance.trust_policy.lifecycle` `0.1.0`;
- `provenance.verification_run.lifecycle` `0.1.0`;
- `provenance.reproduction_request.lifecycle` `0.1.0`;
- `proof.reproduction_run.lifecycle` `0.1.0`.

Acceptance, Readiness, Backend Compatibility, SBOM coverage, signature/attestation decisions, proof domains and reproduction comparison remain separate immutable decisions/results rather than lifecycle states.

## Accepted boundaries

### Recipe and compilation

1. Recipe, immutable Revision, Proposal, Acceptance, Backend Compatibility, Readiness, Plan and Run remain separate.
2. project files, paths, Dockerfiles, CI workflows and backend graph/job IDs remain source Objects or Aliases.
3. detected/imported configuration cannot execute without authorized Acceptance.
4. acceptance state is prohibited inside the immutable Recipe Revision.
5. Backend Compatibility is directional, target-specific and cannot silently weaken required semantics.
6. Readiness binds one exact local or remote execution context and expires.
7. Compiled Plan never mutates Recipe Revision and remains backend-specific/replaceable.
8. `build.step` is the run-scoped Step record; embedded Recipe `step_key` is the immutable definition key. The redundant draft `build.step_run` token is removed.

### Execution

1. Build Run binds exact Recipe/Acceptance/Compatibility/Readiness/Plan/Workspace Materialization/Provider generation and connection epoch.
2. local Builds require exact Node evidence; remote Builds use approved remote-service evidence and never fabricate Nodes.
3. Build Step maps to WP02 Operations and physical Attempts.
4. retries create new Attempts/nonces and retain every Receipt.
5. `build_completed` means required Build steps completed only.
6. export, SBOM, attestation, signing, verification, review, reproduction and release remain separate.
7. uncertain non-idempotent effects block automatic retry until reconciliation.
8. partial outputs survive downstream failure with exact evidence.

### Materials and cache

1. mutable branches/tags/ranges/URLs/paths resolve to immutable evidence or remain explicitly mutable/volatile/unresolved.
2. declared versus observed materials remain separate.
3. Cache Record binds exact producer and identity dimensions.
4. Cache Use is consumer-specific and policy-bound.
5. cache hit is not execution, fresh proof or independent reproduction.
6. cache eviction never removes canonical provenance.

### Secrets

1. raw secret values are prohibited in ordinary/public Build/provenance records.
2. Secret Access binds exact credential reference, Attempt, scope, delivery method and expiry.
3. Provider secret injection does not prove non-leakage.
4. revocation/cleanup/leak scans are separate evidence.
5. lifecycle `expired` requires verified access absence and cleanup; cleanup uncertainty/failure becomes `cleanup_failed` directly.
6. cleanup failure remains explicit and restricted.

### Outputs and release

1. Output Declaration and produced Output Record remain separate.
2. Output Record binds exact producer Attempt/generations to Content, Object Revisions and digests.
3. no `declared` Output Record exists without produced bytes; declaration-only state remains an Output Declaration.
4. paths/tags/coordinates/URLs remain Aliases or Locations.
5. produced bytes become WP03 Objects before Artifact promotion.
6. Artifact Release remains a separate allowlisted authority record.
7. output presence or upload never means release accepted.

### SBOM

1. Package Observation, SBOM Coverage and immutable SBOM Document remain separate.
2. `provenance.sbom` already represents one immutable SBOM document; the overlapping draft `provenance.sbom_revision` token is removed.
3. coverage/skips/unsupported/errors are mandatory evidence.
4. native/SPDX/CycloneDX documents are related Views and may lose information.
5. SBOM does not prove vulnerability status, licence approval, runtime use or release acceptance.

### Attestation, signature and trust

1. Attestation, Signature, Transparency Evidence and their Verification records remain separate.
2. declared versus observed materials/products retain origin.
3. valid signature proves digest/identity binding only under one exact Trust Policy.
4. public transparency requires identity-disclosure acknowledgement.
5. offline/no-log verification remains supported without fabricated log service or entry evidence.
6. trust-policy change produces new Verification records and preserves history.
7. cryptographic validity cannot imply functionality, safety, review, reproduction or release acceptance.

### Proof and reproduction

1. Build execution, integrity, export, SBOM, attestation, signature, functional test, review, reproduction and release remain different proof domains.
2. Proof Bundle is a manifest of distinct records, not a universal verdict.
3. Reproduction Request, Reproduction Run and Comparison remain separate.
4. independent reproduction requires a new Build Run and frozen independence/comparison Protocol.
5. comparison distinguishes byte identity, functional equivalence, accepted variance, non-equivalence, inconclusive and blocked.
6. reproduction results never rewrite the original Build Run.

## Migration closure

The migration record forbids:

- backend/job/path identity replacing Recipe or Run identity;
- detector proposal promoted without authority;
- acceptance state embedded into immutable Recipe Revision;
- stale/multi-candidate readiness used as exact execution authority;
- mixed or fictional local/remote locality evidence;
- stale generations/epoch or mutable alias promoted to exact material;
- retries collapsed into one Attempt;
- cache hit promoted to execution or independent reproduction;
- raw secrets copied into canonical records;
- produced file/tag promoted directly to Artifact Release;
- incomplete SBOM promoted to complete/current truth;
- signed attestation promoted to policy verification;
- valid signature promoted to functional/release acceptance;
- changed trust policy rewriting historical results;
- downstream proof failure deleting valid outputs;
- negative/inconclusive reproduction evidence discarded.

## Conformance closure

The safety net and fixture sets cover:

- proposal/acceptance/readiness/compatibility separation;
- immutable Recipe Revision without embedded acceptance;
- exact Node-local and remote-service execution contexts;
- mixed locality/generation rejection;
- two Plans for one Recipe and backend replacement;
- mutable/volatile input handling;
- Step retry and Attempt identity;
- Build completion with export/SBOM failure;
- cache eligibility and cache-versus-reproduction;
- secret references, verified cleanup and leakage boundaries;
- output registration, required produced bytes, mutable tags and release authority;
- partial SBOM and format conversion;
- attestation origin and policy verification;
- signature correctness/trust/transparency boundaries;
- public disclosure acknowledgement and honest offline/no-log verification;
- proof-bundle domain separation;
- byte-identical and functional reproduction;
- failure isolation.

Structural JSON Schema validation is insufficient. WP13 must enforce typed-reference kinds, cross-record equality, generation/epoch, locality XOR, graph acyclicity/dependencies, mutable-material resolution, cache identity, secret redaction/cleanup, output/digest linkage, coverage, trust-policy semantics and reproduction independence.

## Candidate-completion verdict

**WP07 is candidate-complete for downstream Phase 0B use.**

It does not prove any Build backend, compiler worker, cache service, registry, SBOM generator, attestation/signing system, trust root, transparency service or reproduction runner exists or works.

## Deferred work

- Domain Pack/firmware/disk/Device contracts — WP08;
- Application/Browser/semantic UI/Shell — WP09;
- Knowledge/data/Package/Plugin — WP10;
- isolation/placement/reservation/Lease/secure grants — WP11;
- security/Finding/Claim/Evidence/reproduction extensions — WP12;
- executable harness/golden corpus — WP13/WP14;
- dependency/backend selection — Phase 0C only.

## Acceptance decisions

- `decisions/ADR-0024-RECIPE-BUILD-PROVENANCE-SBOM-SIGNATURE-VERIFICATION-BOUNDARY.md`
- `decisions/ADR-0024A-WP07-FINAL-CATALOG-CONVENTIONS-CORRECTION.md`

## Do-not-build rule

> Candidate-complete contracts authorize downstream schema design only. They do not authorize selecting, installing or deploying BuildKit, Dagger, ORAS, Syft, Witness, in-toto, Sigstore, registry/signing infrastructure, native compiler workers, caches or Build UI.
