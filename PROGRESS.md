# Ptah Progress Ledger

Tick only work backed by reviewed evidence. A source file, screenshot, running demo, test result, pinned commit, or accepted decision must support each completed item.

Status key:

- `[ ]` Not started
- `[-]` Active
- `[?]` Blocked or unresolved
- `[x]` Completed and evidenced

---

# Phase 0A — Donor recovery and requirement closure

**Status:** ACTIVE

## Repository control

- [x] Create private canonical roadmap repository.
- [x] Separate private roadmap control from public Ptah implementation.
- [x] Save canonical master roadmap.
- [x] Save current-state and chat-recovery rules.
- [x] Save tickable progress ledger.
- [-] Save and normalize the donor recovery register.

## Foundation-grade donors

- [ ] OpenClaw core and relevant organisation repositories.
- [ ] Daytona.
- [ ] Temporal and selected SDK.
- [ ] NATS Server, JetStream, and selected clients.
- [ ] containerd and OCI specifications.
- [ ] OpenTelemetry Collector and specification.
- [ ] Dagger.
- [ ] Witness.
- [ ] in-toto.
- [ ] Cosign, Rekor, Fulcio, and Sigstore.
- [ ] ORAS and ORAS Go.

## Workspace and sandbox donors

- [ ] E2B.
- [ ] E2B Desktop.
- [ ] Coder.
- [ ] OpenHands.
- [ ] Human workspace shell donors such as Theia/OpenVSCode.
- [ ] Remote application display donor such as Guacamole.

## Browser donors

- [ ] Playwright.
- [ ] Playwright MCP.
- [ ] Browser-Use.
- [ ] TurboWebFetch canonical source and implementation limits.

## Transfer, synchronization, and backup donors

- [ ] Recover internal Download Manager implementation.
- [ ] aria2.
- [ ] tus/tusd.
- [ ] rclone.
- [ ] Syncthing.
- [ ] restic.

## Android and physical-device donors

- [ ] DeviceFarmer STF.
- [ ] adbkit.
- [ ] minicap.
- [ ] minitouch.
- [ ] Appium.
- [ ] Appium UIAutomator2 driver.
- [ ] scrcpy.
- [ ] Android platform tools.
- [ ] Android UIAutomator.
- [ ] TouchPilot upstream and contributor fork relationship.
- [ ] Internal Device Manager, MIBU, ADB, Fastboot, MTP, META, SPD/Unisoc, Qualcomm, and USB/serial work.

## Build and environment donors

- [ ] BuildKit.
- [ ] Moby and Docker CLI boundaries.
- [ ] Dev Container specification and provider patterns.
- [ ] Internal Software Builder recovery.
- [ ] Deno as a possible tool runtime.
- [ ] Polars for structured activity and data processing.

## Decomposition donors

- [ ] libarchive.
- [ ] Apache Tika.
- [ ] Unstructured.
- [ ] LIEF.
- [ ] Binwalk.
- [ ] JADX.
- [ ] Apktool.
- [ ] libvips.
- [ ] FFmpeg/ffprobe.
- [ ] Internal App Recover and APK Extractor recovery.

## Firmware, disk, and filesystem donors

- [ ] blacktop/ipsw.
- [ ] MTKClient and internal MTK work.
- [ ] Qualcomm EDL/Firehose donors and internal Qualcomm work.
- [ ] Android payload extraction donors.
- [ ] Unisoc PAC/FDL donors and internal Unisoc work.
- [ ] GPT/MBR and sparse-image tooling.
- [ ] Dynamic-partition tooling.
- [ ] Filesystem adapters and libguestfs evaluation.
- [ ] Samsung, Huawei/Honor, LG, Sony, OPPO/Realme/OnePlus, embedded, and unknown-vendor coverage plan.
- [?] P5C format recovery from a real sample or verified tool.

## Knowledge and data donors

- [ ] RAGFlow.
- [ ] LlamaIndex.
- [ ] Dify.
- [ ] Database domain-pack donors.
- [ ] Search and indexing donors.

## Isolation backends

- [ ] gVisor.
- [ ] Kata Containers.
- [ ] Firecracker.
- [ ] youki.
- [ ] crun.

## Proof, provenance, and security donors

- [ ] SparkDistill upstream and fork relationship.
- [ ] NeoZorK ClaimBound and replay projects.
- [ ] ReproZip.
- [ ] GUAC.
- [ ] Syft.
- [ ] Grype.
- [ ] Trivy.
- [ ] Semgrep.
- [ ] ZAP.
- [ ] Strix upstream and contributor fork relationship.

## Research and documentation sources

- [ ] Awesome AI Product Management.
- [ ] tmimmanuel discovery map.
- [?] Chris Ipanaque implementation repositories.
- [?] amertoglu16.github.io source recovery.
- [ ] GitHub README Crisp Links.
- [ ] MkDocs Material.
- [ ] Docusaurus.
- [ ] Mermaid.

## Requirement closure

- [ ] Create complete Ptah v1 requirement list.
- [ ] Map each requirement to internal evidence.
- [ ] Map each requirement to primary donor.
- [ ] Map each requirement to secondary/exit donor.
- [ ] Record native Ptah code still required.
- [ ] Record licence compatibility.
- [ ] Record proof activity for each adopted subsystem.
- [ ] Review and freeze Phase 0A.

---

# Phase 0B — Contracts, migrations, and proof design

**Status:** NOT STARTED

- [ ] Object schema.
- [ ] Relationship schema.
- [ ] Workspace schema.
- [ ] Activity schema.
- [ ] Artifact schema.
- [ ] Node schema.
- [ ] Facility schema.
- [ ] Plugin schema.
- [ ] Session schema.
- [ ] Snapshot schema.
- [ ] Credential-reference schema.
- [ ] Telemetry schema.
- [ ] Provenance schema.
- [ ] Firmware schema.
- [ ] Sync and conflict schemas.
- [ ] Event envelope.
- [ ] Workspace-provider contract.
- [ ] Facility-adapter contract.
- [ ] Schema versioning and migration rules.
- [ ] Golden corpus and validation rules.
- [ ] Review and freeze Phase 0B.

---

# Phase 0C — First vertical slice

**Status:** NOT STARTED

- [ ] Select one Linux execution host.
- [ ] Approve first exact component list.
- [ ] Approve first donor/dependency set.
- [ ] Approve source layout.
- [ ] Approve first proof plan.
- [ ] Record implementation checkpoint in `CURRENT_STATE.md`.

---

# Phase 1 — Concurrent one-node substrate

- [ ] Rust node agent.
- [ ] Workspace namespace.
- [ ] Object catalogue.
- [ ] Activity registry.
- [ ] PTY and process supervision.
- [ ] Live event stream.
- [ ] Cancellation, detach, and reconnect.
- [ ] Node health and resource accounting.
- [ ] Artifact registration.
- [ ] Facility host.
- [ ] Prove at least ten simultaneous activities.

---

# Phase 2 — Intake and transfer

- [ ] Resumable uploads.
- [ ] URL and browser downloads.
- [ ] Segmented/multi-source transfers.
- [ ] Pause and resume.
- [ ] Partial-file recovery.
- [ ] Streaming hashes.
- [ ] Deduplication.
- [ ] Object-store, Drive, and node transfers.
- [ ] Transfer progress events.
- [ ] Prove interrupted large transfers recover.

---

# Phase 3 — Universal decomposition

- [ ] True-type detection.
- [ ] Archive pack.
- [ ] Document pack.
- [ ] Media and image pack.
- [ ] Executable pack.
- [ ] APK/application pack.
- [ ] Embedded/unknown-binary pack.
- [ ] Recursive object graph.
- [ ] Progressive previews and derivatives.
- [ ] Prove mixed-archive recursive decomposition under concurrency.

---

# Phase 4 — Firmware, disks, and filesystems

- [ ] Partition and disk model.
- [ ] Sparse/raw conversion.
- [ ] Dynamic partitions.
- [ ] Android boot-chain formats.
- [ ] Filesystem adapters.
- [ ] Apple firmware pack.
- [ ] MediaTek firmware pack.
- [ ] Unisoc firmware pack.
- [ ] Qualcomm firmware pack.
- [ ] Generic Android OTA pack.
- [ ] Additional vendor packs.
- [ ] Firmware view and comparison.
- [ ] Concurrent multi-family firmware proof.

---

# Phase 5 — Git, containers, environments, and builds

- [ ] Git mirrors and worktrees.
- [ ] Workspace-provider interface.
- [ ] Local-process provider.
- [ ] Container provider.
- [ ] Dev Container support.
- [ ] BuildKit.
- [ ] Typed execution recipes.
- [ ] Shared caches.
- [ ] Reproducible artifact export.
- [ ] Parallel-build proof.

---

# Phase 6 — Browser and live web

- [ ] Interactive Chromium.
- [ ] Persistent profiles and contexts.
- [ ] Playwright automation.
- [ ] Screenshots, recordings, traces, console, and network logs.
- [ ] Browser downloads and uploads.
- [ ] Responsive viewports.
- [ ] Rendered extraction.
- [ ] Warm browser pools.
- [ ] Browser recovery.
- [ ] Multi-context concurrency proof.

---

# Phase 7 — Human workspace shell

- [ ] Ptah home.
- [ ] Project and session selector.
- [ ] Object explorer.
- [ ] File browser and editor.
- [ ] Multi-terminal.
- [ ] Browser panels.
- [ ] Activity Centre.
- [ ] Transfer, process, container, storage, and artifact views.
- [ ] Media, document, firmware, application, and device views.
- [ ] Direct-human operation proof.

---

# Phase 8 — Session Vault

- [ ] Pause and checkpoint.
- [ ] Archive and export.
- [ ] Import and resume.
- [ ] Object and workspace versions.
- [ ] Snapshot references.
- [ ] Restart recovery.
- [ ] Drive export.
- [ ] Online/local sync foundation.
- [ ] Conflict model.
- [ ] Cross-node compatible resume proof.

---

# Phase 9 — Applications and devices

- [ ] Android runtime and devices.
- [ ] Linux applications.
- [ ] Windows node/VM and applications.
- [ ] Apple node and IPA workflows.
- [ ] Unified remote display.
- [ ] Concurrent application-session proof.

---

# Phase 10 — Knowledge, data, search, recipes, and plugins

- [ ] Unified search.
- [ ] Knowledge/retrieval adapters.
- [ ] Database pack.
- [ ] Structured data facility.
- [ ] Deterministic recipes.
- [ ] Service/port registry.
- [ ] Plugin lifecycle.

---

# Phase 11 — Provenance and security evidence

- [ ] Activity receipts.
- [ ] Tool, environment, image, and node identity.
- [ ] SBOMs.
- [ ] in-toto/Witness provenance.
- [ ] Signing and transparency.
- [ ] ORAS artifact relationships.
- [ ] Replay and reproducibility.
- [ ] Security workloads.
- [ ] End-to-end independent artifact verification.

---

# Phase 12 — Distributed Ptah

- [ ] Multiple Linux nodes.
- [ ] Mini-PC node.
- [ ] Windows and macOS nodes.
- [ ] GPU node.
- [ ] Device nodes.
- [ ] Capability placement.
- [ ] Node-to-node object transfer.
- [ ] Secure node identity and networking.
- [ ] Intermittent connectivity.
- [ ] Local-first/offline operation.
- [ ] Multi-node workspace proof.

---

# Phase 13 — OS readiness

- [ ] Separate private OS architecture decision.
- [ ] Select Linux/image foundation.
- [ ] Package proven Ptah services.
- [ ] Hardware profiles and drivers.
- [ ] Bootable image.
- [ ] Atomic updates and rollback.
- [ ] Encryption and recovery.
- [ ] Offline package/cache strategy.
- [ ] Prove no Ptah contract redesign is required.
