# Ptah requirements and decisions recovery ledger

Status: accepted recovered baseline under Phase 0C-16 — runtime implementation remains unauthorized

Recorded: 2026-07-21

## Purpose

This ledger recovers the product requirements, architecture laws, accepted decisions, frozen contracts, Phase 0C selections, donor conclusions, operating constraints and known gaps that must feed the complete Ptah Master Plan and its derived implementation roadmap.

It is intentionally a recovery index rather than a replacement for the referenced contracts, ADRs, fixtures or evidence. A future chat or AI must be able to begin here, follow the source hierarchy, and continue without reconstructing prior conversation history.

## Canonical source hierarchy

When records disagree, use this order:

1. accepted ADRs and accepted owner decisions;
2. `CURRENT_STATE.md`;
3. frozen/proven implementation and conformance evidence;
4. current `jaydumisuni/Ptah-space` source;
5. the complete `MASTER_PLAN.md` once accepted;
6. the derived `IMPLEMENTATION_ROADMAP.md` once accepted;
7. frozen Phase 0B work packages and catalogs;
8. `PROGRESS.md`;
9. donor and internal recovery records;
10. old chat text or conversational memory.

A newer edit is not automatically more authoritative than an older accepted decision.

## Recovered foundational intent

Ptah Space is an independent, open-source, online-first and later local-first digital working world. It provides persistent workspaces, concurrent activities, terminals, browsers, repositories, containers, applications, devices, storage, transfers, object understanding, artifacts, recovery and neutral integration contracts.

Humans and compatible software systems provide intent, reasoning, policy, priorities, restrictions and acceptance criteria. Ptah is the environment and evidence substrate; it is not the intelligence or organizational authority deciding what should happen.

## Non-negotiable architecture laws recovered

1. Ptah is the world, not the thinker.
2. A Workspace is persistent and is not the same thing as one job or chat.
3. Many Activities may run independently inside one Workspace.
4. Files and other inputs are structured Objects with immutable Content, Revisions, Views, Artifacts, Relationships, Locations and provenance.
5. Original bytes remain preserved unless an explicit reviewed replacement operation occurs.
6. Internet access is a normal capability; restrictions are explicit Policy or deployment choices.
7. Active work uses fast local storage; object storage is not a live build filesystem.
8. Online, local and distributed Ptah use the same identities and contracts.
9. Rust is the operational chassis where useful, but mature engines remain behind neutral adapters.
10. Backend IDs, paths, process IDs, container IDs and provider IDs never become canonical Ptah identity.
11. Retry creates a new Attempt; restart creates a new Generation; stale authority is fenced.
12. Acknowledgement, observation, verification, review, acceptance and authoritative external truth remain distinct.
13. Negative, failed, blocked, partial and inconclusive outcomes remain visible evidence.
14. Existing internal and external work is recovered before rebuilding.
15. Public Ptah remains neutral and excludes private THETECHGUY data, restricted workflows, secrets and private Hunter knowledge.
16. No implementation begins merely because an idea is useful; it must be placed, dependency-ordered, approved and proved.
17. Completion follows Understand → Build → Review → Freeze → Prove → Submit/Ship.
18. The permanent local system must package proven Ptah services instead of redesigning them.

## Recovered product requirement families

### World and identity

- stable UUIDv7-based canonical identities;
- typed entity families and absolute schema URNs;
- versioned, namespaced lifecycle machines;
- scoped Aliases for backend and external identifiers;
- explicit supersession, tombstone, retention and referential integrity;
- directional migrations and backend replacement.

Primary frozen authority: WP01.

### Durable work and evidence

- Activity, Operation and Attempt separation;
- independent concurrency, cancellation, retry and failure propagation;
- Event streaming and telemetry without conflating them with truth;
- immutable Receipts and Evidence;
- exact producer, Provider Generation and implementation commit binding;
- negative and inconclusive result retention.

Primary frozen authority: WP02.

### Object world and storage

- Content identity separate from Object role and Artifact role;
- immutable Revisions;
- plural detector claims and disagreements;
- progressive Views, child relationships and derivatives;
- digest-addressed bytes and location-independent identity;
- layered hot storage, durable storage, cache, replica and backup semantics.

Primary frozen authority: WP03.

### Nodes, Facilities and Providers

- stable Node identity across restart;
- Node Generation for each agent/runtime start;
- Facility as stable capability contract;
- Provider revision, instance and generation separation;
- capability, locality, health, pressure, reachability, readiness and dispatch eligibility kept distinct;
- replacement, fencing, limitations and truthful health reporting.

Primary frozen authority: WP04.

### Workspace, Session and recovery

- persistent Workspace identity;
- Session attach/detach and client-specific projections;
- Workspace-scoped Objects, Activities, terminals, browsers, applications and Artifacts;
- checkpoint creation, verification, restore and Recovery Verification as separate stages;
- restart and provider replacement produce new generations;
- uncertain external effects are retained rather than erased.

Primary frozen authority: WP05.

### Transfer, synchronization and backup

- upload and resumable download;
- retained partial state, streaming digest and destination read-back;
- Transfer, Sync and Backup as distinct contracts;
- explicit conflicts and resolutions;
- provider acknowledgement cannot claim byte acceptance;
- restored storage is not automatically recovered Workspace/application state.

Primary frozen authority: WP06.

### Recipe, Build and provenance

- Recipe, Revision, Proposal, Acceptance, Readiness, Plan, Run and Step separation;
- deterministic inputs, environments, tools, caches and secrets evidence;
- Artifact composition, SBOM, attestation, signature and verification separation;
- independent reproduction and release acceptance;
- no cache hit, build completion or signature alone equals release acceptance.

Primary frozen authority: WP07.

### Domain Packs, firmware, disks and Devices

- versioned detect, inventory, decompose, preview, transform, validate, compare, rebuild and execute contracts;
- progressive decomposition with explicit skipped, unknown and unsupported ranges;
- firmware package, disk image and physical Device operation separation;
- Device identity, protocol operation, connection epoch, lease and recovery evidence;
- static analysis or write acknowledgement never substitutes for authorized physical mutation plus read-back verification.

Primary frozen authority: WP08.

### Applications, Browser, semantic UI and human Shell

- Application, Installation, Session, Process, Window and display separation;
- Browser Profile, Process, Context, Page, navigation, download and evidence separation;
- semantic provider/snapshot/target/selector/action with stale-target reacquisition and post-condition read-back;
- human Shell client, Shell Session, panels, layouts, responsive projections and scoped control transfer;
- UI state never replaces runtime truth.

Primary frozen authority: WP09.

### Knowledge, Data, Package and Plugin

- neutral Knowledge Source, Corpus, Document and Index Revisions;
- Query, Result and Citation with source-bound answers;
- Dataset, Table and structured data processing;
- Package, Release, Installed Plugin and Activation identities;
- indexes are derived and replaceable;
- caller reasoning and private memory remain outside Ptah Core.

Primary frozen authority: WP10.

### Isolation, placement and secure grants

- Isolation Class and Runtime Provider separation;
- Node Capability Snapshot, Placement Request and Placement Decision;
- Reservation, Lease, Generation and Fence;
- explicit secure Grant scope, expiry, revocation and audience;
- no silent weakening of isolation or authority;
- checkpoint compatibility and movement constraints.

Primary frozen authority: WP11.

### Security findings and reproduction

- exact authorization, target, plan, machinery and coverage;
- Observation, Correlated Finding, disposition and bounded Claim separation;
- remediation and Verification Run;
- Reproduction Run and Evidence Card;
- no scanner output becomes accepted truth without the required review and verification.

Primary frozen authority: WP12.

### Executable conformance

- offline JSON and JSON Schema validation;
- local URN and `$ref` resolution;
- catalog, lifecycle, fixture and migration integrity;
- cross-contract semantic rules;
- deterministic structural and semantic reports.

Primary frozen authority: WP13.

### Golden, negative and proof corpus

- lawful source, licence, privacy, audience and admission controls;
- immutable expected-proof records;
- paired positive, negative and adversarial fixtures;
- exact first vertical-slice proof plan;
- green summaries without retained reports fail acceptance.

Primary frozen authority: WP14.

## Recovered Phase 0C selections

- public implementation repository: `jaydumisuni/Ptah-space`;
- private control and recovery authority: `jaydumisuni/ptah-roadmap-`;
- Ubuntu Server 24.04.4 amd64 pinned host candidate;
- kernel `6.8.0-136-generic` pinned physical proof target;
- Rust `1.97.1` primary toolchain;
- SQLite `3.53.3` behind repository-owned ledger interfaces;
- native Linux PTY/process supervision;
- containerd `2.3.1` with runc `1.4.2` behind the OCI Provider boundary;
- Node.js `24.18.0`, Playwright `1.60.0` and pinned Chromium for the first Browser Provider;
- hardened Git `2.55.0` process adapter;
- libarchive `3.8.7` first decomposition adapter;
- repository-owned resumable transfer and local content-addressed storage;
- Apache License 2.0 for public repository-owned Ptah source;
- rights-holder wording `John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS`;
- private THETECHGUY systems, data, restricted adapters, donor source and trademarks remain excluded.

## Recovered source and repository boundaries

### Public `Ptah-space`

Permitted:

- generic Ptah runtime source;
- public contracts and generated bindings;
- generic adapters for publicly documented tools and protocols;
- lawful generic fixtures;
- public operator/developer documentation;
- accepted licences and notices.

Excluded:

- private Domain Packs and proprietary procedures;
- customer, employee, payment and device records;
- credentials, signing material and production topology;
- restricted recovery or bypass adapters;
- private Hunter prompts, memory and knowledge stores;
- uncleared donor source.

### Private `ptah-roadmap-`

Owns:

- master product plan;
- implementation roadmap and sequencing;
- private donor recovery;
- accepted decisions and work-package history;
- current state and progress;
- recovery/handoff state;
- implementation authorization.

## Recovered implementation task graph

The first vertical slice already has fourteen ordered tasks:

1. repository and contract-lock scaffold;
2. Node identity and Generation substrate;
3. ledger and migrations;
4. Activity/Operation/Attempt runtime;
5. PTY and multi-terminal Provider;
6. persistent Workspace and Session;
7. Object/Revision/Artifact and local CAS;
8. resumable transfer engine;
9. hardened Git Provider;
10. OCI container Provider;
11. Browser Provider;
12. archive decomposition Provider;
13. checkpoint, restart and verified recovery;
14. exact-head vertical-slice acceptance run.

The detailed implementation roadmap must retain this order and extend it into the full Phase 1–13 programme.

## Recovered real workload candidates

After the generic first slice proves its substrate:

1. `jaydumisuni/linux-0.11-rs` — external systems/build/disk/QEMU/serial workload;
2. `jaydumisuni/TTG-Device-X-Ray` — read-only Device and evidence workload;
3. `jaydumisuni/thetechguy-device-manager` — reversible Android DPC policy workload;
4. `jaydumisuni/MIBU` — cross-application and physical-device workflow;
5. separately reviewed Approved Device Recovery adapters.

Workload-specific identity, source, customer data and restricted behavior remain outside Ptah Core.

## Recovered AI Project Workspace composition

Profile candidate: `ptah.workspace.ai_project.v1`.

It composes existing Workspace, Session, Activity, Event, Attempt, Object, Revision, View, Artifact, Knowledge, Policy, Facility, Provider, Grant, Recipe and Receipt primitives.

Required behavior:

- project/workspace purpose and instructions;
- source-authority classes;
- bounded, inspectable context packets;
- Workspace-only privacy and explicit cross-Workspace denial;
- model-independent handoff and resume;
- explicit Facility Grants;
- scheduled Activities receive only explicitly granted Artifacts;
- generated model output begins as `generated_candidate` and cannot directly become canonical truth.

Hunter plans and coordinates. Ptah owns durable truth, identities, Grants, Activities, Artifacts, evidence and recovery. The owner approves protected actions and truth promotion.

## Recovered operating and release direction

- online service first;
- exact one-node vertical slice first;
- direct human operation must work without an AI caller;
- optional Facilities may fail without collapsing unrelated work;
- local mini-PC and workstation reuse the same contracts;
- distributed Nodes follow proven one-node behavior;
- private OS assembly follows proven services;
- milestones progress from architecture closure to Online Alpha, Object World Beta, Firmware/Device Beta, Full Workspace Release, Distributed Ptah and OS-ready foundation.

## Recovered parked or restricted items

- `.P5C` remains parked pending a lawful sample, specification or verified parser;
- distributed shared POSIX storage remains parked until measured need exceeds Object transfer/cache;
- MiniRouter source reuse remains blocked by licence/source review;
- Dify source integration remains restricted by licence;
- compositor-specific non-GNOME Wayland semantics remain partial/parked;
- unaudited private Device Manager modules remain a source-recovery gap;
- donor source without a clear licence remains blocked from reuse.

These items are not v1 blockers unless a later accepted decision explicitly promotes them.

## Authority defects found during recovery

1. `MASTER_ROADMAP.md` contains valuable architecture and phase intent but its status header still says Phase 0B active and it does not provide a sufficiently detailed execution programme for every phase.
2. `DECISIONS.md` stops at WP07 even though WP08–WP14, Phase 0B freeze, Phase 0C selections, licence acceptance and the AI Project Workspace candidate were later accepted.
3. `DONOR_RECOVERY.md` still describes a final Phase 0A consistency review as active even though Phase 0A is frozen.
4. root `README.md` still describes the current position as Phase 0A donor closure.
5. `PROGRESS.md` contains a useful Phase 1–13 index but not a dependency-complete implementation ledger.
6. No single accepted document currently defines users, operator roles, product surfaces, deployment modes, service boundaries, operational responsibilities, release gates and the exact definition of a finished Ptah programme.
7. No single machine-readable handoff index binds the master plan, derived roadmap, reconciliation status, blockers and exact next action.

## Required closure outputs

This recovery ledger must feed and remain synchronized with:

- `MASTER_PLAN.md` — complete product and operating plan;
- `IMPLEMENTATION_ROADMAP.md` — dependency-ordered delivery programme;
- `planning/MASTER-PLAN-RECONCILIATION.md` — WP01–WP14 and Phase 0C mapping;
- `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md` — remaining evidence and authorization sequence;
- `AI_HANDOFF.md` — concise recovery entry point for any chat or AI;
- `master-plan-index.json` — machine-readable authority and checkpoint index;
- updated `README.md`, `MEMORY_PROTOCOL.md`, `DECISIONS.md`, `PROGRESS.md` and `CURRENT_STATE.md`.

## Current checkpoint

Recovered requirements and decisions: ACCEPTED THROUGH PHASE 0C-16.

Physical pinned-host evidence: OPEN.

ADR-0033: PROPOSED.

Runtime implementation: NOT AUTHORIZED.
