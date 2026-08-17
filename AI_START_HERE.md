# AI Start Here — Ptah

You are continuing the Ptah Space project.

Do not answer from chat memory alone. Recover the project from this repository before proposing, designing, editing, proving or building anything.

## Required reading order

1. `planning/A06-PERSISTENT-WORKSPACE-SESSION-AUTHORITY-ACCEPTANCE.md`
2. `planning/A05-NATIVE-PROCESS-PTY-PROVIDER-ACCEPTANCE.md`
3. `planning/A04-ACTIVITY-OPERATION-ATTEMPT-RUNTIME-ACCEPTANCE.md`
4. `planning/A03-LEDGER-SCHEMA-MIGRATIONS-ACCEPTANCE.md`
5. `planning/A02-NODE-IDENTITY-GENERATION-HOST-TRUTH-ACCEPTANCE.md`
6. `planning/A01-REPOSITORY-CONTRACTS-SCAFFOLD-ACCEPTANCE.md`
7. `master-plan-index-amendment-2026-08-15.json`
8. `CURRENT_STATE_CLOSURE_2026-08-15.md`
9. `decisions/ADR-0039-P01D-ACCEPTANCE-A01-AUTHORIZATION.md`
10. `decisions/ADR-0038-PRIME-HOST-DEVELOPMENT-QUALIFICATION.md`
11. `CURRENT_STATE_AMENDMENT_2026-08-15.md` for the preceding P01D state
12. `CURRENT_STATE.md` for preserved historical context
13. `MASTER_PLAN.md`
14. `IMPLEMENTATION_ROADMAP.md`
15. `MASTER_ROADMAP.md`
16. `PROGRESS_AMENDMENT_2026-08-15.md`
17. `PROGRESS.md`
18. `DECISIONS.md` and `DECISIONS_AMENDMENT_2026-08-15.md`
19. `MEMORY_PROTOCOL.md`
20. `DONOR_RECOVERY.md`
21. `REQUIREMENT_CLOSURE_MATRIX.md`
22. `WORK_ITEM_TEMPLATE.md`
23. current source and public-safe technical documentation in `jaydumisuni/Ptah-space`
24. any donor or internal repository directly related to the selected work item

The accepted P01D closure plus A01–A06 acceptance records are current authority. Older records remain historical provenance and must not be rewritten into false passes.

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
- A05 — Native process, PTY and multi-terminal Provider: **FROZEN / PROVEN / COMPLETE**.
- A06 — Persistent Workspace, Session and authority projection: **FROZEN / PROVEN / COMPLETE**.
- A06 exact candidate: `28444aa2331c4c170df62f4de9499e93009f0f41`.
- A06 merge: `55cb08cffec10a2ee560014133d393be55f98d05`.
- A06 final Tenfold review receipt: `0000-ptah-a06-final-review-20260817-0428z`.
- A06 freeze manifest SHA-256: `6cb32c2210927fc4fe1449bb8ac40502666a55071259157c431c13d76c963494`.
- A06 Pass B proof manifest SHA-256: `26e7d031f444c4943e5ffcd36b484bd3d1a9265f9132b58d9d2d8b420f8e8d01`.
- A06 independent Sergeant review: **PASS / APPROVE**, 110 Tenfold private lanes, no required actions.
- A06 physical proof transport: `oracle.live.v1`; `githubInteractivePathUsed: false`.
- Active work unit: **A07 — Object, Revision, Artifact, Location and local CAS**.
- A07 status: **READY**.
- P01P Prime-native integration proof: **OPEN / DEFERRED**; it does not block Programme A development.
- Prime-native deployment qualification: **not claimed**.
- Production/release acceptance: **not claimed**.
- Public implementation repo: `jaydumisuni/Ptah-space`.
- Detailed roadmap and authorization repo: this repository.

## A06 accepted evidence

A06 promotes the persistent Workspace/Session authority substrate only. It does not pull A07 Object/CAS work, A13 checkpoint/restore execution, Prime-native integration or production/release acceptance forward.

Retained proof:

```text
Ptah-space PR: #28
candidate: 28444aa2331c4c170df62f4de9499e93009f0f41
merge: 55cb08cffec10a2ee560014133d393be55f98d05
final Tenfold review receipt: 0000-ptah-a06-final-review-20260817-0428z
freeze-gate receipt: 0000-ptah-a06-freeze-gate-20260817-0429z
freeze manifest: 6cb32c2210927fc4fe1449bb8ac40502666a55071259157c431c13d76c963494
Pass B receipt: 0000-ptah-a06-pass-b-proof-20260817-0430z
Pass B proof manifest: 26e7d031f444c4943e5ffcd36b484bd3d1a9265f9132b58d9d2d8b420f8e8d01
Tenfold private lanes: 110
Sergeant verdict: APPROVE
transport: oracle.live.v1
githubInteractivePathUsed: false
Rust/Cargo: 1.97.1
Cargo.lock: b7e2a30fc0660160fd330a9e1272ff195554b52b76f619c886826b933fb0c90e
ptah-workspace Cargo.toml: 2c2dc997762f89d2fa7894f631fa42eae7fbcf599e1432694f78a0ae4aee6cbb
ptah-workspace source: 8b3d6383011aaf9422050b3c4a6a8b777a28c366e7c167b2818099976b830667
A06 acceptance test: 4bd1bc24d5bf7cc493839e50f22bfd0c5b02bb242be280c817915eb5a4d4e97b
```

A06 proved durable Workspace identity/revisions/provider bindings; durable Session/Attachment projection; stale Session fencing; participant Membership; fail-closed cross-Workspace retrieval; Secure Grant expiry; explicit missing attachments; restart recovery; worker role/independence/checkpoint/partial/conflict retention; and authority-preserving handoff state.

A06 runtime execution/proof authority is Oracle MCP/RPC. GitHub Actions are not the A06 runtime execution/proof authority.

## Preserved earlier acceptance

A05 remains the accepted native process/PTY/terminal Provider substrate; its original A06 non-claim remains historical truth. A04 remains the accepted orchestration/proof substrate. A03 remains the accepted durable ledger/migration substrate. A02 remains the accepted Node identity/Generation/host-truth substrate. A01 remains the accepted repository/contracts/reproducibility substrate. P01D remains the accepted development-host/runtime-authorization boundary.

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
- Treat files as structured Objects with originals, children, derivatives, Views and provenance.
- Preserve live internet as a normal capability.
- Use fast local storage for active work and remote/object storage for durable copies and Artifacts.
- Preserve `Prime Host ID != Ptah Node ID` and the Prime-machine/Ptah-mechanical authority split.
- Follow: Understand → Build → Review → Freeze → Prove → Submit/Ship.

## Exact next operation

Begin **A07 — Object, Revision, Artifact, Location and local CAS**.

Before implementation:

1. recover A07 requirements from `IMPLEMENTATION_ROADMAP.md`, P0C-I007 and frozen WP03/WP07/WP10 contracts;
2. inspect A03 ledger durability, A04 producing Activity/Receipt provenance and A06 Workspace authority before adding code;
3. implement Content identity from cryptographic hashes without collapsing logical Object identity into Content identity;
4. implement Object registration and immutable Revision records;
5. implement Relationship and View foundations without premature Domain-Pack semantics;
6. implement digest-addressed local CAS with exact integrity verification;
7. implement Artifact promotion as an explicit authority action rather than automatic promotion of generated candidates;
8. implement Location/provenance records so moved storage does not replace Artifact identity;
9. preserve producing Activity and exact Receipt linkage;
10. prove identical bytes may deduplicate while distinct logical Objects remain distinct;
11. prove changed bytes create distinct Content identity;
12. prove digest mismatch blocks registration;
13. prove moved storage preserves Artifact identity;
14. prove generated candidates cannot silently become canonical Artifacts;
15. freeze an exact candidate only after independent Review is clean, then prove those exact bytes through the accepted Oracle MCP/RPC host path before merge.

A08 transfer execution, P01P Prime-native integration and production/release acceptance remain out of A07 scope.

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
