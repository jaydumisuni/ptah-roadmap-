# Ptah Space — Canonical Master Roadmap

**Status:** Accepted planning baseline  
**Implementation:** Not started  
**Current phase:** Phase 0A — Recovery and donor closure  
**Public implementation repository:** `jaydumisuni/Ptah-space`

This document is the complete execution roadmap. It supersedes earlier Ptah plans unless a later accepted decision explicitly changes it.

---

# 1. Canonical definition

Ptah Space is an independent, open-source, online-first, concurrent digital world where humans and compatible software systems can upload, download, open, decompose, inspect, run, build, transform, render, compare, store, resume, and recover files, repositories, applications, firmware, devices, environments, and artifacts.

Ptah provides:

- persistent workspaces;
- concurrent activities;
- terminals and processes;
- Git and repositories;
- browsers and live internet;
- containers, virtual machines, remote nodes, emulators, and devices;
- storage, transfer, artifacts, and recovery;
- media, documents, executables, applications, firmware, disks, and filesystems;
- neutral APIs, SDKs, CLI, event streams, and plugin contracts.

The user or calling system provides intent, reasoning, instructions, priorities, restrictions, and acceptance criteria.

Ptah does not provide company strategy, approval judgment, councils, assistant identity, organizational memory, or autonomous product decisions.

---

# 2. Non-negotiable architecture laws

1. **Ptah is the world, not the thinker.**
2. **A workspace is not a job.** One workspace may host many simultaneous activities.
3. **Files are objects, not opaque blobs.** Originals, children, derivatives, previews, and provenance must be linked.
4. **Original objects remain preserved** unless explicitly replaced.
5. **Live internet is a normal capability.**
6. **Active work uses fast local storage.** Object storage is not a build filesystem.
7. **Online and local Ptah use the same contracts.**
8. **Ptah remains polyglot.** Rust is the operational chassis, not a reason to rewrite mature engines.
9. **Concurrency is foundational.** Heavy work must not globally block terminals, browsers, transfers, or unrelated activities.
10. **Technical isolation preserves world integrity; it is not Ptah making user-policy decisions.**
11. **Existing work is recovered before rebuilding.**
12. **Public Ptah remains neutral and independent.**
13. **No implementation begins before roadmap placement and approval.**
14. **Every capability must be proven, not merely present in source.**
15. **The permanent local system must reuse the online architecture rather than replace it.**

---

# 3. Canonical world model

## 3.1 Object

Anything Ptah can store, inspect, transform, execute, mount, compare, or render.

Required fields include:

- object ID;
- workspace ID;
- original name;
- declared type and detected type;
- content hash and size;
- source and provenance;
- parent and child relationships;
- storage locations;
- metadata;
- available views and operations;
- derivative objects;
- producing activity;
- schema version.

## 3.2 Workspace

A persistent namespace containing:

- files and object graph;
- repositories;
- terminals;
- processes and services;
- browsers;
- containers and runtimes;
- applications;
- devices;
- attached storage;
- activities;
- artifacts;
- checkpoints and session state.

## 3.3 Activity

An independently addressable operation inside a workspace.

Canonical states:

- queued;
- preparing;
- running;
- waiting;
- paused;
- resuming;
- completed;
- failed;
- cancelled;
- detached;
- recovering.

Activities may form caller-supplied dependency graphs while independent branches run concurrently.

## 3.4 Artifact

A durable result retained beyond its producing process, including:

- binaries;
- documents;
- images and video;
- screenshots and recordings;
- reports;
- patches;
- models;
- firmware derivatives;
- test outputs;
- proof bundles;
- SBOMs and attestations.

## 3.5 Node

A physical or virtual machine contributing capabilities. Nodes report:

- identity and version;
- operating system and architecture;
- CPU, RAM, GPU, and storage;
- available facilities and toolchains;
- container or VM support;
- attached devices;
- health and current load;
- active activities.

## 3.6 Facility

A stable Ptah contract implemented by one or more engines. Examples:

- Browser Facility;
- Transfer Facility;
- Git Facility;
- Build Facility;
- Media Facility;
- Firmware Facility;
- Device Facility;
- Document Facility;
- Application Facility;
- Storage Facility.

## 3.7 Session

A recoverable record of a working world. It references workspace state, objects, activities, terminals, browsers, containers, applications, storage, and artifacts without assuming every process can be serialized byte-for-byte.

---

# 4. Domain-pack model

Every domain pack implements a common contract:

- detect;
- inventory;
- decompose;
- preview;
- open or mount;
- transform;
- validate;
- compare;
- rebuild where supported;
- execute through an appropriate runtime.

Planned packs:

- Archives;
- Documents;
- Media;
- Executables;
- Applications;
- Firmware;
- Disks and Filesystems;
- Source Code;
- Databases;
- Web;
- Unknown Binary Research.

Decomposition must be progressive:

- Level 0: registration, hash, size, true type, basic metadata;
- Level 1: fast structure and inventory;
- Level 2: usable views and derivatives;
- Level 3: deep recursive analysis.

---

# 5. Storage and transfer model

## Hot local storage

Used for active work:

- Git mirrors and worktrees;
- package and build caches;
- container layers;
- active downloads;
- browser profiles;
- media intermediates;
- filesystem mounts;
- emulator and VM images;
- local databases.

## Durable object storage

Used for:

- uploaded originals;
- artifacts;
- session archives;
- large logs;
- documents and media;
- firmware packages;
- proof bundles.

The first online implementation may use R2/S3-compatible object storage while the public Ptah storage contract remains backend-neutral.

## Metadata catalogue

Node-local catalogue may begin with SQLite. Shared online records may use PostgreSQL, D1, or another accepted SQL backend.

## Google Drive

Drive is an export and readable recovery destination, not the live build, container, database, or Git filesystem.

## Git

Git remains source truth for code, versioned configuration, and reviewable project documentation.

## Logical paths

- `ptah://projects/<project>`
- `ptah://workspaces/<workspace>`
- `ptah://objects/<object>`
- `ptah://artifacts/<artifact>`
- `ptah://sessions/<session>`
- `ptah://sources/external/<source>`
- `ptah://cache/<cache>`
- `ptah://volumes/<volume>`

---

# 6. Engineering cycle and gates

Every roadmap item passes through:

1. **Understand** — recover existing work, donors, requirements, constraints, licences, and accepted boundaries.
2. **Build** — implement only the approved slice.
3. **Review** — inspect source, architecture, behavior, evidence, and unintended changes.
4. **Freeze** — pin the reviewed checkpoint and contracts.
5. **Prove** — run deterministic and live proof against the frozen checkpoint.
6. **Submit / Ship** — merge, release, or promote only after proof.

No phase is complete because code exists. It is complete only when its gate is proven and recorded.

---

# 7. Roadmap phases

## Phase 0A — Internal and external donor recovery

**Purpose:** close requirements using the strongest available internal work, external donors, mature upstream machinery, and only then identify native Ptah gaps.

Deliverables:

- donor inventory;
- canonical URLs;
- pinned commits or tags;
- licence review;
- activity status and last meaningful update;
- exact relevant files and directories;
- verified capabilities;
- known limitations;
- public/private boundary;
- adopt, adapt, wrap, fork, study, host, reject, or further-inspection classification;
- replacement and exit strategy;
- requirement closure matrix.

Required donor lanes:

- gateway, relay, nodes, and reconnect;
- durable activities and event transport;
- workspaces, sandboxes, and providers;
- container runtime and stronger isolation;
- build graphs and caches;
- observability;
- provenance, signing, and artifact transport;
- browser and live research;
- transfer, uploads, downloads, synchronization, and backup;
- decomposition and file understanding;
- media and documents;
- executables and applications;
- firmware, disks, and filesystems;
- Android and physical devices;
- knowledge, search, and data;
- human workspace shell and remote application display;
- internal THETECHGUY donor pool.

Gate:

- Every v1 requirement has a primary donor, secondary donor, internal evidence source, or accepted native Ptah build decision.
- No important donor remains classified merely from its README.
- Licence and exit strategy are recorded before code reuse.

---

## Phase 0B — Contracts, migrations, and proof design

Deliverables:

- object schema;
- relationship schema;
- workspace schema;
- activity schema;
- artifact schema;
- node schema;
- facility and plugin schema;
- session schema;
- snapshot schema;
- telemetry schema;
- provenance schema;
- firmware schema;
- sync and conflict schemas;
- credential-reference schema;
- schema-version and migration rules;
- event envelope;
- facility adapter contract;
- workspace-provider contract;
- golden test-corpus rules;
- proof levels for extraction and rebuilding.

Gate:

- Contracts support online and later local nodes without private consumer knowledge.
- Old saved sessions and objects have a migration path.
- Concurrency, recovery, provenance, and failure states are explicit.

---

## Phase 0C — First vertical-slice selection

Select the smallest real online world that proves Ptah identity.

Required slice:

- one Linux execution node;
- one persistent workspace;
- object registration;
- concurrent activity runtime;
- several terminals;
- one upload and one resumable download path;
- Git clone or mirror;
- one container execution path;
- one browser path;
- one decomposition adapter;
- artifact registration;
- checkpoint and reconnect.

Gate:

- Exact implementation work is approved and recorded in `CURRENT_STATE.md` before coding.

---

## Phase 1 — Concurrent one-node substrate

Build:

- Rust node agent;
- workspace namespace;
- object catalogue;
- activity registry;
- process and PTY supervision;
- live event streaming;
- cancellation and detach;
- node health;
- resource accounting;
- artifact registration;
- basic facility host.

Proof:

- One workspace runs at least ten independent activities.
- Each activity has separate output, progress, and failure state.
- One failure does not stop unrelated work.
- Disconnect and reconnect restore accurate state.
- A heavy activity does not globally block lightweight activities.

---

## Phase 2 — Intake, transfer, and object registration

Build:

- browser and API upload;
- resumable upload;
- URL and browser download;
- segmented and multi-source download adapter;
- transfer queue and priority;
- pause and resume;
- partial-file preservation;
- streaming hashes;
- duplicate detection;
- local, object-storage, Drive, and node transfer adapters;
- immutable original registration;
- transfer progress events.

Proof:

- Large interrupted upload and download resume without starting over.
- Identical content deduplicates by hash.
- Transfers run while terminals, browsers, and other activities remain active.

---

## Phase 3 — General decomposition and universal object graph

Build:

- true-type detection;
- archive and compression pack;
- document detection, extraction, and rendering adapters;
- media metadata and preview adapters;
- image processing;
- executable parsing;
- APK/AAB/DEX decomposition;
- embedded-data and unknown-binary inspection;
- recursive child-object relationships;
- progressive derivatives and previews;
- searchable metadata.

Proof:

A mixed archive containing a PDF, APK, image, video, executable, and nested archive is recursively decomposed while other workspace activities continue.

---

## Phase 4 — Disk, filesystem, and firmware foundations

Build:

- GPT and MBR parsing;
- raw and Android sparse conversion;
- dynamic partitions and `super.img`;
- boot, vendor boot, init boot, DTBO, and vbmeta inspection;
- filesystem adapters for ext4, EROFS, F2FS, SquashFS, UBI/UBIFS, FAT, NTFS, ISO, and later APFS/HFS through suitable nodes;
- Apple IPSW/OTA/IMG4 family;
- MediaTek scatter and bundle family;
- Unisoc PAC and FDL family;
- Qualcomm MBN/ELF/Firehose/XML family;
- generic Android OTA and `payload.bin`;
- reserved Samsung, Huawei/Honor, LG, Sony, OPPO/Realme/OnePlus, embedded, and unknown-vendor packs;
- firmware inventory and partition views;
- comparison and rebuild proof levels.

Proof:

Process concurrently:

- one IPSW;
- one MTK scatter package;
- one Unisoc PAC;
- one Qualcomm XML/MBN directory;
- one Android OTA payload.

Every meaningful component becomes independently addressable without freezing terminals or Chromium.

---

## Phase 5 — Git, containers, environments, and builds

Build:

- Git mirrors;
- clone, fetch, branches, tags, PR refs, exact commits, worktrees, submodules, and LFS;
- workspace provider interface;
- local-process provider;
- OCI/container provider;
- Dev Container support;
- containerd-compatible lifecycle;
- BuildKit;
- Dagger-style typed recipes where proven useful;
- package and build caches;
- environment manifests;
- artifact export;
- SBOM and provenance hooks.

Proof:

- Two isolated workspaces use one repository mirror and shared caches without interfering.
- Parallel build branches execute concurrently.
- Build outputs are traceable to exact inputs, environment, tool versions, and commands.

---

## Phase 6 — Browser and live web world

Build:

- interactive Chromium;
- Playwright-based automation;
- persistent contexts and profiles;
- authenticated sessions supplied by callers;
- multiple tabs and browser activities;
- screenshots and recordings;
- console and network logs;
- downloads and uploads;
- desktop, tablet, and mobile viewports;
- HTML/SVG rendering;
- JavaScript-rendered extraction;
- warm browser pools;
- browser activity recovery;
- MCP and other external tool adapters without replacing Ptah’s internal contracts.

Proof:

- Multiple independent browser contexts run concurrently.
- A live application is opened, interacted with, captured, and registered as artifacts.
- Closing the client does not destroy active browser work unless requested.

---

## Phase 7 — Human workspace shell

Build:

- Ptah home;
- project and session selector;
- object explorer;
- file browser;
- multi-terminal;
- editor integration;
- browser panels;
- Activity Centre;
- transfers;
- containers and processes;
- media and document viewers;
- firmware views;
- applications and devices;
- artifacts and storage;
- session controls;
- node status.

The shell should reuse a mature extensible framework where appropriate rather than rebuilding editor, terminal, extension, and panel systems from zero.

Proof:

A human can operate the complete vertical slice directly without an AI caller.

---

## Phase 8 — Session Vault, snapshots, and recovery

Build:

- pause;
- checkpoint;
- archive;
- export;
- import;
- resume;
- workspace and object versions;
- filesystem snapshots;
- container, VM, and emulator snapshot references;
- activity recovery after restart;
- Drive export;
- object-storage archive;
- online/local sync foundations;
- conflict representation.

Proof:

- A session survives node and control-plane restart.
- Key files, objects, Git state, terminals, browser state, activities, and artifacts recover accurately.
- The same session can resume on another compatible node.

---

## Phase 9 — Application and device world

### Android

- APK/AAB runtime;
- emulators;
- physical-device bridge;
- ADB and Fastboot;
- package installation;
- application launch and stop;
- semantic UI hierarchy;
- touch, type, scroll, keyboard, clipboard, recording, screenshots, and logs;
- device inventory and unstable-USB recovery;
- emulator and device snapshots.

### Linux

- native applications;
- AppImage, DEB/RPM, Flatpak/Snap, JAR, WebAssembly;
- remote graphical sessions.

### Windows

- Windows node and VM;
- EXE/MSI inspection and execution;
- clean snapshots;
- optional Wine adapter;
- process, crash, filesystem, and registry evidence;
- remote application display.

### Apple

- IPA inspection;
- signing and entitlements;
- macOS node;
- Xcode build;
- compatible iOS Simulator execution;
- signed physical-device execution;
- logs and streamed display.

Proof:

Several application sessions run simultaneously without blocking ordinary Ptah work.

---

## Phase 10 — Knowledge, data, search, and reusable recipes

Build:

- unified search across filenames, metadata, documents, source symbols, logs, firmware manifests, partitions, executable imports, activities, and artifacts;
- document indexing and retrieval adapters;
- database domain pack;
- structured data processing;
- reusable deterministic recipes;
- service and exposed-port registry;
- plugin discovery, installation, pinning, health, rollback, and removal.

Ptah may host knowledge or agent platforms as workloads, but they do not replace Ptah Core.

---

## Phase 11 — Provenance, signing, security evidence, and workload proof

Build and integrate:

- activity receipts;
- source and output hashes;
- tool, plugin, image, environment, and node identity;
- SBOM generation;
- in-toto/Witness-compatible provenance;
- Cosign-compatible signing;
- ORAS/OCI artifact relationships;
- immutable proof bundles;
- replay and reproducibility packs;
- security workload adapters;
- honest claim boundaries and negative-result retention.

Proof:

An artifact can be independently traced and verified from source materials through every producing step.

---

## Phase 12 — Distributed Ptah

Build:

- multiple Linux nodes;
- future mini-PC node;
- Windows and macOS nodes;
- GPU node;
- Android and physical-device nodes;
- capability announcements;
- workload placement;
- direct and relay-based object transfer;
- node identities and secure connections;
- intermittent connectivity;
- local-first/offline mode;
- compatible session movement;
- shared-storage evaluation only when proven necessary.

Proof:

One workspace safely uses capabilities from several machines while preserving activity ownership, object identity, and recoverability.

---

## Phase 13 — Operating-system readiness lane

This is a private integration lane, not part of Ptah’s public identity.

Ptah itself remains OS-neutral. Later operating-system assembly may evaluate:

- Linux distribution or image foundation;
- declarative packages and hardware profiles;
- system services and device rules;
- bootable image creation;
- atomic updates and rollback;
- disk encryption and recovery;
- QEMU/KVM and libvirt;
- desktop/compositor integration;
- offline package caches;
- drivers and hardware diagnostics.

Gate:

The online and node software must be mature enough that the local operating environment packages proven Ptah services rather than redesigning them.

---

# 8. Release milestones

## Milestone 0 — Architecture and donor closure

Phases 0A–0C complete and frozen.

## Milestone 1 — Online Ptah Alpha

One Linux node supports persistent workspaces, concurrent activities, transfers, Git, terminal, container execution, Chromium, one decomposition path, artifacts, and reconnect.

## Milestone 2 — Object World Beta

Progressive decomposition, media, documents, applications, object graph, search, and durable sessions are proven.

## Milestone 3 — Firmware and Device Beta

Major firmware families, disks/filesystems, Android devices, emulators, and specialist node adapters are proven.

## Milestone 4 — Full Workspace Release

Human shell, mature facilities, provenance, security evidence, recipes, plugins, and long-running session recovery are complete.

## Milestone 5 — Distributed Ptah

Mini PC, workstation, platform nodes, devices, and offline/local-first operation are integrated.

## Milestone 6 — OS-ready foundation

Ptah is stable enough to be packaged into a larger local operating environment without changing its public identity or contracts.

---

# 9. Cross-cutting requirements

These apply from the first implementation phase:

- versioned contracts and migrations;
- credential and connection references rather than raw secrets in session files;
- object versions and rollback;
- logs, metrics, traces, timing, and resource use;
- content hashing and deduplication;
- provenance and tool identity;
- golden test corpus;
- public/private boundary;
- licences and upstream tracking;
- replacement and exit strategy for every external dependency;
- online/local synchronization model;
- negative and blocked outcomes retained as evidence;
- accessibility and direct human use;
- performance proof under concurrency.

---

# 10. Definition of done

Ptah is complete only when it can reliably provide one coherent world in which users and compatible systems can:

- work online and later locally;
- run many activities concurrently;
- receive and move large files reliably;
- decompose and navigate complex objects;
- clone, build, test, and render projects;
- browse the live web and operate applications;
- inspect firmware, disks, and devices;
- save, restore, and move sessions;
- verify exactly how artifacts were produced;
- use several physical nodes through one consistent contract;
- continue operating when optional facilities are unavailable;
- extend the world through stable facility and plugin interfaces.

Completion is evidence-backed, not declared from source presence alone.
