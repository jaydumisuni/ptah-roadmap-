# Ptah Requirement Closure Matrix

**Phase:** 0B contract design  
**Status:** ALL V1 REQUIREMENTS CLOSED FOR DESIGN — PHASE 0A FROZEN; WP01–WP03 CANDIDATE COMPLETE; WP04 ACTIVE

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
| CORE-001 | Persistent Workspace model | Workspace Provider | Daytona, Coder, E2B, Dev Containers, DevPod, local/OCI providers | WP05 pending; common/Activity/Object dependencies ready |
| CORE-002 | Concurrent Activity runtime | Activity Ledger | Temporal, NATS/JetStream, OTel and internal runtime/evidence systems | **WP02 candidate complete — ADR-0019** |
| CORE-003 | Universal Object graph plus knowledge/document extensions | Content/Object/Revision/Relationship/View contracts | internal recovery tools, decomposition donors, Hunter, RAGFlow and LlamaIndex | **WP03 candidate complete — ADR-0020** |
| CORE-004 | Facility, Domain Pack, UI and plugin contribution host | Facility/Contribution/Package manifests | OpenClaw/OpenHands/MCP, Deno, ClawHub and specialist adapters | WP04 active; later domain/package WPs pending |
| CORE-005 | Node Protocol, capabilities and placement input | Node/Capability Snapshot | OpenClaw, provider agents, NATS, OTel and runtime inventory | **WP04 active** |
| RELAY-001 | Live Events | Event Fabric | NATS/JetStream, OTel and internal bridge/outbox | **WP02 Event contract candidate complete** |
| RELAY-002 | Durable recovery | Activity Ledger/checkpoints/Receipts | Temporal, SQL, provider snapshots and internal workflows | Activity proof complete; Workspace/checkpoint WP05 pending |
| EXEC-001 | Terminal/process supervision | Process/PTY Facility | OS APIs, OpenClaw, Coder, E2B/OpenHands and internal workers | Facility/Provider WP04 active; Session WP05 pending |
| EXEC-002 | OCI Workspace Provider and runtime variants | OCI Provider | containerd/OCI, runc/crun/youki and stronger isolation | Provider WP04 active; isolation WP11 pending |
| EXEC-003 | Reproducible Build graph | Build Recipe/backend adapter | BuildKit, Dagger and internal Builder | WP07 pending; Activity/Object foundations ready |
| STORE-001–005 | Storage classes, Object storage, catalogue and hashing | Content/Object/Revision/Location contracts | local CAS, SQL, R2/S3, ORAS, rclone and Drive | **WP03 candidate complete for Object/Location/deletion; WP06 transfer/backup pending** |
| XFER-001–003 | Upload, download and cloud/Node transfer | Transfer Facilities | tusd, Lumi, aria2, rclone, Syncthing and browser handoff | WP06 pending; Activity/Object/Location foundations ready |
| SYNC-001 | Online/local revisions and conflicts | Revision/Conflict contracts | Hunter safe sync, Syncthing vectors and Object digests | Object Revision ready; conflict/sync WP06 pending |
| DECOMP-001/002 | Detection and recursive decomposition | Detector and Domain Pack contracts | Tika, libarchive, Binwalk, LIEF, ffprobe, libvips | Decomposition Run/relationships ready; Domain Pack WP08 pending |
| DOC-001 | Document structure/render/proof | Document Domain Pack | Document Generator, Tika, Unstructured and renderers | Object/View/Artifact ready; Domain Pack WP08 pending |
| MEDIA-001 | Video/audio | Media Domain Pack | Creative Studio and FFmpeg/ffprobe | Object/View/Derivative ready; WP08 pending |
| IMAGE-001 | Image processing | Image Domain Pack | Creative Studio and libvips | Object/View/Derivative ready; WP08 pending |
| BIN-001 | Executable/binary decomposition | Binary Domain Pack | App Recover, LIEF and Binwalk | Object/decomposition ready; WP08 pending |
| APP-001 | APK/AAB/DEX decomposition | Android Application Domain Pack | APK Extractor, Apktool and JADX | Object/decomposition ready; WP08 pending |
| FW-001–006 | Firmware families | Firmware Domain Packs and Device adapters | internal evidence plus platform/vendor tools | WP08 pending |
| FS-001 | Disks/partitions/filesystems | Disk/Image/Filesystem Packs | libfdisk, libguestfs and platform image machinery | WP08 pending |
| DEVICE-001/002 | Android inventory/control/display/input/semantic UI | Device Provider/Session/Screen Context | Device Manager, MIBU, STF, platform-tools, scrcpy, Appium | WP08/WP09 pending |
| APP-002–004 | Linux/Windows/macOS/iOS runtime and semantics | Application Provider/Session/Window/Semantic Context | native/OCI/VM providers, remote display and platform automation | WP09 pending |
| BROWSE-001–003 | Persistent browser, retrieval and evidence | Browser Provider/Profile/Context/Page/Evidence | Playwright, Browser-Use, TurboWebFetch and Playwright MCP | WP09 pending |
| UI-001/002 | Human Workspace shell, Activity Centre and review | Shell/Panel/Layout and evidence projections | Theia, Dockview, xterm.js and internal UI evidence | WP09 pending |
| SEARCH-001 | Unified source-grounded search | Knowledge Source/Index/Query/Result/Citation | Hunter, LlamaIndex, RAGFlow and Browser Facility | WP10 pending; Object/Revision/Relationship ready |
| DATA-001 | Structured analytical data | Dataset/Table/Query/Transformation/Result | Polars, DuckDB, Object/Artifact and Activity runtime | WP10 pending |
| PLUGIN-001 | Package/plugin lifecycle | Package/Release/Installed Plugin/Activation | ClawHub, OpenClaw, MCP, Deno, provenance and isolation | WP10/WP11 pending; Artifact Release ready |
| ISOLATION-001 | Runtime isolation classes | Isolation Class/Runtime Provider/Secure Grant | OCI, gVisor, Kata, Firecracker and full VM | Provider WP04 active; isolation WP11 pending |
| DIST-001 | capability, placement, reservation, lease and distributed execution | Capability Snapshot/Placement/Lease/Fence | Node/Activity, Ray, transfer and runtime classes | Node/capability WP04 active; placement WP11 pending |
| SEC-001 | Authorized assessment and Finding lifecycle | Security Authorization/Finding/Verification | Semgrep, Syft, Grype, Trivy, GUAC, ZAP and Strix | WP12 pending; Activity/Object/Artifact evidence ready |
| REPRO-001 | Frozen protocol and reproduction | Protocol/Reproduction Run/Claim/Evidence Card | ReproZip, ClaimBound, SparkDistill and Build/Artifact machinery | WP12 pending; Activity/Object/Artifact ready |
| SESSION-001 | Checkpoint/archive/export/import/resume | Session/Checkpoint Bundle | Workspace, storage, VM, Device, Browser, Shell and runtime checkpoints | WP05 pending |
| OBS-001 | Logs/metrics/traces/resource accounting | OTel conventions and resource projections | OTel plus all runtime/evidence systems | Event/Receipt ready; Node/Provider health WP04 active |
| PROV-001 | Provenance/signing/proof bundles | Provenance/Verification graph | Witness, in-toto, Sigstore, ORAS, Syft and runtime evidence | Receipt/Object/Artifact foundations ready; WP07/WP12 pending |
| OFFLINE-001 | Intermittent Node operation | local journal/outbox and reconciliation | Event Fabric, revisions, generations and local-first providers | Activity reconciliation ready; Node WP04 and Workspace WP05 pending |

---

# Phase 0B candidate closure

## WP01 — Common identity/versioning — CANDIDATE COMPLETE

Evidence:

- `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`
- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`

Closed candidate foundations:

- UUIDv7 plus registered entity kinds;
- scoped aliases;
- Entity Envelope and privacy/retention;
- typed families;
- namespaced state machines;
- directional compatibility and migration;
- tombstone separate from physical deletion.

## WP02 — Activity/Event/Receipt/proof — CANDIDATE COMPLETE

Evidence:

- `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`
- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`

Closed candidate foundations:

- Activity Request, Activity, Operation and Attempt separation;
- Dependencies, cancellation/manual requests and retries;
- Event/telemetry versus immutable Receipts;
- bounded proof domains;
- Review/Verdict/external-result separation;
- explicit reconciliation.

## WP03 — Object/Artifact/storage — CANDIDATE COMPLETE

Evidence:

- `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`
- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`

Closed candidate foundations:

- Content versus logical Object versus immutable Revision;
- authorized deduplication without logical-object merge;
- plural hash/detector observations and separate classification;
- Relationship identity plus immutable revisions;
- child/View/Preview/Derivative and decomposition coverage;
- Artifact promotion versus immutable Release;
- Location lifecycle/health/verification separation;
- retention-aware, referentially safe physical deletion.

---

# Active Phase 0B package

## 0B-WP04 — Node, Facility, Provider, capability and health

Resolve:

- stable Node identity, enrollment/trust/revocation and Node Generation;
- connection epoch and stale projection rules;
- Capability Snapshot, evidence, freshness and expiry;
- total/allocatable/reserved/used/pressure resources;
- Facility definition/version versus Facility Instance;
- Provider definition versus Provider Instance/Generation;
- Provider lifecycle versus readiness/health/degradation;
- heartbeat/liveness versus readiness/operation proof;
- compatibility ranges and optional dependency degradation;
- fencing of stale Node/Provider generations;
- local/remote Provider replacement without canonical identity loss;
- schema, migration, fixture and conformance set;
- ADR-0021 if accepted.

No runtime implementation, dependency selection or donor-source reuse is authorized.

---

# Cross-requirement consistency verdict

**PASS.** No design-blocking contradiction has been found.

Frozen normalization rules remain active:

- Content, Object, Revision, Artifact and Location remain separate.
- Activity, Operation and Attempt remain separate.
- Event, telemetry, Receipt, Evidence, Review and authoritative result remain separate.
- Observation, Claim, Finding and Verdict remain separate but linkable.
- Recipe, Plan, Protocol and Run remain separate.
- Provider, Session, Lease, Event, Revision and Snapshot are typed families.
- state machines are namespaced/versioned; `completed`, `verified` and `accepted` remain distinct.
- capability, permission, authorization, placement, reservation and execution authority remain distinct.
- audience/privacy/redaction/retention travel with exportable records.

---

# Parked and restricted items

None block Phase 0B contract design. Detailed reopening criteria remain in `DONOR_RECOVERY.md` and the Phase 0A consistency review.

The final public Ptah project licence remains a Phase 0C gate because no implementation is distributed yet.
