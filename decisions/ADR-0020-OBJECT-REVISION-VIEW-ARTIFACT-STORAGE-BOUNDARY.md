# ADR-0020 — Object, Revision, View, Artifact and Storage Boundary

**Status:** ACCEPTED FOR PHASE 0B CANDIDATE CONTRACT USE
**Date:** 2026-07-19
**Contract candidates:** `ptah.object` / `ptah.storage` `0.1.0`
**Implementation authorization:** NONE

---

## Context

Phase 0A established immutable originals, plural detector claims, progressive decomposition, explicit derivatives, promoted Artifacts, backend-neutral storage Locations and retention-aware deletion. WP01 added canonical identities/versioning; WP02 added exact Activity/Operation/Attempt/Receipt correlation.

Phase 0B must prevent several recurring false equivalences:

- path/tag/provider key equals Object identity;
- Object identity equals byte identity;
- transfer completion equals verified availability;
- parser success equals universal type truth;
- View/Preview/Derivative equals original;
- Activity completion equals Artifact verification/acceptance/release;
- tombstone equals physical deletion;
- one missing replica equals lost Content;
- matching digest authorizes logical-object merge or cross-tenant disclosure.

---

## Decision

Ptah accepts the WP03 candidate contract set and the following boundaries.

### 1. Content, Object and Revision are separate

- `object.content` owns exact byte identity, qualified digest evidence, size and authorized deduplication scope.
- `object.object` owns durable logical/source identity, authority, provenance, labels and revision lineage.
- `object.revision` owns one immutable version of one Object and binds exact Content where bytes exist.
- `storage.location` owns one backend-specific materialization/replica.
- filename, path, URL, ETag, provider key/version, tag and parser-local ID remain aliases/metadata.

Identical verified bytes may share Content only inside an authorized scope. Distinct logical Objects retain separate provenance and never merge solely by digest.

### 2. Hash and detection remain plural evidence

- hash observations retain algorithm/profile, byte scope, producer, size, outcome and Receipts;
- provider checksums are claims until independently normalized/verified;
- detector observations remain independent and disagreements are retained;
- classification/routing is a separate immutable decision with authority, policy, reason and considered observations;
- unknown/ambiguous/polyglot/encrypted/malformed/truncated/unsupported/opaque outcomes are valid.

### 3. Relationships have identity and immutable revisions

- `core.relationship` is stable identity/current projection;
- `core.relationship_revision` owns exact endpoints, type, locator, coverage and provenance;
- endpoint/type/locator changes create new revisions;
- overlapping relationships are valid;
- containment never implies complete coverage, ownership, trust or deletion authority.

### 4. Child, View, Preview and Derivative remain separate

- child Objects have independent bytes and Object/Revision/Content identity;
- Views are bounded structured interpretations over exact source Revisions;
- Previews are human-oriented derived representations;
- Derivatives produce new output Revisions/Objects with exact transformation lineage;
- decompiled/generated/decoded output cannot become original source without independent evidence;
- the immutable original is never overwritten.

### 5. Decomposition is progressive and coverage-bearing

`object.decomposition_run` retains requested/achieved level, outcome, budgets, coverage, unknown gaps, partial outputs, warnings and WP02 production correlation.

A complete outcome requires complete bounded coverage. Cancellation, parser failure, timeout or budget exhaustion may preserve valid partial outputs but cannot claim completeness.

### 6. Artifact promotion and publication remain separate

- `object.artifact` is a durable promoted-result role over exact Object Revisions;
- promotion does not imply verification, review, acceptance, eligibility or release;
- `object.artifact_release` is an immutable allowlisted publication/export/withdrawal/revocation/supersession manifest;
- public release requires public privacy/audience compatibility and public-safe evidence/provenance;
- withdrawal/revocation never rewrites the original release manifest.

### 7. Storage lifecycle, health and verification are separate

A Location has independent:

- lifecycle: declared/materializing/available/retiring/deleted;
- health: unknown/healthy/degraded/missing/corrupt;
- verification: unverified/verifying/verified/failed/stale.

Availability does not imply verification. Missing/corrupt Locations remain evidence and may be repaired from verified sources. Backend replacement creates new Locations without changing Content/Object/Revision/Artifact identity.

### 8. Tombstone, replica deletion and Content-byte deletion are separate

`storage.deletion_decision` must retain reference/retention/legal-hold/replica analysis, blockers, authority, policy, dry-run and execution Receipts.

Physical Content bytes cannot be deleted while retained Object Revisions, Artifacts, Releases, backups, legal holds or proof records require them. Deleting one replica does not delete Content identity or other replicas. Synchronization deletion never automatically deletes backup history.

### 9. Production and proof are WP02-correlated

Produced Revisions, relationships, Views, Previews, Derivatives, decomposition results, Artifacts, Releases, verification, repair and deletion records link to exact Activity/Operation/Attempt and proof-critical Receipts where applicable.

Events and telemetry may notify/observe; they do not replace durable records or Receipts.

### 10. Migration preserves identity, history and privacy

Migration must not:

- rewrite immutable Revisions/releases/observations;
- merge Objects solely by matching bytes;
- fabricate parentage, digest verification, detector consensus or complete coverage;
- expose cross-scope deduplication;
- promote outputs without production evidence;
- mark provider existence as verified;
- authorize shared-byte deletion without analysis.

---

## Candidate records

Normative records:

- `contracts/PHASE-0B-WP03-OBJECT-STORAGE-CONVENTIONS.md`
- `contracts/PHASE-0B-WP03-ENTITY-KIND-SUPPLEMENT.md`
- `contracts/PHASE-0B-WP03-RELATIONSHIP-TYPE-REGISTRY.md`
- `migrations/phase-0b/WP03-OBJECT-STORAGE-MIGRATION-COMPATIBILITY.md`
- `work-packages/PHASE-0B-WP03-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE.md`

Schema catalog:

- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`

Conformance planning:

- `conformance/PHASE-0B-WP03-OBJECT-ARTIFACT-STORAGE-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp03/object-artifact-storage-cases.v0.1.0.json`

State machines:

- Object lifecycle;
- Relationship lifecycle;
- Artifact lifecycle;
- Storage Location lifecycle;
- Storage Deletion Decision lifecycle.

---

## Consequences

### Positive

- byte identity survives backend movement without erasing logical provenance;
- immutable originals/revisions remain trustworthy;
- parser disagreement and partial decomposition remain honest;
- Views/Previews/Derivatives and Artifacts cannot masquerade as originals;
- public release has an explicit leakage boundary;
- replica loss/corruption is repairable without identity change;
- shared-byte garbage collection becomes reference/retention safe;
- later Domain Packs and storage backends can be replaced behind stable contracts.

### Costs

- richer graph and history records;
- explicit reference analysis and deletion decisions;
- more storage for observations, relationships, Receipts and immutable release history;
- executable graph/semantic conformance is required beyond JSON Schema;
- deduplication scope and privacy policy require careful implementation.

---

## Do-not-break rule

> Never collapse byte Content, logical Object, immutable Revision, relationship/View/Derivative, promoted Artifact, released manifest or Storage Location into one record or one backend identifier. Never overwrite original/history, infer proof from availability/process success, or physically delete shared bytes without explicit retained reference, policy and Receipt analysis.

---

## Freeze status

WP03 is candidate-complete for downstream Phase 0B contract design.

It is not implementation-frozen, proven or authorized for build. Executable schema/graph/state/migration conformance and lawful golden/negative corpus proof remain WP13/WP14 and Phase 0B freeze requirements.
