# Ptah Current State

**Last updated:** 2026-07-20  
**Overall status:** PHASE 0B FROZEN — PHASE 0C ACTIVE  
**Current phase:** Phase 0C — implementation selection, licensing, repository layout and authorization  
**Active work unit:** 0C-02 — frozen-contract lock, generated bindings, runtime dependency evidence and host capability proof  
**Runtime implementation:** NOT AUTHORIZED  
**Production dependency/backend selection:** CANDIDATE SET RECORDED — FINAL EVIDENCE OPEN  
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

## Phase 0C candidate decisions now recorded

The following records are merged:

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`;
- `work-packages/PHASE-0C-02-HOST-BASELINE-PIN.md`;
- `work-packages/PHASE-0C-03-DIRECT-DEPENDENCY-LICENCE-RECORD.md`;
- `work-packages/PHASE-0C-04-SOURCE-LAYOUT-AND-BOUNDARY-ACCEPTANCE.md`;
- `work-packages/PHASE-0C-05-WP14-IMPLEMENTATION-TASK-AND-PROOF-MAP.md`;
- `work-packages/PHASE-0C-06-CI-EXACT-HEAD-ACCEPTANCE-GATE.md`;
- `work-packages/PHASE-0C-07-REAL-WORKLOAD-CANDIDATE-REGISTRY.md`;
- `work-packages/PHASE-0C-08-NONCLAIMING-SCAFFOLD-EVIDENCE-REVIEW.md`;
- `work-packages/PHASE-0C-09-IMMUTABLE-ACTION-AND-FROZEN-CONFORMANCE-EVIDENCE.md`;
- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.

Selection/evidence merge before the latest hardening:

```text
79e83be0c340e871521d574719cdf6d20d52f4c9
```

### Candidate first-slice baseline

- Ubuntu Server 24.04.4 LTS amd64 image pinned by SHA-256;
- Noble GA 6.8 generic kernel line;
- Rust `1.97.1` primary Node/control toolchain;
- SQLite `3.53.3` behind a repository-owned ledger boundary;
- native Linux PTY/process supervision;
- containerd `2.3.1` with runc `1.4.2` behind an OCI Provider boundary;
- Node.js `24.18.0`, Playwright `1.60.0` and its pinned Chromium build for the first Browser Provider;
- hardened Git `2.55.0` process adapter;
- libarchive `3.8.7` first decomposition adapter;
- repository-owned resumable transfer and local content-addressed storage;
- Apache License 2.0 as the proposed public Ptah-owned source licence, pending owner acceptance.

Concrete tools remain replaceable backends. They may not redefine canonical Ptah identity, lifecycle or proof. Backend IDs remain Aliases.

---

## Merged non-claiming implementation scaffold

`jaydumisuni/Ptah-space` contains a Phase 0C scaffold merged at:

```text
ff26fa93d1b60781b49f33f5d1758680e1282d5f
```

The initial exact tested scaffold head:

```text
2f1fcedaa398254e5fa4b82583675a08755fa953
```

passed workflow run `29717770393` for:

- the explicit no-build boundary;
- Rust `1.97.1` formatting, Clippy and workspace tests;
- locked Browser Provider npm installation, syntax and tests.

The evidence-hardening head:

```text
900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc
```

passed workflow run `29717942201` for:

- exact pull-request-head source-policy/no-build checks;
- Rust formatting, Clippy, tests and locked metadata;
- Browser locked installation, syntax, tests and dependency inventory;
- frozen WP13 unit, structural and semantic conformance using local files;
- per-lane report retention under immutable Action commit pins.

The hardening merged at:

```text
23fc97ff0acd2b219990411ec4fb84d8a8c0a567
```

The scaffold contains package boundaries, locks and CI only. It is not a Ptah runtime.

---

## Active Phase 0C blockers

Implementation remains unauthorized until all of the following are merged and reviewed:

1. owner acceptance of the Apache-2.0 public/private boundary;
2. final public `LICENSE`, `NOTICE`, contribution and security boundary;
3. exact external Rust crate, system package and binary/source locks with hashes/signatures, licence inventory and advisory review;
4. complete frozen public catalog inventory in `Ptah-space/contracts/upstream-lock.json` by path, URN and digest;
5. reproducible offline generated bindings and output-tree digest;
6. an implemented host capability collector and a real report from the pinned host image revision;
7. CI for dependency policy and frozen-contract generation at the exact candidate commit;
8. durable retention of final Phase 0C evidence beyond temporary CI artifact expiry;
9. a Phase 0C closure review proving no frozen contract was weakened;
10. acceptance of ADR-0033;
11. explicit `Runtime implementation: AUTHORIZED` in this file in the same reviewed closure change.

The source-policy, Rust, Browser and frozen-WP13 scaffold lanes are now complete. They do not close dependency policy, binding generation, real host evidence or WP14 runtime proofs.

### Required first vertical slice after authorization

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

---

## No-build boundary

Allowed during the remainder of Phase 0C:

- licence and contribution decisions;
- exact dependency and host evidence;
- frozen catalog locking and generated bindings;
- non-claiming repository/CI scaffolding;
- executable proof-plan preparation;
- WP13 integration and contract-conformance maintenance;
- Phase 0C closure review.

Not yet allowed:

- claiming the Ptah runtime or UI is implemented;
- deploying production Nodes, Providers or Workspaces;
- adding runtime functionality under the name of scaffolding;
- weakening the frozen WP14 proof burden;
- bypassing WP13 conformance;
- reusing donor source outside its accepted licence and extraction boundary;
- authorizing implementation without the accepted ADR and exact evidence.

Implementation becomes authorized only when a Phase 0C acceptance ADR and an explicit `Runtime implementation: AUTHORIZED` entry are merged into this file.

---

## Immediate continuation order

1. Populate and verify the frozen public catalog lock in `Ptah-space`.
2. Generate Rust contract bindings offline and record input/output digests.
3. Select the minimal external Rust crate set and produce exact licence/advisory evidence.
4. Implement and run the host capability collector on the pinned image revision.
5. Add dependency-policy and frozen-contract-generation evidence to `Ptah-space` CI.
6. Persist final acceptance evidence in a durable Location.
7. Complete the Apache-2.0 owner decision and public/private notice boundary.
8. Conduct the Phase 0C closure review.
9. Accept ADR-0033 and authorize runtime only if every blocker passes.