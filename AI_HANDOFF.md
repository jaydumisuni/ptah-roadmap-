# Ptah durable AI/chat handoff

Last updated: 2026-07-21

Status: Phase 0C master-plan closure active — runtime implementation remains unauthorized

## Read first

A new chat, model or agent must read in this order:

1. `AI_HANDOFF.md` — this checkpoint;
2. `CURRENT_STATE.md` — canonical current phase and selected action;
3. `master-plan-index.json` — machine-readable authority, blockers and next step;
4. `MASTER_PLAN.md` — complete product and operating plan;
5. `IMPLEMENTATION_ROADMAP.md` — dependency-ordered delivery programme;
6. `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`;
7. `planning/MASTER-PLAN-RECONCILIATION.md`;
8. `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`;
9. `PROGRESS.md`;
10. `DECISIONS.md` and the referenced ADRs;
11. `MEMORY_PROTOCOL.md`;
12. relevant current source and open work in `jaydumisuni/Ptah-space`.

Do not ask the owner to repeat information recoverable from these records.

## Why this branch exists

The earlier repository had strong donor research, frozen contracts and Phase 0C evidence, but the authoritative planning layer was incomplete and stale:

- `MASTER_ROADMAP.md` was architecture-heavy and still marked Phase 0B active;
- `DECISIONS.md` stopped at WP07;
- the Phase 1–13 progress list did not form a dependency-complete programme;
- no concise machine-readable handoff bound plan, roadmap, blockers and exact next action.

The owner explicitly required:

```text
Recover every requirement and design decision
→ write the complete Ptah Master Plan
→ review missing product and operational scope
→ derive the detailed implementation roadmap
→ reconcile WP01–WP14 and Phase 0C
→ close physical-host evidence
→ accept ADR-0033
→ authorize implementation
```

The owner also required save-as-you-go recovery so any chat or AI can continue.

## Current branch

Repository: `jaydumisuni/ptah-roadmap-`

Branch:

```text
phase0c-master-plan-roadmap-closure
```

Durable checkpoints already committed:

- `a413dd010e248419514b50e8297154719f00fc91` — recovered requirements and decisions ledger;
- `566a166054f894a7bb9cf37d33b558c9da481e24` — complete Master Plan candidate;
- `57453b2b074cdea7cd905f0a5331d2edb7d707a0` — detailed implementation roadmap candidate;
- `85ded1c782ddd83e030319a2088b03c90054444c` — WP01–WP14 and Phase 0C reconciliation;
- `27e8b09109455f234867f05a65f6cff2b0563496` — physical-host through authorization closure procedure.

## Completed in this work session

- recovered product requirements, architecture laws, participant roles, operating modes, domain scope, security, storage, recovery and release intent;
- identified stale and missing authority records;
- wrote a complete product and operating Master Plan;
- converted Phase 1–13 headings and the existing fourteen-task first-slice map into a dependency-ordered Programme 0 plus Programmes A–F;
- reconciled the new plan against every frozen work package and all Phase 0C records;
- confirmed no new Core entity or immediate WP01–WP14 reopening is required;
- recorded the exact external physical-host and authorization sequence.

## Work still required on this branch

1. add `master-plan-index.json`;
2. add Phase 0C-16 work-package evidence and plan-authority ADR;
3. repair `README.md`, `MEMORY_PROTOCOL.md`, `DECISIONS.md`, `DONOR_RECOVERY.md`, `MASTER_ROADMAP.md`, `PROGRESS.md` and `CURRENT_STATE.md`;
4. add fail-closed consistency validation and tests;
5. open a draft pull request;
6. run review and exact-head checks;
7. merge only after the Master Plan and implementation roadmap are internally consistent and non-authorizing.

## After the planning merge

The next blocker is external and physical:

```bash
python3 tools/run_pinned_host_proof.py \
  --repo-root . \
  --output evidence/phase0c/pinned-host-candidate
```

Run only on Ubuntu Server 24.04.4 amd64 with kernel `6.8.0-136-generic`, exact required capabilities, complete local APT metadata and a clean exact `Ptah-space` commit.

Then independently retain the candidate:

```bash
python3 tools/retain_verified_pinned_host_evidence.py \
  --repo-root . \
  --bundle-dir evidence/phase0c/pinned-host-candidate \
  --output-dir evidence/phase0c/pinned-host-durable-candidate
```

Review and accept the host, installed packages, package artifacts, APT boundary and durable retention before ADR-0033 acceptance.

## Hard boundary

Current state:

```text
Master Plan: CANDIDATE
Implementation roadmap: CANDIDATE
Physical-host proof: OPEN
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```

Do not create runtime features, deploy Nodes, claim a working Workspace or change authorization before the reviewed closure sequence passes.

## Safest next action

Continue the control-book repair and machine-readable validation on `phase0c-master-plan-roadmap-closure`. Do not return to donor research or runtime implementation unless a concrete missing requirement is discovered.
