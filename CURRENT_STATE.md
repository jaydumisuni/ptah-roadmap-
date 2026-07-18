# Ptah Current State

**Last updated:** 2026-07-18  
**Overall status:** ACTIVE PLANNING — ARCHITECTURE SUBSYSTEMS CLOSED FOR DESIGN  
**Current phase:** Phase 0A — donor cleanup and cross-requirement review  
**Active inspection unit:** Research/documentation sources and unresolved-profile cleanup  
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

One repository never closes a subsystem. Research, corrections and decisions are committed after every meaningful inspection unit.

Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

Design closure does not authorize implementation.

---

# Phase 0A architecture subsystems closed for Phase 0B contract design

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
- Linux AT-SPI/libatspi semantic tree, query, action, text, selection, value, cache and Event composition;
- X11 versus GNOME-Wayland input paths and explicit visual fallback;
- Semantic Provider/Snapshot/Target/Selector/Action identities and post-condition proof.

Linux semantic rules:

1. AT-SPI/libatspi is the primary Linux semantic Provider foundation.
2. D-Bus names, object paths, AccessibleIds and child indices remain provider-local observations.
3. targets are reacquired against current Application, Window and provider generations.
4. events update/invalidate state but do not replace fresh snapshots/reconciliation.
5. semantic inspection, semantic mutation, raw input, clipboard and visual automation are separate permissions.
6. GNOME Ponytail is one GNOME-Wayland input adapter, not universal Wayland support.
7. command/action protocol success requires semantic and/or visual read-back.
8. opaque applications degrade explicitly to partial or visual-only behavior.
9. mutually untrusted Workspaces do not share one privileged accessibility session.

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
- ClawHub/OpenClaw registry/lifecycle patterns;
- Dify licence restriction and Hermes/OpenClaw/Hunter external-caller boundary;
- MiniRouter as a future study-only routing/evaluation workload pending licence.

Evidence:

- `work-packages/PHASE-0A-WP10-KNOWLEDGE-DATA-SEARCH-PLUGIN.md`
- ADR-0013 and listed donor/internal records.

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

Evidence:

- `work-packages/PHASE-0A-WP11-ISOLATION-DISTRIBUTED-PLACEMENT.md`
- ADR-0014 and listed donor/internal records.

## Security Assessment and Reproduction Workloads

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

Inspected and saved:

- ReproZip;
- ClaimBound;
- SparkDistill;
- Syft and Grype;
- GUAC;
- Semgrep;
- Trivy;
- ZAP;
- Strix.

Accepted direction:

1. exact Security Assessment Authorization, Plan, Target Revision, machinery revision and Coverage are mandatory.
2. static, inventory, vulnerability, configuration, secret, licence, passive, active, exploit and agent-originated observations remain distinct.
3. raw scanner/workload reports remain immutable restricted Artifacts.
4. Finding Observation and Correlated Finding remain separate; scanner disagreement is retained.
5. severity, confidence, exploitability, impact, disposition, remediation priority, release policy and acceptance remain separate.
6. false-positive, not-affected, accepted-risk and suppression records require authority, reason, scope and optional expiry.
7. active/fuzz/exploit/agentic work requires exact authorization, strong isolation, network/credential budgets, emergency stop and cleanup/read-back.
8. scanner/agent fixes remain proposals until correct owner implementation, re-test and independent review.
9. frozen Protocol Revision, Reproduction Run and bounded claim/Evidence Card remain separate from Result and acceptance.
10. ReproZip is one environment-capture/replay class, not universal reproduction.
11. ClaimBound cards are Views, not certification or Activity truth.
12. SparkDistill is an optional specialist AI-reproduction workload; recipe, dataset, checkpoint, metric claim, attestation and recheck remain separate.
13. negative, blocked, drift, inconclusive and not-independently-reproduced outcomes remain visible.
14. no-findings, exit code zero, clean scan, PoC, hash, attestation or replay never becomes broad proof of security or correctness.

Closed requirements:

- `SEC-001`;
- `REPRO-001`.

Evidence:

- `work-packages/PHASE-0A-SECURITY-REPRODUCTION-WORKLOADS.md`
- `decisions/ADR-0016-SECURITY-FINDING-VALIDATION-REPRODUCTION-BOUNDARY.md`
- canonical donor records in `donors/`.

No scanner, security agent, test target, security gate, evidence-card renderer or reproduction runtime is approved for implementation yet.

---

# Active inspection unit

## Research/documentation sources and unresolved-profile cleanup

This is a cleanup/classification unit, not a new architecture cluster.

Resolve or explicitly classify:

1. Awesome AI Product Management catalogue;
2. `tmimmanuel` profile as discovery lineage only after individual repositories are already assessed;
3. Chris Ipanaque's correct GitHub identity/repositories;
4. `amertoglu16.github.io` repository/site and actual functionality;
5. GitHub README Crisp Links or equivalent documentation tooling;
6. MkDocs Material, Docusaurus and Mermaid documentation/presentation roles;
7. any remaining donor-list names, redirects, stale URLs, duplicate records or licence gaps;
8. remaining public/private donor-register inconsistencies.

Expected outcomes:

- documentation/research source;
- discovery source only;
- public presentation tool;
- already covered;
- parked with reopening criteria;
- rejected/no implementation evidence;
- donor record corrected and pinned.

Do not reopen accepted runtime architecture merely because a catalogue or profile mentions another tool.

After cleanup:

1. cross-requirement consistency review;
2. parked/rejected/blocked gap review;
3. Phase 0A freeze/readiness decision for Phase 0B.

---

# Accepted decisions

ADR-0001 through ADR-0016 are accepted and indexed in `DECISIONS.md`.

---

# No-build boundary

Allowed now:

- donor/internal recovery;
- source inspection, canonical pins and licence review;
- classification/cleanup and duplicate removal;
- cross-requirement review;
- ADR, schema and proof planning after Phase 0A review.

Not allowed yet:

- copying donor code;
- beginning runtime or large UI implementation;
- choosing first-slice dependencies before Phase 0C;
- declaring implementation readiness from design closure;
- replacing internal work without evidence;
- exposing private consumers publicly.

---

# Phase 0A completion gate

Every v1 requirement now has composite design closure. Phase 0A still cannot freeze until:

1. remaining research/documentation/profile entries are resolved or parked;
2. stale URLs, duplicate donor files and licence gaps are identified;
3. all ADR/work-package/matrix/current-state references agree;
4. cross-requirement schemas and identities are checked for contradictions;
5. parked/blocked gaps have explicit reopening criteria;
6. Phase 0B inputs and proof corpus are enumerated;
7. the no-build boundary remains explicit.

---

# Chat continuation instruction

Read this file first, followed by `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, `DONOR_RECOVERY.md`, `REQUIREMENT_CLOSURE_MATRIX.md`, relevant donor/internal records, work packages and ADRs before proposing or performing further work.
