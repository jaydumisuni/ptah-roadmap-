# Ptah Progress Ledger

Tick only work backed by source inspection, pinned commits, accepted decisions, tests or live evidence.

- `[ ]` Not started
- `[-]` Active
- `[?]` Blocked/unresolved
- `[x]` Completed and evidenced

---

# Phase 0A — Donor recovery and requirement closure

**Status:** COMPLETE AND FROZEN AT `7d2dffee48f1400ba1cf88823343f09a3895ad33`

- [x] Private roadmap repository and public/private separation.
- [x] Master roadmap, Current State, progress and recovery rules.
- [x] Requirement Closure Matrix and donor/internal-record structure.
- [x] All v1 requirement clusters closed for Phase 0B contract design.
- [x] Linux semantic completion, parked-item audit and cross-requirement consistency review.
- [x] ADR-0017 accepted; Phase 0A frozen.

Evidence:

- `work-packages/PHASE-0A-CROSS-REQUIREMENT-CONSISTENCY-REVIEW.md`
- `work-packages/PHASE-0B-ENTRY-CONTRACT-PROOF-INPUTS.md`
- `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`

---

# Phase 0B — Contracts, migrations, conformance and proof design

**Status:** ACTIVE — IMPLEMENTATION STILL NOT AUTHORIZED

## 0B-WP01 — Common identity, versioning and typed families

**Status:** CANDIDATE COMPLETE.

- [x] UUIDv7 canonical identity and scoped Alias/public-remapping rules.
- [x] controlled entity-kind and identity/authority registries.
- [x] JSON Schema 2020-12, absolute Ptah URNs and local catalog.
- [x] common Entity Envelope.
- [x] record revision versus Object Revision/generation/epoch separation.
- [x] typed Provider/Session/Lease/Event/Revision/Snapshot/Recipe/Protocol/Evidence families.
- [x] namespaced/versioned state-machine and transition schemas.
- [x] migration definition/run and directional compatibility schemas.
- [x] privacy/audience/redaction/retention, extensions and tombstone rules.
- [x] consolidated safety net, fixtures and ADR-0018.

Evidence:

- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`
- `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`

## 0B-WP02 — Activity, Operation, Attempt, Event, Receipt and proof

**Status:** CANDIDATE COMPLETE.

- [x] Activity Request, Activity, Operation and Attempt separation.
- [x] retry/idempotency classes and uncertain-side-effect blocking.
- [x] exact Node/Provider/workload generation, epoch and nonce correlation.
- [x] dependencies, cancellation and manual-action requests.
- [x] typed Events and delivery attempts.
- [x] immutable Receipts and bounded proof claims.
- [x] Review, Verdict and authoritative external-result separation.
- [x] explicit stale/late/duplicate/contradictory evidence reconciliation.
- [x] six lifecycle machines and active catalog `0.1.1`.
- [x] migration, safety net, fixtures and ADR-0019.

Evidence:

- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`
- `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`

## 0B-WP03 — Object, Revision, View, Artifact and storage

**Status:** CANDIDATE COMPLETE.

- [x] Content byte identity, qualified hashes and deduplication scope.
- [x] durable Object and immutable Object Revision.
- [x] plural detector observations and classification decisions.
- [x] stable Relationship plus immutable Relationship Revisions.
- [x] child Object, View, Preview and Derivative separation.
- [x] bounded progressive decomposition.
- [x] Artifact promotion versus review/verification/acceptance/release.
- [x] immutable allowlisted Artifact Release.
- [x] Storage Location lifecycle/health/verification and safe deletion.
- [x] 20 active schemas, five lifecycle machines, migration, safety net, fixtures and ADR-0020.

Evidence:

- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`
- `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`

## 0B-WP04 — Node, Facility, Provider, capability and health

**Status:** CANDIDATE COMPLETE.

- [x] stable Node identity separated from aliases, enrollment, trust and reachability.
- [x] Node generation and connection epoch fencing.
- [x] immutable capability/resource observations and freshness.
- [x] Capability Definition/Claim/Verification/Availability/Snapshot separation.
- [x] Facility/Revision/Instance and Provider/Revision/Instance separation.
- [x] local Node-backed and remote-service Provider locality without fictional Nodes.
- [x] lifecycle, reachability, readiness, health and pressure separation.
- [x] operation-scoped dependency degradation.
- [x] exact-generation expiring Dispatch Eligibility.
- [x] 19 record schemas and six lifecycle machines in runtime catalog `0.1.2`.
- [x] migration, safety net, fixtures and ADR-0021/0021A/0021B.

Evidence:

- `schemas/phase-0b/runtime/schema-catalog.v0.1.2.json`
- `decisions/ADR-0021-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH-BOUNDARY.md`
- `decisions/ADR-0021B-WP04-FINAL-CATALOG-CORRECTION.md`

## 0B-WP05 — Workspace, Session, checkpoint, restore and recovery

**Status:** CANDIDATE COMPLETE.

- [x] stable Workspace identity and immutable Workspace Revision.
- [x] Membership and Provider Binding separated from runtime state.
- [x] Materialization identity/generation and truthful local/remote locality.
- [x] typed Session and Session Attachment/control separation.
- [x] Journal/outbox/cursor reconstruction without Activity replay authority.
- [x] Checkpoint Request, Component, Bundle and Verification separation.
- [x] consistency, completeness, portability, privacy and credential classification.
- [x] target-specific expiring Restore Compatibility before mutation.
- [x] Restore Run with new Activities/Attempts/generations.
- [x] runtime restore versus post-condition Recovery Verification.
- [x] explicit Export/Import identity, authority and provenance decisions.
- [x] 19 schemas and nine lifecycle machines in workspace catalog `0.1.0`.
- [x] migration, safety net, fixtures, WP05 package and ADR-0022.

Evidence:

- `schemas/phase-0b/workspace/schema-catalog.v0.1.0.json`
- `work-packages/PHASE-0B-WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY.md`
- `decisions/ADR-0022-WORKSPACE-SESSION-CHECKPOINT-RESTORE-RECOVERY-BOUNDARY.md`

## 0B-WP06 — Transfer, synchronization, conflict, backup and storage restore

**Status:** CANDIDATE COMPLETE.

- [x] Transfer Request/Run/Attempt/Manifest/Progress/Verification separation.
- [x] safe resume identity, validators, partial-state and authority checks.
- [x] Content/Object/Location acceptance after byte movement.
- [x] uncertain non-idempotent finalize/commit/delete handling.
- [x] Sync Relationship, Cursor, Run, Conflict and Resolution separation.
- [x] cursor freshness and destination-acceptance advancement rules.
- [x] first-class conflict history and explicit merge/selection decisions.
- [x] Backup Policy, Snapshot, Verification, Prune, Restore Decision and Restore Run separation.
- [x] encryption/key/read-back and dependency-aware restore/prune proof.
- [x] sync/replica/checkpoint/export/backup separation.
- [x] storage restore versus WP05 Workspace/application recovery.
- [x] 18 schemas and seven lifecycle machines in transfer catalog `0.1.0`.
- [x] migration, safety net, fixtures, WP06 package and ADR-0023.

Evidence:

- `schemas/phase-0b/transfer/schema-catalog.v0.1.0.json`
- `work-packages/PHASE-0B-WP06-TRANSFER-SYNC-CONFLICT-BACKUP.md`
- `decisions/ADR-0023-TRANSFER-SYNC-CONFLICT-BACKUP-RESTORE-BOUNDARY.md`

## 0B-WP07 — Recipe, Build, provenance, SBOM, signature and verification

**Status:** ACTIVE.

- [-] recover and normalize frozen Build/Artifact/Provenance requirements.
- [ ] define Recipe identity, immutable revision/hash and proposal/acceptance boundary.
- [ ] define backend-neutral Recipe versus backend-specific Compiled Plan.
- [ ] define Build Run, step mapping and Activity/Operation/Attempt correlation.
- [ ] define cache entry/use/verification and volatile-input reproducibility impact.
- [ ] define secret/credential access, redaction and cleanup evidence.
- [ ] bind outputs to exact Objects, Artifacts, Locations and provenance.
- [ ] define SBOM/package observations and explicit coverage limitations.
- [ ] define attestation creation versus policy verification.
- [ ] define signature, trust root, certificate, transparency and offline verification.
- [ ] define Build/export/SBOM/attestation/signing/review/reproduction/acceptance separation.
- [ ] define independent reproduction and byte-identical/functional comparison.
- [ ] commit candidate schemas, lifecycle machines and catalog.
- [ ] commit migration/compatibility rules, fixtures and consolidated safety net.
- [ ] accept WP07 package and ADR-0024 only after consistency review.

---

# Ordered work packages

- [x] 0B-WP01 — Common identity, versioning and typed-family conventions.
- [x] 0B-WP02 — Activity, Operation, Attempt, Event, Receipt and proof.
- [x] 0B-WP03 — Object, Revision, View, Artifact and storage relationships.
- [x] 0B-WP04 — Node, Facility, Provider, capability and health.
- [x] 0B-WP05 — Workspace, Session, checkpoint and recovery.
- [x] 0B-WP06 — Transfer, sync, conflict and backup.
- [-] 0B-WP07 — Recipe, Build, provenance, SBOM, signature and verification.
- [ ] 0B-WP08 — Domain Pack, firmware, disk and Device contracts.
- [ ] 0B-WP09 — Application, Browser, semantic UI and Shell contracts.
- [ ] 0B-WP10 — Knowledge, data, Package and Plugin contracts.
- [ ] 0B-WP11 — Isolation, placement, reservation, lease and secure grants.
- [ ] 0B-WP12 — Security, Finding, Claim, Evidence and reproduction contracts.
- [ ] 0B-WP13 — Cross-contract migrations and executable conformance harness.
- [ ] 0B-WP14 — Golden/negative corpus and proof-plan freeze.
- [ ] Phase 0B review/freeze and Phase 0C readiness decision.

## Cross-cutting Phase 0B gates

- [-] every schema versioned and traceable — WP01–WP06 complete; remaining domains pending.
- [-] state machines/transitions explicit and namespaced — WP01–WP06 complete; remaining domains pending.
- [-] saved records/sessions have migration paths — WP01–WP06 complete; remaining domains pending.
- [-] permissions, audience, privacy and redaction represented — WP01–WP06 mapped; remaining domains pending.
- [x] Provider/Facility candidate contracts defined — executable conformance deferred.
- [-] lawful positive/negative fixtures pinned — WP01–WP06 committed; remaining corpus pending.
- [-] proof plans name exact Receipts/Evidence — WP01–WP06 complete; remaining domains pending.
- [-] backend replacement testable — identity/runtime/storage/Workspace/transfer layers complete; remaining domains pending.
- [-] online and later local Nodes use the same contracts — candidate contracts neutral; executable proof pending.
- [-] private consumer knowledge absent from public schemas — WP01–WP06 neutral; full audit pending.
- [ ] public licence/dependency strategy ready for Phase 0C.
- [ ] first vertical slice selectable without identity/proof ambiguity.

---

# Phase 0C — First vertical slice approval

- [ ] Select Linux host and exact components.
- [ ] Select public project licence and dependency/source layout.
- [ ] Approve implementation proof plan.
- [ ] Record implementation authorization in `CURRENT_STATE.md`.

# Implementation phases

- [ ] Phase 1 — Concurrent one-Node substrate.
- [ ] Phase 2 — Intake and transfer.
- [ ] Phase 3 — Universal decomposition.
- [ ] Phase 4 — Firmware, disks and filesystems.
- [ ] Phase 5 — Git, containers, environments and Builds.
- [ ] Phase 6 — Browser and live web.
- [ ] Phase 7 — Human Workspace shell.
- [ ] Phase 8 — Session Vault.
- [ ] Phase 9 — Applications and devices.
- [ ] Phase 10 — Knowledge, data, search, recipes and plugins.
- [ ] Phase 11 — Provenance and security workloads.
- [ ] Phase 12 — Distributed Ptah.
- [ ] Phase 13 — OS readiness.
