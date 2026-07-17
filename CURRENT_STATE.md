# Ptah Current State

**Last updated:** 2026-07-17  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Sessions and Artifacts.

Ptah supplies the working world; humans and compatible systems supply intent and reasoning.

The complete roadmap is stored in `MASTER_ROADMAP.md`.

---

# Mandatory closure method

Every requirement must combine:

1. internal THETECHGUY foundation and intentional constraints;
2. primary capability donor;
3. completion donors;
4. mature upstream machinery and standards;
5. native Ptah contracts and integration;
6. fallback or exit path;
7. proof of the complete assembled subsystem.

One repository never closes a subsystem by itself.

Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

Research, corrections and decisions are saved after meaningful inspection units.

---

# Completed and saved work packages

## WP01 — Node and Workspace boundary

OpenClaw and Daytona established the first boundary:

- Node Protocol and Workspace Provider are separate contracts.
- Node, Workspace, Activity, Object and Session have separate identities and lifecycles.
- Large PTY, Object, display and media streams remain outside ordinary JSON control messages.

Saved evidence:

- `donors/OPENCLAW.md`
- `donors/DAYTONA.md`
- `decisions/ADR-0001-NODE-WORKSPACE-BOUNDARY.md`
- `work-packages/PHASE-0A-WP01-OPENCLAW-DAYTONA.md`

## WP02A — Workspace and execution composition

Inspected and saved:

- Coder;
- E2B and E2B Desktop;
- Development Containers Specification and CLI;
- DevPod;
- containerd and OCI Runtime/Image/Distribution specifications;
- OpenHands runtime family.

Accepted provisional direction:

- Ptah owns the provider-neutral Workspace Provider contract.
- Native local-process and OCI providers are the first owned implementations.
- Dev Containers is a compatibility/import standard, not Ptah's universal schema.
- Coder, E2B and DevPod are optional provider/compatibility paths.
- OpenHands is a caller/workload and interaction donor, not Ptah's identity.
- Provider limitations are explicit capabilities.
- Ptah identity survives provider replacement.

Saved evidence:

- `donors/CODER.md`
- `donors/E2B.md`
- `donors/E2B-DESKTOP.md`
- `donors/DEV-CONTAINERS-SPEC.md`
- `donors/DEV-CONTAINERS-CLI.md`
- `donors/DEVPOD.md`
- `donors/CONTAINERD-OCI.md`
- `donors/OPENHANDS.md`
- `work-packages/PHASE-0A-WP02A-WORKSPACE-EXECUTION-COMPOSITION.md`

## WP02B — Activities, events, recovery and observability

**External donor composition complete and saved.**

Inspected:

- Temporal Server;
- Temporal Rust/Core SDK;
- NATS Server and JetStream;
- Rust `async-nats` client;
- OpenTelemetry Collector, Collector Contrib and specification.

Accepted boundary:

1. Ptah owns a neutral Activity contract and Activity Ledger.
2. Temporal is the primary durable-orchestration backend candidate.
3. NATS is the primary low-latency internal Event Fabric candidate.
4. JetStream is the primary bounded replayable-event candidate.
5. OpenTelemetry/OTLP is the observability standard and Collector pipeline candidate.
6. None of those systems replaces Ptah's Object, Artifact, Activity or Session truth.
7. PTY, Object/file, display and media bytes use dedicated streams.
8. Side effects require operation IDs, idempotency keys, retry classes and durable receipts.
9. Disconnected Nodes require a Ptah-owned local journal/outbox and reconciliation model.
10. Proof-critical receipts are durable and unsampled even when ordinary telemetry is sampled.

Saved evidence:

- `donors/TEMPORAL.md`
- `donors/NATS-JETSTREAM.md`
- `donors/OPENTELEMETRY.md`
- `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`
- `work-packages/PHASE-0A-WP02B-ACTIVITY-EVENT-OBSERVABILITY.md`

---

# Active inspection unit

## WP02C — Internal core-runtime recovery

The external core-runtime composition is not enough. Before design closure, recover internal implementations and intentional behavior from:

- Hunter/AgentOps operation and job records;
- Hunter Foreman process/task state;
- Sergeant evidence, receipts and proof storage;
- TechGuy Relay registration, heartbeat and expiry experiments;
- Software Builder and other background workers;
- Hunter online/local synchronization and failure-continuation rules;
- existing terminal, process and browser bridges;
- MIBU correlation nonces, stale-result rejection and device evidence;
- relevant CodeOps bridge and artifact contracts.

For each internal source, record:

- what genuinely exists;
- exact files/components inspected;
- what is intentional versus incomplete;
- capability stronger than or missing from the external composition;
- what remains private;
- extract, wrap, adapt, rebuild or reject classification;
- proof already available and proof still needed.

Required saved output:

1. internal donor/recovery records;
2. comparison against WP02A/WP02B external composition;
3. updates to `CORE-001`, `CORE-002`, `CORE-004`, `CORE-005`, `RELAY-001`, `RELAY-002`, `EXEC-001`, `EXEC-002`, `SESSION-001`, `OBS-001`, `DIST-001` and `OFFLINE-001`;
4. amendments to ADR-0001 or ADR-0003 where internal evidence proves a stronger intentional design;
5. a core-runtime closure verdict for Phase 0B contract design.

---

# Requirements moving toward design closure

- `CORE-001 Persistent Workspace model` — external composite selected; internal recovery and provider conformance remain.
- `CORE-002 Concurrent Activity runtime` — Temporal/NATS/OTel composition selected; internal worker evidence and proof remain.
- `CORE-004 Facility/plugin host` — external tool/plugin patterns identified; internal engine boundaries remain.
- `CORE-005 Node Protocol` — boundary selected; internal relay/device evidence remains.
- `RELAY-001 Live events` — NATS/JetStream candidate selected; schema and internal reconciliation remain.
- `RELAY-002 Durable recovery` — Temporal candidate selected; internal retry/receipt semantics remain.
- `EXEC-001 Terminal/process supervision` — donor composition selected; internal process implementations remain.
- `EXEC-002 OCI provider` — containerd/OCI machinery selected; native provider contract and internal Docker work remain.
- `SESSION-001 Session Vault` — lifecycle and durable orchestration donors selected; internal recovery/sync evidence remains.
- `OBS-001 Observability` — OpenTelemetry selected; internal proof and semantic conventions remain.

No runtime requirement is yet approved for build.

---

# Accepted repository boundary

`ptah-roadmap-` owns the private roadmap, donor research, requirement closure, decisions, sequencing, progress and chat recovery.

`Ptah-space` owns public implementation, public-safe contracts, source, tests, releases and earned progress.

The complete private roadmap and private consumer relationships must not be copied into the public repository.

---

# No-build boundary

Allowed now:

- donor and internal-work recovery;
- source-level inspection and pinning;
- licence review;
- composite gap analysis;
- requirement closure and ADRs;
- proof/schema planning after Phase 0A review.

Not allowed yet:

- declaring closure from one donor;
- selecting dependencies from README claims alone;
- copying donor code;
- beginning runtime or large UI implementation;
- replacing internal work without evidence;
- exposing private consumers publicly.

---

# Phase 0A completion gate

Phase 0A moves to review only when every v1 requirement has a composite closure path, internal overlap, exact pins and licences, native gap, exit strategy and proof plan, or is explicitly parked/rejected with a replacement.

---

# Chat continuation instruction

Read this file first, followed by `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, `DONOR_RECOVERY.md`, `REQUIREMENT_CLOSURE_MATRIX.md`, relevant donor records, work-package records and accepted ADRs before proposing or performing further work.
