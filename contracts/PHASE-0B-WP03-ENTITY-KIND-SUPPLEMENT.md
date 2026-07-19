# Phase 0B WP03 — Entity Kind Supplement

**Status:** CANDIDATE
**Registry:** `ptah.common.entity-kind`
**Supplement version:** `0.1.0`

The following entity kinds extend the Phase 0B common registry for WP03.

| Entity kind | Canonical role | Mutability rule |
|---|---|---|
| `object.content` | exact byte identity and authorized deduplication scope | append-only observations; canonical digest correction creates superseding record |
| `object.hash_observation` | one producer's qualified digest observation | immutable |
| `object.object` | durable logical/source Object identity | mutable projection through record revisions; history preserved |
| `object.revision` | one immutable version of one Object | immutable; corrections supersede |
| `object.detector_observation` | one detector claim over an exact Object Revision | immutable |
| `object.classification_decision` | selected route/type for a purpose and policy revision | immutable decision; replacement supersedes |
| `core.relationship` | stable relationship identity | mutable current-revision projection |
| `core.relationship_revision` | exact subject/object/type/locator/provenance relationship revision | immutable |
| `object.view` | structured interpretation over exact source Revision(s) | immutable output record |
| `object.preview` | human-oriented View/derived representation | immutable output record |
| `object.derivative` | transformation lineage from source Revision(s) to output Object/Revision | immutable |
| `object.decomposition_run` | bounded decomposition result summary for an Activity | immutable result record; later continuation creates another run |
| `object.artifact` | durable promoted-result role over exact Object Revision(s) | mutable projection; promotion/review/acceptance history remains separate |
| `object.artifact_release` | immutable publication/export/revocation manifest | immutable |
| `storage.location` | one backend-specific materialization/replica/location | mutable lifecycle/health/verification projections with retained observations |
| `storage.location_observation` | one observed availability/health/provider state | immutable |
| `storage.verification` | one verification check over exact Content and Location | immutable |
| `storage.repair` | one repair/copy/reconstruction record | immutable result linked to Activity/Receipts |
| `storage.deletion_decision` | reference/retention analysis and authorized physical-deletion decision | immutable decision; execution produces Receipts |

## Required typed references

Canonical schemas must reject a reference whose `entity_kind` does not match the field's declared family or exact kind.

Examples:

- `object_ref` requires `object.object`;
- `revision_ref` requires `object.revision`;
- `content_ref` requires `object.content`;
- `location_ref` requires `storage.location`;
- `artifact_ref` requires `object.artifact`;
- `release_ref` requires `object.artifact_release`;
- production correlation uses WP02 kinds such as `activity.activity`, `activity.operation`, `activity.attempt` and `proof.receipt`.

Structural JSON Schema cannot enforce every cross-document kind constraint by itself. The WP13 executable harness must enforce them through the entity-kind registry and schema catalog.

## Identity prohibitions

The following remain aliases, claims or metadata and cannot become canonical entity IDs:

- filename or extension;
- local path or cloud object key;
- URL;
- ETag, provider generation or object version;
- OCI tag;
- Git ref;
- MIME/type detector claim;
- parser-local child/view ID;
- backend CAS path;
- transfer/download engine ID.
