# Ptah Current State

**Last updated:** 2026-07-17  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Sessions and Artifacts.

It is intended to support files, repositories, terminals, browsers, containers, applications, firmware, devices, media, documents, storage, transfer, rendering and recovery.

Ptah is the world where work occurs; the human or compatible caller supplies intent and reasoning.

The complete roadmap is stored in `MASTER_ROADMAP.md`.

---

# Mandatory requirement-closure method

A subsystem is not complete because one repository was selected.

Every Ptah requirement must combine:

1. internal THETECHGUY foundation and real operating requirements;
2. primary capability donor;
3. completion donors for the primary donor's missing capabilities;
4. mature upstream machinery and standards;
5. native Ptah contracts and integration;
6. fallback or exit donor;
7. validation of the complete assembled subsystem.

Canonical decision: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

Research and decisions must be saved as meaningful inspection units finish.

---

# Work package status

## WP01 — OpenClaw and Daytona boundary pass

**Status:** COMPLETED AND SAVED

Established:

- Ptah owns separate Node Protocol and Workspace Provider contracts.
- A Node is a capability host; it is not a Workspace.
- Workspace, Activity, Object, Session and Node remain different records and lifecycles.
- Large terminal, object, display and media streams remain separate from the JSON control envelope.
- OpenClaw is a Node/gateway protocol donor, not Ptah Core.
- Daytona is a workspace-lifecycle architecture donor, not an adopted foundation.

Saved:

- `donors/OPENCLAW.md`
- `donors/DAYTONA.md`
- `decisions/ADR-0001-NODE-WORKSPACE-BOUNDARY.md`
- `work-packages/PHASE-0A-WP01-OPENCLAW-DAYTONA.md`

## WP02A — Workspace and execution donor composition

**Status:** FIRST-PASS DONOR COMPOSITION COMPLETED AND SAVED

Inspected:

- Coder;
- E2B;
- E2B Desktop;
- Development Containers Specification;
- Dev Container CLI;
- DevPod;
- containerd and OCI Runtime/Image/Distribution specifications;
- OpenHands transition repository, Software Agent SDK and Agent Canvas.

Saved:

- `donors/CODER.md`
- `donors/E2B.md`
- `donors/E2B-DESKTOP.md`
- `donors/DEV-CONTAINERS-SPEC.md`
- `donors/DEV-CONTAINERS-CLI.md`
- `donors/DEVPOD.md`
- `donors/CONTAINERD-OCI.md`
- `donors/OPENHANDS.md`
- `work-packages/PHASE-0A-WP02A-WORKSPACE-EXECUTION-COMPOSITION.md`

Provisional architecture direction:

1. Ptah owns the provider-neutral Workspace Provider contract.
2. Native local-process and OCI providers are the first owned implementations.
3. OCI standards are foundational for container compatibility.
4. Dev Container definitions are a supported import/compatibility format, not Ptah's universal schema.
5. Coder, E2B and DevPod remain optional provider or protocol-compatibility paths.
6. Graphical Application/Display sessions are distinct activities and may use several backends.
7. OpenHands and similar systems are callers or workloads, not Ptah's identity.
8. Provider limitations such as pause, fork, checkpoint, migration and multi-stream display are explicit capabilities.
9. Ptah Object, Activity, Workspace and Session identity must survive provider replacement.

The full composition is recorded in the WP02A work-package file.

---

# Active inspection unit

## WP02B — Activities, events, recovery and observability

Inspect as one complementary group:

1. Temporal server and the most suitable SDK/runtime boundary;
2. NATS Server, JetStream and appropriate clients;
3. OpenTelemetry Collector and specifications;
4. internal THETECHGUY worker, relay, terminal, logging and recovery patterns.

Resolve:

- public Node Protocol versus internal event fabric;
- live events versus durable workflow history;
- retries, cancellation, timers and checkpoints;
- worker leases, crash recovery and activity resumption;
- event ordering, sequence, replay, retention and backpressure;
- trace, log, metric and resource correlation across control plane, Node, provider, Activity, Object and Artifact;
- direct adoption versus replaceable compatibility contracts.

Required saved output:

- donor records for each inspected source;
- a composite runtime closure record;
- Relay / Durable Activity / Observability boundary ADR;
- Requirement Closure Matrix updates for `CORE-002`, `RELAY-001`, `RELAY-002`, `OBS-001` and related runtime rows;
- `PROGRESS.md` and this file updated after each meaningful unit.

---

# Requirements moving toward design closure

- `CORE-001 Persistent workspace model` — composite candidate selected; internal recovery and conformance proof remain.
- `CORE-005 Node Protocol` — boundary selected; full event/recovery cluster remains.
- `EXEC-001 Terminal and process supervision` — donor composition selected; native implementation and durable recovery remain.
- `EXEC-002 OCI/container Workspace Provider` — OCI machinery and completion donors selected; provider contract and proof remain.
- `APP-002 Linux graphical application runtime` — first donor patterns selected; alternate display gateways and concurrency proof remain.
- `SESSION-001 Checkpoint/resume` — lifecycle donors selected; durable workflow, storage and sync work remain.

No runtime requirement is yet fully closed for build.

---

# Accepted repository boundary

## `ptah-roadmap-`

Owns the private master roadmap, donor research, requirement closure, decisions, sequencing, progress ledger, chat recovery memory and future OS-integration notes.

## `Ptah-space`

Owns public implementation, public-safe contracts and architecture required by contributors, tests, schemas, source, releases and earned public progress.

The complete private roadmap and private consumer relationships must not be copied into `Ptah-space`.

---

# No-build boundary

Allowed now:

- donor and internal-work recovery;
- source-level inspection and canonical pinning;
- licence review;
- composite donor and gap analysis;
- requirement closure;
- architecture decisions;
- proof and schema planning after Phase 0A review.

Not allowed yet:

- declaring a subsystem complete from one donor;
- selecting dependencies from README claims alone;
- copying donor code;
- beginning the runtime or large UI;
- replacing internal systems without evidence;
- exposing private consumers in public Ptah.

---

# Phase 0A completion gate

Phase 0A can move to review only when:

- every v1 requirement has a recorded composite closure path;
- selected donors have canonical URLs, pinned versions and licence decisions;
- exact files/components studied are recorded;
- primary-donor gaps and completion donors are explicit;
- internal overlap and intentional constraints are recovered;
- native Ptah gaps are isolated;
- every selected foundation has an exit strategy;
- validation activities prove the assembled subsystem;
- no unresolved or abandoned source is critical without a replacement path.

---

# Chat continuation instruction

A future chat must read this file first, followed by `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, `DONOR_RECOVERY.md`, `REQUIREMENT_CLOSURE_MATRIX.md`, relevant donor records, work-package records and accepted ADRs before proposing or performing the next work.
