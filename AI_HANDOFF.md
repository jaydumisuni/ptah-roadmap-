# Ptah durable AI/chat handoff

Last updated: 2026-07-24

Status: Master Plan and implementation roadmap accepted — Campaign 001 accepted complete — P01 physical-host closure active — runtime implementation unauthorized

## Read first

1. `AI_HANDOFF.md`
2. `CURRENT_STATE.md`
3. `master-plan-index.json`
4. `MASTER_PLAN.md`
5. `IMPLEMENTATION_ROADMAP.md`
6. `archive/campaign-001/OPERATIVE-BINDING.md`
7. `archive/campaign-001/OPERATIVE-STATE.json`
8. `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`
9. `planning/MASTER-PLAN-RECONCILIATION.md`
10. `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`
11. `PROGRESS.md`
12. `DECISIONS.md` and the referenced ADRs
13. `MEMORY_PROTOCOL.md`
14. current source and evidence in `jaydumisuni/Ptah-space`

Do not ask the owner to repeat information recoverable from these records.

## Accepted planning authority

- Master Plan version: `1.0.0`;
- implementation roadmap version: `1.0.0`;
- accepted authority decision: ADR-0034;
- accepted work package: Phase 0C-16;
- candidate exact head: `37d23449fda9a426f56ee8b09042dda91587a6d1`;
- exact-head workflow run: `29842137511`;
- retained artifact: `8499790872`;
- artifact archive digest: `sha256:82d6b452777e2c5e60c4d08bf88dd2c848d6b2570650b70a4eede633c8065d9f`;
- candidate squash merge: `2c24f9e6b0fc98d5e03605596db75d7495796353`;
- accepted-state exact head: `5860b4bfe177aa375fb2fa4305d62dbe3d2141e1`;
- permanent accepted-state workflow run: `29844040274`;
- retained accepted-state artifact: `8500540358`;
- accepted-state archive digest: `sha256:6f5229fe850d8b6f6f083b09f2c5f53189f3edbf38d4f28b9d2878ab0c78862d`;
- operative authority acceptance merge: `66bd2410d4c777cd3fd3278107f40fe425e875e9`.

The accepted programme is:

```text
P00 Master-plan authority closure — COMPLETE
P01 Physical-host and ADR-0033 closure — ACTIVE / BLOCKED ON EXACT PHYSICAL HOST
Programme A Online Ptah Alpha — PLANNED / NOT AUTHORIZED
Programmes B–F — PLANNED
```

## Accepted cross-cutting archive formation

```text
ADR-0035: ACCEPTED
Phase 0C-17: COMPLETE
protocol version: 1.0.0
formation-authority candidate merge: c4973cbf4d02a34f14a7aefa85b8e2ea7b392752
formation-authority operative acceptance merge: 40ca127c6d3054bda785061090acefaefcf4cd42
Campaign 001: ACCEPTED COMPLETE
AF01–AF10: ACCEPTED COMPLETE
obligations closed: 98 of 98
accepted archive records: 91
completed blocked outcomes: 7
remaining evidence: 0
AF11: DOES NOT EXIST
```

Read when doing archive/recovery work:

- `planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md`;
- `archive/CAMPAIGN-001-FORMATION-MANIFEST.md`;
- `archive/campaign-001/ACCEPTANCE.md`;
- `archive/campaign-001/OPERATIVE-BINDING.md`;
- `archive/campaign-001/OPERATIVE-STATE.json`;
- `archive/ARCHIVE-RECORD-TEMPLATE.md`;
- accepted ADR-0035;
- accepted Phase 0C-17 work package.

Formation-authority candidate evidence: exact head `58b577b6793ec28de084e6d712c3c1e88bfe2d3a`, run `29853954659`, artifact `8504497355`, digest `sha256:936740e8087e6f7f0a58b3d731117fcb9a4861edfd20c396fb1bb20a7d4f18f4`.

Formation-authority accepted evidence: exact head `b96b84d17cf03e905bd0b1baf3c46b8aec09334a`, run `29855000427`, artifact `8504901567`, digest `sha256:9d96a1f299060e50ab63132d1bb1da0903d5435f73acdf4fa9e394cdcccf21d2`. Operative merge: `40ca127c6d3054bda785061090acefaefcf4cd42`.

Campaign AF04–AF10 candidate evidence: exact head `6eed78a9acca4614d9dd99c175681ba4ff476c8e`, run `30076705760`, artifact `8590135926`, digest `sha256:c7e3a9be59b5ba859b67a1b352fee32b2c43c44e774e3e70b07aaac857d8b3a7`, validation SHA-256 `7a53cdccfb520cbc29dfb842b952dbcbca5800f02ed1ce2a67b8a3743180d247`, candidate merge `ec78db9ce5b44a5d05465a1cb6271c7e6594079e`.

Campaign accepted-state evidence: exact head `03e027b5b2898b096652688157623ad31d3c16d7`, run `30078410676`, artifact `8590777774`, digest `sha256:9a9948862f7c8af5f6551a239a19091c2e37a5565442be0ff9c90459932a2398`, validation SHA-256 `f78ebcbe2781480ce90472b5d373cc282cb13628acc3e7dcc853f8abe6ebab7f`. Operative acceptance merge: `f7280e4af1323096196ab0534e5f76b9375fd6d7`.

The seven completed blocks are `D047`, `D065`, `I018`, `I008`, `I019`, `I024` and `I025`. They remain source/rights recovery blocks with retained safe next actions; campaign closure does not grant source reuse.

The campaign is an archive/recovery workflow, not proof that a 200-agent runtime exists and not runtime implementation authority.

P01 physical-host closure remains the exact next authorization action.

## Neutral Ptah substrate correction

The Workspace donor was corrected and merged as `8a8d620c5227a6508145cd4a30f4f45142bfabe9` after all ten exact-head workflows passed at `5a95c577edf366bad1d8949ee37c17b81f296254`.

Use this boundary:

```text
Ptah = neutral platform and mechanical access enforcement
Hunter = intelligence, context selection and coordination
Sergeant = independent reviewer producing Sergeant results
Human/calling application = intent, approval, acceptance and release
```

Ptah does not select context, rank sources, approve work, issue review verdicts, promote candidates or choose the next agent/action. Private correction merge `fc8ac4c42a3358da37c4866879543a5d7c4d1885` is bound in `planning/PTAH-NEUTRAL-SUBSTRATE-CORRECTION-MERGE.md`.

Campaign 001 is ACCEPTED COMPLETE; all ten formation results remain non-authorizing archive evidence.

## Accepted diagnostic advisory and efficient worker boundary

```text
ADR-0036: ACCEPTED
Phase 0C-18: COMPLETE
protocol version: 1.0.0
candidate merge: fbc4ee80284a2d7ea38a44fdbfa90f0348b875ae
```

Ptah may diagnose its own platform condition and ask a caller for an upgrade. For a caller-submitted job and Recipe/Plan, Ptah may execute `max(20, human-equivalent workers × 10)` bounded workers with independent checks and checkpoints.

Ptah may not choose caller work, invent semantic scope, approve a result, approve/install its own upgrade or treat acknowledgement as resolution.

Evidence: exact head `d2608ba7c619c1c402091edd619a4b29813ee9a7`, run `29986975197`, artifact `8555395796`, digest `sha256:72025fb0aa5a969ea73abe95d7352f7cf14f1c847943955bd768a46d964a4c61`. Full record: `planning/PTAH-DIAGNOSTIC-WORKER-AUTHORITY-ACCEPTANCE.md`.

Campaign 001 archive closure does not change the Phase 0C-18 diagnostic authority boundary and does not authorize implementation.

## Exact next action

On the exact Ubuntu Server 24.04.4 LTS / x86_64 / `6.8.0-136-generic` physical proof host, check out the selected clean reviewed `Ptah-space` preparation commit and run:

```bash
python3 tools/run_pinned_host_proof.py \
  --repo-root . \
  --output evidence/phase0c/pinned-host-candidate
```

Require `proof_eligible: true`, empty failure sets and complete package/APT artifact evidence. Then independently retain the same exact bundle:

```bash
python3 tools/retain_verified_pinned_host_evidence.py \
  --repo-root . \
  --bundle-dir evidence/phase0c/pinned-host-candidate \
  --output-dir evidence/phase0c/pinned-host-durable-candidate
```

Review and explicitly accept host identity, capabilities, installed packages, package artifacts, APT sources/indexes, durable bytes and repository binding.

## Remaining authorization sequence

```text
Physical pinned-host proof
→ package/package-artifact acceptance
→ durable bundle commit and acceptance
→ final Phase 0C consistency review
→ ADR-0033 acceptance
→ explicit Runtime implementation: AUTHORIZED
→ A01 becomes READY
```

## Hard boundary

```text
Master Plan: ACCEPTED
Implementation roadmap: ACCEPTED
ADR-0034: ACCEPTED
Archive Campaign 001: ACCEPTED COMPLETE
Physical-host proof: OPEN
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```

No chat, model or owner-intent statement may replace the missing physical evidence and reviewed ADR-0033 closure.