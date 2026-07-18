# Ptah Current State

**Last updated:** 2026-07-18  
**Overall status:** ACTIVE PLANNING — PHASE 0A FROZEN; PHASE 0B ACTIVE  
**Current phase:** Phase 0B — contracts, migrations, conformance and proof design  
**Active work package:** 0B-WP03 — Object, Revision, View, Artifact and storage relationships  
**Runtime implementation:** NOT STARTED  
**Dependency selection:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Frozen Phase 0A checkpoint

Phase 0A is complete and frozen at:

```text
7d2dffee48f1400ba1cf88823343f09a3895ad33
```

Freeze decision:

- `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`

All current v1 requirements are closed for contract design. No runtime implementation is authorized by that closure.

---

# Phase 0B common layer — WP01 candidate complete

Accepted candidate:

- `ptah.common` `0.1.0`
- `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`
- `work-packages/PHASE-0B-WP01-COMMON-IDENTITY-VERSIONING-TYPED-FAMILIES.md`
- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`

Common rules remain active:

1. canonical IDs use lowercase UUIDv7 plus registered `entity_kind`;
2. backend IDs remain scoped Aliases;
3. schemas use JSON Schema 2020-12, absolute Ptah URNs and local catalogs;
4. domain entities embed the common Entity Envelope;
5. record revision, Object Revision, schema version, generation and connection epoch remain separate;
6. Provider, Session, Lease, Event, Revision, Snapshot, Recipe, Protocol and Evidence are typed families;
7. state machines are namespaced/versioned and there is no global `status` enum;
8. migration preserves frozen history and compatibility is directional;
9. privacy/audience/redaction/retention and tombstone/deletion are explicit;
10. structural validation never replaces semantic conformance.

---

# Phase 0B Activity/Event/proof layer — WP02 candidate complete

Accepted candidate:

- `ptah.activity` `0.1.0`;
- corrected mutable-request schemas at `0.1.1`;
- `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`;
- `work-packages/PHASE-0B-WP02-ACTIVITY-EVENT-RECEIPT-PROOF.md`;
- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`.

Normative records:

- `contracts/PHASE-0B-WP02-ACTIVITY-EVENT-PROOF-CONVENTIONS.md`
- `contracts/PHASE-0B-WP02-ENTITY-KIND-SUPPLEMENT.md`
- `contracts/PHASE-0B-WP02-PROOF-LEVEL-REGISTRY.md`
- `state-machines/phase-0b/`
- `conformance/PHASE-0B-WP02-ACTIVITY-EVENT-RECEIPT-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp02/activity-event-receipt-cases.v0.1.0.json`

## WP02 boundaries now active

1. Activity Request and Activity are different entities; acceptance creates a new durable Activity.
2. Activity lifecycle is limited to `queued`, `preparing`, `running`, `waiting`, `paused`, `resuming`, `recovering`, `completed`, `failed`, and `cancelled`.
3. requested, leasing, cancelling, retrying, detached and unknown belong to separate requests/entities/dimensions.
4. Activity Dependency is first-class and Event delivery cannot satisfy it by itself.
5. Operation owns one logical side effect/observation and persists across physical retries.
6. Attempt owns one physical try with a new ID/nonce and exact Node/Provider/workload generations and connection epoch.
7. retry and idempotency classes are explicit; uncertain non-idempotent work cannot retry automatically.
8. Cancellation Request and Manual Action Request have independent versioned lifecycles.
9. Event is typed notification; telemetry is sampled operational observation; neither is proof by itself.
10. Receipt is immutable append-only producer evidence bound to exact Activity/Operation/Attempt/nonce/generations/epoch.
11. proof levels are bounded by request/dispatch, runtime, output, external-result, and review domains; no automatic cross-domain ladder exists.
12. Review and Verdict are separate, and Verdict is not caller acceptance.
13. Authoritative External Result preserves the source system/device authority and cannot be fabricated from weaker evidence.
14. Reconciliation explicitly dispositions stale, late, duplicate, contradictory, unauthenticated and wrong-correlation evidence.
15. Event or telemetry loss cannot erase durable Activity truth or proof-critical Receipts.
16. the first mutable-request drafts were not rewritten; corrected `0.1.1` schemas supersede them through catalog history.

## WP02 proof status

- normative conventions and proof-level registry: candidate complete;
- 17 active schema entries plus common dependencies: candidate complete;
- six lifecycle state machines: candidate complete;
- consolidated safety-net specification: committed;
- positive/negative fixtures: committed;
- executable conformance harness: deferred to 0B-WP13/0B-WP14;
- implementation freeze: not granted.

---

# Active work — 0B-WP03

## Object, Revision, View, Artifact and storage relationships

WP03 must turn ADR-0006 and ADR-0007 plus WP01/WP02 into exact contracts.

### Required entities and boundaries

- `object.object` — canonical content/logical Object identity;
- `object.revision` — immutable source/logical revision;
- content byte identity and hash observation;
- `object.detector_observation` — one detector/type/structure claim;
- `core.relationship` — first-class typed relationship and revision;
- `object.view` — derived representation over an exact Object/revision;
- `object.preview` — human-oriented derived View;
- `object.derivative` — transformed output;
- child Object relationships from decomposition;
- `object.decomposition_run` and progressive levels;
- `object.artifact` — durable promoted-result role;
- `object.artifact_release` — immutable released/published Artifact revision;
- `storage.location` — physical/logical replica/location;
- content-addressed storage identity versus mutable location aliases;
- production links to Activity/Operation/Attempt/Receipt;
- storage verification, corruption, missing-location and repair evidence;
- retention, tombstone, shared-reference deletion and supersession;
- migrations, compatibility and negative fixtures.

### Core questions WP03 must resolve

1. Object content identity versus logical revision identity.
2. Whether identical bytes across different logical sources share one content record while retaining separate provenance/roles.
3. Hash algorithm/version and multi-hash records without letting path/tag/name become identity.
4. Original, child, View, Preview, Derivative and Artifact relationships.
5. Detector disagreement and confidence without destructive type flattening.
6. progressive decomposition and partial/failed/unsupported levels.
7. Artifact promotion without copying/replacing Object identity.
8. immutable Artifact Release, publication audience and provenance.
9. storage Location/replica state, verification and movement.
10. tombstone versus physical deletion while retained references still exist.
11. production and proof correlation through WP02 Receipts.
12. exact migration/compatibility behavior for saved Objects/Artifacts.

### WP03 minimum proof cases

- identical bytes from two sources retain content deduplication and distinct provenance;
- same logical Object receives a new immutable Revision without rewriting the prior one;
- detector disagreement remains visible;
- View/Preview/Derivative cannot replace the original;
- child extraction records exact parent/revision/range/tool/Activity evidence;
- partial decomposition does not claim complete coverage;
- Artifact role references exact Object(s) and producing Activity/Operation/Attempt/Receipts;
- mutable path/tag/location cannot become content identity;
- corrupted/missing replica is retained as a location state and repaired from a verified replica;
- shared bytes are not physically deleted while retained Objects/Artifacts reference them;
- public Artifact Release cannot leak restricted source/evidence;
- backend replacement preserves Object/Artifact identities.

---

# Ordered Phase 0B sequence

1. 0B-WP01 — common identity/versioning/typed families. **CANDIDATE COMPLETE**
2. 0B-WP02 — Activity/Operation/Attempt/Event/Receipt/proof. **CANDIDATE COMPLETE**
3. 0B-WP03 — Object/Revision/View/Artifact/storage relationships. **ACTIVE**
4. 0B-WP04 — Node/Facility/Provider/capability/health.
5. 0B-WP05 — Workspace/Session/checkpoint/recovery.
6. 0B-WP06 — transfer/sync/conflict/backup.
7. 0B-WP07 — Recipe/Build/provenance/SBOM/signature/verification.
8. 0B-WP08 — Domain Pack/firmware/disk/Device.
9. 0B-WP09 — Application/Browser/semantic UI/Shell.
10. 0B-WP10 — knowledge/data/Package/Plugin.
11. 0B-WP11 — isolation/placement/reservation/lease/secure grants.
12. 0B-WP12 — security/Finding/Claim/Evidence/reproduction.
13. 0B-WP13 — migrations and executable conformance harness.
14. 0B-WP14 — golden/negative corpus and proof-plan freeze.
15. Phase 0B review/freeze and Phase 0C readiness decision.

---

# Parked/restricted items

The Phase 0A parked/restricted items remain non-blocking and retain recorded reopening criteria, including `.P5C`, shared POSIX filesystems, MiniRouter licence, Dify modified licence, Ponytail/non-GNOME Wayland completion, unaudited private device source, prototype repos without clear licences/proof, missing `amertoglu16` source, and final public Ptah project licence.

---

# No-build boundary

Allowed now:

- contracts, schemas and state machines;
- migration/compatibility design;
- conformance and lawful fixture design;
- proof plans and public/private export boundaries.

Not allowed yet:

- runtime or UI implementation;
- donor-source reuse;
- production dependency/backend selection;
- deployment of Nodes, Providers, browsers, scanners or schedulers;
- presenting candidates as built or proven.

Implementation begins only after Phase 0C approval is recorded here.

---

# Chat continuation instruction

Read this file first, then:

1. `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`;
2. `work-packages/PHASE-0B-WP02-ACTIVITY-EVENT-RECEIPT-PROOF.md`;
3. `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`;
4. `contracts/PHASE-0B-WP02-ACTIVITY-EVENT-PROOF-CONVENTIONS.md`;
5. `decisions/ADR-0006-STORAGE-TRANSFER-SYNC-BOUNDARY.md`;
6. `decisions/ADR-0007-OBJECT-GRAPH-DECOMPOSITION-DERIVATIVE-BOUNDARY.md`;
7. `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`;
8. `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `REQUIREMENT_CLOSURE_MATRIX.md`.

Do not restart donor research or implementation from conversational memory.
