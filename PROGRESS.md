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
- [x] Master roadmap, Current State, progress and recovery rules.
- [x] Requirement Closure Matrix and donor/internal-record structure.
- [x] ADR-0001 through ADR-0013 accepted and indexed.
- [-] Normalize remaining donor register and unresolved profiles.
- [-] Save after every meaningful inspection unit.

## Completed clusters

### WP01–WP02 — Core runtime

- [x] Node/Workspace boundary.
- [x] Workspace/provider execution composition.
- [x] Activities, Events, recovery and observability.
- [x] Internal runtime/evidence comparison.
- [x] Phase 0B design closure.

### WP03 — Build, Artifact and provenance

- [x] BuildKit/Dagger and internal Builder comparison.
- [x] ORAS, SBOM, attestation, signing and reproduction boundaries.
- [x] ADR-0005 and WP03.
- [x] Phase 0B design closure.

### WP04 — Storage, transfer, synchronization and backup

- [x] Lumi, aria2, tusd, rclone, Syncthing and restic.
- [x] local CAS/catalogue and revision/conflict direction.
- [x] distributed shared filesystems evaluated and parked.
- [x] ADR-0006 and WP04.
- [x] Phase 0B design closure.

### WP05 — Universal Object and decomposition

- [x] internal recovery/decomposition products.
- [x] archive/document/binary/Android/image/media/source donors.
- [x] ADR-0007 and WP05.
- [x] Phase 0B design closure.

### WP06 — Firmware, disks and filesystems

- [x] Apple, MTK, Qualcomm, Unisoc, Android OTA and Samsung composition.
- [x] libguestfs/libfdisk and isolated disk/filesystem boundary.
- [x] P5C parked with reopening criteria.
- [x] ADR-0008 and WP06.
- [x] Phase 0B design closure.

### WP07 — Device and Application Runtime

- [x] Android Device Provider, ADB/Fastboot, display/input and semantic UI.
- [x] Linux, Windows, macOS and iOS Application Providers.
- [x] remote display, VM, Window and Application Session boundaries.
- [x] ADR-0009, ADR-0010, WP07A and WP07B.
- [x] Phase 0B design closure.

### WP08 — Browser and Live Research

- [x] Playwright, Playwright MCP, Browser-Use and TurboWebFetch.
- [x] Profile/Process/Context/Page/Download/Evidence model.
- [x] source/citation and challenge/human-completion model.
- [x] ADR-0011 and WP08.
- [x] Phase 0B design closure.

### WP09 — Human Workspace Shell and Operator Interface

- [x] Eclipse Theia.
- [x] OpenVSCode Server and code-server compatibility paths.
- [x] xterm.js terminal renderer.
- [x] Dockview responsive layout candidate.
- [x] internal Hunter/Sergeant/MIBU/Device Manager/website UI patterns.
- [x] Ptah Home, Workspace switcher and Panel contract direction.
- [x] Activity Centre, Evidence Explorer and exact lifecycle/proof labels.
- [x] human/automation focus and fenced control handoff.
- [x] responsive desktop/tablet/phone and accessibility direction.
- [x] ADR-0012 and WP09.
- [x] Human Workspace/UI Phase 0B design closure.

### WP10 — Knowledge, Data, Search and Plugin Composition

- [x] Internal Hunter knowledge/memory/learning/search/provider foundations.
- [x] RAGFlow end-to-end ingestion/retrieval platform donor.
- [x] LlamaIndex modular connector/ingestion/retrieval donor.
- [x] Dify workflow/application/plugin patterns and licence boundary.
- [x] Polars DataFrame/lazy/streaming analytical engine.
- [x] DuckDB embedded SQL analytical engine.
- [x] Deno permission-scoped lightweight tool runtime.
- [x] MCP specification and official reference-server adapter patterns.
- [x] OpenClaw/ClawHub registry, manifest and plugin-lifecycle patterns.
- [x] Hermes Agent classified as optional caller/workload.
- [x] MiniRouter canonical repository recovered and moved to later routing evaluation; licence unresolved.
- [x] Knowledge Source/Corpus/Document/Chunk and Index Revision model.
- [x] ingestion, freshness, deletion, tombstone and reconciliation model.
- [x] Query/Result/Citation and exact source-grounding boundary.
- [x] search across Objects, Activities, Artifacts, Workspaces and external sources.
- [x] Dataset/Table/Schema/Data Query/Transformation/Result direction.
- [x] Package/Release/Installed Plugin/Activation lifecycle.
- [x] provider-neutral model/data adapter and external-reasoning boundary.
- [x] ADR-0013 and composite WP10 record.
- [x] Knowledge/Data/Search/Plugin Phase 0B design closure.

## Active WP11 — Strong Isolation and Distributed Placement/Scheduling

- [x] gVisor userspace application-kernel/`runsc` isolation donor first pass.
- [-] Kata Containers.
- [ ] Firecracker.
- [ ] youki.
- [ ] crun.
- [ ] Ray.
- [ ] isolation-class and escalation model.
- [ ] Node/provider capability and resource snapshots.
- [ ] placement, reservation, lease and fencing model.
- [ ] secure networking and credential-delivery boundary.
- [ ] interruption, rescheduling, checkpoint and recovery behavior.
- [ ] local one-Node fallback versus multi-Node placement.
- [ ] cost, locality, data-gravity and accelerator-aware scheduling.
- [ ] MiniRouter only as a routing/evaluation workload, not Core.
- [ ] composite WP11 record.
- [ ] isolation/placement/scheduling ADR.
- [ ] Isolation/Distributed Placement Phase 0B design closure.

## Remaining donor groups

- [ ] Linux AT-SPI semantic completion.
- [ ] Reproduction/security workloads and scanners.
- [ ] research/documentation sources and unresolved profiles.

## Requirement closure

- [x] Core runtime.
- [x] Build/Artifact/Provenance.
- [x] Storage/Transfer/Sync/Backup.
- [x] Object/Decomposition.
- [x] Firmware/Disk/Filesystem.
- [x] Device/Application Runtime.
- [x] Browser/Live Research.
- [x] Human Workspace/UI.
- [x] Knowledge/Data/Search/Plugin.
- [-] Isolation/Distributed placement.
- [ ] Security/reproduction workloads.
- [ ] Phase 0A review and freeze.

---

# Phase 0B — Contracts, migrations and proof design

**Status:** NOT STARTED

- [ ] Node, Workspace, Activity, Event and Facility schemas.
- [ ] Operation Receipt and proof schemas.
- [ ] Object, View, storage, revision and transfer schemas.
- [ ] Build, Artifact and provenance schemas.
- [ ] firmware, disk and Device schemas.
- [ ] Application, Window, display and semantic-context schemas.
- [ ] Browser Profile/Context/Page/evidence schemas.
- [ ] Shell, Panel, Layout and human-control schemas.
- [ ] Knowledge Source, Corpus, Index, Query, citation, data and plugin schemas.
- [ ] Session, checkpoint, credential and privacy schemas.
- [ ] isolation, placement, scheduler and secure-network schemas.
- [ ] telemetry conventions and resource accounting.
- [ ] versioning, migrations, golden corpus and failure proofs.
- [ ] Review and freeze.

# Phase 0C — First vertical slice approval

- [ ] Select Linux host and exact components.
- [ ] Approve dependency/source layout and proof plan.
- [ ] Record implementation authorization in `CURRENT_STATE.md`.

# Implementation phases

- [ ] Phase 1 — Concurrent one-Node substrate.
- [ ] Phase 2 — Intake and transfer.
- [ ] Phase 3 — Universal decomposition.
- [ ] Phase 4 — Firmware, disks and filesystems.
- [ ] Phase 5 — Git, containers, environments and Builds.
- [ ] Phase 6 — Browser and live web.
- [ ] Phase 7 — Human Workspace shell.
- [ ] Phase 8 — Session Vault.
- [ ] Phase 9 — Applications and devices.
- [ ] Phase 10 — Knowledge, data, search, recipes and plugins.
- [ ] Phase 11 — Provenance and security workloads.
- [ ] Phase 12 — Distributed Ptah.
- [ ] Phase 13 — OS readiness.
