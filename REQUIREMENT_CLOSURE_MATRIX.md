# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — WORK PACKAGE 01 RECORDED

This file is the decisive map between the accepted Ptah requirements, internal work, external donors, mature upstream machinery, and native Ptah implementation.

A requirement is not closed by naming a repository. It is closed only when the exact implementation boundary and proof path are known.

---

# Status values

- `OPEN`
- `RECOVERING INTERNAL WORK`
- `INSPECTING DONORS`
- `CANDIDATE SELECTED`
- `LICENCE REVIEW`
- `VALIDATION REQUIRED`
- `CLOSED FOR DESIGN`
- `REJECTED PATH`
- `PARKED`

---

# Matrix

| ID | Requirement | Roadmap phase | Internal evidence | Primary donor | Secondary / exit donor | Mature upstream machinery | Native Ptah gap | Public/private boundary | Licence decision | Integration classification | Validation activity | Evidence | Status |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| CORE-001 | Persistent workspace model | 1 | Internal project/workspace patterns still recovering | Native Ptah Workspace Provider contract; Daytona studied for lifecycle | Coder, E2B, Dev Containers | OCI/containerd; local filesystem | Neutral provider lifecycle; object/activity/session separation; local and remote providers | Public neutral contract; private consumers external | Daytona AGPL prevents code adoption without review | Native implementation + architecture study | Provider conformance suite; two concurrent workspaces; lifecycle recovery | `donors/DAYTONA.md`; ADR-0001 | CANDIDATE SELECTED |
| CORE-002 | Concurrent activity runtime | 1 | Foreman, AgentOps, Sergeant and build workers still recovering | TBD after Temporal/NATS inspection | Ray, Celery, internal worker patterns | OS processes and async runtime | Durable concurrent activity state independent of workspaces | Public neutral runtime | TBD | TBD | Ten independent activities, isolated failure and reconnect | TBD | INSPECTING DONORS |
| CORE-003 | Object graph and catalogue | 1–3 | App Recover, APK Extractor, Creative Studio and source mirrors still recovering | TBD | Tika, libarchive, LIEF, domain packs | Content hashes and local/object storage | Universal object identity, relationships, provenance and derivatives | Public schema; private objects remain external | TBD | TBD | Mixed recursive decomposition with immutable original | TBD | RECOVERING INTERNAL WORK |
| CORE-004 | Facility and plugin host | 0B–1 | Internal engine boundaries still recovering | TBD | OpenClaw plugin patterns, MCP adapters | Process/container/plugin interfaces | Neutral facility manifest, lifecycle and multi-language host | Public SDK; private adapters external | TBD | TBD | Load, health-check, upgrade, rollback and unload adapter | TBD | INSPECTING DONORS |
| CORE-005 | Node protocol and capability reporting | 1, 12 | TechGuy Relay and device-node work still recovering | Native Ptah Node Protocol adapted from OpenClaw patterns | NATS, OpenClaw organisation node projects | WebSocket first; separate data streams | Neutral resources/facilities, reconnect epoch, event cursor, binary streams and multi-language SDK | Public neutral protocol; no private consumer identity | OpenClaw MIT compatible with selective adaptation and notices | Selective adaptation + native contract | Handshake, capability refresh, heartbeat, invoke, cancel, reconnect and stream separation | `donors/OPENCLAW.md`; ADR-0001 | VALIDATION REQUIRED |
| RELAY-001 | Live event transport | 1 | Existing relay experiments still recovering | OpenClaw envelope for public protocol; NATS inspection pending for internal fabric | WebSocket/SSE alternatives | NATS candidate; WebSocket control link | Transport abstraction, sequence/replay, backpressure and stream routing | Public envelope; internal bus implementation replaceable | OpenClaw MIT; NATS licence pending record | Protocol adaptation; internal donor still pending | Ordered events, reconnect cursor, bounded buffering and backpressure | `donors/OPENCLAW.md`; ADR-0001 | INSPECTING DONORS |
| RELAY-002 | Durable activity recovery | 1, 8 | Internal job/recovery patterns still recovering | Temporal inspection pending | JetStream, native database-backed coordinator | Durable database and worker leases | Workflow history, checkpoint, retries, timers and recovery | Public activity semantics; backend replaceable | TBD | TBD | Kill control plane and node during long activity, then recover exactly | TBD | OPEN |
| STORE-001 | Hot local workspace storage | 1–2 | Internal local workbench patterns still recovering | TBD | Coder/Daytona storage patterns | Linux filesystem and volumes | Storage classes, mounts, quota/health and object links | Public-neutral storage contract | TBD | TBD | Concurrent workspace I/O and restart persistence | TBD | OPEN |
| STORE-002 | Durable object storage | 2 | R2 usage patterns exist | TBD | S3-compatible providers, ORAS | R2/S3 | Object catalogue, retention, multipart and backend neutrality | Public S3-compatible contract; private buckets external | TBD | TBD | Store, recover and verify by object ID/hash | TBD | OPEN |
| STORE-003 | Metadata catalogue | 1–2 | D1/SQLite patterns exist | TBD | PostgreSQL/D1 | SQLite and SQL | Versioned graph, migrations and sync | Public schema; deployment private | TBD | TBD | Restore catalogue after restart and migration | TBD | OPEN |
| STORE-004 | Content hashing and deduplication | 1–2 | Partial checksum patterns exist | TBD | ORAS/CAS patterns | Cryptographic hashing | Streaming hash, chunk identity, dedupe and integrity repair | Public | TBD | TBD | Same content enters by three paths and stores once | TBD | OPEN |
| STORE-005 | Drive export and recovery | 2, 8 | Google recovery rules exist | TBD | OpenClaw Google tools, rclone | Google Drive API | Export manifest, resumability and import | Private connection references | TBD | TBD | Export and import a session bundle | TBD | OPEN |
| XFER-001 | Resumable uploads | 2 | Internal upload flows exist | TBD | tus/tusd | HTTP multipart/object storage | Unified intake and object registration | Public endpoint; private storage external | TBD | TBD | Interrupt and resume large upload | TBD | OPEN |
| XFER-002 | Fast resumable downloads | 2 | Download Manager recovery required | TBD | aria2 | HTTP range/mirror protocols | Native queue, object landing, browser handoff and progress | Public facility | TBD | TBD | Multi-source interrupted download recovery | TBD | RECOVERING INTERNAL WORK |
| XFER-003 | Cloud and node synchronization | 2, 12 | Online/local sync rules exist | TBD | rclone, Syncthing | S3/Drive/node transports | Object-aware sync and conflict model | Public-neutral; private connections external | TBD | TBD | Offline edits and object dedupe across nodes | TBD | OPEN |
| GIT-001 | Mirrors, worktrees, branches, tags, commits | 5 | Git-based ecosystem exists | TBD | Coder/OpenHands patterns | Git | Mirror catalogue, concurrency and artifact links | Public | TBD | TBD | Two worktrees share mirror without collision | TBD | OPEN |
| EXEC-001 | Terminal and process supervision | 1 | Internal terminal/process patterns still recovering | Native Ptah process facility; OpenClaw terminal semantics studied | OpenHands, Coder | OS PTY/process APIs | Multi-terminal ownership, detach/replay, activity links and node portability | Public neutral facility | OpenClaw MIT for selective patterns | Native implementation + selective adaptation | Detach, reconnect, replay, cancel and isolate terminal failure | `donors/OPENCLAW.md`; ADR-0001 | VALIDATION REQUIRED |
| EXEC-002 | OCI/container workspace provider | 5 | Internal Docker/build work still recovering | Native Ptah OCI provider; Daytona architecture study | Coder, E2B, Dev Containers | containerd/OCI | Provider conformance, lifecycle mapping, object/session links and exit strategy | Public neutral provider | Daytona AGPL study only; runtime licences pending | Native implementation over mature OCI machinery | Create two providers, execute independently, snapshot/restore where supported | `donors/DAYTONA.md`; ADR-0001 | CANDIDATE SELECTED |
| EXEC-003 | Reproducible build graph | 5 | Software Builder recovery required | TBD | Dagger | BuildKit | Ptah recipe/activity/artifact bridge | Public facility; private signing adapters external | TBD | TBD | Parallel cached build and reproducible artifact | TBD | OPEN |
| EXEC-004 | Stronger isolation backends | 5, 12 | None selected | TBD | gVisor, Kata, Firecracker | OCI/KVM | Provider adapters and capability model | Public | TBD | TBD | Same workload against supported backends | TBD | OPEN |
| BROWSE-001 | Interactive persistent browser | 6 | Website/browser work exists | TBD | Browser-Use, TurboWebFetch | Playwright/Chromium | Persistent activity/session/browser object contract | Public | TBD | TBD | Multiple authenticated contexts and reconnect | TBD | OPEN |
| BROWSE-002 | Rendered extraction and research | 6 | Research requirements documented | TBD | TurboWebFetch | Chromium/Playwright | Object registration, batch activity and source provenance | Public | TBD | TBD | Concurrent rendered extraction with retained sources | TBD | OPEN |
| BROWSE-003 | Screenshots, recordings, traces, network, console | 6 | Proof screenshot patterns exist | TBD | Browser-Use | Playwright | Unified artifact/provenance bridge | Public | TBD | TBD | Capture all evidence from one browser activity | TBD | OPEN |
| DECOMP-001 | True-type detection | 3 | Internal file tools exist | TBD | Apache Tika/file signatures | MIME/magic | Universal detection confidence and routing | Public | TBD | TBD | Misnamed mixed corpus detection | TBD | OPEN |
| DECOMP-002 | Recursive archive decomposition | 3 | Internal extraction tools exist | TBD | internal tools | libarchive | Recursive object graph and extraction budgets | Public | TBD | TBD | Nested mixed archive proof | TBD | OPEN |
| DOC-001 | Document extraction, structure, rendering, proof | 3, 10 | Document Generator exists | TBD | Unstructured/Tika | Office/PDF renderers | Neutral source/render/page graph | Public facility; private templates external | TBD | TBD | DOCX/PDF structure and rendered proof | TBD | OPEN |
| MEDIA-001 | Video/audio inspection and transformation | 3 | Creative Studio exists | TBD | internal media work | FFmpeg | Activity/object adapter and proxy strategy | Public | TBD | TBD | Concurrent derivatives from one source | TBD | OPEN |
| IMAGE-001 | Fast image processing and previews | 3 | Creative Studio exists | TBD | internal image work | libvips | Object/preview adapter | Public | TBD | TBD | Large image progressive preview | TBD | OPEN |
| BIN-001 | PE/ELF/Mach-O and binary decomposition | 3 | App Recover exists | TBD | internal recovery work | LIEF | Neutral executable graph and proof levels | Public | TBD | TBD | Cross-platform binary corpus | TBD | OPEN |
| APP-001 | APK/AAB/DEX decomposition | 3, 9 | APK Extractor exists | TBD | internal extractor | JADX/Apktool | Object graph, signatures and runtime bridge | Public | TBD | TBD | APK decompose and launch | TBD | OPEN |
| FW-001 | Apple firmware family | 4 | Apple research repos exist | TBD | internal Apple work | blacktop/ipsw | Public-neutral adapter and object graph | Public generic; private operations external | TBD | TBD | IPSW inventory/decompose/compare | TBD | OPEN |
| FW-002 | MediaTek firmware family | 4 | Strong internal MTK/META work exists | TBD | MTKClient | Specialist parsers/tools | Neutral package/device separation | Public generic; private repair chain external | TBD | TBD | Scatter bundle graph and device adapter proof | TBD | RECOVERING INTERNAL WORK |
| FW-003 | Unisoc firmware family | 4 | Internal SPD/Unisoc work exists | TBD | PAC/FDL donors | Vendor tools/formats | Verified parser and fixtures | Public generic | TBD | TBD | PAC object graph | TBD | RECOVERING INTERNAL WORK |
| FW-004 | Qualcomm firmware family | 4 | Internal Qualcomm work exists | TBD | EDL/Firehose donors | LIEF/XML parsers | Semantic rawprogram/patch graph | Public generic | TBD | TBD | XML/MBN directory validation | TBD | RECOVERING INTERNAL WORK |
| FW-005 | Generic Android OTA and dynamic partitions | 4 | OTA work exists | TBD | payload tools | Android platform tooling | Unified partition/filesystem graph | Public | TBD | TBD | Payload and super image proof | TBD | RECOVERING INTERNAL WORK |
| FW-006 | Other vendor and embedded firmware packs | 4 | Partial internal references | TBD | Binwalk/vendor donors | Domain tools | Plugin packs and golden fixtures | Public generic | TBD | TBD | At least two additional families | TBD | OPEN |
| FS-001 | Disk, partition, image, and filesystem facility | 4 | Device/image work exists | TBD | libguestfs/tooling donors | OS filesystem tools | Neutral mount/convert/extract contract | Public | TBD | TBD | Sparse/raw/dynamic/filesystem proof | TBD | OPEN |
| DEVICE-001 | Android device inventory and ADB | 9 | Device Manager/MIBU/ADB exist | TBD | STF/adbkit/Appium | Android platform tools | Neutral device state and activity bridge | Public generic; private workflows external | TBD | TBD | Multi-device inventory and unstable reconnect | TBD | RECOVERING INTERNAL WORK |
| DEVICE-002 | Android screen, input, semantic UI, and recording | 9 | Device work exists | TBD | TouchPilot/STF/Appium/scrcpy | Android UIAutomator | Unified screen/action/trace contract | Public | TBD | TBD | Interactive APK session with traces | TBD | OPEN |
| APP-002 | Linux graphical and native application runtime | 9 | TBD | TBD | E2B Desktop/Coder | Linux desktop/remote display | App/session/display adapter | Public | TBD | TBD | Launch and interact with Linux app | TBD | OPEN |
| APP-003 | Windows EXE/MSI runtime | 9 | Athena and Windows tools exist | TBD | Appium/remote desktop donors | Windows VM/native node | Windows provider and snapshots | Public generic; private node external | TBD | TBD | Clean install, interact and restore | TBD | OPEN |
| APP-004 | Apple IPA/macOS runtime | 9 | Apple work exists | TBD | Appium/Peekaboo | macOS/Xcode | Apple node/provider and signed runtime | Public generic; private hardware external | TBD | TBD | Simulator/device proof | TBD | OPEN |
| UI-001 | Human workspace shell | 7 | Existing UIs provide requirements | TBD | OpenVSCode | Theia | Ptah-specific object/activity/app panels | Public | TBD | TBD | Direct human completes vertical slice | TBD | OPEN |
| UI-002 | Activity Centre | 7 | Foreman/Sergeant status patterns exist | TBD | OpenHands/Coder patterns | Web UI framework | Unified concurrent activity view | Public | TBD | TBD | Ten live activities remain independently operable | TBD | OPEN |
| SESSION-001 | Checkpoint, archive, export, import, resume | 8 | Recovery rules exist | TBD | Daytona/Coder/ReproZip patterns | Storage snapshots | Cross-provider session manifest | Public schema; private storage external | TBD | TBD | Restart and cross-compatible resume | TBD | OPEN |
| SYNC-001 | Online/local synchronization and conflicts | 8, 12 | Hunter sync principles documented | TBD | Syncthing/rclone patterns | Object hashes/SQL revisions | Explicit authority, conflicts and activity ownership | Public-neutral | TBD | TBD | Offline divergence and merge proof | TBD | OPEN |
| SEARCH-001 | Unified search and indexing | 10 | Search requirements exist | TBD | RAGFlow/LlamaIndex | Search databases | Multi-domain object index | Public | TBD | TBD | Search files, docs, code, firmware and logs | TBD | OPEN |
| DATA-001 | Structured data and database pack | 10 | Pay/data systems exist | TBD | Polars/database donors | SQL engines | Neutral data object and query activities | Public | TBD | TBD | Large structured dataset activity | TBD | OPEN |
| PLUGIN-001 | Plugin discovery, pinning, health, upgrade, rollback | 10 | Internal adapter patterns exist | TBD | OpenClaw/ClawHub patterns | Package/OCI registries | Neutral manifest, compatibility and rollback | Public SDK | TBD | TBD | Install, health, upgrade, rollback and remove | TBD | OPEN |
| OBS-001 | Logs, metrics, traces, correlation, resource accounting | 1, 11 | Internal logging/proof patterns exist | TBD | Daytona/OpenClaw patterns | OpenTelemetry | Ptah correlation IDs and object/activity links | Public schema; deployment private | TBD | TBD | Trace one operation across control, node, provider and artifact | TBD | OPEN |
| PROV-001 | Provenance, attestations, signing, and proof bundles | 11 | Sergeant/MIBU evidence patterns exist | TBD | SparkDistill/ClaimBound | Witness/in-toto/Cosign/ORAS | Unified evidence and claim boundary | Public | TBD | TBD | Independently verify produced artifact | TBD | OPEN |
| SEC-001 | Security workload hosting and evidence | 11 | Internal security/device work exists | TBD | Strix/Semgrep/ZAP | Trivy/Syft/Grype | Workload adapter and normalized findings | Public workload surface | TBD | TBD | Parallel security workload proof | TBD | OPEN |
| DIST-001 | Multi-node capability placement and transfer | 12 | Relay/device experiments still recovering | Native Ptah Node Protocol + future scheduler | OpenClaw node patterns; Ray/MiniRouter later | NATS and object transfer machinery | Resource telemetry, placement, leases and transfer | Public protocol; private topology external | OpenClaw MIT for patterns | Native implementation + selective adaptation | Two nodes advertise different capabilities; route and recover activity | `donors/OPENCLAW.md`; ADR-0001 | INSPECTING DONORS |
| OFFLINE-001 | Local-first and intermittent-connectivity operation | 12 | Online/local design principles exist | Native Ptah reconnect model | OpenClaw background presence; Syncthing later | Durable local catalogue and queue | Offline activity ownership, event replay and conflict handling | Public neutral contract | OpenClaw MIT for patterns | Native implementation + architecture study | Disconnect node, continue permitted local work, reconnect and reconcile | `donors/OPENCLAW.md`; ADR-0001 | INSPECTING DONORS |

---

# Work package 01 conclusion

- OpenClaw is the primary architecture donor for the Node Protocol, not a direct runtime dependency.
- Daytona is a historical architecture donor for the Workspace Provider contract, not an adopted codebase.
- Node and Workspace are now explicitly separate contracts.
- `CORE-005`, `CORE-001`, `EXEC-001` and `EXEC-002` have candidate design paths but still require validation.
- `RELAY-001`, `DIST-001` and `OFFLINE-001` remain open to NATS, Temporal, synchronization and scheduler inspection.

---

# Completion rule

Phase 0A cannot close until every v1 row is either:

- `CLOSED FOR DESIGN`, with evidence and exit strategy;
- explicitly `PARKED` outside v1;
- or `REJECTED PATH`, with reason and replacement.