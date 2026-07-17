# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — CORE RUNTIME AND BUILD/PROVENANCE CLOSED FOR DESIGN

This file maps each Ptah requirement to internal evidence, a composite donor set, mature machinery, native Ptah ownership, licence/exit decisions and proof.

A requirement is never closed by naming one repository. Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

Status values:

- `OPEN`
- `RECOVERING INTERNAL WORK`
- `INSPECTING DONORS`
- `COMPOSITE CANDIDATE`
- `LICENCE REVIEW`
- `VALIDATION REQUIRED`
- `CLOSED FOR DESIGN`
- `REJECTED PATH`
- `PARKED`

---

# Requirements closed for Phase 0B contract design

Design closure does **not** authorize implementation. Phase 0B schemas/conformance and Phase 0C slice approval remain mandatory.

| ID | Requirement | Native Ptah owner | Composite machinery/evidence | Phase 0B focus | Evidence |
|---|---|---|---|---|---|
| CORE-001 | Persistent Workspace model | Workspace Provider contract | Daytona, Coder, E2B, Dev Containers/CLI, DevPod, local Linux, containerd/OCI, Hunter local boundaries | lifecycle, capabilities, provider conformance, identity separation | WP02A/WP02C, ADR-0001 |
| CORE-002 | Concurrent Activity runtime | Activity contract and Ledger | Temporal, NATS/JetStream, OTel, internal AgentOps/Foreman/Hunter workers/outbox/MIBU | states, leases/fencing, retries, cancellation, checkpoints, receipts, backend migration | WP02B/WP02C, ADR-0003/0004 |
| CORE-004 | Facility/plugin host foundation | Facility Manifest/host/invocation | OpenClaw plugins, OpenHands tools, MCP, Sergeant manifests, CodeOps routes, AgentOps packets | capability/version/status/resources/permissions/health/pin/upgrade/rollback | WP02C |
| CORE-005 | Node Protocol/capabilities | Node Protocol | OpenClaw, Coder/DevPod agents, NATS, OTel, TechGuy Relay lessons, MIBU epochs/correlation | cryptographic identity, epoch, replay, capabilities, pairing and streams | ADR-0001/0003/0004 |
| RELAY-001 | Live Event transport | Event envelope/Fabric adapter | NATS Core, JetStream, OTel, Foreman bridge, Hunter outbox, MIBU stale rejection | sequence/cursor, retention, duplicate handling, backpressure and local outbox | WP02B/WP02C |
| RELAY-002 | Durable Activity recovery | Activity Ledger/checkpoints/receipts | Temporal, SQL, provider snapshots, Hunter Workflow/outbox and MIBU proof | retry classes, idempotency, compensation, leases/fencing and backend portability | WP02B/WP02C |
| EXEC-001 | Terminal/process supervision | Process/PTY Facility | OS APIs, OpenClaw detach/replay, Coder agent, E2B/OpenHands, internal subprocess/worker patterns | stream identity, process lifecycle, cancellation, resource accounting and recovery | WP02A/WP02C |
| EXEC-002 | OCI/container Workspace Provider | OCI Provider | containerd/OCI, Daytona lifecycle, Dev Containers/CLI, DevPod, E2B/Coder, internal shared-cache rules | lifecycle mapping, ports, storage, restart reconciliation and capability limits | WP02A/WP02C |
| SESSION-001 core | Checkpoint/archive/resume relationship | Session manifest | Workspace donors, containerd, Temporal, Hunter checkpoints/retry-of/resume-of, CodeOps backups, MIBU late status | references to provider snapshots, Objects, Activities, apps/terminals and compatibility | WP02C; storage/sync remains WP04 |
| OBS-001 | Logs/metrics/traces/resource accounting | OTel semantic conventions and receipt links | OTel/Collector, internal health/audit/proof/outbox attempts | correlation, redaction, buffering, resource accounting and proof classes | WP02B/WP02C |
| OFFLINE-001 core | Intermittent Node journal/reconciliation | local Node journal/outbox | NATS/JetStream, Activity Ledger, Hunter safe sync/outbox, MIBU late result | authority, acknowledgements, revision/conflict records and Object links | ADR-0003/0004; transport/sync remains WP04 |
| EXEC-003 | Reproducible Build graph | Build Recipe and backend compilation record | BuildKit, Dagger, internal Software Builder, containerd/OCI | recipes, step mapping, cache identity, secret refs, native backend support | WP03, ADR-0005 |
| PROV-001 | Provenance/signing/proof bundles | Provenance/Verification graph | Witness, in-toto, Sigstore/Cosign/Fulcio/Rekor, ORAS, Syft, internal receipts | SBOM, attestation, signature, trust, policy, review and reproduction records | WP03, ADR-0005 |

## Build-side closure notes

- `STORE-002` has a closed **Artifact storage/backend abstraction direction**, but general Object retention/backup remains WP04.
- `STORE-004` has a closed **immutable digest/cache/proof direction**, but upload/download hashing, chunking and repair remain WP04.
- `CORE-003` has closed Build Artifact relationship requirements, but the universal Object graph still requires decomposition/storage donor groups.
- `PLUGIN-001` has closed Build module/adapter requirements, but general discovery/install/upgrade remains later.

---

# Active WP04 — Storage, transfer, synchronization and backup

## STORE-001 — Hot local Workspace storage

**Status:** INSPECTING DONORS

- Internal foundation: Software Builder clean-Project/shared-cache rules; Hunter rooted local files and explicit authority domains.
- Current direction: Linux filesystem/volumes, containerd snapshots and native storage classes.
- Native gap: active/project/cache/temp/volume classes, mount references, pressure/health and cache truth rules.
- Proof: concurrent I/O, restart persistence, pressure handling and no object-store-as-live-build-filesystem behavior.

## STORE-002 — Durable Object/Artifact storage

**Status:** COMPOSITE CANDIDATE — WP04 COMPLETION REQUIRED

- Closed Build direction: Ptah Object/Artifact catalogue with local/R2-S3/OCI/Drive locations; ORAS for suitable OCI Artifacts.
- Internal evidence: Hunter D1-authoritative metadata and temporary R2 lifecycle.
- Open: retention, multipart/resumable transfer, replication, health/repair, backup and general non-Build Objects.
- Exit: no storage backend is canonical identity.

## STORE-003 — Metadata catalogue

**Status:** COMPOSITE CANDIDATE

- Direction: SQLite local, shared SQL and versioned migrations.
- Internal evidence: Hunter D1 idempotency/outbox/attempt schema; local JSON limitations.
- Open: transactional Object/relationship/revision graph, local journal, synchronization and conflict projections.

## STORE-004 — Content hashing and deduplication

**Status:** COMPOSITE CANDIDATE — WP04 COMPLETION REQUIRED

- Closed Build direction: immutable content digests, cache records, ORAS/OCI descriptor identity and checksum proof.
- Open: streaming hash during intake, chunk identity, partial verification, cross-location dedupe and integrity repair.

## STORE-005 — Drive export and recovery

**Status:** INSPECTING DONORS

- Direction: rclone/Drive adapter plus Session export manifest.
- Rule: Drive is readable export/recovery, never the active Build/DB/container filesystem.

## XFER-001 — Resumable uploads

**Status:** INSPECTING DONORS

- Direction: tus/tusd or compatible resumable protocol plus Object registration, hash and storage-location receipts.

## XFER-002 — Fast resumable downloads

**Status:** RECOVERING INTERNAL WORK

- Direction: internal Download Manager/Lumi plus aria2 and native queue/Object landing.
- Required: segmented/multi-source, partial-file preservation, checksums, browser handoff, background progress and restart recovery.

## XFER-003 — Cloud and Node transport

**Status:** INSPECTING DONORS

- Direction: rclone, Syncthing and dedicated Node/Object streams.
- Native gap: Object-aware transfer, dedupe, authority/revision identity and conflict-safe reconciliation.

## SYNC-001 — Online/local synchronization and conflicts

**Status:** INSPECTING DONORS

- Internal evidence: Hunter status-first fast-forward source sync, local/online authority separation and D1 outbox.
- Direction: content-addressed immutable Objects plus explicit mutable revisions/conflicts; Syncthing/rclone are transports, not merge authority.

---

# Other requirements still open or recovering

| ID | Requirement | Status | Current direction |
|---|---|---|---|
| CORE-003 | Universal Object graph/catalogue | RECOVERING INTERNAL WORK | App Recover, APK Extractor, Creative Studio, Tika/libarchive/LIEF, storage WP04 and native relationships |
| GIT-001 | Mirrors/worktrees/refs | OPEN | Git plus internal ecosystem and Workspace patterns |
| EXEC-004 | Stronger isolation | OPEN | gVisor, Kata, Firecracker and alternate OCI runtimes |
| BROWSE-001 | Persistent interactive browser | OPEN | Playwright/Chromium, Browser-Use and TurboWebFetch |
| BROWSE-002 | Rendered extraction/research | OPEN | TurboWebFetch + Playwright + source provenance |
| BROWSE-003 | Browser evidence | OPEN | screenshots, recordings, traces, console/network Artifacts |
| DECOMP-001 | True-type detection | OPEN | Tika, magic/signatures and confidence routing |
| DECOMP-002 | Recursive archive decomposition | OPEN | libarchive + extraction budgets + Object graph |
| DOC-001 | Document structure/render/proof | OPEN | internal generator, Tika/Unstructured and renderers |
| MEDIA-001 | Video/audio | OPEN | Creative Studio + FFmpeg |
| IMAGE-001 | Image processing | OPEN | Creative Studio + libvips |
| BIN-001 | Executable decomposition | OPEN | App Recover + LIEF |
| APP-001 | APK/AAB/DEX decomposition | OPEN | APK Extractor + JADX/Apktool |
| FW-001 | Apple firmware | OPEN | internal Apple work + blacktop/ipsw |
| FW-002 | MediaTek firmware | RECOVERING INTERNAL WORK | internal MTK/META + MTKClient |
| FW-003 | Unisoc firmware | RECOVERING INTERNAL WORK | internal SPD/Unisoc + PAC/FDL donors |
| FW-004 | Qualcomm firmware | RECOVERING INTERNAL WORK | internal Qualcomm + EDL/Firehose/XML/LIEF |
| FW-005 | Android OTA/dynamic partitions | RECOVERING INTERNAL WORK | internal OTA + payload/platform tools |
| FW-006 | Other vendor/embedded firmware | OPEN | Binwalk and vendor Domain Packs |
| FS-001 | Disks, partitions, images/filesystems | OPEN | libguestfs and platform tools |
| DEVICE-001 | Android inventory/ADB | COMPOSITE CANDIDATE | Device Manager/MIBU/ADB + STF/adbkit/Appium; exact donor pass pending |
| DEVICE-002 | Android screen/input/semantic UI | OPEN | TouchPilot/STF/Appium/scrcpy/UIAutomator |
| APP-002 | Linux graphical/native app | INSPECTING DONORS | E2B Desktop + remote display/native Linux |
| APP-003 | Windows EXE/MSI runtime | OPEN | Windows Node/VM + remote display |
| APP-004 | Apple IPA/macOS runtime | OPEN | macOS/Xcode Node + Appium/Peekaboo |
| UI-001 | Human Workspace shell | OPEN | Theia + optional OpenVSCode + native panels |
| UI-002 | Activity Centre | COMPOSITE CANDIDATE | Foreman/Sergeant + OpenHands/Coder + native concurrent view |
| SEARCH-001 | Unified search/indexing | OPEN | RAGFlow/LlamaIndex + multi-domain Object index |
| DATA-001 | Structured data/database pack | OPEN | Polars/SQL + native data Objects/Activities |
| PLUGIN-001 | General plugin lifecycle | OPEN | OpenClaw/ClawHub, MCP and OCI registries |
| SEC-001 | Security workload/evidence | OPEN | Strix, Semgrep, ZAP, Trivy, Syft and Grype |
| DIST-001 | Multi-Node placement/transfer | COMPOSITE CANDIDATE | core protocol/events closed; scheduler, secure networking and Object transport open |

---

# Current conclusion

Core runtime and Build/Artifact/Provenance are closed for **Phase 0B contract design**, not implementation.

Active Phase 0A group: Storage, Transfer, Synchronization and Backup (`WP04`) as recorded in `CURRENT_STATE.md`.

Phase 0A cannot close until every v1 requirement is `CLOSED FOR DESIGN`, explicitly `PARKED`, or a `REJECTED PATH` with a replacement.
