# Ptah Current State

**Last updated:** 2026-07-19  
**Overall status:** ACTIVE PLANNING — PHASE 0A FROZEN; PHASE 0B ACTIVE  
**Current phase:** Phase 0B — contracts, migrations, conformance and proof design  
**Active work package:** 0B-WP04 — Node, Facility, Provider, capability and health  
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

# Phase 0B completed candidate packages

## 0B-WP01 — Common identity, versioning and typed families

Accepted candidate:

- `ptah.common` `0.1.0`;
- `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`;
- `work-packages/PHASE-0B-WP01-COMMON-IDENTITY-VERSIONING-TYPED-FAMILIES.md`;
- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`.

Active common rules:

1. canonical IDs use lowercase UUIDv7 plus registered `entity_kind`;
2. backend IDs remain scoped Aliases;
3. schemas use JSON Schema 2020-12, absolute Ptah URNs and local catalogs;
4. domain entities embed the common Entity Envelope;
5. record revision, Object Revision, schema version, generation and connection epoch remain separate;
6. Provider, Session, Lease, Event, Revision, Snapshot, Recipe, Protocol and Evidence are typed families;
7. state machines are namespaced/versioned and there is no global `status` enum;
8. migration preserves frozen history and compatibility is directional;
9. privacy, audience, redaction, retention and tombstone/deletion are explicit;
10. structural validation never replaces semantic conformance.

## 0B-WP02 — Activity, Event, Receipt and proof

Accepted candidate:

- `ptah.activity` `0.1.0`;
- corrected mutable-request schemas at `0.1.1`;
- `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`;
- `work-packages/PHASE-0B-WP02-ACTIVITY-EVENT-RECEIPT-PROOF.md`;
- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`.

Active WP02 boundaries:

1. Activity Request and Activity are separate entities; acceptance creates a new Activity.
2. Activity, Operation and Attempt remain separate.
3. Operation owns one logical effect and persists across physical retries.
4. Attempt owns one physical try with a new ID/nonce and exact Node/Provider/workload generations and connection epoch.
5. request, placement, cancellation, retry, attachment and projection-health dimensions do not enter Activity lifecycle.
6. Event is typed notification and telemetry is sampled observation; neither is proof by itself.
7. Receipt is immutable append-only producer evidence bound to exact work and execution generations.
8. proof levels remain bounded by proof domain; there is no automatic universal ladder.
9. Review, Verdict, caller acceptance and authoritative external result remain separate.
10. stale, late, duplicate, contradictory and wrong-correlation evidence is reconciled explicitly.

Proof status:

- normative conventions, schemas, state machines, fixtures and consolidated safety net: candidate complete;
- executable conformance harness: deferred to 0B-WP13/0B-WP14;
- implementation freeze: not granted.

## 0B-WP03 — Object, Revision, View, Artifact and storage

**Status:** CANDIDATE COMPLETE — downstream use approved; implementation freeze deferred.

Accepted candidate:

- `ptah.object` / `ptah.storage` `0.1.0`;
- `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`;
- `work-packages/PHASE-0B-WP03-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE.md`;
- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`.

Normative and proof records:

- `contracts/PHASE-0B-WP03-OBJECT-STORAGE-CONVENTIONS.md`;
- `contracts/PHASE-0B-WP03-ENTITY-KIND-SUPPLEMENT.md`;
- `contracts/PHASE-0B-WP03-RELATIONSHIP-TYPE-REGISTRY.md`;
- `migrations/phase-0b/WP03-OBJECT-STORAGE-MIGRATION-COMPATIBILITY.md`;
- `conformance/PHASE-0B-WP03-OBJECT-ARTIFACT-STORAGE-SAFETY-NET.md`;
- `conformance/fixtures/phase-0b/wp03/object-artifact-storage-cases.v0.1.0.json`;
- Object, Relationship, Artifact, Storage Location and Storage Deletion Decision lifecycle machines.

Active WP03 boundaries:

1. Content owns exact bytes/digests and authorized deduplication scope.
2. Object owns durable logical/source identity; Object Revision owns one immutable version.
3. Storage Location owns one backend-specific materialization and never canonical identity.
4. filename, path, URL, ETag, provider key/version, tag and parser-local IDs remain aliases or metadata.
5. identical bytes may share Content only inside an authorized scope; logical Objects never merge solely by digest.
6. hash and detector observations remain plural evidence; classification/routing is a separate decision.
7. Relationship has stable identity plus immutable Relationship Revisions; overlapping relationships remain valid.
8. child Objects, Views, Previews and Derivatives remain separate and cannot replace originals.
9. Decomposition Runs retain budgets, coverage, unknown gaps and partial outputs; incomplete work cannot claim complete coverage.
10. Artifact promotion does not imply verification, review, acceptance or release.
11. Artifact Release is immutable, allowlisted and privacy/audience constrained.
12. Location lifecycle, health and verification remain independent.
13. tombstone, replica deletion and shared Content-byte deletion remain separate and receipted.
14. every produced record links to exact WP02 Activity/Operation/Attempt/Receipts where applicable.
15. migration preserves identity/history/privacy and cannot fabricate proof, parentage or detector consensus.

Candidate contents:

- 20 active schemas plus common/activity dependencies;
- five state machines;
- positive and negative fixtures;
- consolidated structural, graph, lifecycle, migration and privacy safety net;
- executable harness deferred to WP13/WP14;
- implementation/backend selection remains blocked.

---

# Active work — 0B-WP04

## Node, Facility, Provider, capability and health

WP04 must turn the frozen Node/Facility/Provider architecture plus WP01–WP03 into exact candidate contracts.

### Required entities and boundaries

- Node identity and Node generation;
- Node enrollment, ownership, trust and revocation;
- Node Capability Snapshot with observation time, expiry and source evidence;
- resource inventory, allocation, pressure and unavailable/reserved capacity;
- Facility definition, version, implementation and contribution manifests;
- Provider definition, Provider instance and Provider generation;
- Provider lifecycle, readiness, health, degradation and capability advertisement;
- Provider/Facility compatibility and exact implementation revision;
- endpoint, transport and protocol aliases without backend identity leakage;
- Node-local and remote Provider placement;
- Provider worker/process/session relationships;
- dependency, credential, network, device and Object-access requirements;
- capability claims versus verified conformance;
- health observation versus lifecycle/readiness;
- heartbeat, lease, last-seen and stale/offline projection rules;
- failover, replacement and generation fencing;
- operation dispatch eligibility through current Node/Provider capability evidence;
- migration, compatibility, negative fixtures and backend replacement.

### Core questions WP04 must resolve

1. stable Node identity versus enrollment, connection, boot and capability generations;
2. Node ownership/trust/authorization versus reachability;
3. declared capability versus observed/verified capability;
4. total, allocatable, reserved, used and pressure resource dimensions;
5. Facility contract identity versus one implementation/plugin/package;
6. Provider definition versus running Provider instance and generation;
7. Provider lifecycle versus readiness, health and capability state;
8. heartbeat loss versus durable Provider/Activity truth;
9. stale capability snapshots and scheduling eligibility;
10. Provider restart/replacement fencing and late Receipt rejection;
11. optional dependency degradation without false `ready` claims;
12. one-Node and later multi-Node compatibility through the same contracts.

### Minimum proof cases

- reconnecting Node retains stable identity but receives a new connection epoch;
- Node reboot or agent replacement advances the appropriate generation without creating a new Node identity;
- expired capability snapshot cannot authorize new placement/dispatch;
- declared GPU/device/runtime capability remains unverified until probed;
- pressure/resource observations do not overwrite durable capacity history;
- Facility remains stable while Provider implementation is replaced;
- Provider restart advances generation and fences stale Attempts/Receipts;
- lifecycle `running` does not imply readiness or health;
- optional dependency outage produces explicit degraded capability rather than full failure or false ready;
- heartbeat loss marks projection stale/offline without fabricating Activity failure;
- unauthorized/revoked Node cannot receive new work even when reachable;
- backend/provider replacement preserves Facility and caller contract identity.

Required outputs:

- normative Node/Facility/Provider conventions;
- entity-kind and capability registries;
- candidate schemas and local catalog;
- namespaced lifecycle/readiness/health state machines where mutable;
- migration/compatibility record;
- positive/negative fixtures;
- consolidated safety net;
- WP04 work-package record and ADR-0021 if the review accepts the boundary.

---

# Ordered Phase 0B sequence

1. 0B-WP01 — common identity/versioning/typed families. **CANDIDATE COMPLETE**
2. 0B-WP02 — Activity/Operation/Attempt/Event/Receipt/proof. **CANDIDATE COMPLETE**
3. 0B-WP03 — Object/Revision/View/Artifact/storage relationships. **CANDIDATE COMPLETE**
4. 0B-WP04 — Node/Facility/Provider/capability/health. **ACTIVE**
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

The Phase 0A parked/restricted items remain non-blocking and retain recorded reopening criteria, including `.P5C`, shared POSIX filesystems, MiniRouter licence, Dify modified licence, Ponytail/non-GNOME Wayland completion, unaudited private device source, prototype repositories without clear licences/proof, missing `amertoglu16` source, and final public Ptah project licence.

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

1. `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`;
2. `work-packages/PHASE-0B-WP03-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE.md`;
3. `schemas/phase-0b/object/schema-catalog.v0.1.0.json`;
4. `contracts/PHASE-0B-WP03-OBJECT-STORAGE-CONVENTIONS.md`;
5. `decisions/ADR-0001-NODE-PROTOCOL-WORKSPACE-PROVIDER-BOUNDARY.md`;
6. `work-packages/PHASE-0A-WP01-NODE-PROTOCOL.md` and core-runtime records;
7. `decisions/ADR-0014-ISOLATION-RUNTIME-PLACEMENT-SCHEDULING-BOUNDARY.md`;
8. `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`;
9. `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`;
10. `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `REQUIREMENT_CLOSURE_MATRIX.md`.

Do not restart donor research or implementation from conversational memory.
