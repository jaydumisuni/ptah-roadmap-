# AI Start Here — Ptah

You are continuing the Ptah Space project.

Do not answer from chat memory alone. Recover the project from this repository before proposing, designing, editing, proving or building anything.

## Required reading order

1. `planning/A03-LEDGER-SCHEMA-MIGRATIONS-ACCEPTANCE.md`
2. `planning/A02-NODE-IDENTITY-GENERATION-HOST-TRUTH-ACCEPTANCE.md`
3. `planning/A01-REPOSITORY-CONTRACTS-SCAFFOLD-ACCEPTANCE.md`
4. `master-plan-index-amendment-2026-08-15.json`
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

The 2026-08-15 P01D closure, A01 acceptance, 2026-08-16 A02 acceptance, 2026-08-16 A03 acceptance and machine amendment are current authority. Older records remain historical provenance and must not be rewritten into false passes.

## Current position

- Ptah architecture: accepted planning baseline.
- Phase 0C P01D: **ACCEPTED / COMPLETE**.
- Physical development host: **accepted for Ptah development**.
- Runtime implementation: **AUTHORIZED**.
- A01 — Repository, contracts and reproducible scaffold: **FROZEN / PROVEN / COMPLETE**.
- A02 — Node identity, Generation and host truth: **FROZEN / PROVEN / COMPLETE**.
- A03 — Ledger, schema versions and crash-safe migrations: **FROZEN / PROVEN / COMPLETE**.
- A03 exact candidate: `19d390e22807a8540c7c4c5c3a94a37b93f5e3be`.
- A03 merge: `da35986327010cba575093d905875ee966e3d755`.
- A03 physical proof: `0000-ptah-a03-pass-b-physical-proof-20260816-1528z` via `oracle.live.v1`; proof manifest SHA-256 `26d684fb63e36b159e5a83c373bcd3a02dee04e893e00e282ae60b1cf400f861`.
- A03 proof results: rustfmt PASS; scoped Clippy `-D warnings` PASS; ledger 19/19; crash/recovery 4/4; complete workspace tests PASS; checksum-bound direct test binaries PASS against native SQLite.
- A03 independent Sergeant review: PASS / APPROVE, 0 admitted findings, 0 unresolved assurances; packet SHA-256 `520f82f371e3a0b39183044ead54331542d82ea85c27ee2226496e23a8256ad5`.
- Active work unit: **A04 — Activity, Operation, Attempt, Event and Receipt runtime**.
- A04 status: **READY**.
- P01P Prime-native integration proof: **OPEN / DEFERRED**; it does not block Programme A development.
- Prime-native deployment qualification: **not claimed**.
- Production/release acceptance: **not claimed**.
- Public implementation repo: `jaydumisuni/Ptah-space`.
- Detailed roadmap and authorization repo: this repository.

## A03 accepted evidence

A03 promotes only the repository-owned persistence substrate. It does not pull A04 Activity execution, A05 PTY/process, Workspace/Object work, Prime-native integration or production authorization forward.

Retained proof:

```text
Ptah-space PR: #25
candidate: 19d390e22807a8540c7c4c5c3a94a37b93f5e3be
merge: da35986327010cba575093d905875ee966e3d755
Oracle Pass B: 0000-ptah-a03-pass-b-physical-proof-20260816-1528z
receipt blob: dd78ee595abfec5a96250f060505df8e5d19765b
proof manifest: 26d684fb63e36b159e5a83c373bcd3a02dee04e893e00e282ae60b1cf400f861
Kratos: ledger 19/19; crash/recovery 4/4; full workspace PASS
Sergeant packet: 520f82f371e3a0b39183044ead54331542d82ea85c27ee2226496e23a8256ad5 — PASS / 0 admitted / 0 unresolved
```

A03 proved canonical record persistence, frozen schema registration, deterministic directional migrations, fail-closed incompatible state, transaction rollback, committed WAL recovery after abrupt process death, checkpoint policy, canonical query boundaries, and isolation of Ptah identity from SQLite row identity.

A03-specific GitHub Actions runtime-proof workflows were removed before freeze. Its physical proof authority is the Oracle MCP/RPC receipt and checksum-bound Pass B evidence.

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

Begin **A04 — Activity, Operation, Attempt, Event and Receipt runtime**.

Before implementation:

1. recover A04 requirements from `IMPLEMENTATION_ROADMAP.md`, P0C-I004 and frozen WP02, WP04, WP11 and WP12 contracts;
2. inspect the current `ptah-activity-runtime`, `ptah-events`, `ptah-receipts`, A03 ledger boundary and A02 identity/Generation primitives before adding code;
3. implement independent Activity, Operation and Attempt lifecycle engines without collapsing their identities;
4. add the Activity registry and scheduling queue with bounded concurrency and failure isolation;
5. implement retry, scoped cancellation and failure propagation so retry always creates a new Attempt;
6. stream Events and generate immutable Receipts without treating acknowledgement as completion;
7. support caller-defined Recipe/Plan worker formations, declared independent verification lanes, checkpoints, partial results and visible conflicts;
8. preserve Policy authority for retries and any effectful continuation; diagnostics may advise but may not self-start work;
9. prove at least ten independent Activities can run concurrently and one failure does not collapse unrelated work;
10. prove reused Attempt identity fails, acknowledgement-only completion fails, failed/cancelled work remains queryable, and cancellation stays scoped;
11. prove the caller-selected two-human-equivalent ten-for-two Recipe creates twenty bounded worker slots without silently collapsing verifier independence;
12. prove conflicting worker outputs remain visible and worker completion cannot become result acceptance;
13. freeze an exact candidate only after independent review is clean, then prove those exact bytes through the accepted MCP/RPC host path before merge.

A05 PTY/process execution, A06 Workspace persistence, P01P Prime-native integration and production/release acceptance remain out of A04 scope.

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
