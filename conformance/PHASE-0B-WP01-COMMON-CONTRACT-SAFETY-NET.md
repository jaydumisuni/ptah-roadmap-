# Phase 0B WP01 — Common Contract Safety Net

**Suite ID:** `ptah.conformance.common.0.1.0`  
**Status:** CANDIDATE TEST SPECIFICATION  
**Date:** 2026-07-18  
**Runtime harness:** NOT IMPLEMENTED

## Purpose

Define one consolidated safety-net suite for common identity, versioning, typed-family, state-machine, migration, privacy and deletion behavior.

A later Phase 0B conformance harness must run this suite against every schema implementation and every Provider/Facility adapter that creates canonical records.

A test passes only when the expected valid/invalid result and exact stable error class are produced. Merely parsing JSON is insufficient.

---

# A. Schema loading and resolution

| ID | Case | Expected |
|---|---|---|
| A01 | Load the common schema catalog with all four candidate URNs available locally | PASS |
| A02 | Resolve an absolute `$ref` to `urn:ptah:schema:common:definitions:0.1.0` without network access | PASS |
| A03 | Reference an unknown Ptah schema URN | `invalid_contract` / unknown schema; preserve raw input without interpretation only when policy permits |
| A04 | Mutate bytes under an already frozen schema ID | FAIL; hash/catalog conflict |
| A05 | Catalog maps the same schema ID to two differing byte sets | FAIL; ambiguous schema identity |
| A06 | Schema declares malformed SemVer | FAIL validation |
| A07 | Schema ID version and declared `x-ptah-schema-version` disagree | FAIL semantic conformance |
| A08 | Candidate schema is presented as frozen without freeze decision/evidence | FAIL maturity conformance |

# B. Canonical identity

| ID | Case | Expected |
|---|---|---|
| B01 | Generate lowercase RFC 9562 UUIDv7 entity ID | PASS |
| B02 | Submit UUIDv4 where candidate schema requires new canonical UUIDv7 | FAIL validation |
| B03 | Submit uppercase canonical UUID text | FAIL normalization/validation |
| B04 | Submit malformed or nil/all-zero ID | FAIL validation |
| B05 | Use backend process/container/browser ID as canonical entity ID | FAIL semantic conformance |
| B06 | Import legacy ID as Alias while assigning new canonical ID | PASS |
| B07 | Infer `created_at` solely from UUIDv7 timestamp bits | FAIL proof rule; timestamp is hint only |
| B08 | Create public remapped handle while retaining restricted canonical lineage | PASS |
| B09 | Public remapping exposes the internal canonical ID in an extension | FAIL privacy conformance |
| B10 | Same UUID appears under two different registered entity kinds | FAIL identity-integrity check unless explicit migration evidence proves a historical error |

# C. Entity kind and registry

| ID | Case | Expected |
|---|---|---|
| C01 | Registered lowercase token `core.activity` | PASS |
| C02 | Uppercase or whitespace-bearing token | FAIL validation |
| C03 | Unknown token in strict write mode | FAIL `invalid_contract` |
| C04 | Unknown token in archival preservation mode | Preserve opaque record; do not execute or reinterpret |
| C05 | Reuse frozen token for changed semantics | FAIL registry review |
| C06 | Add token without state/authority/privacy mapping | FAIL registry review |
| C07 | Use `identity.principal` with email address as canonical ID | FAIL; email must be Alias |
| C08 | Merge Principals because two providers report similar display names | FAIL identity proof |

# D. Entity envelope

| ID | Case | Expected |
|---|---|---|
| D01 | Workspace-scoped entity with all required fields | PASS |
| D02 | Global-scoped entity with all required fields | PASS |
| D03 | Both `workspace_ref` and `global_scope` supplied | FAIL validation |
| D04 | Neither scope supplied | FAIL validation |
| D05 | Audience is `named_recipients` without recipients | FAIL validation |
| D06 | Recipient list supplied for another audience | FAIL validation |
| D07 | Unknown top-level property outside `extensions` | FAIL validation |
| D08 | Valid namespaced extension with schema/version/value | PASS |
| D09 | Extension attempts to override canonical `entity_id` meaning | FAIL semantic conformance |
| D10 | Update does not increment `record_revision` | FAIL optimistic-concurrency rule |
| D11 | `updated_at` precedes `created_at` | FAIL semantic validation |
| D12 | Restricted source exported with public audience without explicit derived/public View | FAIL publication policy |

# E. Typed references, generations and epochs

| ID | Case | Expected |
|---|---|---|
| E01 | Resolve typed reference to matching entity kind | PASS |
| E02 | Reference ID exists but requested kind differs | FAIL `invalid_contract` |
| E03 | Exact revision requested but only newer revision exists | FAIL `stale_revision` or `not_found`; no silent upgrade |
| E04 | Stale Provider generation used for mutation | FAIL `stale_generation` |
| E05 | Stale Node generation used for placement/execution | FAIL `stale_generation` |
| E06 | Stale workload generation presents old credential/network grant | FAIL and revoke/deny |
| E07 | Output arrives from old connection epoch | Retain as stale evidence; do not update current projection |
| E08 | Unqualified read resolves current revision under a contract that permits current reads | PASS with resolved revision recorded |
| E09 | Unqualified side-effecting target silently resolves current revision | FAIL unless contract/policy explicitly permits and records precondition |
| E10 | Tombstoned target reference | Typed `tombstoned` outcome with replacement/policy evidence |

# F. Aliases

| ID | Case | Expected |
|---|---|---|
| F01 | Same alias value from two namespaces/providers | Preserve separately |
| F02 | Provider reuses alias after generation change | New scoped Alias; old history retained |
| F03 | Mutable image tag treated as content identity | FAIL |
| F04 | Alias conflict is overwritten by latest timestamp | FAIL; retain conflict/evidence |
| F05 | Alias removed while canonical entity remains | PASS with historical relationship retained |
| F06 | Backend lookup returns Alias but no canonical mapping | Typed unresolved result; do not invent identity |

# G. Typed families and authority

| ID | Case | Expected |
|---|---|---|
| G01 | `resource_reservation` Lease reserves CPU/RAM | PASS within scope |
| G02 | Same Lease sends browser/device input | FAIL forbidden capability |
| G03 | `interactive_control` Lease sends scoped input | PASS with current fence token |
| G04 | Same control Lease reserves GPU capacity | FAIL forbidden capability |
| G05 | `device_ownership` Lease controls unrelated Device | FAIL resource scope |
| G06 | Provider kind claims capability not declared in Provider revision | FAIL unsupported/invalid contract |
| G07 | Authentication Session used as Permission Grant | FAIL authority separation |
| G08 | Expired/revoked Permission Grant | FAIL forbidden/expired |
| G09 | Approval bound to old Artifact/Object revision | FAIL stale approval under freshness policy |
| G10 | Reviewer verdict used as caller acceptance | FAIL authority separation |

# H. State machines

| ID | Case | Expected |
|---|---|---|
| H01 | Initial transition with `from_state: null`, sequence 1 | PASS if state machine permits |
| H02 | Accepted transition includes resulting record revision | PASS |
| H03 | Accepted transition lacks resulting revision | FAIL validation |
| H04 | Rejected transition includes typed rejection outcome | PASS and current state unchanged |
| H05 | Rejected transition includes resulting revision | FAIL validation |
| H06 | Sequence repeats or skips contrary to state-machine policy | FAIL conflict |
| H07 | Transition not listed in active state-machine version | FAIL rejected transition |
| H08 | UI writes `current_state` without transition record | FAIL |
| H09 | Provider health becomes degraded while Activity continues | PASS; separate state machines |
| H10 | Activity `completed` auto-sets verification `verified` | FAIL dimension separation |
| H11 | Verification `verified` auto-sets acceptance `accepted` | FAIL authority separation |
| H12 | Recovery resets state history | FAIL; append recovery transition |
| H13 | Expiry transition lacks evaluating authority/time | FAIL |
| H14 | Side-effecting completion lacks correlated Receipt/read-back required by machine | FAIL precondition |
| H15 | Reconstruct current state from accepted transition sequence | PASS and equal stored projection |

# I. Revision, Snapshot and Checkpoint

| ID | Case | Expected |
|---|---|---|
| I01 | Immutable Revision remains readable after newer revision | PASS |
| I02 | Snapshot is labelled restorable without Checkpoint contract | FAIL |
| I03 | Checkpoint produced but restore not attempted | Proof level remains `produced` |
| I04 | Restore accepted by provider but application read-back fails | Preserve distinct restore/application states |
| I05 | Capability Snapshot expired | Reject for new placement until refreshed |
| I06 | Semantic Snapshot used after Provider generation changes | FAIL stale/reacquire |
| I07 | `record_revision` confused with Object Revision ID | FAIL schema/type conformance |

# J. Migration

| ID | Case | Expected |
|---|---|---|
| J01 | Completed migration has output, target hash and supersession relationship | PASS |
| J02 | Completed migration lacks output | FAIL validation |
| J03 | Failed migration leaves source record valid | PASS failure behavior |
| J04 | Migration mutates frozen source bytes in place | FAIL |
| J05 | Field dropped without loss report | FAIL migration conformance |
| J06 | Default inserted without default report | FAIL migration conformance |
| J07 | Unknown extension preserved without execution | PASS |
| J08 | Bulk migration resumes after interruption without duplicate outputs | PASS idempotency |
| J09 | Migration tool version/digest omitted | FAIL proof requirement |
| J10 | New record links to source through migrated/supersedes relationship | PASS |
| J11 | Reverse/rollback unavailable but migration labelled reversible | FAIL |
| J12 | Source/target schemas are directionally incompatible and no migration exists | `incompatible`; block write/import |

# K. Compatibility

| ID | Case | Expected |
|---|---|---|
| K01 | Compatibility matrix explicitly allows older reader to ignore preserved extension | PASS |
| K02 | Consumer assumes MINOR version always compatible | FAIL policy |
| K03 | New enum value breaks exhaustive older consumer | Mark incompatible or migration required |
| K04 | Round-trip loses unknown fields | Mark lossy; never `compatible` |
| K05 | Compatibility is unknown for a mutation | Block unsafe mutation |
| K06 | Read-compatible but write-incompatible pair | Permit bounded read, block write |

# L. Privacy, audience and redaction

| ID | Case | Expected |
|---|---|---|
| L01 | Private entity exported to Workspace audience with policy | PASS |
| L02 | Restricted security report exported public unredacted | FAIL |
| L03 | Redacted public View links restricted source under access control | PASS |
| L04 | Raw credential appears in Event/Receipt/entity payload | FAIL secret-leak test |
| L05 | Search index contains source excluded from public audience | FAIL leakage test |
| L06 | Public ID remapping preserves restricted lineage | PASS |
| L07 | Migration lowers privacy class without named authority/policy | FAIL |
| L08 | Tombstoned personal entity remains publicly searchable contrary to policy | FAIL privacy/deletion policy |

# M. Tombstones, relationships and deletion

| ID | Case | Expected |
|---|---|---|
| M01 | Tombstone preserves canonical identity and reason/authority | PASS |
| M02 | Tombstone silently deletes relationship history | FAIL |
| M03 | Shared Object bytes deleted while referenced by retained Artifact | FAIL referential/retention check |
| M04 | Location deleted but Object remains with other replicas/history | PASS |
| M05 | Superseding entity rewrites predecessor | FAIL |
| M06 | Backend cascade deletes Receipts/Claims/relationships | FAIL |
| M07 | Physical byte deletion has receipted Activity and policy evidence | PASS |
| M08 | Replacement reference is visible to authorized current resolution | PASS |

# N. Stable outcomes

| ID | Case | Expected |
|---|---|---|
| N01 | Unsupported capability returns typed `unsupported` with limitations | PASS |
| N02 | Provider outage returns empty success result | FAIL |
| N03 | Partial result is flattened to success | FAIL |
| N04 | Stale generation is returned as generic failed | FAIL precision requirement |
| N05 | Retryability is omitted | FAIL validation |
| N06 | Failure retains evidence/Receipt references | PASS |

---

# Execution profile

The future executable safety net should run in this order:

1. parse all schemas and catalog entries;
2. register absolute schema URNs locally;
3. validate positive/negative structural fixtures;
4. run semantic invariants not expressible in JSON Schema;
5. run migration and round-trip compatibility cases;
6. run state transition reconstruction/rejection cases;
7. run privacy/export/leakage cases;
8. run tombstone/referential-integrity cases;
9. produce one signed/hashed conformance report Artifact;
10. retain every failed assertion with stable code and exact fixture.

## Freeze gate for 0B-WP01

This suite must be implemented and pass before the common schemas can be frozen for Phase 0C implementation.

Candidate schema presence alone is not proof.
