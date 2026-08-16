# AI Start Here — Ptah

You are continuing the Ptah Space project.

Do not answer from chat memory alone. Recover the project from this repository before proposing, designing, editing, proving or building anything.

## Required reading order

1. `planning/A02-NODE-IDENTITY-GENERATION-HOST-TRUTH-ACCEPTANCE.md`
2. `master-plan-index-amendment-2026-08-16.json`
3. `planning/A01-REPOSITORY-CONTRACTS-SCAFFOLD-ACCEPTANCE.md`
4. `master-plan-index-amendment-2026-08-15.json` for the preceding A01 checkpoint
5. `CURRENT_STATE_CLOSURE_2026-08-15.md`
6. `decisions/ADR-0039-P01D-ACCEPTANCE-A01-AUTHORIZATION.md`
7. `decisions/ADR-0038-PRIME-HOST-DEVELOPMENT-QUALIFICATION.md`
8. `CURRENT_STATE_AMENDMENT_2026-08-15.md` for the preceding P01D state
9. `CURRENT_STATE.md` for preserved historical context
10. `MASTER_PLAN.md`
11. `IMPLEMENTATION_ROADMAP.md`
12. `MASTER_ROADMAP.md`
13. `PROGRESS_AMENDMENT_2026-08-15.md`
14. `PROGRESS.md`
15. `DECISIONS.md` and `DECISIONS_AMENDMENT_2026-08-15.md`
16. `MEMORY_PROTOCOL.md`
17. `DONOR_RECOVERY.md`
18. `REQUIREMENT_CLOSURE_MATRIX.md`
19. `WORK_ITEM_TEMPLATE.md`
20. current source and public-safe technical documentation in `jaydumisuni/Ptah-space`
21. any donor or internal repository directly related to the selected work item

The 2026-08-16 A02 acceptance is current implementation authority. The 2026-08-15 P01D closure and A01 acceptance remain accepted historical prerequisites. Older records remain provenance and must not be rewritten into false passes.

## Current position

- Ptah architecture: accepted planning baseline.
- Phase 0C P01D: **ACCEPTED / COMPLETE**.
- Physical development host: **accepted for Ptah development**.
- Runtime implementation: **AUTHORIZED**.
- A01 — Repository, contracts and reproducible scaffold: **FROZEN / PROVEN / COMPLETE**.
- A01 merge: `d33122c8cc625d38f2394d57fcbd2a3ef7027b08`.
- A02 — Node identity, Generation and host truth: **FROZEN / PROVEN / COMPLETE**.
- A02 exact candidate: `80adcd0aefe0053b2354b26676bfc9e28d9b8ec3`.
- A02 merge: `1603ac80b5d2c5925fde62392ec0fff4b07a1219`.
- A02 exact-head workflow run: `31909732507` — all 13 repository workflows PASS.
- A02 Kratos physical proof: **PASS** — 9/9 identity tests and 17/17 node-agent tests.
- A02 independent Sergeant review: **PASS / 0 blocking / 0 needs-work**.
- Active work unit: **A03 — Ledger, schema versions and crash-safe migrations**.
- A03 status: **READY**.
- P01P Prime-native integration proof: **OPEN / DEFERRED**; it does not block Programme A development.
- Prime-native deployment qualification: **not claimed**.
- Production/release acceptance: **not claimed**.
- Public implementation repo: `jaydumisuni/Ptah-space`.
- Detailed roadmap and authorization repo: this repository.

## A02 accepted evidence

A02 implemented only the roadmap-authorized Node identity/Generation/host-truth slice on top of the accepted A01 scaffold.

Retained proof:

```text
Ptah-space PR: #24
candidate: 80adcd0aefe0053b2354b26676bfc9e28d9b8ec3
candidate tree: 9b477dc1bf9ab2dd466da9615dbbd0e881216ed6
merge: 1603ac80b5d2c5925fde62392ec0fff4b07a1219
workflow run: 31909732507
exact-head artifact: 9253318003
artifact digest: sha256:dbafc252ab2fb3e2eb9938de6648bca0105f698d27321be9eb2bdb1a3782ba0a
Oracle physical receipt: 0000-ptah-a02-kratos-physical-proof-20260816-013450z
Oracle transport: oracle.live.v1
Sergeant reviewer: 56961f12e5cc97cde447e5150e7a00ef3a8deba8
Sergeant verdict: PASS
```

A02 proves canonical lowercase UUIDv7 identity, validated identity/revision boundaries, Generation and connection-epoch fencing, restart-seed semantics, stale-generation rejection with evidence, evidence-bound health/capability/resource/worker-capacity projection, overflow fail-closed behavior and bounded advisory no-auto-upgrade semantics.

A02 does **not** claim ledger persistence, crash-safe migrations, Activity execution, Prime-native integration, production qualification or release acceptance.

## Accepted P01D proof boundary

The corrected physical development-host proof executed on Kratos through the existing Oracle Live MCP/RPC control path and was accepted before A01 began.

Private P01D execution evidence remains:

```text
receipt: 0000-ptah-p01d-final-kratos-proof-20260815-194730z
receipt blob: bf81cc24f7fce84d777da3c668b8716b475e8002
transport: oracle.live.v1
githubInteractivePathUsed: false
```

The public P01D report proves portable mechanics and exact clean repository binding. It deliberately keeps physical-host acceptance and runtime-authorization fields false because public evidence cannot accept itself. The private closure is the acceptance authority.

## Core identity

Ptah is an independent, open-source, online-first and later local-first concurrent digital working world.

Ptah provides the workplace, tools, files, internet, storage, terminals, browsers, containers, applications, firmware, devices, rendering, sessions and artifacts.

The human or compatible calling system supplies intent, reasoning, priorities, instructions, restrictions and acceptance criteria. Ptah is the world where work happens, not the intelligence deciding what work should happen.

Ptah stays OS-neutral. In the intended Prime deployment, Prime owns machine authority and Ptah consumes Prime-exposed capabilities through an explicit integration boundary.

```text
Prime Host ID != Ptah Node ID
```

## Host and integration rule

- Do not install or boot a second server OS solely for Ptah.
- Do not create a dedicated guest VM solely to satisfy the superseded host pin.
- Oracle/MCP/RPC is private control/evidence infrastructure, not a Ptah Core dependency.
- Keep public Ptah proof tooling provider-neutral; private machine/control topology stays outside public Ptah source.
- Preserve the old Ubuntu 24.04.4 / `6.8.0-136-generic` proof kit as historical evidence; do not claim it passed.
- Prime-owned isolation/resource mechanisms belong to the later P01P Prime-native capability proof.

## Mandatory rules

- Do not put the complete private roadmap into the public Ptah repository.
- Do not expose private consumers, machine names, private control topology or private operating-system integration publicly.
- Implement only roadmap-authorized work with satisfied dependencies.
- Recover existing internal work before recommending a rebuild.
- Inspect donors beyond README claims.
- Treat a workspace as persistent and capable of many concurrent activities.
- Treat files as structured objects with originals, children, derivatives, previews and provenance.
- Preserve live internet as a normal capability.
- Use fast local storage for active work and remote/object storage for durable copies and artifacts.
- Preserve `Prime Host ID != Ptah Node ID` and the Prime-machine/Ptah-mechanical authority split.
- Follow: Understand → Build → Review → Freeze → Prove → Submit/Ship.

## Exact next operation

Begin **A03 — Ledger, schema versions and crash-safe migrations**.

Before implementation:

1. recover A03 requirements from `IMPLEMENTATION_ROADMAP.md` and P0C-I003;
2. recover frozen WP01–WP06 schemas, lifecycle rules, migration requirements and conformance fixtures;
3. inspect existing `ptah-ledger`, generated bindings, persistence-related scaffolds and any retained Phase 0C storage evidence before adding code;
4. implement repository-owned ledger interfaces and SQLite WAL persistence without exposing backend row IDs as canonical identities;
5. implement entity/schema version registry and immutable numbered directional migrations;
6. enforce transactional writes, crash-safe checkpoint policy and deterministic migration replay;
7. reject incompatible migration/state combinations fail-closed;
8. preserve canonical A02 identity/Generation semantics across restart and persistence boundaries;
9. prove restart durability, interrupted-transaction safety, deterministic migration replay, incompatible-migration rejection and backend-ID non-leakage;
10. keep A04 Activity runtime out of scope;
11. merge only a frozen exact head after required workflows and independent review pass.

A04 Activity execution remains out of A03 scope. P01P remains open until Prime exposes the required machine Capability Interface.

## Before doing work

State:

1. recovered current phase;
2. exact roadmap item;
3. existing internal foundation;
4. donor evidence;
5. native Ptah gap;
6. dependencies;
7. public/private boundary;
8. proof plan;
9. whether build permission has been given.

## After approved work

Update current recovery/decision/progress authority without falsifying historical records. Do not ask the owner to repeat information recoverable from these sources.
