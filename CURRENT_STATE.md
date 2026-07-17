# Ptah Current State

**Last updated:** 2026-07-17  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Sessions and Artifacts.

Ptah supplies the working world; humans and compatible systems supply intent and reasoning.

The complete roadmap is stored in `MASTER_ROADMAP.md`.

---

# Mandatory closure method

Every requirement combines internal foundation, primary capability donor, completion donors, mature machinery, native Ptah contracts, an exit path and proof. One repository never closes a subsystem by itself.

Research and decisions are committed after every meaningful inspection unit.

Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

---

# Completed and saved work packages

## WP01 — Node and Workspace boundary

Separate Node Protocol and Workspace Provider contracts; distinct Node, Workspace, Activity, Object and Session identity; large streams separated from control events.

## WP02A–WP02C — Core runtime composition

Workspace/execution donors, Temporal, NATS/JetStream, OpenTelemetry and internal AgentOps/Foreman/Sergeant/Relay/CodeOps/MIBU/Hunter runtime evidence were inspected.

Closed for Phase 0B design:

- provider-neutral Workspaces;
- durable concurrent Activities;
- live/replayable Events;
- Facility manifests;
- Node Protocol;
- receipts, proof levels and stale-result rejection;
- terminal/process and OCI-provider foundations;
- observability and intermittent-Node journal boundaries.

## WP03 — Build, Artifact and provenance composition

BuildKit, Dagger, ORAS, Witness, in-toto, Sigstore/Cosign/Rekor/Fulcio, Syft and the internal Software Builder were inspected.

Closed for Phase 0B design:

- Build Recipes and backend compilation;
- cache and reproducibility identity;
- Artifact relationships;
- SBOM, attestation, signature, trust, review and independent-reproduction levels.

## WP04 — Storage, transfer, synchronization and backup composition

Lumi, aria2, tus/tusd, rclone, Syncthing, restic and internal storage-authority rules were inspected.

Closed for Phase 0B design:

- hot local Workspace storage;
- local CAS + SQLite/shared SQL + R2/S3 storage direction;
- immutable Objects and mutable revisions/conflicts;
- resumable upload/download and cloud/Node transport;
- encrypted backup/restore;
- Drive export/recovery;
- explicit parking of distributed shared filesystems until measured need.

## WP05 — Universal Object and decomposition composition

App Recover, APK Extractor, Creative Studio, Document Generator, libarchive, Tika, Unstructured, LIEF, Binwalk, JADX, Apktool, libvips, FFmpeg/ffprobe and Tree-sitter were inspected.

Closed for Phase 0B design:

- immutable Object graph;
- plural detector claims and progressive decomposition;
- bounded recursive extraction;
- document, image, media, binary, Android application and source-structure Domain Packs;
- Views, previews, transforms, rebuilds and explicit source-like origin classes.

## WP06 — Firmware, disks and filesystems composition

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

### Internal sources saved

- Apple tool/ramdisk/compatibility foundations;
- MediaTek read-only META handoff;
- Android updater-package control utility;
- Android driver repository gap;
- private Device Manager firmware-engine source recovery gap.

### External/upstream sources saved

- blacktop/ipsw;
- MTKClient;
- Qualcomm EDL/Sahara/Firehose;
- Unisoc PAC/BootROM/FDL composition;
- AOSP OTA payload, sparse, dynamic partition and AVB sources;
- payload-dumper-go;
- Samsung Heimdall/Odin/PIT;
- libguestfs;
- util-linux libfdisk;
- SRLabs generic firmware extractor;
- Binwalk/LIEF/libarchive reuse.

### Accepted direction

1. Firmware Package, Disk/Image, Manifest Graph, Device Profile, Compatibility Result, Static Activity and Physical Device Activity are separate contracts.
2. Filename, product name, chipset family, partition name and USB VID/PID are insufficient compatibility evidence.
3. Static firmware/package/disk analysis works without a connected device.
4. USB presence, protocol handshake, loader/programmer stage, configured service session, read, write acknowledgement and read-back verification are separate proof levels.
5. Read-only and mutation capabilities are independently declared and authorized.
6. Loader/programmer/FDL/DA/preloader/ramdisk assets are immutable Objects with exact source, digest, licence and target compatibility.
7. Physical mutation requires reviewed compatibility, immutable backup and post-operation read-back where possible.
8. Transport loss cannot trigger blind replay of non-idempotent physical operations.
9. Encrypted/signed originals remain preserved; decrypted/patched/rebuilt outputs receive new identity and trust state.
10. Untrusted filesystems use an isolated appliance rather than direct host-kernel mounts.
11. Vendor GPL/proprietary backends remain separate replaceable Facilities.
12. Generic firmware extraction does not imply vendor-aware flashing.
13. `.P5C` remains explicitly parked until a verified sample/spec/tool exists.
14. Exact private Device Manager Qualcomm/Unisoc source remains preserved for a later local-tree recovery pass and is not credited without inspection.

### Saved records

- `internal/APPLE-TOOL-FOUNDATIONS.md`
- `internal/MTK-META-FOUNDATIONS.md`
- `internal/ANDROID-OTA-CONTROL.md`
- `internal/ANDROID-DRIVER-REPOSITORIES.md`
- `internal/DEVICE-MANAGER-FIRMWARE-ENGINE-RECOVERY-GAP.md`
- `donors/BLACKTOP-IPSW.md`
- `donors/MTKCLIENT.md`
- `donors/QUALCOMM-EDL.md`
- `donors/UNISOC-PAC-FDL.md`
- `donors/ANDROID-OTA-IMAGE-FOUNDATIONS.md`
- `donors/SAMSUNG-HEIMDALL.md`
- `donors/LIBGUESTFS.md`
- `donors/LIBFDISK.md`
- `donors/OTHER-FIRMWARE-COVERAGE.md`
- `donors/P5C-STATUS.md`
- `decisions/ADR-0008-DISK-FIRMWARE-DEVICE-OPERATION-BOUNDARY.md`
- `work-packages/PHASE-0A-WP06-FIRMWARE-DISK-FILESYSTEM.md`

### Requirements closed for Phase 0B design

- `FW-001` through `FW-006`;
- `FS-001`;
- firmware/package/image portions of `CORE-003`, `CORE-004` and `SESSION-001`;
- firmware-side physical-operation boundary of `DEVICE-001`.

This does not approve runtime dependencies, driver bundles, loaders, device writes or implementation.

---

# Active inspection unit

## WP07 — Device and application runtime composition

Inspect as one complementary group:

1. recover exact internal Device Manager/MIBU/ADB/Fastboot/MTP/USB runtime evidence available through discoverable repositories;
2. DeviceFarmer STF, adbkit, minicap and minitouch;
3. Appium and the UIAutomator2 driver;
4. scrcpy;
5. TouchPilot upstream/fork relationship;
6. Android platform-tools and package/file/process/screen/input boundaries;
7. Linux graphical application runtime completion and remote-display gateways;
8. Windows application/VM/runtime and remote-display boundaries;
9. macOS/iOS application runtime, Xcode/Appium/Peekaboo-like boundaries;
10. physical device lease, multi-device inventory, session reconnect, recording and semantic UI proof.

Resolve:

- stable Device identity versus USB/ADB/transport identity;
- device inventory, exact selection and lease ownership;
- ADB, Fastboot, MTP, shell/process, package and file Facilities;
- screen/video stream, screenshots, input and semantic UI as separate capabilities;
- installed-package/application/session Object relationships;
- runtime proof versus command/launch proof;
- multiple simultaneous devices and applications;
- physical device, emulator, VM and remote application-provider distinctions;
- reconnect and stale-session rejection;
- sensitive screen/input/device-data handling;
- static firmware analysis versus physical runtime/control separation from ADR-0008;
- product-specific automation versus neutral public Ptah contracts.

Required saved output:

- donor/internal records after each inspection unit;
- Device/Application Runtime composition record;
- Device Session / Display / Input / Semantic UI boundary ADR;
- Requirement Closure Matrix updates for `DEVICE-001`, `DEVICE-002`, `APP-002`, `APP-003`, `APP-004`, application portions of `SESSION-001`, `UI-001`/`UI-002` and related Node/Activity rows;
- `PROGRESS.md` and this file updated continuously.

---

# Accepted decisions

- ADR-0001 — Node Protocol and Workspace Provider Boundary
- ADR-0002 — Composite Donor Closure Method
- ADR-0003 — Activity, Event and Observability Boundary
- ADR-0004 — Operation Identity, Receipts and Proof Levels
- ADR-0005 — Build Recipe, Artifact and Provenance Boundary
- ADR-0006 — Storage Classes, Object Transfer, Synchronization and Backup Boundary
- ADR-0007 — Object Graph, Decomposition, Views and Derivatives Boundary
- ADR-0008 — Disk Images, Firmware Packages and Physical Device Operations Boundary

---

# No-build boundary

Allowed now:

- donor/internal-work recovery;
- source inspection, canonical pins and licence review;
- composite requirement closure;
- ADRs, schemas and proof planning after Phase 0A review.

Not allowed yet:

- copying donor code;
- declaring closure from one donor;
- beginning runtime or large UI implementation;
- selecting dependencies from README claims alone;
- replacing internal work without evidence;
- exposing private consumers publicly.

---

# Phase 0A completion gate

Every v1 requirement must have a composite closure path, internal overlap, canonical pins/licences, native gap, exit strategy and validation plan, or be explicitly parked/rejected with a replacement.

---

# Chat continuation instruction

Read this file first, followed by `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, `DONOR_RECOVERY.md`, `REQUIREMENT_CLOSURE_MATRIX.md`, relevant donor/internal records, work packages and ADRs before proposing or performing further work.
