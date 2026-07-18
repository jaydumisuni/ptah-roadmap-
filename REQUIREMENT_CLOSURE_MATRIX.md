# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — CORE THROUGH KNOWLEDGE/DATA/SEARCH/PLUGIN CLOSED FOR DESIGN

This file maps Ptah requirements to internal evidence, composite donors, native ownership, exit strategy and proof.

A requirement is never closed by naming one repository. Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

Design closure does **not** authorize implementation. Phase 0B schemas/conformance and Phase 0C slice approval remain mandatory.

---

# Requirements closed for Phase 0B contract design

| ID | Requirement | Native Ptah owner | Composite machinery/evidence | Evidence |
|---|---|---|---|---|
| CORE-001 | Persistent Workspace model | Workspace Provider | Daytona, Coder, E2B, Dev Containers, DevPod, local/OCI providers | WP02, ADR-0001 |
| CORE-002 | Concurrent Activity runtime | Activity Ledger | Temporal, NATS/JetStream, OTel and internal runtime/evidence systems | WP02, ADR-0003/0004 |
| CORE-003 | Universal Object graph plus knowledge-source/document extensions | Object/Claim/Relationship/View and Knowledge Source contracts | internal recovery tools, decomposition donors, Hunter, RAGFlow and LlamaIndex | WP05/06/10, ADR-0007/0008/0013 |
| CORE-004 | Facility, Domain Pack, UI and plugin contribution host | Facility/Contribution/Package manifests | OpenClaw/OpenHands/MCP, Deno, ClawHub, internal specialist bridges and UI/runtime adapters | WP02–WP10 |
| CORE-005 | Node Protocol and capabilities | Node Protocol | OpenClaw, provider agents, NATS, OTel and Device/Application/Browser Providers | WP01/02/07/08 |
| RELAY-001 | Live Events | Event Fabric | NATS/JetStream, OTel, internal bridge/outbox and runtime streams | WP02 |
| RELAY-002 | Durable recovery | Activity Ledger/checkpoints/receipts | Temporal, SQL, provider snapshots and internal workflows/outbox | WP02 |
| EXEC-001 | Terminal/process supervision | Process/PTY Facility | OS APIs, OpenClaw, Coder, E2B/OpenHands and internal workers | WP02 |
| EXEC-002 | OCI Workspace Provider | OCI Provider | containerd/OCI, Daytona, Dev Containers, DevPod, E2B/Coder | WP02 |
| EXEC-003 | Reproducible Build graph | Build Recipe/backend adapter | BuildKit, Dagger and internal Builder | WP03, ADR-0005 |
| STORE-001–005 | Storage classes, Object storage, catalogue, hashing and Drive recovery | Storage/Object/Location contracts | local CAS, SQL, R2/S3, ORAS, rclone and Drive | WP03/04 |
| XFER-001–003 | Upload, download and cloud/Node transfer | Transfer Facilities | tusd, Lumi, aria2, rclone, Syncthing and browser handoff | WP04/08 |
| SYNC-001 | Online/local revisions and conflicts | Revision/Conflict contracts | Hunter safe sync, Syncthing vectors and Object digests | WP04/10 |
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
| SEARCH-001 | Unified source-grounded search and retrieval | Knowledge Source/Corpus/Document/Chunk/Index/Query/Result/Citation contracts | Hunter, LlamaIndex, RAGFlow, Browser Facility, native lexical/SQL search and MCP adapters | WP10, ADR-0013 |
| DATA-001 | Structured datasets, tables and analytical Query Activities | Dataset/Table/Schema/Query/Transformation/Result contracts | Polars, DuckDB, Object/Artifact storage and Activity runtime | WP10, ADR-0013 |
| PLUGIN-001 | Package/plugin discovery, install, activation, upgrade, rollback and removal | Package/Release/Installed Plugin/Activation contracts | ClawHub, OpenClaw, MCP, Deno, Dify patterns, OCI/Artifact/provenance machinery | WP10, ADR-0013 |
| SESSION-001 | Checkpoint/archive/export/import/resume | Session manifest | Workspace, storage, VM, Device, Application, Browser, Shell, Knowledge and Plugin checkpoints/projections | WP02–WP10 |
| OBS-001 | Logs/metrics/traces/resource accounting | OTel conventions and human projections | OTel plus Build/runtime/device/application/browser/UI/knowledge/data/plugin evidence | WP02–WP10 |
| PROV-001 | Provenance/signing/proof bundles | Provenance/Verification graph | Witness, in-toto, Sigstore, ORAS, Syft and runtime/knowledge/plugin evidence | WP03–WP10 |
| OFFLINE-001 | Intermittent Node operation | local journal/outbox and reconciliation | Event Fabric, revisions, runtime generations and local-first knowledge/index providers | WP02/04/07/08/10 |

## Closed-foundation notes

- `DIST-001` has Node, Event, provider, Object-transfer, capability and UI foundations; scheduler quality, isolation selection and secure multi-Node placement remain open in WP11.
- Linux semantic automation retains an AT-SPI completion gap.
- JuiceFS/SeaweedFS are parked until measured shared-POSIX need.
- `.P5C` is parked pending a lawful immutable sample or authoritative format/tool.
- private device-manager modules that could not be audited remain an internal source-recovery gap.
- Hunter Foreman is excluded from active shell reuse unless explicitly reintroduced.
- Dify remains study-only or separately licensed because of its modified licence.
- MiniRouter remains study-only until a repository licence is resolved and belongs to later routing evaluation.

---

# WP10 closure summary

## SEARCH-001 — CLOSED FOR DESIGN

- Source truth, derived indexes, Queries, Results, Citations and caller-owned memory are separate.
- Source Objects/View revisions are authoritative; embeddings and indexes are rebuildable derived state.
- Exact Citations bind to exact permitted source revisions and ranges.
- LlamaIndex is the primary modular local foundation candidate; RAGFlow is an optional heavier Facility.
- Backend conformance, freshness, deletion, tombstones, reconciliation and permissions are native Ptah responsibilities.

## DATA-001 — CLOSED FOR DESIGN

- Ptah owns Dataset, Table, Column Schema, snapshot, Data Query, Transformation, Result and lineage identities.
- Polars is the primary local lazy/streaming DataFrame engine candidate.
- DuckDB is the primary embedded SQL analytical engine candidate.
- Transactional databases remain separate Facilities.

## PLUGIN-001 — CLOSED FOR DESIGN

- Package, immutable Package Release, Installed Plugin, Activation and Registry Entry are separate.
- Family, executes-code state, runtime class, permissions, resources, digest, signature, SBOM and provenance are explicit.
- Discovery, scans and registry trust are evidence inputs rather than approval.
- Deno is the lightweight runtime candidate; stronger isolation is selected by risk.
- MCP is an external adapter, not Ptah's internal model.
- Upgrade/migration/health/rollback and full removal cleanup are Activity-driven.

Evidence:

- `work-packages/PHASE-0A-WP10-KNOWLEDGE-DATA-SEARCH-PLUGIN.md`
- `decisions/ADR-0013-KNOWLEDGE-DATA-SEARCH-PLUGIN-BOUNDARY.md`

---

# Active WP11 — Strong Isolation and Distributed Placement/Scheduling

## ISOLATION-001 — Runtime isolation classes and escalation

**Status:** ACTIVE

- Primary donors: gVisor, Kata Containers and Firecracker.
- OCI/runtime completion: containerd, youki and crun.
- Native gap: runtime classes, threat/risk selection, host capability checks, network/credential/object scopes, checkpoint support, failure evidence and fallback.

## DIST-001 — Distributed placement and scheduling

**Status:** ACTIVE COMPOSITE CANDIDATE

- Existing foundations: Node Protocol, Provider generations, Activity runtime, capability announcements, Object transfer, leases/fencing, checkpoints and UI projections.
- Primary completion donor: Ray plus lower-level Node/provider scheduling patterns recovered during WP11.
- MiniRouter is only a future routing/evaluation workload, not the scheduler or Core reasoning layer.
- Native gap: resource/capability snapshots, reservation, placement, data gravity, locality, accelerator/cost policy, secure networking, rescheduling, recovery and degraded one-Node fallback.

---

# Remaining open clusters

| Cluster | Status | Direction |
|---|---|---|
| Strong isolation and distributed placement | ACTIVE | WP11: gVisor, Kata, Firecracker, youki, crun, Ray and native placement contracts |
| Reproduction/security workloads | OPEN | SparkDistill, ClaimBound, ReproZip, GUAC, Strix, Semgrep, Trivy, ZAP and scanners |
| Research/documentation sources | OPEN | unresolved profiles/catalogues and public documentation tooling |
| Linux semantic UI | OPEN COMPLETION GAP | AT-SPI-specific donor pass |

---

# Current conclusion

Core runtime, Build/Artifact/Provenance, Storage/Transfer/Sync, Object/Decomposition, Firmware/Disk/Filesystem, Device/Application Runtime, Browser/Live Research, Human Workspace/UI and Knowledge/Data/Search/Plugin are closed for **Phase 0B contract design**, not implementation.

Active Phase 0A group: Strong Isolation and Distributed Placement/Scheduling (`WP11`) as recorded in `CURRENT_STATE.md`.

Phase 0A cannot close until every v1 requirement is `CLOSED FOR DESIGN`, explicitly parked, or rejected with a replacement.
