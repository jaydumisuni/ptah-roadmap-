# Ptah Progress Ledger

Tick only work backed by source inspection, pinned commits, accepted decisions, tests or live evidence.

- `[ ]` Not started
- `[-]` Active
- `[?]` Blocked/unresolved
- `[x]` Completed and evidenced

---

# Phase 0A — Donor recovery and requirement closure

**Status:** ACTIVE

## Repository and method control

- [x] Private roadmap repository and public/private separation.
- [x] Master roadmap, Current State, progress and chat-recovery rules.
- [x] Requirement Closure Matrix and donor-record structure.
- [x] ADR-0001 Node Protocol / Workspace Provider boundary.
- [x] ADR-0002 Composite Donor Closure method.
- [x] ADR-0003 Activity / Event / Observability boundary.
- [-] Normalize full donor register and internal overlap.
- [-] Save after every meaningful inspection unit.

## Core runtime external donor cluster

### Boundary and workspace/execution

- [x] OpenClaw.
- [x] Daytona.
- [x] Coder.
- [x] E2B.
- [x] E2B Desktop.
- [x] Development Containers Specification.
- [x] Dev Container CLI.
- [x] DevPod.
- [x] containerd and OCI Runtime/Image/Distribution specifications.
- [x] OpenHands runtime family.
- [x] WP02A composition record.

### Activities, events, recovery and observability

- [x] Temporal Server and Rust/Core SDK boundary.
- [x] NATS Server, JetStream and `async-nats` boundary.
- [x] OpenTelemetry Collector, Contrib and specification.
- [x] WP02B composition record.
- [x] Activity Ledger versus Temporal/NATS/OTel boundary recorded.

### Internal core-runtime recovery

- [-] Hunter/AgentOps operation and job records.
- [ ] Hunter Foreman process/task state.
- [ ] Sergeant evidence and receipts.
- [ ] TechGuy Relay registration/heartbeat lessons.
- [ ] Software Builder/background workers.
- [ ] Hunter online/local sync and failure-continuation rules.
- [ ] Existing terminal, process and browser bridges.
- [ ] MIBU correlation/stale-result/device-evidence patterns.
- [ ] CodeOps bridge and Artifact contracts.
- [ ] Compare internal evidence against WP02A/WP02B.
- [ ] Core-runtime Phase 0B closure verdict.

## Remaining donor groups

- [ ] OpenClaw organisation projects.
- [ ] BuildKit, Dagger, Moby/Docker boundaries.
- [ ] Witness, in-toto, Cosign/Sigstore and ORAS.
- [ ] gVisor, Kata, Firecracker, youki and crun.
- [ ] Theia/OpenVSCode and remote-display gateway.
- [ ] Playwright, Playwright MCP, Browser-Use and TurboWebFetch.
- [ ] aria2, tusd, rclone, Syncthing, restic and internal Download Manager.
- [ ] STF, adbkit, Appium, scrcpy, TouchPilot and internal device engines.
- [ ] Tika, Unstructured, libarchive, LIEF, Binwalk, JADX, Apktool, libvips and FFmpeg.
- [ ] Apple, MTK, Qualcomm, Unisoc, Android OTA, disk/filesystem and vendor firmware donors.
- [ ] RAGFlow, LlamaIndex, Dify, search and data donors.
- [ ] SparkDistill, ClaimBound, ReproZip, GUAC and security workloads.
- [ ] Research/documentation donor sources and unresolved profiles.

## Requirement closure

- [x] Complete v1 requirement list.
- [x] First Node/Workspace boundary.
- [x] Workspace/execution external composition.
- [x] Activity/event/observability external composition.
- [-] Map every requirement to internal foundation.
- [-] Map primary and completion donors.
- [-] Record native Ptah layer, licences and exit strategies.
- [-] Record complete validation set.
- [ ] Review and freeze Phase 0A.

---

# Phase 0B — Contracts, migrations and proof design

**Status:** NOT STARTED

- [ ] Object, relationship, Workspace and Activity schemas.
- [ ] Artifact, Node, Facility and plugin schemas.
- [ ] Session, snapshot, credential, sync and conflict schemas.
- [ ] Event envelope, large-stream and receipt contracts.
- [ ] Workspace Provider and Facility Adapter contracts.
- [ ] Telemetry semantic conventions and provenance schemas.
- [ ] Firmware schema and Domain Pack contract.
- [ ] Versioning, migrations, golden corpus and failure proofs.
- [ ] Review and freeze.

# Phase 0C — First vertical slice approval

- [ ] Select Linux host and exact components.
- [ ] Approve dependency/source layout and proof plan.
- [ ] Record implementation authorization in `CURRENT_STATE.md`.

# Phase 1 — Concurrent one-Node substrate

- [ ] Node agent, Workspace namespace, Object catalogue and Activity Ledger.
- [ ] PTY/process supervision, Event Fabric, cancellation and reconnect.
- [ ] Resource accounting, Artifact registration and Facility host.
- [ ] Prove at least ten independent simultaneous Activities.

# Phase 2 — Intake and transfer

- [ ] Resumable upload/download, partial recovery, hashing and deduplication.
- [ ] Object-store, Drive and Node transport proof.

# Phase 3 — Universal decomposition

- [ ] Detection and archive/document/media/image/executable/application packs.
- [ ] Recursive Object graph and concurrent decomposition proof.

# Phase 4 — Firmware, disks and filesystems

- [ ] Disk/filesystem foundation and Apple/MTK/Unisoc/Qualcomm/OTA packs.
- [ ] Multi-family concurrent firmware proof.

# Phase 5 — Git, containers, environments and builds

- [ ] Git mirrors/worktrees, local and OCI providers, Dev Containers and BuildKit.
- [ ] Parallel reproducible build proof.

# Phase 6 — Browser and live web

- [ ] Persistent browser, Playwright, evidence, extraction, pools and recovery.

# Phase 7 — Human Workspace shell

- [ ] Ptah Home, Object/file views, multi-terminal, browser panels and Activity Centre.
- [ ] Domain views and direct-human proof.

# Phase 8 — Session Vault

- [ ] Checkpoint, archive, export/import, versions, restart recovery and sync/conflicts.

# Phase 9 — Applications and devices

- [ ] Android, Linux, Windows and Apple runtimes with unified display.

# Phase 10 — Knowledge, data, search, recipes and plugins

- [ ] Search/retrieval, databases, data, recipes, services and plugin lifecycle.

# Phase 11 — Provenance and security evidence

- [ ] Receipts, SBOMs, attestations, signing, replay and security workloads.

# Phase 12 — Distributed Ptah

- [ ] Linux, mini-PC, Windows, macOS, GPU and device Nodes.
- [ ] Placement, secure identity, transfer, intermittent connectivity and local-first proof.

# Phase 13 — OS readiness

- [ ] Separate private OS decision, Linux/image foundation and service packaging.
- [ ] Hardware, boot, updates, encryption, recovery and offline cache proof.
