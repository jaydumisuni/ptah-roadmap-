# Ptah Current State

**Last updated:** 2026-07-20  
**Overall status:** PHASE 0B FROZEN — PHASE 0C ACTIVE  
**Current phase:** Phase 0C — implementation selection, licensing, repository layout and authorization  
**Active work unit:** 0C-01 — first vertical-slice implementation selection  
**Runtime implementation:** NOT AUTHORIZED  
**Production dependency/backend selection:** IN REVIEW  
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

## Active Phase 0C decisions

Phase 0C must complete all of the following before implementation authorization:

1. select and pin the Linux host baseline;
2. select the public Ptah licence and contribution boundary;
3. approve the implementation repository and source layout;
4. select the exact first implementations behind the frozen neutral contracts;
5. approve the first vertical-slice delivery plan;
6. bind that plan to the WP14 proof plan and WP13 exact-head conformance;
7. record explicit implementation authorization in this file.

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
- pinned dependency evaluation;
- build scaffolding that does not claim runtime completion;
- executable proof-plan preparation;
- contract-conformance maintenance.

Not yet allowed:

- claiming the Ptah runtime or UI is implemented;
- deploying production Nodes, Providers or Workspaces;
- selecting a backend without a pinned licence/exit record;
- weakening the frozen WP14 proof burden;
- bypassing WP13 conformance;
- reusing donor source outside its accepted licence and extraction boundary.

Implementation becomes authorized only when a Phase 0C acceptance ADR and an explicit `Runtime implementation: AUTHORIZED` entry are merged into this file.

---

## Immediate continuation order

1. Read `decisions/ADR-0032-PHASE-0B-FREEZE-PHASE-0C-ENTRY.md`.
2. Read `work-packages/PHASE-0B-FREEZE-READINESS-REVIEW.md`.
3. Read `conformance/phase-0b/WP14-FIRST-VERTICAL-SLICE-PROOF-PLAN.md`.
4. Produce the Phase 0C Linux, licence, layout and backend-selection record.
5. Run exact-head conformance on any contract-affecting change.
6. Do not start runtime implementation until authorization is explicitly merged here.
