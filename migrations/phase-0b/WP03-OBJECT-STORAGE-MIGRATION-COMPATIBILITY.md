# Phase 0B WP03 — Object and Storage Migration/Compatibility Plan

**Status:** CANDIDATE
**Source families:** pre-WP03 records, exports and internal donor records
**Target catalog:** `urn:ptah:schema-catalog:object:0.1.0`

This plan defines migration behavior only. Executable migrations are deferred to WP13.

---

# 1. Migration identities

Every migration run must use the common `common.migration-run` contract and retain:

- source schema/catalog identity;
- target schema/catalog identity;
- exact source record digests;
- migration implementation/version;
- defaults, losses, unresolved fields and manual-review items;
- old/new record references;
- Receipts and review result.

Source records remain immutable.

---

# 2. Legacy file/blob records

A legacy record that collapses filename, path, bytes, hash and storage backend must split into:

1. `object.object` for logical/source identity;
2. `object.revision` for the captured immutable version;
3. `object.content` for exact bytes when independently verified;
4. `storage.location` for each local/cloud/provider path;
5. `object.hash_observation` for every retained digest/provider checksum claim.

Rules:

- legacy path/provider IDs become aliases only;
- missing bytes create no verified Content claim;
- provider checksum with unknown byte scope remains an observation, not canonical digest;
- two legacy records are not merged solely because a weak/provider checksum matches;
- identical independently verified bytes may share Content only inside authorized deduplication scope.

---

# 3. Legacy mutable file history

Legacy overwrites become an ordered Object Revision history only when timestamps, snapshots, hashes or source control establish separate versions.

Where ordering/parentage is uncertain:

- create distinct Revisions;
- mark parentage unresolved;
- retain source timestamps as claims;
- do not fabricate a linear chain;
- require manual review before selecting current Revision.

Deleted legacy files create tombstone Revisions only when deletion evidence exists.

---

# 4. Legacy detector/type metadata

Each independent detector/parser/user assertion becomes `object.detector_observation`.

A single legacy `type` field may become:

- caller assertion observation;
- filename/extension hint observation;
- selected `object.classification_decision` only when the original selection authority/reason is known.

Conflicting legacy values remain separate observations.

---

# 5. Legacy child trees and extracted folders

A directory/extraction tree migrates into:

- child Object/Revision/Content records where bytes exist;
- Relationship identities/Revisions for path/range/container membership;
- Views where records are structured interpretations without independent original bytes;
- a Decomposition Run with partial/unknown coverage unless complete scope is proven.

Filesystem layout alone does not prove complete decomposition or parent ownership.

---

# 6. Legacy build/output/artifact records

A legacy output becomes an Artifact only when exact promoted Object Revisions and producing Activity/Operation/Attempt/Receipt evidence can be retained.

Otherwise migrate it as:

- Object/Revision/Content;
- `artifact_candidate=true` extension or limitation;
- no promoted/verified/accepted/released claim.

Legacy release records require immutable manifest reconstruction. Missing included/excluded sets or audience/redaction evidence blocks public-release migration and requires manual review.

---

# 7. Legacy storage locations

For every retained location:

- create distinct `storage.location` identity;
- classify location kind and replica role;
- retain path/key/ETag/version as aliases;
- import last known availability as `storage.location_observation` with source limitations;
- set verification `unverified` unless an exact digest/size check is evidenced;
- retain missing/corrupt/deleted locations rather than dropping history.

A legacy `exists=true` flag never becomes `verified`.

---

# 8. Legacy deletion and retention

Legacy delete flags/timestamps migrate to tombstones or Location observations, not automatic byte-deletion proof.

Physical deletion claims require:

- source evidence;
- exact target Location/Content;
- execution Receipt or bounded imported evidence;
- post-delete observation where available.

Unknown reference/retention state blocks new deletion authorization.

---

# 9. Directional compatibility

## Reader `0.1.0` reading older records

Allowed only through explicit migration/adaptation. Unknown old fields are preserved in extensions or migration evidence.

## Older reader reading `0.1.0`

Not assumed. Export requires a target-version projection with declared information loss.

## `0.1.x` additive evolution

May add optional fields, registered relationship/view kinds or additional observations without changing existing semantics.

## Breaking changes

Require:

- new schema major/minor according to common compatibility policy;
- explicit field/state/relationship mapping;
- corpus migration tests;
- no identity or immutable-history rewrite.

---

# 10. Mandatory migration negatives

Reject or require manual review when migration would:

- use path/tag/ETag as canonical identity;
- rewrite an existing Revision;
- merge logical Objects solely by digest;
- expose cross-scope deduplication;
- flatten detector disagreement;
- label decompiled/generated content original;
- mark partial decomposition complete;
- promote an output to Artifact without production evidence;
- mark a Location verified from provider existence alone;
- authorize shared-byte deletion without reference/retention analysis;
- make a public Release from restricted source/evidence.
