# Ptah Progress Ledger

Tick only work backed by reviewed evidence. A source file, running proof, test, pinned commit or accepted decision must support every completed item.

Status key:

- `[ ]` Not started
- `[-]` Active
- `[?]` Blocked or unresolved
- `[x]` Completed and evidenced

---

# Phase 0A — Donor recovery and requirement closure

**Status:** ACTIVE

## Repository and method control

- [x] Create private canonical roadmap repository.
- [x] Separate private roadmap control from public implementation.
- [x] Save master roadmap, current state, recovery rules and progress ledger.
- [x] Create Requirement Closure Matrix and donor-record structure.
- [x] Accept Node Protocol / Workspace Provider boundary.
- [x] Accept composite donor closure method.
- [-] Normalize complete donor register and internal overlap.
- [-] Save work continuously after each meaningful inspection unit.

## Core runtime donor cluster

### Boundary pass

- [x] OpenClaw source-level first pass, pin, licence, limits and Node Protocol boundary.
- [x] Daytona source-level first pass, final public release, maintenance notice, licence and lifecycle boundary.

### Workspace and execution composition

- [x] Coder — persistent human workspace and workspace-agent patterns.
- [x] E2B — automation-facing sandbox API patterns.
- [x] E2B Desktop — graphical desktop/application patterns and limitations.
- [x] Development Containers Specification — portable environment standard.
- [x] Dev Container CLI — reference implementation and lockfile/lifecycle limits.
- [x] DevPod — provider portability and local/remote/cloud patterns.
- [x] containerd and OCI Runtime/Image/Distribution specifications.
- [x] OpenHands transition repo, Software Agent SDK and Agent Canvas boundaries.
- [x] Save WP02A composite closure record.
- [-] Recover internal THETECHGUY process, terminal, worker, relay and workspace patterns.

### Activities, events, recovery and observability

- [-] Temporal server and SDK/runtime boundary.
- [ ] NATS Server, JetStream and selected clients.
- [ ] OpenTelemetry Collector, Contrib and specification.
- [ ] Save Relay / Durable Activity / Observability ADR.
- [ ] Complete runtime-cluster matrix updates and validation set.

## Remaining foundation donor groups

- [ ] Relevant OpenClaw organisation projects.
- [ ] BuildKit and Dagger.
- [ ] Witness and in-toto.
- [ ] Cosign, Rekor, Fulcio and Sigstore.
- [ ] ORAS and ORAS libraries.
- [ ] Stronger isolation: gVisor, Kata, Firecracker, youki and crun.

## Workspace shell and remote applications

- [ ] Theia and optional OpenVSCode boundary.
- [ ] Guacamole or equivalent remote-display gateway.
- [ ] Additional platform-specific application-display adapters.

## Browser and live web

- [ ] Playwright.
- [ ] Playwright MCP.
- [ ] Browser-Use.
- [ ] TurboWebFetch canonical source and limits.

## Transfer, synchronization and backup

- [ ] Recover internal Download Manager implementation.
- [ ] aria2.
- [ ] tus/tusd.
- [ ] rclone.
- [ ] Syncthing.
- [ ] restic.

## Android and physical devices

- [ ] DeviceFarmer STF, adbkit, minicap and minitouch.
- [ ] Appium and UIAutomator2 driver.
- [ ] scrcpy and Android platform tools.
- [ ] TouchPilot upstream/fork relationship.
- [ ] Recover internal Device Manager, MIBU, ADB, Fastboot, MTP, META, SPD/Unisoc, Qualcomm and USB/serial work.

## Build and structured execution

- [ ] BuildKit detailed inspection.
- [ ] Dagger typed execution graph.
- [ ] Moby/Docker CLI boundary.
- [ ] Recover internal Software Builder.
- [ ] Deno tool-runtime evaluation.
- [ ] Polars structured-data evaluation.

## Universal decomposition

- [ ] libarchive.
- [ ] Apache Tika and Unstructured.
- [ ] LIEF and Binwalk.
- [ ] JADX and Apktool.
- [ ] libvips and FFmpeg/ffprobe.
- [ ] Recover internal App Recover, APK Extractor, Creative Studio and document tooling.

## Firmware, disks and filesystems

- [ ] blacktop/ipsw and Apple sources.
- [ ] MTKClient plus internal MTK/META work.
- [ ] Qualcomm EDL/Firehose plus internal Qualcomm work.
- [ ] Unisoc PAC/FDL plus internal Unisoc work.
- [ ] Android payload, sparse image and dynamic-partition tooling.
- [ ] GPT/MBR, filesystem and libguestfs tooling.
- [ ] Other vendor and embedded-firmware coverage plan.
- [?] P5C format recovery from a verified sample/tool.

## Knowledge, data and search

- [ ] RAGFlow.
- [ ] LlamaIndex.
- [ ] Dify.
- [ ] Database and structured-data pack donors.
- [ ] Search/indexing donors.

## Proof, provenance and security

- [ ] SparkDistill upstream/fork relationship.
- [ ] NeoZorK ClaimBound and replay projects.
- [ ] ReproZip and GUAC.
- [ ] Syft, Grype and Trivy.
- [ ] Semgrep and ZAP.
- [ ] Strix upstream/fork relationship.

## Research and documentation

- [ ] Awesome AI Product Management.
- [ ] tmimmanuel discovery map.
- [?] Chris Ipanaque implementation repositories.
- [?] amertoglu16.github.io source recovery.
- [ ] GitHub README Crisp Links.
- [ ] MkDocs Material, Docusaurus and Mermaid.

## Requirement closure

- [x] Create complete Ptah v1 requirement list.
- [-] Map each requirement to internal foundation.
- [-] Map primary and completion donor sets.
- [-] Record native Ptah layer and exit strategies.
- [-] Record licence decisions and exact pins.
- [-] Record validation/proof for every assembled subsystem.
- [x] Record first Node/Workspace boundary.
- [x] Record workspace/execution donor composition.
- [ ] Complete activity/event/recovery composition.
- [ ] Review and freeze Phase 0A.

---

# Phase 0B — Contracts, migrations and proof design

**Status:** NOT STARTED

- [ ] Object and relationship schemas.
- [ ] Workspace and Activity schemas.
- [ ] Artifact, Node, Facility and plugin schemas.
- [ ] Session, snapshot and credential-reference schemas.
- [ ] Telemetry and provenance schemas.
- [ ] Firmware, sync and conflict schemas.
- [ ] Event envelope and streaming contracts.
- [ ] Workspace Provider and Facility Adapter contracts.
- [ ] Schema versioning/migrations.
- [ ] Golden corpus and validation rules.
- [ ] Review and freeze Phase 0B.

---

# Phase 0C — First vertical slice approval

**Status:** NOT STARTED

- [ ] Select one Linux execution host.
- [ ] Approve exact components, dependencies and source layout.
- [ ] Approve proof plan and frozen checkpoint.
- [ ] Record implementation authorization in `CURRENT_STATE.md`.

---

# Phase 1 — Concurrent one-node substrate

- [ ] Rust Node agent and control-plane link.
- [ ] Workspace namespace and provider host.
- [ ] Object catalogue and Activity registry.
- [ ] PTY/process supervision, cancellation, detach and reconnect.
- [ ] Live event stream and resource accounting.
- [ ] Artifact registration and Facility host.
- [ ] Prove at least ten independent simultaneous activities.

# Phase 2 — Intake and transfer

- [ ] Resumable uploads/downloads and partial recovery.
- [ ] Segmented/multi-source transfers.
- [ ] Streaming hashes and deduplication.
- [ ] Object-store, Drive and node transfers.
- [ ] Transfer progress/recovery proof.

# Phase 3 — Universal decomposition

- [ ] Detection, archive, document, media, image, executable and application packs.
- [ ] Recursive Object graph and progressive derivatives.
- [ ] Mixed recursive decomposition under concurrent load.

# Phase 4 — Firmware, disks and filesystems

- [ ] Partition/disk/image/filesystem foundations.
- [ ] Apple, MediaTek, Unisoc, Qualcomm and Android OTA packs.
- [ ] Additional vendor packs and firmware comparison UI.
- [ ] Concurrent multi-family firmware proof.

# Phase 5 — Git, containers, environments and builds

- [ ] Git mirrors/worktrees.
- [ ] Local-process and OCI providers.
- [ ] Dev Container compatibility.
- [ ] BuildKit, typed recipes, shared caches and reproducible artifacts.
- [ ] Parallel build proof.

# Phase 6 — Browser and live web

- [ ] Persistent interactive Chromium and profiles.
- [ ] Playwright automation, evidence and downloads.
- [ ] Rendered extraction, warm pools and recovery.
- [ ] Multi-context concurrency proof.

# Phase 7 — Human workspace shell

- [ ] Ptah Home and project/session selection.
- [ ] Object/file explorer and editor.
- [ ] Multi-terminal, browser panels and Activity Centre.
- [ ] Transfer, storage, artifact, media, document, firmware, app and device views.
- [ ] Direct-human vertical-slice proof.

# Phase 8 — Session Vault

- [ ] Checkpoint, archive, export, import and resume.
- [ ] Object/workspace versions and snapshot references.
- [ ] Restart recovery, Drive export and online/local sync.
- [ ] Conflict model and cross-provider resume proof.

# Phase 9 — Applications and devices

- [ ] Android, Linux, Windows and Apple runtimes.
- [ ] Unified remote display and concurrent application sessions.

# Phase 10 — Knowledge, data, search, recipes and plugins

- [ ] Unified search, retrieval, database and structured-data packs.
- [ ] Deterministic recipes, service registry and plugin lifecycle.

# Phase 11 — Provenance and security evidence

- [ ] Receipts, environment/tool identity and SBOMs.
- [ ] Witness/in-toto provenance, signing and ORAS relationships.
- [ ] Replay, reproducibility and security workloads.
- [ ] Independent artifact-verification proof.

# Phase 12 — Distributed Ptah

- [ ] Multiple Linux, mini-PC, Windows, macOS, GPU and device Nodes.
- [ ] Capability placement and node-to-node Object transport.
- [ ] Secure identity, intermittent connectivity and local-first operation.
- [ ] Multi-node workspace proof.

# Phase 13 — OS readiness

- [ ] Separate private OS architecture decision.
- [ ] Select Linux/image foundation and package proven Ptah services.
- [ ] Hardware profiles, drivers, bootable image and atomic updates.
- [ ] Encryption, recovery and offline package/cache strategy.
- [ ] Prove no Ptah contract redesign is required.
