# Ptah durable AI/chat handoff

Last updated: 2026-08-20

## Operative authority

This file is a recovery handoff, not an implementation authority by itself. Read `AI_START_HERE.md`, `master-plan-index-amendment-2026-08-15.json`, the current accepted planning record and the public implementation before doing work.

Recover repository and proof evidence before reasoning. Do not infer acceptance from branch existence, PR state, command success or GitHub CI alone.

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
A08 — SOURCE FROZEN / exact-head proof PASS / blocked behind A07 acceptance / UNMERGED
A09 — SOURCE FROZEN / private proof PASS / blocked behind A08+A07 acceptance / UNMERGED
A10 — independently re-proven against actual frozen A07 predecessor; recover exact current lane before modifying
A11 — CURRENT PRIVATE CONSTRUCTION FRONTIER: Browser Provider on corrected A08 substrate
A12 — CANONICAL SOURCE CANDIDATE PUBLISHED / private proof PASS / exact-head proof lane requires final re-verification / UNMERGED
A13–A15 — NOT COMPLETE
Programmes B–F — NOT COMPLETE
P01P Prime-native integration — OPEN / DEFERRED
Production authorization — FALSE
Release acceptance — FALSE
```

## Exact current pickup — 2026-08-20

Continue the roadmap continuously from the recovered frontier. Do not restart at A07 and do not announce phase-by-phase transitions merely to narrate progress.

Primary active construction lane:

**A11 — Browser Provider** on exact corrected A08 substrate.

```text
A08 exact substrate:
d19bcf3e86373b2710fbf731e094a9a3f8e2a469

A08 exact tree:
4eb5ffe1686e1b472ed2c6959679fe54c891fb30

A08 source archive SHA-256 recovered for A11:
45bd0e04dcab9f555c7506fbdff89133e929be4fcbb9a5142ccf1cc8fdcc0c04

A08 Cargo.lock SHA-256:
6e7ef35fd0419f75dd0f2b4f9c9c173be1b4a050b26970bb80e3e1cff89c56e3
```

Disposable A11 source-export PR #46 completed and was closed without merge. It contained no product changes.

A11 Browser authority already recovered from the frozen roadmap/contracts:

- Browser Provider supervises binary/process/pool/local-resource mechanics; backend IDs remain aliases/evidence.
- persistent Browser Profile identity is separate from Profile Revision, Process, Context and Page generations;
- writable Profile sharing requires canonical Lease/fence control and must fail closed across mutually untrusted Workspaces;
- Context/Page/Frame references are generation-bound and stale references must be rejected after restart/navigation drift;
- browser downloads must enter A08 Transfer and A07 Content/Object verification rather than becoming browser-owned storage truth;
- response source, DOM, accessibility, pixels/screenshot, trace/video, console and network evidence remain separate Views/Artifacts;
- MFA, CAPTCHA, passkey, consent, restricted access and human completion are explicit states; Ptah has no bypass authority;
- crash recovery preserves safe evidence/partial results and must not blindly replay non-idempotent actions.

Recovered browser dependency locks for the implementation lane:

```text
Node.js          24.18.0
Playwright       1.60.0
playwright-core  1.60.0
Chromium         148.0.7778.96
Chromium revision 1223
```

Before adding A11 source, inspect current `jaydumisuni/Ptah-space`, the WP08 browser/live-research architecture and frozen WP09 Application/Browser/Semantic/Shell contracts. Preserve Ptah's neutral mechanical boundary; Browser-Use reasoning/memory/model behavior remains caller-side, not Ptah Core.

## A12 current canonical candidate

A12 archive decomposition was constructed privately, reviewed, frozen, proven, byte-verified during transport, and then published as exactly one canonical product commit over frozen A07.

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

### A12 exact-head proof lane status

Disposable proof PR #45 is **DO NOT MERGE** and exists only to independently prove the canonical candidate.

The candidate source itself did not move during proof-lane corrections.

Two proof-environment defects were found after publication:

1. hosted Ubuntu runner lacked required liblzma/compression development headers for the static helper build; the disposable workflow was amended to provision the required development libraries;
2. after proof-only commits accumulated above the candidate, the ancestry assertion became stale; it was corrected so the disposable branch anchors the immutable candidate below workflow-only commits.

Current disposable proof branch correction head at handoff:

```text
temp/a12-exact-proof-20260820
b9105b0b5de8e01076b5c5718086d86ac23d57c3
```

A new chat must check the latest workflow run on PR #45 before claiming exact-head GitHub proof completion. Do not alter canonical A12 `2e98ddc...` merely to repair the disposable proof environment.

A12 must not merge ahead of A07 acceptance order.

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

Do not let later privately constructed/frozen milestones erase this dependency gate.

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

Recover documented evidence before reasoning. Do not treat command success as mission acceptance. After freeze, do not alter the frozen candidate; prove those exact bytes from an independent/fresh checkout.

Current owner execution instruction:

- continue through the full roadmap rather than stopping to ask permission between normal phases;
- do not provide narration merely announcing movement to the next phase;
- use Tenfold/private construction machinery where appropriate and move only reviewed/frozen outputs into canonical product history;
- preserve dependency order and truthful acceptance states even when later work is constructed in parallel;
- no reboot/restart operations unless the owner explicitly changes that instruction.

## Recovery rule

Do not ask the owner to repeat information recoverable from this repository, `jaydumisuni/Ptah-space`, or directly relevant accepted internal evidence. Historical documents below current amendments remain provenance, not current machine authority.

When another chat picks up:

1. read this handoff first;
2. inspect current Ptah-space PR/branch heads because proof-only lanes may have advanced after this timestamp;
3. verify A12 PR #45 latest exact-head proof result without changing canonical A12 bytes;
4. continue A11 from exact corrected A08 `d19bcf3e...` using the recovered Browser contracts and locked dependency set;
5. continue the remaining roadmap after each Review/Freeze boundary while preserving the unresolved A07 physical acceptance gate;
6. never claim A13–A15, Programmes B–F, production or release acceptance unless evidence actually closes them.
