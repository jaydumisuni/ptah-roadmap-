# Ptah Space — Complete Master Plan

Status: accepted product and operating authority — runtime implementation remains unauthorized

Version: 1.0.0

Recorded: 2026-07-21

Public implementation repository: `jaydumisuni/Ptah-space`

Private plan, recovery and authorization repository: `jaydumisuni/ptah-roadmap-`

## 1. Plan authority and purpose

This document defines what Ptah is intended to become, who it serves, what it must and must not own, how it operates online and locally, how humans and software systems interact with it, how it is built and operated, and what evidence is required before it can be called complete.

It is the product and operating plan. The dependency-ordered delivery programme is maintained separately in `IMPLEMENTATION_ROADMAP.md`.

The older `MASTER_ROADMAP.md` remains retained historical architecture and phase source material. Under accepted ADR-0034, this document is the primary product and operating authority and `IMPLEMENTATION_ROADMAP.md` is the primary delivery-sequencing authority.

## 2. Executive definition

Ptah Space is an independent, open-source, online-first and later local-first digital working world in which humans and compatible software systems can receive, store, inspect, decompose, run, build, transform, render, compare, move, resume, recover and verify files, repositories, applications, firmware, devices, environments and artifacts.

Ptah provides the world and machinery:

- persistent Workspaces;
- concurrent Activities;
- terminals, processes and services;
- repositories and builds;
- browsers and live internet;
- containers, virtual machines, emulators and remote Nodes;
- applications and physical Devices;
- structured Objects, Revisions, Views and Artifacts;
- transfer, synchronization, backup and recovery;
- Knowledge, Data, Packages, Plugins and deterministic Recipes;
- provenance, security evidence and reproducibility;
- human-facing and machine-facing control surfaces.

The caller provides intent, reasoning, policy, priority, business judgment and acceptance criteria. Hunter may coordinate work through Ptah, but Ptah does not become Hunter and Hunter does not own Ptah truth.

## 3. Problem Ptah solves

Modern technical work is fragmented across chat sessions, local terminals, cloud sandboxes, browsers, download tools, build systems, device utilities, storage providers, remote desktops, evidence folders and project trackers. State disappears when a process, client, provider or conversation ends. Files are treated as opaque blobs. Backends leak their temporary identifiers into product logic. Failures are hidden behind optimistic success messages. Human and AI collaborators repeatedly reconstruct context.

Ptah solves this by providing one coherent, durable and evidence-bound world with stable identities and replaceable providers.

The platform must expose enough exact state for an authorized caller to answer questions such as:

- What Workspace are we in?
- What Objects, Revisions and Artifacts exist?
- What Activities are running, waiting, failed or complete?
- Which Node and Provider Generation performed each action?
- What Receipts and evidence were retained?
- What mechanically recoverable state exists after interruption?
- What configured Grants, Leases and Fences apply to this caller or Activity?
- What caller-supplied labels and provenance are stored on each record?
- Can the same stored work continue on another compatible Node or with another model/provider?

Ptah exposes and preserves the records. The caller decides meaning, relevance, authority, correctness and next action.

## 4. Product principles

1. **Ptah is the world, not the thinker.**
2. **Workspace and Activity are different.** One Workspace may host many independent Activities.
3. **Objects are structured and versioned.** Original bytes, children, derivatives, Views and Artifacts remain linked.
4. **Canonical identity is backend-neutral.** Paths, process IDs, container IDs and provider IDs remain scoped Aliases or evidence.
5. **Concurrency is foundational.** Heavy work may not globally block unrelated terminals, browsers, transfers or Activities.
6. **Recovery is explicit.** Checkpoint existence is not proof of successful restore.
7. **Acknowledgement is not completion.** Post-condition verification is required where the contract demands it.
8. **Negative results are evidence.** Failed, partial, blocked and inconclusive outcomes remain visible.
9. **Internet is normal.** Offline and restricted modes are explicit deployments or Policies.
10. **Active work is local to a capable Node.** Durable object storage is not used as a live build filesystem.
11. **Polyglot integration is preferred over unnecessary rewrites.** Mature engines sit behind Ptah contracts.
12. **Public Ptah is neutral.** Private THETECHGUY knowledge and customer/device data stay outside public Core.
13. **Human use is first-class.** A human must be able to operate the system without an AI caller.
14. **Model and provider replacement must not erase caller-owned records, configured access or provenance.**
15. **Completion is evidence-backed.** Source presence and UI claims are insufficient.

## 5. Intended users and participants

### 5.1 Human owner or administrator

The owner:

- creates and closes high-level goals;
- controls deployment, funding and private integration decisions;
- approves protected or destructive actions;
- accepts architecture and release decisions;
- promotes reviewed candidates into canonical truth;
- accepts evidence required for implementation authorization and release.

### 5.2 Human operator

An operator:

- creates or opens Workspaces;
- uploads, downloads and organizes Objects;
- starts and supervises Activities;
- uses terminals, browsers, containers, applications and Devices;
- reviews evidence, failures and limitations;
- checkpoints, resumes, exports and archives work.

### 5.3 Technician or specialist

A specialist receives scoped Facility and Domain Pack access. Restricted Device or recovery actions require separate approved adapters, case authority, consent, backups, immutable evidence and read-back verification.

### 5.4 Developer and contributor

A developer:

- implements approved roadmap work;
- consumes frozen contracts;
- adds tests and proof fixtures;
- maintains public/private and licence boundaries;
- cannot redefine canonical identities or lifecycle truth inside an adapter.

### 5.5 Hunter

Hunter is the primary internal planning and coordination participant for THETECHGUY use. Hunter:

- interprets owner or operator intent;
- requests records from Ptah and constructs Hunter-owned bounded context;
- selects relevant sources and applies Hunter or owner-defined trust labels;
- proposes plans and caller-defined Activities;
- selects suitable Providers within configured access;
- produces candidate Artifacts and handoffs;
- requests protected-action approval from the applicable human or application;
- proposes next actions and never assigns those decisions to Ptah.

### 5.6 Sergeant or independent reviewer

Sergeant or another reviewer:

- independently selects or requests the frozen candidate and review evidence;
- uses Ptah compute, storage and Facilities without becoming part of Ptah;
- challenges claims, unsafe shortcuts and incomplete proof;
- records Sergeant's review outcome without silently mutating Hunter’s result;
- issues no Ptah verdict: a human or calling application decides what to do with the review.

### 5.7 Replaceable software agent or model

Any compatible agent may participate through the same Workspace, Activity, Facility, Grant and Artifact contracts. A model change must not change permissions, accepted decisions, canonical source authority or handoff state.

### 5.8 External API or automation client

An API, CLI, SDK, scheduled job or external system may create and observe authorized Workspaces and Activities through stable contracts. It receives only the scope and Artifacts explicitly granted to it.

## 6. Product scope

### 6.1 Core world services

Ptah Core owns:

- canonical identifiers and versioned entity envelopes;
- Workspace, Session, Activity, Operation, Attempt and Event records;
- Node, Facility, Provider, Generation, capability and health records;
- Object, Content, Revision, View, Artifact, Relationship and Location records;
- caller-configured Policy, Grant, Lease and Fence records with mechanical enforcement;
- caller-defined Recipe, Plan, Run and Step records plus Receipt and Evidence storage;
- migrations, retention, supersession, tombstones and recovery projections;
- neutral APIs and event envelopes.

### 6.2 First-class Facilities

Ptah plans stable Facility contracts for:

- Terminal and Process;
- Transfer and Synchronization;
- Git and Source;
- Build and Test;
- Container and Environment;
- Browser and Web;
- Decomposition and Object Inspection;
- Media and Document;
- Firmware, Disk and Filesystem;
- Application and Display;
- Device and Protocol;
- Storage and Backup;
- Knowledge, Data and Search;
- Package and Plugin;
- Provenance, Signing and Security Evidence.

Each Facility may have multiple replaceable Providers with explicit versions, generations, limitations and health.

### 6.3 Domain Packs

Domain Packs implement versioned detect, inventory, decompose, preview, open or mount, transform, validate, compare, rebuild and execute capabilities where lawful and supported.

Planned domains:

- archives and compression;
- documents;
- images, audio and video;
- executables and libraries;
- applications and mobile packages;
- source repositories;
- databases and structured data;
- web content;
- firmware families;
- disks and filesystems;
- unknown binary research.

### 6.4 Human Workspace experience

The human shell must provide:

- Ptah home and current-state overview;
- Project/Workspace selector;
- Session and handoff selector;
- Object explorer and file browser;
- multi-terminal workspace;
- editor integration;
- Browser panels;
- Activity Centre;
- transfers and queues;
- process, container and environment views;
- document, media and firmware viewers;
- Application and Device sessions;
- Artifact, Evidence and provenance views;
- storage and backup controls;
- checkpoint, recovery, export and archive controls;
- Node, Provider and health status;
- approvals and security boundaries;
- accessible desktop, tablet and mobile projections where practical.

The shell may reuse mature editor, terminal, docking and panel frameworks. UI state is a projection and never becomes runtime truth.

### 6.5 AI Project Workspace substrate and application experience

The `ptah.workspace.ai_project.v1` profile composes neutral Ptah capabilities for applications:

- durable Workspace and Session identities;
- caller-owned instruction, purpose, objective and label Artifacts;
- parallel Sessions or work threads;
- reusable Artifact Library views;
- exact caller-requested record retrieval;
- model-independent stored state and caller-produced handoffs;
- caller-submitted scheduled Activities with configured mechanical access;
- failure, provenance, checkpoint and recovery retention.

Hunter, Sergeant, humans or other applications perform context selection, source ranking, review, approval, candidate promotion and next-action choice. Ptah stores and executes the requested operations but does not make those decisions.

This is a composition of frozen Ptah primitives, not a new ChatGPT-specific Core entity.

## 7. Explicit non-goals

Ptah Core does not own:

- company strategy or business judgment;
- assistant personality or identity;
- private Hunter prompts, memory or model data;
- autonomous release approval;
- universal policy decisions for every user;
- hidden provider memory;
- implicit global tool access;
- private customer, Device, payment or employee records in the public repository;
- proprietary repair protocols or restricted bypass workflows;
- vendor backend identity as canonical truth;
- an operating-system distribution as its public identity;
- every possible format or protocol in v1.

## 8. Operating modes

### 8.1 Online managed mode

The first product operates online with a control service and one or more execution Nodes. Users connect through the web shell, API, CLI or approved agents. Online operation must remain useful when an optional Facility is unavailable.

### 8.2 Single local Node mode

A local Linux Node may host the same Core services and Providers. The identity, data model and APIs remain compatible with online mode.

### 8.3 Hybrid mode

A Workspace may use online control and storage while executing selected Activities on local Nodes. Artifacts, Objects, Events and Receipts synchronize through explicit contracts.

### 8.4 Offline/local-first mode

A local deployment may continue with cached contracts, local metadata, local Artifacts and queued synchronization. Offline work must not manufacture online acceptance or authority.

### 8.5 Distributed mode

Several Nodes contribute different capabilities. Placement, Reservation, Lease, Generation and Fence records preserve authority and recovery. Shared POSIX storage is not required unless measured evidence proves it necessary.

### 8.6 Private OS integration mode

A later private operating-environment lane packages proven Ptah services, system units, Device rules, hardware profiles, local models, virtualization and update/rollback machinery. It may not redefine Ptah’s public identity or contracts.

## 9. Canonical world model

### Workspace

A persistent namespace for Objects, repositories, terminals, browsers, processes, environments, Applications, Devices, Activities, Artifacts, Policies, Grants, checkpoints and Sessions.

### Session

A recoverable human or software interaction projection over a Workspace. Session attachment, client layout and temporary context do not replace Workspace identity.

### Activity

Independently addressable durable work. Activities may be queued, preparing, running, waiting, paused, resuming, completed, failed, cancelled, detached or recovering.

### Operation

A logical requested effect within an Activity.

### Attempt

One physical try to perform an Operation. Retry creates a new Attempt.

### Object and Content

Content represents exact bytes. Object represents the logical item and role. Identical bytes may support distinct Objects without collapsing their identity.

### Revision and View

A Revision is an immutable version of an Object. A View is a derived representation, inspection result or projection with explicit source and limitations.

### Artifact

A promoted durable result such as a binary, document, image, report, patch, proof bundle, model, firmware derivative, SBOM or attestation.

### Node

A physical or virtual machine contributing capabilities and reporting exact identity, Generation, operating system, architecture, resources, storage, toolchains, Devices, health and load.

### Facility and Provider

A Facility is a stable contract. A Provider is one concrete implementation with revision, instance, Generation, capability, limitations, health and replacement metadata.

### Grant, Lease and Fence

A Grant defines authority. A Lease defines time-bound ownership or use. A Fence prevents stale actors or Generations from continuing protected work.

### Receipt and Evidence

A Receipt is immutable producer evidence. Evidence may support a bounded Claim but does not automatically equal review, acceptance or authoritative truth.

## 10. Data, storage and memory architecture

### 10.1 Hot Workspace storage

Used for active work:

- Git mirrors and worktrees;
- transfer partials;
- package and build caches;
- container layers;
- browser profiles;
- media intermediates;
- filesystem mounts;
- VM and emulator images;
- local metadata databases.

### 10.2 Durable object storage

Used for:

- uploaded originals;
- immutable Artifacts;
- proof and evidence bundles;
- session archives;
- large logs and recordings;
- firmware and media packages;
- backups and exports.

### 10.3 Metadata ledger

The first Node may use SQLite WAL behind `ptah-ledger`. Shared services may later use a reviewed SQL backend. SQL row IDs never escape as canonical identity.

### 10.4 Git

Git is source truth for code, schemas, versioned configuration, ADRs and reviewable project documentation.

### 10.5 Google Drive and readable recovery

Drive may hold readable exports, recovery copies and large documents. It is not the live build, Git, database, container or browser filesystem.

### 10.6 Workspace knowledge and caller-owned memory

Ptah stores inspectable Objects, Artifacts, Knowledge Sources, Index Revisions and caller-produced decision or handoff records. Hidden provider memory cannot replace durable caller-owned records.

Applications may attach labels such as `canonical`, `accepted_evidence`, `recovery_copy`, `reference`, `generated_candidate`, `temporary_context`, `rejected` or `superseded`. Ptah preserves the label, author, revision and provenance but does not interpret, rank or enforce the label's meaning.

## 11. Application-owned context and agent handoff

Before an agent participates, Hunter, Sergeant, a human-facing application or another caller may request exact Workspace records and construct its own bounded packet.

The caller decides whether to include:

- purpose or objective records;
- participant-role metadata;
- caller-accepted decisions;
- Activities and caller-identified blockers;
- selected Objects and Artifacts;
- selected Sessions;
- Facility and Grant records;
- evidence or privacy instructions;
- a previous caller-produced handoff or proposed next action.

Ptah returns records the caller is mechanically permitted to read and preserves exact source revisions and provenance. Ptah does not select context, rank authority, infer blockers, approve work or choose a next action.

A human, Hunter, Sergeant or another application may create a durable handoff containing:

- completed work;
- exact source and evidence commits;
- current state;
- blockers;
- active branch or Activity;
- proposed next action;
- unresolved questions;
- limitations and failed attempts.

Ptah stores and versions the handoff Artifact. It does not verify its conclusions or decide that it is authoritative.

## 12. Provider and adapter architecture

Core crates depend on stable contracts and provider APIs. Concrete adapters depend inward on those contracts. Core may not import concrete adapter implementations.

First selected adapters:

- native Linux process and PTY;
- Git CLI;
- containerd/runc OCI execution;
- Playwright/Chromium Browser;
- libarchive decomposition;
- repository-owned transfer and local CAS.

Every adapter must expose:

- exact version and source identity;
- Provider revision, instance and Generation;
- capabilities and limitations;
- health and readiness;
- sanitized command/API evidence;
- replacement and exit path;
- positive, negative and recovery fixtures.

## 13. Security, privacy and authority

### 13.1 General rule

Least privilege and explicit authority apply to humans, agents, scheduled Activities and Providers.

### 13.2 Secrets

Secrets are referenced through secure Grant or secret-reference records. Raw credentials may not appear in Workspace manifests, public fixtures, logs, model context or public source.

### 13.3 Protected and destructive actions

Protected actions require explicit role and Policy authority. Destructive Device or recovery actions additionally require:

- lawful case and consent;
- exact target identity;
- immutable pre-action backup where possible;
- approved protocol and adapter;
- lease/fence and Provider Generation;
- command/operation evidence;
- independent read-back verification;
- retained failure and limitation records.

### 13.4 Privacy

Audience, privacy class, retention and redaction are explicit on records and Artifacts. Public Ptah fixtures contain no customer, Device, payment or employee data.

### 13.5 Supply chain

Dependencies, actions, images, binaries and tools are pinned and inventoried. SBOM, provenance, signatures and independent verification are progressively required by release gate.

## 14. Reliability and recovery requirements

- Node identity survives restart; Generation changes.
- Workspace identity survives client and runtime restart where recovery is supported.
- client disconnect does not silently terminate durable work;
- retries create new Attempts;
- stale Provider Generations, Sessions, Leases and fences are rejected;
- partial transfers and outputs remain retained and labelled;
- checkpoint integrity, compatibility, restore and Recovery Verification remain distinct;
- optional Facility failure does not collapse unrelated Activities;
- events and logs may be incomplete without manufacturing success;
- every accepted recovery is tied to exact evidence.

## 15. Observability and evidence

From the first runtime slice, Ptah records:

- structured Events;
- Activity, Operation and Attempt correlation;
- logs, metrics and traces;
- timing and resource use;
- Node and Provider Generation;
- exact commands, inputs and output digests where permitted;
- limitations, truncation and privacy filtering;
- immutable Receipts and retained Artifacts;
- exact implementation commit and dependency lock.

Observability is not the Activity Ledger and cannot independently declare truth.

## 16. APIs, SDKs and integration surfaces

Planned stable surfaces:

- REST or equivalent control API;
- event stream;
- CLI;
- Rust SDK or internal library;
- generated contract bindings;
- later TypeScript/Python SDKs where justified;
- Facility Provider interface;
- Plugin and Domain Pack contracts;
- Workspace profile and handoff formats;
- MCP and other external protocols only as adapters, never as the sole internal architecture.

All public surfaces are versioned and migration-aware.

## 17. Operations and service ownership

### 17.1 Control services

Responsible for canonical metadata, authorization, Workspace/Activity coordination, API, event routing and recovery state.

### 17.2 Node agent

Responsible for truthful host capability, local Provider lifecycle, Activity execution, local storage, evidence generation and reconnect.

### 17.3 Storage services

Responsible for durable Object/Artifact bytes, integrity, retention and export. Storage success does not equal application recovery.

### 17.4 Operator responsibilities

Operators monitor:

- Node and Provider health;
- storage pressure;
- Activity queues and failures;
- transfer partials;
- backup and checkpoint verification;
- security findings;
- dependency and image updates;
- evidence retention;
- release and rollback state.

### 17.5 Upgrade and rollback

- contracts and persisted records are versioned;
- migrations are directional and immutable after release;
- rollback restores a compatible checkpoint or uses reviewed compensating migration;
- Provider updates create new revisions and Generations;
- dependency/security updates rerun the affected proof suites;
- no upgrade erases failed or uncertain external effects.

## 18. Product surfaces and release boundaries

### Milestone 0 — Plan, contracts and authorization

Complete master plan, detailed implementation roadmap, frozen WP01–WP14 contracts, Phase 0C selections, physical-host evidence, ADR-0033 acceptance and explicit authorization.

### Milestone 1 — Online Ptah Alpha

One Linux Node proves persistent Workspace, concurrent Activities, terminals, upload/resumable download, Git, OCI container, Browser, archive decomposition, Object/Artifact registration and verified checkpoint/reconnect.

### Milestone 2 — Object World Beta

Progressive decomposition, documents, media, executables, applications, searchable object graph, durable Sessions and broader transfer/storage are proven.

### Milestone 3 — Firmware and Device Beta

Disk/filesystem and major firmware families, read-first Device evidence, Android Device sessions, emulators and approved specialist adapters are proven.

### Milestone 4 — Full Workspace Release

Human shell, AI Project Workspace composition, mature Facilities, Knowledge/Data/Search, Recipes, Plugins, provenance, security evidence and long-running recovery are complete.

### Milestone 5 — Distributed Ptah

Mini PC, workstation, Windows/macOS/GPU/Device Nodes, hybrid execution, intermittent connectivity, compatible Workspace movement and local-first operation are proven.

### Milestone 6 — OS-ready foundation

Proven Ptah services can be packaged into a larger private local operating environment with updates, rollback, encryption, virtualization and hardware integration without changing Ptah identity.

## 19. Success measures

Ptah is succeeding when:

- a user can resume meaningful work without reconstructing context;
- ten or more independent Activities run without global blocking in the first slice;
- large interrupted transfers resume and verify exact destination bytes;
- failures remain visible and scoped;
- a Workspace survives client and runtime interruption with verified recovery;
- Artifacts trace to exact source, environment, tool versions and producing Activities;
- Provider replacement preserves canonical identity;
- humans can operate the complete slice without an AI;
- Hunter or another model can resume from the same handoff without gaining new authority;
- public source remains free of private THETECHGUY data and restricted knowledge;
- every release gate is supported by retained exact-head evidence.

## 20. Definition of product completion

Ptah is complete only when users and compatible systems can reliably:

- work online and locally through compatible contracts;
- run many Activities concurrently;
- receive and move large files reliably;
- inspect and navigate structured Objects and derivatives;
- clone, build, test, render and reproduce projects;
- browse the live web and operate Applications;
- inspect firmware, disks, filesystems and Devices through lawful adapters;
- save, restore and move compatible Workspaces and Sessions;
- inspect authority, privacy, provenance and failure state;
- verify how every accepted Artifact was produced;
- use multiple Nodes while preserving identity and recoverability;
- continue useful work when optional Facilities are unavailable;
- extend the system through stable Facility, Provider, Plugin and Domain Pack boundaries;
- switch agents or model providers without losing project truth or silently changing permissions.

Completion is evidence-backed and release-specific. Ptah may reach useful public releases before every optional Domain Pack or platform adapter exists.

## 21. Parked and future scope

The following remain parked until their reopening criteria are met:

- `.P5C` parsing;
- distributed shared POSIX storage;
- MiniRouter source reuse;
- Dify source integration;
- compositor-specific non-GNOME Wayland completion;
- private unaudited Device modules;
- optional full VM and specialized hardware Providers not needed by the current milestone.

A parked item does not block v1 unless an accepted roadmap decision promotes it.

## 22. Planning and implementation governance

Before work begins, the item must be:

- present in this Master Plan;
- placed and dependency-ordered in `IMPLEMENTATION_ROADMAP.md`;
- mapped to frozen contracts and proof requirements;
- selected in `CURRENT_STATE.md`;
- unticked or active in `PROGRESS.md`;
- approved by the owner;
- assigned a public/private boundary.

Every work item follows:

```text
Understand
→ Build
→ Review
→ Freeze
→ Prove
→ Submit/Ship
```

A roadmap change records the problem, evidence, affected phases, dependency changes, reused and superseded work, public/private impact and status.

## 23. Current closure state

Recovered requirements and decisions: accepted through Phase 0C-16.

Master Plan: accepted as version `1.0.0` through ADR-0034 and merge `2c24f9e6b0fc98d5e03605596db75d7495796353`.

Detailed implementation roadmap: accepted as version `1.0.0`; Programme P01 is the active pre-runtime gate.

WP01–WP14 contracts: frozen.

Phase 0C selections, licence and proof tooling: complete except the physical-host evidence result and final closure.

Physical pinned-host evidence: open.

ADR-0033: proposed.

Runtime implementation: **NOT AUTHORIZED**.
