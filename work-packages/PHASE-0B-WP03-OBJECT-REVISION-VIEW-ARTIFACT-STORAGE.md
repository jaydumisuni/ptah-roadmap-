# Phase 0B WP03 — Object, Revision, View, Artifact and Storage Relationships

**Status:** CANDIDATE COMPLETE
**Date:** 2026-07-19
**Contract families:** `ptah.object` / `ptah.storage` `0.1.0`
**Implementation authorization:** NONE

---

# 1. Purpose

WP03 turns ADR-0005, ADR-0006, ADR-0007, WP01 and WP02 into exact candidate contracts for content identity, logical Objects, immutable Revisions, detector evidence, relationship history, Views/Previews/Derivatives, progressive decomposition, Artifact promotion/publication and storage replica truth.

No backend, parser, CAS, database, cloud provider, transfer engine or runtime dependency is selected by this package.

---

# 2. Normative records

- `contracts/PHASE-0B-WP03-OBJECT-STORAGE-CONVENTIONS.md`
- `contracts/PHASE-0B-WP03-ENTITY-KIND-SUPPLEMENT.md`
- `contracts/PHASE-0B-WP03-RELATIONSHIP-TYPE-REGISTRY.md`
- `migrations/phase-0b/WP03-OBJECT-STORAGE-MIGRATION-COMPATIBILITY.md`

---

# 3. Candidate schema catalog

Catalog:

- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`

Active schemas:

1. `object.definitions` `0.1.0`;
2. `object.content` `0.1.0`;
3. `object.hash-observation` `0.1.0`;
4. `object.object` `0.1.0`;
5. `object.revision` `0.1.0`;
6. `object.detector-observation` `0.1.0`;
7. `object.classification-decision` `0.1.0`;
8. `core.relationship` `0.1.0`;
9. `core.relationship-revision` `0.1.0`;
10. `object.view` `0.1.0`;
11. `object.preview` `0.1.0`;
12. `object.derivative` `0.1.0`;
13. `object.decomposition-run` `0.1.0`;
14. `object.artifact` `0.1.0`;
15. `object.artifact-release` `0.1.0`;
16. `storage.location` `0.1.0`;
17. `storage.location-observation` `0.1.0`;
18. `storage.verification` `0.1.0`;
19. `storage.repair` `0.1.0`;
20. `storage.deletion-decision` `0.1.0`.

Dependencies:

- `ptah.common` catalog `0.1.0`;
- `ptah.activity` catalog `0.1.1`.

---

# 4. Accepted contract boundaries

## 4.1 Content, Object and Revision

1. Content is exact byte identity and qualified digest evidence.
2. Object is durable logical/source identity with authority, provenance, labels and revision lineage.
3. Object Revision is one immutable version of one Object.
4. Location is one backend-specific materialization and never canonical content identity.
5. filenames, paths, URLs, ETags, provider IDs, tags and parser claims remain aliases/metadata/evidence.
6. identical bytes may share Content only inside an authorized deduplication scope.
7. distinct logical Objects never merge solely because bytes match.

## 4.2 Hash and detector evidence

1. Hash observations are plural and retain producer, algorithm/profile, byte scope, size and Receipts.
2. SHA-256 is the initial interoperability baseline; algorithm-specific semantic validation remains required.
3. detector observations remain plural and conflicting claims are retained.
4. route/type selection is an independent Classification Decision with authority/policy/reason.
5. unknown, ambiguous, polyglot, encrypted, malformed, truncated, unsupported and opaque remain valid outcomes.

## 4.3 Relationship graph

1. Relationship identity and immutable Relationship Revisions are separate.
2. endpoint/type/locator/coverage changes create a new Revision.
3. overlapping regions and multiple relationships are valid.
4. containment does not imply complete coverage.
5. relationship direction does not imply ownership, trust or deletion authority.

## 4.4 Views, Previews, Derivatives and decomposition

1. child Objects have independently addressable bytes.
2. Views are structured interpretations over exact source Revisions and may be virtual or serialized.
3. Previews are human-oriented derived representations and do not replace originals.
4. Derivatives produce new Object Revisions/Objects with explicit source and transformation lineage.
5. Decomposition Runs retain requested/achieved levels, outcome, budgets, coverage, unknown gaps and partial outputs.
6. complete outcome requires complete bounded coverage; partial/error/budget/cancel outcomes cannot claim complete coverage.
7. decompiled/generated/decoded output cannot be labeled original source without independent evidence.

## 4.5 Artifact and Release

1. Artifact is a durable promoted-result role over exact Object Revisions.
2. promotion does not imply verification, review, acceptance or release.
3. Artifact Release is an immutable allowlisted publication/export manifest.
4. withdrawal/revocation/supersession creates a new Release record.
5. public release requires public privacy/audience compatibility and a public-safe evidence/provenance subset.

## 4.6 Storage truth

1. Location lifecycle, health and verification are separate dimensions.
2. availability does not imply verification.
3. provider checksum/ETag is a claim until algorithm and byte scope are known.
4. missing/corrupt Locations remain records and may be repaired from verified sources.
5. repair requires pre/post verification and WP02 production correlation.
6. backend replacement creates new Locations without changing Content/Object/Revision/Artifact identities.

## 4.7 Tombstone and deletion

1. logical tombstone is separate from Location deletion and shared Content-byte deletion.
2. physical deletion requires an immutable Storage Deletion Decision.
3. retained Object Revisions, Artifacts, Releases, backups, proof, legal holds and retention can block deletion.
4. authorization requires a dry-run Receipt and no blockers/legal holds.
5. execution requires Receipts and post-delete observation.
6. synchronization deletion never erases backup history automatically.

---

# 5. State machines

Candidate state machines:

- `object.lifecycle` `0.1.0`;
- `relationship.lifecycle` `0.1.0`;
- `artifact.lifecycle` `0.1.0`;
- `storage.location.lifecycle` `0.1.0`;
- `storage.deletion_decision.lifecycle` `0.1.0`.

Location health and verification remain independent observation/projection dimensions rather than lifecycle states.

The common state-machine registry review corrected storage authority classes to `provider`/`external_provider` before candidate acceptance.

---

# 6. Safety net and fixtures

- `conformance/PHASE-0B-WP03-OBJECT-ARTIFACT-STORAGE-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp03/object-artifact-storage-cases.v0.1.0.json`

The consolidated safety net includes structural and cross-record cases for:

- authorized deduplication with separate provenance;
- immutable Object/Relationship Revision history;
- path/provider alias rejection;
- hash/detector disagreement;
- overlapping relationships;
- View/Preview/original separation;
- partial decomposition honesty;
- Artifact promotion/proof separation;
- public-release leakage rejection;
- available-but-unverified Locations;
- missing/corrupt replica repair;
- shared Content deletion blocking;
- backend replacement;
- migration without silent Object merge or privacy leakage.

Executable harness implementation remains deferred to WP13/WP14.

---

# 7. Review findings resolved during WP03

1. WP02 canonical kinds are `core.activity`, `core.operation`, `core.attempt`; an initial supplement wording error was corrected before acceptance.
2. storage state-machine authority tokens were normalized to the WP01 common registry.
3. deletion failure reporting was corrected to non-side-effecting transition semantics; the destructive effect belongs to the execution Attempt/Receipt.
4. Location availability, health and verification were separated instead of reusing ADR-0006's earlier combined state list.
5. Object/content language was normalized: logical Object identity and byte Content identity are separate while immutable Revisions bind them.

---

# 8. Deferred executable/implementation decisions

Still deferred:

- exact digest library/algorithm package and multihash encoding;
- database schema/index implementation;
- local CAS directory layout implementation;
- S3/R2/OCI/Drive adapters;
- parser/Domain Pack selection;
- garbage collector implementation;
- cross-tenant deduplication policy implementation;
- executable JSON Schema and graph-conformance harness;
- performance/scale proof;
- public repository schema publication;
- runtime code.

These are WP13/WP14, Phase 0C or implementation-phase decisions.

---

# 9. Candidate completion conclusion

WP03 is complete for downstream Phase 0B candidate contract use.

It is not implementation-frozen, proven or authorized for build. Its schemas and invariants may be consumed by WP04 onward and must later pass executable cross-contract conformance, migration and golden/negative corpus proof.
