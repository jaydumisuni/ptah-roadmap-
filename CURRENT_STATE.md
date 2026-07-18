# Ptah Current State

**Last updated:** 2026-07-18  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Active work package:** WP11 — Strong Isolation and Distributed Placement/Scheduling  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Devices, Applications, Browsers, Sessions, Panels, Knowledge Sources, Datasets, Plugins and Artifacts.

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
- resumable transfer, sync, backup/restore and Drive recovery;
- distributed shared filesystems parked pending measured need.

## WP05 — Universal Object and decomposition

Closed:

- immutable Object graph and plural detector claims;
- progressive bounded decomposition;
- child, View, preview, transform, decompilation and rebuild relationships;
- document, archive, image, media, binary, Android application and source-structure Domain Packs.

## WP06 — Firmware, disks and filesystems

Closed:

- Apple, MediaTek, Qualcomm, Unisoc, Android OTA and Samsung/vendor composition;
- GPT/MBR and isolated filesystem inspection;
- static analysis versus physical mutation;
- exact compatibility, immutable backup and read-back proof.

`.P5C` remains parked until a lawful verified sample, specification or parser exists.

## WP07 — Device and Application Runtime

Closed:

- stable Device identity, interface epochs, Provider workers and lease/fencing;
- Android device control, display/input and semantic UI;
- Linux, Windows, macOS and iOS Application Providers/Sessions;
- remote display, Window, checkpoint and platform proof boundaries.

Known retained gap: dedicated Linux AT-SPI semantic automation requires a later completion pass.

## WP08 — Browser and Live Research

Closed:

- Browser Provider, Binary, Profile, Process, Context, Page, Frame, Popup and Download identities;
- Playwright foundation and Browser-Use/TurboWebFetch completion patterns;
- source, DOM, accessibility, screenshot, video, trace, console and network evidence;
- source/citation records and explicit authentication/challenge/human-completion states.

## WP09 — Human Workspace Shell and Operator Interface

Closed:

- Shell Client/Session, Panel Type/Instance, Layout Profile/Revision and control ownership;
- Theia full workbench, Dockview responsive layouts, xterm.js terminal rendering and optional coding Applications;
- Activity Centre, Evidence Explorer and exact lifecycle/proof labels;
- desktop/tablet/phone projections, accessibility and human/automation fenced control.

Saved decision: `decisions/ADR-0012-HUMAN-WORKSPACE-SHELL-PANEL-CONTROL-BOUNDARY.md`.

## WP10 — Knowledge, Data, Search and Plugin Composition

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

Inspected and saved:

- internal Hunter knowledge, memory, learning, sync, retrieval and provider foundations;
- RAGFlow;
- LlamaIndex;
- Dify;
- Polars;
- DuckDB;
- Deno;
- MCP specification and official reference servers;
- ClawHub;
- OpenClaw plugin lifecycle;
- Hermes Agent;
- MiniRouter boundary recovery.

Accepted direction:

1. Conversation, Knowledge Source, Source Object/View, Corpus, Document Revision, Chunk, Index Revision and caller-owned memory remain separate.
2. Source Objects and exact revisions are truth; indexes, embeddings, summaries and caches are derived and rebuildable.
3. Query, Result, ranking explanation and exact Citation remain separate.
4. Permissions apply during acquisition, retention, embedding, indexing, retrieval, citation, export and deletion.
5. LlamaIndex is the primary modular local knowledge-foundation candidate; RAGFlow is an optional heavier Knowledge Facility.
6. Search across Objects, Activities, Artifacts and Workspaces is native Ptah catalogue/index behavior, not only document RAG.
7. Polars and DuckDB are analytical engines behind Ptah Dataset/Query/Result identities; transactional databases remain separate Facilities.
8. Package, Package Release, Installed Plugin, Activation and Registry Entry remain separate.
9. Registry presence, verification, scans and manifest claims are evidence inputs, not approval or runtime proof.
10. Deno is the lightweight permission-scoped runtime candidate; native, FFI, untrusted or broad-privilege code escalates to OCI or VM isolation.
11. MCP is an external Facility adapter protocol, not Ptah's internal Object/Activity model.
12. Hunter, Hermes, Dify, OpenClaw and future systems remain external callers/Applications that own reasoning, personal memory and relationship policy.
13. Dify is study-only or separately licensed because of its modified licence.
14. MiniRouter moves to later routing/evaluation work and remains study-only until its licence is resolved.

Saved:

- `internal/HUNTER-KNOWLEDGE-MEMORY-SEARCH.md`
- `donors/RAGFLOW.md`
- `donors/LLAMAINDEX.md`
- `donors/DIFY.md`
- `donors/POLARS.md`
- `donors/DUCKDB.md`
- `donors/DENO.md`
- `donors/MCP.md`
- `donors/CLAWHUB.md`
- `donors/OPENCLAW.md`
- `donors/HERMES-AGENT.md`
- `donors/MINIROUTER.md`
- `decisions/ADR-0013-KNOWLEDGE-DATA-SEARCH-PLUGIN-BOUNDARY.md`
- `work-packages/PHASE-0A-WP10-KNOWLEDGE-DATA-SEARCH-PLUGIN.md`

Closed for Phase 0B design:

- `SEARCH-001`;
- `DATA-001`;
- `PLUGIN-001`;
- knowledge/index extensions of Object, storage, Session, observability and provenance contracts;
- provider-neutral model/data adapter direction;
- MCP adapter and external reasoning/caller boundaries.

No Knowledge Facility, search index, data engine, plugin manager, registry, MCP server or UI implementation is approved yet.

---

# Active inspection unit

## WP11 — Strong Isolation and Distributed Placement/Scheduling

Inspect as one complementary group:

1. gVisor;
2. Kata Containers;
3. Firecracker;
4. youki;
5. crun;
6. Ray;
7. existing containerd/OCI, Workspace Provider, Node Protocol, Activity, transfer and checkpoint foundations;
8. internal THETECHGUY Node, worker, resource and deployment requirements;
9. MiniRouter only as an optional routing/evaluation workload.

Resolve:

- lightweight OCI versus syscall sandbox versus VM-strength isolation;
- runtime-class selection and escalation rules;
- Node/provider capability and resource snapshots;
- placement, reservation, lease, fencing and generation identity;
- secure networking, credential delivery and data locality;
- CPU, RAM, disk, accelerator and cost-aware scheduling;
- interruption, checkpoint, migration, rescheduling and recovery;
- local one-Node operation versus multi-Node distribution;
- failure domains and degraded fallback;
- scheduler policy versus caller reasoning;
- routing/evaluation workloads without embedding a router into Ptah Core.

Required saved output:

- donor records after each inspection unit;
- isolation and distributed-placement composition record;
- isolation/runtime-class/placement/scheduling boundary ADR;
- Requirement Closure Matrix updates for isolation and `DIST-001`;
- continuous `PROGRESS.md` and Current State updates.

---

# Accepted decisions

ADR-0001 through ADR-0013 are accepted and indexed in `DECISIONS.md`.

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
