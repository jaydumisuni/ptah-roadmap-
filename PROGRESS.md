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
- [x] ADR-0007 Object Graph / Decomposition / Derivative boundary.
- [x] ADR-0008 Disk Image / Firmware Package / Physical Operation boundary.
- [x] ADR-0009 Device Session / Display / Input / Semantic UI boundary.
- [x] ADR-0010 Application Provider / Window / Display boundary.
- [x] ADR-0011 Browser Profile / Context / Page / Evidence boundary.
- [-] Normalize remaining donor register and unresolved profiles.
- [-] Save after every meaningful inspection unit.

## Completed requirement clusters

### WP01–WP02 — Core runtime

- [x] Node/Workspace boundary.
- [x] Workspace/provider execution composition.
- [x] Activities, Events, recovery and observability.
- [x] Internal AgentOps/Foreman/Sergeant/Relay/CodeOps/MIBU/Hunter recovery.
- [x] Core-runtime Phase 0B design closure.

### WP03 — Build, Artifact and provenance

- [x] Software Builder comparison.
- [x] BuildKit and Dagger.
- [x] ORAS/OCI relationships.
- [x] Witness/in-toto.
- [x] Sigstore/Cosign/Rekor/Fulcio.
- [x] Syft/SBOM.
- [x] WP03 and ADR-0005.
- [x] Phase 0B design closure.

### WP04 — Storage, transfer, synchronization and backup

- [x] Lumi/Download Manager recovery.
- [x] aria2 and tus/tusd.
- [x] rclone and Syncthing.
- [x] restic.
- [x] local CAS/catalogue direction.
- [x] revision/conflict model.
- [x] JuiceFS/SeaweedFS evaluated and parked.
- [x] WP04 and ADR-0006.
- [x] Phase 0B design closure.

### WP05 — Universal Object and decomposition

- [x] App Recover, APK Extractor, Creative Studio and Document Generator.
- [x] libarchive, Tika and Unstructured.
- [x] LIEF and Binwalk.
- [x] JADX and Apktool.
- [x] libvips and FFmpeg/ffprobe.
- [x] Tree-sitter/source-structure evaluation.
- [x] WP05 and ADR-0007.
- [x] Phase 0B design closure.

### WP06 — Firmware, disks and filesystems

- [x] Apple firmware/tool recovery and blacktop/ipsw.
- [x] MTK META and MTKClient.
- [x] Qualcomm EDL/Firehose.
- [x] Unisoc PAC/FDL.
- [x] Android OTA/payload/sparse/dynamic partition/AVB.
- [x] libguestfs and libfdisk.
- [x] Samsung and generic vendor coverage.
- [x] P5C parked with reopening criteria.
- [x] internal monorepo source-recovery gaps recorded.
- [x] WP06 and ADR-0008.
- [x] Phase 0B design closure.

### WP07A — Android Device Runtime

- [x] THETECHGUY Device Manager and MIBU runtime recovery.
- [x] DeviceFarmer STF and adbkit.
- [x] minicap and minitouch.
- [x] scrcpy.
- [x] Appium and UIAutomator2.
- [x] TouchPilot canonical repository and implementation.
- [x] official Android ADB/Fastboot boundary.
- [x] AndroidX UI Automator boundary.
- [x] ADR-0009 and WP07A.
- [x] Android Device Runtime Phase 0B design closure.

### WP07B — Desktop and Apple Application Runtime

- [x] Xpra/Xpra HTML5.
- [x] Apache Guacamole.
- [x] noVNC/websockify.
- [x] QEMU/libvirt.
- [x] FreeRDP.
- [x] FlaUI, NovaWindows and legacy WinAppDriver boundary.
- [x] Peekaboo macOS.
- [x] Appium XCUITest and IDB.
- [x] Apple Xcode/Simulator/XCTest/Virtualization foundation.
- [x] ADR-0010 and WP07B.
- [x] Device/Application Runtime Phase 0B design closure.

### WP08 — Browser and Live Research

- [x] Playwright core and cross-browser foundation.
- [x] Playwright MCP.
- [x] Browser-Use.
- [x] TurboWebFetch canonical URL and source inspection.
- [x] internal browser/download/research requirements and implementation gap.
- [x] persistent Profile and authenticated Context model.
- [x] browser process pooling and Workspace isolation direction.
- [x] Page/Frame/Popup/Download lifecycle.
- [x] screenshot, PDF, video, trace, console, network and HAR evidence.
- [x] rendered extraction, source and citation model.
- [x] browser crash/restart and stale-page rejection.
- [x] ADR-0011 and WP08.
- [x] Browser/Live Research Phase 0B design closure.

## Active WP09 — Human Workspace Shell and Operator Interface

- [-] Eclipse Theia.
- [ ] OpenVSCode Server.
- [ ] code-server compatibility path.
- [ ] xterm.js terminal surface.
- [ ] Monaco/editor integration where required.
- [ ] multi-panel/dock/layout donor decision.
- [ ] recover internal Hunter/Foreman/Sergeant/device/tool/website UI patterns.
- [ ] Ptah Home and Workspace switcher.
- [ ] Object/file/tree/search/preview views.
- [ ] multi-terminal, Browser, Device and Application panels.
- [ ] Activity Centre, evidence and proof views.
- [ ] human/automation focus and control handoff.
- [ ] responsive desktop/mobile/browser layout.
- [ ] accessibility, keyboard and reduced-motion requirements.
- [ ] honest planned/configured/connected/running/verified labels.
- [ ] composite WP09 record.
- [ ] Workspace Shell / Panel / Human Control ADR.
- [ ] Human Workspace/UI Phase 0B design closure.

## Remaining donor groups

- [ ] Remaining OpenClaw organisation projects where requirements remain.
- [ ] Moby/Docker CLI operator boundary.
- [ ] gVisor, Kata, Firecracker, youki and crun.
- [ ] Linux AT-SPI semantic completion.
- [ ] RAGFlow, LlamaIndex, Dify, Polars and data/search donors.
- [ ] MiniRouter/Ray/Celery/Huey scheduling completion.
- [ ] SparkDistill, ClaimBound, ReproZip, GUAC and security workloads.
- [ ] research/documentation sources and unresolved profiles.

## Requirement closure

- [x] Complete v1 requirement list.
- [x] Core runtime closure.
- [x] Build/Artifact/Provenance closure.
- [x] Storage/Transfer/Sync/Backup closure.
- [x] Object/Decomposition closure.
- [x] Firmware/Disk/Filesystem closure.
- [x] Device/Application Runtime closure.
- [x] Browser/Live Research closure.
- [-] Human Workspace/UI closure.
- [ ] Knowledge/Data/Search/Plugin closure.
- [ ] Isolation/Distributed placement completion.
- [ ] Security/reproduction workload closure.
- [ ] Phase 0A review and freeze.

---

# Phase 0B — Contracts, migrations and proof design

**Status:** NOT STARTED

- [ ] Node identity, epoch and capability schemas.
- [ ] Workspace Provider and conformance schemas.
- [ ] Activity Ledger, Event and local-journal schemas.
- [ ] operation receipt, proof level and authority schemas.
- [ ] Facility and Domain Pack schemas.
- [ ] Build Recipe, cache, Artifact and provenance schemas.
- [ ] Object, detection, relationship, View and derivative schemas.
- [ ] storage location, revision, conflict, transfer and backup schemas.
- [ ] firmware, disk/image and physical-operation schemas.
- [ ] Device identity, interface, lease and Device Session schemas.
- [ ] Application Object, Provider, Installation, Session, Process and Window schemas.
- [ ] Display Gateway, stream and semantic Screen Context schemas.
- [ ] Browser Profile, Process, Context, Page and evidence schemas.
- [ ] Workspace Shell, panel, layout, focus and human-control schemas.
- [ ] Session, checkpoint, credential and privacy schemas.
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
