# AI Start Here — Ptah

You are continuing the Ptah Space project.

Do not answer from chat memory alone. Recover the project from this repository before proposing, designing, editing, proving or building anything.

## Required reading order

1. `planning/A02-NODE-IDENTITY-GENERATION-HOST-TRUTH-ACCEPTANCE.md`
2. `planning/A01-REPOSITORY-CONTRACTS-SCAFFOLD-ACCEPTANCE.md`
3. `master-plan-index-amendment-2026-08-15.json`
4. `CURRENT_STATE_CLOSURE_2026-08-15.md`
5. `decisions/ADR-0039-P01D-ACCEPTANCE-A01-AUTHORIZATION.md`
6. `decisions/ADR-0038-PRIME-HOST-DEVELOPMENT-QUALIFICATION.md`
7. `CURRENT_STATE_AMENDMENT_2026-08-15.md` for the preceding P01D state
8. `CURRENT_STATE.md` for preserved historical context
9. `MASTER_PLAN.md`
10. `IMPLEMENTATION_ROADMAP.md`
11. `MASTER_ROADMAP.md`
12. `PROGRESS_AMENDMENT_2026-08-15.md`
13. `PROGRESS.md`
14. `DECISIONS.md` and `DECISIONS_AMENDMENT_2026-08-15.md`
15. `MEMORY_PROTOCOL.md`
16. `DONOR_RECOVERY.md`
17. `REQUIREMENT_CLOSURE_MATRIX.md`
18. `WORK_ITEM_TEMPLATE.md`
19. current source and public-safe technical documentation in `jaydumisuni/Ptah-space`
20. any donor or internal repository directly related to the selected work item

The 2026-08-15 P01D closure, A01 acceptance, 2026-08-16 A02 acceptance and machine amendment are current authority. Older records remain historical provenance and must not be rewritten into false passes.

## Current position

- Ptah architecture: accepted planning baseline.
- Phase 0C P01D: **ACCEPTED / COMPLETE**.
- Physical development host: **accepted for Ptah development**.
- Runtime implementation: **AUTHORIZED**.
- A01 — Repository, contracts and reproducible scaffold: **FROZEN / PROVEN / COMPLETE**.
- A02 — Node identity, Generation and host truth: **FROZEN / PROVEN / COMPLETE**.
- A02 exact candidate: `80adcd0aefe0053b2354b26676bfc9e28d9b8ec3`.
- A02 merge: `1603ac80b5d2c5925fde62392ec0fff4b07a1219`.
- A02 exact-head workflow run: `31909732507` — all 13 repository workflows PASS.
- A02 proof artifact: `9253318003`, digest `sha256:dbafc252ab2fb3e2eb9938de6648bca0105f698d27321be9eb2bdb1a3782ba0a`.
- A02 physical Kratos proof: `ptah-identifiers` 9/9 and `ptah-node-agent` 17/17 PASS via `oracle.live.v1` with checksum-bound executables from the exact frozen source.
- A02 independent Sergeant review: exact review commit `56961f12e5cc97cde447e5150e7a00ef3a8deba8`, PASS, 0 blocking, 0 needs-work.
- Active work unit: **A03 — Ledger, schema versions and crash-safe migrations**.
- A03 status: **READY**.
- P01P Prime-native integration proof: **OPEN / DEFERRED**; it does not block Programme A development.
- Prime-native deployment qualification: **not claimed**.
- Production/release acceptance: **not claimed**.
- Public implementation repo: `jaydumisuni/Ptah-space`.
- Detailed roadmap and authorization repo: this repository.

## A02 accepted evidence

A02 promoted only the Node identity/Generation/host-truth runtime slice. It did not pull A03 persistence, A04 Activity execution, Prime-native integration or production authorization forward.

Retained proof:

```text
Ptah-space PR: #24
candidate: 80adcd0aefe0053b2354b26676bfc9e28d9b8ec3
merge: 1603ac80b5d2c5925fde62392ec0fff4b07a1219
workflow run: 31909732507
proof artifact: 9253318003
proof digest: sha256:dbafc252ab2fb3e2eb9938de6648bca0105f698d27321be9eb2bdb1a3782ba0a
Kratos: identifiers 9/9 PASS; node-agent 17/17 PASS
Sergeant: 56961f12e5cc97cde447e5150e7a00ef3a8deba8 — PASS, 0 blocking, 0 needs-work
```

A02 proved stable canonical UUIDv7 Ptah identity, validated entity-kind and record-revision primitives, bounded Generation/epoch handling, stale-generation rejection with Event/Receipt correlation, evidence-bound host health/capability/resource projections, worker-capacity evidence binding and non-self-authorizing diagnostic advisories.

## A01 accepted evidence

A01 exact candidate `d12feedb5b66a39d5649b1d3ffea752deb5692c6`, merge `d33122c8cc625d38f2394d57fcbd2a3ef7027b08`, workflow run `31906473232` and final proof artifact `9252486137` remain frozen historical acceptance evidence. A01 proved scaffold/contracts/reproducibility, not runtime semantics.

## Accepted P01D proof boundary

The corrected physical proof executed on Kratos through the existing Oracle Live MCP/RPC control path.

Private execution evidence:

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

1. recover A03 requirements from `IMPLEMENTATION_ROADMAP.md`, P0C-I003 and frozen WP01–WP06 contracts;
2. inspect the current `ptah-ledger`, `ptah-identifiers`, generated contracts and dependency locks so existing boundaries are extended rather than replaced;
3. implement repository-owned ledger interfaces and a SQLite WAL backend;
4. implement canonical entity/schema-version storage without exposing SQLite row IDs as Ptah identity;
5. implement immutable numbered directional migrations and fail closed on incompatible/newer schema versions;
6. make writes transactional and define an explicit WAL checkpoint policy;
7. keep queries behind repository-owned boundaries;
8. prove canonical records survive reopen/restart;
9. prove an interrupted/uncommitted write cannot manufacture success;
10. prove migration replay is deterministic and incompatible migration state fails closed;
11. freeze an exact candidate only after independent review is clean;
12. prove the exact frozen candidate in CI and on the accepted physical development host where the A03 runtime semantics require host evidence;
13. merge only the proved exact head.

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
