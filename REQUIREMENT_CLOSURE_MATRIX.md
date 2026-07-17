# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — WP02A AND WP02B SAVED

This file maps accepted Ptah requirements to internal evidence, composite donor sets, mature machinery, native Ptah gaps, licences, exits and proof.

A requirement is not closed by naming one repository. Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

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

# Core-runtime cluster

## CORE-001 — Persistent Workspace model

**Status:** COMPOSITE CANDIDATE

- Internal foundation: project/workspace patterns still recovering.
- Native owner: Ptah Workspace Provider contract.
- Donor set: Daytona lifecycle; Coder long-lived human workspaces; E2B automation API; Dev Containers/CLI portability; DevPod provider model.
- Machinery: local Linux processes, containerd and OCI.
- Native gap: provider-neutral lifecycle, capabilities, conformance and Workspace/Object/Activity/Session separation.
- Licence: Daytona/Coder AGPL study-only; E2B/OCI/containerd Apache-2.0; CLI MIT; DevPod MPL-2.0.
- Exit: no external control plane mandatory.
- Proof: local and OCI providers plus one optional external provider pass the same suite; two concurrent Workspaces; provider replacement preserves Ptah identity.
- Evidence: workspace donor records, WP02A and ADR-0001.

## CORE-002 — Concurrent Activity runtime

**Status:** COMPOSITE CANDIDATE — INTERNAL RECOVERY REQUIRED

- Internal foundation: AgentOps, Foreman, Sergeant and worker implementations still recovering.
- Native owner: Ptah Activity contract and Activity Ledger.
- Primary durable backend candidate: Temporal.
- Completion donors: NATS/JetStream for live/replayable events; OpenTelemetry for correlation; OpenHands/internal workers for tool execution.
- Machinery: durable SQL, OS processes and async runtimes.
- Native gap: portable Activity identity/state; dependencies; leases; retry classes; cancellation; checkpoints; receipts; backend references and migration.
- Licence: Temporal MIT; Rust SDK Apache-2.0; NATS and OTel Apache-2.0.
- Exit: SQL-backed or alternate durable coordinator behind the same contract.
- Proof: ten independent Activities; worker/control-plane/Node failure; no duplicate side effects; event and trace correlation.
- Evidence: `donors/TEMPORAL.md`, `donors/NATS-JETSTREAM.md`, `donors/OPENTELEMETRY.md`, WP02B and ADR-0003.

## CORE-003 — Object graph and catalogue

**Status:** RECOVERING INTERNAL WORK

- Internal: App Recover, APK Extractor, Creative Studio and source mirrors.
- Donors/machinery pending: Tika, libarchive, LIEF, Domain Packs, hashes and local/Object storage.
- Native gap: universal Object identity, relationships, provenance, storage locations and derivatives.
- Proof: mixed recursive decomposition with immutable original.

## CORE-004 — Facility and plugin host

**Status:** INSPECTING DONORS / INTERNAL WORK

- Internal engine boundaries still recovering.
- Donors: OpenClaw plug-ins, OpenHands tools/SDK, MCP and later ClawHub.
- Native gap: neutral manifest, capability, health, lifecycle, version, pin, upgrade and rollback across languages.
- Proof: load, invoke, health-check, upgrade, rollback and unload without changing Ptah Core.

## CORE-005 — Node Protocol and capability reporting

**Status:** VALIDATION REQUIRED — INTERNAL RECOVERY REQUIRED

- Internal: TechGuy Relay and device-node work still recovering.
- Primary donor: OpenClaw protocol patterns.
- Completion: Coder/DevPod agents, NATS event transport and OpenTelemetry correlation.
- Native gap: neutral resources/facilities, connection epoch, replay cursor, cancellation, large-stream references and multi-language SDKs.
- Licence: OpenClaw MIT; completion machinery Apache-2.0/MPL boundaries recorded.
- Proof: handshake, capabilities, heartbeat, invoke/cancel, reconnect/replay and stream separation.
- Evidence: relevant donor records, ADR-0001 and ADR-0003.

## RELAY-001 — Live event transport

**Status:** COMPOSITE CANDIDATE — INTERNAL RECOVERY REQUIRED

- Public control: Ptah Node Protocol informed by OpenClaw.
- Internal live fabric: NATS Core candidate.
- Replayable operational events: JetStream candidate.
- Telemetry bridge: OpenTelemetry.
- Large data: separate PTY/Object/display/media transports.
- Native gap: versioned event envelope, sequence, cursor, retention class, duplicate handling, backpressure and local outbox.
- Exit: alternate broker or direct transport behind Ptah Event Fabric.
- Proof: ordered events, cursor reconnect, slow consumer, intermittent Node and cross-language clients.
- Evidence: `donors/NATS-JETSTREAM.md`, WP02B and ADR-0003.

## RELAY-002 — Durable Activity recovery

**Status:** COMPOSITE CANDIDATE — INTERNAL RECOVERY REQUIRED

- Native owner: Ptah Activity Ledger and receipts.
- Primary backend: Temporal candidate.
- Completion: JetStream delivery, provider snapshots and SQL state.
- Native gap: retry classification, idempotency, compensation, cancellation, manual resume, checkpoint references and portable state.
- Exit: alternate coordinator behind the same contract.
- Proof: terminate workers, control plane and Node during long work; recover without duplicate side effects.
- Evidence: `donors/TEMPORAL.md`, WP02B and ADR-0003.

## STORE-001 — Hot local Workspace storage

**Status:** INSPECTING DONORS

- Direction: Linux filesystem/volumes with containerd snapshots and workspace donor patterns.
- Native gap: storage classes, mounts, pressure/health, cache truth rules and Object references.

## STORE-002 — Durable Object storage

**Status:** OPEN

- Direction: S3/R2, later ORAS relationships and Ptah catalogue.

## STORE-003 — Metadata catalogue

**Status:** OPEN

- Direction: SQLite local, shared SQL, versioned migrations and sync.

## STORE-004 — Hashing/deduplication

**Status:** OPEN

- Direction: streaming cryptographic hashes, chunk identity and integrity repair.

## STORE-005 — Drive export/recovery

**Status:** OPEN

- Direction: Drive/rclone adapter plus Session export manifests.

## XFER-001 — Resumable uploads

**Status:** OPEN

- Direction: tus/tusd plus Object registration.

## XFER-002 — Fast resumable downloads

**Status:** RECOVERING INTERNAL WORK

- Direction: internal Download Manager plus aria2 and native queue/object landing.

## XFER-003 — Cloud and Node synchronization

**Status:** OPEN

- Direction: rclone/Syncthing plus Object-aware revisions and conflicts.

## GIT-001 — Mirrors, worktrees and refs

**Status:** OPEN

- Direction: Git plus internal ecosystem and workspace donor patterns.

## EXEC-001 — Terminal and process supervision

**Status:** COMPOSITE CANDIDATE — INTERNAL RECOVERY REQUIRED

- Native implementation: Ptah process/PTY Facility.
- Donors: OpenClaw detach/replay; Coder agent; E2B SDK; OpenHands tools.
- Completion: NATS events, Temporal durable orchestration where applicable and OpenTelemetry.
- Native gap: ownership, detach/replay, cancellation, Node portability, resource accounting and durable receipts.
- Proof: concurrent terminals, reconnect/replay, isolated failure and worker restart.

## EXEC-002 — OCI/container Workspace Provider

**Status:** COMPOSITE CANDIDATE — INTERNAL RECOVERY REQUIRED

- Native implementation: Ptah OCI Provider.
- Machinery: containerd and OCI Runtime/Image/Distribution.
- Completion: Daytona lifecycle, Dev Containers/CLI, DevPod, E2B and Coder.
- Exit: Docker/Moby, CRI or alternate OCI runtime.
- Native gap: lifecycle mapping, ports, storage, reconciliation, errors, capabilities and Object/Session links.
- Proof: isolated concurrent providers, shared content, restart/reconcile, explicit checkpoint limits and alternate backend.

## EXEC-003 — Reproducible build graph

**Status:** OPEN

- Direction: internal Software Builder, BuildKit and Dagger.

## EXEC-004 — Stronger isolation

**Status:** OPEN

- Direction: gVisor, Kata, Firecracker and alternate OCI runtimes.

## BROWSE-001 — Persistent interactive browser

**Status:** OPEN

- Direction: Playwright/Chromium, Browser-Use and TurboWebFetch.

## BROWSE-002 — Rendered extraction/research

**Status:** OPEN

- Direction: TurboWebFetch plus Playwright and source provenance.

## BROWSE-003 — Browser evidence

**Status:** OPEN

- Direction: screenshots, recordings, traces, console and network Artifacts.

## DECOMP-001 — True-type detection

**Status:** OPEN

- Direction: Tika, magic/signatures and native confidence routing.

## DECOMP-002 — Recursive archive decomposition

**Status:** OPEN

- Direction: libarchive plus extraction budgets and Object graph.

## DOC-001 — Document structure/render/proof

**Status:** OPEN

- Direction: internal generator, Tika/Unstructured and renderers.

## MEDIA-001 — Video/audio

**Status:** OPEN

- Direction: Creative Studio and FFmpeg.

## IMAGE-001 — Image processing

**Status:** OPEN

- Direction: Creative Studio and libvips.

## BIN-001 — Executable decomposition

**Status:** OPEN

- Direction: App Recover and LIEF.

## APP-001 — APK/AAB/DEX decomposition

**Status:** OPEN

- Direction: APK Extractor, JADX and Apktool.

## FW-001 — Apple firmware

**Status:** OPEN

- Direction: internal Apple work and blacktop/ipsw.

## FW-002 — MediaTek firmware

**Status:** RECOVERING INTERNAL WORK

- Direction: internal MTK/META plus MTKClient.

## FW-003 — Unisoc firmware

**Status:** RECOVERING INTERNAL WORK

- Direction: internal SPD/Unisoc plus PAC/FDL donors.

## FW-004 — Qualcomm firmware

**Status:** RECOVERING INTERNAL WORK

- Direction: internal Qualcomm plus EDL/Firehose/XML/LIEF.

## FW-005 — Android OTA/dynamic partitions

**Status:** RECOVERING INTERNAL WORK

- Direction: internal OTA work plus payload/platform tools.

## FW-006 — Other vendor/embedded firmware

**Status:** OPEN

- Direction: Binwalk and vendor Domain Packs.

## FS-001 — Disks, partitions, images and filesystems

**Status:** OPEN

- Direction: libguestfs and platform tools.

## DEVICE-001 — Android inventory and ADB

**Status:** RECOVERING INTERNAL WORK

- Direction: Device Manager/MIBU/ADB plus STF/adbkit/Appium.

## DEVICE-002 — Android screen/input/semantic UI

**Status:** OPEN

- Direction: TouchPilot/STF/Appium/scrcpy/UIAutomator.

## APP-002 — Linux graphical/native Application runtime

**Status:** INSPECTING DONORS

- Initial donor: E2B Desktop.
- Completion: remote-display gateway, native Linux desktop and browser surfaces.
- Native gap: Application Session, windows, concurrent displays, reconnect, recording and Artifacts.

## APP-003 — Windows EXE/MSI runtime

**Status:** OPEN

- Direction: Windows Node/VM and remote display.

## APP-004 — Apple IPA/macOS runtime

**Status:** OPEN

- Direction: macOS/Xcode Node, Appium and Peekaboo.

## UI-001 — Human Workspace shell

**Status:** OPEN

- Direction: Theia, optional OpenVSCode and native Ptah panels.

## UI-002 — Activity Centre

**Status:** INSPECTING DONORS

- Internal: Foreman/Sergeant patterns.
- External: OpenHands Agent Canvas and Coder.
- Native gap: unrelated concurrent Activities/Objects/Nodes/Providers rather than agent conversations.

## SESSION-001 — Checkpoint/archive/export/import/resume

**Status:** COMPOSITE CANDIDATE — INTERNAL RECOVERY REQUIRED

- Lifecycle donors: Daytona, Coder, DevPod, E2B and containerd.
- Durable orchestration: Temporal.
- Live/replay correlation: NATS/JetStream.
- Native owner: Ptah Session manifest referencing provider snapshots, Objects, Activities, terminals, browsers, apps and Artifacts.
- Completion still open: storage, sync/conflicts and internal recovery rules.

## SYNC-001 — Online/local synchronization/conflicts

**Status:** OPEN

- Direction: Object hashes/revisions, Syncthing/rclone and Ptah authority/conflict model.

## SEARCH-001 — Unified search/indexing

**Status:** OPEN

- Direction: RAGFlow/LlamaIndex and multi-domain Object index.

## DATA-001 — Structured data/database pack

**Status:** OPEN

- Direction: Polars, SQL engines and native data Objects/Activities.

## PLUGIN-001 — Plugin lifecycle

**Status:** OPEN

- Direction: OpenClaw/ClawHub, MCP and OCI registries.

## OBS-001 — Logs, metrics, traces and resource accounting

**Status:** COMPOSITE CANDIDATE — INTERNAL RECOVERY REQUIRED

- Primary machinery: OpenTelemetry specification, OTLP and Collector.
- Completion: Collector Contrib, Node/Provider/Facility telemetry and internal proof systems.
- Native owner: Ptah semantic conventions, resource accounting, redaction, local buffering and proof-critical receipt classes.
- Exit: replace Collectors/exporters without changing instrumentation or durable records.
- Proof: end-to-end request→Node→Provider→Facility→Artifact trace; Collector outage recovery; redaction and bounded overhead.
- Evidence: `donors/OPENTELEMETRY.md`, WP02B and ADR-0003.

## PROV-001 — Provenance/signing/proof bundles

**Status:** OPEN

- Direction: Sergeant/MIBU plus Witness/in-toto/Cosign/ORAS.

## SEC-001 — Security workload hosting/evidence

**Status:** OPEN

- Direction: Strix, Semgrep, ZAP, Trivy, Syft and Grype.

## DIST-001 — Multi-Node placement/transfer

**Status:** INSPECTING DONORS

- Foundations: Ptah Node Protocol, NATS event fabric and OpenTelemetry resource reporting.
- Still open: scheduler, leases, object transport and placement quality.

## OFFLINE-001 — Local-first/intermittent operation

**Status:** COMPOSITE BOUNDARY ACCEPTED — IMPLEMENTATION OPEN

- Native owner: Node local journal/outbox, connection epoch and conflict reconciliation.
- Completion: NATS/JetStream transport, durable Activity Ledger and future sync donors.
- Proof: disconnect, continue permitted local work, reject duplicates and reconcile Objects/Activities on reconnect.
- Evidence: ADR-0003 and WP02B.

---

# Current core-runtime conclusion

The external donor composition for Workspaces, execution, Activities, events and observability is complete enough to begin internal comparison.

It is **not closed for design** until internal THETECHGUY process, relay, worker, evidence and sync behavior is recovered and compared.

Next active unit: `WP02C — Internal core-runtime recovery` as recorded in `CURRENT_STATE.md`.

---

# Completion rule

Phase 0A cannot close until every v1 requirement is `CLOSED FOR DESIGN`, explicitly `PARKED`, or a `REJECTED PATH` with a replacement.
