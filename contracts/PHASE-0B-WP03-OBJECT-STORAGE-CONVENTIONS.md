# Phase 0B WP03 — Object, Revision, View, Artifact and Storage Conventions

**Status:** CANDIDATE
**Contract family:** `ptah.object` / `ptah.storage`
**Candidate version:** `0.1.0`
**Phase:** 0B-WP03

This record turns ADR-0005, ADR-0006, ADR-0007, ADR-0018 and ADR-0019 into exact contract rules. It does not select a storage backend or authorize implementation.

---

# 1. Canonical identity layers

Ptah preserves four different identity layers:

1. **Content** — byte identity, size and qualified cryptographic digests.
2. **Object** — durable logical/source identity and ownership/provenance context.
3. **Object Revision** — one immutable version of one Object, bound to exact Content or an explicit no-bytes semantic state.
4. **Location** — one physical or logical place where bytes or a representation may exist.

These identities never collapse.

A filename, path, URL, provider key, ETag, tag, MIME type, parser claim or storage backend ID is not canonical Content or Object identity.

## 1.1 Content record

A Content record represents exact bytes and declares:

- canonical algorithm-qualified digest;
- additional qualified digests and hash observations;
- byte size;
- content encoding/wrapper state;
- authorized deduplication scope;
- verification evidence;
- known collision, corruption or ambiguity limitations.

SHA-256 is the initial required interoperability digest. Other digests may coexist. A provider checksum is only a claim until its algorithm, byte scope and verification are known.

## 1.2 Deduplication and privacy

Identical verified bytes may share one Content record only inside an authorized deduplication scope.

Initial scope classes:

- `object_only`;
- `workspace`;
- `organization_trust_domain`;
- `deployment_trust_domain`;
- `public_content`.

Cross-tenant or cross-privacy-domain equality must not be exposed merely because digests match. Deduplication is a storage optimization, not an authorization grant.

## 1.3 Object

An Object is the stable logical/source identity that retains:

- source/provenance;
- owner/authority and Workspace scope;
- declared names and labels;
- current Revision projection;
- revision lineage;
- privacy, audience, retention and tombstone policy;
- available Views, relationships and Artifact roles.

An Object may receive new immutable Revisions without rewriting earlier Revisions.

## 1.4 Object Revision

An Object Revision is immutable after creation. It declares:

- the owning Object;
- exact Content reference where bytes exist;
- parent Revision references;
- revision role and origin;
- source metadata captured at that revision;
- producing Activity/Operation/Attempt and Receipt references;
- creation reason;
- limitations and verification state.

Correction creates a new Revision or a superseding record. It never edits frozen history.

---

# 2. Hash observations and verification

Hash observations are plural and evidence-bearing.

Each observation records:

- algorithm and algorithm version/profile;
- digest text and byte scope;
- producer identity/version;
- source Location or stream;
- Activity/Operation/Attempt/Receipt correlation;
- observed size;
- outcome and limitations.

A Content record chooses one canonical digest only after the required verification policy passes. Conflicting observations remain visible.

Hash equality does not prove semantic equivalence, safety, authorization, provenance or absence of collision.

---

# 3. Detection and classification

Detection remains plural.

`object.detector_observation` records one detector's claim over one exact Object Revision. It never mutates Object truth.

A separate `object.classification_decision` may select routing or a preferred interpretation for an exact purpose. It records:

- considered observations;
- decision authority and policy revision;
- selected type/route;
- reason and limitations;
- expiry/re-evaluation triggers.

`unknown`, `ambiguous`, `polyglot`, `encrypted`, `malformed`, `truncated`, `unsupported` and `opaque` remain valid outcomes.

---

# 4. Relationship model

A relationship has a stable identity and immutable relationship revisions.

`core.relationship` owns:

- relationship identity;
- current relationship-revision projection;
- Workspace/authority/privacy/retention scope.

`core.relationship_revision` owns:

- exact subject and object references;
- registered relationship type and direction;
- source locator/range/path/page/coordinates where relevant;
- producing Activity/Operation/Attempt/Receipt;
- confidence, coverage and limitations;
- effective, superseded or tombstoned state.

A relationship does not imply ownership, trust, containment completeness or deletion authority beyond its registered semantics.

Multiple relationships may point to the same Content/Object. Overlapping byte regions are valid.

---

# 5. Child Object, View, Preview and Derivative

## 5.1 Child Object

A child Object has independently addressable bytes and its own Object/Revision/Content identity.

Examples include archive entries, embedded executables, extracted tracks, attachments, DEX files and carved byte regions.

The parent relationship records exact source Revision, locator/range/path, extraction machinery and proof.

## 5.2 View

A View is a structured interpretation over exact source Revision(s). It may or may not serialize to independent bytes.

A View records:

- `view_kind` and schema/version;
- exact source Revision references;
- parser/model/grammar/configuration provenance;
- coverage and completeness;
- serialized Object/Revision reference when materialized;
- warnings, disagreement and limitations.

A View cannot replace the source Object or claim original-source status without independent evidence.

## 5.3 Preview

A Preview is a human-oriented View/derivative optimized for display or quick understanding.

It records renderer/decoder version, dimensions/range/duration, environment, output Content/Object, source Revision and limitations.

Renderability under one backend does not prove complete semantic correctness.

## 5.4 Derivative

A Derivative is a new Object Revision or Object produced through an explicit transformation, normalization, edit, conversion, transcode, remux, patch or rebuild.

The original remains immutable. The Derivative records source Revisions, Recipe/Operation, exact settings, output Content, invalidated trust/signature state and comparison evidence.

---

# 6. Progressive decomposition

`object.decomposition_run` summarizes one bounded decomposition Activity over one exact source Revision.

Levels remain:

- `L0_registered`;
- `L1_detected`;
- `L2_inventoried`;
- `L3_decomposed`;
- `L4_enriched`;
- `L5_transformed`;
- `L6_rebuilt`;
- `L7_verified`.

Level is a claimed achieved boundary backed by exact outputs and Receipts, not a generic status ladder.

A run records:

- requested and achieved levels;
- complete, partial, unsupported, locked, failed, cancelled or budget-exhausted outcome;
- byte/entry/page/region/stream coverage;
- budgets requested/used;
- children, Views, Derivatives and unknown gaps;
- warnings, skipped scope and limitations.

Partial valid outputs remain registered. Higher levels are never inferred from process exit alone.

---

# 7. Artifact and Artifact Release

## 7.1 Artifact

An Artifact is a durable promoted-result role over exact Object Revision(s). Promotion does not copy or replace Object identity.

An Artifact records:

- purpose/type and version;
- subject/source Object Revision references;
- promoted Object Revision references;
- producing Activity/Operation/Attempt;
- required Receipt/proof references;
- verification, review and acceptance projections;
- retention, visibility and release eligibility;
- provenance/SBOM/signature/reproduction references where applicable.

`completed`, `verified`, `reviewed`, `accepted` and `released` remain separate facts.

## 7.2 Artifact Release

An Artifact Release is an immutable publication/export manifest over exact Artifact and Object Revision references.

It records:

- release action (`publish`, `withdraw`, `revoke`, `supersede`);
- exact manifest digest;
- audience/privacy/redaction decision;
- included and excluded records;
- public-safe provenance/evidence subset;
- signing/attestation references;
- release authority and policy revision;
- predecessor/supersession relationship.

Withdrawal or revocation creates a new immutable Release record. It does not rewrite the published manifest.

A public Release must never include restricted source bytes, private consumer identity, raw credentials or restricted evidence merely because the underlying Artifact can access them.

---

# 8. Storage Location and replica truth

A Storage Location is one backend-specific physical/logical location for exact Content or materialized representation.

It records:

- Location identity and kind;
- Content/Object Revision reference;
- backend/provider/connection reference;
- provider key/path/version/ETag as aliases only;
- stored size and provider digest claims;
- encryption/wrapper reference;
- replica role;
- lifecycle, health and verification projections;
- last observation and verification Receipts.

The three dimensions remain separate:

1. **Location lifecycle:** declared, materializing, available, retiring, deleted.
2. **Location health:** unknown, healthy, degraded, missing, corrupt.
3. **Location verification:** unverified, verifying, verified, failed, stale.

Metadata cannot claim availability or verification without evidence.

A missing/corrupt Location remains a durable record. Repair creates new Receipts and may materialize a new or repaired Location from a verified source.

---

# 9. Retention, tombstone and physical deletion

Tombstoning a logical Object/Artifact is different from deleting a Location or deleting shared Content bytes.

Physical deletion requires an explicit `storage.deletion_decision` with:

- target Content/Location;
- reference and retention analysis;
- legal hold and policy checks;
- reachable Object Revision/Artifact/Release/Backup references;
- deletion scope;
- authority;
- dry-run/result Receipts;
- blocked reasons and repair/restore consequences.

Content bytes must not be physically deleted while any retained authorized Object Revision, Artifact Release, backup, legal hold or proof record requires them.

Deleting one replica does not delete the Content identity or other replicas. Synchronization deletion never deletes backup history automatically.

---

# 10. Source, production and proof correlation

Every produced Revision, child, View, Preview, Derivative, Artifact, Release and Location must link as applicable to:

- source Object Revision(s);
- Activity Request/Activity;
- Operation and Attempt;
- exact nonce/generations/connection epoch through WP02 Receipt;
- Facility/Provider/Node and version;
- Recipe/Protocol/configuration/model/grammar;
- content hashes;
- coverage, warnings and limitations.

Events and telemetry may notify or observe. Proof-critical creation, verification, repair, release and deletion require Receipts.

---

# 11. Migration and compatibility

Migrations preserve:

- Object and Content identity;
- immutable Revision history;
- relationship history;
- Artifact Release manifests;
- Location observations and verification history;
- tombstones and deletion decisions;
- privacy/audience/redaction/retention.

A migration may create replacement projections or normalized hash observations. It must not recompute or claim a digest without evidence, silently merge distinct Objects, expose cross-scope deduplication, or flatten conflicting detector observations.

Compatibility is directional and tested against saved Objects, Revisions, relationships, Artifact Releases and missing/corrupt Location states.

---

# 12. Do-not-break rules

1. Never use filename, path, URL, ETag, tag or provider ID as Content/Object identity.
2. Never overwrite an immutable Object Revision.
3. Never let a detector or parser claim erase competing observations.
4. Never let a View, Preview, Derivative or Artifact replace the original.
5. Never claim complete decomposition without explicit coverage.
6. Never promote transport completion into verified Content availability.
7. Never call an Artifact released or accepted from Activity completion alone.
8. Never physically delete shared bytes without reference/retention analysis and Receipts.
9. Never expose digest equality across unauthorized privacy domains.
10. Never allow a backend replacement to change canonical Object, Revision, Artifact or relationship identity.
