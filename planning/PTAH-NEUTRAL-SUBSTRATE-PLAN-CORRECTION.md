# Ptah neutral substrate plan correction

Status: correction candidate under review — no runtime implementation authorization

Recorded: 2026-07-22

## Owner correction

The Master Plan established the correct foundation before later wording drifted:

```text
Ptah is the world, not the thinker.
The caller provides intent, reasoning, policy, priority, business judgment and acceptance criteria.
```

Ptah is comparable to a powerful computer, operating system and digital workspace. It provides the platform required to perform work. It does not decide what the platform should be used for.

## Drift being corrected

Later plan and AI Project Workspace language incorrectly assigned some of the following to Ptah:

- context compilation and relevance selection;
- source-authority ranking;
- objective and blocker selection;
- approval and candidate promotion;
- review-packet construction;
- next-action choice;
- deciding which agent should act.

That language did not represent a new owner decision. It contradicted the existing product principle and is superseded by this correction.

## Correct responsibility boundary

### Ptah

Ptah supplies neutral mechanical capabilities:

- Workspaces, Sessions and Activities;
- Objects, Revisions, Views and Artifacts;
- storage, transfer, synchronization and recovery;
- terminals, Processes, browsers, containers, VMs, Applications and Devices;
- Facilities, Providers and exact Generations;
- configured Grants, Leases and Fences;
- Events, Receipts, logs and checkpoints;
- APIs for callers to create, read, update, execute and observe authorized state.

Ptah does not decide meaning, truth, priority, correctness, approval, review verdicts or next actions.

### Hunter

Hunter supplies intelligence, context selection, planning, coordination, source judgments, Provider choice and next-action proposals.

### Sergeant

Sergeant independently reviews frozen candidates using Ptah compute, storage and tools. Sergeant issues Sergeant's result. Ptah only runs and stores the review workload and evidence.

### Human or calling application

The human or calling application owns intent, configured access decisions, acceptance, rejection, release and final authorization.

## Mechanical enforcement is not judgment

Ptah may enforce configured Grants, Leases, Fences, quotas, capability requirements and access boundaries. This is platform behavior, like an operating system enforcing permissions.

Ptah does not decide who deserves access, whether an approval is wise or whether the result should be accepted.

## Documents requiring reconciliation

At minimum:

- `MASTER_PLAN.md` sections 3, 5, 6.5, 10.6 and 11;
- `IMPLEMENTATION_ROADMAP.md` wherever context compilation or authority judgment is assigned to Ptah;
- `AI_HANDOFF.md` and `CURRENT_STATE.md` donor summaries;
- `master-plan-index.json` machine boundary;
- Phase 0C-15 Workspace donor record;
- public `Ptah-space` Workspace donor/profile/bridge candidate.

## AF03 and authorization effect

- AF03 remains `READY / NOT STARTED` while the plan boundary is repaired;
- Phase 0A remains frozen;
- P01 remains active;
- ADR-0033 remains proposed;
- runtime implementation remains unauthorized.
