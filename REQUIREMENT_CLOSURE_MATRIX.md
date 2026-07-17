# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — CORE RUNTIME, BUILD/PROVENANCE, STORAGE/TRANSFER, OBJECT/DECOMPOSITION AND FIRMWARE/DISK CLOSED FOR DESIGN

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
| CORE-003 | Universal Object graph/catalogue | Object, Claim, Relationship and View contracts | internal App Recover/APK Extractor/Creative Studio/Document Generator; libarchive, Tika, Unstructured, LIEF, Binwalk, JADX, Apktool, libvips, FFmpeg, Tree-sitter and firmware/image packs | immutable identity, claims/conflicts, relationships, Views, derivatives, progressive depth, disk/partition/component relationships and partial coverage | WP05/WP06, ADR-0007/0008 |
| CORE-004 | Facility/Domain Pack host foundation | Facility Manifest and Domain Pack contract | OpenClaw plugins, OpenHands tools, MCP, Sergeant/CodeOps manifests, WP05 parser/renderer packs and WP06 firmware/disk packs | capability/version/status/resources/permissions/health, operations, compatibility and proof outputs | WP02C/WP05/WP06, ADR-0007/0008 |
| CORE-005 | Node Protocol/capabilities | Node Protocol | OpenClaw, Coder/DevPod agents, NATS, OTel, TechGuy Relay lessons, MIBU epochs/correlation | cryptographic identity, epoch, replay, capabilities, pairing and streams | ADR-0001/0003/0004 |
| RELAY-001 | Live Event transport | Event envelope/Fabric adapter | NATS Core, JetStream, OTel, Foreman bridge, Hunter outbox, MIBU stale rejection | sequence/cursor, retention, duplicate handling, backpressure and local outbox | WP02B/WP02C |
| RELAY-002 | Durable Activity recovery | Activity Ledger/checkpoints/receipts | Temporal, SQL, provider snapshots, Hunter Workflow/outbox and MIBU proof | retry classes, idempotency, compensation, leases/fencing and backend portability | WP02B/WP02C |
| EXEC-001 | Terminal/process supervision | Process/PTY Facility | OS APIs, OpenClaw detach/replay, Coder agent, E2B/OpenHands, internal subprocess/worker patterns | stream identity, process lifecycle, cancellation, resource accounting and recovery | WP02A/WP02C |
| EXEC-002 | OCI/container Workspace Provider | OCI Provider | containerd/OCI, Daytona lifecycle, Dev Containers/CLI, DevPod, E2B/Coder, internal shared-cache rules | lifecycle mapping, ports, storage, restart reconciliation and capability limits | WP02A/WP02C |
| EXEC-003 | Reproducible Build graph | Build Recipe and backend compilation | BuildKit, Dagger, internal Software Builder, containerd/OCI | recipes, step mapping, cache identity, secret refs, native backend support | WP03, ADR-0005 |
| SESSION-001 | Checkpoint/archive/export/import/resume | Session manifest | Workspace donors, Temporal, provider snapshots, Hunter checkpoints, WP04 Objects/revisions/backups/exports and WP06 disk/image snapshots | compatibility, storage locations, revisions, backup/export, provider references and image/snapshot relationships | WP02C/WP04/WP06, ADR-0003/0006/0008 |
| OBS-001 | Logs/metrics/traces/resource accounting | OTel semantic conventions and receipt links | OTel/Collector, internal health/audit/proof/outbox attempts | correlation, redaction, buffering, resource accounting and proof classes | WP02B/WP02C |
| OFFLINE-001 | Intermittent Node journal and reconciliation | local Node journal/outbox | NATS/JetStream, Activity Ledger, Hunter safe sync/outbox, MIBU late result, WP04 revision/transfer model | authority, acknowledgements, revisions/conflicts, Object repair and reconnect | ADR-0003/0004/0006 |
| PROV-001 | Provenance/signing/proof bundles | Provenance/Verification graph | Witness, in-toto, Sigstore/Cosign/Fulcio/Rekor, ORAS, Syft, internal receipts | SBOM, attestation, signature, trust, policy, review and reproduction records | WP03, ADR-0005 |
| STORE-001 | Hot local Workspace storage | Storage Class/Volume contract | local SSD/NVMe, Linux filesystems, provider volumes, containerd snapshots, Builder/Hunter rules | active/cache/temp/project/volume classes, pressure and health | WP04, ADR-0006 |
| STORE-002 | Durable Object/Artifact storage | Object/Location catalogue | local CAS, R2/S3, ORAS/OCI, Drive export, Hunter R2 lifecycle | location health, replication, retention, repair and backend replacement | WP03/WP04, ADR-0005/0006 |
| STORE-003 | Metadata catalogue | local SQLite/shared SQL schemas | SQLite direction, PostgreSQL/D1-compatible shared SQL, Hunter idempotency/outbox evidence | migrations, transactions, projections, local journal and conflict records | WP04, ADR-0006 |
| STORE-004 | Hashing and deduplication | qualified digest/Object identity | streaming hashes, OCI descriptors, aria2 pieces, tus landing, restic/Syncthing block evidence | digest algorithms, chunks, partial validation, dedupe and repair | WP03/WP04, ADR-0005/0006 |
| STORE-005 | Drive export and recovery | Export/Import Facility | rclone/Drive adapter and Ptah export manifest | readable bundles, verification and explicit non-live-filesystem rule | WP04, ADR-0006 |
| XFER-001 | Resumable uploads | Upload/Transfer Facility | tus/tusd, Object landing/finalization and local/S3-compatible stores | offsets, locks, hashes, finalization, cleanup and Object registration | WP04, ADR-0006 |
| XFER-002 | Fast resumable downloads | Download/Transfer Facility | Lumi DM, aria2, yt-dlp/libtorrent/FFmpeg adapters | segmented/multi-source, source validators, restart, progress and verification | WP04, ADR-0006 |
| XFER-003 | Cloud and Node transport | Object Transfer Facility | rclone, Syncthing, dedicated Ptah streams | source/destination locations, scoped credentials, direct replication and receipts | WP04, ADR-0006 |
| SYNC-001 | Online/local synchronization and conflicts | Revision/Conflict contract | Hunter safe sync, Syncthing vectors, rclone transport, Object digests | parents, tombstones, divergence, merge/resolution and authority | WP04, ADR-0006 |
| DECOMP-001 | True-type detection | Detector Claim and routing contract | Tika, libarchive, LIEF, Binwalk, ffprobe, libvips/image loaders, Android parsers and internal App Recover evidence | plural claims, evidence classes, confidence/calibration, conflict and unknown/encrypted/malformed states | WP05, ADR-0007 |
| DECOMP-002 | Recursive archive/container decomposition | bounded Archive/Container Domain Pack | libarchive, Binwalk, Tika embedded resources and internal recovery tools | streaming children, recursive budgets, path/link safety, dedupe, partial states and rebuild comparison | WP05, ADR-0007 |
| DOC-001 | Document structure/render/proof | Document Domain Pack | internal Document Generator, Tika, Unstructured, browser/PDF renderers and private template packs | payload/model/template/HTML/PDF/page/element relationships, truth references, privacy and visual proof | WP05, ADR-0007 |
| MEDIA-001 | Video/audio decomposition/transforms | Media Domain Pack | Creative Studio, ffprobe/FFmpeg and Object-backed Assets | containers, streams/tracks/chapters/frames/subtitles, transforms, A/V proof and build features | WP05, ADR-0007 |
| IMAGE-001 | Image decomposition/processing | Image Domain Pack | Creative Studio, libvips and specialist loader packs | dimensions/pages/frames/bands, EXIF/ICC/HDR, bounded transforms, previews and visual equivalence | WP05, ADR-0007 |
| BIN-001 | Executable/binary decomposition | Binary Domain Pack | App Recover, LIEF, Binwalk and platform signature/debug tools | formats/slices/sections/imports/resources/signatures/embedded regions, static-only default and mutation proof | WP05, ADR-0007 |
| APP-001 | APK/AAB/DEX decomposition | Android Application Domain Pack | internal APK Extractor, raw package view, Apktool, JADX, LIEF and later signing/bundle tools | package sets, manifest/components/resources/DEX/native/signing, view origins, rebuild/sign/install separation | WP05, ADR-0007 |
| FW-001 | Apple firmware package analysis | Apple Firmware Domain Pack | internal Apple tool/index/ramdisk evidence, blacktop/ipsw, BuildManifest/device-tree/component parsing and verified downloads | product/build/board compatibility, manifest identities, components, encryption/key/signature states and analysis-versus-restore separation | WP06, ADR-0008 |
| FW-002 | MediaTek firmware and service-mode composition | MediaTek Firmware/Device adapters | internal META handoff and mtkclient-meta-mode, upstream MTKClient, scatter/GPT/partition/loader evidence | package/partition/region relationships, SoC/profile/loader compatibility, META/BROM/Preloader/DA separation and read-before-write proof | WP06, ADR-0008 |
| FW-003 | Unisoc PAC/FDL firmware composition | Unisoc Firmware/Device adapters | internal requirement evidence, spreadtrum_flash, unpac and sprdproto | PAC entries, FDL stages/base addresses, partition inventory, exact target compatibility, safe extraction and physical-operation separation | WP06, ADR-0008 |
| FW-004 | Qualcomm Sahara/Firehose firmware composition | Qualcomm Firmware/Device adapters | internal DIAG/Firehose requirements, bkerler/edl, Sahara identity, programmer database, GPT/LUN/rawprogram evidence | programmer/device compatibility, memory/LUN/partition relationships, read/write/erase classes and programmer provenance | WP06, ADR-0008 |
| FW-005 | Android OTA, sparse and dynamic partitions | Android Firmware Image Domain Pack | internal OTA control utility, payload-dumper-go, AOSP update payload/sparse/liblp/AVB definitions | payload operation graph, source/target compatibility, sparse/raw views, logical extents, AVB verification and analysis-versus-apply separation | WP06, ADR-0008 |
| FW-006 | Other vendor and embedded firmware coverage | Generic Firmware router plus optional vendor packs | Binwalk/LIEF/libarchive, Heimdall for Samsung, SRLabs Extractor and explicit Huawei/ZTE/router/UEFI gaps | evidence-based routing, vendor-pack boundaries, unsupported/proprietary states and no extension-only trust | WP06, ADR-0008 |
| FS-001 | Disks, partitions, images and filesystems | Disk/Image/Filesystem Domain Packs | libfdisk, libguestfs, Android sparse/dynamic machinery, generic Object/Claim contracts | disk→partition→filesystem→file graph, exact image format, read-only appliance inspection, encryption/locked states, overlays, compare and mutation plans | WP06, ADR-0008 |
| DEVICE-001 firmware boundary | Static firmware analysis versus physical device operations | Device Profile, Compatibility Result and Device Activity contracts | internal MIBU/META/ADB/USB lessons, MTKClient, EDL, spreadtrum_flash, Heimdall and ADR proof levels | exact profile/programmer/loader identity, immutable backup, lease, mutation authorization, receipts and read-back verification | WP06, ADR-0008 |

## Closed foundation notes

- `PLUGIN-001` has closed Facility-manifest, Domain Pack and Build-module foundations, while general discovery/install/upgrade remains later.
- `DIST-001` has protocol, events and Object-transfer foundations, but scheduler, secure networking and placement policy remain open.
- JuiceFS and SeaweedFS are `PARKED` until measured Phase 12 shared-POSIX requirements justify them.
- Source Structure is closed as an optional Tree-sitter-backed View contract, while compiler/LSP/search integration remains later.
- P5C is `PARKED`; reopening requires a lawful immutable sample or authoritative specification/tool, reproducible header/table evidence and a source/licence review.
- The private `thetechguy-device-manager` repository remains a recorded source-recovery gap where exact Qualcomm/Unisoc/shared-engine paths could not be audited through the connector.
- Firmware analysis, mounted image inspection and physical device mutation remain separate activities under ADR-0008.

---

# Active WP07 — Device and application runtime composition

## DEVICE-001 runtime — Android inventory, transport and control

**Status:** RECOVERING INTERNAL WORK / INSPECTING DONORS

- Internal recovery: exact Device Manager, MIBU, ADB, Fastboot, MTP, USB/serial and package/process/file runtime evidence available through discoverable repositories.
- External direction: DeviceFarmer STF, adbkit, Android platform-tools and provider-specific transport adapters.
- Native gap: stable Device identity, transport/interface identity, inventory state, exact selection, lease ownership, authorization, reconnect epochs, stale-session rejection and per-capability receipts.

## DEVICE-002 — Android display, input and semantic UI

**Status:** INSPECTING DONORS

- External direction: minicap/minitouch, scrcpy, Appium, UIAutomator2, Android UIAutomator and verified TouchPilot lineage.
- Native gap: display/video stream, screenshot, recording, clipboard, raw input, gesture, element hierarchy and semantic action as distinct capabilities with separate evidence.

## APP-002 — Linux graphical/native application runtime

**Status:** INSPECTING DONORS

- Foundation: E2B Desktop and Workspace-provider work from WP02.
- Open: native Linux process/display/session provider, Wayland/X11/RDP/VNC/WebRTC boundaries, app lifecycle and user-visible readiness proof.

## APP-003 — Windows EXE/MSI runtime

**Status:** OPEN / DONOR RECOVERY REQUIRED

- Direction: Windows Node or VM provider, process/package/runtime services and remote-display transport.
- Native gap: executable/install/session identity, UAC/desktop boundaries, state capture, application readiness and restart/reconnect proof.

## APP-004 — Apple IPA/macOS runtime

**Status:** OPEN / DONOR RECOVERY REQUIRED

- Direction: macOS/Xcode/simulator/device Nodes, Appium/XCUITest and Peekaboo-like screen/application automation boundaries.
- Native gap: bundle/signing/provisioning/runtime identity, simulator versus physical device, application session, display/input and notarization/trust states.

## SESSION-001 application extension

**Status:** COMPOSITE CANDIDATE — WP07 EXTENSION REQUIRED

- Extend the closed Session manifest with Device lease, transport epoch, display/input stream references, installed application, foreground process/window, recording and reconnect compatibility.

## UI-001 / UI-002 runtime extension

**Status:** COMPOSITE CANDIDATE — WP07 EVIDENCE REQUIRED

- Human Workspace shell and Activity Centre must present multiple simultaneous devices/applications without confusing command acceptance, launched process, visible screen readiness, semantic state and completed action.

---

# Other requirements still open or recovering

| ID | Requirement | Status | Current direction |
|---|---|---|---|
| GIT-001 | Mirrors/worktrees/refs | OPEN | Git plus internal ecosystem and Workspace patterns |
| EXEC-004 | Stronger isolation | OPEN | gVisor, Kata, Firecracker and alternate OCI runtimes |
| BROWSE-001 | Persistent interactive browser | OPEN | Playwright/Chromium, Browser-Use and TurboWebFetch |
| BROWSE-002 | Rendered extraction/research | OPEN | TurboWebFetch + Playwright + source provenance |
| BROWSE-003 | Browser evidence | OPEN | screenshots, recordings, traces, console/network Artifacts |
| DEVICE-001 runtime | Android inventory/ADB | RECOVERING INTERNAL WORK / INSPECTING DONORS | Device Manager/MIBU/ADB + STF/adbkit/platform-tools |
| DEVICE-002 | Android screen/input/semantic UI | INSPECTING DONORS | minicap/minitouch, Appium/UIAutomator2, scrcpy and TouchPilot verification |
| APP-002 | Linux graphical/native app | INSPECTING DONORS | E2B Desktop + remote display/native Linux |
| APP-003 | Windows EXE/MSI runtime | OPEN | Windows Node/VM + remote display |
| APP-004 | Apple IPA/macOS runtime | OPEN | macOS/Xcode Node + Appium/XCUITest/Peekaboo-like donors |
| UI-001 | Human Workspace shell | COMPOSITE CANDIDATE | Theia/remote-display/native panels plus WP07 multi-device/application requirements |
| UI-002 | Activity Centre | COMPOSITE CANDIDATE | Foreman/Sergeant + OpenHands/Coder + native concurrent device/application view |
| SEARCH-001 | Unified search/indexing | OPEN | RAGFlow/LlamaIndex + multi-domain Object index |
| DATA-001 | Structured data/database pack | OPEN | Polars/SQL + native data Objects/Activities |
| PLUGIN-001 | General plugin lifecycle | OPEN | OpenClaw/ClawHub, MCP and OCI registries |
| SEC-001 | Security workload/evidence | OPEN | Strix, Semgrep, ZAP, Trivy, Syft and Grype |
| DIST-001 | Multi-Node placement/transfer | COMPOSITE CANDIDATE | core protocol/events/Object transport closed; scheduler and secure networking open |

---

# Current conclusion

Core runtime, Build/Artifact/Provenance, Storage/Transfer/Sync/Backup, Universal Object/Decomposition and Firmware/Disk/Filesystem are closed for **Phase 0B contract design**, not implementation.

Active Phase 0A group: Device and Application Runtime composition (`WP07`) as recorded in `CURRENT_STATE.md`.

Phase 0A cannot close until every v1 requirement is `CLOSED FOR DESIGN`, explicitly `PARKED`, or a `REJECTED PATH` with a replacement.
