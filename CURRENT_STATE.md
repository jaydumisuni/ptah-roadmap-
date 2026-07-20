# Ptah Current State

**Last updated:** 2026-07-20  
**Overall status:** PHASE 0B FROZEN — PHASE 0C ACTIVE  
**Current phase:** Phase 0C — implementation selection, licensing, repository layout and authorization  
**Active work unit:** 0C-05 — runtime dependency and installed-environment closure  
**Runtime implementation:** NOT AUTHORIZED  
**Production dependency/backend selection:** PARTIALLY PINNED — ACCEPTANCE INCOMPLETE  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

## Frozen checkpoints

### Phase 0A donor and requirement closure

Frozen checkpoint:

```text
7d2dffee48f1400ba1cf88823343f09a3895ad33
```

Decision:

- `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`

### Phase 0B contract and proof closure

Phase 0B is frozen by:

- WP01 through WP14 candidate packages;
- exact local schema catalogs and namespaced lifecycle machines;
- directional migration and backend-replacement rules;
- positive, negative and adversarial fixtures;
- the offline WP13 structural and semantic conformance harness;
- the WP14 lawful golden/negative corpus and first vertical-slice proof plan;
- `work-packages/PHASE-0B-FREEZE-READINESS-REVIEW.md`;
- `decisions/ADR-0032-PHASE-0B-FREEZE-PHASE-0C-ENTRY.md`.

Freeze merge:

```text
dc2db457f1705d0cba80f17ab76e5e93f808aee0
```

WP13 and WP14 exact-head workflows passed unit, structural and semantic conformance before merge. Contract changes after this checkpoint require a versioned schema/lifecycle change, migration, fixtures, conformance evidence and a reopening ADR.

---

## Completed Phase 0B packages

1. WP01 — Common identity, versioning and typed families
2. WP02 — Activity, Operation, Attempt, Event, Receipt and proof
3. WP03 — Object, Revision, View, Artifact and storage
4. WP04 — Node, Facility, Provider, capability and health
5. WP05 — Workspace, Session, checkpoint, restore and recovery
6. WP06 — Transfer, synchronization, conflict, backup and restore
7. WP07 — Recipe, Build, provenance, SBOM, signature and verification
8. WP08 — Domain Pack, firmware, disk, filesystem and Device
9. WP09 — Application, Browser, semantic UI and Shell
10. WP10 — Knowledge, Data, Package and Plugin
11. WP11 — Isolation, placement, reservation, Lease and secure grants
12. WP12 — Security, Finding, Claim, Evidence, remediation and reproduction
13. WP13 — executable cross-contract conformance
14. WP14 — golden/negative corpus and proof-plan freeze

These packages define implementation boundaries. They are not evidence that the Ptah runtime already exists.

---

## Phase 0C preparation completed

The following preparation work is complete without authorizing runtime implementation:

### Host and first-slice plan

- Ubuntu Server 24.04.4 LTS amd64 installation source is pinned by SHA-256;
- the mandatory Node capability/admission profile is defined;
- the first-slice task graph maps T00–T13 to WP14 positive proofs P01–P15 and negative proofs N01–N12;
- backend replacement, exact-head evidence and offline conformance remain mandatory.

### Implementation repository and layout

The broader non-claiming `Ptah-space` scaffold is merged at:

```text
ff26fa93d1b60781b49f33f5d1758680e1282d5f
```

It establishes:

- 17 non-publishable Rust package boundaries;
- Rust `1.97.1` and edition 2024;
- no third-party Rust dependencies in the scaffold lock;
- a private Browser scaffold pinned to Node.js `24.18.0` and Playwright `1.60.0`;
- no-build, incomplete-contract-lock and no-private-gateway guards;
- no claim that any Node, Workspace, Activity, Provider or UI runtime exists.

### Exact-head CI and frozen conformance

Evidence-hardening was tested at exact head:

```text
900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc
```

Workflow run:

```text
29717942201
```

Passed lanes:

- source-policy/no-build boundary;
- Rust formatting, Clippy, tests and locked metadata;
- Browser locked installation, syntax, tests and dependency inventory;
- frozen WP13 harness unit, structural and semantic conformance.

The hardening merged at:

```text
23fc97ff0acd2b219990411ec4fb84d8a8c0a567
```

GitHub Actions are pinned to immutable commits, and all four lanes retained digest-addressed artifacts. Runtime authorization remained false.

---

## Active Phase 0C decisions

### Completed or candidate-complete

1. Linux installation source and host capability profile — candidate complete.
2. Public implementation repository and source layout — complete.
3. First vertical-slice delivery/task graph — candidate complete.
4. Binding to WP14 proof cases and frozen WP13 conformance — complete for scaffold preparation.
5. External backend/tool candidates — version and licence boundaries recorded.
6. Scaffold Rust and Browser package locks — reviewed.
7. Immutable GitHub Action pins and exact-head evidence — complete.

### Still required before implementation authorization

1. owner decision on the public Ptah licence and contribution boundary;
2. minimal runtime Rust crate/features graph and amended `Cargo.lock`;
3. crate licence and advisory acceptance;
4. exact installed Ubuntu kernel/package inventory and mandatory capability-probe evidence;
5. exact installed SQLite, containerd, runc, Git and libarchive versions/digests;
6. Playwright Chromium installation, executable digest and notices;
7. durable retention of final Phase 0C evidence beyond temporary CI artifact retention;
8. final Phase 0C consistency review;
9. accepted ADR-0033 or successor;
10. explicit implementation authorization in this file.

### Required first vertical slice

The first authorized slice must demonstrate, at minimum:

- one Linux Node;
- one persistent Workspace;
- canonical Object registration;
- concurrent Activities and multiple terminals;
- upload and resumable download;
- Git clone or mirror;
- one container execution path;
- one interactive Browser path;
- one decomposition adapter;
- Artifact registration;
- checkpoint, restart and reconnect;
- exact Receipts, generation evidence and negative-path retention.

### Selection rule

Concrete tools are replaceable backends. They may not redefine canonical Ptah identity, lifecycle or proof. Backend IDs remain Aliases. A selected dependency must have a pinned version, licence decision, integration boundary, replacement strategy and proof cases.

---

## No-build boundary

Allowed during Phase 0C:

- implementation-selection ADRs;
- licence and contribution decisions;
- source/repository layout;
- pinned dependency evaluation and lock generation;
- non-claiming package scaffolding;
- host/backend installation evidence preparation;
- executable proof-plan preparation;
- contract-conformance maintenance.

Not yet allowed:

- implementing or claiming the Ptah runtime or UI;
- deploying production Nodes, Providers or Workspaces;
- adding runtime dependencies without the reviewed lock/licence boundary;
- selecting a backend without pinned licence/exit evidence;
- weakening the frozen WP14 proof burden;
- bypassing WP13 conformance;
- reusing donor source outside its accepted licence and extraction boundary.

Implementation becomes authorized only when a Phase 0C acceptance ADR and an explicit `Runtime implementation: AUTHORIZED` entry are merged into this file.

---

## Immediate continuation order

1. Read `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.
2. Read `work-packages/PHASE-0C-SELECTION-CLOSURE-STATUS.md`.
3. Read `work-packages/PHASE-0C-04-SCAFFOLD-AND-CI-EVIDENCE-REVIEW.md`.
4. Define and review the minimal runtime Rust dependency candidates and features.
5. Prepare exact host/backend/browser installation and digest evidence procedures.
6. Obtain the owner licence/contribution decision.
7. Conduct final Phase 0C review.
8. Do not start runtime implementation until authorization is explicitly merged here.