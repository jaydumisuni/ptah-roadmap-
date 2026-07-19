# Ptah Requirement Closure Matrix

**Phase:** 0B contract design  
**Status:** ALL V1 REQUIREMENTS CLOSED FOR DESIGN — PHASE 0A FROZEN; WP01–WP06 CANDIDATE COMPLETE; WP07 ACTIVE

This file maps Ptah requirements to internal evidence, composite donors, native ownership, exit strategy and proof.

A requirement is never closed by naming one repository. Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

Design closure does **not** authorize implementation. Phase 0B executable conformance and Phase 0C slice approval remain mandatory.

Phase 0A frozen checkpoint:

```text
7d2dffee48f1400ba1cf88823343f09a3895ad33
```

Freeze/entry decision: `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`.

---

# Requirements closed for Phase 0B contract design

| ID | Requirement | Native Ptah owner | Composite machinery/evidence | Phase 0B contract status |
|---|---|---|---|---|
| CORE-001 | Persistent Workspace model | Workspace/Revision/Materialization/Session | Daytona, Coder, E2B, Dev Containers, DevPod, local/OCI providers | **WP05 candidate complete — ADR-0022** |
| CORE-002 | Concurrent Activity runtime | Activity Ledger | Temporal, NATS/JetStream, OTel and internal runtime/evidence systems | **WP02 candidate complete — ADR-0019** |
| CORE-003 | Universal Object graph plus knowledge/document extensions | Content/Object/Revision/Relationship/View | internal recovery tools, decomposition donors, Hunter, RAGFlow and LlamaIndex | **WP03 candidate complete — ADR-0020** |
| CORE-004 | Facility, Domain Pack, UI and plugin contribution host | Facility/Contribution/Package manifests | OpenClaw/OpenHands/MCP, Deno, ClawHub and specialist adapters | Facility/Provider WP04 complete; Domain/UI/Package WPs pending |
| CORE-005 | Node Protocol, capabilities and placement input | Node/Capability/Resource/Dispatch | OpenClaw, provider agents, NATS, OTel and runtime inventory | **WP04 candidate complete — ADR-0021; placement WP11 pending** |
| RELAY-001 | Live Events | Event Fabric | NATS/JetStream, OTel and internal bridge/outbox | **WP02 Event contract complete** |
| RELAY-002 | Durable recovery | Activity Ledger/checkpoints/Receipts | Temporal, SQL, provider snapshots and internal workflows | **Activity WP02 and Workspace/checkpoint WP05 complete** |
| EXEC-001 | Terminal/process supervision | Process/PTY Facility and Session | OS APIs, OpenClaw, Coder, E2B/OpenHands and internal workers | Provider WP04 and neutral Session/recovery WP05 complete; specialist runtime WP09 pending |
| EXEC-002 | OCI Workspace Provider and runtime variants | Workspace/Runtime Provider | containerd/OCI, runc/crun/youki and stronger isolation | Provider WP04 and Workspace WP05 complete; isolation WP11 pending |
| EXEC-003 | Reproducible Build graph | Build Recipe/Compiled Plan/Run | BuildKit, Dagger and internal Software Builder | **WP07 active; WP01–WP06 foundations ready** |
| STORE-001–005 | Storage classes, Object storage, catalogue, hashing and recoverable copies | Content/Object/Revision/Location/Backup | local CAS, SQL, R2/S3, ORAS, rclone, restic and Drive | **WP03 Object/Location and WP06 transfer/backup complete** |
| XFER-001–003 | Upload, download and cloud/Node transfer | Transfer Request/Run/Verification | tusd, Lumi, aria2, rclone, Syncthing and browser handoff | **WP06 candidate complete — ADR-0023** |
| SYNC-001 | Online/local revisions and conflicts | Sync Relationship/Cursor/Run/Conflict | Hunter safe sync, Syncthing vectors and Object digests | **WP06 candidate complete — ADR-0023** |
| DECOMP-001/002 | Detection and recursive decomposition | Detector and Domain Pack contracts | Tika, libarchive, Binwalk, LIEF, ffprobe and libvips | Object/decomposition ready; Domain Pack WP08 pending |
| DOC-001 | Document structure/render/proof | Document Domain Pack | Document Generator, Tika, Unstructured and renderers | Object/View/Artifact ready; WP08 pending |
| MEDIA-001 | Video/audio | Media Domain Pack | Creative Studio and FFmpeg/ffprobe | Object/View/Derivative ready; WP08 pending |
| IMAGE-001 | Image processing | Image Domain Pack | Creative Studio and libvips | Object/View/Derivative ready; WP08 pending |
| BIN-001 | Executable/binary decomposition | Binary Domain Pack | App Recover, LIEF and Binwalk | Object/decomposition ready; WP08 pending |
| APP-001 | APK/AAB/DEX decomposition | Android Application Domain Pack | APK Extractor, Apktool and JADX | Object/decomposition ready; WP08 pending |
| FW-001–006 | Firmware families | Firmware Domain Packs and Device adapters | internal evidence plus platform/vendor tools | WP08 pending |
| FS-001 | Disks/partitions/filesystems | Disk/Image/Filesystem Packs | libfdisk, libguestfs and platform image machinery | WP08 pending |
| DEVICE-001/002 | Android inventory/control/display/input/semantic UI | Device Provider/Session/Screen Context | Device Manager, MIBU, STF, platform-tools, scrcpy and Appium | Provider/Session foundations ready; WP08/WP09 pending |
| APP-002–004 | Linux/Windows/macOS/iOS runtime and semantics | Application Provider/Session/Window/Semantic Context | native/OCI/VM providers, remote display and platform automation | Provider/Session foundations ready; WP09 pending |
| BROWSE-001–003 | Persistent browser, retrieval and evidence | Browser Provider/Profile/Context/Page/Evidence | Playwright, Browser-Use, TurboWebFetch and Playwright MCP | Provider/Session/Object foundations ready; WP09 pending |
| UI-001/002 | Human Workspace shell, Activity Centre and review | Shell/Panel/Layout and evidence projections | Theia, Dockview, xterm.js and internal UI evidence | Workspace/Session WP05 complete; UI contracts WP09 pending |
| SEARCH-001 | Unified source-grounded search | Knowledge Source/Index/Query/Result/Citation | Hunter, LlamaIndex, RAGFlow and Browser Facility | WP10 pending; Object/Revision/Relationship ready |
| DATA-001 | Structured analytical data | Dataset/Table/Query/Transformation/Result | Polars, DuckDB, Object/Artifact and Activity runtime | WP10 pending |
| PLUGIN-001 | Package/plugin lifecycle | Package/Release/Installed Plugin/Activation | ClawHub, OpenClaw, MCP, Deno, provenance and isolation | WP10/WP11 pending; Artifact Release and Facility/Provider ready |
| ISOLATION-001 | Runtime isolation classes | Isolation Class/Runtime Provider/Secure Grant | OCI, gVisor, Kata, Firecracker and full VM | Provider foundation complete; WP11 pending |
| DIST-001 | Capability, placement, reservation, lease and distributed execution | Capability Snapshot/Placement/Lease/Fence | Node/Activity, Ray, transfer and runtime classes | Node/runtime WP04 complete; placement WP11 pending |
| SEC-001 | Authorized assessment and Finding lifecycle | Security Authorization/Finding/Verification | Semgrep, Syft, Grype, Trivy, GUAC, ZAP and Strix | WP12 pending; Activity/Object/Artifact/Provider evidence ready |
| REPRO-001 | Frozen protocol and reproduction | Protocol/Reproduction Run/Claim/Evidence Card | ReproZip, ClaimBound, SparkDistill and Build/Artifact machinery | Build-side reproduction WP07 active; security reproduction WP12 pending |
| SESSION-001 | Checkpoint/archive/export/import/resume | Workspace Session/Checkpoint Bundle/Restore | Workspace, storage, VM, Device, Browser, Shell and runtime checkpoints | **WP05 candidate complete — ADR-0022** |
| OBS-001 | Logs/metrics/traces/resource accounting | OTel conventions and resource projections | OTel plus all runtime/evidence systems | Event/Receipt and Node/Provider health/resource contracts ready; later domain mappings pending |
| PROV-001 | Provenance/signing/proof bundles | Provenance/Verification graph | Witness, in-toto, Sigstore, ORAS, Syft and runtime evidence | **WP07 active** |
| OFFLINE-001 | Intermittent Node operation | journal/outbox, generations and reconciliation | Event Fabric, revisions, generations and local-first providers | Activity/Node/Workspace journal and transfer/sync contracts complete; executable proof pending |

---

# Phase 0B candidate closure

## WP01 — Common identity/versioning — CANDIDATE COMPLETE

Evidence:

- `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`
- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`

Closed foundations:

- UUIDv7 plus registered entity kinds;
- scoped Aliases and Entity Envelope;
- typed families and namespaced state machines;
- directional compatibility/migration;
- privacy/retention/tombstone rules.

## WP02 — Activity/Event/Receipt/proof — CANDIDATE COMPLETE

Evidence:

- `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`
- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`

Closed foundations:

- Activity Request, Activity, Operation and Attempt separation;
- dependency, cancellation/manual requests and retry semantics;
- Event/telemetry versus immutable Receipts;
- bounded proof domains and explicit reconciliation;
- Review/Verdict/external-result separation.

## WP03 — Object/Artifact/storage — CANDIDATE COMPLETE

Evidence:

- `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`
- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`

Closed foundations:

- Content versus Object versus immutable Revision;
- plural hash/detector observations and Relationship revisions;
- child/View/Preview/Derivative and decomposition coverage;
- Artifact promotion versus immutable Release;
- Location lifecycle/health/verification and retention-safe deletion.

## WP04 — Node/Facility/Provider/capability/health — CANDIDATE COMPLETE

Evidence:

- `decisions/ADR-0021-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH-BOUNDARY.md`
- `decisions/ADR-0021B-WP04-FINAL-CATALOG-CORRECTION.md`
- `schemas/phase-0b/runtime/schema-catalog.v0.1.2.json`

Closed foundations:

- stable Node identity, enrollment/trust, generation and epoch;
- immutable capability/resource observations and freshness;
- Capability Definition/Claim/Verification/Availability separation;
- Facility/Provider definitions, revisions, instances and locality;
- lifecycle/readiness/health/pressure separation;
- generation fencing and expiring Dispatch Eligibility.

## WP05 — Workspace/Session/checkpoint/recovery — CANDIDATE COMPLETE

Evidence:

- `decisions/ADR-0022-WORKSPACE-SESSION-CHECKPOINT-RESTORE-RECOVERY-BOUNDARY.md`
- `schemas/phase-0b/workspace/schema-catalog.v0.1.0.json`
- `work-packages/PHASE-0B-WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY.md`

Closed foundations:

- Workspace/Revision/Membership/Binding/Materialization separation;
- Session/Attachment/control separation;
- journal/cursor reconstruction and generation fencing;
- Checkpoint Request/Component/Bundle/Verification separation;
- compatibility-before-mutation and new-generation Restore Runs;
- runtime restore versus Recovery Verification;
- explicit Export/Import identity, privacy and authority decisions.

## WP06 — Transfer/Sync/Conflict/Backup — CANDIDATE COMPLETE

Evidence:

- `decisions/ADR-0023-TRANSFER-SYNC-CONFLICT-BACKUP-RESTORE-BOUNDARY.md`
- `schemas/phase-0b/transfer/schema-catalog.v0.1.0.json`
- `work-packages/PHASE-0B-WP06-TRANSFER-SYNC-CONFLICT-BACKUP.md`

Closed foundations:

- logical Transfer versus physical Attempts/progress/verification;
- safe resume and Content/Object/Location acceptance;
- Sync Relationship/Cursor/Run/Conflict/Resolution separation;
- Backup Policy/Snapshot/Verification/Prune/Restore separation;
- sync/replica/checkpoint/export/backup distinction;
- storage restore versus Workspace/application recovery.

---

# Active Phase 0B package

## 0B-WP07 — Recipe, Build, provenance, SBOM, signature and verification

Resolve:

- Build Recipe identity, immutable revision/hash and detector proposal/acceptance;
- requested targets, platform/toolchain/Facility/environment/service/network requirements;
- Recipe versus backend Compiled Plan and capability alterations;
- Build Run and exact step-to-Activity/Operation/Attempt mapping;
- cache identity, reuse verification and volatile-input reproducibility impact;
- secret/credential access, redaction, cleanup and output-contamination boundaries;
- output declaration versus Object creation, Artifact promotion and Release;
- SBOM/package observations, generator identity, scope and coverage limitations;
- attestation production, materials/products and policy verification;
- signature/trust-root/certificate/transparency/offline verification;
- Build/export/SBOM/attestation/signing/review/reproduction/acceptance separation;
- independent reproduction and byte-identical/functional-equivalence comparison;
- partial failure, migration, fixtures, safety net and backend replacement;
- ADR-0024 only if the reviewed candidate boundary is accepted.

No runtime implementation, production dependency selection, signing infrastructure or donor-source reuse is authorized.

---

# Cross-requirement consistency verdict

**PASS.** No design-blocking contradiction has been found.

Frozen normalization rules remain active:

- Content, Object, Revision, Artifact and Location remain separate.
- Workspace, Revision, Materialization, Session and Attachment remain separate.
- Activity, Operation and Attempt remain separate.
- Event, telemetry, Receipt, Evidence, Review and authoritative result remain separate.
- Recipe, Plan, Protocol and Run remain separate.
- Transfer, Sync, Conflict, Backup and Restore remain separate.
- Node, Facility, Provider, Session, Lease, Event, Revision and Snapshot are typed families.
- lifecycle, reachability, readiness, health, capability availability and pressure remain separate.
- `completed`, `verified`, `ready`, `recovered` and `accepted` remain distinct.
- capability, permission, authorization, placement, reservation and execution authority remain distinct.
- audience/privacy/redaction/retention travel with exportable records.

---

# Parked and restricted items

None block Phase 0B contract design. Detailed reopening criteria remain in `DONOR_RECOVERY.md` and the Phase 0A consistency review.

The final public Ptah project licence remains a Phase 0C gate because no implementation is distributed yet.
