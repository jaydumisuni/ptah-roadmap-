# Ptah Space — Detailed Implementation Roadmap

Status: candidate delivery authority derived from `MASTER_PLAN.md` — runtime implementation remains unauthorized

Version: 1.0-candidate

Recorded: 2026-07-21

## 1. Purpose and authority

This roadmap converts the Ptah Master Plan into dependency-ordered, evidence-gated implementation work.

It does not authorize runtime work by itself. Runtime work begins only after:

1. this roadmap and the Master Plan are reviewed and accepted;
2. physical pinned-host evidence is produced, reviewed and durably retained;
3. the Phase 0C closure consistency review passes;
4. ADR-0033 is accepted;
5. `CURRENT_STATE.md` explicitly states `Runtime implementation: AUTHORIZED` in the same reviewed closure change.

## 2. Status vocabulary

- `PLANNED` — placed and defined but not authorized.
- `READY` — prerequisites and authorization are satisfied.
- `ACTIVE` — implementation is in progress at an exact branch/commit.
- `BLOCKED` — a named external or prerequisite condition is open.
- `IN REVIEW` — source and behavior are being reviewed.
- `FROZEN` — reviewed checkpoint is pinned.
- `PROVEN` — required positive, negative and recovery evidence passed at the frozen checkpoint.
- `COMPLETE` — proven and merged/released where required.
- `PARKED` — intentionally outside the active release path.

## 3. Universal work-package gate

Every implementation work package must record:

- exact requirement and Master Plan section;
- frozen WP01–WP14 contracts consumed;
- dependencies and upstream commits;
- public/private boundary;
- source and licence inventory;
- implementation repository, branch and exact commit;
- positive tests;
- negative/adversarial tests;
- disconnect, restart or recovery tests where applicable;
- exact Provider revision and Generation evidence;
- retained logs, Receipts, reports and Artifacts;
- limitations and unsupported cases;
- reviewer outcome;
- next dependency.

No package is complete because code exists.

## 4. Programme critical path

```text
P00 Master-plan closure
  → P01 Physical-host and ADR-0033 closure
  → A01 Contract/runtime scaffold
  → A02 Node identity and ledger
  → A03 Activity runtime
  → A04 PTY + Workspace
  → A05 Object store + transfer
  → A06 Git + OCI + Browser + archive decomposition
  → A07 checkpoint/recovery
  → A08 exact-head Online Alpha acceptance
  → B Object World
  → C Firmware and Device
  → D Full Workspace
  → E Distributed Ptah
  → F OS-ready foundation
```

Adapter work may proceed in parallel only after the identity, ledger, Activity and Provider substrates it consumes are proven.

# PROGRAMME 0 — Plan, evidence and implementation authorization

## P00 — Master-plan authority closure

Status: ACTIVE on planning branch.

Deliver:

- recovered requirement and decision ledger;
- complete `MASTER_PLAN.md`;
- this detailed implementation roadmap;
- WP01–WP14 and Phase 0C reconciliation matrix;
- machine-readable plan index;
- durable AI/chat handoff;
- repaired README, memory protocol, decision index, progress and current-state records;
- accepted plan-authority ADR.

Proof:

- every product scope area maps to a frozen contract, a planned work package or an explicit parked item;
- every roadmap package maps back to Master Plan scope;
- no runtime claim or authorization is introduced;
- recovery order lets a new chat identify the exact state and next action without conversation history.

Exit gate:

- reviewed and merged master-plan closure package.

## P01 — Physical-host and ADR-0033 closure

Status: BLOCKED on access to the exact physical host.

Deliver:

- proof-eligible report from Ubuntu Server 24.04.4 amd64 with kernel `6.8.0-136-generic`;
- exact host capability report;
- exact installed package/version/architecture inventory;
- exact local APT package-artifact and source-index digests;
- clean exact `Ptah-space` commit binding;
- independently verified durable bundle;
- explicit host, package, artifact and retention review acceptance;
- Phase 0C closure consistency review;
- ADR-0033 status changed from proposed to accepted;
- explicit runtime authorization in `CURRENT_STATE.md`.

Proof:

- all fail-closed proof-runner and retention checks pass;
- `proof_eligible: true`;
- host, capability, package, artifact, APT and repository failure sets are empty;
- retained bundle bytes and repository binding verify independently;
- no frozen WP01–WP14 contract is weakened;
- authorization occurs only in the reviewed closure merge.

Exit gate:

- `Runtime implementation: AUTHORIZED`.

# PROGRAMME A — Online Ptah Alpha: exact first vertical slice

Programme A is the smallest coherent world proving Ptah identity. Its ordered work is authoritative from the existing Phase 0C implementation/proof map.

## A01 — Repository, contracts and reproducible scaffold

Maps: P0C-I001; Master Plan sections 9, 12, 16, 22; WP01–WP14.

Deliver:

- accepted monorepo layout;
- Rust workspace and Node/browser package boundaries;
- exact toolchain and dependency locks;
- frozen contract import lock;
- reproducible generated bindings;
- migration and conformance harness wiring;
- licence, notice and source-policy enforcement;
- CI reports tied to exact commit.

Proof:

- clean generation is byte-identical twice;
- modified catalog digest fails;
- network-disabled schema generation passes;
- private and restricted paths are absent from public packaging;
- direct dependencies and immutable action pins are inventoried.

Dependencies: P01.

Exit: scaffold FROZEN and PROVEN; still no runtime behavior claimed until the relevant package exists.

## A02 — Node identity, Generation and host truth

Maps: P0C-I002; WP01, WP02, WP04, WP11.

Deliver:

- stable Node identity;
- Node revision and Generation records;
- boot and process evidence without identity leakage;
- host capability snapshot;
- Node health, readiness, reachability and pressure projections;
- Event and Receipt correlation.

Proof:

- Node identity survives agent restart;
- Generation changes after restart;
- stale-generation commands fail and remain evidenced;
- process ID, hostname and boot ID cannot replace Node identity;
- health and capability claims are evidence-bound.

Dependencies: A01.

## A03 — Ledger, schema versions and crash-safe migrations

Maps: P0C-I003; WP01–WP06.

Deliver:

- `ptah-ledger` interfaces;
- SQLite WAL implementation;
- entity/schema version registry;
- immutable numbered directional migrations;
- transactional write and checkpoint policy;
- repository-owned query boundaries.

Proof:

- restart preserves canonical records;
- interrupted transaction cannot manufacture success;
- migration replay is deterministic;
- incompatible migration fails closed;
- backend row IDs never escape as canonical identities.

Dependencies: A01, A02.

## A04 — Activity, Operation, Attempt, Event and Receipt runtime

Maps: P0C-I004; WP02, WP04, WP11, WP12.

Deliver:

- independent lifecycle engines;
- Activity registry and scheduling queue;
- Operation and Attempt creation;
- retry, cancellation and failure propagation;
- Event streaming;
- immutable Receipt generation;
- resource and timing evidence.

Proof:

- at least ten independent Activities run concurrently;
- one failure does not collapse unrelated Activities;
- cancellation remains scoped;
- retry creates a new Attempt;
- reused Attempt identity fails;
- acknowledgement-only completion fails;
- failed and cancelled work remains queryable.

Dependencies: A02, A03.

## A05 — Native process, PTY and multi-terminal Provider

Maps: P0C-I005; WP02, WP04, WP05, WP09, WP11.

Deliver:

- native process Provider;
- PTY-backed terminal Activities;
- independent stdout/stderr streams;
- input, resize, detach and reconnect;
- terminal attachment and control leases;
- Provider revision and Generation;
- truncation and stream limitation records.

Proof:

- several terminals remain independent;
- client disconnect does not terminate a durable terminal unless Policy requires it;
- stale terminal attachment and stale control lease are fenced;
- stream ordering and truncation limits remain visible;
- process exit is independently verified.

Dependencies: A04.

## A06 — Persistent Workspace, Session and authority projection

Maps: P0C-I006; WP05, WP09, WP11; AI Project Workspace profile.

Deliver:

- persistent Workspace identity;
- Workspace revisions and provider bindings;
- Session attach/detach;
- Workspace-scoped Objects, Activities, terminals and Policies;
- participant and Grant projection;
- restart recovery projection;
- basic handoff record.

Proof:

- Workspace identity survives disconnect and runtime restart;
- Session changes do not replace Workspace identity;
- missing attachments remain explicit;
- stale Session authority fails;
- cross-Workspace retrieval fails without Grant;
- agent replacement preserves authority and handoff state.

Dependencies: A03, A04, A05.

## A07 — Object, Revision, Artifact, Location and local CAS

Maps: P0C-I007; WP03, WP07, WP10.

Deliver:

- Content hashing;
- Object registration;
- immutable Revision records;
- Relationship and View foundations;
- digest-addressed local CAS;
- Artifact promotion;
- Location and provenance records;
- integrity verifier.

Proof:

- identical bytes may deduplicate without collapsing distinct logical Objects;
- changed bytes create distinct Content identity;
- moved storage preserves Artifact identity;
- digest mismatch blocks registration;
- a generated candidate cannot silently become canonical Artifact;
- producing Activity and exact Receipt remain linked.

Dependencies: A03, A04, A06.

## A08 — Upload and resumable download engine

Maps: P0C-I008; WP03, WP06, WP11.

Deliver:

- upload API and shell path;
- resumable download;
- retained partial state;
- streaming digest;
- destination read-back verification;
- transfer progress Events;
- queue, pause and resume foundations;
- safe destination materialization.

Proof:

- interrupted transfer resumes without restarting;
- corrupted partial data is detected;
- provider acknowledgement cannot claim completion;
- path traversal and destination escape fail;
- exact source and destination digests are retained;
- transfer Activity does not block terminals or unrelated work.

Dependencies: A04, A07.

## A09 — Hardened Git Provider

Maps: P0C-I009; WP02–WP07, WP11.

Deliver:

- clone or mirror as receipted Activity;
- exact remote and commit resolution;
- protocol allow-list;
- credential-reference boundary;
- hook suppression;
- explicit submodule and LFS policy;
- repository Object/Revision projection;
- failed clone evidence.

Proof:

- exact remote and resolved commit are retained;
- disallowed protocols fail closed;
- untrusted hooks do not execute;
- submodule policy cannot be bypassed silently;
- worktree paths remain Locations/Aliases;
- failed and partial clones remain evidenced.

Dependencies: A04, A06, A07, A08.

## A10 — OCI container Provider

Maps: P0C-I010; WP02, WP04, WP07, WP11.

Deliver:

- pinned containerd/runc integration;
- exact image digest binding;
- isolated execution and resource limits;
- Provider capability and Generation;
- process/output/exit evidence;
- backend replacement projection;
- explicit network and mount Policy.

Proof:

- backend IDs remain Aliases;
- mutable tag without digest cannot satisfy exact proof;
- start ACK does not equal workload success;
- stale Provider Generation fails;
- replacement simulation preserves Ptah identities;
- unauthorized mount/network capability fails closed.

Dependencies: A04, A06, A07.

## A11 — Browser Provider

Maps: P0C-I011; WP02–WP05, WP09, WP11.

Deliver:

- Playwright/Chromium service;
- Browser Profile, Process, Context and Page projections;
- navigation and post-condition verification;
- download/upload integration;
- screenshot, console and network evidence foundations;
- detach/reconnect;
- privacy filtering.

Proof:

- persistent profile survives Provider restart where Policy permits;
- stale Context/Page Generation fails;
- navigation ACK does not equal page-state success;
- private browser data does not enter public logs;
- provider IDs remain Aliases;
- Browser work continues after client disconnect when requested.

Dependencies: A04, A06, A07, A08.

## A12 — Archive decomposition Provider

Maps: P0C-I012; WP03, WP08, WP11.

Deliver:

- libarchive-backed read-only decomposition;
- archive inventory;
- child Object and View registration;
- recursive depth and resource Policy;
- encrypted, malformed, partial and unsupported handling;
- coverage and limitation report;
- safe materialization.

Proof:

- source Object remains unchanged;
- skipped and unknown ranges remain explicit;
- traversal entries cannot escape root;
- malformed archive cannot claim complete coverage;
- backend replacement preserves source/decomposition identity;
- decompression bomb limits fail safely.

Dependencies: A07.

## A13 — Checkpoint, restart and verified recovery

Maps: P0C-I013; WP04–WP06, WP11.

Deliver:

- checkpoint request and result;
- integrity and compatibility verification;
- Workspace/process/terminal/browser metadata capture;
- Node agent restart;
- restore run;
- independent Recovery Verification;
- explicit reconciliation of Activities, attachments, Leases and partials.

Proof:

- checkpoint existence does not equal restore success;
- recovery creates new Generations;
- stale Leases and fences do not survive;
- missing evidence yields failed/inconclusive recovery;
- retained Activities and terminal attachments reconcile explicitly;
- uncertain external effects remain visible.

Dependencies: A02–A12 as applicable.

## A14 — Human Alpha control surface

Maps: Master Plan section 6.4; WP05, WP09, WP11.

Deliver:

- minimal Ptah home;
- Workspace selector;
- Activity Centre;
- Object/Artifact explorer;
- multi-terminal panel;
- transfer view;
- Browser panel;
- Provider/Node health view;
- checkpoint/reconnect controls;
- evidence and limitation links.

Proof:

- a human completes the vertical slice without an AI caller;
- stale UI projection cannot issue protected control;
- closing/reopening client restores accurate state;
- mobile/tablet projection does not hide critical status or approval controls.

Dependencies: A05–A13.

## A15 — Exact-head Online Ptah Alpha acceptance

Maps: P0C-I014; WP13, WP14.

Deliver:

- clean exact physical or accepted host revision;
- exact dependencies and backend artifacts;
- complete positive, negative and recovery suite;
- immutable report bundle;
- implementation commit binding;
- limitations record;
- release candidate and rollback instructions.

Proof:

- WP13 structural and semantic conformance passes;
- frozen WP14 first-slice suite passes;
- offline schema resolution passes;
- reports, logs, Receipts and Artifacts are digest-bound and retained;
- green status without reports fails;
- human operator and Hunter handoff tests pass.

Dependencies: A01–A14.

Milestone: **Online Ptah Alpha**.

# PROGRAMME B — Object World Beta

## B01 — Transfer and storage expansion

Deliver:

- resumable upload;
- segmented and multi-source download adapter;
- transfer priority and queue policy;
- Node-to-Node, object-store and Drive export adapters;
- deduplication and retention policy;
- Sync Relationship, Cursor, Conflict and Resolution;
- Backup Policy, Snapshot, Verification, Prune and Restore.

Proof:

- large interrupted uploads/downloads resume;
- synchronization conflict is explicit;
- backup and sync are not conflated;
- restored bytes do not claim Workspace recovery;
- optional remote adapter failure does not block local work.

Dependencies: A15.

## B02 — General type detection and progressive decomposition

Deliver:

- detector evidence aggregation;
- true-type and declared-type comparison;
- progressive Levels 0–3;
- recursion and resource policies;
- child relationship graph;
- searchable metadata.

Proof:

- detector disagreement is preserved;
- unsupported regions remain explicit;
- recursion limits fail safely;
- original Content remains immutable.

Dependencies: A12, B01.

## B03 — Documents and structured text

Deliver:

- document detection;
- metadata/text extraction;
- page/render Views;
- office/PDF/HTML adapters where lawful;
- citation/source anchoring;
- safe preview and conversion.

Proof:

- extraction and rendering limitations are recorded;
- malicious document content remains isolated;
- converted output links to exact source Revision.

Dependencies: B02.

## B04 — Images, audio and video

Deliver:

- metadata and technical inspection;
- thumbnails and previews;
- image transformation;
- audio/video probes and frame/waveform Views;
- controlled transcoding;
- large-media partial and cache policy.

Proof:

- transformations produce new Revisions/Artifacts;
- source bytes remain unchanged;
- incomplete media cannot claim full duration/coverage;
- heavy transcode does not block unrelated work.

Dependencies: B02.

## B05 — Executables and application packages

Deliver:

- PE, ELF, Mach-O and library inspection;
- import/export, section and signature Views;
- APK/AAB/DEX decomposition;
- embedded-object relationships;
- package metadata and safe static inspection.

Proof:

- static analysis does not claim execution success;
- packed/unknown regions remain explicit;
- extracted children retain provenance.

Dependencies: B02.

## B06 — Session Vault v1

Deliver:

- archive/export/import;
- Workspace versions;
- verified Session bundle;
- Object and Artifact manifest;
- readable recovery export;
- compatible restore on another Node;
- explicit conflicts and missing capabilities.

Proof:

- Workspace survives control and Node restart;
- compatible Node resume works;
- incompatible target fails with exact missing capability;
- recovered state is independently verified.

Dependencies: A13, B01–B05.

## B07 — Search v1

Deliver:

- filename and metadata search;
- document text and source symbol adapters;
- logs, Activities and Artifact search;
- index revision and rebuild;
- source-bound results.

Proof:

- index deletion/rebuild does not change canonical Objects;
- result points to exact source and Revision;
- private Workspace content remains isolated.

Dependencies: B02–B06.

Milestone: **Object World Beta**.

# PROGRAMME C — Firmware and Device Beta

## C01 — Disk image and partition foundations

Deliver:

- MBR/GPT parsing;
- raw/sparse conversion;
- partition Objects and Views;
- block-range coverage;
- safe read-only mount/materialization;
- comparison foundations.

Proof:

- partition boundaries and unknown ranges are exact;
- corrupt maps remain partial/inconclusive;
- source image remains immutable.

Dependencies: B02, B05.

## C02 — Filesystem Providers

Deliver in evidence-driven order:

- ext4;
- EROFS;
- F2FS;
- SquashFS;
- UBI/UBIFS;
- FAT;
- NTFS;
- ISO;
- later APFS/HFS through compatible Nodes.

Proof:

- read coverage and limitations are explicit;
- mount/provider IDs remain Aliases;
- traversal and unsafe materialization fail;
- unsupported features do not claim completeness.

Dependencies: C01.

## C03 — Generic Android image and OTA pack

Deliver:

- boot, vendor boot, init boot, DTBO and vbmeta inspection;
- dynamic partitions and `super.img`;
- Android OTA and `payload.bin`;
- partition and manifest relationships;
- comparison and rebuild proof levels.

Dependencies: C01, C02.

## C04 — Apple IPSW/OTA/IMG4 pack

Deliver read-first inventory, component extraction, signing/manifest Views and explicit supported proof levels.

Dependencies: C01, C02.

## C05 — MediaTek pack

Deliver scatter/bundle inventory, partition relationships and integration with lawful MTK/META evidence. Physical writes remain outside static pack authority.

Dependencies: C01, C02.

## C06 — Unisoc and Qualcomm packs

Deliver PAC/FDL and MBN/ELF/Firehose/XML static families with explicit loader/programmer evidence boundaries.

Dependencies: C01, C02.

## C07 — Reserved vendor completion packs

Samsung, Huawei/Honor, LG, Sony, OPPO/Realme/OnePlus, embedded and unknown-vendor lanes are added only with lawful samples, source and proof.

Dependencies: C01–C06.

## C08 — Device identity and transport substrate

Deliver:

- stable Device identity and candidate grouping;
- interface and connection epochs;
- ADB, Fastboot/Fastbootd, Apple and supported USB/serial observation Providers;
- Device Lease and Fence;
- protocol Operation/Attempt evidence;
- unstable USB recovery.

Proof:

- backend serial/port IDs remain Aliases;
- multiple-device ambiguity fails closed;
- stale epoch/Provider Generation fails;
- read evidence and write authority remain separate.

Dependencies: A04, A06, A07, A13.

## C09 — TTG Device X-Ray workload admission

Deliver read-only evidence workflow, exact repository pin, private/public boundary, profiles and fixtures.

Proof:

- observations correlate without manufacturing authority;
- disagreement and stale evidence remain visible;
- no destructive action is exposed.

Dependencies: C01–C08.

## C10 — Android Application and Device Session v1

Deliver:

- emulator and physical-device session;
- package install/version/signature verification;
- application launch/stop;
- UI hierarchy and semantic target;
- touch/type/scroll/keyboard/clipboard;
- screenshots, recording and logs;
- recovery and cleanup.

Proof:

- stale UI target is reacquired;
- input acknowledgement requires post-condition read-back;
- Device Session authority is leased and fenced;
- cleanup is independently verified.

Dependencies: C08, B05.

## C11 — Device Manager and MIBU workload admissions

Admit reversible DPC policy first, then cross-application/device workflow. Restricted recovery remains a separate later adapter family.

Dependencies: C09, C10.

Milestone: **Firmware and Device Beta**.

# PROGRAMME D — Full Workspace Release

## D01 — Human Workspace shell v2

Deliver mature docking/layout, editor integration, object/browser/application/device/media panels, responsive layouts, control transfer, approvals and accessibility.

Dependencies: A14, B, C.

## D02 — AI Project Workspace and context compiler

Deliver:

- `ptah.workspace.ai_project.v1` manifest;
- source-authority service;
- bounded context compiler;
- visible selected sources;
- parallel Session/thread projections;
- reusable Artifact Library;
- model-independent handoff;
- candidate-to-canonical review flow;
- scheduled Activity context with least privilege.

Proof:

- no cross-Workspace leakage;
- superseded source cannot outrank canonical source;
- model replacement preserves authority and state;
- scheduled Activity sees only granted Artifacts;
- private Hunter memory cannot enter public Workspace without explicit lawful promotion.

Dependencies: B06, B07, D01, WP10/11 implementation.

## D03 — Knowledge, Data and Search v2

Deliver document indexing, source symbols, firmware manifests, partition data, structured datasets, tables, query/citation evidence and database Domain Pack.

Dependencies: B07, C.

## D04 — Recipes and service registry

Deliver deterministic Recipes, versioned proposals/acceptance, service/exposed-port registry, reusable execution plans and parameter/secret boundaries.

Dependencies: A04, A10, B, D03.

## D05 — Package and Plugin lifecycle

Deliver discovery, install, exact pin, activation, health, rollback and removal with public/private and licence controls.

Dependencies: D04, WP10/11 implementation.

## D06 — Provenance, SBOM, signing and proof bundles

Deliver in-toto/Witness-compatible provenance, SBOM, Cosign-compatible signatures, ORAS relationships, trust policy and independent verification.

Dependencies: A07, A09, A10, D04.

## D07 — Security evidence and reproduction

Deliver authorization/plan/target records, Observation and Finding flows, remediation verification, Reproduction Runs, Evidence Cards and optional security workload adapters.

Dependencies: D06, WP12 implementation.

## D08 — Application platform expansion

Deliver Linux native/packaged applications, Windows Node/VM, macOS Node, compatible iOS Simulator and remote application display in an evidence-driven order.

Dependencies: D01, C10, Programme E foundations where remote Nodes are needed.

## D09 — Full Workspace release acceptance

Proof concurrent human and agent operation, long-running recovery, provider replacement, provenance, security evidence, plugin rollback and complete public/private audit.

Milestone: **Full Workspace Release**.

# PROGRAMME E — Distributed Ptah

## E01 — Secure multi-Node identity and connection

Deliver Node enrollment, revision/Generation, secure channel, capability announcements and reconnect.

Dependencies: A15, D06.

## E02 — Placement, Reservation, Lease and Fence runtime

Deliver Policy-aware placement, resource reservation, dispatch eligibility, expiry and stale-owner fencing.

Dependencies: E01, WP11 implementation.

## E03 — Node-to-Node Object and Artifact transfer

Deliver direct and relay transfer, resumable movement, cache policy and exact integrity verification.

Dependencies: E01, B01.

## E04 — Compatible Workspace movement

Deliver capability comparison, checkpoint bundle movement, target restore and Recovery Verification.

Dependencies: E02, E03, B06.

## E05 — Platform Nodes

Admit in order based on proof need:

- always-on Linux mini PC;
- workstation/GPU Node;
- Windows Node;
- macOS Node;
- Android/Device Nodes.

## E06 — Intermittent and local-first operation

Deliver offline queues, local authority boundaries, sync/reconciliation and useful degraded operation.

Dependencies: E01–E05.

## E07 — Distributed acceptance

Proof one Workspace safely uses several machines while preserving Activity ownership, Object identity, authority and recoverability.

Milestone: **Distributed Ptah**.

# PROGRAMME F — OS-ready foundation

Private integration lane; public Ptah remains OS-neutral.

## F01 — Declarative service and package profile

Package proven Ptah services, Providers and dependencies without changing contracts.

## F02 — Hardware and Device rules

Define hardware profiles, udev/Device rules, diagnostics and capability evidence.

## F03 — Virtualization and local workload substrate

Integrate QEMU/KVM/libvirt and optional stronger isolation Providers from proven interfaces.

## F04 — Bootable image and installation

Build reproducible installation/image process, offline package cache and recovery media.

## F05 — Update, rollback and encryption

Deliver atomic or otherwise verified updates, compatible rollback, disk encryption and recovery.

## F06 — Desktop and local shell integration

Integrate the Human Workspace shell with the selected desktop/compositor without making the desktop Ptah’s public identity.

## F07 — OS-ready acceptance

Prove the environment packages released Ptah services and can update/rollback without redesigning canonical identity or data.

Milestone: **OS-ready foundation**.

# 5. Cross-programme tracks

## Track X1 — Conformance and migrations

Runs in every package:

- local schema resolution;
- generated binding verification;
- migration and compatibility fixtures;
- backend replacement;
- exact-head structural and semantic reports.

## Track X2 — Security and privacy

Runs in every package:

- threat and misuse boundary;
- secrets and private-data scan;
- least privilege;
- audience/redaction/retention;
- dependency and supply-chain review;
- protected-action approval and read-back.

## Track X3 — Observability and evidence

Runs in every package:

- Event and trace correlation;
- exact Activity/Operation/Attempt identity;
- resource and timing evidence;
- immutable Receipt/Artifact retention;
- limitations and negative evidence.

## Track X4 — Human usability

Runs from Alpha onward:

- direct human control;
- accessible status and failure state;
- desktop/tablet/mobile projection where appropriate;
- no critical function hidden behind AI-only interaction.

## Track X5 — Recovery and handoff

Runs in every substantial Session:

- exact branch/commit;
- completed work;
- active blockers;
- failed attempts;
- evidence links;
- next safe action;
- durable `AI_HANDOFF.md` and current-state update.

# 6. Release and promotion rules

A release candidate may be promoted only when:

- all included packages are PROVEN;
- exact source/dependency/provider identities are retained;
- public/private and licence review passes;
- rollback and recovery instructions exist;
- known limitations are published at the appropriate audience;
- negative and partial results are not erased;
- the release is independently reviewable from retained evidence.

Security or dependency changes that affect runtime identity create new Provider/host revisions and rerun the relevant proof suites.

# 7. Current programme state

P00 Master-plan authority closure: ACTIVE.

P01 Physical-host and ADR-0033 closure: BLOCKED on the actual pinned host.

Programme A runtime packages: PLANNED and NOT AUTHORIZED.

Programmes B–F: PLANNED, dependency-ordered, and not active.

Runtime implementation: **NOT AUTHORIZED**.
