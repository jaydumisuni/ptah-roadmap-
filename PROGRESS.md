# Ptah Progress Ledger

Tick only work backed by source inspection, pinned commits, accepted decisions, tests or live evidence.

- `[ ]` Not started
- `[-]` Active
- `[?]` Blocked or unresolved
- `[x]` Completed and evidenced

---

# Phase 0A — Donor recovery and requirement closure

**Status:** COMPLETE AND FROZEN

Frozen checkpoint:

`7d2dffee48f1400ba1cf88823343f09a3895ad33`

- [x] private roadmap repository and public/private separation;
- [x] master roadmap, Current State, progress and recovery rules;
- [x] Requirement Closure Matrix and donor/internal-record structure;
- [x] all v1 requirement clusters closed for contract design;
- [x] Linux semantic completion and parked-item audit;
- [x] cross-requirement consistency review;
- [x] ADR-0017 accepted and Phase 0A frozen.

---

# Phase 0B — Contracts, migrations, conformance and proof design

**Status:** COMPLETE AND FROZEN — RUNTIME IMPLEMENTATION NOT AUTHORIZED BY THIS PHASE

Freeze/Phase 0C entry merge:

`dc2db457f1705d0cba80f17ab76e5e93f808aee0`

## Completed packages

### WP01 — Common identity, versioning and typed families

- [x] UUIDv7 canonical identity and scoped Alias/public-remapping rules;
- [x] controlled entity-kind and identity/authority registries;
- [x] JSON Schema 2020-12, absolute Ptah URNs and local catalog;
- [x] typed families, lifecycle machines and migration rules;
- [x] privacy, retention, fixtures, safety net and ADR-0018.

### WP02 — Activity, Operation, Attempt, Event, Receipt and proof

- [x] Activity/Operation/Attempt separation;
- [x] retry/idempotency and uncertain-side-effect handling;
- [x] generation, epoch and nonce correlation;
- [x] immutable Receipts and bounded claims;
- [x] Review/Verdict/external-authority separation;
- [x] migrations, fixtures, safety net and ADR-0019.

### WP03 — Object, Revision, View, Artifact and storage

- [x] Content byte identity and qualified hashes;
- [x] stable Object and immutable Revision;
- [x] detector observations and relationship history;
- [x] child/View/Preview/Derivative boundaries;
- [x] Artifact promotion/review/verification/release separation;
- [x] Storage Location lifecycle and safe deletion;
- [x] migrations, fixtures, safety net and ADR-0020.

### WP04 — Node, Facility, Provider, capability and health

- [x] Node identity, generation and connection epoch;
- [x] capability/resource observations and freshness;
- [x] Facility and Provider revision/instance boundaries;
- [x] locality, reachability, readiness, health and pressure separation;
- [x] dispatch eligibility and dependency degradation;
- [x] migrations, fixtures, safety net and ADR-0021 series.

### WP05 — Workspace, Session, checkpoint and recovery

- [x] Workspace identity and immutable revisions;
- [x] membership, Provider binding and materialization;
- [x] Session attachment/control separation;
- [x] journal/outbox/cursor reconstruction;
- [x] checkpoint, restore compatibility and new-generation recovery;
- [x] export/import identity, authority and provenance;
- [x] migrations, fixtures, safety net and ADR-0022.

### WP06 — Transfer, synchronization, conflict, backup and restore

- [x] Transfer Request/Run/Attempt/Manifest/Progress/Verification;
- [x] resumable partial state and uncertain finalize handling;
- [x] synchronization, conflict and resolution records;
- [x] backup policy/snapshot/verification/prune/restore;
- [x] storage restore versus Workspace/application recovery;
- [x] migrations, fixtures, safety net and ADR-0023.

### WP07 — Recipe, Build, provenance, SBOM, signature and verification

- [x] Recipe/Revision/Proposal/Acceptance/Readiness boundaries;
- [x] backend-neutral Recipe versus Compiled Plan;
- [x] Build Run/Step and WP02 execution mapping;
- [x] inputs, outputs, cache, volatile data and secrets;
- [x] SBOM, attestation, signature, transparency and trust policy;
- [x] proof bundles, reproduction and comparison;
- [x] migrations, fixtures, safety net and ADR-0024.

### WP08 — Domain Pack, firmware, disk, filesystem and Device

- [x] Domain Pack identity/revision/capability/compatibility;
- [x] detector observations, inventory, decomposition and coverage;
- [x] firmware Package/Manifest/Component and compatibility;
- [x] disk image, partitions, filesystem and mount-session boundaries;
- [x] Device, Interface, connection epoch, Session, Stream and Screen Context;
- [x] Lease/fencing, backup, authorization, operation and verification;
- [x] uncertain physical outcomes and recovery;
- [x] catalog `0.1.2`, fixtures, safety net and ADR-0025/0025A.

### WP09 — Application, Browser, semantic UI and Shell

- [x] Application install/instance/session/process/window/display boundaries;
- [x] Browser profile/process/context/page/frame/navigation/download/challenge;
- [x] semantic Snapshot/Selector/Target/Action/Result and stale-target rejection;
- [x] human/automation control transfer using canonical Leases;
- [x] Shell views/panels/layouts and responsive projections;
- [x] 51 schemas, 18 lifecycle machines and 92 conformance cases;
- [x] migration, safety net and ADR-0026.

### WP10 — Knowledge, Data, Package and Plugin

- [x] Source/Revision/Segment/Index/Query/Result/Citation/Generated Output;
- [x] Dataset, processing, database reference/snapshot and export;
- [x] Package/Revision/Manifest/Constraint/Resolved Graph/Lock/Installation;
- [x] Plugin installation/activation/instance/health/grant/update/rollback/removal;
- [x] 50 schemas, nine lifecycle machines and 54 conformance cases;
- [x] migration, safety net and ADR-0027.

### WP11 — Isolation, placement, reservation, Lease and secure grants

- [x] isolation policy versus runtime realization;
- [x] placement, capacity, reservation, consumption and admission;
- [x] preemption, eviction and migration;
- [x] canonical Lease/fence projections;
- [x] secure grants, secret delivery/cleanup and bounded exposure;
- [x] 28 schemas, seven lifecycle machines and 36 conformance cases;
- [x] migration, safety net and ADR-0028.

### WP12 — Security, Finding, Claim, Evidence and reproduction

- [x] Observation, Finding, Claim and Evidence boundaries;
- [x] validation, review, dispute, accepted risk and disclosure;
- [x] remediation, patch application and independent post-fix verification;
- [x] reproduction protocol/request/run/comparison;
- [x] failed, negative and inconclusive evidence retention;
- [x] 19 schemas, five lifecycle machines and 40 conformance cases;
- [x] migration, safety net and ADR-0029.

### WP13 — Executable cross-contract conformance

- [x] offline Python harness;
- [x] JSON Schema meta-validation and local reference resolution;
- [x] catalog, URN, lifecycle and fixture validation;
- [x] semantic rule engine and migration execution contracts;
- [x] exact-head workflow and immutable report upload;
- [x] real WP03/WP06/WP08 defects found and corrected;
- [x] exact-head unit, structural and semantic gates passed;
- [x] ADR-0030 accepted.

Merged at:

`261b3e4a71657898643271a1625e14560a5bc769`

### WP14 — Golden/negative corpus and proof-plan freeze

- [x] stable Corpus and immutable Corpus Revision;
- [x] Fixture Manifest, Admission, Expected Proof and Freeze Decision;
- [x] lawful source, digest, licence, audience and privacy metadata;
- [x] executable paired positive/negative semantic corpus;
- [x] first vertical-slice proof plan;
- [x] exact-head WP13 conformance passed;
- [x] ADR-0031 accepted.

Merged at:

`fef387c4f074af7fcf86f2d99f7f9b7637e91f88`

## Phase 0B freeze gates

- [x] all schemas versioned and locally traceable;
- [x] lifecycle machines explicit and namespaced;
- [x] saved-record migration paths defined;
- [x] permissions, audience, privacy and redaction represented;
- [x] Provider/Facility replacement boundaries defined;
- [x] lawful positive/negative fixtures pinned;
- [x] proof plans name exact Receipts/Evidence;
- [x] backend replacement testable at contract level;
- [x] online and later local Nodes share the same public contracts;
- [x] private THETECHGUY knowledge absent from public contract identity;
- [x] WP13 executable conformance passed;
- [x] WP14 proof burden frozen;
- [x] ADR-0032 accepted and Phase 0B frozen.

---

# Phase 0C — First vertical-slice approval

**Status:** ACTIVE — RUNTIME IMPLEMENTATION NOT AUTHORIZED

## Completed preparation

- [x] Phase 0B freeze and Phase 0C entry decision;
- [x] implementation repository selected: `jaydumisuni/Ptah-space`;
- [x] Ubuntu Server 24.04.4 amd64 installation source digest pinned;
- [x] mandatory Linux Node capability profile defined;
- [x] first-slice package/source layout selected;
- [x] 17 non-publishable Rust scaffold package boundaries merged;
- [x] Rust `1.97.1` scaffold toolchain locked;
- [x] zero-third-party-dependency Rust scaffold `Cargo.lock` reviewed;
- [x] private Browser scaffold pinned to Node.js `24.18.0` and Playwright `1.60.0`;
- [x] external backend/tool candidate versions and licence boundaries recorded;
- [x] T00–T13 mapped to WP14 P01–P15 and N01–N12;
- [x] GitHub Actions pinned to immutable commits;
- [x] exact-head source-policy, Rust and Browser scaffold jobs passed;
- [x] frozen WP13 unit, structural and semantic conformance passed from `Ptah-space`;
- [x] four digest-addressed CI artifacts retained;
- [x] scaffold and CI evidence review passed;
- [x] control book advanced to 0C-05.

Implementation scaffold commits:

- package/layout scaffold: `ff26fa93d1b60781b49f33f5d1758680e1282d5f`;
- exact-head tested hardening head: `900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`;
- hardening merge: `23fc97ff0acd2b219990411ec4fb84d8a8c0a567`;
- passing workflow run: `29717942201`.

## Active and blocked conditions

- [?] owner public licence and contribution-boundary decision;
- [-] minimal runtime Rust crate/features selection;
- [ ] amended runtime `Cargo.lock` and crate licence/advisory evidence;
- [ ] admitted Ubuntu Node kernel/package/capability evidence;
- [ ] exact SQLite/containerd/runc/Git/libarchive installed versions and digests;
- [ ] Playwright Chromium executable digest and notices;
- [ ] durable retention of final Phase 0C proof bundle;
- [ ] final Phase 0C consistency review;
- [ ] ADR-0033 accepted;
- [ ] `CURRENT_STATE.md` changed to `Runtime implementation: AUTHORIZED`.

## Authorization rule

- [x] scaffold work remains non-claiming;
- [x] no production Node/Provider/Workspace deployed;
- [x] no public licence claimed before owner acceptance;
- [x] no runtime third-party Rust crates accepted by implication;
- [x] WP14 proof burden remains unchanged;
- [x] WP13 conformance remains mandatory;
- [ ] runtime implementation authorization merged.

---

# Implementation phases

No implementation phase may be ticked before Phase 0C authorization.

- [ ] Phase 1 — Concurrent one-Node substrate.
- [ ] Phase 2 — Intake and transfer.
- [ ] Phase 3 — Universal decomposition.
- [ ] Phase 4 — Firmware, disks and filesystems.
- [ ] Phase 5 — Git, containers, environments and Builds.
- [ ] Phase 6 — Browser and live web.
- [ ] Phase 7 — Human Workspace shell.
- [ ] Phase 8 — Session Vault.
- [ ] Phase 9 — Applications and devices.
- [ ] Phase 10 — Knowledge, data, search, Recipes and Plugins.
- [ ] Phase 11 — Provenance and security workloads.
- [ ] Phase 12 — Distributed Ptah.
- [ ] Phase 13 — OS readiness.