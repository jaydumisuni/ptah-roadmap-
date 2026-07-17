# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — WP02A SAVED

This is the decisive map between accepted Ptah requirements, internal work, external donors, mature upstream machinery and native Ptah implementation.

A requirement is not closed by naming one repository. Closure requires a complete donor composition, a native Ptah boundary, licence and exit decisions, and a proof path.

Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

---

# Status values

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

# Active core-runtime cluster

## CORE-001 — Persistent Workspace model

**Phase:** 1  
**Status:** COMPOSITE CANDIDATE

- Internal foundation: project/workspace patterns still recovering.
- Primary capability: native Ptah Workspace Provider contract.
- Lifecycle donor: Daytona.
- Completion donors: Coder, E2B, Dev Containers, Dev Container CLI and DevPod.
- Mature machinery: local Linux processes, containerd and OCI.
- Native Ptah gap: provider-neutral lifecycle; Workspace/Object/Activity/Session separation; local/remote/native/container/VM/device provider families; capability and conformance model.
- Licence: Daytona and Coder AGPL study-only; E2B Apache-2.0; Dev Container CLI MIT; DevPod MPL-2.0; OCI/containerd Apache-2.0.
- Integration: native contract with optional provider and compatibility adapters.
- Exit: no external control plane is mandatory.
- Validation: local and OCI providers plus one optional external provider must pass the same conformance suite; two Workspaces run concurrently; provider replacement preserves Ptah identity.
- Evidence: `donors/DAYTONA.md`, `donors/CODER.md`, `donors/E2B.md`, `donors/DEV-CONTAINERS-SPEC.md`, `donors/DEV-CONTAINERS-CLI.md`, `donors/DEVPOD.md`, `donors/CONTAINERD-OCI.md`, ADR-0001 and WP02A.

## CORE-002 — Concurrent Activity runtime

**Phase:** 1  
**Status:** INSPECTING DONORS

- Internal foundation: Foreman, AgentOps, Sergeant and existing workers still recovering.
- Primary donor: pending Temporal inspection.
- Completion donors: NATS/JetStream, OpenHands event/tool patterns, internal workers and later scheduler donors.
- Mature machinery: OS processes, async runtime and durable SQL state.
- Native Ptah gap: durable concurrent Activity identity independent of Workspace; cancellation; leases; retries; timers; recovery; dependency graphs; resource accounting.
- Validation: at least ten independent Activities; isolated failure; control-plane and Node restarts; exact recovery and replay.

## CORE-004 — Facility and plugin host

**Phase:** 0B–1  
**Status:** INSPECTING DONORS

- Internal foundation: internal engine boundaries still recovering.
- Donors: OpenClaw plugin patterns, OpenHands tools/SDK, MCP and later ClawHub.
- Mature machinery: process, container and service adapters.
- Native Ptah gap: neutral manifest, health, lifecycle, capability, version, pin, upgrade and rollback across languages.
- Validation: load, invoke, health-check, upgrade, rollback and unload adapters without changing Ptah Core.

## CORE-005 — Node Protocol and capability reporting

**Phase:** 1, 12  
**Status:** VALIDATION REQUIRED

- Internal foundation: TechGuy Relay and device-node work still recovering.
- Primary capability donor: OpenClaw protocol patterns.
- Completion donors: Coder workspace-agent patterns, DevPod provider agents, NATS and OpenTelemetry pending.
- Mature machinery: WebSocket control link plus separate data streams.
- Native Ptah gap: neutral resources and facilities; connection epoch; replay cursor; cancellation; binary streams; multi-language SDKs.
- Licence: OpenClaw MIT permits selective adaptation.
- Integration: native Ptah protocol, not direct OpenClaw dependency.
- Validation: handshake, capability refresh, heartbeat, invocation, cancellation, reconnect, event replay and stream separation.
- Evidence: `donors/OPENCLAW.md`, `donors/CODER.md`, `donors/DEVPOD.md`, ADR-0001 and ADR-0002.

## RELAY-001 — Live event transport

**Phase:** 1  
**Status:** INSPECTING DONORS

- Public control envelope: Ptah Node Protocol informed by OpenClaw.
- Internal event fabric: NATS/JetStream inspection pending.
- Completion: OpenTelemetry correlation and dedicated PTY/object/display streams.
- Native Ptah gap: event sequence, replay, bounded buffering, backpressure and transport abstraction.
- Validation: ordered live events, cursor reconnect, slow consumer handling and intermittent Node recovery.

## RELAY-002 — Durable Activity recovery

**Phase:** 1, 8  
**Status:** INSPECTING DONORS

- Internal foundation: internal job/recovery patterns still recovering.
- Primary donor: Temporal inspection pending.
- Completion donors: JetStream, SQL-backed state and provider snapshots.
- Native Ptah gap: workflow history, checkpoints, retries, timers, cancellation, worker leases and exact recovery semantics.
- Validation: terminate control plane, worker and Node during a long Activity and recover without duplicate side effects.

## EXEC-001 — Terminal and process supervision

**Phase:** 1  
**Status:** COMPOSITE CANDIDATE

- Internal foundation: terminal/process work still recovering.
- Primary implementation: native Ptah process/PTY Facility.
- Donors: OpenClaw detach/replay, Coder workspace agent, E2B SDK ergonomics and OpenHands tools.
- Mature machinery: OS process and PTY APIs.
- Native Ptah gap: multi-terminal ownership; activity links; cancellation; detach/replay; Node portability; resource accounting and durable status.
- Licence: selective MIT/Apache patterns; Coder AGPL study-only.
- Validation: concurrent terminals, detach/reconnect/replay, cancellation and isolated process failure.
- Evidence: `donors/OPENCLAW.md`, `donors/CODER.md`, `donors/E2B.md`, `donors/OPENHANDS.md`, ADR-0001 and WP02A.

## EXEC-002 — OCI/container Workspace Provider

**Phase:** 5  
**Status:** COMPOSITE CANDIDATE

- Internal foundation: Docker/build work still recovering.
- Primary implementation: native Ptah OCI provider.
- Mature upstream machinery: containerd and OCI Runtime/Image/Distribution specifications.
- Completion donors: Daytona lifecycle, Dev Containers/CLI, DevPod, E2B and Coder.
- Exit donors: Docker/Moby, CRI-compatible or other OCI runtimes.
- Native Ptah gap: lifecycle mapping; conformance; ports; storage; Object/Session links; error mapping; restart reconciliation and explicit unsupported capabilities.
- Licence: OCI/containerd Apache-2.0; Daytona/Coder source study-only; DevPod MPL boundary.
- Validation: two isolated providers share content safely; execute independently; restart/reconcile; snapshot where supported; same conformance suite against an alternate backend.
- Evidence: `donors/CONTAINERD-OCI.md`, `donors/DEV-CONTAINERS-SPEC.md`, `donors/DEV-CONTAINERS-CLI.md`, `donors/DEVPOD.md`, `donors/DAYTONA.md`, ADR-0001 and WP02A.

## APP-002 — Linux graphical/native Application runtime

**Phase:** 9  
**Status:** INSPECTING DONORS

- Initial donor: E2B Desktop.
- Completion donors: Guacamole or equivalent remote-display gateway, native Linux desktop and later Theia/browser surfaces.
- Native Ptah gap: Application Session, window and display identities; concurrent streams; reconnect; recording; input; platform-neutral artifacts.
- Known donor limit: E2B Desktop documents only one active stream at a time.
- Validation: two graphical applications plus independent terminals/background jobs; reconnect and evidence capture.
- Evidence: `donors/E2B-DESKTOP.md` and WP02A.

## UI-002 — Activity Centre and multi-backend presentation

**Phase:** 7  
**Status:** INSPECTING DONORS

- Internal foundation: Foreman and Sergeant status/evidence patterns.
- Completion donors: OpenHands Agent Canvas and Coder workspace UX.
- Native Ptah gap: one view over unrelated concurrent Activities, Objects, Nodes, Providers and Artifacts rather than agents/conversations only.
- Validation: ten live Activities remain independently inspectable and controllable.
- Evidence: `donors/OPENHANDS.md`, `donors/CODER.md` and WP02A.

## SESSION-001 — Checkpoint, archive, export, import and resume

**Phase:** 8  
**Status:** INSPECTING DONORS

- Internal foundation: recovery rules and Google Recovery model.
- Lifecycle donors: Daytona, Coder, DevPod, E2B and containerd snapshots.
- Completion donors: Temporal, ReproZip, storage/sync donors and provider snapshots.
- Native Ptah gap: cross-provider Session manifest, Object graph, Activity history, terminal/browser/app references and compatibility rules.
- Validation: Node restart, provider restart and resume on a compatible alternative provider.
- Evidence: workspace donor records and WP02A; durable-activity work pending.

## OBS-001 — Logs, metrics, traces, correlation and resource accounting

**Phase:** 1, 11  
**Status:** INSPECTING DONORS

- Internal foundation: logging/proof patterns exist.
- Primary machinery: OpenTelemetry inspection pending.
- Completion donors: containerd metrics, Coder/Daytona/OpenClaw patterns and internal evidence systems.
- Native Ptah gap: correlation across control plane, Node, Provider, Activity, Object and Artifact; cost and resource accounting.
- Validation: trace one operation end-to-end and diagnose failure/resource pressure from retained evidence.

---

# Other v1 requirement rows

These remain open or in internal recovery. Detailed composite records will replace each line as its donor group is inspected.

| ID | Requirement | Phase | Status | Current direction |
|---|---|---:|---|---|
| CORE-003 | Object graph and catalogue | 1–3 | RECOVERING INTERNAL WORK | App Recover, APK Extractor, Creative Studio, Tika/libarchive/LIEF and native content-addressed graph |
| STORE-001 | Hot local Workspace storage | 1–2 | INSPECTING DONORS | Linux filesystems/volumes plus Coder/Daytona/containerd patterns |
| STORE-002 | Durable Object storage | 2 | OPEN | S3/R2, ORAS and native catalogue |
| STORE-003 | Metadata catalogue | 1–2 | OPEN | SQLite locally; SQL shared; versioned migrations |
| STORE-004 | Hashing and deduplication | 1–2 | OPEN | streaming cryptographic hashes and CAS |
| STORE-005 | Drive export/recovery | 2, 8 | OPEN | Drive API/rclone with Session export manifests |
| XFER-001 | Resumable uploads | 2 | OPEN | tus/tusd plus Object registration |
| XFER-002 | Fast resumable downloads | 2 | RECOVERING INTERNAL WORK | internal DM plus aria2 and native queue |
| XFER-003 | Cloud/Node synchronization | 2, 12 | OPEN | rclone/Syncthing plus Object-aware conflict model |
| GIT-001 | Mirrors/worktrees/refs | 5 | OPEN | Git plus internal ecosystem and workspace donors |
| EXEC-003 | Reproducible build graph | 5 | OPEN | BuildKit, Dagger and internal Software Builder |
| EXEC-004 | Stronger isolation | 5, 12 | OPEN | gVisor, Kata, Firecracker and alternate OCI runtimes |
| BROWSE-001 | Persistent interactive browser | 6 | OPEN | Playwright/Chromium, Browser-Use and TurboWebFetch |
| BROWSE-002 | Rendered extraction/research | 6 | OPEN | TurboWebFetch plus Playwright and source provenance |
| BROWSE-003 | Browser evidence | 6 | OPEN | screenshots, recordings, traces, console and network artifacts |
| DECOMP-001 | True-type detection | 3 | OPEN | Tika, magic/signatures and native confidence routing |
| DECOMP-002 | Recursive archive decomposition | 3 | OPEN | libarchive and native extraction budgets/Object graph |
| DOC-001 | Document structure/render/proof | 3, 10 | OPEN | internal generator, Tika/Unstructured and renderers |
| MEDIA-001 | Video/audio | 3 | OPEN | internal Creative Studio and FFmpeg |
| IMAGE-001 | Image processing | 3 | OPEN | internal Creative Studio and libvips |
| BIN-001 | Executable decomposition | 3 | OPEN | internal App Recover and LIEF |
| APP-001 | APK/AAB/DEX decomposition | 3, 9 | OPEN | internal APK Extractor, JADX and Apktool |
| FW-001 | Apple firmware | 4 | OPEN | internal Apple work and blacktop/ipsw |
| FW-002 | MediaTek firmware | 4 | RECOVERING INTERNAL WORK | internal MTK/META plus MTKClient |
| FW-003 | Unisoc firmware | 4 | RECOVERING INTERNAL WORK | internal SPD/Unisoc plus PAC/FDL donors |
| FW-004 | Qualcomm firmware | 4 | RECOVERING INTERNAL WORK | internal Qualcomm plus EDL/Firehose/XML/LIEF |
| FW-005 | Android OTA/dynamic partitions | 4 | RECOVERING INTERNAL WORK | internal OTA plus payload/platform tools |
| FW-006 | Other vendor/embedded firmware | 4 | OPEN | Binwalk and vendor-specific Domain Packs |
| FS-001 | Disks, partitions, images, filesystems | 4 | OPEN | libguestfs and platform tools |
| DEVICE-001 | Android inventory/ADB | 9 | RECOVERING INTERNAL WORK | internal Device Manager/MIBU/ADB plus STF/adbkit/Appium |
| DEVICE-002 | Android screen/input/semantic UI | 9 | OPEN | TouchPilot/STF/Appium/scrcpy/UIAutomator |
| APP-003 | Windows EXE/MSI runtime | 9 | OPEN | native/VM Windows Node and remote display |
| APP-004 | Apple IPA/macOS runtime | 9 | OPEN | macOS/Xcode Node, Appium and Peekaboo patterns |
| UI-001 | Human Workspace shell | 7 | OPEN | Theia with optional OpenVSCode and native Ptah panels |
| SYNC-001 | Online/local synchronization/conflicts | 8, 12 | OPEN | object hashes, revisions, Syncthing/rclone patterns |
| SEARCH-001 | Unified search/indexing | 10 | OPEN | RAGFlow/LlamaIndex and multi-domain index |
| DATA-001 | Structured data/database pack | 10 | OPEN | Polars, SQL engines and native data Objects/Activities |
| PLUGIN-001 | Plugin lifecycle | 10 | OPEN | OpenClaw/ClawHub, MCP and OCI registries |
| PROV-001 | Provenance/signing/proof bundles | 11 | OPEN | Sergeant/MIBU plus Witness/in-toto/Cosign/ORAS |
| SEC-001 | Security workload hosting/evidence | 11 | OPEN | Strix, Semgrep, ZAP, Trivy, Syft and Grype |
| DIST-001 | Multi-Node placement/transfer | 12 | INSPECTING DONORS | Ptah Node Protocol, NATS, scheduler and Object transfer |
| OFFLINE-001 | Local-first/intermittent connectivity | 12 | INSPECTING DONORS | Node reconnect, local catalogue/queue and sync conflict model |

---

# WP02A conclusion

- The workspace/execution subsystem now has a recorded composite donor set rather than a single selected product.
- OCI/containerd is the mature execution foundation candidate; Ptah owns the provider contract.
- Dev Containers is a compatibility standard, not the universal Ptah schema.
- Coder, E2B, DevPod and OpenHands supply different completion capabilities and remain optional adapters/callers.
- Activity durability, live internal events and observability remain open to Temporal, NATS and OpenTelemetry inspection.

---

# Completion rule

Phase 0A cannot close until every v1 requirement is either:

- `CLOSED FOR DESIGN`, with evidence, composite donor set, native boundary and exit strategy;
- explicitly `PARKED` outside v1;
- or `REJECTED PATH`, with reason and replacement.
