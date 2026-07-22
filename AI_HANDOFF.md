# Ptah durable AI/chat handoff

Last updated: 2026-07-21

Status: Master Plan and implementation roadmap accepted — P01 physical-host closure active — runtime implementation unauthorized

## Read first

1. `AI_HANDOFF.md`
2. `CURRENT_STATE.md`
3. `master-plan-index.json`
4. `MASTER_PLAN.md`
5. `IMPLEMENTATION_ROADMAP.md`
6. `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`
7. `planning/MASTER-PLAN-RECONCILIATION.md`
8. `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`
9. `PROGRESS.md`
10. `DECISIONS.md` and the referenced ADRs
11. `MEMORY_PROTOCOL.md`
12. current source and evidence in `jaydumisuni/Ptah-space`

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
candidate merge: c4973cbf4d02a34f14a7aefa85b8e2ea7b392752
operative acceptance merge: 40ca127c6d3054bda785061090acefaefcf4cd42
AF01: ACCEPTED COMPLETE
AF02: ACCEPTED COMPLETE
AF03: READY / NOT STARTED
```

Read when doing archive/recovery work:

- `planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md`;
- `archive/CAMPAIGN-001-FORMATION-MANIFEST.md`;
- `archive/ARCHIVE-RECORD-TEMPLATE.md`;
- accepted ADR-0035;
- accepted Phase 0C-17 work package.

Candidate evidence: exact head `58b577b6793ec28de084e6d712c3c1e88bfe2d3a`, run `29853954659`, artifact `8504497355`, digest `sha256:936740e8087e6f7f0a58b3d731117fcb9a4861edfd20c396fb1bb20a7d4f18f4`.

Accepted-state evidence: exact head `b96b84d17cf03e905bd0b1baf3c46b8aec09334a`, run `29855000427`, artifact `8504901567`, digest `sha256:9d96a1f299060e50ab63132d1bb1da0903d5435f73acdf4fa9e394cdcccf21d2`. Operative merge: `40ca127c6d3054bda785061090acefaefcf4cd42`. Full record: `planning/TENFOLD-ARCHIVE-AUTHORITY-ACCEPTANCE-MERGE.md`.

Campaign 001 covers 98 source obligations with ten twenty-private formations and one primary/verifier pair per obligation. AF01 is accepted complete with nine accepted archive records and one completed MiniRouter source-reuse block. Evidence: exact head `f60e340cb856d50e88b4279147a933d838fce759`, run `29862087745`, artifact `8507695005`, candidate merge `0a35a8a904bdf235fa4989ea05b684443d5a879a`, acceptance record `archive/campaign-001/af01/ACCEPTANCE.md`. AF01 accepted closure merged as `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`. AF02 is accepted complete with ten accepted archive records and zero blocks. Evidence: exact head `b710574b99269647cdd9029db5a2b217642aa344`, run `29875542752`, artifact `8512821506`, candidate merge `58d89dfd1d5348cc8423222e3aff256ee041dce2`, acceptance record `archive/campaign-001/af02/ACCEPTANCE.md`. AF03 is READY / NOT STARTED.

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

AF03 remains READY / NOT STARTED.

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
Physical-host proof: OPEN
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```

No chat, model or owner-intent statement may replace the missing physical evidence and reviewed ADR-0033 closure.
