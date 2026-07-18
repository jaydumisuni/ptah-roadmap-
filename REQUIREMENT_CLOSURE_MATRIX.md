# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** ALL V1 REQUIREMENTS CLOSED FOR DESIGN — FINAL CONSISTENCY/FREEZE REVIEW ACTIVE

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
| CORE-005 | Node Protocol, capabilities and placement input | Node Protocol/Capability Snapshot | OpenClaw, provider agents, NATS, OTel, Device/Application/Browser Providers and WP11 runtime inventory | WP01/02/07/08/11 |
| RELAY-001 | Live Events | Event Fabric | NATS/JetStream, OTel, internal bridge/outbox and runtime streams | WP02 |
| RELAY-002 | Durable recovery | Activity Ledger/checkpoints/receipts | Temporal, SQL, provider snapshots and internal workflows/outbox | WP02/11 |
| EXEC-001 | Terminal/process supervision | Process/PTY Facility | OS APIs, OpenClaw, Coder, E2B/OpenHands and internal workers | WP02 |
| EXEC-002 | OCI Workspace Provider and runtime variants | OCI Provider | containerd/OCI, Daytona, Dev Containers, runc, crun, youki and stronger isolation escalation | WP02/11, ADR-0014 |
| EXEC-003 | Reproducible Build graph | Build Recipe/backend adapter | BuildKit, Dagger and internal Builder | WP03, ADR-0005 |
| STORE-001–005 | Storage classes, Object storage, catalogue, hashing and Drive recovery | Storage/Object/Location contracts | local CAS, SQL, R2/S3, ORAS, rclone and Drive | WP03/04 |
| XFER-001–003 | Upload, download and cloud/Node transfer | Transfer Facilities | tusd, Lumi, aria2, rclone, Syncthing, browser handoff and placement/data-locality integration | WP04/08/11 |
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
| APP-002 | Linux graphical/native runtime and semantic UI | Application Provider/Session/Window/Semantic Context | native/OCI providers, Xpra, Guacamole, noVNC, AT-SPI/libatspi, Dogtail patterns and GNOME Ponytail | WP07B, ADR-0010/0015 |
| APP-003 | Windows EXE/MSI/UWP runtime | Windows native/VM Application Provider | QEMU/libvirt, FreeRDP/Guacamole, FlaUI and NovaWindows | WP07B, ADR-0010 |
| APP-004 | macOS/iOS runtime | macOS/iOS Application and Device Providers | Peekaboo, Appium XCUITest, IDB and Apple platform tooling | WP07B, ADR-0010 |
| BROWSE-001–003 | Persistent browser, rendered retrieval and evidence | Browser Provider/Profile/Context/Page/Evidence contracts | Playwright, Browser-Use, TurboWebFetch and Playwright MCP | WP08, ADR-0011 |
| UI-001 | Human Workspace shell | Shell Client/Session, Panel and Layout contracts | Theia, Dockview, OpenVSCode/code-server, xterm.js and internal UI evidence | WP09, ADR-0012 |
| UI-002 | Activity Centre, evidence and review | Activity/Evidence projection contracts | Activity Ledger, OTel, Receipts, Sergeant/MIBU patterns and runtime panels | WP09, ADR-0012 |
| SEARCH-001 | Unified source-grounded search and retrieval | Knowledge Source/Corpus/Document/Chunk/Index/Query/Result/Citation contracts | Hunter, LlamaIndex, RAGFlow, Browser Facility, native lexical/SQL search and MCP adapters | WP10, ADR-0013 |
| DATA-001 | Structured datasets, tables and analytical Query Activities | Dataset/Table/Schema/Query/Transformation/Result contracts | Polars, DuckDB, Object/Artifact storage and Activity runtime | WP10, ADR-0013 |
| PLUGIN-001 | Package/plugin discovery, install, activation, upgrade, rollback and removal | Package/Release/Installed Plugin/Activation contracts | ClawHub, OpenClaw, MCP, Deno, Dify patterns, OCI/Artifact/provenance and isolation machinery | WP10/11, ADR-0013/0014 |
| ISOLATION-001 | Runtime isolation classes, provider selection and no-silent-weakening escalation | Isolation Class/Runtime Provider/Secure Grant contracts | runc/containerd, crun, youki, gVisor, Kata, Firecracker, full VM and Deno/WASM foundations | WP11, ADR-0014 |
| DIST-001 | Node capability, placement, reservation, lease, fencing and distributed execution | Capability Snapshot/Placement/Reservation/Lease/Fence contracts | Node/Activity foundations, Ray, Object transfer, provider generations, gVisor/Kata/Firecracker runtime classes | WP11, ADR-0014 |
| SEC-001 | Authorized security assessment, Finding lifecycle, remediation and re-test | Security Authorization/Assessment/Finding/Disposition/Verification contracts | Semgrep, Syft, Grype, Trivy, GUAC, ZAP, Strix plus isolation/provenance/review foundations | Security/reproduction WP, ADR-0016 |
| REPRO-001 | Frozen protocol, replay/re-execution, bounded claim and independent reproduction | Protocol/Reproduction Run/Claim/Evidence Card contracts | ReproZip, ClaimBound, SparkDistill plus Build/Artifact/Receipt/provenance machinery | Security/reproduction WP, ADR-0016 |
| SESSION-001 | Checkpoint/archive/export/import/resume | Session/Checkpoint Bundle | Workspace, storage, VM, Device, Application, Browser, Shell, Knowledge, Plugin, CRIU, gVisor/Kata/Firecracker and Ray/application checkpoints | WP02–WP11 |
| OBS-001 | Logs/metrics/traces/resource accounting | OTel conventions, resource/pressure and human projections | OTel plus Build/runtime/device/application/browser/UI/knowledge/data/plugin/placement/security evidence | WP02–WP11 plus security/reproduction closure |
| PROV-001 | Provenance/signing/proof bundles | Provenance/Verification graph | Witness, in-toto, Sigstore, ORAS, Syft and runtime/knowledge/plugin/isolation/placement/security/reproduction evidence | WP03–WP11 plus ADR-0016 |
| OFFLINE-001 | Intermittent Node operation | local journal/outbox, generations and reconciliation | Event Fabric, revisions, runtime generations, local-first providers and rescheduling/checkpoint rules | WP02/04/07/08/10/11 |

---

# Closed-foundation notes

- Linux semantic automation is closed through `donors/AT-SPI.md`, the Linux semantic work package and ADR-0015; exact GNOME Ponytail dependency approval remains Phase 0B/0C selection work.
- JuiceFS/SeaweedFS are parked until measured shared-POSIX need.
- `.P5C` is parked pending a lawful immutable sample or authoritative format/tool.
- private device-manager modules that could not be audited remain an internal source-recovery gap with existing public/native fallback contracts.
- Hunter Foreman is excluded from active shell reuse unless explicitly reintroduced.
- Dify remains study-only or separately licensed because of its modified licence.
- MiniRouter remains study-only until a repository licence is resolved and is only a future routing/evaluation workload.
- Design closure of `ISOLATION-001`/`DIST-001` does not select one production runtime, scheduler or Node topology.
- Strix remains an authorized high-risk workload, not a production security authority or proof engine.
- ClaimBound Evidence Cards are presentation Views and SparkDistill is an optional specialist workload; neither replaces Ptah Activities, Claims or review.
- `chrisipanaque` prototypes remain parked for source reuse pending exact need, compatible licence and independent proof.
- `amertoglu16.github.io` remains parked because no recoverable implementation source was found.
- research catalogues, profiles and documentation frameworks do not close runtime requirements or alter this matrix.

---

# Research/documentation cleanup — COMPLETE

- `aza-ali/awesome-ai-product-management` is an optional versioned Research Source.
- `tmimmanuel` is discovery lineage only.
- Chris/Christiam Ipanaque identity is resolved to `chrisipanaque`; profile claims and prototypes are not architecture evidence.
- `amertoglu16.github.io` is parked with reopening criteria.
- Crisp Links is an optional README asset generator.
- Material for MkDocs is the primary lightweight documentation-site candidate, not selected.
- Docusaurus is an optional richer documentation/project-site alternative.
- Mermaid is the primary text-defined documentation-diagram candidate.
- documentation outputs are derived Artifacts and public builds use allowlisted public source only.

Evidence:

- `donors/RESEARCH-DISCOVERY-SOURCES.md`
- `donors/DOCUMENTATION-PRESENTATION-TOOLS.md`
- `work-packages/PHASE-0A-RESEARCH-DOCUMENTATION-SOURCE-CLEANUP.md`

---

# Remaining open Phase 0A work

| Review unit | Status | Required result |
|---|---|---|
| Cross-requirement identity/authority/state/lifecycle consistency | ACTIVE | no unresolved contradictions across ADRs, work packages and schemas |
| Parked/rejected/blocked gap audit | OPEN | explicit reopening criteria and v1 consequence for every item |
| Phase 0B input/proof-corpus enumeration | OPEN | schema, migration, conformance, golden and negative-evidence checklist |
| Phase 0A freeze/readiness decision | OPEN | accepted freeze or named blocking gaps; implementation still prohibited |

---

# Current conclusion

Every current v1 architecture requirement is closed for **Phase 0B contract design**, not implementation.

No research catalogue, profile, documentation tool or unresolved stale link remains an architecture gap.

Phase 0A now requires only the consistency, parked-gap and Phase 0B-input review recorded in `CURRENT_STATE.md`. Phase 0A cannot freeze until those checks pass and all roadmap references agree.
