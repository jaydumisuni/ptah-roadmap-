# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — CORE THROUGH HUMAN WORKSPACE SHELL CLOSED FOR DESIGN

This file maps Ptah requirements to internal evidence, composite donors, native ownership, exit strategy and proof.

A requirement is never closed by naming one repository. Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

Design closure does **not** authorize implementation. Phase 0B schemas/conformance and Phase 0C slice approval remain mandatory.

---

# Requirements closed for Phase 0B contract design

| ID | Requirement | Native Ptah owner | Composite machinery/evidence | Evidence |
|---|---|---|---|---|
| CORE-001 | Persistent Workspace model | Workspace Provider | Daytona, Coder, E2B, Dev Containers, DevPod, local/OCI providers | WP02, ADR-0001 |
| CORE-002 | Concurrent Activity runtime | Activity Ledger | Temporal, NATS/JetStream, OTel and internal runtime/evidence systems | WP02, ADR-0003/0004 |
| CORE-003 | Universal Object graph | Object/Claim/Relationship/View contracts | internal recovery tools plus archive/document/binary/media/firmware parsers | WP05/06, ADR-0007/0008 |
| CORE-004 | Facility, Domain Pack and UI-contribution host foundation | Facility/Contribution manifests | OpenClaw/OpenHands/MCP, internal specialist bridges, parser/runtime/browser/shell adapters | WP02–WP09 |
| CORE-005 | Node Protocol and capabilities | Node Protocol | OpenClaw, provider agents, NATS, OTel, Device/Application/Browser Providers | WP01/02/07/08 |
| RELAY-001 | Live Events | Event Fabric | NATS/JetStream, OTel, internal bridge/outbox and runtime streams | WP02 |
| RELAY-002 | Durable recovery | Activity Ledger/checkpoints/receipts | Temporal, SQL, provider snapshots and internal workflows/outbox | WP02 |
| EXEC-001 | Terminal/process supervision | Process/PTY Facility | OS APIs, OpenClaw, Coder, E2B/OpenHands and internal workers | WP02 |
| EXEC-002 | OCI Workspace Provider | OCI Provider | containerd/OCI, Daytona, Dev Containers, DevPod, E2B/Coder | WP02 |
| EXEC-003 | Reproducible Build graph | Build Recipe/backend adapter | BuildKit, Dagger and internal Builder | WP03, ADR-0005 |
| STORE-001–005 | Storage classes, Object storage, catalogue, hashing and Drive recovery | Storage/Object/Location contracts | local CAS, SQL, R2/S3, ORAS, rclone and Drive | WP03/04 |
| XFER-001–003 | Upload, download and cloud/Node transfer | Transfer Facilities | tusd, Lumi, aria2, rclone, Syncthing and browser handoff | WP04/08 |
| SYNC-001 | Online/local revisions and conflicts | Revision/Conflict contracts | Hunter safe sync, Syncthing vectors and Object digests | WP04 |
| DECOMP-001/002 | Detection and recursive decomposition | Detector and Domain Pack contracts | Tika, libarchive, Binwalk, LIEF, ffprobe, libvips and internal tools | WP05 |
| DOC-001 | Document structure/render/proof | Document Domain Pack | Document Generator, Tika, Unstructured and renderers | WP05 |
| MEDIA-001 | Video/audio | Media Domain Pack | Creative Studio and FFmpeg/ffprobe | WP05 |
| IMAGE-001 | Image processing | Image Domain Pack | Creative Studio and libvips | WP05 |
| BIN-001 | Executable/binary decomposition | Binary Domain Pack | App Recover, LIEF and Binwalk | WP05 |
| APP-001 | APK/AAB/DEX decomposition | Android Application Domain Pack | APK Extractor, Apktool and JADX | WP05 |
| FW-001–006 | Apple, MTK, Unisoc, Qualcomm, OTA and other firmware | Firmware Domain Packs and Device adapters | internal evidence plus blacktop/ipsw, MTKClient, edl, PAC/FDL, AOSP image tools and vendor adapters | WP06 |
| FS-001 | Disks/partitions/filesystems | Disk/Image/Filesystem Packs | libfdisk, libguestfs and platform image machinery | WP06 |
| DEVICE-001/002 | Android inventory/control/display/input/semantic UI | Device Provider/Session/Stream/Screen Context | Device Manager, MIBU, STF, platform-tools, scrcpy, AndroidX UIA, Appium and TouchPilot | WP07A, ADR-0009 |
| APP-002 | Linux graphical/native runtime | Application Provider/Session/Window | native/OCI providers, Xpra, Guacamole and noVNC | WP07B, ADR-0010 |
| APP-003 | Windows EXE/MSI/UWP runtime | Windows native/VM Application Provider | QEMU/libvirt, FreeRDP/Guacamole, FlaUI and NovaWindows | WP07B, ADR-0010 |
| APP-004 | macOS/iOS runtime | macOS/iOS Application and Device Providers | Peekaboo, Appium XCUITest, IDB and Apple platform tooling | WP07B, ADR-0010 |
| BROWSE-001–003 | Persistent browser, rendered retrieval and evidence | Browser Provider/Profile/Context/Page/Evidence contracts | Playwright, Browser-Use, TurboWebFetch and Playwright MCP | WP08, ADR-0011 |
| UI-001 | Human Workspace shell | Shell Client/Session, Panel and Layout contracts | Theia, Dockview, OpenVSCode/code-server, xterm.js and internal UI evidence | WP09, ADR-0012 |
| UI-002 | Activity Centre, evidence and review | Activity/Evidence projection contracts | Activity Ledger, OTel, Receipts, Sergeant/MIBU patterns and runtime panels | WP09, ADR-0012 |
| SESSION-001 | Checkpoint/archive/export/import/resume | Session manifest | Workspace, storage, VM, Device, Application, Browser and Shell checkpoints/projections | WP02–WP09 |
| OBS-001 | Logs/metrics/traces/resource accounting | OTel conventions and human projections | OTel plus Build/runtime/device/application/browser/UI evidence | WP02–WP09 |
| PROV-001 | Provenance/signing/proof bundles | Provenance/Verification graph | Witness, in-toto, Sigstore, ORAS, Syft and runtime/UI evidence | WP03–WP09 |
| OFFLINE-001 | Intermittent Node operation | local journal/outbox and reconciliation | Event Fabric, revisions and runtime generations | WP02/04/07/08 |

## Closed-foundation notes

- `PLUGIN-001` has closed Facility, Domain Pack, Build-module and UI-contribution foundations; complete discovery/install/upgrade/rollback remains WP10.
- `DIST-001` has Node, Event, provider, Object-transfer, capability and UI foundations; scheduler quality and secure multi-Node placement remain open.
- Linux semantic automation retains an AT-SPI completion gap.
- JuiceFS/SeaweedFS are parked until measured shared-POSIX need.
- `.P5C` is parked pending a lawful immutable sample or authoritative format/tool.
- private device-manager modules that could not be audited remain an internal source-recovery gap.
- Hunter Foreman is excluded from active shell reuse unless explicitly reintroduced.

---

# Active WP10 — Knowledge, Data, Search and Plugin Composition

## SEARCH-001 — Unified source-grounded search and retrieval

**Status:** INTERNAL + RAGFLOW FIRST PASS COMPLETE; LLAMAINDEX ACTIVE

- Internal foundation recovered: Hunter chat/knowledge/memory separation, approval, local-first sync, sync proof state, degraded retrieval and provider-adapter patterns.
- Internal evidence: `internal/HUNTER-KNOWLEDGE-MEMORY-SEARCH.md`.
- Primary end-to-end donor recovered: RAGFlow ingestion pipelines, dataset/document state, hybrid retrieval, metadata filtering, backend abstraction and deletion/reconciliation lessons.
- RAGFlow evidence: `donors/RAGFLOW.md` pinned at `b7a3a2760f46dbdff1e0cce307bfb874944244b4`.
- Active primary library donor: LlamaIndex.
- Remaining completion: Dify knowledge/workflow patterns and Browser/Live Research source records.
- Native gap: Knowledge Source, Corpus, Document, Chunk, Index Revision, Query, Result, Citation, freshness, permissions, deletion, ranking explanation and backend-conformance contracts.
- Current invariant: Objects/Views and their revisions remain source truth; embeddings, chunks, indexes and retrieval caches are derived, versioned and replaceable.

## DATA-001 — Structured data, tables and database Activities

**Status:** INSPECTING DONORS

- Primary direction: Polars plus SQL/database Facilities.
- Completion: Object/Artifact storage, Build/Activity runtime and evidence contracts.
- Native gap: Dataset/Table/Query/Transformation identities, schemas, lazy/eager execution, result Artifacts, lineage and resource controls.

## PLUGIN-001 — General Facility/plugin lifecycle

**Status:** INSPECTING DONORS

- Foundation already closed: Facility manifests, Domain Packs, Build modules and UI contributions.
- Primary completion: MCP specification/servers, OpenClaw/ClawHub patterns, Deno tool runtime and OCI/Artifact distribution.
- Native gap: discovery, install, trust, permission, pin, health, activation, upgrade, migration, rollback, removal and replacement contracts.

## Knowledge and provider extensions

Resolve:

- source permissions, freshness, revision and deletion;
- embeddings/indexes as derived state rather than source truth;
- citation binding to exact Object/View/source revisions;
- local versus shared knowledge locations;
- provider-neutral model/data interfaces;
- external reasoning ownership;
- Dify/Hermes/agent systems as optional callers/workloads rather than Ptah Core;
- MCP as one adapter protocol rather than Ptah's internal object model.

---

# Remaining open clusters

| Cluster | Status | Direction |
|---|---|---|
| Strong isolation | OPEN | gVisor, Kata, Firecracker, youki and crun |
| Distributed placement | COMPOSITE CANDIDATE | Node/provider foundations exist; scheduler, leases and secure networking remain |
| Reproduction/security workloads | OPEN | SparkDistill, ClaimBound, ReproZip, GUAC, Strix, Semgrep, Trivy, ZAP and scanners |
| Research/documentation sources | OPEN | unresolved profiles/catalogues and public documentation tooling |
| Linux semantic UI | OPEN COMPLETION GAP | AT-SPI-specific donor pass |

---

# Current conclusion

Core runtime, Build/Artifact/Provenance, Storage/Transfer/Sync, Object/Decomposition, Firmware/Disk/Filesystem, Device/Application Runtime, Browser/Live Research and Human Workspace/UI are closed for **Phase 0B contract design**, not implementation.

Active Phase 0A group: Knowledge, Data, Search and Plugin Composition (`WP10`) as recorded in `CURRENT_STATE.md`.

Phase 0A cannot close until every v1 requirement is `CLOSED FOR DESIGN`, explicitly parked, or rejected with a replacement.
