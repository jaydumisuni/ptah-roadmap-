# AI Start Here — Ptah

You are continuing the Ptah Space project.

Do not answer from chat memory alone. Recover the project from this repository before proposing, designing, editing, proving or building anything.

## Required reading order

1. `planning/A05-NATIVE-PROCESS-PTY-PROVIDER-ACCEPTANCE.md`
2. `planning/A04-ACTIVITY-OPERATION-ATTEMPT-RUNTIME-ACCEPTANCE.md`
3. `planning/A03-LEDGER-SCHEMA-MIGRATIONS-ACCEPTANCE.md`
4. `planning/A02-NODE-IDENTITY-GENERATION-HOST-TRUTH-ACCEPTANCE.md`
5. `planning/A01-REPOSITORY-CONTRACTS-SCAFFOLD-ACCEPTANCE.md`
6. `master-plan-index-amendment-2026-08-15.json`
7. `CURRENT_STATE_CLOSURE_2026-08-15.md`
8. `decisions/ADR-0039-P01D-ACCEPTANCE-A01-AUTHORIZATION.md`
9. `decisions/ADR-0038-PRIME-HOST-DEVELOPMENT-QUALIFICATION.md`
10. `CURRENT_STATE_AMENDMENT_2026-08-15.md` for the preceding P01D state
11. `CURRENT_STATE.md` for preserved historical context
12. `MASTER_PLAN.md`
13. `IMPLEMENTATION_ROADMAP.md`
14. `MASTER_ROADMAP.md`
15. `PROGRESS_AMENDMENT_2026-08-15.md`
16. `PROGRESS.md`
17. `DECISIONS.md` and `DECISIONS_AMENDMENT_2026-08-15.md`
18. `MEMORY_PROTOCOL.md`
19. `DONOR_RECOVERY.md`
20. `REQUIREMENT_CLOSURE_MATRIX.md`
21. `WORK_ITEM_TEMPLATE.md`
22. current source and public-safe technical documentation in `jaydumisuni/Ptah-space`
23. any donor or internal repository directly related to the selected work item

The accepted P01D closure plus A01, A02, A03, A04 and A05 acceptance records are current authority. Older records remain historical provenance and must not be rewritten into false passes.


## Current position

- Ptah architecture: accepted planning baseline.
- Phase 0C P01D: **ACCEPTED / COMPLETE**.
- Physical development host: **accepted for Ptah development**.
- Runtime implementation: **AUTHORIZED**.
- A01 — Repository, contracts and reproducible scaffold: **FROZEN / PROVEN / COMPLETE**.
- A01 exact candidate: `d12feedb5b66a39d5649b1d3ffea752deb5692c6`.
- A01 merge: `d33122c8cc625d38f2394d57fcbd2a3ef7027b08`.
- A01 exact-head workflow run: `31906473232`.
- A02 — Node identity, Generation and host truth: **FROZEN / PROVEN / COMPLETE**.
- A03 — Ledger, schema versions and crash-safe migrations: **FROZEN / PROVEN / COMPLETE**.
- A04 — Activity, Operation, Attempt, Event and Receipt runtime: **FROZEN / PROVEN / COMPLETE**.
- A04 exact candidate: `fad9029504258c773f5ab496c79cfceea17c0b5e`.
- A04 merge: `a63eb8f2c73f961b8466b844c6f194f2381a8139`.
- A04 freeze manifest SHA-256: `6d69f74a209e95ab7faa9ab7a543b247dfc00d170e9d0af5be0f573d4eb5aa1f`.
- A04 Pass B proof manifest SHA-256: `db3f3561b85de30c001ac405261d2507128cfd2a87687f955ac6a862f9ebfda1`.
- A04 SQLite supplement SHA-256: `bd65b89e5cc1180b96612b18901c530892d5b753123c5b1ea237a0bd8a1fb734`.
- A04 independent Sergeant review: **PASS / APPROVE**, 190 Tenfold private lanes, 0 admitted findings, 0 unresolved assurances; packet SHA-256 `8f471eee95374fcad509aff88b80be08b95eae22dd719934978feac70ddb53d4`.
- A04 physical proof transport: `oracle.live.v1`; `githubInteractivePathUsed: false`.
- A05 — Native process, PTY and multi-terminal Provider: **FROZEN / PROVEN / COMPLETE**.
- A05 exact candidate: `4be4f170219701841aca367dd98c7b746fdd444c`.
- A05 merge: `34bc4beed57517532a1d79ae64131835a395f7b2`.
- A05 freeze-quality receipt: `0000-ptah-a05-freeze-quality-20260817-0155z`.
- A05 frozen exact-head proof receipt: `0000-ptah-a05-frozen-proof-fast-20260817-0204z`.
- A05 independent Sergeant review: **PASS / APPROVE**, 150 Tenfold private lanes, 0 admitted findings, 0 unresolved assurances; packet SHA-256 `627074b11c36014d8f8c391bdbcecbb5130a68e0fbbe8151d8af03aa700b9061`.
- A05 physical proof transport: `oracle.live.v1`; `githubInteractivePathUsed: false`.
- Active work unit: **A06 — Persistent Workspace, Session and authority projection**.
- A06 status: **READY**.
- P01P Prime-native integration proof: **OPEN / DEFERRED**; it does not block Programme A development.
- Prime-native deployment qualification: **not claimed**.
- Production/release acceptance: **not claimed**.
- Public implementation repo: `jaydumisuni/Ptah-space`.
- Detailed roadmap and authorization repo: this repository.

## A05 accepted evidence

A05 promotes the native process/terminal Provider only. It does not pull A06 Workspace persistence, A07 Object/CAS work, Prime-native integration or production/release acceptance forward.

Retained proof:

```text
Ptah-space PR: #27
candidate: 4be4f170219701841aca367dd98c7b746fdd444c
merge: 34bc4beed57517532a1d79ae64131835a395f7b2
freeze-quality receipt: 0000-ptah-a05-freeze-quality-20260817-0155z
frozen exact-head proof receipt: 0000-ptah-a05-frozen-proof-fast-20260817-0204z
Tenfold final review packet: 627074b11c36014d8f8c391bdbcecbb5130a68e0fbbe8151d8af03aa700b9061
Tenfold private lanes: 150
transport: oracle.live.v1
githubInteractivePathUsed: false
Rust/Cargo: 1.97.1
Cargo.lock: cbcec35bac0fb9c08782390e28398d0f451cbd97e35381ee418f66574c6e4f0e
portable-pty 0.9.0 checksum: b4a596a2b3d2752d94f51fac2d4a96737b8705dddd311a32b9af47211f08671e
```

A05 proved Provider Revision/Instance/Generation binding; PID-as-alias semantics; independent pipe stdout/stderr; truthful merged PTY-stream limitation; input/resize; durable detach/reconnect; Policy-required disconnect termination; stale attachment/lease fencing; visible stream sequence/truncation; several independent PTYs; independent exit observation; and exact A04 Attempt-context binding.

A05 runtime execution/proof authority is Oracle MCP/RPC. GitHub Actions are not the A05 runtime proof path.

## A04 accepted evidence

A04 promotes the orchestration/proof substrate only. It does not pull A05 process/PTY execution, A06 Workspace persistence, Prime-native integration or production/release acceptance forward.

Retained proof:

```text
Ptah-space PR: #26
candidate: fad9029504258c773f5ab496c79cfceea17c0b5e
merge: a63eb8f2c73f961b8466b844c6f194f2381a8139
freeze manifest: 6d69f74a209e95ab7faa9ab7a543b247dfc00d170e9d0af5be0f573d4eb5aa1f
Pass B proof manifest: db3f3561b85de30c001ac405261d2507128cfd2a87687f955ac6a862f9ebfda1
SQLite supplement: bd65b89e5cc1180b96612b18901c530892d5b753123c5b1ea237a0bd8a1fb734
Tenfold final review packet: 8f471eee95374fcad509aff88b80be08b95eae22dd719934978feac70ddb53d4
Tenfold private lanes: 190
transport: oracle.live.v1
githubInteractivePathUsed: false
Rust/Cargo: 1.97.1
SQLite static archive: c1978ab409aa5195e1819e4fe9d3fc8634de3fc9a5a6fc2bfdde69acaa8fab10
```

A04 proved independent Activity/Operation/Attempt lifecycles; bounded concurrent Activity admission; retry with stable logical Operation and fresh physical Attempt identity/nonce; scoped cancellation; Event ordering/replay without treating delivery as proof; immutable exact-context Receipts; proof-gated result completion; independent worker formations/checkpoints/partials/conflicts; diagnostic-only repeated-failure correlation; and durable-before-visible A03 journal integration.

A04 runtime execution/proof authority is Oracle MCP/RPC. GitHub Actions are not the A04 runtime proof path.

## Preserved earlier acceptance

A03 remains the accepted durable ledger/migration substrate. Its exact candidate is `19d390e22807a8540c7c4c5c3a94a37b93f5e3be`, merge `da35986327010cba575093d905875ee966e3d755`, and physical proof authority remains its accepted Oracle MCP/RPC evidence.

A02 remains the accepted Node identity/Generation/host-truth substrate. A01 remains the accepted repository/contracts/reproducibility substrate with exact candidate `d12feedb5b66a39d5649b1d3ffea752deb5692c6`, merge `d33122c8cc625d38f2394d57fcbd2a3ef7027b08`, and exact-head workflow run `31906473232`. P01D remains the accepted development-host/runtime-authorization boundary.

These older acceptance records are invariants. Their original non-claims remain historical truth even after later phases complete.

## Core identity

Ptah is an independent, open-source, online-first and later local-first concurrent digital working world.

Ptah provides the workplace, tools, files, internet, storage, terminals, browsers, containers, applications, firmware, devices, rendering, sessions and artifacts.

The human or compatible calling system supplies intent, reasoning, priorities, instructions, restrictions and acceptance criteria. Ptah is the world where work happens, not the intelligence deciding what work should happen.

Ptah stays OS-neutral. In the intended Prime deployment, Prime owns machine authority and Ptah consumes Prime-exposed capabilities through an explicit integration boundary.

```text
Prime Host ID != Ptah Node ID
```

## Host and integration rule

- Oracle/MCP/RPC is private control/evidence infrastructure, not a Ptah Core dependency.
- Keep public Ptah proof tooling provider-neutral; private machine/control topology stays outside public Ptah source.
- Prime-owned isolation/resource mechanisms belong to the later P01P Prime-native capability proof.
- Do not infer Prime-native, production or release authority from successful Programme A development work.

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

Begin **A06 — Persistent Workspace, Session and authority projection**.

Before implementation:

1. recover A06 requirements from `IMPLEMENTATION_ROADMAP.md`, P0C-I006, frozen WP05/WP09/WP11 contracts and the AI Project Workspace profile;
2. inspect A03 durability, A04 Activity/Operation/Attempt/Event/Receipt runtime and A05 Provider/terminal foundations before adding code;
3. implement persistent Workspace identity and Workspace revisions/provider bindings without replacing identity on Session changes;
4. implement Session attach/detach and stale-Session authority fencing;
5. project Workspace-scoped Objects, Activities, terminals and Policies without yet implementing A07 Object/CAS semantics;
6. implement participant and Grant projection with fail-closed cross-Workspace retrieval;
7. implement restart-recovery projection for Workspace/session state and missing attachments;
8. preserve worker formation role, independence, checkpoint, partial-result and conflict evidence across interruption/recovery;
9. implement the basic handoff record required by A06;
10. prove Workspace identity survives disconnect and runtime restart;
11. prove Session changes do not replace Workspace identity;
12. prove missing attachments remain explicit and stale Session authority fails closed;
13. prove cross-Workspace retrieval fails without Grant;
14. prove agent replacement preserves authority/handoff state and interrupted worker formations recover without losing evidence;
15. freeze an exact candidate only after independent Review is clean, then prove those exact bytes through the accepted Oracle MCP/RPC host path before merge.

A07 Object/CAS work, P01P Prime-native integration and production/release acceptance remain out of A06 scope.

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
