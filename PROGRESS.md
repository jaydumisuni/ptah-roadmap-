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
- [x] Requirement Closure Matrix and donor/internal-record structure.
- [x] ADR-0001 Node Protocol / Workspace Provider boundary.
- [x] ADR-0002 Composite Donor Closure method.
- [x] ADR-0003 Activity / Event / Observability boundary.
- [x] ADR-0004 Operation Identity / Receipts / Proof Levels.
- [-] Normalize full donor register and all internal overlap.
- [-] Save after every meaningful inspection unit.

## Core-runtime requirement cluster

### External composition

- [x] OpenClaw and Daytona boundary pass.
- [x] Coder, E2B/Desktop, Dev Containers/CLI and DevPod.
- [x] containerd and OCI specifications.
- [x] OpenHands runtime family.
- [x] Temporal Server and Rust/Core SDK.
- [x] NATS Server, JetStream and `async-nats`.
- [x] OpenTelemetry Collector, Contrib and specification.
- [x] WP02A and WP02B composition records.

### Internal recovery

- [x] Hunter AgentOps operation/evidence ownership.
- [x] Hunter Foreman task, bridge, health and proof patterns.
- [x] Sergeant mission, Facility-manifest and grounded-evidence patterns.
- [x] TechGuy Relay registration/heartbeat/TTL experiment and limits.
- [x] Software Builder shared-environment, scanner/planner and worker requirements.
- [x] Hunter CodeOps routing, credential, edit, backup and review-loop patterns.
- [x] MIBU nonce, proof-protocol, stale-result and device-state patterns.
- [x] Hunter source/local sync, Task Runner, persistent Workflow Manager, local file/process bridge and D1 outbox.
- [x] Compare internal evidence against WP02A/WP02B.
- [x] Save WP02C internal core-runtime closure record.
- [x] Core-runtime Phase 0B design-closure verdict.

## Active WP03 — Build, Artifact and provenance composition

- [-] BuildKit.
- [ ] Dagger.
- [x] Internal Software Builder first-pass recovery.
- [ ] ORAS and OCI Artifact/referrer relationships.
- [ ] Witness.
- [ ] in-toto and specifications.
- [ ] Cosign, Rekor, Fulcio and Sigstore.
- [ ] Syft/SBOM machinery where required.
- [ ] Composite Build/Artifact/Provenance work-package record.
- [ ] Build Recipe / Artifact / Attestation ADR.

## Remaining donor groups

- [ ] Relevant OpenClaw organisation projects.
- [ ] Moby/Docker CLI detailed boundary.
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
- [x] Core Workspace/Node/Activity/Event/Observability donor composition.
- [x] Core-runtime internal comparison and Phase 0B design closure.
- [-] Map all remaining requirements to internal foundations.
- [-] Map primary and completion donors.
- [-] Record native Ptah layers, licences and exit strategies.
- [-] Record complete validation sets.
- [ ] Close build/provenance cluster.
- [ ] Close transfer/storage cluster.
- [ ] Close decomposition/firmware/device/browser/UI/search/security clusters.
- [ ] Review and freeze Phase 0A.

---

# Phase 0B — Contracts, migrations and proof design

**Status:** NOT STARTED

- [ ] Node identity, epoch and capability schema.
- [ ] Workspace Provider contract and conformance schema.
- [ ] Activity Ledger, retries, dependency and backend-reference schema.
- [ ] Event envelope, retention, replay and local-journal contracts.
- [ ] Operation receipt, proof level and authority schema.
- [ ] Facility manifest/invocation/result schema.
- [ ] Object, relationship, Artifact and provenance schemas.
- [ ] Session, snapshot, credential, sync and conflict schemas.
- [ ] Large-stream reference contracts.
- [ ] Telemetry semantic conventions and resource accounting.
- [ ] Firmware/Domain Pack schemas.
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
- [ ] Typed recipes, shared caches, provenance and parallel reproducible build proof.

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
