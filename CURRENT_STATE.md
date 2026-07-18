# Ptah Current State

**Last updated:** 2026-07-18  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Active inspection unit:** Reproduction/security workloads and scanners  
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
- remote display, Window, checkpoint and platform proof boundaries;
- Linux AT-SPI/libatspi semantic tree, query, action, text, selection, value, cache and Event composition;
- Xorg versus GNOME-Wayland input paths and explicit visual fallback;
- Semantic Context/Snapshot/Node/Action identities and semantic post-condition proof.

Linux semantic completion record: `donors/AT-SPI.md`.

Accepted Linux semantic direction:

1. AT-SPI/libatspi is the primary Linux semantic UI Provider foundation.
2. New Ptah provider work uses direct libatspi/GObject-introspection rather than legacy pyatspi.
3. Dogtail contributes bounded search, retry, stale-node and diagnostic patterns without defining Ptah contracts.
4. GNOME Ponytail is a GNOME-Wayland input completion adapter, not universal Wayland automation.
5. D-Bus names, object paths, application IDs, AccessibleIds and child indices remain provider-local aliases.
6. Accessibility-bus observation and mutation are separately scoped privileged capabilities.
7. Events update/invalidate projections but never replace a fresh Semantic Snapshot.
8. semantic action success requires semantic and/or visual post-condition read-back.
9. opaque applications degrade explicitly to visual/coordinate automation.
10. password, sensitive text, clipboard and cross-application access require dedicated privacy/permission controls.

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
- RAGFlow and LlamaIndex;
- Dify;
- Polars and DuckDB;
- Deno;
- MCP specification and official reference servers;
- ClawHub and OpenClaw plugin lifecycle;
- Hermes Agent and MiniRouter boundary recovery.

Accepted direction:

1. Conversation, Knowledge Source, Source Object/View, Corpus, Document Revision, Chunk, Index Revision and caller-owned memory remain separate.
2. Source Objects and exact revisions are truth; indexes, embeddings, summaries and caches are derived and rebuildable.
3. Query, Result, ranking explanation and exact Citation remain separate.
4. Permissions apply during acquisition, retention, embedding, indexing, retrieval, citation, export and deletion.
5. LlamaIndex is the primary modular local knowledge-foundation candidate; RAGFlow is an optional heavier Knowledge Facility.
6. Search across Objects, Activities, Artifacts and Workspaces is native Ptah catalogue/index behavior, not only document RAG.
7. Polars and DuckDB are analytical engines behind Ptah Dataset/Query/Result identities.
8. Package, Package Release, Installed Plugin, Activation and Registry Entry remain separate.
9. Registry presence, verification, scans and manifest claims are evidence inputs, not approval or runtime proof.
10. Deno is the lightweight permission-scoped runtime candidate; native, FFI, untrusted or broad-privilege code escalates to OCI or VM isolation.
11. MCP is an external Facility adapter protocol, not Ptah's internal Object/Activity model.
12. Hunter, Hermes, Dify, OpenClaw and future systems remain external callers/Applications that own reasoning, memory and relationship policy.
13. Dify is study-only or separately licensed because of its modified licence.
14. MiniRouter remains study-only until its licence is resolved and belongs to later routing/evaluation work.

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

## WP11 — Strong Isolation and Distributed Placement/Scheduling

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

Inspected and saved:

- gVisor;
- Kata Containers;
- Firecracker;
- youki;
- crun;
- Ray;
- existing containerd/OCI, Workspace Provider, Node Protocol, Activity, transfer, checkpoint and lease/fencing foundations;
- MiniRouter only as an optional later routing/evaluation workload.

Accepted direction:

1. Isolation Class, runtime implementation, placement, reservation, execution generation and proof remain separate.
2. The closed isolation ladder is host/native trusted → Deno/WASM permission runtime → baseline OCI → gVisor → Kata → Firecracker → full VM.
3. runc, crun and youki remain replaceable implementations below one OCI Provider contract.
4. Rootless and memory-safe implementation are useful properties, not stronger isolation classes.
5. Incompatible work may move to an equal or stronger approved class or be blocked; Ptah never silently falls back to weaker isolation.
6. Node Capability Snapshots retain current kernel, architecture, virtualization, resources, pressure, providers, devices, checkpoint compatibility and health.
7. Placement filters hard feasibility before scoring locality, load, cost, accelerator fit, failure domain, checkpoint locality and interruption risk.
8. Placement Request, Candidate/Decision, Reservation, Lease, Generation and Fence remain separate.
9. Network, exact Object/View mounts, devices and credentials require explicit workload-generation grants.
10. Checkpoint production, restore compatibility and application recovery/read-back are separate proof levels.
11. gVisor is the primary stronger-container candidate.
12. Kata is the primary VM-backed container/sandbox candidate.
13. Firecracker is the primary standalone microVM candidate.
14. Ray is an optional trusted distributed Compute Facility behind Ptah Activities and placement, not the global scheduler or Object truth.
15. Mutually untrusted Ray workloads use separate isolated clusters.
16. Local one-Node and multi-Node operation use the same identities and contracts.
17. Scheduler policy is operational policy; caller reasoning may supply constraints/preferences but does not silently control Node authority.
18. MiniRouter remains an optional evaluation workload, not a Ptah routing authority.

Saved:

- `donors/GVISOR.md`
- `donors/KATA-CONTAINERS.md`
- `donors/FIRECRACKER.md`
- `donors/YOUKI.md`
- `donors/CRUN.md`
- `donors/RAY.md`
- `donors/MINIROUTER.md`
- `decisions/ADR-0014-ISOLATION-RUNTIME-PLACEMENT-SCHEDULING-BOUNDARY.md`
- `work-packages/PHASE-0A-WP11-ISOLATION-DISTRIBUTED-PLACEMENT.md`

Closed for Phase 0B design:

- `ISOLATION-001`;
- `DIST-001`;
- strong-isolation completion portions of runtime/plugin/caller contracts;
- distributed placement, checkpoint, observability, resource-accounting and proof extensions.

No Runtime Provider, scheduler, Ray cluster, network plane, credential broker or isolation implementation is approved yet.

---

# Active inspection unit

## Reproduction/security workloads and scanners

Inspect as one complementary group:

1. ReproZip and reproducible workload capture;
2. GUAC and security/provenance graph aggregation;
3. Semgrep and source/static analysis;
4. Trivy and Artifact/container/filesystem/IaC scanning;
5. ZAP and dynamic web/API security testing;
6. Strix and other approved offensive-validation orchestration only within explicit test scopes;
7. SparkDistill, ClaimBound and any internal/external reproduction or claim-evidence systems already named in the donor plan;
8. existing Build, SBOM, attestation, Object, Activity, Receipt, isolation and Sergeant review foundations.

Resolve:

- scanner invocation versus Finding, Claim, Evidence and review;
- source/static, dependency/SBOM, secret, configuration, container, runtime and dynamic-test classes;
- scanner/tool/database/rule versions and freshness;
- target Object/Artifact/Workspace revision and test authorization;
- suppression, exception, accepted-risk and false-positive records;
- finding deduplication without losing independent detector disagreement;
- exploitability/impact/confidence versus severity;
- active security-test network, credential and destructive-action scopes;
- reproducible environment capture and replay limitations;
- security result signing, provenance and retention;
- independent Sergeant/department review and release gates;
- public/private security evidence boundaries.

Required outputs:

- donor/composition records for the security/reproduction group;
- security Finding/Claim/Evidence/reproduction boundary ADR if required;
- Requirement Closure Matrix updates;
- progress/current-state synchronization;
- explicit parked/rejected tools or unsafe paths.

After this group:

1. research/documentation-source and unresolved-profile cleanup;
2. cross-requirement Phase 0A review;
3. Phase 0A freeze/readiness decision for Phase 0B.

---

# Accepted decisions

ADR-0001 through ADR-0014 are accepted and indexed in `DECISIONS.md`.

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
