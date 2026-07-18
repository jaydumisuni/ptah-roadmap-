# Ptah Current State

**Last updated:** 2026-07-18  
**Overall status:** ACTIVE PLANNING — ALL V1 SUBSYSTEMS CLOSED FOR DESIGN  
**Current phase:** Phase 0A — cross-requirement review and freeze readiness  
**Active inspection unit:** Identity, authority, proof and parked-gap consistency review  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Devices, Applications, Browsers, Sessions, Panels, Knowledge Sources, Datasets, Plugins, security Findings and Artifacts.

Ptah supplies the working world. Humans and compatible systems supply intent, reasoning, policy, restrictions, risk acceptance and acceptance criteria.

The complete roadmap is stored in `MASTER_ROADMAP.md`.

---

# Mandatory closure method

Every requirement combines:

1. internal THETECHGUY foundation and intentional constraints;
2. primary capability donor;
3. completion donors;
4. mature upstream machinery and standards;
5. native Ptah contracts and integration;
6. fallback or exit path;
7. proof of the complete assembled subsystem.

One repository never closes a subsystem. Research, corrections and decisions are committed after every meaningful inspection/review unit.

Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

Design closure does not authorize implementation.

---

# Phase 0A architecture closed for Phase 0B contract design

## WP01–WP02 — Core runtime

Closed:

- Node Protocol versus Workspace Provider;
- persistent Workspaces and concurrent Activities;
- Facility manifests and polyglot adapters;
- terminal/process and OCI-provider foundations;
- durable orchestration, live Events and observability;
- local journal/reconnect;
- operation/attempt/nonce/Receipt/proof boundaries.

Evidence: ADR-0001 through ADR-0004 and WP01/WP02 records.

## WP03 — Build, Artifact and provenance

Closed:

- Build Recipe and backend compilation;
- BuildKit and Dagger roles;
- Artifact relationships and ORAS transport;
- SBOM, attestation, signature, trust, review and independent-reproduction levels.

Evidence: ADR-0005 and WP03.

## WP04 — Storage, transfer, synchronization and backup

Closed:

- hot local Workspace storage;
- local CAS plus local/shared SQL and R2/S3 direction;
- immutable Objects and mutable revisions/conflicts;
- resumable transfer, sync, backup/restore and Drive recovery;
- distributed shared filesystems parked pending measured need.

Evidence: ADR-0006 and WP04.

## WP05 — Universal Object and decomposition

Closed:

- immutable Object graph and plural detector claims;
- progressive bounded decomposition;
- child, View, preview, transform, decompilation and rebuild relationships;
- document, archive, image, media, binary, Android application and source-structure Domain Packs.

Evidence: ADR-0007 and WP05.

## WP06 — Firmware, disks and filesystems

Closed:

- Apple, MediaTek, Qualcomm, Unisoc, Android OTA and Samsung/vendor composition;
- GPT/MBR and isolated filesystem inspection;
- static analysis versus physical mutation;
- exact compatibility, immutable backup and read-back proof.

`.P5C` remains parked until a lawful verified sample, specification or parser exists.

Evidence: ADR-0008 and WP06.

## WP07 — Device and Application Runtime

Closed:

- stable Device identity, interface epochs, Provider workers and lease/fencing;
- Android device control, display/input and semantic UI;
- Linux, Windows, macOS and iOS Application Providers/Sessions;
- remote display, Window, checkpoint and platform proof boundaries;
- Linux AT-SPI/libatspi semantic tree, target, selector, action, cache and Event composition;
- X11 versus GNOME-Wayland input paths and explicit visual fallback;
- post-condition semantic/visual read-back and sensitive-access boundaries.

Evidence:

- `donors/AT-SPI.md`
- `work-packages/PHASE-0A-LINUX-AT-SPI-SEMANTIC-COMPLETION.md`
- ADR-0009, ADR-0010 and ADR-0015.

## WP08 — Browser and Live Research

Closed:

- Browser Provider, Binary, Profile, Process, Context, Page, Frame, Popup and Download identities;
- Playwright foundation and Browser-Use/TurboWebFetch completion patterns;
- source, DOM, accessibility, screenshot, video, trace, console and network evidence;
- source/citation records and explicit authentication/challenge/human-completion states.

Evidence: ADR-0011 and WP08.

## WP09 — Human Workspace Shell and Operator Interface

Closed:

- Shell Client/Session, Panel Type/Instance, Layout Profile/Revision and control ownership;
- Theia full workbench, Dockview responsive layouts, xterm.js terminal rendering and optional coding Applications;
- Activity Centre, Evidence Explorer and exact lifecycle/proof labels;
- desktop/tablet/phone projections, accessibility and human/automation fenced control.

Evidence: ADR-0012 and WP09.

## WP10 — Knowledge, Data, Search and Plugin Composition

Closed:

- Conversation, Knowledge Source, Source Object/View, Corpus, Document Revision, Chunk, Index Revision and caller-owned memory separation;
- source-grounded Query, Result, ranking explanation and exact Citation;
- ingestion, freshness, deletion, tombstone, reconciliation and permission boundaries;
- LlamaIndex modular local direction and optional RAGFlow Facility;
- Dataset/Table/Schema/Query/Transformation/Result identities behind Polars and DuckDB;
- Package, Package Release, Installed Plugin, Activation and Registry Entry lifecycle;
- Deno lightweight runtime and stronger-isolation escalation;
- MCP as an external adapter, not the internal model;
- Dify licence restriction and external-caller boundaries;
- MiniRouter as a future study-only routing/evaluation workload pending licence.

Evidence: WP10, ADR-0013 and listed donor/internal records.

## WP11 — Strong Isolation and Distributed Placement/Scheduling

Closed:

- Isolation Class separate from runtime implementation;
- baseline OCI, gVisor, Kata, Firecracker and full-VM classes;
- runc, crun and youki as replaceable baseline OCI implementations;
- no silent weakening of isolation;
- Node Capability/Resource Snapshots;
- Placement Request, Candidate/Decision, Reservation, Lease, Generation and Fence;
- secure network, Object mount, Device and credential grants;
- interruption, rescheduling, checkpoint, restore and application read-back;
- one-Node and multi-Node operation under the same identities;
- Ray as an optional trusted distributed Compute Facility, not the global scheduler or security boundary.

Evidence: WP11, ADR-0014 and listed donor/internal records.

## Security Assessment and Reproduction Workloads

Closed:

- exact Security Assessment Authorization, Plan, Target Revision, machinery revision and Coverage;
- separate static, inventory, vulnerability, configuration, secret, licence, passive, active, exploit and agent-originated observations;
- immutable restricted scanner/workload reports;
- Finding Observation versus Correlated Finding;
- severity, confidence, exploitability, impact, disposition, remediation priority, release policy and acceptance separation;
- scoped exception, not-affected, false-positive and accepted-risk records;
- active/offensive isolation, network, credential, stop and cleanup boundaries;
- frozen Protocol Revision, Reproduction Run and bounded Evidence Card;
- remediation proposal, owner implementation, re-test and independent review;
- negative, blocked, drift, inconclusive and not-independently-reproduced evidence.

Closed requirements:

- `SEC-001`;
- `REPRO-001`.

Evidence:

- `work-packages/PHASE-0A-SECURITY-REPRODUCTION-WORKLOADS.md`
- `decisions/ADR-0016-SECURITY-FINDING-VALIDATION-REPRODUCTION-BOUNDARY.md`
- canonical donor records in `donors/`.

## Research, documentation and source cleanup

Closed:

- Awesome AI Product Management verified as optional Research Source only;
- `tmimmanuel` retained as discovery lineage only;
- Chris/Christiam Ipanaque identity resolved to `chrisipanaque` and prototype reuse parked pending licence/proof;
- `amertoglu16.github.io` parked after no source or functionality was recovered;
- Crisp Links verified as optional README asset generator;
- Material for MkDocs pinned as primary lightweight docs candidate;
- Docusaurus pinned as optional richer docs/site alternative;
- Mermaid pinned as primary text-defined documentation-diagram candidate;
- catalogue/profile/README claims prevented from becoming donor proof;
- public/private documentation build and leakage boundary recorded.

Evidence:

- `donors/RESEARCH-DISCOVERY-SOURCES.md`
- `donors/DOCUMENTATION-PRESENTATION-TOOLS.md`
- `work-packages/PHASE-0A-RESEARCH-DOCUMENTATION-SOURCE-CLEANUP.md`

No research catalogue, profile, documentation framework or presentation tool changes accepted runtime architecture.

---

# Active inspection unit

## Cross-requirement consistency and freeze-readiness review

This is the final Phase 0A review lane. It must not invent a new architecture cluster.

### 1. Identity consistency

Check that every accepted record uses compatible and non-overlapping meanings for:

- Node, Workspace, Activity, operation, attempt and Event;
- Object, View, Artifact, revision, location and derivative;
- Facility, Provider, Package, Plugin and Activation;
- Device, Application, Browser, Window, Page, Session and generation;
- Claim, Finding Observation, Correlated Finding, Evidence and Receipt;
- Recipe, Build, Scan, Protocol, Reproduction Run and Comparison;
- Placement, Reservation, Lease, Fence and Checkpoint.

No donor-local identifier may be silently promoted to canonical Ptah identity.

### 2. Authority consistency

Verify separation of:

- caller intent and Ptah execution;
- policy decision and operation result;
- user/department/organization approval and provider capability;
- human-control lease and automation authority;
- security authorization, scanner output and release acceptance;
- Code Ops/specialist ownership, Sergeant proof and caller acceptance;
- credentials/session ownership and plugin/tool permissions.

### 3. State and proof consistency

Verify that all work packages preserve:

- Activity state versus Event/telemetry;
- protocol acknowledgement versus read-back;
- Evidence versus Claim;
- signature/attestation versus semantic correctness;
- checkpoint produced versus restored versus application recovered;
- no-findings versus bounded scan coverage;
- bundle assembled versus workload reproduced;
- UI projection versus runtime truth;
- review versus external authoritative result.

### 4. Lifecycle consistency

Check create/start/pause/retry/recover/stop/archive/delete behavior across:

- Workspaces and Activities;
- Objects and revisions;
- Builds and Artifacts;
- transfers, sync and backups;
- Devices, Applications, Browsers and Shell Sessions;
- Knowledge indexes and Plugins;
- reservations, leases and distributed work;
- Findings, exceptions and reproduction records.

### 5. Parked/rejected/blocked gap audit

At minimum review:

- `.P5C` format/sample gap;
- distributed shared POSIX filesystems;
- MiniRouter source licence;
- Dify modified-licence boundary;
- `chrisipanaque` prototype source reuse;
- `amertoglu16.github.io` missing source;
- GNOME Ponytail exact source/dependency approval;
- unsupported Wayland compositors/toolkits;
- private internal device-manager source not yet auditable;
- any donor root without a clear licence;
- any stale, redirected or duplicate donor path.

Every parked/blocked item must have reopening criteria and a non-blocking v1 path or be declared a true blocker.

### 6. Phase 0B input enumeration

Produce one explicit checklist of required:

- schemas and migrations;
- conformance suites;
- golden Objects/Artifacts/reports;
- failure and negative-proof corpus;
- security/privacy fixtures;
- versioning and compatibility matrices;
- observability conventions;
- backend replacement tests;
- first-slice decision inputs.

### 7. Freeze decision

Phase 0A may freeze only when:

1. ADR, work-package, donor, matrix, progress and Current State references agree;
2. no identity or authority contradiction remains unresolved;
3. every parked gap has reopening criteria and a v1 consequence;
4. all Phase 0B schema/proof inputs are enumerated;
5. implementation remains blocked until Phase 0C approval.

---

# Accepted decisions

ADR-0001 through ADR-0016 are accepted and indexed in `DECISIONS.md`.

---

# No-build boundary

Allowed now:

- cross-requirement review;
- parked/rejected/blocked gap classification;
- source/reference corrections and duplicate removal;
- Phase 0B schema, migration and proof-corpus planning;
- freeze/readiness decision.

Not allowed yet:

- copying donor code;
- beginning runtime or large UI implementation;
- choosing first-slice dependencies before Phase 0C;
- declaring implementation readiness from design closure;
- replacing internal work without evidence;
- exposing private consumers publicly.

---

# Phase 0A completion gate

Every v1 requirement has composite design closure. Phase 0A still cannot freeze until:

1. cross-requirement identities, authority, states, proofs and lifecycles agree;
2. stale URLs, duplicates and licence gaps are classified;
3. parked/blocked gaps have explicit reopening criteria and v1 consequences;
4. all ADR/work-package/matrix/progress/current-state references agree;
5. Phase 0B schemas, conformance and proof corpus are enumerated;
6. the no-build boundary remains explicit.

---

# Chat continuation instruction

Read this file first, followed by `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, `DONOR_RECOVERY.md`, `REQUIREMENT_CLOSURE_MATRIX.md`, relevant donor/internal records, work packages and ADRs before proposing or performing further work.
