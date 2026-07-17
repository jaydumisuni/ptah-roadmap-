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

> Produce the Ptah Requirement Closure Matrix and complete donor records before selecting implementation dependencies or writing runtime code.

## Work package 01 — completed

OpenClaw and Daytona were inspected side by side at source level.

Saved evidence:

- `donors/OPENCLAW.md`
- `donors/DAYTONA.md`
- `decisions/ADR-0001-NODE-WORKSPACE-BOUNDARY.md`
- populated first rows in `REQUIREMENT_CLOSURE_MATRIX.md`

Accepted findings:

1. OpenClaw is the primary architecture donor for Ptah Node Protocol patterns, not a direct Ptah Core dependency.
2. Daytona is a useful historical architecture donor for workspace lifecycle, runners and snapshots, but is not an adopted foundation because its public codebase is unmaintained and AGPL-3.0.
3. Ptah owns its Node Protocol and Workspace Provider contracts.
4. A node is a physical or virtual capability host.
5. A workspace provider is one facility available through a node.
6. Node, Workspace, Activity, Object and Session remain separate records and lifecycles.
7. Large object, terminal, display and media streams must be separate from the JSON control envelope.

## Current donor pool

The active pool includes:

- internal THETECHGUY repositories and unfinished work;
- OpenClaw organisation projects;
- Daytona, E2B, Coder, OpenHands;
- Temporal and NATS;
- containerd, OCI, BuildKit, Dagger;
- OpenTelemetry;
- Witness, in-toto, Cosign, ORAS;
- Playwright, Playwright MCP, Browser-Use, TurboWebFetch;
- STF, adbkit, Appium, scrcpy, Android platform tools, TouchPilot;
- decomposition, media, document, executable, firmware, filesystem, knowledge, security, and documentation donors listed in `DONOR_RECOVERY.md`.

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
- donor adoption/wrap/adaptation/rejection decisions;
- schema and proof planning after Phase 0A review.

Not allowed yet:

- choosing dependencies from README claims alone;
- copying donor code;
- building a large UI;
- starting the runtime because a donor looks promising;
- replacing existing internal systems without evidence;
- exposing private consumers in the public repository.

---

# Immediate next actions

## Work package 02 — Durable activities and live event fabric

Inspect side by side:

1. Temporal and the most suitable Ptah SDK candidate.
2. NATS Server, JetStream and likely Rust/TypeScript/Go clients.

Resolve:

- public control protocol versus internal event bus;
- live events versus durable workflow history;
- retry, cancellation, timer and checkpoint semantics;
- event sequence, replay and backpressure;
- worker leases, crash recovery and activity resumption;
- whether Ptah v1 should adopt these directly, wrap them, or preserve replaceable compatibility contracts.

Then:

3. Save donor records.
4. Create the Relay / Durable Activity boundary decision.
5. Update `REQUIREMENT_CLOSURE_MATRIX.md` for `CORE-002`, `RELAY-001` and `RELAY-002`.
6. Update `PROGRESS.md` and this file.

---

# Completion evidence for Phase 0A

Phase 0A can move to review only when:

- every v1 requirement has a recorded closure path;
- each selected donor has a pinned version and licence decision;
- exact files/components studied are recorded;
- limitations and non-inheritance boundaries are explicit;
- internal overlap is identified;
- native Ptah gaps are isolated;
- no selected foundation depends on an unresolved or abandoned source without an exit strategy.

---

# Chat continuation instruction

A future chat must read this file first, then `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, `DONOR_RECOVERY.md`, the donor records, and accepted ADRs before proposing next work.