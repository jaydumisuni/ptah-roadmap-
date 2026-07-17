# Phase 0A Work Package 02 — Composite Runtime Closure

**Status:** ACTIVE  
**Started:** 2026-07-17  
**Build permission:** NOT GRANTED

## Purpose

Complete the runtime architecture that the OpenClaw–Daytona boundary pass only began.

The goal is not to select one winning repository. The goal is to assemble and prove the most complete compatible Ptah runtime from internal work, primary donors, completion donors, mature upstream machinery and native Ptah contracts.

Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

## Requirements in scope

- `CORE-001` Persistent workspace model
- `CORE-002` Concurrent activity runtime
- `CORE-005` Node Protocol and capability reporting
- `RELAY-001` Live event transport
- `RELAY-002` Durable activity recovery
- `EXEC-001` Terminal and process supervision
- `EXEC-002` OCI/container workspace provider
- `OBS-001` Logs, metrics, traces, correlation and resource accounting
- supporting parts of `SESSION-001`, `DIST-001` and `OFFLINE-001`

## Existing first-pass evidence

- `donors/OPENCLAW.md`
- `donors/DAYTONA.md`
- `decisions/ADR-0001-NODE-WORKSPACE-BOUNDARY.md`

These establish a useful boundary but do not close the subsystem.

## Inspection group A — Workspace and execution completion

Inspect:

1. Coder
2. E2B
3. E2B Desktop
4. Dev Container specification and a practical provider implementation
5. containerd
6. OCI runtime, image and distribution specifications
7. OpenHands
8. relevant internal THETECHGUY terminal, build, process and workspace code

Determine:

- persistent workspace ownership;
- local and remote provider lifecycle;
- process, filesystem, PTY, port and preview contracts;
- templates and portable environment descriptions;
- snapshots, archive, restore and provider capability truth;
- human and compatible-system access to the same workspace;
- owned deployment without vendor lock-in;
- provider conformance and exit strategy.

## Inspection group B — Activities, events and recovery completion

Inspect:

1. Temporal and the most appropriate Ptah SDK candidate
2. NATS Server
3. JetStream
4. likely Rust, TypeScript and Go NATS clients
5. OpenTelemetry Collector and specification
6. internal Foreman, AgentOps, Sergeant, relay and worker patterns

Determine:

- live control and progress transport;
- durable activity state and history;
- retries, cancellation, timers and checkpoints;
- worker leases and crash recovery;
- event ordering, replay cursors and backpressure;
- intermittent node behavior;
- correlation across control plane, node, provider, process, object and artifact;
- backend replaceability.

## Required donor record for each repository

Record:

- canonical URL;
- pinned commit or release;
- licence;
- activity/maintenance state;
- exact files and components inspected;
- verified capabilities;
- what it provides better than the current cluster;
- what it still lacks;
- code extraction boundary;
- integration classification;
- exit strategy;
- proof activity.

## Required architecture output

1. Updated composite closure rows in `REQUIREMENT_CLOSURE_MATRIX.md`.
2. Relay / Durable Activity boundary ADR.
3. Refined Node Protocol and Workspace Provider boundary if evidence requires it.
4. First draft of the complete runtime component map.
5. Clear list of native Ptah code after all donor overlap is removed.
6. Provider and activity conformance proof plans.

## Save-as-we-go rule

After each inspected donor or coherent donor pair:

- save the donor record;
- update the requirement rows it affects;
- record missing capabilities and the next completion donor;
- update `CURRENT_STATE.md`;
- update `PROGRESS.md` or save an evidence-backed progress record;
- create or amend an ADR if a boundary changes.

Do not wait until the whole work package is finished to save conclusions.

## Completion gate

This work package closes only when the runtime cluster collectively covers:

- stable node connection and capability publication;
- persistent workspaces through replaceable providers;
- concurrent activities independent of workspace lifecycle;
- live ordered events;
- durable history and crash recovery;
- reconnectable terminals and processes;
- OCI/container execution owned by Ptah-compatible infrastructure;
- end-to-end observability;
- local, online and future multi-node operation;
- explicit licences and exit strategies;
- validation proving the combined subsystem rather than one donor.

No runtime implementation begins from this work package without separate review and approval.
