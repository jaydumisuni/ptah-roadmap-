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
- [x] ADR-0005 Build Recipe / Artifact / Provenance boundary.
- [x] ADR-0006 Storage / Transfer / Sync / Backup boundary.
- [-] Normalize full donor register and all internal overlap.
- [-] Save after every meaningful inspection unit.

## Core-runtime cluster

- [x] OpenClaw and Daytona boundary pass.
- [x] Coder, E2B/Desktop, Dev Containers/CLI and DevPod.
- [x] containerd and OCI specifications.
- [x] OpenHands runtime family.
- [x] Temporal, NATS/JetStream and OpenTelemetry.
- [x] Hunter AgentOps, Foreman, Sergeant, Relay, Software Builder, CodeOps, MIBU and Hunter runtime/sync/outbox.
- [x] WP02A, WP02B and WP02C records.
- [x] Core-runtime Phase 0B design closure.

## WP03 — Build, Artifact and provenance composition

- [x] Internal Software Builder comparison.
- [x] BuildKit.
- [x] Dagger.
- [x] ORAS and OCI Artifact/referrer relationships.
- [x] Witness.
- [x] in-toto.
- [x] Cosign, Rekor, Fulcio and sigstore-go.
- [x] Syft/SBOM machinery.
- [x] Composite WP03 record.
- [x] ADR-0005.
- [x] Build/Artifact/Provenance Phase 0B design closure.

## WP04 — Storage, transfer, synchronization and backup

- [x] Recover internal Download Manager/Lumi implementation.
- [x] aria2.
- [x] tus/tusd.
- [x] rclone.
- [x] Syncthing.
- [x] restic.
- [x] Hunter R2/D1/local/Drive storage comparison.
- [x] Local content-addressed storage and metadata catalogue direction.
- [x] Online/local Object revision and conflict model.
- [x] Future shared-filesystem decision: JuiceFS/SeaweedFS evaluated and parked.
- [x] Composite Storage/Transfer/Sync work-package record.
- [x] ADR-0006.
- [x] Storage/Transfer/Sync/Backup Phase 0B design closure.

## Active WP05 — Universal Object and decomposition composition

- [-] Recover internal App Recover.
- [ ] Recover internal APK Extractor.
- [ ] Recover internal Creative Studio/media asset handling.
- [ ] Recover internal Document Generator/rendering.
- [ ] libarchive.
- [ ] Apache Tika.
- [ ] Unstructured.
- [ ] LIEF.
- [ ] Binwalk.
- [ ] JADX.
- [ ] Apktool.
- [ ] libvips.
- [ ] FFmpeg/ffprobe.
- [ ] Tree-sitter/source structure only where needed.
- [ ] Composite Object/Decomposition work-package record.
- [ ] Object Graph / Decomposition / Derivative ADR.

## Remaining donor groups

- [ ] Relevant OpenClaw organisation projects.
- [ ] Moby/Docker CLI detailed boundary.
- [ ] gVisor, Kata, Firecracker, youki and crun.
- [ ] Theia/OpenVSCode and remote-display gateway.
- [ ] Playwright, Playwright MCP, Browser-Use and TurboWebFetch.
- [ ] STF, adbkit, Appium, scrcpy, TouchPilot and internal device engines.
- [ ] Apple, MTK, Qualcomm, Unisoc, Android OTA, disk/filesystem and vendor firmware donors.
- [ ] RAGFlow, LlamaIndex, Dify, search and data donors.
- [ ] SparkDistill, ClaimBound, ReproZip, GUAC and security workloads.
- [ ] Research/documentation donor sources and unresolved profiles.

## Requirement closure

- [x] Complete v1 requirement list.
- [x] Core Workspace/Node/Activity/Event/Observability donor composition.
- [x] Core-runtime internal comparison and Phase 0B design closure.
- [x] Build/Artifact/Provenance composition and Phase 0B design closure.
- [x] Storage/Transfer/Sync/Backup composition and Phase 0B design closure.
- [-] Map all remaining requirements to internal foundations.
- [-] Map primary and completion donors.
- [-] Record native Ptah layers, licences and exit strategies.
- [-] Record complete validation sets.
- [-] Close universal Object/decomposition cluster.
- [ ] Close firmware/device/browser/UI/search/security clusters.
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
- [ ] Build Recipe and backend compilation schema.
- [ ] Cache identity/reproducibility schema.
- [ ] Object, relationship, Artifact and storage-location schemas.
- [ ] Object detection, decomposition, view and derivative schemas.
- [ ] SBOM, attestation, signature and verification schemas.
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

- [ ] Git mirrors/worktrees, local and OCI providers and Dev Containers.
- [ ] BuildKit/Dagger recipes, shared caches and parallel reproducible Build proof.

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

- [ ] Runtime receipts, replay, security workloads and independent verification proof.

# Phase 12 — Distributed Ptah

- [ ] Linux, mini-PC, Windows, macOS, GPU and device Nodes.
- [ ] Placement, secure identity, transfer, intermittent connectivity and local-first proof.

# Phase 13 — OS readiness

- [ ] Separate private OS decision, Linux/image foundation and service packaging.
- [ ] Hardware, boot, updates, encryption, recovery and offline cache proof.
