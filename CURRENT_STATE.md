# Ptah Current State

**Last updated:** 2026-07-19  
**Overall status:** ACTIVE PLANNING — PHASE 0A FROZEN; PHASE 0B ACTIVE  
**Current phase:** Phase 0B — contracts, migrations, conformance and proof design  
**Active work package:** 0B-WP05 — Workspace, Session, checkpoint and recovery  
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

Active rules:

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

## 0B-WP02 — Activity, Operation, Attempt, Event, Receipt and proof

Accepted candidate:

- `ptah.activity` `0.1.0` with corrected mutable-request schemas `0.1.1`;
- `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`;
- `work-packages/PHASE-0B-WP02-ACTIVITY-EVENT-RECEIPT-PROOF.md`;
- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`.

Active rules:

1. Activity Request, Activity, Operation and Attempt remain separate;
2. Operation persists across physical retries and every Attempt has a new ID/nonce;
3. Attempt binds exact Node/Provider/workload generations and connection epoch;
4. request, placement, cancellation, retry, attachment and projection-health dimensions remain outside Activity lifecycle;
5. Event/telemetry are not proof;
6. Receipt is immutable append-only producer evidence with exact correlation;
7. proof levels remain bounded by domain;
8. Review, Verdict, caller acceptance and authoritative external result remain separate;
9. stale, late, duplicate and contradictory evidence is reconciled explicitly.

## 0B-WP03 — Object, Revision, View, Artifact and storage

Accepted candidate:

- `ptah.object` / `ptah.storage` `0.1.0`;
- `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`;
- `work-packages/PHASE-0B-WP03-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE.md`;
- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`.

Active rules:

1. Content owns exact bytes/digests and authorized deduplication scope;
2. Object owns logical/source identity and Object Revision owns one immutable version;
3. Location is one backend materialization and never canonical identity;
4. hash/detector observations remain plural and classification is separate;
5. relationships have stable identity plus immutable revisions;
6. child Objects, Views, Previews and Derivatives cannot replace originals;
7. decomposition retains budgets, coverage, unknown gaps and partial outputs;
8. Artifact promotion does not imply verification, review, acceptance or release;
9. Artifact Release is immutable, allowlisted and audience/privacy constrained;
10. lifecycle, health and verification remain separate for Locations;
11. tombstone, replica deletion and shared Content-byte deletion remain separate and receipted.

## 0B-WP04 — Node, Facility, Provider, capability and health

**Status:** CANDIDATE COMPLETE — downstream use approved; implementation freeze deferred.

Accepted records:

- `decisions/ADR-0021-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH-BOUNDARY.md`;
- `decisions/ADR-0021A-WP04-CATALOG-PROOF-VOCABULARY-CORRECTION.md`;
- `decisions/ADR-0021B-WP04-FINAL-CATALOG-CORRECTION.md`;
- `work-packages/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH.md`;
- `contracts/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CONVENTIONS.md`;
- `contracts/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CONVENTIONS.v0.1.1.md`;
- `contracts/PHASE-0B-WP04-ENTITY-KIND-SUPPLEMENT.md`;
- `schemas/phase-0b/runtime/schema-catalog.v0.1.2.json`;
- `migrations/phase-0b/WP04-NODE-FACILITY-PROVIDER-MIGRATION-COMPATIBILITY.md`;
- `conformance/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-SAFETY-NET.md`;
- `conformance/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-SAFETY-NET.v0.1.1.md`;
- `conformance/fixtures/phase-0b/wp04/node-facility-provider-cases.v0.1.0.json`.

Active catalog:

- `ptah.runtime` `0.1.2`;
- 19 record schemas remain `0.1.0`;
- Node Enrollment lifecycle `0.1.1`;
- Node lifecycle `0.1.0`;
- Facility lifecycle `0.1.0`;
- Facility Instance lifecycle `0.1.1`;
- Provider lifecycle `0.1.0`;
- Provider Instance lifecycle `0.1.2`.

Active WP04 boundaries:

1. Node identity remains separate from aliases, enrollment, trust, reachability, lifecycle, generation and connection epoch.
2. ordinary reconnect may advance only epoch; reboot/reinstall/restore/replacement may advance Node generation under policy.
3. heartbeat proves recent authenticated contact only.
4. Node capability/resource snapshots are immutable, expiring and generation-bound.
5. resource total, allocatable, reserved, consumed, available, unavailable/quarantined, overcommit and pressure remain separate.
6. Capability Definition, Claim, Verification, Availability and Snapshot remain separate.
7. Facility, Facility Revision and Facility Instance remain caller-facing contracts independent of implementation.
8. Provider, Provider Revision and Provider Instance/generation remain separate.
9. Provider lifecycle, reachability, readiness and health remain separate.
10. running does not imply ready; ready does not imply healthy; healthy does not imply authorized/capable/resourced.
11. local Providers bind exact Node evidence; remote Providers bind approved remote-service evidence and never fabricate Nodes.
12. optional dependency loss degrades only affected operation/capability scope.
13. Dispatch Eligibility is immutable, operation-specific, exact-generation-bound and expiring; it is not Placement, Reservation, Lease, Attempt or proof.
14. Provider/backend/locality replacement preserves Facility identity and fences stale work/evidence.
15. the acceptance review corrected unregistered proof labels through versioned `0.1.1`/`0.1.2` lifecycle records without rewriting candidate history.

Candidate contents:

- 19 active record schemas;
- six active lifecycle machines;
- migration/compatibility rules;
- positive/negative cross-record fixtures;
- consolidated identity, generation, freshness, resource, locality, lifecycle and dispatch safety net;
- executable harness deferred to WP13/WP14;
- implementation/backend selection remains blocked.

---

# Active work — 0B-WP05

## Workspace, Session, checkpoint and recovery

WP05 must turn the frozen persistent-Workspace and recovery architecture plus WP01–WP04 into exact candidate contracts.

### Required entities and boundaries

- stable Workspace identity and Workspace Revision/configuration;
- Workspace ownership, membership, policy and visibility;
- Workspace Provider binding without making one backend the Workspace identity;
- Workspace lifecycle versus Provider readiness/health;
- Workspace generation and active materialization;
- Workspace Session typed family and exact Session kinds;
- human, automation and service attachment relationships;
- control ownership/lease references without duplicating WP11 lease authority;
- runtime components and mounted Object/View/Location references;
- Workspace journal/outbox and reconnect cursor;
- checkpoint request, checkpoint bundle and component manifests;
- checkpoint consistency, completeness, privacy and credential classification;
- restore request, compatibility decision, restore attempt and recovery read-back;
- archive/export/import versus checkpoint/resume;
- Node/Provider replacement and generation fencing;
- session detachment versus Workspace/runtime persistence;
- partial checkpoint, failed restore and uncertain external-side-effect handling;
- migration, compatibility, positive/negative fixtures and backend replacement.

### Core questions WP05 must resolve

1. persistent Workspace identity versus one running materialization/generation;
2. Workspace configuration revision versus runtime state and checkpoint state;
3. Workspace lifecycle versus Provider lifecycle/readiness/health;
4. Workspace Session identity versus client connection and presentation state;
5. detachment versus stop, suspend, checkpoint and archive;
6. checkpoint creation versus restorable/recovered state;
7. application-consistent versus crash-consistent versus partial checkpoints;
8. secret/credential and private-object handling inside checkpoints;
9. restore compatibility across Node/Provider/runtime revisions;
10. new generation/epoch/Attempt identities after restore;
11. reconciliation of uncertain Operations and external results;
12. one-Node and later multi-Node recovery under the same contracts.

### Minimum proof cases

- Workspace survives client/session detachment without becoming stopped;
- Provider restart creates a new materialization generation while Workspace ID remains stable;
- checkpoint files created does not equal restore-ready;
- incomplete or credential-bearing checkpoint is classified honestly;
- incompatible target Node/Provider blocks restore before mutation;
- successful restore still requires Provider readiness and application read-back;
- old Attempts/Receipts cannot prove restored-generation work;
- uncertain non-idempotent Operations remain unresolved after crash until reconciliation;
- export/import creates explicit identity/provenance decisions rather than silent clone/merge;
- backend replacement preserves Workspace identity and history.

Required outputs:

- normative Workspace/Session/checkpoint/recovery conventions;
- entity-kind supplement;
- candidate schemas and local catalog;
- namespaced lifecycle state machines;
- migration/compatibility record;
- positive/negative fixtures;
- consolidated safety net;
- WP05 work-package record and ADR-0022 if the review accepts the boundary.

---

# Ordered Phase 0B sequence

1. 0B-WP01 — common identity/versioning/typed families. **CANDIDATE COMPLETE**
2. 0B-WP02 — Activity/Operation/Attempt/Event/Receipt/proof. **CANDIDATE COMPLETE**
3. 0B-WP03 — Object/Revision/View/Artifact/storage. **CANDIDATE COMPLETE**
4. 0B-WP04 — Node/Facility/Provider/capability/health. **CANDIDATE COMPLETE**
5. 0B-WP05 — Workspace/Session/checkpoint/recovery. **ACTIVE**
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

The Phase 0A parked/restricted items remain non-blocking with recorded reopening criteria, including `.P5C`, shared POSIX filesystems, MiniRouter licence, Dify modified licence, Ponytail/non-GNOME Wayland completion, unaudited private device source, prototype repositories without clear licences/proof, missing `amertoglu16` source and final public Ptah project licence.

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
- deployment of Nodes, Providers, Workspaces, browsers, scanners or schedulers;
- presenting candidates as built or proven.

Implementation begins only after Phase 0C approval is recorded here.

---

# Chat continuation instruction

Read this file first, then:

1. `decisions/ADR-0021-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH-BOUNDARY.md`;
2. `decisions/ADR-0021B-WP04-FINAL-CATALOG-CORRECTION.md`;
3. `work-packages/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH.md`;
4. `schemas/phase-0b/runtime/schema-catalog.v0.1.2.json`;
5. `decisions/ADR-0001-NODE-PROTOCOL-WORKSPACE-PROVIDER-BOUNDARY.md`;
6. core Workspace/Session/recovery Phase 0A records;
7. `decisions/ADR-0014-ISOLATION-RUNTIME-PLACEMENT-SCHEDULING-BOUNDARY.md`;
8. `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`;
9. `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`;
10. `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`;
11. `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `REQUIREMENT_CLOSURE_MATRIX.md`.

Do not restart donor research or implementation from conversational memory.