# ADR-0024 — Recipe, Build, Provenance, SBOM, Signature and Verification Boundary

**Status:** ACCEPTED FOR PHASE 0B DOWNSTREAM CONTRACT DESIGN  
**Date:** 2026-07-19  
**Phase:** 0B-WP07  
**Implementation authorization:** NONE

## Context

Ptah must represent project detection, Build intent, backend compilation, execution, outputs, package inventory, attestations, signatures, verification and reproduction without allowing one backend job, cache hit, generated document, cryptographic result or green status to become universal truth.

The frozen architecture established BuildKit/Dagger, ORAS, SBOM, in-toto/Witness, Sigstore and internal Builder patterns as complementary machinery. No donor defines canonical Ptah Recipe, Run, Object, proof or release authority.

## Decision

Ptah owns separate canonical records for:

1. Build Recipe;
2. immutable Recipe Revision;
3. Recipe Proposal;
4. Recipe Acceptance;
5. Build Readiness;
6. Backend Compatibility;
7. Compiled Plan;
8. Build Run;
9. run-scoped Build Step;
10. Output Declaration;
11. Build Output Record;
12. Cache Record and Cache Use;
13. Secret Access;
14. Package Observation;
15. SBOM Coverage and SBOM Document;
16. Trust Policy and Transparency Evidence;
17. Attestation and Attestation Verification;
18. Signature and Signature Verification;
19. Verification Run and Proof Bundle;
20. Reproduction Request, Run and Comparison;
21. Provenance Graph Revision;
22. independent Review/Verdict and release acceptance through existing proof/authority contracts.

Backend/job/graph/cache/registry/scanner/signing/log identifiers, paths, tags and coordinates remain scoped aliases or evidence.

## Recipe and backend boundary

A Recipe is durable intended work, not a Dockerfile, CI workflow, Dagger function, BuildKit graph or one run.

Recipe Revision is immutable. Detectors/importers/callers may propose a revision, but execution requires authorized Acceptance and fresh Readiness.

Backend Compatibility is directional and target-specific. Unsupported, converted, reduced or weakened semantics remain explicit and cannot be silently accepted.

A Compiled Plan is backend-specific and cannot mutate Recipe Revision. Backend replacement creates new Plans/Runs while preserving Recipe identity.

## Execution boundary

Build Run binds exact Recipe Revision, Acceptance, Readiness, Plan, Workspace Materialization, Facility/Provider revision/generation and Activity.

A Recipe step definition is identified by immutable `step_key`; `build.step` is the run-scoped Step projection mapped to WP02 Operations and Attempts. The redundant draft `build.step_run` identity is rejected.

Every physical retry creates a new Attempt/nonce. `build_completed` means required Build steps completed only. It never implies export, SBOM, attestation, signature, verification, review, reproduction or release acceptance.

Non-idempotent uncertain effects require read-back/reconciliation rather than automatic retry.

## Material and cache boundary

Mutable branches, tags, package ranges, URLs and paths resolve to exact immutable evidence or remain explicitly mutable/volatile/unresolved.

Cache Record binds exact producer, inputs, toolchain/environment, policy/platform and output digest. Cache Use is a new consumer-specific decision. A cache hit is not executed work, fresh proof or independent reproduction.

## Secret boundary

Recipes and Plans contain opaque credential references only.

Secret Access binds exact recipient Attempt, scope, delivery method and expiry. Provider secret injection does not prove executed code did not copy the secret. Revocation, cleanup and leak scans remain separate evidence; cleanup failure is explicit.

## Output and Artifact boundary

Output Declaration states expected output. Build Output Record binds exact producer Attempt/generations to produced Content, Object Revisions and digests.

Paths, filenames, tags, registry coordinates and URLs are Aliases/Locations, not output identity.

Produced bytes become WP03 Objects before Artifact promotion. Artifact Release remains a separate allowlisted authority record. Build output existence or upload does not mean release accepted.

## SBOM boundary

Package Observation, SBOM Coverage and immutable SBOM Document remain separate.

`provenance.sbom` is one immutable versioned SBOM document; the redundant draft `provenance.sbom_revision` identity is rejected.

Coverage retains requested/scanned/skipped/unsupported/error scope. SBOM inventory does not prove completeness, vulnerability status, licence approval, runtime use or release acceptance. Native and interoperable formats remain related Views with possible information loss.

## Attestation, signature and trust boundary

Attestation statement, Signature, Transparency Evidence, Attestation Verification and Signature Verification remain separate.

Declared and observed materials/products retain origin.

A valid signature proves subject-digest/identity binding under one exact Trust Policy. It does not prove functionality, safety, review, reproducibility or release acceptance.

Public transparency requires explicit identity-disclosure acknowledgement. Private/offline verification remains valid under policy and never fabricates public-log evidence.

Trust-policy/root changes produce new Verification records; historical positive and negative decisions remain immutable.

## Proof and reproduction boundary

Build execution, output integrity, export availability, SBOM, attestation creation, attestation policy verification, signature verification, functional test, independent review, reproduction and release acceptance are separate proof domains.

Proof Bundle is a manifest preserving domain, authority class and limitations; it is not a universal verdict.

Reproduction requires an accepted Request, new Build Run/Activities/Attempts, frozen independence/cache policy and explicit Comparison. Same-backend cache reuse is not independent reproduction.

Comparison distinguishes byte identity, functional equivalence under protocol, accepted variance, non-equivalence, inconclusive and blocked. Reproduction results never rewrite the original Build.

## Entity-kind correction

Accepted correction `0.1.1` removes:

- `build.step_run`, because `build.step` already represents the separately addressable run-scoped Step while Recipe definitions use `step_key`;
- `provenance.sbom_revision`, because `provenance.sbom` already represents one immutable SBOM document.

It adds/retains `build.backend_compatibility`, `build.output_record` and `provenance.transparency_evidence`.

## Schema and conformance decision

Accepted candidate package:

- 30 active schemas in `schemas/phase-0b/build/schema-catalog.v0.1.1.json`;
- nine namespaced lifecycle machines;
- normative conventions and entity-kind correction;
- migration/compatibility rules;
- positive/negative fixture corpus;
- consolidated safety net.

Catalog `0.1.1` supersedes incomplete catalog `0.1.0` without rewriting it.

Structural JSON Schema validation is insufficient. WP13 must enforce typed references, exact cross-record identity, generation/epoch, Recipe/Step graph constraints, mutable-material resolution, cache identity, secret redaction, output/digest binding, SBOM coverage, trust/transparency semantics and reproduction independence.

## Consequences

### Positive

- detected configuration cannot silently execute;
- backend replacement preserves Recipe and output identity;
- retries/cache/volatile materials remain honest;
- secrets have scoped cleanup evidence;
- outputs survive downstream proof/export failure;
- SBOM, signature and attestation claims remain bounded;
- trust-policy changes do not rewrite history;
- reproduction becomes an independently evidenced result;
- no proof domain can impersonate release acceptance.

### Costs

- more records than one CI/build job table;
- full material resolution, SBOM coverage and verification require extra work/storage;
- trust/transparency/privacy policy must be maintained;
- reproducibility and independent review can be expensive;
- legacy migration frequently remains partial/manual-review.

## Rejected alternatives

- Dockerfile/CI/backend job as canonical Recipe/Run identity;
- detector proposal or stale readiness as execution authority;
- Compiled Plan mutating Recipe;
- cache hit as executed/reproduced work;
- raw secrets in build records;
- path/tag as Artifact identity;
- output/upload as Release acceptance;
- SBOM as complete/vulnerability/licence truth;
- signed attestation as verified attestation;
- valid signature as functional or release proof;
- public transparency without privacy acknowledgement;
- Proof Bundle as one universal status;
- same-backend cached rerun as independent reproduction;
- backend replacement rewriting historical Runs/proof.

## Downstream requirements

WP08 and later packages must preserve:

- Recipe/Revision/Proposal/Acceptance/Readiness/Plan/Run separation;
- Step/Operation/Attempt retry identity;
- exact Material and output Object binding;
- cache and credential evidence boundaries;
- SBOM coverage and package-observation limits;
- attestation/signature creation versus verification;
- trust/transparency privacy policy;
- proof-domain and release-authority separation;
- reproduction independence and immutable comparison;
- WP02 Receipt correlation;
- WP03 Object/Artifact/Release identity;
- WP04 Provider/generation/freshness;
- WP05 Workspace/Materialization boundaries;
- WP06 export/transfer verification.

No Build backend, cache, registry, SBOM generator, signing/attestation infrastructure, trust service, transparency log, reproduction runner or Build UI implementation is authorized by this ADR.

## Related records

- `work-packages/PHASE-0B-WP07-RECIPE-BUILD-PROVENANCE.md`
- `contracts/phase-0b/build/BUILD-RECIPE-PROVENANCE-CONVENTIONS.md`
- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP07-CORRECTION-0.1.1.md`
- `schemas/phase-0b/build/schema-catalog.v0.1.1.json`
- `migrations/phase-0b/WP07-BUILD-PROVENANCE-MIGRATION-COMPATIBILITY.md`
- `conformance/PHASE-0B-WP07-BUILD-PROVENANCE-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp07/build-provenance-cases.v0.1.0.json`
