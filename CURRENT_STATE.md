# Ptah Current State

**Last updated:** 2026-07-18  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Devices, Applications, Browsers, Sessions, Panels and Artifacts.

Ptah supplies the working world. Humans and compatible systems supply intent, reasoning, policy, restrictions and acceptance criteria.

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

---

# Phase 0A work packages closed for Phase 0B contract design

## WP01–WP02 — Core runtime

Closed:

- Node Protocol versus Workspace Provider;
- persistent Workspaces and concurrent Activities;
- Facility manifests and polyglot adapters;
- terminal/process and OCI-provider foundations;
- durable orchestration, live Events and observability;
- local journal/reconnect;
- operation/attempt/nonce/receipt/proof-level boundaries.

Primary machinery: OpenClaw, Daytona, Coder, E2B, Dev Containers, DevPod, containerd/OCI, OpenHands, Temporal, NATS/JetStream and OpenTelemetry, completed by internal AgentOps, Sergeant, Relay, CodeOps, MIBU and Hunter runtime evidence.

## WP03 — Build, Artifact and provenance

Closed:

- Build Recipe and backend compilation;
- BuildKit and Dagger roles;
- Artifact relationships and ORAS transport;
- SBOM, attestation, signature, trust, review and independent-reproduction levels.

## WP04 — Storage, transfer, synchronization and backup

Closed:

- hot local Workspace storage;
- local CAS plus local/shared SQL and R2/S3 direction;
- immutable Objects and mutable revisions/conflicts;
- resumable upload/download;
- cloud/Node transfer;
- encrypted backup/restore;
- Drive export/recovery;
- distributed shared filesystems parked pending measured need.

## WP05 — Universal Object and decomposition

Closed:

- immutable Object graph and plural detector claims;
- progressive bounded decomposition;
- child, View, preview, transform, decompilation and rebuild relationships;
- document, archive, image, media, binary, Android application and source-structure Domain Packs.

## WP06 — Firmware, disks and filesystems

Closed:

- Apple IPSW/BuildManifest;
- MediaTek META/BROM/Preloader/DA;
- Qualcomm Sahara/Firehose;
- Unisoc PAC/FDL;
- Android OTA/sparse/dynamic-partition/AVB;
- Samsung and generic vendor routing;
- GPT/MBR and isolated filesystem inspection;
- static analysis versus physical mutation;
- exact compatibility, immutable backup and read-back proof.

`.P5C` remains parked until a lawful verified sample, specification or parser exists.

## WP07 — Device and Application Runtime

Closed:

- stable Device identity, interface epochs, Provider workers and lease/fencing;
- Android ADB/Fastboot, files, packages, logs, display/audio/input and semantic UI;
- Device and Application Sessions;
- Linux graphical applications and remote display;
- Windows native/VM applications, RDP and semantic automation;
- macOS native/VM applications and visual/accessibility automation;
- iOS Simulator/physical-device providers and XCUITest/IDB;
- platform-specific checkpoint and proof classes.

Known retained gap: dedicated Linux AT-SPI semantic automation requires a later completion pass.

## WP08 — Browser and Live Research

Closed:

- Browser Provider, Binary, Profile, Process, Context, Page, Frame, Popup and Download identities;
- Playwright foundation;
- Browser-Use profile/session/recovery patterns without its agent identity;
- TurboWebFetch rendered batch retrieval adapted over pooled Contexts;
- MCP/SDK/UI adapter separation;
- source, DOM, accessibility, pixels, screenshot, video, trace, console and network evidence;
- source/citation records and explicit authentication/challenge/human-completion states.

## WP09 — Human Workspace Shell and Operator Interface

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

Inspected and saved:

- Eclipse Theia;
- OpenVSCode Server;
- code-server;
- xterm.js;
- Dockview;
- internal Hunter, Sergeant, MIBU, Device Manager and website UI patterns.

Accepted direction:

1. Ptah owns Shell Client, Shell Session, Panel Type/Instance, Layout Profile/Revision and control ownership.
2. Eclipse Theia is the primary full desktop/workbench foundation, not Ptah Core or the phone shell.
3. Dockview is the lighter responsive/wide-screen layout candidate.
4. Phone presentation uses one primary panel, compact switching, drawers and Activity status rather than arbitrary docking.
5. OpenVSCode Server and code-server are optional coding Applications/Providers.
6. xterm.js is the browser terminal renderer over Ptah PTY Sessions.
7. Panel/layout restoration never implies runtime recovery.
8. Activity Centre and Evidence Explorer project live Activities, Receipts, Artifacts, disagreements and limitations.
9. Settings remains separate from live operational control.
10. Human and automation control uses scoped leases, fencing and receipted takeover/return.
11. UI contributions call scoped Ptah Facilities rather than accessing host resources directly.
12. Accessibility, keyboard, touch, safe-area, reduced-motion and low-resource behavior are first-class.
13. Specialist UIs remain products/clients.
14. Hunter Foreman is excluded from active shell composition unless explicitly reintroduced.

Saved:

- `donors/ECLIPSE-THEIA.md`
- `donors/OPENVSCODE-CODE-SERVER.md`
- `donors/XTERMJS.md`
- `donors/DOCKVIEW.md`
- `internal/UI-FOUNDATIONS.md`
- `decisions/ADR-0012-HUMAN-WORKSPACE-SHELL-PANEL-CONTROL-BOUNDARY.md`
- `work-packages/PHASE-0A-WP09-HUMAN-WORKSPACE-SHELL.md`

Closed for Phase 0B design:

- `UI-001` Human Workspace shell;
- `UI-002` Activity Centre/evidence/review;
- Human Workspace portions of `SESSION-001`;
- shell contribution portions of `CORE-004`;
- human projections of `OBS-001`, `PROV-001` and runtime control leases.

No shell framework or UI implementation is approved yet.

---

# Active inspection unit

## WP10 — Knowledge, Data, Search and Plugin Composition

Inspect as one complementary group:

1. RAGFlow;
2. LlamaIndex;
3. Dify;
4. Polars;
5. Deno;
6. Model Context Protocol specification and official server examples;
7. OpenClaw/ClawHub plugin discovery and lifecycle patterns where requirements remain;
8. internal Hunter knowledge, memory, learning, search and provider bridges;
9. exact unresolved MiniRouter/Hermes relationships only where they overlap this subsystem.

Resolve:

- Knowledge Source, Corpus, Document and Chunk identities;
- source-grounded indexing and citations;
- ingestion, parsing, embedding and index revisions;
- permissions, deletion, freshness and re-indexing;
- search across Objects, Activities, Artifacts, Workspaces and external sources;
- structured data/table/database Activities;
- Polars/SQL execution and result Artifacts;
- recipe, service, tool and plugin manifests;
- MCP as one external adapter rather than Ptah's internal model;
- Deno/other sandboxed lightweight tool execution;
- provider-neutral model and data interfaces;
- plugin install, pin, health, upgrade, rollback and removal;
- public/private plugin registries and contribution boundaries;
- external reasoning/caller ownership without embedding a council into Ptah.

Required saved output:

- internal and external donor records after each inspection unit;
- Knowledge/Data/Search/Plugin composition record;
- Knowledge Source / Index / Query / Plugin boundary ADR;
- Requirement Closure Matrix updates for `SEARCH-001`, `DATA-001`, `PLUGIN-001` and related extensions;
- continuous `PROGRESS.md` and Current State updates.

---

# Accepted decisions

ADR-0001 through ADR-0012 are accepted and indexed in `DECISIONS.md`.

---

# No-build boundary

Allowed now:

- donor/internal recovery;
- source inspection, canonical pins and licence review;
- composite requirement closure;
- ADR, schema and proof planning after Phase 0A review.

Not allowed yet:

- copying donor code;
- declaring closure from one donor;
- beginning runtime or large UI implementation;
- selecting dependencies from README claims alone;
- replacing internal work without evidence;
- exposing private consumers publicly.

---

# Phase 0A completion gate

Every v1 requirement must have internal overlap, composite donors, canonical pins/licences, native gap, exit strategy and proof plan, or be explicitly parked/rejected with a replacement.

---

# Chat continuation instruction

Read this file first, followed by `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, `DONOR_RECOVERY.md`, `REQUIREMENT_CLOSURE_MATRIX.md`, relevant donor/internal records, work packages and ADRs before proposing or performing further work.
