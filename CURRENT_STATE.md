# Ptah Current State

**Last updated:** 2026-07-17  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

The Ptah concept and full replacement architecture have been accepted in principle.

Ptah is:

- independent and open source;
- online first;
- a concurrent digital world rather than a reasoning system;
- built around persistent workspaces, objects, activities, facilities, nodes, sessions, and artifacts;
- capable of files, repositories, terminals, browsers, containers, applications, firmware, devices, media, documents, storage, transfer, rendering, and recovery;
- intended to reuse and improve proven internal and external machinery instead of rebuilding everything blindly.

The complete roadmap is stored in `MASTER_ROADMAP.md`.

---

# Active work

## Phase 0A — Donor recovery and requirement closure

Current objective:

> Close every Ptah requirement through the best compatible donor composition, native Ptah boundary, exit strategy and proof plan before selecting implementation dependencies or writing runtime code.

## Mandatory recovery method

A subsystem is not complete because one repository was selected.

Every requirement must combine:

1. internal THETECHGUY foundation and real operating requirements;
2. primary capability donor;
3. completion donors for the primary donor's missing capabilities;
4. mature upstream machinery and standards;
5. native Ptah contracts and integration;
6. fallback or exit donor;
7. validation of the complete assembled subsystem.

Canonical decision: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

## Work package 01 — boundary pass completed

OpenClaw and Daytona were inspected side by side at source level.

Saved evidence:

- `donors/OPENCLAW.md`
- `donors/DAYTONA.md`
- `decisions/ADR-0001-NODE-WORKSPACE-BOUNDARY.md`
- `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`
- populated first rows in `REQUIREMENT_CLOSURE_MATRIX.md`

Accepted boundary findings:

1. OpenClaw is the first primary architecture donor for Ptah Node Protocol patterns, not a direct Ptah Core dependency.
2. Daytona is a useful historical donor for workspace lifecycle, runners and snapshots, but is not an adopted foundation because its public codebase is unmaintained and AGPL-3.0.
3. Ptah owns its Node Protocol and Workspace Provider contracts.
4. A node is a physical or virtual capability host.
5. A workspace provider is one facility available through a node.
6. Node, Workspace, Activity, Object and Session remain separate records and lifecycles.
7. Large object, terminal, display and media streams must be separate from the JSON control envelope.

These findings establish the boundary only. They do not close the full runtime subsystem.

## Runtime donor cluster still open

The OpenClaw–Daytona combination must be completed by inspecting what each lacks:

- Coder, E2B and Dev Containers for persistent and portable workspace patterns;
- containerd and OCI specifications for the owned execution foundation;
- OpenHands for agent/computer workspace interaction and event trajectories;
- Temporal for durable activities, history, retries and recovery;
- NATS and JetStream for live event transport and intermittent node communication;
- OpenTelemetry for end-to-end correlation and resource observability;
- internal THETECHGUY process, terminal, worker, relay and recovery patterns.

Only after this cluster is inspected can `CORE-001`, `CORE-002`, `CORE-005`, `RELAY-001`, `RELAY-002`, `EXEC-001`, `EXEC-002` and `OBS-001` move toward design closure.

## Current donor pool

The active pool includes:

- internal THETECHGUY repositories and unfinished work;
- OpenClaw organisation projects;
- Daytona, E2B, Coder, OpenHands and Dev Containers;
- Temporal and NATS;
- containerd, OCI, BuildKit and Dagger;
- OpenTelemetry;
- Witness, in-toto, Cosign and ORAS;
- Playwright, Playwright MCP, Browser-Use and TurboWebFetch;
- STF, adbkit, Appium, scrcpy, Android platform tools and TouchPilot;
- decomposition, media, document, executable, firmware, filesystem, knowledge, security and documentation donors listed in `DONOR_RECOVERY.md`.

---

# Accepted repository boundary

## `ptah-roadmap-`

Owns:

- master roadmap;
- current state;
- tickable progress;
- donor research;
- requirement closure;
- private decisions;
- sequencing;
- chat recovery memory;
- future local/OS integration notes.

## `Ptah-space`

Owns:

- public implementation;
- public-safe architecture and contracts needed by contributors;
- the build slice currently being implemented;
- tests, schemas, source, releases, and earned public progress.

The full private roadmap must not be copied into the public Ptah repository.

---

# No-build boundary

No Ptah runtime implementation is currently approved.

Allowed now:

- donor recovery;
- canonical URL and upstream verification;
- licence review;
- exact source-tree inspection;
- requirement closure matrix;
- internal existing-work recovery;
- donor composition and gap analysis;
- donor adoption, wrap, adaptation and rejection decisions;
- schema and proof planning after Phase 0A review.

Not allowed yet:

- choosing dependencies from README claims alone;
- declaring a subsystem complete from one donor;
- copying donor code;
- building a large UI;
- starting the runtime because a donor looks promising;
- replacing existing internal systems without evidence;
- exposing private consumers in the public repository.

---

# Immediate next actions

## Work package 02 — Complete the core runtime donor cluster

Inspect in coordinated groups rather than isolated winners.

### Workspace and execution completion

1. Coder
2. E2B and E2B Desktop
3. Dev Container specification and a provider implementation
4. containerd and OCI runtime/image specifications
5. OpenHands workspace/runtime boundaries

Resolve what OpenClaw and Daytona do not fully cover:

- owned local execution;
- persistent human-and-system workspaces;
- provider portability;
- process, filesystem, PTY and port contracts;
- snapshots and recovery without vendor lock-in;
- container/runtime separation;
- platform and capability conformance.

### Activities, events and recovery completion

6. Temporal and the most suitable Ptah SDK candidate
7. NATS Server, JetStream and likely Rust/TypeScript/Go clients
8. OpenTelemetry Collector and specification

Resolve:

- public Node Protocol versus internal event fabric;
- live events versus durable workflow history;
- retries, cancellation, timers and checkpoints;
- event sequence, replay and backpressure;
- worker leases, crash recovery and activity resumption;
- trace and metric correlation across control plane, node, provider and artifact.

### Required saved output

9. Create donor records for every inspected repository.
10. Record each donor's strengths and missing capabilities.
11. Update the runtime requirement rows with primary and completion donor sets.
12. Create the Relay / Durable Activity boundary ADR.
13. Amend ADR-0001 if the full donor cluster changes its provider or protocol boundary.
14. Update `PROGRESS.md` and this file after each meaningful inspection unit.

---

# Completion evidence for Phase 0A

Phase 0A can move to review only when:

- every v1 requirement has a recorded composite closure path;
- each selected donor has a pinned version and licence decision;
- exact files/components studied are recorded;
- primary-donor gaps and completion donors are explicit;
- limitations and non-inheritance boundaries are explicit;
- internal overlap is identified;
- native Ptah gaps are isolated;
- every selected foundation has an exit strategy;
- no selected foundation depends on an unresolved or abandoned source without a replacement path.

---

# Chat continuation instruction

A future chat must read this file first, then `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, `DONOR_RECOVERY.md`, the donor records, and accepted ADRs before proposing next work.
