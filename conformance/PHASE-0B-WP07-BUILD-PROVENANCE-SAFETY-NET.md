# Phase 0B WP07 — Recipe, Build and Provenance Safety Net

**Status:** CANDIDATE SPECIFICATION  
**Date:** 2026-07-19  
**Executable harness:** DEFERRED TO WP13  
**Fixture suite:** `conformance/fixtures/phase-0b/wp07/build-provenance-cases.v0.1.0.json`  
**Authoritative catalog:** `schemas/phase-0b/build/schema-catalog.v0.1.1.json`

## Purpose

Define structural, cross-record, temporal, identity, generation, privacy, trust and proof invariants that every WP07 implementation, migration and backend adapter must satisfy.

## A. Recipe identity and authority

1. Build Recipe, immutable Recipe Revision, Proposal, Acceptance, Readiness, Backend Compatibility, Compiled Plan and Build Run remain distinct.
2. Dockerfile, CI workflow, path, module/function, backend graph and job IDs are source Objects or Aliases, never canonical Recipe/Run identity.
3. execution requires one exact accepted Recipe Revision.
4. detector/importer confidence cannot become Acceptance.
5. `accepted_with_conditions` requires explicit condition records.
6. changes after execution begins create a new Recipe Revision.
7. Recipe lifecycle never substitutes for Revision acceptance/readiness.

## B. Readiness and backend compatibility

1. Readiness binds exact Recipe/Workspace/material/capability/Provider/Node/policy evidence and expires.
2. stale inputs, snapshots, policy or generations invalidate dispatch.
3. Backend Compatibility is directional and target-specific.
4. unsupported, converted, weakened or reduced-scope semantics remain explicit.
5. required semantics cannot be silently weakened.
6. Compiled Plan cannot mutate Recipe Revision.
7. different backends create different Plans while preserving Recipe identity.

## C. Build Run, Step, Operation and Attempt

1. Run binds exact Recipe Revision, Acceptance, Readiness, Plan, Workspace Materialization and Provider generation.
2. local Run requires exact Node generation/connection epoch; remote Run uses approved remote-service identity without fabricated Node fields.
3. Recipe step definition (`step_key`), run-scoped Build Step, logical Operation and physical Attempt remain distinct.
4. retries preserve Operation identity and create new Attempts/nonces.
5. stale-generation Receipts/outputs cannot prove current Run.
6. required Step failure prevents `build_completed`.
7. `build_completed` covers Build execution only.
8. uncertain non-idempotent effects are reconciled before retry.

## D. Materials and volatile inputs

1. mutable branch/tag/range/URL/path resolves to exact immutable evidence or remains explicitly mutable/unresolved.
2. material class and observation time are mandatory.
3. secret references remain a distinct material class.
4. declared and observed materials remain distinguishable.
5. output-affecting volatile inputs lower reproducibility unless independently validated.
6. no migration invents missing digests/revisions.

## E. Cache

1. Cache Record binds exact producer Recipe, Plan, Run, Step, Operation, Attempt, inputs, toolchain/environment and output digests.
2. Cache Use is a separate consumer-specific decision.
3. input/toolchain/platform/policy/visibility mismatch rejects or stales reuse.
4. cache hit is not executed work, fresh proof or independent reproduction.
5. unknown-producer legacy cache is reference-only, stale or quarantined.
6. cache eviction removes reusable bytes only, never canonical provenance.

## F. Credentials and secret access

1. raw values are prohibited from Recipe, Plan, fixtures, logs, cache metadata, SBOM, attestation, telemetry and public outputs.
2. Secret Access binds exact credential reference, trust domain, Run/Step/Operation/Attempt, scope, delivery method and expiry.
3. a Provider secret mount does not prove non-leakage.
4. revocation/cleanup and required leak scans are separate evidence.
5. cleanup failure remains a restricted security result.
6. secret-dependent outputs/cache/reproduction restrictions remain explicit.

## G. Outputs, Objects and Releases

1. Output Declaration and Build Output Record remain separate.
2. Output Record requires exact producer Attempt/generations and produced Content/Object Revision/digests.
3. no `declared` Output Record exists without produced bytes; declarations remain `build.output_declaration`.
4. paths, filenames, tags, package coordinates and URLs are Aliases/Locations.
5. produced bytes become WP03 Content/Object Revisions before Artifact promotion.
6. Artifact promotion and Artifact Release are separate decisions.
7. failed export/proof/signing retains valid local outputs and honest partial state.
8. cleanup does not delete canonical evidence without WP03/WP06 authority.

## H. SBOM and package observations

1. every package observation binds exact subject, generator revision, evidence location and confidence.
2. SBOM binds exact subject digest, generator/configuration, native report and Coverage.
3. coverage retains requested/scanned/skipped/unsupported/error scope.
4. partial coverage cannot claim complete inventory.
5. zero packages/no findings cannot imply empty or safe software.
6. native/SPDX/CycloneDX documents are related Views; lossless conversion requires comparison evidence.
7. SBOM inventory does not imply vulnerability, licence approval, runtime use or release acceptance.

## I. Attestation

1. Attestation statement, Signature and Attestation Verification remain separate.
2. statement bytes, predicate/version, subjects, materials/products and producer are exact.
3. declared and observed materials/products retain origin.
4. creation/signing cannot imply predicate/layout/policy PASS.
5. verification binds exact parser/verifier, trust policy, Protocol/Layout and requirement results.
6. negative/incomplete verification remains immutable.

## J. Signature, trust and transparency

1. Signature binds exact subject digest and signer/key/certificate/issuer evidence.
2. Signature Verification is a new record under one exact Trust Policy/root/version.
3. cryptographic validity proves digest/identity binding only.
4. functionality, safety, review, reproduction and release acceptance remain separate.
5. public transparency requires explicit identity-disclosure acknowledgement.
6. offline/no-log verification does not fabricate log service/entry evidence.
7. trust-policy change creates new Verification records; old results remain historical.
8. revocation applies prospectively/currently under policy without rewriting prior observations.

## K. Proof bundles and verification domains

1. Build execution, output integrity, export availability, SBOM, attestation, signature, functional test, review, reproduction and release are separate proof domains.
2. Proof Bundle is a manifest, not a universal verdict.
3. every bundle entry retains domain, authority class and limitations.
4. producer statement, tool verification, independent review, external authoritative result and caller acceptance remain distinct.
5. absence/failure in one domain cannot be hidden by success in another.

## L. Independent reproduction

1. Reproduction Request, Reproduction Run and Comparison remain separate.
2. accepted Request fixes Recipe, original Run, Protocol, independence and cache policy.
3. Reproduction Run uses new Build Run, Activities, Operations, Attempts and outputs.
4. independence evidence satisfies the frozen Protocol; same-output reference or same-backend cache is insufficient.
5. comparison distinguishes byte identity, functional equivalence, accepted variance, non-equivalence, inconclusive and blocked.
6. all differences/nondeterminism remain evidence.
7. failed/inconclusive reproduction does not rewrite original Build state.

## M. Privacy and publication

1. source, package inventories, signer identities, credentials and private provenance obey audience/redaction policy.
2. transparency identity disclosure is explicit and durable.
3. public Proof Bundle/Artifact Release is allowlisted rather than a database dump.
4. private/offline signing remains supported where policy permits.
5. raw sensitive build/security data is restricted by default.

## N. Backend replacement

1. Recipe, Object, Artifact and proof identities survive Build/export/SBOM/attestation/signing backend replacement.
2. replacement creates new Facility/Provider/adapter revisions, Plans, Runs and Receipts.
3. incompatible cache entries are invalidated or reverified.
4. changed semantics require Backend Compatibility evidence.
5. old Plans/Runs/reports/signatures/verifications remain immutable.
6. backend equivalence is a tested Claim, not inferred from a common interface.

## O. Property-based invariants for WP13

- every accepted Run references one accepted Recipe Revision and non-stale Readiness;
- every Build Step belongs to one Run and maps at least one Operation;
- every physical retry has a unique Attempt ID/nonce;
- `build_completed` implies all required Step records completed and required Output Records exist;
- every Output Record has non-empty Content, Object Revision and digest references;
- no raw credential value exists in ordinary/public schemas/fixtures;
- accepted Cache Use has all mandatory identity comparisons satisfied;
- complete SBOM coverage has no required skipped/unsupported/error scope;
- valid Signature Verification subject digest equals Signature subject digest;
- Attestation Verification subject/material/product checks match exact statement;
- public-log Transparency Evidence has disclosure acknowledgement;
- offline/no-log evidence has no fabricated log entry/service;
- Reproduction Comparison subjects belong to original/reproduction Runs;
- byte-identical class requires matching exact digest sets;
- release acceptance cannot be inferred from Build/signature lifecycle.

## Exit condition

WP07 is candidate-complete only when:

1. all 30 active schemas resolve through catalog `0.1.1`;
2. nine lifecycle machines use registered identities/proof vocabulary;
3. entity-kind correction `0.1.1` removes overlapping Step/SBOM identities;
4. fixtures cover mandatory positive/negative cases;
5. migration preserves history, privacy and negative evidence;
6. work package and ADR reference this safety net;
7. implementation and dependency selection remain blocked until Phase 0C.
