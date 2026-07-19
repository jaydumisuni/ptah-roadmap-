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
