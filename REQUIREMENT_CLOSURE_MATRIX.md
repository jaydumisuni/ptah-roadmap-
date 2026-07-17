# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — CORE RUNTIME, BUILD/PROVENANCE AND STORAGE/TRANSFER CLOSED FOR DESIGN

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
| CORE-004 | Facility/plugin host foundation | Facility Manifest/host/invocation | OpenClaw plugins, OpenHands tools, MCP, Sergeant manifests, CodeOps routes, AgentOps packets | capability/version/status/resources/permissions/health/pin/upgrade/rollback | WP02C |
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

## Closed foundation notes

- `CORE-003` now has closed storage-location, digest and Build Artifact relationship foundations, but universal detection/decomposition and child/derivative relationships remain WP05.
- `PLUGIN-001` has closed Build-module and Facility-manifest foundations, while general discovery/install/upgrade remains later.
- `DIST-001` has protocol, events and Object-transfer foundations, but scheduler, secure networking and placement policy remain open.
- JuiceFS and SeaweedFS are `PARKED` until measured Phase 12 shared-POSIX requirements justify them.

---

# Active WP05 — Universal Object and decomposition composition

## CORE-003 — Universal Object graph and catalogue

**Status:** RECOVERING INTERNAL WORK / INSPECTING DONORS

- Closed foundations: content identity, storage locations, revisions, Artifacts, Activities and provenance.
- Internal recovery: App Recover, APK Extractor, Creative Studio and Document Generator.
- External donor direction: libarchive, Tika, Unstructured, LIEF, Binwalk, JADX, Apktool, libvips, FFmpeg/ffprobe and source-structure donors where required.
- Native gap: type claims/confidence, parent/child/contains/derived-from/view relationships, progressive depth, extraction budgets, malformed/encrypted/opaque states and derivative identity.

## DECOMP-001 — True-type detection

**Status:** INSPECTING DONORS

- Direction: signature/magic/container/parser claims with evidence and confidence rather than extension-only classification.
- Required: conflicting detector claims, encrypted/unsupported states and exact detector/version receipts.

## DECOMP-002 — Recursive archive and container decomposition

**Status:** INSPECTING DONORS

- Direction: libarchive plus format-specific Domain Packs and native recursion/budget controls.
- Required: depth, child-count, byte-expansion, path, symlink and time/resource limits.

## DOC-001 — Document structure, render and proof

**Status:** RECOVERING INTERNAL WORK

- Direction: internal Document Generator plus Tika/Unstructured and format-specific renderers.
- Required: structured text/metadata, page/section/table/image Objects, previews and renderer receipts.

## MEDIA-001 — Video/audio decomposition and transforms

**Status:** RECOVERING INTERNAL WORK

- Direction: Creative Studio plus FFmpeg/ffprobe.
- Required: streams/tracks/chapters/frames/thumbnails/waveforms, codec/container evidence and transform receipts.

## IMAGE-001 — Image decomposition and processing

**Status:** RECOVERING INTERNAL WORK

- Direction: Creative Studio plus libvips and metadata/color-profile donors as needed.
- Required: originals, derivatives, regions/pages/frames, dimensions, color/EXIF claims and bounded transforms.

## BIN-001 — Executable/binary decomposition

**Status:** RECOVERING INTERNAL WORK

- Direction: App Recover plus LIEF/Binwalk and platform-specific packs.
- Required: headers, sections, imports/exports, resources, signatures, embedded files and safe static-only defaults.

## APP-001 — APK/AAB/DEX decomposition

**Status:** RECOVERING INTERNAL WORK

- Direction: APK Extractor plus JADX/Apktool and Android signing/manifest/resource tooling.
- Required: package/manifest/components/resources/DEX/native libs/signatures, source/resource derivatives and rebuild distinction.

---

# Other requirements still open or recovering

| ID | Requirement | Status | Current direction |
|---|---|---|---|
| GIT-001 | Mirrors/worktrees/refs | OPEN | Git plus internal ecosystem and Workspace patterns |
| EXEC-004 | Stronger isolation | OPEN | gVisor, Kata, Firecracker and alternate OCI runtimes |
| BROWSE-001 | Persistent interactive browser | OPEN | Playwright/Chromium, Browser-Use and TurboWebFetch |
| BROWSE-002 | Rendered extraction/research | OPEN | TurboWebFetch + Playwright + source provenance |
| BROWSE-003 | Browser evidence | OPEN | screenshots, recordings, traces, console/network Artifacts |
| FW-001 | Apple firmware | OPEN | internal Apple work + blacktop/ipsw |
| FW-002 | MediaTek firmware | RECOVERING INTERNAL WORK | internal MTK/META + MTKClient |
| FW-003 | Unisoc firmware | RECOVERING INTERNAL WORK | internal SPD/Unisoc + PAC/FDL donors |
| FW-004 | Qualcomm firmware | RECOVERING INTERNAL WORK | internal Qualcomm + EDL/Firehose/XML/LIEF |
| FW-005 | Android OTA/dynamic partitions | RECOVERING INTERNAL WORK | internal OTA + payload/platform tools |
| FW-006 | Other vendor/embedded firmware | OPEN | Binwalk and vendor Domain Packs |
| FS-001 | Disks, partitions, images/filesystems | OPEN | libguestfs and platform tools |
| DEVICE-001 | Android inventory/ADB | COMPOSITE CANDIDATE | Device Manager/MIBU/ADB + STF/adbkit/Appium; exact donor pass pending |
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

Core runtime, Build/Artifact/Provenance and Storage/Transfer/Sync/Backup are closed for **Phase 0B contract design**, not implementation.

Active Phase 0A group: Universal Object and Decomposition (`WP05`) as recorded in `CURRENT_STATE.md`.

Phase 0A cannot close until every v1 requirement is `CLOSED FOR DESIGN`, explicitly `PARKED`, or a `REJECTED PATH` with a replacement.
