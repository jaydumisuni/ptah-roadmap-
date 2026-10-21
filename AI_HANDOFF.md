# E07 roaming requirement overrides same-LAN qualification

## E07 roaming correction — ATHENA travels (2026-10-21)

**Binding requirement:** E07 native E02/A05 must operate when ATHENA is away
from KRATOS, on unrelated home, hotspot, work or mobile networks.
The successful seventh LAN dispatch establishes actual native execution
but is NOT cross-Internet, NAT traversal or ATHENA roaming proof.
Do not certify E07 roaming from an equal-subnet test.

**Ptah-only implementation:** [Ptah-space PR #155](https://github.com/jaydumisuni/Ptah-space/pull/155)
(commit 00083094a1f992c0f87870b540181d119e04abe7) adds a small opaque
outbound TCP rendezvous relay, outbound Control and Node sockets, and
backward-compatible direct LAN mode. Existing TLS 1.3 mutual
authentication remains strictly end-to-end; the relay cannot grant
permissions, select A05 work or forge completion evidence. ATHENA's
Node worker can be configured with a public relay endpoint instead of
a fixed private KRATOS IP. Linux/Windows native artifact build CI was
added. KRATOS complete Rust workspace tests, relay mTLS transport tests,
affected strict Clippy and A01/Phase0C checks passed locally.

**Not yet claimed:** PR #155 source has not necessarily merged; a
globally reachable TCP relay has NOT been provisioned, Windows Node
replaced or an ATHENA-off-LAN E02/A05 effect physically verified. Those
are the remaining *transport deployment/roaming acceptance* steps,
not Ptah-side login, Grants or permission gates. Normal workspace
operations remain available during an E07 relay transport outage.
Do not overwrite the working ATHENA scheduled-task config before the
new relay and Windows binary are independently reachable and verified.

**Boundaries:** Only Ptah code and Ptah roadmap changed. Knights,
Oracle configuration, ATHENA Wi-Fi and existing services untouched.
Prime OS integration LAST after the roaming requirement is met.

---

# Latest E07 post-restart A05 physical success — 2026-10-21 (READ FIRST)

E07's last measured runtime gap is CLOSED. KRATOS and ATHENA are back on
the same private LAN. The E01 `UnknownCA` technical error was traced to
ATHENA's newer Ptah CA being inconsistent with KRATOS Control; re-used
existing ATHENA Ptah backup CA and Node certificate, verified the
original private-key match and Control enrollment fingerprint, saved the
previous worker.json and restarted only ATHENA's Ptah worker. New PID 31572.

KRATOS's existing native dispatch succeeded after that restart:
E02 frames delivered, A05 `cmd /C echo` completion acknowledged. Independent
read-only journals: Control 7 dispatches; Node 7 attempts. Exact latest
dispatch/attempt/Node generation/epoch/fence **7**/request digest match.
Node completed, exit code **0**, durable output SHA-256 independently
matches expected Windows CRLF echo. Both SQLite integrity checks pass.
Control truthfully retains sent_unconfirmed (does not claim an independent
Control effect receipt). This is a qualified physical post-restart E07
native execution, not an invented promise or new Ptah access gate.

**There is NO defined Programme E08 in IMPLEMENTATION_ROADMAP.md**.
Programme E ends at E07. Do not introduce an E08 approval process;
F01–F03 standalone Ptah foundations are already merged; Prime OS
integration (F04–F07) remains LAST. Knights and Oracle settings remain
untouched; Ptah's own worker configuration was the only live adjustment.
The previous E07 cross-subnet and unverified-post-restart paragraphs
below are historical and superseded.

---

# E07 Native E02/A05 mainline integration — 2026-10-20 (read FIRST)

E07 source PR #153 is now MERGED into Ptah-space/main (de627797).
Windows SQLite exact dependency PR #154 is MERGED (c2c0a1d).
The entire KRATOS Rust workspace suite, native strict Clippy and
A01/Phase0C historical scaffold checks passed.

Six KRATOS Control journal dispatches match six ATHENA durable completed
native A05 executions by dispatch ID, fence, generation and connection
epoch. All exit 0 with output SHA-256; both journals integrity=ok.
Control retains honest sent_unconfirmed, ATHENA stores actual local effects.

Windows task Ptah-E07-Native-Node automatically restarted the persistent
Node worker at 13:36:48 local after worker termination (PID 30756 alive).
The sixth verified completed dispatch was ~13:28 (BEFORE restart).
At ~14:50 ATHENA changed Wi-Fi to 192.168.1.155 while KRATOS's
Control listener used 192.168.238.52:47821; ATHENA TCP failed and a
fresh post-restart dispatch timed out WITHOUT new completion.
Never claim E07 post-restart full end-to-end effect until a reachable
transport path exists and another dispatch is recorded in both journals.

E07 physical remote A05 execution is REAL and source-integrated; worker
restart resilience is REAL independently; split-subnet transport is a
per-operation technical limitation, NEVER a global workspace gate.
Ptah is a workspace; Oracle transports; the caller decides. Knights
files/systems stay untouched. E06 and F01-F03 are merged.
Prime OS integration LAST. Older E07 "not yet implemented" entries
below are historical and superseded.

---

# E07 physical two-host E01 qualification — VERIFIED 2026-10-20 (read first)

Ptah-space PR #152 merged into protected main at
`1f39acec718acebb48b7fba3ed614762e0e91b85`.
Real KRATOS Rust `ptah-enrollment-gateway` ↔ ATHENA Windows Python
Ptah wire client over TLS 1.3 passed NodeHello/HelloAck, 3
heartbeats and close, then second connection with 2 heartbeats.
Wrong canonical Node ID and absent TLS client certificate were rejected.
35 Python tests and 16 hosted PR workflows passed. Test-only
certificates and temporary listeners/files were removed.

This CLOSES the previously missing physical two-host E01 transport
evidence. Do NOT re-report it as untested. It does not claim a
production-installed native Node, remote E02/E05/A05 dispatch, or
persistent system deployment; these are separate optional technical
features, **never workspace security/access blockers**. Ptah is a shared
workspace; Oracle only transports. No Knights modifications or Ptah
login/Grants. E06, E07 source, F01–F03 and shared-workspace source
remain merged. **Prime OS integration LAST.**

---
# Ptah closure — 2026-10-20 VERIFIED CURRENT STATUS (read first)

**E07 source integration FINISHED and MERGED** — Ptah-space PR #138 at
`982210d25c15e5a1c69d9c2f2a318e096e4d9309`.
**Shared Ptah workspace runtime correction FINISHED and MERGED** — PR #150
at `aa413dc3140fbd8a5273c8870eb06d17be51080c`.
**Current-head CI and trusted-base integrity migration MERGED** — PR #151
at `7c6080964768732b9166bbb1d7233b0ad11cae78`.
Branch protection stays strict with A01, Rust dependency, static,
artifact and signature checks plus trusted-base integrity and actual
current-head integration tests. The original historic exact-predecessor
workflows remain as dated audit evidence, not a merge veto against normal
new source maintenance.

E06 and F01–F03 are DONE at tested standalone source level. Ptah is a
shared workspace; no duplicate login, per-user Grants, individual tool
approvals, or Ptah task-decider. Oracle transports requests to nodes.
This work **did not touch Knights**. E07 physical native two-host
deployment was not claimed as proven, but is optional and does not block
using existing workspace tools. Prime OS integration LAST.

**ALL prior notes below calling PR #138 or #150 "not merged" or a required
CI problem are historical snapshots, superseded by this verified record.**

---

# Latest Ptah integration status — 2026-10-20 (current)

**Read before resuming:** PR #138 E07 latest `785f202b7b43a799a13330653009721f44b3d177`; exact E07 local-only Cargo.lock change now reconstructs unchanged historical E01/E06 lock bytes and tests pass; A01 and Phase0C local + hosted static checks PASS; GitHub current-head universal admission PASS. **The protected GitHub A11 governance check refuses edits to trusted `tools/check_current_pr_admission.py`**, making PR #138 unmergeable as presently structured (GitHub 405). Four legacy predecessor proofs remain red, and they are NOT genuine E07 native runtime tests. Correct the repository's approved governance mechanism; do not bypass protection or claim a merge.

PR #150 shared workspace runtime has latest merged Ptah main on head `1356736a06e1c165daa7a526ffe84e508ef48dd1`, physical KRATOS full Rust workspace test PASS and 6 native D02 bridge tests PASS. Old A11/D02/D03/D05 exact-head checks still reject the cross-module maintenance; protected merge remains open. No Knights changes.

E06 and F01–F03 are MERGED/DONE at standalone source level. Oracle remains machine transport, Ptah a workspace, caller decides tasks. No owner permission, second login, individual approval, or per-tool Grant is a prerequisite. E07 optional native work does not gate normal Ptah. Prime OS integration LAST.

---

# E07 current review/merge checkpoint — 2026-10-20

PR #138 current head `b95eaac5c1d022d78ba5e66f0b1d130d193ad5eb`
fixes three actual Ptah E07 defects: exact persisted A05 process/Attempt
identity for completion; private Control SQLite/lock creation (0600 Unix);
live expiry time after TLS+Hello and owner lock. Full KRATOS Rust workspace
tests, 29 Python client tests and strict native component Clippy passed.
All three review threads are resolved. **E07 remains unmerged** because
GitHub protected main reports 3 of 9 required status checks failing,
principally legacy historical phase/scope/lock proof. This does not
authorize Ptah to deny normal workspace access or to invent additional
security/approval steps. No live two-host native production activated,
no Knights changes, Oracle remains transport. PR #150 cross-tool caller
boundary is also open. F01–F03 remain MERGED/DONE at standalone level;
Prime OS integration LAST. Continue Ptah engineering from these facts.

---

# Current Ptah build completion checkpoint — 2026-10-20

F01–F03 standalone Ptah capabilities are **MERGED in Ptah-space main**
(PRs #139, #141, #143, #144, #145, #146). F01 deterministic binary
archive + detached Ed25519 integrity, F02 passive USB inventories and
inert rules, and F03 physical KRATOS KVM guest/COW crash recovery were
tested. Do not label them unfinished or create an extra Ptah-side access
approval. Prime OS integration is LAST.

E07 optional native Control/Node gateway PR #138 is **source-tested but
NOT merged** as of reviewed head b95eaac. Fresh KRATOS full Rust workspace tests,
29 Python client tests and strict Control/Node/Node-link Clippy pass.
Older E01/D01/D08/A14 and exact-head predecessor workflows report failures;
the Cargo.lock historical E06 extension checker also rejects E07's
additional local package dependencies. These are *repository integration
and evidence-classification issues*, not authority to block an admitted
user's ordinary Ptah workspace. No permanent Control/Node service or
two-host native deployment was activated. Oracle remains machine transport.

The separately tracked shared workspace caller-gate runtime PR #150 has
not been merged. Continue that Ptah correction without touching Knights,
without disabling record consistency or process integrity, and without
introducing another Ptah login, Grant or tool approval.

---

# E06 supplementary physical evidence completed — 2026-10-20

E06 is DONE, tests executed on KRATOS and ATHENA through already
authenticated Oracle transports. Separate real Oracle invocation
reopened an NVMe/ext4-backed E06 journal and Ptah's reconnect comparator
detected matching, stale fence, changed generation and uncertain prior
effect without any automatic replay, login, second approval or journal
writes. Physical KRATOS: 44 CLI worker attempts / 22 SIGKILLs, 23
persisted consecutive queue entries, sqlite integrity=ok and zero
extra worker processes; disposable deleted-receipt-table and invalid
generation-JSON copies failed closed. No host reboot, mains-power cut or
forced network outage was run. Those are optional further reliability
experiments, NEVER workspace access/feature blockers. Do not reopen E06
as unfinished simply because a different deployment asks for stronger
durability proof. Knights left alone; Oracle transport only; Prime OS LAST.

---

# E06 closure / no second Ptah gate — 2026-10-20 (read first)

E06 source implementation is DONE and merged in Ptah-space/main:
PR #137 durable queue, journal and saved reconnect references;
PR #140 strict comparison, stale versions and unknown-outcome priority.
Further live session/reconnect and physical crash/power tests are
**optional reliability evidence**, not blockers for accessing Ptah,
other providers, E07 work or standalone F01–F03. Do not create new
Ptah owner login, "authenticated reconnect" enrollment, release GO/NO-GO,
per-agent Grants or physical test prerequisites to let an upstream-admitted
caller use the workspace. Technical errors remain actual errors for only
the affected operation; process/journal integrity is not an access policy.
Knights stays entirely out of scope. Oracle is transport. Caller chooses
tools. Prime OS integration LAST.

Older contradictory E06 "NOT STARTED", "release OPEN" or "blocked"
paragraphs below are historical snapshots, not present-day instructions.

---

# CURRENT OWNER ARCHITECTURE — 2026-10-19 (read first)

Knights handles external security and future cybersecurity; while unfinished
the Ptah development workspace remains open. Ptah must NEVER invent a second
login, authorization, owner enrollment, agent registration, per-tool Grant,
policy approval, semantic tool choice, or release gate to let an admitted
human/AI work. Oracle ONLY transports commands to machines. Caller chooses
tools/tasks. Ptah executes available capabilities or reports precise
technical errors. Preserve mechanical process/lease/ledger isolation, never
fabricate authority. See IMPLEMENTATION_ROADMAP.md section 2026-10-19
Owner Correction and CURRENT_STATE.md.

Return to standalone E06/E07 and F01-F03 implementation; Prime OS comes LAST.
Track PR #147 Search, PR #148 Browser and PR #150 D02/D03/D05/shared
workspace migration without conflating review with a permissions office.
Older authentication/Grant approvals below are historical and not binding
authorization for an already admitted caller.

---

F03 candidate PR #146: 13/13 CI and 6/6 additional process-crash recovery cycles; real Linux guest/physical power test NOT accepted. E07 older D01/A14 phase CI predecessor mismatch is not an independent E07 release. ATHENA not currently Oracle-reachable. Prime OS last. See CURRENT_STATE.md.

F03 COW crash/rollback and guest restart candidate PR #146 is source-verified and physically tested on KRATOS; still not host power-loss or guest OS acceptance. ATHENA not currently reachable via Oracle. Prime OS is LAST. See CURRENT_STATE.md.

Continue standalone Ptah first: qualified F02 candidate PR #143; F03 bounded KVM guest boot PR #144 (13/13 exact-head CI pass, ready for review). Keep Prime OS F04-F07 system integration last; Oracle is transport and Ptah shared workspace. See CURRENT_STATE.md for scope/acceptance distinctions.

Current additional qualified candidates: E06 reconnect PR #140 and unsigned F01 package PR #141; both source review ready and 13/13 hosted CI green, still not released. See CURRENT_STATE.md for exact acceptance gates.

# Current continuation — 2026-10-19

The authoritative status is CURRENT_STATE.md. Oracle is machine transport;
Ptah is neutral shared workspace. E06 #137 passed CI but release is open;
optional native E07 #138 remains physical NO-GO; Programme F #139 is a
non-activating candidate, with all F stages still unaccepted. Review the
exact branch, owner and physical evidence gates before claiming completion.

---

# Ptah durable AI/chat handoff

Last updated: 2026-10-02

## Current pickup override — 2026-10-02

The August construction-state material retained later in this file is historical. Do not resume A07/A12 or Phase 0C from that old snapshot.

Current accepted implementation boundary:

```text
Programme E — Distributed Ptah
E01 — COMPLETE
E02 — COMPLETE
E03 — COMPLETE
E04 — COMPLETE
E05 — COMPLETE / RELEASED
E06 — RECOVERY / DESIGN ACTIVE / IMPLEMENTATION NOT STARTED
E07 — NOT STARTED
```

Exact current public release state:

```text
E04 accepted merge: 77bbd876aaefd78fed2c0583b2b124eee428eb5f
E05 proven candidate: aa2c8b5efef87787354e41075f3d35efc573b960
E05 frozen release: 90a3ad012f0b3e15bd871e6e955dd79bbf757ded
E05 release tree: 58312f1e72dd05a28978c52e04268c5db30dd2db
current Ptah-space/main: e11c744c4e9900c460e3c4a3fda9fe385f6e1dc9
```

The unchanged E05 candidate passed pull-request exact-head proof run `36847594835`; the frozen release passed integration proof run `36848216032`; PR #107 merged the immutable E05 release forward without rewriting the intervening operational mainline.

Supervisor auto-continuation has consumed the completed E05 handoff. The bounded E06 recovery/design branch `e06-intermittent-local-first` is published at accepted base/head `e11c744c4e9900c460e3c4a3fda9fe385f6e1dc9`; Cookpit E06 micro and heavy recovery proofs pass. This opens E06 recovery/design only and does not claim an E06 implementation delta.

A bounded private live-consumption proof also exercised the released Ptah authority chain against a real workload. Machine-specific and credential details remain in private ecosystem evidence, not this public handoff. That proof does not claim a permanently installed Ptah daemon or production credential enrollment.

**Zero-context recovery order now:**

1. `TTG-progress/projects/ptah-space/CURRENT.md`;
2. `TTG-ecosystem/docs/PTAH_RECOVERY.md`;
3. `ptah-roadmap-/CURRENT_STATE.md`;
4. `ptah-roadmap-/IMPLEMENTATION_ROADMAP.md`, Programme E / E06;
5. frozen E05 release `90a3ad012f0b3e15bd871e6e955dd79bbf757ded`;
6. current `Ptah-space/main` `e11c744c4e9900c460e3c4a3fda9fe385f6e1dc9`.

No E06 implementation is claimed by this handoff.

---

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
