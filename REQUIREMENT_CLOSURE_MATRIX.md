# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** POPULATING — CORE RUNTIME CLOSED FOR PHASE 0B DESIGN

This file maps Ptah requirements to internal evidence, composite donor sets, mature machinery, native gaps, licences, exits and proof.

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

# Core-runtime cluster

## CORE-001 — Persistent Workspace model

**Status:** CLOSED FOR DESIGN

- Native owner: Ptah Workspace Provider contract.
- Donor composition: Daytona lifecycle; Coder long-lived human Workspaces; E2B automation API; Dev Containers/CLI portability; DevPod provider model.
- Machinery: local Linux processes, containerd and OCI.
- Internal evidence: safe local file roots, explicit source/local authority and specialist bridge separation from Hunter/CodeOps.
- Licence: Daytona/Coder AGPL study-only; E2B/OCI/containerd Apache-2.0; Dev Container CLI MIT; DevPod MPL-2.0.
- Exit: no external control plane is mandatory.
- Phase 0B work: lifecycle/capability schema, provider conformance and Workspace/Object/Activity/Session separation.
- Proof later: local and OCI providers plus one optional external provider pass the same suite; concurrent Workspaces; provider replacement preserves identity.
- Evidence: workspace donor records, internal Hunter records, WP02A/WP02C and ADR-0001.

## CORE-002 — Concurrent Activity runtime

**Status:** CLOSED FOR DESIGN

- Native owner: Ptah Activity contract and Activity Ledger.
- Durable backend candidate: Temporal.
- Completion: NATS/JetStream, OpenTelemetry, OpenHands and internal workers.
- Internal evidence: AgentOps operation packets; Foreman work status; Hunter in-memory Tasks, persistent JSON Workflows and D1 outbox; MIBU correlation; CodeOps result/evidence/review separation.
- Machinery: durable SQL, OS processes and async runtimes.
- Licence: Temporal MIT; Rust SDK/NATS/OTel Apache-2.0.
- Exit: SQL-backed or alternate durable coordinator behind the same contract.
- Phase 0B work: Activity states, dependencies, leases/fencing, retry classes, cancellation, checkpoints, backend references, receipts and migration.
- Proof later: ten independent Activities; worker/control-plane/Node failure; no duplicate side effects; exact event/trace/receipt correlation.
- Evidence: Temporal/NATS/OTel records, internal runtime records, WP02B/WP02C, ADR-0003 and ADR-0004.

## CORE-003 — Object graph and catalogue

**Status:** RECOVERING INTERNAL WORK

- Internal direction: App Recover, APK Extractor, Creative Studio, document/source mirrors and Hunter Object/file patterns.
- Donors/machinery pending: Tika, libarchive, LIEF, Domain Packs, hashes and layered storage.
- Native gap: universal Object identity, relationships, provenance, storage locations, versions and derivatives.
- Proof later: mixed recursive decomposition with immutable originals and shared source reuse.

## CORE-004 — Facility and plugin host

**Status:** CLOSED FOR DESIGN

- Native owner: Ptah Facility Manifest, host and invocation/result contract.
- Donors: OpenClaw plugins, OpenHands tools/SDK, MCP and later ClawHub.
- Internal evidence: Sergeant WeaponManifest; CodeOps capability routes; AgentOps specialist packets; Hunter bridges; Software Builder target/tool registry ideas.
- Phase 0B work: neutral IDs, version/status/maturity, platforms, schemas, required permissions/resources, side effects, runtime, failure behavior, evidence output, health, pin/upgrade/rollback and credential references.
- Exit: process, service, container, MCP or other adapters behind one contract.
- Proof later: load, invoke, health-check, upgrade, rollback and unload polyglot Facilities without changing Ptah Core.
- Evidence: OpenClaw/OpenHands records, `internal/SERGEANT.md`, `internal/HUNTER-CODEOPS.md`, `internal/HUNTER-AGENTOPS.md` and WP02C.

## CORE-005 — Node Protocol and capability reporting

**Status:** CLOSED FOR DESIGN

- Native owner: Ptah Node Protocol.
- Primary donor: OpenClaw protocol patterns.
- Completion: Coder/DevPod agents, NATS transport and OpenTelemetry correlation.
- Internal evidence: TechGuy Relay pairing/heartbeat/TTL experiment, MIBU device state/correlation and Hunter local/runtime bridges.
- Licence: OpenClaw MIT; completion machinery Apache-2.0/MPL boundaries recorded.
- Phase 0B work: stable cryptographic Node identity, connection epoch, resources/Facilities, replay cursor, cancellation, credential/pairing flow, large-stream references and SDKs.
- Exit: public protocol remains independent of OpenClaw/NATS.
- Proof later: handshake, capabilities, heartbeat, invoke/cancel, stale-epoch rejection, reconnect/replay and stream separation.
- Evidence: donor/internal records, ADR-0001, ADR-0003 and ADR-0004.

## RELAY-001 — Live Event transport

**Status:** CLOSED FOR DESIGN

- Public control: Ptah Node Protocol.
- Internal live fabric: NATS Core candidate.
- Replayable operational events: JetStream candidate.
- Telemetry bridge: OpenTelemetry.
- Internal evidence: Foreman versioned bridge envelope; MIBU nonce/stale rejection; Hunter D1 outbox/attempts; TechGuy Relay heartbeat lessons.
- Large data: separate PTY/Object/display/media transports.
- Phase 0B work: event envelope, source/correlation IDs, sequence/cursor, epoch, retention class, duplicate handling, backpressure and local outbox.
- Exit: alternate broker/direct transport behind Ptah Event Fabric.
- Proof later: ordered events, cursor reconnect, slow consumer, intermittent Node, stale receipt rejection and cross-language clients.
- Evidence: NATS/OTel and internal records, ADR-0003/0004 and WP02C.

## RELAY-002 — Durable Activity recovery

**Status:** CLOSED FOR DESIGN

- Native owner: Ptah Activity Ledger, checkpoints and receipts.
- Primary backend: Temporal candidate.
- Completion: JetStream delivery, provider snapshots, SQL state and local Node journal.
- Internal evidence: Hunter persistent Workflow Manager; D1 transactional outbox, attempts, retry/dead and stale-lock recovery; AgentOps/CodeOps/MIBU proof boundaries.
- Phase 0B work: retry classes, idempotency, compensation, cancellation, manual resume, leases/fencing, checkpoint references and backend portability.
- Exit: alternate coordinator behind same contract.
- Proof later: terminate worker/control plane/Node during long work and recover without duplicated side effects.
- Evidence: Temporal record, internal Hunter/MIBU records, ADR-0003/0004 and WP02C.

## EXEC-001 — Terminal and process supervision

**Status:** CLOSED FOR DESIGN

- Native owner: Ptah Process/PTY Facility.
- Donors: OpenClaw detach/replay; Coder agent; E2B SDK; OpenHands tools.
- Completion: NATS events, Temporal orchestration where relevant and OpenTelemetry.
- Internal evidence: Hunter task/workflow/process bridges, CodeOps/AgentOps subprocess adapters, Software Builder background-worker requirements and MIBU ADB/fastboot execution.
- Phase 0B work: multi-terminal ownership, stream references, process identity, cancellation, detach/replay, resource accounting, receipts and restart reconciliation.
- Proof later: concurrent terminals/processes, reconnect/replay, cancellation, isolated failure and worker restart.

## EXEC-002 — OCI/container Workspace Provider

**Status:** CLOSED FOR DESIGN

- Native owner: Ptah OCI Workspace Provider.
- Machinery: containerd and OCI Runtime/Image/Distribution.
- Completion: Daytona lifecycle, Dev Containers/CLI, DevPod, E2B and Coder.
- Internal evidence: shared Builder caches/environment rules and Hunter Docker/runtime needs.
- Exit: Docker/Moby, CRI or alternate OCI runtime.
- Phase 0B work: lifecycle mapping, ports/services, storage, restart reconciliation, explicit capability limits and Object/Session links.
- Proof later: isolated concurrent providers, shared content, restart/reconcile, explicit checkpoint limits and alternate backend.

## SESSION-001 — Checkpoint/archive/export/import/resume

**Status:** CLOSED FOR DESIGN — STORAGE/SYNC DEPENDENCIES REMAIN OPEN

- Native owner: Ptah Session manifest.
- Donors: Daytona, Coder, DevPod, E2B, containerd and Temporal.
- Internal evidence: Hunter Workflow checkpoints/retry-of/resume-of, source/local authority, CodeOps backups and MIBU late authoritative status.
- Phase 0B work: references to provider snapshots, Objects, Activities, terminals, browsers, apps, Artifacts, receipts and compatibility class.
- Remaining requirement dependencies: durable Object storage, versions, online/local synchronization and conflicts.
- Proof later: restart and resume on same provider plus compatible alternative provider without losing identity/provenance.

## OBS-001 — Logs, metrics, traces and resource accounting

**Status:** CLOSED FOR DESIGN

- Machinery: OpenTelemetry specification, OTLP and Collector.
- Completion: Collector Contrib and Facility-native telemetry.
- Internal evidence: Foreman health/status; Sergeant proof; AgentOps/CodeOps audit records; MIBU proof protocol; Hunter task/workflow/outbox attempts.
- Native owner: Ptah semantic conventions, resource accounting, redaction, local buffering and proof-critical receipt classification.
- Exit: replace Collector/exporters without changing instrumentation or durable receipts.
- Proof later: request→Node→Provider→Facility→Artifact trace; Collector outage recovery; redaction and bounded overhead.
- Evidence: OpenTelemetry/internal records, ADR-0003/0004 and WP02C.

## OFFLINE-001 — Local-first/intermittent operation

**Status:** CLOSED FOR DESIGN — TRANSFER/SYNC IMPLEMENTATION REMAINS OPEN

- Native owner: Node local journal/outbox, connection epoch and reconciliation.
- Completion: NATS/JetStream transport, Activity Ledger and future sync donors.
- Internal evidence: Hunter fast-forward-only source sync, D1 outbox and MIBU late status/correlation.
- Phase 0B work: local authority, pending acknowledgements, duplicate rejection, revision/conflict records and Object/Artifact references.
- Proof later: disconnect, continue permitted local work, reconcile exact state and surface conflicts without overwrite.

## DIST-001 — Multi-Node placement and transfer

**Status:** COMPOSITE CANDIDATE — SCHEDULER/NETWORK/OBJECT TRANSPORT OPEN

- Foundations closed: Node Protocol, Event Fabric, OTel resource reporting and provider capabilities.
- Internal evidence: capability-based CodeOps routing and exact device state.
- Still open: scheduler/placement quality, secure Node identity/networking, leases and Object transport.

---

# Build, storage and transfer cluster

## STORE-001 — Hot local Workspace storage

**Status:** INSPECTING DONORS

- Direction: Linux filesystems/volumes, containerd snapshots and Workspace donor patterns.
- Internal evidence: Software Builder clean-Project/shared-cache rules and Hunter local-file boundaries.
- Native gap: storage classes, mounts, pressure/health, cache truth and Object links.

## STORE-002 — Durable Object storage

**Status:** OPEN

- Direction: S3/R2, ORAS relationships and Ptah catalogue.
- Internal evidence: Hunter D1-authoritative metadata and temporary R2 lifecycle.

## STORE-003 — Metadata catalogue

**Status:** COMPOSITE CANDIDATE

- Direction: SQLite local, shared SQL and versioned migrations.
- Internal evidence: D1 schema/idempotency/outbox and local JSON limitations.
- Native gap: transactional Object/Activity graph, local journal and synchronization.

## STORE-004 — Hashing and deduplication

**Status:** OPEN

- Direction: streaming cryptographic hashes, chunk identity and integrity repair.
- Internal evidence: proof/release checksum manifests.

## STORE-005 — Drive export/recovery

**Status:** OPEN

- Direction: Drive/rclone adapter and Session export manifests.

## XFER-001 — Resumable uploads

**Status:** OPEN

- Direction: tus/tusd plus Object registration.

## XFER-002 — Fast resumable downloads

**Status:** RECOVERING INTERNAL WORK

- Direction: internal Download Manager plus aria2 and native queue/Object landing.

## XFER-003 — Cloud and Node synchronization

**Status:** OPEN

- Direction: rclone/Syncthing plus Object-aware revisions/conflicts.
- Internal evidence: safe source sync and local/online authority separation.

## GIT-001 — Mirrors, worktrees and refs

**Status:** OPEN

- Direction: Git plus internal ecosystem and Workspace donor patterns.

## EXEC-003 — Reproducible build graph

**Status:** INSPECTING DONORS — WP03 ACTIVE

- Internal evidence: Software Builder shared machinery, scanner/planner, target readiness and background-worker requirements; actual central build execution incomplete.
- Donors/machinery: BuildKit and Dagger pending.
- Native gap: typed Build Recipe, Activity/Artifact bridge, cache identity, tool/environment identity and reproducibility proof.

## EXEC-004 — Stronger isolation

**Status:** OPEN

- Direction: gVisor, Kata, Firecracker and alternate OCI runtimes.

## PROV-001 — Provenance/signing/proof bundles

**Status:** INSPECTING DONORS — WP03 ACTIVE

- Internal evidence: Sergeant, MIBU, AgentOps, CodeOps and Hunter outbox/attempt records.
- Donors/machinery: Witness, in-toto, Cosign/Sigstore and ORAS pending.
- Native gap: universal materials/products/command/environment/receipt relationships and independently verifiable bundles.

---

# Browser, decomposition, firmware, application and UI requirements

| ID | Requirement | Status | Current direction |
|---|---|---|---|
| BROWSE-001 | Persistent interactive browser | OPEN | Playwright/Chromium, Browser-Use and TurboWebFetch |
| BROWSE-002 | Rendered extraction/research | OPEN | TurboWebFetch + Playwright + source provenance |
| BROWSE-003 | Browser evidence | OPEN | screenshots, recordings, traces, console/network Artifacts |
| DECOMP-001 | True-type detection | OPEN | Tika, magic/signatures and native confidence routing |
| DECOMP-002 | Recursive archive decomposition | OPEN | libarchive + budgets + Object graph |
| DOC-001 | Document structure/render/proof | OPEN | internal generator, Tika/Unstructured and renderers |
| MEDIA-001 | Video/audio | OPEN | Creative Studio + FFmpeg |
| IMAGE-001 | Image processing | OPEN | Creative Studio + libvips |
| BIN-001 | Executable decomposition | OPEN | App Recover + LIEF |
| APP-001 | APK/AAB/DEX decomposition | OPEN | APK Extractor + JADX/Apktool |
| FW-001 | Apple firmware | OPEN | internal Apple work + blacktop/ipsw |
| FW-002 | MediaTek firmware | RECOVERING INTERNAL WORK | internal MTK/META + MTKClient |
| FW-003 | Unisoc firmware | RECOVERING INTERNAL WORK | internal SPD/Unisoc + PAC/FDL donors |
| FW-004 | Qualcomm firmware | RECOVERING INTERNAL WORK | internal Qualcomm + EDL/Firehose/XML/LIEF |
| FW-005 | Android OTA/dynamic partitions | RECOVERING INTERNAL WORK | internal OTA + payload/platform tools |
| FW-006 | Other vendor/embedded firmware | OPEN | Binwalk and vendor Domain Packs |
| FS-001 | Disks, partitions, images/filesystems | OPEN | libguestfs and platform tools |
| DEVICE-001 | Android inventory/ADB | COMPOSITE CANDIDATE | Device Manager/MIBU/ADB + STF/adbkit/Appium; exact donor pass pending |
| DEVICE-002 | Android screen/input/semantic UI | OPEN | TouchPilot/STF/Appium/scrcpy/UIAutomator |
| APP-002 | Linux graphical/native application | INSPECTING DONORS | E2B Desktop + remote display/native Linux |
| APP-003 | Windows EXE/MSI runtime | OPEN | Windows Node/VM + remote display |
| APP-004 | Apple IPA/macOS runtime | OPEN | macOS/Xcode Node + Appium/Peekaboo |
| UI-001 | Human Workspace shell | OPEN | Theia + optional OpenVSCode + native panels |
| UI-002 | Activity Centre | COMPOSITE CANDIDATE | Foreman/Sergeant + OpenHands/Coder; native concurrent view |
| SYNC-001 | Online/local sync/conflicts | OPEN | Object revisions + Syncthing/rclone + authority model |
| SEARCH-001 | Unified search/indexing | OPEN | RAGFlow/LlamaIndex + multi-domain Object index |
| DATA-001 | Structured data/database pack | OPEN | Polars/SQL + native data Objects/Activities |
| PLUGIN-001 | Plugin lifecycle | OPEN | OpenClaw/ClawHub, MCP and OCI registries |
| SEC-001 | Security workload/evidence | OPEN | Strix, Semgrep, ZAP, Trivy, Syft and Grype |

---

# Current conclusion

The complete core-runtime cluster is closed for **Phase 0B contract design**, not implementation.

Active Phase 0A group: deterministic Build, Artifact and provenance composition (`WP03`) as recorded in `CURRENT_STATE.md`.

Phase 0A cannot close until every v1 requirement is `CLOSED FOR DESIGN`, explicitly `PARKED`, or a `REJECTED PATH` with a replacement.
