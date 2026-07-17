# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — CORE THROUGH BROWSER/LIVE RESEARCH CLOSED FOR DESIGN

This file maps Ptah requirements to internal evidence, composite donors, native ownership, exit strategy and proof.

A requirement is never closed by naming one repository. Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

Design closure does **not** authorize implementation. Phase 0B schemas/conformance and Phase 0C slice approval remain mandatory.

---

# Requirements closed for Phase 0B contract design

| ID | Requirement | Native Ptah owner | Composite machinery/evidence | Evidence |
|---|---|---|---|---|
| CORE-001 | Persistent Workspace model | Workspace Provider | Daytona, Coder, E2B, Dev Containers, DevPod, local/OCI providers | WP02A/C, ADR-0001 |
| CORE-002 | Concurrent Activity runtime | Activity Ledger | Temporal, NATS/JetStream, OTel, AgentOps/Foreman/Hunter/MIBU | WP02B/C, ADR-0003/0004 |
| CORE-003 | Universal Object graph | Object/Claim/Relationship/View contracts | internal recovery tools, libarchive, Tika, Unstructured, LIEF, Binwalk, JADX, Apktool, libvips, FFmpeg, firmware/image packs | WP05/06, ADR-0007/0008 |
| CORE-004 | Facility/Domain Pack host | Facility Manifest and Domain Pack contract | OpenClaw/OpenHands/MCP, Sergeant/CodeOps, parser, firmware, Device, Application and Browser adapters | WP02C–WP08 |
| CORE-005 | Node Protocol/capabilities | Node Protocol | OpenClaw, Coder/DevPod agents, NATS, OTel, Relay, Device/Application/Browser Providers | ADR-0001/0003/0009/0010/0011 |
| RELAY-001 | Live Events | Event Fabric adapter | NATS/JetStream, OTel, internal bridge/outbox and runtime streams | WP02B/C |
| RELAY-002 | Durable recovery | Activity Ledger/checkpoints/receipts | Temporal, SQL, provider snapshots and internal workflows/outbox | WP02B/C |
| EXEC-001 | Terminal/process supervision | Process/PTY Facility | OS APIs, OpenClaw, Coder, E2B/OpenHands and internal workers | WP02A/C |
| EXEC-002 | OCI Workspace Provider | OCI Provider | containerd/OCI, Daytona, Dev Containers, DevPod, E2B/Coder | WP02A |
| EXEC-003 | Reproducible Build graph | Build Recipe/backend adapter | BuildKit, Dagger, Software Builder | WP03, ADR-0005 |
| STORE-001 | Hot local Workspace storage | Storage Class/Volume contract | local SSD/NVMe, provider volumes and containerd snapshots | WP04, ADR-0006 |
| STORE-002 | Durable Object/Artifact storage | Object/Location catalogue | local CAS, R2/S3, ORAS/OCI and Drive exports | WP03/04 |
| STORE-003 | Metadata catalogue | local/shared SQL schemas | SQLite, shared SQL and internal outbox evidence | WP04 |
| STORE-004 | Hashing/deduplication | qualified digest/Object identity | streaming hashes, OCI descriptors, aria2/tus/restic/Syncthing evidence | WP03/04 |
| STORE-005 | Drive export/recovery | Export/Import Facility | rclone/Drive plus Ptah manifests | WP04 |
| XFER-001 | Resumable upload | Upload Facility | tus/tusd and Object landing/finalization | WP04 |
| XFER-002 | Fast resumable download | Download Facility | Lumi, aria2, browser download handoff and specialist adapters | WP04/WP08 |
| XFER-003 | Cloud/Node transport | Object Transfer Facility | rclone, Syncthing and Ptah streams | WP04 |
| SYNC-001 | Online/local sync/conflicts | Revision/Conflict contract | Hunter safe sync, Syncthing vectors and Object digests | WP04 |
| DECOMP-001 | True-type detection | Detector Claim/router | Tika, libarchive, LIEF, Binwalk, ffprobe, libvips and platform parsers | WP05 |
| DECOMP-002 | Recursive decomposition | bounded Container Domain Pack | libarchive, Binwalk, Tika and internal recovery | WP05 |
| DOC-001 | Document structure/render/proof | Document Domain Pack | Document Generator, Tika, Unstructured and renderers | WP05 |
| MEDIA-001 | Video/audio | Media Domain Pack | Creative Studio and FFmpeg/ffprobe | WP05 |
| IMAGE-001 | Image processing | Image Domain Pack | Creative Studio and libvips | WP05 |
| BIN-001 | Executable/binary decomposition | Binary Domain Pack | App Recover, LIEF and Binwalk | WP05 |
| APP-001 | APK/AAB/DEX decomposition | Android Application Domain Pack | APK Extractor, raw package, Apktool and JADX | WP05 |
| FW-001 | Apple firmware packages | Apple Firmware Domain Pack | internal Apple evidence and blacktop/ipsw | WP06 |
| FW-002 | MediaTek firmware/service modes | MTK Firmware/Device adapters | internal META and MTKClient | WP06 |
| FW-003 | Unisoc PAC/FDL | Unisoc Firmware/Device adapters | spreadtrum_flash, unpac and sprdproto | WP06 |
| FW-004 | Qualcomm Sahara/Firehose | Qualcomm Firmware/Device adapters | internal requirements and bkerler/edl | WP06 |
| FW-005 | Android OTA/dynamic partitions | Android Firmware Image Pack | internal OTA and AOSP payload/sparse/liblp/AVB | WP06 |
| FW-006 | Other vendor/embedded firmware | Generic Firmware router/vendor packs | Binwalk/LIEF/libarchive, Heimdall and explicit gaps | WP06 |
| FS-001 | Disks/partitions/filesystems | Disk/Image/Filesystem Packs | libfdisk, libguestfs and Android image machinery | WP06 |
| DEVICE-001 | Android inventory/ADB/Fastboot/control | Device identity/interface/provider/lease contract | Device Manager, MIBU, STF, adbkit and official platform-tools | WP07A, ADR-0009 |
| DEVICE-002 | Android display/input/semantic UI | Device Session/Stream/Screen Context | scrcpy, minicap/minitouch, AndroidX UIA, Appium UIA2 and TouchPilot | WP07A, ADR-0009 |
| APP-002 | Linux graphical/native runtime | Application Provider/Session/Window | native/OCI providers, Xpra, Guacamole and noVNC | WP07B, ADR-0010 |
| APP-003 | Windows EXE/MSI/UWP runtime | Windows native/VM Application Provider | QEMU/libvirt, FreeRDP/Guacamole, FlaUI and NovaWindows | WP07B, ADR-0010 |
| APP-004 | macOS/iOS runtime | macOS/iOS Application and Device Providers | Peekaboo, Appium XCUITest, IDB and Apple platform tooling | WP07B, ADR-0010 |
| BROWSE-001 | Persistent interactive browser | Browser Provider/Profile/Context/Page contracts | Playwright, Browser-Use profile/session patterns and internal secret/Transfer rules | WP08, ADR-0011 |
| BROWSE-002 | Rendered extraction/live research | Rendered Retrieval and Source/Citation contracts | Playwright, TurboWebFetch, Browser-Use and Readability/Markdown derivatives | WP08, ADR-0011 |
| BROWSE-003 | Browser evidence | Browser View/Evidence contracts | Playwright screenshot/PDF/video/trace/console/network/HAR and source/DOM/accessibility Views | WP08, ADR-0011 |
| SESSION-001 | Checkpoint/archive/export/import/resume | Session manifest | Workspace donors, Temporal, storage/backups, VM/device/application/browser checkpoints | WP02–WP08 |
| OBS-001 | Logs/metrics/traces/resource accounting | OTel conventions and receipt links | OTel, internal audits, Build/device/application/browser evidence | WP02–WP08 |
| PROV-001 | Provenance/signing/proof bundles | Provenance/Verification graph | Witness, in-toto, Sigstore, ORAS, Syft and runtime/browser evidence | WP03–WP08 |
| OFFLINE-001 | Intermittent Node operation | local journal/outbox and reconciliation | Event Fabric, revision model and Device/Application/Browser epochs | WP02/04/07/08 |

## Closed-foundation notes

- `PLUGIN-001` has closed Facility, Domain Pack and Build-module foundations; general discovery/install/upgrade remains later.
- `DIST-001` has Node, event, provider, Object-transfer and capability foundations; scheduler/placement quality and secure multi-Node networking remain open.
- `UI-001` and `UI-002` have Activity, Object, Device, Application, Window, Browser and evidence data models, but the Human Workspace shell remains open.
- Linux semantic automation retains an AT-SPI completion gap.
- JuiceFS/SeaweedFS are `PARKED` until measured Phase 12 shared-POSIX need.
- `.P5C` is `PARKED` pending a lawful immutable sample or authoritative format/tool.
- Private device-manager monorepo paths that could not be audited remain an internal source-recovery gap.

---

# Active WP09 — Human Workspace Shell and Operator Interface

## UI-001 — Human Workspace shell

**Status:** INSPECTING DONORS

- Primary direction: Eclipse Theia with native Ptah panels and service contracts.
- Compatibility candidates: OpenVSCode Server and code-server.
- Completion: xterm.js/Monaco and a dock/layout engine where Theia's contribution model is insufficient.
- Internal evidence: Hunter, Foreman, Sergeant, Device Manager, MIBU, website and THETECHGUY Tool interfaces.
- Native gap: Ptah Home, Workspace switcher, Object/file views, multi-terminal/browser/device/application panels, responsive layouts and direct-human operation.

## UI-002 — Activity Centre, evidence and review

**Status:** INSPECTING DONORS

- Foundation: Activity Ledger, Event Fabric, OTel, Foreman/Sergeant status and proof models.
- Runtime inputs: Device/Application/Browser Sessions, streams, receipts, evidence and degraded states.
- Native gap: simultaneous unrelated Activities, dependency/status views, retry/cancel/recover controls, evidence/proof inspection and honest claim labels.

## Human-control extension

**Status:** INSPECTING DONORS

Resolve:

- panel/window/tab/layout identity and saved layouts;
- input focus and control lease between human and automation;
- human takeover/return receipts;
- mobile/desktop/browser responsive behavior;
- accessibility, keyboard navigation and reduced motion;
- planned/configured/connected/running/verified distinctions;
- public-safe versus private/operator UI contributions.

---

# Remaining open clusters

| Cluster | Status | Direction |
|---|---|---|
| Knowledge/Data/Search | OPEN | RAGFlow, LlamaIndex, Dify, Polars/SQL and source-grounded indexing |
| General plugin lifecycle | OPEN | OpenClaw/ClawHub, MCP, OCI registries and Ptah Facility governance |
| Strong isolation | OPEN | gVisor, Kata, Firecracker, youki and crun |
| Distributed placement | COMPOSITE CANDIDATE | Node resources/capabilities exist; scheduler, leases and secure networking remain |
| Reproduction/security workloads | OPEN | SparkDistill, ClaimBound, ReproZip, GUAC, Strix, Semgrep, Trivy, ZAP and scanners |
| Research/documentation sources | OPEN | unresolved profiles, catalogues and public documentation tooling |

---

# Current conclusion

Core runtime, Build/Artifact/Provenance, Storage/Transfer/Sync, Object/Decomposition, Firmware/Disk/Filesystem, Device/Application Runtime and Browser/Live Research are closed for **Phase 0B contract design**, not implementation.

Active Phase 0A group: Human Workspace Shell and Operator Interface (`WP09`) as recorded in `CURRENT_STATE.md`.

Phase 0A cannot close until every v1 requirement is `CLOSED FOR DESIGN`, explicitly `PARKED`, or a `REJECTED PATH` with a replacement.
