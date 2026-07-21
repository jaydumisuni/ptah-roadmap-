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
- candidate squash merge: `2c24f9e6b0fc98d5e03605596db75d7495796353`.

The accepted programme is:

```text
P00 Master-plan authority closure — COMPLETE
P01 Physical-host and ADR-0033 closure — ACTIVE / BLOCKED ON EXACT PHYSICAL HOST
Programme A Online Ptah Alpha — PLANNED / NOT AUTHORIZED
Programmes B–F — PLANNED
```

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
