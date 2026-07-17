# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — CORE RUNTIME, BUILD/PROVENANCE, STORAGE/TRANSFER AND OBJECT/DECOMPOSITION CLOSED FOR DESIGN

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
| CORE-003 | Universal Object graph/catalogue | Object, Claim, Relationship and View contracts | internal App Recover/APK Extractor/Creative Studio/Document Generator; libarchive, Tika, Unstructured, LIEF, Binwalk, JADX, Apktool, libvips, FFmpeg and Tree-sitter | immutable identity, claims/conflicts, relationships, Views, derivatives, progressive depth and partial coverage | WP05, ADR-0007 |
| CORE-004 | Facility/Domain Pack host foundation | Facility Manifest and Domain Pack contract | OpenClaw plugins, OpenHands tools, MCP, Sergeant/CodeOps manifests plus WP05 parser/renderer packs | capability/version/status/resources/permissions/health, operations and proof outputs | WP02C/WP05, ADR-0007 |
| CORE-005 | Node Protocol/capabilities | Node Protocol | OpenClaw, Coder/DevPod agents, NATS, OTel, TechGuy Relay lessons, MIBU epochs/correlation | cryptographic identity, epoch, replay, capabilities, pairing and streams | ADR-0001/0003/0004 |
| RELAY-001 | Live Event transport | Event envelope/Fabric adapter | NATS Core, JetStream, OTel, Foreman bridge, Hunter outbox, MIBU stale rejection | sequence/cursor, retention, duplicate handling, backpressure and local outbox | WP02B/WP02C |
| RELAY-002 | Durable Activity recovery | Activity Ledger/checkpoints/receipts | Temporal, SQL, provider snapshots, Hunter Workflow/outbox and MIBU proof | retry classes, idempotency, compensation, leases/fencing and backend portability | WP02B/WP02C |
| EXEC-001 | Terminal/process supervision | Process/PTY Facility | OS APIs, OpenClaw detach/replay, Coder agent, E2B/OpenHands, internal subprocess/worker patterns | stream identity, process lifecycle, cancellation, resource accounting and recovery | WP02A/WP02C |
| EXEC-002 | OCI/container Workspace Provider | OCI Provider | containerd/OCI, Daytona lifecycle, Dev Containers/CLI, DevPod, E2B/Coder, internal shared-cache rules | lifecycle mapping, ports, storage, restart reconciliation and capability limits | WP02A/WP02C |
| EXEC-003 | Reproducible Build graph | Build Recipe and backend compilation | BuildKit, Dagger, internal Software Builder, containerd/OCI | recipes, step mapping, cache identity, secret refs, native backend support | WP03, ADR-0005 |
| SESSION-001 | Checkpoint/archive/export/import/resume | Session manifest | Workspace donors, Temporal, provider snapshots, Hunter checkpoints, WP04 Objects/revisions/backups/exports | compatibility, storage locations, revisions, backup/export and provider references | WP02C/WP04, ADR-0003/0006 |
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

## Closed foundation notes

- `PLUGIN-001` has closed Facility-manifest, Domain Pack and Build-module foundations, while general discovery/install/upgrade remains later.
- `DIST-001` has protocol, events and Object-transfer foundations, but scheduler, secure networking and placement policy remain open.
- JuiceFS and SeaweedFS are `PARKED` until measured Phase 12 shared-POSIX requirements justify them.
- Source Structure is closed as an optional Tree-sitter-backed View contract, while compiler/LSP/search integration remains later.
- Firmware, disk and filesystem packs reuse the WP05 Object/Claim/Relationship/Budget contracts and are now the active closure group.

---

# Active WP06 — Firmware, disks and filesystems composition

## FW-001 — Apple firmware

**Status:** RECOVERING INTERNAL WORK / INSPECTING DONORS

- Internal recovery: Apple/iPhone firmware, restore and download-manager work.
- External direction: blacktop/ipsw and authoritative Apple metadata/catalogue sources.
- Native gap: product/build/board/device compatibility, IPSW/OTA manifests, component/partition/file relationships, encryption/key states, signatures and restore-versus-analysis separation.

## FW-002 — MediaTek firmware

**Status:** RECOVERING INTERNAL WORK / INSPECTING DONORS

- Internal recovery: MTK/META, TSM DLL, Boot META, read-info/NVRAM/proinfo/nvdata and device profiles.
- External direction: MTKClient and specialist scatter/preloader/partition parsers.
- Native gap: scatter/package/partition/region relationships, SoC/profile compatibility, read-before-write receipts, backup/restore and META/BROM/Preloader capability separation.

## FW-003 — Unisoc firmware

**Status:** RECOVERING INTERNAL WORK / INSPECTING DONORS

- Internal recovery: SPD/Unisoc engine and PAC/FDL requirements.
- External direction: verified PAC/FDL parsers and service/download donors.
- Native gap: PAC manifest/partition/FDL/SoC relationships, checksum/compression/encryption states and safe static extraction.

## FW-004 — Qualcomm firmware

**Status:** RECOVERING INTERNAL WORK / INSPECTING DONORS

- Internal recovery: Qualcomm/DIAG, Firehose and XML flow work.
- External direction: EDL/Firehose programmers, rawprogram/patch XML and Sahara/Firehose donors.
- Native gap: programmer/device compatibility, GPT/LUN/partition relationships, read/write/erase operation classes and signed programmer provenance.

## FW-005 — Android OTA, sparse and dynamic partitions

**Status:** RECOVERING INTERNAL WORK / INSPECTING DONORS

- Internal recovery: Android OTA Manager and device-update workflows.
- External direction: update payload, sparse image, super/dynamic partition, vbmeta/AVB and platform tooling.
- Native gap: payload operation graph, source/target build compatibility, partition reconstruction, sparse/raw views, AVB verification and apply-versus-analysis separation.

## FW-006 — Other vendor/embedded firmware

**Status:** INSPECTING DONORS

- Foundation: Binwalk, LIEF, libarchive and generic firmware Object relationships from WP05.
- Open: Samsung/Odin, Huawei/Honor, ZTE, embedded/router/UEFI and other vendor pack coverage.
- `P5C`: unresolved until a verified sample/tool establishes the format; otherwise explicitly park with recovery criteria.

## FS-001 — Disks, partitions, images and filesystems

**Status:** INSPECTING DONORS

- Direction: GPT/MBR parsers, sparse/raw/qcow/vmdk/vhd images, libguestfs and filesystem-specific read-only adapters.
- Native gap: disk→partition→filesystem→file relationships, snapshots/overlays, read-only mounting, encrypted/locked states, journal consistency and rebuild/compare proof.

## DEVICE-001 firmware boundary — Device inventory and firmware operations

**Status:** COMPOSITE CANDIDATE — WP06 DEVICE-OPERATION BOUNDARY REQUIRED

- Existing foundation: MIBU proof levels, nonces/stale rejection, internal ADB/META/DIAG/USB work and Node/Activity/Receipt contracts.
- WP06 must separate static package/image analysis from physical read/write/flash/erase/reset operations and require exact device/profile/programmer compatibility plus backup/read-back proof.

---

# Other requirements still open or recovering

| ID | Requirement | Status | Current direction |
|---|---|---|---|
| GIT-001 | Mirrors/worktrees/refs | OPEN | Git plus internal ecosystem and Workspace patterns |
| EXEC-004 | Stronger isolation | OPEN | gVisor, Kata, Firecracker and alternate OCI runtimes |
| BROWSE-001 | Persistent interactive browser | OPEN | Playwright/Chromium, Browser-Use and TurboWebFetch |
| BROWSE-002 | Rendered extraction/research | OPEN | TurboWebFetch + Playwright + source provenance |
| BROWSE-003 | Browser evidence | OPEN | screenshots, recordings, traces, console/network Artifacts |
| DEVICE-001 runtime | Android inventory/ADB | COMPOSITE CANDIDATE | Device Manager/MIBU/ADB + STF/adbkit/Appium; exact donor pass pending |
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
| DIST-001 | Multi-Node placement/transfer | COMPOSITE CANDIDATE | core protocol/events/Object transport closed; scheduler and secure networking open |

---

# Current conclusion

Core runtime, Build/Artifact/Provenance, Storage/Transfer/Sync/Backup and Universal Object/Decomposition are closed for **Phase 0B contract design**, not implementation.

Active Phase 0A group: Firmware, Disks and Filesystems (`WP06`) as recorded in `CURRENT_STATE.md`.

Phase 0A cannot close until every v1 requirement is `CLOSED FOR DESIGN`, explicitly `PARKED`, or a `REJECTED PATH` with a replacement.
