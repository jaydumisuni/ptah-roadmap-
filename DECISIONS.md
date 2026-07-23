# Ptah Accepted Decisions

This is the compact index of decisions that must not be silently reversed. Full architecture, limitations, donor boundaries and proof requirements live in the referenced ADRs.

---

## Foundational decisions

### D-001 — Ptah is independent

**ACCEPTED.** Ptah is a neutral open-source working world. Private consumers integrate through public-safe contracts rather than defining Ptah identity.

### D-002 — Ptah is the world, not the thinker

**ACCEPTED.** Ptah supplies environments, Objects, Activities, Facilities, applications, devices, browsers, storage and evidence. Callers supply intent, reasoning, policy and acceptance.

### D-003 — Roadmap and implementation are separate

**ACCEPTED.** `ptah-roadmap-` owns private planning/recovery. `Ptah-space` owns public implementation and earned public progress.

### D-004 — Online first, local later, same contracts

**ACCEPTED.** Online, local mini-PC and future OS deployments reuse the same identities, contracts and data model.

### D-005 — Workspace and Activity are different

**ACCEPTED.** A Workspace persists while many unrelated Activities run, pause, fail, recover and complete inside it.

### D-006 — Object-first architecture

**ACCEPTED.** Original bytes remain preserved through Content/Object/Revision identities with hashes, Locations, provenance, Relationships, Views and Derivatives.

### D-007 — Domain Packs

**ACCEPTED.** Specialist formats use versioned detect, inventory, decompose, preview, transform, validate, compare, rebuild and execute contracts.

### D-008 — Internet is normally available

**ACCEPTED.** Internet access is an operating-environment capability. Restrictions come from caller, Workspace, Provider or deployment configuration.

### D-009 — Storage is layered

**ACCEPTED.** Fast local storage performs active work; Object storage retains durable bytes; Git owns source history; SQL owns metadata; Drive is export/recovery.

### D-010 — Integration first, not greenfield pride

**ACCEPTED.** Every subsystem begins with internal recovery, donor inspection, mature machinery and identification of the true native Ptah gap.

### D-011 — Polyglot operational chassis

**ACCEPTED.** Rust is preferred where valuable, while mature tools in other languages remain behind stable adapters.

### D-012 — Evidence before completion

**ACCEPTED.** Source presence and optimistic UI claims are not proof. Completion requires frozen records, live evidence, hashes, limitations and retained negative results.

### D-013 — No work before placement and approval

**ACCEPTED.** Ideas are preserved, placed, dependency-ordered and approved before implementation.

### D-014 — Engineering cycle

**ACCEPTED.** Understand → Build → Review → Freeze → Prove → Submit/Ship.

### D-015 — Public Ptah remains neutral

**ACCEPTED.** Public source must not expose private consumers, workflows, credentials, topology, customer data or unpublished company decisions.

### D-016 — Operating-system assembly is a later private lane

**ACCEPTED.** Ptah stays OS-neutral. Distribution, boot, update and hardware integration follow proven online and Node software.

---

## Architecture boundary decisions

### D-017 — Composite donor closure

**ACCEPTED.** No subsystem closes through one repository. Closure combines internal foundation, primary donor, completion donors, mature machinery, native contracts, exit strategy and proof.

Full decision: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

### D-018 — Activity, Event and observability remain separate

**ACCEPTED.** Ptah owns the Activity Ledger. Temporal, NATS/JetStream, OpenTelemetry, large streams and proof Receipts have different guarantees.

Full decision: `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`.

### D-019 — Operation state, evidence and authority remain separate

**ACCEPTED.** Activity state, Operations, Attempts, Events, telemetry, Receipts, Artifact proof, review and authoritative external results are distinct. Stale or unverified evidence never becomes PASS.

Full decision: `decisions/ADR-0004-OPERATION-RECEIPTS-PROOF-LEVELS.md`.

### D-020 — Build, Artifact and provenance remain separate

**ACCEPTED.** Build Recipe, execution graph, Artifact/Object graph, SBOM, attestation, signature, review, reproduction and release acceptance are separate layers.

Full decision: `decisions/ADR-0005-BUILD-ARTIFACT-PROVENANCE-BOUNDARY.md`.

### D-021 — Storage, transfer, synchronization and backup remain separate

**ACCEPTED.** Hot Workspace bytes, immutable Objects, revisions, caches, partial transfers, replicas, backups and exports have different guarantees.

Full decision: `decisions/ADR-0006-STORAGE-TRANSFER-SYNC-BOUNDARY.md`.

### D-022 — Object identity, detector claims, Views and rebuilds remain separate

**ACCEPTED.** Originals remain immutable; detector disagreements are retained; decomposition is bounded; children, Views, previews, transformations, decompilations and rebuilds carry explicit origin.

Full decision: `decisions/ADR-0007-OBJECT-GRAPH-DECOMPOSITION-DERIVATIVE-BOUNDARY.md`.

### D-023 — Firmware packages, disk images and physical operations remain separate

**ACCEPTED.** Static analysis does not authorize physical mutation. Device presence, protocol stages, loaders/programmers, write acknowledgement and read-back are distinct proof levels.

Full decision: `decisions/ADR-0008-DISK-FIRMWARE-DEVICE-OPERATION-BOUNDARY.md`.

### D-024 — Device identity, lease, display, input and semantic UI remain separate

**ACCEPTED.** Ptah owns stable Device identity, interface epochs, Provider generation, leases/fencing, Device Sessions, streams and semantic contexts. Backend IDs are aliases; cleanup is verified.

Full decision: `decisions/ADR-0009-DEVICE-SESSION-DISPLAY-INPUT-SEMANTIC-UI-BOUNDARY.md`.

### D-025 — Application Provider, Window, display and semantic context remain separate

**ACCEPTED.** Application Object, Provider, Installation, Session, Process, Window, display, semantics and checkpoint state are distinct across Linux, Windows, macOS and mobile runtimes.

Full decision: `decisions/ADR-0010-APPLICATION-PROVIDER-WINDOW-DISPLAY-BOUNDARY.md`.

### D-026 — Browser Profile, Process, Context, Page and evidence remain separate

**ACCEPTED.** Playwright is the primary Browser foundation. Profiles, processes, Contexts, Pages, downloads, source Views, evidence and research claims retain separate identities and privacy/recovery rules.

Full decision: `decisions/ADR-0011-BROWSER-PROFILE-CONTEXT-PAGE-EVIDENCE-BOUNDARY.md`.

### D-027 — Human Workspace shell, Panels, Layout and control remain separate

**ACCEPTED.** Ptah owns Shell Client/Session, Panel Type/Instance, Layout Profile/Revision and scoped control leases. UI state never becomes runtime truth; human/automation takeover is fenced and receipted.

Full decision: `decisions/ADR-0012-HUMAN-WORKSPACE-SHELL-PANEL-CONTROL-BOUNDARY.md`.

### D-028 — Knowledge source, indexes, queries, data and plugins remain separate

**ACCEPTED.** Ptah owns neutral Knowledge Source, Corpus, Document/Index Revision, Query/Result/Citation, Dataset/Table and Package/Release/Installed Plugin/Activation identities. Indexes are derived and caller reasoning/memory remains external.

Full decision: `decisions/ADR-0013-KNOWLEDGE-DATA-SEARCH-PLUGIN-BOUNDARY.md`.

### D-029 — Isolation Class, runtime, placement, reservation and proof remain separate

**ACCEPTED.** Ptah owns Isolation Class, Runtime Provider, Node Capability Snapshot, Placement Request/Decision, Reservation, Lease, Generation, Fence, secure grants and Checkpoint Bundle. No silent weakening is permitted.

Full decision: `decisions/ADR-0014-ISOLATION-RUNTIME-PLACEMENT-SCHEDULING-BOUNDARY.md`.

### D-030 — Linux semantic target, snapshot, actions, raw input and proof remain separate

**ACCEPTED.** AT-SPI/libatspi is the primary Linux semantic foundation. Ptah owns Semantic Provider/Snapshot/Target/Selector/Action identities; stale targets are reacquired and post-condition read-back is required.

Full decision: `decisions/ADR-0015-LINUX-APPLICATION-SEMANTIC-AUTOMATION-BOUNDARY.md`.

### D-031 — Security Observation, Finding, validation, reproduction and acceptance remain separate

**ACCEPTED.** Ptah owns exact Security Authorization/Plan/Target/machinery/Coverage, Finding Observation, Correlated Finding, disposition, remediation, Verification Run, Reproduction Run, bounded Claim and Evidence Card identities.

Full decision: `decisions/ADR-0016-SECURITY-FINDING-VALIDATION-REPRODUCTION-BOUNDARY.md`.

### D-032 — Phase 0A is frozen; Phase 0B contract design is active

**ACCEPTED.** Phase 0A architecture and donor closure are frozen at roadmap commit `7d2dffee48f1400ba1cf88823343f09a3895ad33`. Phase 0B is limited to schemas, migrations, conformance and proof design; implementation and dependency selection remain blocked until Phase 0C approval.

Full decision: `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`.

---

## Phase 0B candidate decisions

### D-033 — Common identity, schema versioning and typed families are explicit

**ACCEPTED.** `ptah.common` `0.1.0` defines UUIDv7 canonical identity, scoped Aliases, absolute schema URNs, the Entity Envelope, typed families, namespaced state machines, directional migration and explicit privacy/retention semantics.

Full decision: `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`.

### D-034 — Activity, Operation, Attempt, Event, Receipt and proof remain exact

**ACCEPTED.** `ptah.activity` `0.1.0` with corrected request schemas `0.1.1` separates durable work, logical effects, physical tries, notifications, telemetry, immutable producer evidence, review and authoritative external truth.

Full decision: `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`.

### D-035 — Content, Object, Revision, View, Artifact and Location remain separate

**ACCEPTED.** `ptah.object` / `ptah.storage` `0.1.0` define exact byte identity, logical source identity, immutable revisions, plural detector evidence, relationship history, derived representations, promoted results and storage replicas without backend leakage.

Full decision: `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`.

### D-036 — Node, Facility, Provider, capability and health remain separate

**ACCEPTED.** `ptah.runtime` `0.1.2` defines stable Node/Facility identity, Provider revisions/instances/generations, capability evidence, resource truth, truthful local/remote locality and expiring Dispatch Eligibility. Lifecycle, reachability, readiness, health and pressure remain separate.

Full decisions:

- `decisions/ADR-0021-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH-BOUNDARY.md`;
- `decisions/ADR-0021A-WP04-CATALOG-PROOF-VOCABULARY-CORRECTION.md`;
- `decisions/ADR-0021B-WP04-FINAL-CATALOG-CORRECTION.md`.

### D-037 — Workspace, Session, Checkpoint, Restore and Recovery remain separate

**ACCEPTED.** `ptah.workspace` `0.1.0` preserves stable Workspace identity across revisions, Provider bindings, materializations, Sessions, clients and layouts. Checkpoint creation, integrity verification, target compatibility, runtime restore and application Recovery Verification are distinct. Restore creates new generations and cannot erase uncertain external effects.

Full decision: `decisions/ADR-0022-WORKSPACE-SESSION-CHECKPOINT-RESTORE-RECOVERY-BOUNDARY.md`.

### D-038 — Transfer, Sync, Conflict, Backup and storage restore remain separate

**ACCEPTED.** `ptah.transfer` `0.1.0` separates Transfer Request/Run/Manifest/Progress/Verification; Sync Relationship/Cursor/Run/Conflict/Resolution; and Backup Policy/Snapshot/Verification/Prune/Restore. Provider acknowledgement is not Content acceptance, sync is not backup, and restored storage is not Workspace/application recovery.

Full decision: `decisions/ADR-0023-TRANSFER-SYNC-CONFLICT-BACKUP-RESTORE-BOUNDARY.md`.

### D-039 — Recipe, Build, provenance, SBOM, signature and verification remain separate

**ACCEPTED.** `ptah.build` / `ptah.provenance` catalog `0.1.1` separates Recipe/Revision/Proposal/Acceptance/Readiness/Compatibility/Plan/Run/Step, cache and secret evidence, produced output identity, SBOM coverage, attestation/signature creation and verification, trust/transparency policy, proof domains and independent reproduction. `build_completed`, a cache hit, a signed statement or a Proof Bundle cannot become release acceptance.

Full decisions:

- `decisions/ADR-0024-RECIPE-BUILD-PROVENANCE-SBOM-SIGNATURE-VERIFICATION-BOUNDARY.md`;
- `decisions/ADR-0024A-WP07-FINAL-CATALOG-CONVENTIONS-CORRECTION.md`.


---

## Phase 0B completion decisions

### D-040 — Domain Pack, firmware, disk, filesystem and Device boundaries are explicit

**ACCEPTED.** WP08 preserves Domain Packs, firmware packages, Disk Images, filesystems, Devices, protocol Operations, recovery and physical mutation as separate identities and proof levels. Static analysis and write acknowledgement cannot authorize or prove physical mutation.

Full decision: `decisions/ADR-0025-DOMAIN-FIRMWARE-DISK-DEVICE-BOUNDARY.md`.

### D-041 — Application, Browser, semantic UI and human Shell boundaries are explicit

**ACCEPTED.** WP09 separates Application, Installation, Session, Process, Window and display; Browser Profile, Process, Context and Page; Semantic snapshots/targets/actions; and Shell clients, panels, layouts and control transfer. UI state cannot become runtime truth.

Full decision: `decisions/ADR-0026-APPLICATION-BROWSER-SEMANTIC-UI-SHELL-BOUNDARY.md`.

### D-042 — Knowledge, Data, Package and Plugin boundaries are explicit

**ACCEPTED.** WP10 defines neutral Knowledge Sources, revisions, indexes, queries, citations, datasets, tables, packages, releases, installations, Plugins and activations. Indexes remain derived and caller reasoning/private memory remains external.

Full decision: `decisions/ADR-0027-KNOWLEDGE-DATA-PACKAGE-PLUGIN-BOUNDARY.md`.

### D-043 — Isolation, placement, reservations, Leases and secure Grants are explicit

**ACCEPTED.** WP11 separates Isolation Class, runtime Provider, capability snapshot, placement, Reservation, Lease, Generation, Fence and secure Grants. Silent isolation or authority weakening is prohibited.

Full decision: `decisions/ADR-0028-ISOLATION-PLACEMENT-RESERVATION-LEASE-SECURE-GRANTS-BOUNDARY.md`.

### D-044 — Security Observation, Finding, Claim, Evidence and reproduction are explicit

**ACCEPTED.** WP12 separates authorization, target, plan, Observation, Finding, validation, disposition, remediation, Verification Run, Reproduction Run, bounded Claim and Evidence. Scanner output cannot become accepted truth by itself.

Full decision: `decisions/ADR-0029-SECURITY-FINDING-CLAIM-EVIDENCE-REPRODUCTION-BOUNDARY.md`.

### D-045 — Executable conformance and exact-head proof are mandatory

**ACCEPTED.** WP13 provides offline structural and semantic conformance, local URN resolution, catalog/lifecycle/fixture integrity and exact-head reports. It found and forced correction of real cross-package defects.

Full decision: `decisions/ADR-0030-EXECUTABLE-CONFORMANCE-AND-EXACT-HEAD-PROOF.md`.

### D-046 — Golden/negative corpus and proof-plan freeze are authoritative

**ACCEPTED.** WP14 freezes lawful positive, negative and adversarial fixtures, immutable expected-proof records and the first vertical-slice proof burden. A green summary without retained reports fails acceptance.

Full decision: `decisions/ADR-0031-GOLDEN-NEGATIVE-CORPUS-AND-PROOF-PLAN-FREEZE.md`.

### D-047 — Phase 0B is frozen and Phase 0C selection is active

**ACCEPTED.** WP01–WP14 are frozen at `dc2db457f1705d0cba80f17ab76e5e93f808aee0`. Runtime dependency, host, licence, source-layout and first-slice selections belong to Phase 0C.

Full decision: `decisions/ADR-0032-PHASE-0B-FREEZE-PHASE-0C-ENTRY.md`.

---

## Phase 0C accepted governance and design evidence

### D-048 — Apache-2.0 public/private boundary is operative

**ACCEPTED.** Public repository-owned Ptah source is Apache-2.0 under `John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS`. Private THETECHGUY systems, customer/device/payment data, restricted adapters, donor source and trademarks remain excluded.

Evidence: `work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md`.

### D-049 — AI Project Workspace is a provider-independent composition profile

**ACCEPTED AS NON-OPERATIVE DESIGN EVIDENCE.** `ptah.workspace.ai_project.v1` composes existing frozen primitives. Hidden provider memory and implicit global tool access are rejected. Ptah owns durable truth and Grants; Hunter coordinates through bounded context packets.

Evidence: `work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md`.

---

## Phase 0C accepted planning authority

### D-050 — Master Plan, implementation roadmap and durable handoff have separate authorities

**ACCEPTED.** `MASTER_PLAN.md` version `1.0.0` is the product and operating authority; `IMPLEMENTATION_ROADMAP.md` version `1.0.0` is the delivery-sequencing authority; frozen WP01–WP14 remain technical contract authority; `CURRENT_STATE.md` selects the exact current work; `AI_HANDOFF.md` and `master-plan-index.json` provide durable recovery. Phase 0C-16 candidate `37d23449fda9a426f56ee8b09042dda91587a6d1` passed exact-head validation and merged as `2c24f9e6b0fc98d5e03605596db75d7495796353`. Runtime implementation remains unauthorized.

Full decision: `decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md`.

### D-051 — Tenfold archive formation separates parallel evidence from promotion authority

**ACCEPTED.** Large Ptah archive/recovery campaigns use `max(20, human-equivalent workers × 10)`. A normal twenty-private formation pairs ten Primary Archivists with ten Independent Verifiers for at most ten ordinary records; harder sources consume 40/60/80–100/up to 120 privates. Privates cannot issue verdicts, adopt donors, reopen Phase 0A or authorize implementation. Campaign 001 queues 98 obligations across ten formations and 200 private slots without pre-accepting any record. Candidate `58b577b6793ec28de084e6d712c3c1e88bfe2d3a` passed run `29853954659` and merged as `c4973cbf4d02a34f14a7aefa85b8e2ea7b392752`.

Full decision: `decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md`.

---

## Current proposed decisions

### ADR-0033 — First vertical-slice host, licence, layout and backend selections

**PROPOSED.** Master Plan/roadmap authority is complete. The physical pinned-host result, package and retention acceptance, final Phase 0C closure review and explicit runtime authorization remain open.

### ADR-0036 — Platform diagnostic advisory and efficient worker execution boundary

**PROPOSED.** Ptah may compare configured platform expectations with observed health, capability and execution evidence and emit a bounded upgrade or inspection advisory. For a caller-submitted job and Recipe/Plan, Ptah may apply the Sergeant-derived ten-for-two pattern to run bounded parallel workers and independent checks. Ptah may not choose caller work, invent semantic scope, approve a result or install its own upgrade.

Full decision: `decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md`.
