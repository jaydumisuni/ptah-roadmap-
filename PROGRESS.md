# Ptah Progress Ledger

Tick only work backed by source inspection, pinned commits, accepted decisions, tests or live evidence.

- `[ ]` Not started
- `[-]` Active
- `[?]` Blocked/unresolved
- `[x]` Completed and evidenced

---

# Phase 0A — Donor recovery and requirement closure

**Status:** COMPLETE AND FROZEN AT `7d2dffee48f1400ba1cf88823343f09a3895ad33`

## Repository, architecture and freeze control

- [x] Private roadmap repository and public/private separation.
- [x] Master roadmap, Current State, progress and recovery rules.
- [x] Requirement Closure Matrix and donor/internal-record structure.
- [x] Core runtime, Build/Artifact, storage, Object/decomposition, firmware/disk, Device/Application, Browser, UI, knowledge/data/plugin, isolation/placement and security/reproduction clusters closed for design.
- [x] Linux AT-SPI semantic completion.
- [x] research/documentation/source cleanup and parked-item audit.
- [x] cross-requirement identity, authority, state and lifecycle review.
- [x] Phase 0B contract/proof inputs enumerated.
- [x] ADR-0017 accepted; Phase 0A frozen.

## Phase 0A requirement closure

- [x] Core runtime.
- [x] Build/Artifact/Provenance.
- [x] Storage/Transfer/Sync/Backup.
- [x] Object/Decomposition.
- [x] Firmware/Disk/Filesystem.
- [x] Device/Application Runtime.
- [x] Browser/Live Research.
- [x] Human Workspace/UI.
- [x] Knowledge/Data/Search/Plugin.
- [x] Isolation/Distributed placement.
- [x] Security/reproduction workloads.
- [x] Review and freeze.

Evidence:

- `work-packages/PHASE-0A-CROSS-REQUIREMENT-CONSISTENCY-REVIEW.md`
- `work-packages/PHASE-0B-ENTRY-CONTRACT-PROOF-INPUTS.md`
- `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`

---

# Phase 0B — Contracts, migrations, conformance and proof design

**Status:** ACTIVE — IMPLEMENTATION STILL NOT AUTHORIZED

## 0B-WP01 — Common identity, versioning and typed families

**Status:** CANDIDATE COMPLETE — downstream use approved; implementation freeze deferred.

- [x] UUIDv7 canonical identity and Alias/public-remapping rules.
- [x] controlled entity-kind and identity/authority registries.
- [x] JSON Schema 2020-12 and absolute Ptah schema URNs.
- [x] local candidate schema catalog.
- [x] nested common Entity Envelope direction.
- [x] record revision versus Object Revision/generation/epoch separation.
- [x] typed Provider/Session/Lease/Event/Revision/Snapshot/Recipe/Protocol/Evidence families.
- [x] namespaced/versioned state-machine and transition schemas.
- [x] migration definition/run and directional compatibility schemas.
- [x] privacy/audience/redaction/retention, extensions and tombstone rules.
- [x] consolidated safety net and positive/negative fixtures.
- [x] ADR-0018 accepted.

Evidence:

- `work-packages/PHASE-0B-WP01-COMMON-IDENTITY-VERSIONING-TYPED-FAMILIES.md`
- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`
- `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`

## 0B-WP02 — Activity, Operation, Attempt, Event, Receipt and proof

**Status:** CANDIDATE COMPLETE — downstream use approved; executable conformance deferred.

- [x] Activity Request and durable Activity separation.
- [x] Activity, logical Operation and physical Attempt identities.
- [x] retry/idempotency classes and uncertain-side-effect blocking.
- [x] exact Node/Provider/workload generations, connection epoch and nonce correlation.
- [x] first-class Activity Dependency, Cancellation Request and Manual Action Request.
- [x] typed Event payloads and delivery attempts.
- [x] immutable Receipts, bounded proof claims and correction/supersession.
- [x] Review, Verdict and Authoritative External Result separation.
- [x] explicit reconciliation of stale/late/duplicate/contradictory evidence.
- [x] six lifecycle state machines.
- [x] active schema catalog plus corrected request schemas `0.1.1`.
- [x] migration/compatibility rules, consolidated safety net and fixtures.
- [x] ADR-0019 accepted.

Evidence:

- `work-packages/PHASE-0B-WP02-ACTIVITY-EVENT-RECEIPT-PROOF.md`
- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`
- `conformance/PHASE-0B-WP02-ACTIVITY-EVENT-RECEIPT-SAFETY-NET.md`
- `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`

## 0B-WP03 — Object, Revision, View, Artifact and storage

**Status:** CANDIDATE COMPLETE — downstream use approved; executable graph/storage conformance deferred.

- [x] Content byte identity, qualified hash observations and deduplication scope.
- [x] durable logical Object and immutable Object Revision.
- [x] plural detector observations and separate classification decisions.
- [x] stable Relationship plus immutable Relationship Revisions.
- [x] child Object, View, Preview and Derivative separation.
- [x] progressive Decomposition Run with budgets, coverage, gaps and partial output.
- [x] Artifact promotion separated from verification/review/acceptance/release.
- [x] immutable allowlisted Artifact Release and withdrawal/revocation history.
- [x] Storage Location lifecycle, health and verification separation.
- [x] storage observation, verification, repair and deletion-decision records.
- [x] tombstone, replica deletion and shared Content-byte deletion separation.
- [x] five lifecycle state machines.
- [x] 20 active schemas plus common/activity dependencies.
- [x] migration/compatibility record, consolidated safety net and fixtures.
- [x] ADR-0020 accepted and indexed.

Evidence:

- `work-packages/PHASE-0B-WP03-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE.md`
- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`
- `conformance/PHASE-0B-WP03-OBJECT-ARTIFACT-STORAGE-SAFETY-NET.md`
- `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`

## 0B-WP04 — Node, Facility, Provider, capability and health

**Status:** CANDIDATE COMPLETE — downstream use approved; executable runtime conformance deferred.

- [x] stable Node identity separated from aliases, enrollment, trust and reachability.
- [x] Node generation and connection epoch separation/fencing.
- [x] immutable Node observations, capability snapshots and resource snapshots.
- [x] total/allocatable/reserved/consumed/available/unavailable/pressure resource dimensions.
- [x] Capability Definition, Claim, Verification, Availability and Snapshot separation.
- [x] Facility, Facility Revision and Facility Instance contracts.
- [x] Provider, Provider Revision and Provider Instance/generation contracts.
- [x] local Node-backed and remote-service Provider locality without fictional Nodes.
- [x] Provider lifecycle, reachability, readiness and health separation.
- [x] operation-scoped optional-dependency degradation.
- [x] immutable, exact-generation, expiring Dispatch Eligibility.
- [x] 19 active record schemas in runtime catalog `0.1.2`.
- [x] six active lifecycle machines with versioned proof/locality corrections.
- [x] migration/compatibility rules, consolidated safety net and cross-record fixtures.
- [x] ADR-0021 accepted and indexed; ADR-0021A/0021B record catalog corrections.

Evidence:

- `work-packages/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH.md`
- `schemas/phase-0b/runtime/schema-catalog.v0.1.2.json`
- `conformance/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-SAFETY-NET.md`
- `decisions/ADR-0021-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH-BOUNDARY.md`
- `decisions/ADR-0021B-WP04-FINAL-CATALOG-CORRECTION.md`

## Ordered work packages

- [x] 0B-WP01 — Common identity, versioning and typed-family conventions.
- [x] 0B-WP02 — Activity, Operation, Attempt, Event, Receipt and proof.
- [x] 0B-WP03 — Object, Revision, View, Artifact and storage relationships.
- [x] 0B-WP04 — Node, Facility, Provider, capability and health.
- [-] 0B-WP05 — Workspace, Session, checkpoint and recovery.
- [ ] 0B-WP06 — Transfer, sync, conflict and backup.
- [ ] 0B-WP07 — Recipe, Build, provenance, SBOM, signature and verification.
- [ ] 0B-WP08 — Domain Pack, firmware, disk and Device contracts.
- [ ] 0B-WP09 — Application, Browser, semantic UI and Shell contracts.
- [ ] 0B-WP10 — Knowledge, data, Package and Plugin contracts.
- [ ] 0B-WP11 — Isolation, placement, reservation, lease and secure grants.
- [ ] 0B-WP12 — Security, Finding, Claim, Evidence and reproduction contracts.
- [ ] 0B-WP13 — Cross-contract migrations and executable conformance harness.
- [ ] 0B-WP14 — Golden/negative corpus and proof-plan freeze.
- [ ] Phase 0B review/freeze and Phase 0C readiness decision.

## Cross-cutting Phase 0B gates

- [-] every schema versioned and traceable to ADR/requirement — WP01–WP04 complete; remaining domains pending.
- [-] state machines/transitions explicit and namespaced — WP01–WP04 complete; remaining domains pending.
- [-] saved records/sessions have migration paths — WP01–WP04 complete; Workspace/session and later domains pending.
- [-] permissions, audience and redaction represented — common/Object/runtime mappings complete; remaining domains pending.
- [x] Provider/Facility candidate contracts defined — executable conformance deferred.
- [-] lawful golden and negative fixtures pinned — WP01–WP04 committed; remaining corpus pending.
- [-] proof plans name exact Receipts/Evidence — Activity/Object/runtime layers complete; remaining domains pending.
- [-] backend replacement testable — Object/storage and Facility/Provider contracts complete; remaining domains pending.
- [-] online and later local Nodes use the same contracts — Node/Provider contracts neutral; executable proof pending.
- [-] private consumer knowledge absent from public schemas — WP01–WP04 neutral; full audit pending.
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