# Ptah durable AI/chat handoff

Last updated: 2026-08-21

## Operative authority

This file is a recovery handoff, not implementation authority by itself. Read `AI_START_HERE.md`, `master-plan-index-amendment-2026-08-15.json`, the current accepted planning record and the public implementation before doing work.

Recover repository and proof evidence before reasoning. Do not infer acceptance from branch existence, PR state, command success or GitHub CI alone.

Ptah construction is executed through the existing Tenfold campaign in the working environment. Use Tenfold OM-001 (Private Workspace / Canonical Milestone Promotion) with PM-PTAH-001. The workspace is the execution plane; `jaydumisuni/Ptah-space` is the canonical promotion surface. Only reviewed/frozen product candidates enter canonical history.

Current operative state:

```text
Phase 0C P01D — ACCEPTED COMPLETE
Runtime implementation — AUTHORIZED
A01 — ACCEPTED COMPLETE
A02 — ACCEPTED COMPLETE
A03 — ACCEPTED COMPLETE
A04 — ACCEPTED COMPLETE
A05 — ACCEPTED COMPLETE
A06 — ACCEPTED COMPLETE
A07 — SOURCE FROZEN / REVIEW RECONCILED / awaiting accepted Oracle physical Pass B / UNMERGED
A08 — SOURCE FROZEN + EXACT-HEAD PROVEN / blocked behind A07 acceptance / UNMERGED
A09 — SOURCE FROZEN + PRIVATE PROVEN / blocked behind A08+A07 acceptance / UNMERGED
A10 — independently re-proven against actual frozen A07 predecessor; canonical product lane must be recovered before A13
A11 — FROZEN + EXACT-HEAD PHYSICAL BROWSER PROVEN / canonical PR #48 READY / blocked behind A08+A07 acceptance / UNMERGED
A12 — CANONICAL SOURCE CANDIDATE PUBLISHED + PRIVATE PROVEN / disposable exact-head proof lane still requires repair/re-run / UNMERGED
A13–A15 — NOT COMPLETE
Programmes B–F — NOT COMPLETE
P01P Prime-native integration — OPEN / DEFERRED
Production authorization — FALSE
Release acceptance — FALSE
```

## Exact current pickup — 2026-08-21

Do **not** restart A11. A11 source is frozen and its exact canonical bytes have passed physical Playwright/Chromium qualification.

The next safe Tenfold frontier is:

1. repair and rerun **A12 exact-head proof PR #45** without modifying canonical A12 source;
2. recover the exact **A10 product lane/source authority** before A13 instead of inferring it from the disposable A07 export/re-proof record;
3. recalculate A13 readiness only after A10/A11/A12 evidence is reconciled;
4. preserve the unresolved A07 physical acceptance gate and canonical promotion order throughout.

Later construction may continue on a safe dependency frontier, but no later milestone may merge ahead of its unaccepted predecessor.

## A11 — Browser Provider — FROZEN + PROVEN

Canonical source:

```text
Ptah-space canonical PR: #48
branch: a11-browser-provider
candidate commit: cf02bec49775479ede404f0a80d1aa5cd03742e5
candidate tree:   9fa433d36c272badf72d5c2af41f5994a258bd82
parent A08:       d19bcf3e86373b2710fbf731e094a9a3f8e2a469
commit count over A08: 1
changed files: 19
PR state: open / ready for review / unmerged
```

A11 was constructed on the exact corrected A08 substrate and delivers:

- mechanical Playwright/Chromium Browser Provider;
- canonical Browser Profile, Process, Context and Page projections;
- Provider/Context/Page Generation fencing;
- writable Profile Lease/fence ownership with serialized writer lifecycle;
- fresh A04 Attempt binding for navigation, with navigation ACK separated from page-state success;
- explicit Challenge fencing for MFA, CAPTCHA, passkey, consent and human-completion boundaries;
- A08-backed bounded download integration and upload mechanics;
- screenshot, console, network, response-source and DOM/accessibility evidence foundations under A07 truth boundaries;
- detach/reconnect behavior;
- privacy filtering and personal-profile protection.

Review corrected real product defects before Freeze, including incomplete generation fencing, unbounded browser-download reads, Challenge-to-ready escape, Attempt reuse, transient writable-Profile authority, profileless ephemeral Page mismatch, browser error-detail privacy leakage and Linux Chrome personal-profile detection.

Private Tenfold Review/Freeze evidence:

```text
exact A08 substrate: d19bcf3e86373b2710fbf731e094a9a3f8e2a469
A08 tree:            4eb5ffe1686e1b472ed2c6959679fe54c891fb30
freeze payload SHA-256:
6858c55f0623d1a5a524cadae0f743f6e94d6d740e814a9568c8ec912625ab00
private freeze manifest SHA-256:
2a1ea239216515805a480c772c40595f1ffa23ce86804384e4d33c91bce599fb
Rust/Cargo: 1.97.1
fmt: PASS
strict scoped Clippy -D warnings: PASS
A11 Rust acceptance: 11/11 PASS
Provider API: 4/4 PASS
full locked Rust workspace: 182/182 PASS
Node mechanical Browser corpus: 15/15 PASS
registry packages: 97
resolved packages: 117
Git dependencies: 0
```

### A11 canonical packaging record

Disposable PR #47 reconstructed the SHA-256-bound private freeze payload, verified every frozen file and exact candidate scope, and generated the canonical commit object above.

Three packaging-runner defects were retained as tooling evidence and did not change product bytes:

1. unstaged new files were initially omitted from `git diff --name-only` scope calculation;
2. `git commit-tree` initially lacked hosted-runner author identity;
3. the GitHub Actions token could create the commit object but could not update a ref containing a newly added workflow file.

The already-retained canonical object `cf02bec...` was attached to `a11-browser-provider` through the connected GitHub authority without byte mutation. PR #47 is closed without merge. No `.a11-pack` or disposable packaging workflow entered canonical product history.

### A11 exact-head physical Browser proof

The first canonical PR #48 exact-head run passed every substantive Rust, Node and real Chromium gate but failed its final retention cleanliness assertion because `npm ci` generated `browser-provider/node_modules/`, while the root ignore rule covered only `/node_modules/`. This was classified as a proof-runner retention defect, not a product-source defect.

Disposable PR #49 therefore checked out the exact frozen canonical commit and reran the complete proof without modifying canonical A11 bytes. It removed only generated `browser-provider/node_modules/` before the final clean-tree assertion.

Accepted exact-head Browser proof:

```text
workflow run: 32423596200
job:          96600708972
result:       PASS
candidate:    cf02bec49775479ede404f0a80d1aa5cd03742e5
tree:         9fa433d36c272badf72d5c2af41f5994a258bd82
parent A08:   d19bcf3e86373b2710fbf731e094a9a3f8e2a469
Rust/Cargo:   1.97.1
Node:         24.18.0
Playwright:   1.60.0
playwright-core: 1.60.0
Chrome for Testing: 148.0.7778.96
Chromium revision: 1223
A11 Rust acceptance: 11/11 PASS
Provider API: 4/4 PASS
full locked Rust workspace: 182/182 PASS
Browser mechanical corpus: 15/15 PASS
real Chromium physical qualification: 1/1 PASS
post-qualification tracked/untracked source cleanliness: PASS
exact commit/tree recheck: PASS
registry packages: 97
resolved packages: 117
Git dependencies: 0
```

Retained proof:

```text
proof JSON SHA-256:
54f61ec131df7547acd212882243934fff30511584e61ddd1816ded9f6b08692
artifact ID: 9426621460
artifact SHA-256:
aa395a6e6ce5b409df4fed198c39e7b6b11c3a62b9104f6cbd5f8645eb66a1a6
artifact retention: through 2026-09-19
```

PR #49 is closed without merge. Canonical PR #48 is **FROZEN + PROVEN**, but must remain unmerged until A07 then A08 are accepted/promoted in dependency order. A11 is not `COMPLETE` merely because its own proof passed.

## A12 current canonical candidate

A12 archive decomposition was constructed privately, reviewed, frozen, proven, byte-verified during transport, and published as exactly one canonical product commit over frozen A07.

```text
Ptah-space canonical PR: #44
branch: a12-archive-decomposition-libarchive
candidate commit: 2e98ddccd99775e4e7fab61936b4b7f9b319c162
candidate tree:   31652c5aaf89c978c31c8846c0e762b21831c9f2
parent A07:       05e2e75b7a2069d0df74eb73f9b9ecd7cd17d0d4
commit count over A07: 1
changed product/lock files: 13
```

A12 delivered:

- libarchive-backed read-only decomposition boundary;
- deterministic archive inventory;
- child Object, View and immediate-container Relationship registration through existing A07 authority;
- traversal, duplicate, link, recursion/resource and decompression-bomb policy;
- malformed/partial/unsupported handling with retained verified prefix results and explicit incomplete coverage;
- CAS-only safe materialization;
- exact source Revision + A04 Operation targeting;
- backend-replacement identity preservation;
- exact libarchive 3.8.7 helper version/source/hash fencing.

Locked libarchive source:

```text
version: 3.8.7
source SHA-256: d3a8ba457ae25c27c84fd2830a2efdcc5b1d40bf585d4eb0d35f47e99e5d4774
```

Private pre-publication Review/Prove evidence on the frozen bytes:

```text
Rust/Cargo 1.97.1 pinned
registry dependencies: 97
Git dependencies: 0
fmt: PASS
scoped Clippy -D warnings: PASS
A12 core/persistence: 10/10 PASS
physical exact-libarchive qualification: 6/6 PASS
inherited A03/A04/A07: 74/74 PASS
complete exact-A07+A12 ordinary workspace: 162/162 PASS
C -fanalyzer: PASS
```

The physical suite rejects a wrong libarchive version and proves the exact 3.8.7 helper. Do not downgrade this to the host libarchive 3.7.4.

### A12 exact-head proof lane — CURRENT NEXT ACTION

Disposable proof PR #45 is **DO NOT MERGE** and exists only to independently prove canonical A12.

```text
proof branch: temp/a12-exact-proof-20260820
current proof head: b9105b0b5de8e01076b5c5718086d86ac23d57c3
canonical A12 that must remain unchanged:
2e98ddccd99775e4e7fab61936b4b7f9b319c162
```

Latest known exact-head proof run on `b9105b0...` is still failed. The known defect is in proof-runner ancestry/scope logic: proof-only commits accumulated above the immutable candidate and an ancestry-depth assertion became stale. Do not mutate canonical A12 to repair this.

Repair the disposable workflow so it binds directly to explicit canonical candidate SHA/tree/base identities rather than assuming `HEAD~N` ancestry depth. Then rerun the full exact-head/physical proof, retain the artifact, close PR #45 without merge and reconcile the successful receipt into canonical PR #44.

A12 must not merge ahead of A07 acceptance order.

## A10 recovery requirement before A13

A10 — OCI container Provider — was independently re-proven against its actual roadmap predecessor A07 after Tenfold detected contamination risk from later A08/A09 work.

The currently discoverable Ptah-space record is disposable PR #38, `TEMP — exact A07 source export for A10`, closed without merge at `feaff614b401636d3e46c552dda02dd3878d2150`.

Do not treat that disposable transport/export branch as the canonical A10 product lane. Before A13 construction, recover the exact A10 frozen product bytes/candidate authority from Tenfold private campaign evidence or another durable source and reconcile a canonical product lane if one is absent.

## A09 current frozen candidate

```text
Ptah-space PR: #37
candidate: 76aed337fd62ee38b303cc435525d31a2b0d3581
tree:      31e0fcabbb9aa00a7b0829544bfe23750b1b2488
parent A08: d19bcf3e86373b2710fbf731e094a9a3f8e2a469
commit count over A08: 1
```

A09 owns hardened mechanical Git resolution/materialization only. Private proof recorded fmt PASS, scoped Clippy PASS, A09 13/13, inherited A03/A04/A07/A08 92/92 and full locked workspace 182/182. It remains blocked by predecessor acceptance order and must not manufacture A07 identity or treat Git object IDs/paths as Ptah identity.

## A08 current frozen candidate

```text
Ptah-space PR: #30
candidate: d19bcf3e86373b2710fbf731e094a9a3f8e2a469
tree:      4eb5ffe1686e1b472ed2c6959679fe54c891fb30
parent A07: 05e2e75b7a2069d0df74eb73f9b9ecd7cd17d0d4
commit count over A07: 1
```

Exact-head confirmation recorded:

```text
GitHub run 32310390734 / job 96251997048: PASS
A08 behavior: 18/18 PASS
inherited A03/A04/A07: 74/74 PASS
full locked workspace: 170/170 PASS
```

A08 remains source-frozen and unmerged until A07 is accepted.

## A07 frozen candidate and remaining gate

```text
Ptah-space PR: #29
candidate: 05e2e75b7a2069d0df74eb73f9b9ecd7cd17d0d4
base accepted A06 main: 55cb08cffec10a2ee560014133d393be55f98d05
source state: REVIEW-RECONCILED / FROZEN
```

A07's GitHub exact-head confirmation passed, including 27/27 A07 behavior and 47/47 A03/A04 regression tests. It remains explicitly **not COMPLETE and not merge-authorized** until accepted final physical Pass B executes from a fresh detached checkout through Oracle MCP/RPC (`oracle.live.v1`, non-GitHub interactive path), matching the A06 acceptance class.

Do not let later privately constructed/frozen/proven milestones erase this dependency gate.

## A06 accepted implementation

```text
Ptah-space PR: #28
frozen candidate: 28444aa2331c4c170df62f4de9499e93009f0f41
merge: 55cb08cffec10a2ee560014133d393be55f98d05
final Tenfold review receipt: 0000-ptah-a06-final-review-20260817-0428z
freeze manifest SHA-256: 6cb32c2210927fc4fe1449bb8ac40502666a55071259157c431c13d76c963494
Pass B proof manifest SHA-256: 26e7d031f444c4943e5ffcd36b484bd3d1a9265f9132b58d9d2d8b420f8e8d01
Tenfold private lanes: 110
Sergeant verdict: APPROVE
transport: oracle.live.v1
githubInteractivePathUsed: false
```

A06 proved persistent Workspace identity and revisions, Provider bindings, durable Session/Attachment projection, stale Session authority fencing, participant/Membership projection, fail-closed cross-Workspace retrieval, Secure Grant expiry enforcement, explicit missing attachments, restart recovery projection, worker/checkpoint/partial/conflict preservation and basic authority-preserving handoff.

A06 explicitly does not claim A07 Object/CAS materialization or A13 checkpoint/restore execution. GitHub Actions are not the A06 runtime execution/proof authority; accepted proof ran through Oracle MCP/RPC.

## A05 accepted implementation

```text
Ptah-space PR: #27
frozen candidate: 4be4f170219701841aca367dd98c7b746fdd444c
merge: 34bc4beed57517532a1d79ae64131835a395f7b2
Tenfold final-review packet SHA-256: 627074b11c36014d8f8c391bdbcecbb5130a68e0fbbe8151d8af03aa700b9061
transport: oracle.live.v1
githubInteractivePathUsed: false
```

A05 remains the accepted native process/PTY/terminal Provider substrate. Its original A06 non-claim remains historical truth and is not rewritten by later completion.

## Earlier accepted invariants

- A04 candidate `fad9029504258c773f5ab496c79cfceea17c0b5e`, merge `a63eb8f2c73f961b8466b844c6f194f2381a8139`: Activity/Operation/Attempt/Event/Receipt runtime.
- A03 candidate `19d390e22807a8540c7c4c5c3a94a37b93f5e3be`, merge `da35986327010cba575093d905875ee966e3d755`: durable ledger/schema/migration substrate.
- A02 candidate `80adcd0aefe0053b2354b26676bfc9e28d9b8ec3`, merge `1603ac80b5d2c5925fde62392ec0fff4b07a1219`: Node identity/Generation/host-truth substrate.
- A01 candidate `d12feedb5b66a39d5649b1d3ffea752deb5692c6`, merge `d33122c8cc625d38f2394d57fcbd2a3ef7027b08`: repository/contracts/reproducibility substrate.
- P01D remains the accepted development-host/runtime-authorization boundary.

Later progress must not rewrite older packages into claims they did not make at their acceptance time.

## Core boundary

```text
Ptah = neutral platform and mechanical access enforcement
Hunter = intelligence, context selection and coordination
Sergeant = independent reviewer producing Sergeant results
Human/calling application = intent, approval, acceptance and release

Prime Host ID != Ptah Node ID
```

Oracle/MCP/RPC is private control/evidence infrastructure, not a Ptah Core dependency.

## Engineering and execution rules

For every authorized work item:

```text
Understand → Build → Review → Freeze → Prove → Submit / Ship
```

Recover documented evidence before reasoning. Do not treat command success as mission acceptance. After Freeze, do not alter the frozen candidate; prove those exact bytes from an independent/fresh checkout.

Current owner execution instruction:

- continue through the full roadmap rather than stopping to ask permission between normal phases;
- do not provide narration merely announcing movement to the next phase;
- use the existing Tenfold Ptah campaign in the working environment and move only reviewed/frozen outputs into canonical product history;
- use exact-predecessor construction and recalculate the safe dependency frontier when a proof/promotion gate is blocked;
- classify proof-runner, stale-workspace/substrate and product defects before mutating source;
- preserve dependency order and truthful acceptance states even when later work is constructed in parallel;
- no reboot/restart operations unless the owner explicitly changes that instruction.

## Recovery rule

Do not ask the owner to repeat information recoverable from this repository, `jaydumisuni/Ptah-space`, Tenfold campaign evidence or directly relevant accepted internal evidence. Historical documents below current amendments remain provenance, not current machine authority.

When another chat picks up:

1. read this handoff first;
2. inspect current Ptah-space PR/branch heads because proof-only lanes may have advanced after this timestamp;
3. do not rebuild or re-open A11 unless `cf02bec...` itself moves or a new grounded defect is found;
4. repair/rerun A12 PR #45 against immutable canonical A12 `2e98ddc...`, then reconcile its successful exact-head proof into PR #44;
5. recover the exact A10 product lane before A13;
6. recalculate the A13 frontier through Tenfold after A10/A11/A12 are reconciled;
7. preserve A07 → A08 → later canonical promotion order;
8. never claim A13–A15, Programmes B–F, production or release acceptance unless evidence actually closes them.
