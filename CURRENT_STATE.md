# Ptah Current State

**Last updated:** 2026-07-19  
**Overall status:** ACTIVE PLANNING — PHASE 0A FROZEN; PHASE 0B ACTIVE  
**Current phase:** Phase 0B — contracts, migrations, conformance and proof design  
**Active work package:** 0B-WP08 — Domain Pack, firmware, disk and Device contracts  
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

All current v1 requirements are closed for contract design. That closure does not authorize implementation.

---

# Phase 0B completed candidate packages

## 0B-WP01 — Common identity, versioning and typed families

**Status:** CANDIDATE COMPLETE — downstream use approved; implementation freeze deferred.

Accepted candidate:

- `ptah.common` `0.1.0`;
- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`;
- `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`.

Key boundaries:

- UUIDv7 canonical identities and scoped Aliases;
- JSON Schema 2020-12 with absolute local URN catalogs;
- typed families and namespaced/versioned state machines;
- directional migrations and explicit privacy/retention/deletion;
- structural validation never replaces semantic conformance.

## 0B-WP02 — Activity, Operation, Attempt, Event, Receipt and proof

**Status:** CANDIDATE COMPLETE — downstream use approved; executable conformance deferred.

Accepted candidate:

- `ptah.activity` `0.1.0` with corrected request schemas `0.1.1`;
- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`;
- `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`.

Key boundaries:

- Activity Request, Activity, Operation and physical Attempt remain separate;
- every retry gets new Attempt/nonce/generation evidence;
- Event/telemetry are not proof;
- Receipt, Review, Verdict, caller acceptance and external authoritative result remain separate;
- stale, duplicate, contradictory and wrong-generation evidence is reconciled explicitly.

## 0B-WP03 — Object, Revision, View, Artifact and storage

**Status:** CANDIDATE COMPLETE — downstream use approved; executable graph/storage conformance deferred.

Accepted candidate:

- `ptah.object` / `ptah.storage` `0.1.0`;
- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`;
- `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`.

Key boundaries:

- Content owns exact bytes; Object owns logical/source identity; Revision owns one immutable version;
- detector/relationship evidence remains plural;
- children, Views, Previews and Derivatives never replace originals;
- Artifact promotion, Release, storage Location, health and verification remain separate;
- tombstone, Location deletion and shared Content-byte deletion are different receipted acts.

## 0B-WP04 — Node, Facility, Provider, capability and health

**Status:** CANDIDATE COMPLETE — downstream use approved; executable runtime conformance deferred.

Accepted candidate:

- `ptah.runtime` `0.1.2`;
- 19 record schemas and six active lifecycle machines;
- `schemas/phase-0b/runtime/schema-catalog.v0.1.2.json`;
- ADR-0021 plus ADR-0021A/0021B corrections.

Key boundaries:

- Node, Facility, Provider definition/revision/instance/generation remain separate;
- heartbeat, lifecycle, reachability, readiness, health, pressure and capability evidence remain separate;
- local Providers bind exact Node evidence; remote Providers use truthful remote-service identity;
- Dispatch Eligibility is operation-specific, exact-generation-bound and expiring;
- Provider/backend/locality replacement fences stale work/evidence.

## 0B-WP05 — Workspace, Session, checkpoint, restore and recovery

**Status:** CANDIDATE COMPLETE — downstream use approved; executable recovery conformance deferred.

Accepted candidate:

- `ptah.workspace` `0.1.0`;
- 19 schemas and nine lifecycle machines;
- `schemas/phase-0b/workspace/schema-catalog.v0.1.0.json`;
- `decisions/ADR-0022-WORKSPACE-SESSION-CHECKPOINT-RESTORE-RECOVERY-BOUNDARY.md`;
- `work-packages/PHASE-0B-WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY.md`.

Key boundaries:

- Workspace survives Revision, Provider, Materialization, Session, client and layout changes;
- detaching a client does not stop runtime;
- Checkpoint Request, Component, Bundle, integrity Verification and target Compatibility remain separate;
- restore creates new Activities/Attempts/generations;
- `restored_runtime` is not application recovery;
- uncertain external effects survive crash/restore until reconciled.

## 0B-WP06 — Transfer, synchronization, conflict, backup and storage restore

**Status:** CANDIDATE COMPLETE — downstream use approved; executable transfer/backup conformance deferred.

Accepted candidate:

- `ptah.transfer` `0.1.0`;
- 18 schemas and seven lifecycle machines;
- `schemas/phase-0b/transfer/schema-catalog.v0.1.0.json`;
- `decisions/ADR-0023-TRANSFER-SYNC-CONFLICT-BACKUP-RESTORE-BOUNDARY.md`;
- `work-packages/PHASE-0B-WP06-TRANSFER-SYNC-CONFLICT-BACKUP.md`.

Key boundaries:

- Transfer Request/Run/Attempt/Manifest/Progress/Verification remain separate;
- Provider acknowledgement does not create accepted Content/Object/Location truth;
- Sync Relationship/Cursor/Run/Conflict/Resolution remain separate;
- Backup Policy/Snapshot/Verification/Prune/Restore remain separate;
- sync, replica, checkpoint, export and backup are not interchangeable;
- `restored_storage` does not mean Workspace/application recovery.

## 0B-WP07 — Recipe, Build, provenance, SBOM, signature and verification

**Status:** CANDIDATE COMPLETE — downstream use approved; executable Build/provenance conformance deferred.

Accepted candidate:

- `ptah.build` / `ptah.provenance` catalog `0.1.1`;
- 30 active schemas and nine lifecycle machines;
- `schemas/phase-0b/build/schema-catalog.v0.1.1.json`;
- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP07-CORRECTION-0.1.1.md`;
- `work-packages/PHASE-0B-WP07-RECIPE-BUILD-PROVENANCE.md`;
- `decisions/ADR-0024-RECIPE-BUILD-PROVENANCE-SBOM-SIGNATURE-VERIFICATION-BOUNDARY.md`.

Key boundaries:

1. Recipe, immutable Revision, Proposal, Acceptance, Readiness, Backend Compatibility, Plan, Run and Step remain separate.
2. backend/job/path IDs remain Aliases; Recipe identity survives backend replacement.
3. Build Step maps Recipe `step_key` to WP02 Operations/Attempts; retries never reuse Attempt identity.
4. exact materials, mutable/volatile inputs, cache identity and secret access are explicit.
5. Cache Use is not execution or independent reproduction.
6. Build Output Record binds exact producer Attempt/generations to Content/Object Revision/digests.
7. paths/tags/coordinates never become output or Artifact identity.
8. Build completion is separate from export, SBOM, attestation, signing, verification, review, reproduction and release acceptance.
9. Package Observation, SBOM Coverage and immutable SBOM Document remain separate.
10. Attestation, Signature, Transparency Evidence and their Verifications remain separate.
11. valid cryptography proves identity/integrity only under exact Trust Policy, not functionality or acceptance.
12. Proof Bundle preserves distinct proof domains/authority; it is not a universal verdict.
13. Reproduction requires a new Run/Activities/Attempts and explicit byte/functional Comparison.
14. draft overlapping `build.step_run` and `provenance.sbom_revision` identities are removed by correction `0.1.1`.

---

# Active work — 0B-WP08

## Domain Pack, firmware, disk and Device contracts

WP08 must turn the frozen Object decomposition, Domain Pack, firmware/disk/filesystem and Device architecture plus WP01–WP07 into exact candidate contracts without selecting parser, flasher, device-control or filesystem backends.

### Required entities and boundaries

- Domain Pack identity, immutable Pack Revision, capability declarations and compatibility;
- detection claims, confidence, coverage and conflicting detector results;
- Inventory, Decomposition, Validation, Compare, Rebuild and Execute recipes/runs;
- progressive/budgeted decomposition and retained unknown gaps;
- firmware Package, Manifest, Component, target compatibility and tool/loader/programmer evidence;
- disk/block image, partition table, partition, filesystem and mount/inspection Sessions;
- read-only/static analysis versus state-changing transformation/write;
- Device stable identity, Interface incarnation, Connection epoch and Provider generation;
- Device Session, Lease/fencing, protocol stage and physical Operation/Attempt;
- display/log/input Streams and Screen Context boundaries;
- immutable backup before destructive device operations;
- protocol acknowledgement versus write/read-back verification;
- recovery/cleanup and partial/uncertain physical outcomes;
- migration, backend replacement and cross-platform/device-family extension.

### Core questions WP08 must resolve

1. generic Domain Pack contract versus format/family-specific revisions;
2. detector observation versus accepted classification/compatibility;
3. inventory/decomposition outputs versus source Object truth;
4. child/partition/component identity across parser changes;
5. static transformation versus physical mutation authority;
6. firmware target compatibility versus Device presence/identity;
7. Device identity versus transient USB/ADB/Fastboot/META/DIAG/interface aliases;
8. connection epoch, Provider generation, Lease/fence and physical retry safety;
9. vendor protocol stages, loaders/programmers and exact target evidence;
10. acknowledgement versus verified physical state;
11. required backup, destructive-action approval and post-operation read-back;
12. unsupported/opaque/partial formats and devices without false success;
13. Domain Pack/backend replacement without Object/Device identity loss.

### Minimum proof cases

- two detectors disagree without destroying either observation;
- bounded decomposition produces useful partial children and explicit unknown gaps;
- parser/version replacement preserves source Object identity and creates new derived revisions;
- disk/partition/filesystem hierarchy retains exact offsets/ranges and overlap checks;
- read-only mount/inspection cannot silently become writable;
- firmware compatibility binds exact package/component/Device/tool revisions;
- disconnected/re-enumerated Device advances interface/connection generation;
- stale Lease/fence/Provider evidence cannot mutate the Device;
- protocol acknowledgement without read-back cannot become verified success;
- destructive operation is blocked without required immutable backup and approval;
- disconnect during non-idempotent write produces uncertain state and reconciliation, not blind retry;
- unsupported family/tool path remains explicit negative capability evidence;
- replacement Domain Pack/Provider preserves canonical Object/Device history.

### Required outputs

- normative Domain Pack/firmware/disk/Device conventions;
- entity-kind supplements/corrections where required;
- candidate schemas and local catalog;
- namespaced lifecycle state machines;
- migration/compatibility record;
- positive/negative fixtures;
- consolidated safety net;
- WP08 work-package record and ADR-0025 if review accepts the boundary.

---

# Ordered Phase 0B sequence

1. WP01 common identity/versioning/typed families — **CANDIDATE COMPLETE**
2. WP02 Activity/Operation/Attempt/Event/Receipt/proof — **CANDIDATE COMPLETE**
3. WP03 Object/Revision/View/Artifact/storage — **CANDIDATE COMPLETE**
4. WP04 Node/Facility/Provider/capability/health — **CANDIDATE COMPLETE**
5. WP05 Workspace/Session/checkpoint/recovery — **CANDIDATE COMPLETE**
6. WP06 transfer/sync/conflict/backup — **CANDIDATE COMPLETE**
7. WP07 Recipe/Build/provenance/SBOM/signature/verification — **CANDIDATE COMPLETE**
8. WP08 Domain Pack/firmware/disk/Device — **ACTIVE**
9. WP09 Application/Browser/semantic UI/Shell
10. WP10 knowledge/data/Package/Plugin
11. WP11 isolation/placement/reservation/lease/secure grants
12. WP12 security/Finding/Claim/Evidence/reproduction
13. WP13 migrations and executable conformance harness
14. WP14 golden/negative corpus and proof-plan freeze
15. Phase 0B review/freeze and Phase 0C readiness decision

---

# Parked/restricted items

Phase 0A parked/restricted items remain non-blocking with recorded reopening criteria, including `.P5C`, shared POSIX filesystems, MiniRouter licence, Dify modified licence, Ponytail/non-GNOME Wayland completion, unaudited private device source, prototype repositories without clear licences/proof, missing `amertoglu16` source and the final public Ptah project licence.

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
- deployment of Nodes, Providers, Workspaces, build/device workers, registries or signing infrastructure;
- presenting candidate contracts as built or proven.

Implementation begins only after Phase 0C approval is recorded here.

---

# Chat continuation instruction

Read this file first, then:

1. `decisions/ADR-0024-RECIPE-BUILD-PROVENANCE-SBOM-SIGNATURE-VERIFICATION-BOUNDARY.md`;
2. `work-packages/PHASE-0B-WP07-RECIPE-BUILD-PROVENANCE.md`;
3. `schemas/phase-0b/build/schema-catalog.v0.1.1.json`;
4. `decisions/ADR-0007-OBJECT-GRAPH-DECOMPOSITION-DERIVATIVE-BOUNDARY.md`;
5. `decisions/ADR-0008-DISK-FIRMWARE-DEVICE-OPERATION-BOUNDARY.md`;
6. `decisions/ADR-0009-DEVICE-SESSION-DISPLAY-INPUT-SEMANTIC-UI-BOUNDARY.md`;
7. the relevant Phase 0A WP05/WP06/WP07 Domain Pack, firmware/disk and Device donor/internal records;
8. ADR-0018 through ADR-0024;
9. `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `REQUIREMENT_CLOSURE_MATRIX.md`.

Do not restart donor research or implementation from conversational memory.
