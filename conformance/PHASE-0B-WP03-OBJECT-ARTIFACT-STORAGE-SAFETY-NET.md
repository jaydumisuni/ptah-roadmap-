# Phase 0B WP03 — Object, Artifact and Storage Safety Net

**Status:** CANDIDATE TEST SPECIFICATION
**Contract families:** `ptah.object` / `ptah.storage` `0.1.0`
**Execution:** deferred to 0B-WP13/0B-WP14

This is the one consolidated safety net for WP03. A backend, migration, importer, exporter or implementation does not conform merely because individual JSON documents validate.

---

# 1. Harness layers

The future executable harness must run all layers:

1. JSON syntax and JSON Schema 2020-12 validation through local catalogs;
2. schema-ID/version and entity-kind checks;
3. typed-reference checks against the entity-kind registry;
4. immutable-record/history checks;
5. cross-record graph invariants;
6. state-machine transition checks;
7. privacy/deduplication scope checks;
8. Receipt and production-correlation checks;
9. storage/reference/retention/deletion analysis;
10. migration and backend-replacement tests.

Unknown schemas or kinds are rejected in strict mode or preserved without interpretation in archive/import mode.

---

# 2. Content, Object and Revision cases

## O01 — identical bytes, separate provenance

Create two Objects from two independent sources with byte-identical content.

Required result:

- two distinct `object.object` IDs;
- two distinct original `object.revision` IDs;
- one shared `object.content` only when deduplication scope authorizes sharing;
- separate source/provenance/authority/privacy records;
- no equality leak outside the allowed scope.

## O02 — same logical Object, new immutable Revision

Create a second Revision for one Object.

Required result:

- Object ID remains stable;
- new Revision ID and incremented logical revision number;
- old Revision bytes/metadata remain unchanged;
- current-revision projection advances through a retained record revision/transition;
- parent Revision is explicit.

## O03 — reject path/tag/provider ID as identity

Reject specimens that use filename, local path, cloud key, URL, ETag, OCI tag, Git ref or transfer engine ID as canonical Content/Object/Revision ID.

## O04 — reject in-place Revision mutation

Changing `content_ref`, parent Revisions, revision role, origin, captured metadata or production correlation of an existing Revision must fail. Correction creates a new superseding Revision.

## O05 — digest conflict retention

Retain two Hash Observations that disagree. Do not silently replace the canonical digest. The Content remains disputed/inconclusive until policy-backed verification resolves it.

## O06 — algorithm-specific validation

The harness must verify SHA-256 length/encoding and other algorithm profiles semantically. Generic hexadecimal syntax is insufficient.

---

# 3. Detection and classification cases

## D01 — competing detector observations

Retain extension, magic, parser and model observations independently, including disagreement.

Required result:

- no observation overwrites another;
- confidence is detector-specific unless calibrated;
- selected route is a separate Classification Decision;
- extension-only evidence cannot silently outrank parser-validated evidence.

## D02 — ambiguous/polyglot/opaque outcomes

Accept `ambiguous`, `polyglot`, `encrypted`, `malformed`, `truncated`, `unsupported`, `opaque` and `unknown` without forcing one universal type.

## D03 — classification replacement

A changed policy or new evidence creates a superseding Classification Decision. It does not rewrite prior detector observations or decision history.

---

# 4. Relationship graph cases

## R01 — stable identity, immutable revisions

Changing relationship endpoints, type, direction, locator, coverage or confidence creates a new Relationship Revision.

## R02 — overlapping regions

Allow overlapping `embedded_in`, `carved_from` or `region_of` relationships over the same source Revision. Do not force a non-overlapping tree.

## R03 — deduplicated child bytes, separate relationships

Two parent paths/ranges producing identical child bytes may reference one Content record while retaining separate child Objects or relationship revisions according to source/provenance policy.

## R04 — containment is not completeness

A `contains` relationship without complete coverage cannot imply every member was discovered.

## R05 — relationship deletion isolation

Tombstoning one Relationship must not delete endpoint Objects, Content or other relationships.

---

# 5. View, Preview, Derivative and decomposition cases

## V01 — View cannot replace original

Reject attempts to set a View, Preview, decoded resource, decompiled source, normalized output or rebuilt output as the original Revision without a new Object/Revision and explicit origin.

## V02 — materialized versus virtual View

Allow a View with no serialized Revision. If serialized bytes exist, require an exact `object.revision` reference and production Receipts.

## V03 — Preview limitations

A rendered Preview proves bounded renderability under its recorded backend/settings only. It cannot satisfy semantic correctness, source authenticity, acceptance or release requirements.

## V04 — Derivative lineage

A Derivative must reference exact source Revision(s), output Revision, transformation/Recipe and WP02 production correlation. Rebuild/transform success cannot imply installability or functional equivalence.

## X01 — partial decomposition

A cancelled, timed-out, parser-error or budget-exhausted run may retain verified children/Views but must have `complete_claim=false`, skipped scope and limitations.

## X02 — complete decomposition

A `complete` outcome requires complete coverage under a declared bounded scope. Unknown gaps must be empty or explicitly outside the scope.

## X03 — crash/restart deduplication

Restarting a decomposition Activity must not duplicate already verified child Content/Object/relationship records. New Attempts and Receipts remain distinct.

## X04 — traversal and unsafe extraction

Reject/quarantine absolute paths, traversal, drive prefixes, unsafe symlink/hardlink targets, special files and path collisions. No extraction writes outside approved Workspace/storage roots.

---

# 6. Artifact and Release cases

## A01 — promotion without false verification

A valid Artifact may be `promoted` while verification, review and acceptance remain pending/not requested. These projections must not be inferred from lifecycle state.

## A02 — promotion requires exact production evidence

Reject Artifact promotion lacking exact Object Revisions, Activity/Operation/Attempt correlation and promotion Receipts.

## A03 — immutable public Release

A Release manifest binds exact Artifact/Object Revisions, digest, audience, redaction, release authority/policy and Receipt references.

## A04 — public leakage rejection

Reject public Release manifests that include restricted/private source bytes, private consumer identity, raw credentials, restricted evidence, unredacted internal paths or non-public provenance.

## A05 — withdraw/revoke history

Withdrawal, revocation and supersession create new immutable Release records referencing the previous Release. The original release manifest remains retained.

## A06 — release is not acceptance

A release action cannot fabricate review, verification, external authority or caller acceptance.

---

# 7. Location, verification and repair cases

## S01 — availability is not verification

Accept a Location with lifecycle `available`, health `healthy`, verification `unverified`. Do not infer verified Content readiness.

## S02 — verified then stale

After the verification freshness policy expires or provider representation changes, retain the old Storage Verification and set the Location verification projection to `stale` until a new check.

## S03 — missing/corrupt replica

Retain a missing/corrupt Location and observations. Content/Object identity remains valid when another verified Location exists.

## S04 — repair from verified source

Repair requires at least one verified source Location, exact Content, target Location, Activity/Operation/Attempt/Receipts and post-repair verification before claiming `repaired_and_verified`.

## S05 — provider checksum limitation

A provider ETag/checksum is a claim unless algorithm and byte scope are known. Multipart/wrapped/encrypted representations cannot silently satisfy raw-Content digest verification.

## S06 — backend replacement

Move the same Content among local CAS, S3/R2, OCI and export locations without changing Content/Object/Revision/Artifact identities.

---

# 8. Retention and deletion cases

## G01 — shared Content blocks byte deletion

If any retained Object Revision, Artifact, Release, backup, legal hold or proof record requires Content, physical Content deletion must be blocked.

## G02 — replica-only deletion

Deletion of one Location may proceed when policy allows and sufficient required replicas remain. Content identity and other Locations remain.

## G03 — authorized deletion requires dry run

Reject `authorized` Storage Deletion Decision with blockers, legal holds, unsatisfied retention or no dry-run Receipt.

## G04 — executed deletion requires read-back

Reject `executed` decision without execution Receipt and post-delete Location observation.

## G05 — synchronization is not backup deletion authority

A sync tombstone or provider delete event cannot delete backup history or other replicas without a separate Storage Deletion Decision.

## G06 — tombstone is not physical deletion

Tombstoning an Object/Artifact/relationship does not imply Content or Location deletion.

---

# 9. Migration and compatibility cases

## M01 — preserve immutable history

Migrate old records into new schemas without changing Content/Object/Revision IDs, prior relationships, Releases, Receipts, privacy or retention.

## M02 — no silent Object merge

A migration may share verified Content but must not merge distinct logical Objects solely because bytes match.

## M03 — no cross-scope deduplication leak

Changing deduplication scope requires explicit authority/policy and must not expose equality to unauthorized readers.

## M04 — missing/corrupt states survive export/import

Location lifecycle, health, verification, observations, repair history and deletion decisions must round-trip.

## M05 — unknown relationship/view kind

Strict readers reject unknown required semantics. Archive readers preserve the record without pretending to understand it.

---

# 10. Completion gate

WP03 may be called candidate-complete only when:

- all active schemas are catalogued;
- entity/relationship registries are committed;
- mutable lifecycles are versioned;
- positive and negative fixture scenarios are committed;
- every required Phase 0A proof boundary maps to a WP03 contract/invariant;
- known structural-versus-semantic validation limits are explicit;
- implementation and backend selection remain blocked.

Executable proof remains deferred to WP13/WP14 and Phase 0B freeze.
