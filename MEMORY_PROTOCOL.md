# Ptah Chat Recovery and Memory Protocol

This repository is the durable memory source for continuing Ptah work across chats, models, devices and time.

A chat must not rely on conversational memory alone.

---

# 1. Mandatory recovery order

Before evaluating, planning, designing, editing or building Ptah:

1. Read `AI_HANDOFF.md`.
2. Read `CURRENT_STATE.md`.
3. Read `master-plan-index.json`.
4. Read `MASTER_PLAN.md`.
5. Read `IMPLEMENTATION_ROADMAP.md`.
6. Read `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`.
7. Read `planning/MASTER-PLAN-RECONCILIATION.md`.
8. Read `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`.
9. Read `PROGRESS.md`.
10. Read `DECISIONS.md` and the relevant ADRs.
11. Read `DONOR_RECOVERY.md` when donor or requirement context is relevant.
12. Inspect the current state of `jaydumisuni/Ptah-space`.
13. Inspect any donor or internal repository directly related to the selected work item.

Do not ask the owner to re-explain information recoverable from these sources.

---

# 2. Truth hierarchy

When sources differ, prefer:

1. accepted ADRs and accepted owner decisions;
2. `CURRENT_STATE.md`;
3. frozen or proven implementation and conformance evidence;
4. current public implementation source;
5. accepted `MASTER_PLAN.md`;
6. accepted `IMPLEMENTATION_ROADMAP.md`;
7. frozen WP01–WP14 contracts and work packages;
8. `PROGRESS.md`;
9. donor and internal recovery records;
10. old chat text or conversational memory.

A newer date does not automatically make a source more authoritative. Determine whether the content represents an accepted change or merely an edit.

`AI_HANDOFF.md` and `master-plan-index.json` are recovery indexes. They summarize but do not override accepted decisions, frozen contracts or evidence.

---

# 3. Work-selection rule

No build work begins unless the exact item is:

- present in `MASTER_PLAN.md`;
- placed and ordered after its dependencies in `IMPLEMENTATION_ROADMAP.md`;
- mapped to frozen contracts and proof requirements;
- selected as current work in `CURRENT_STATE.md`;
- unticked, ready or active in `PROGRESS.md`;
- approved by the owner;
- assigned an explicit public/private boundary.

Ideas that are useful but not approved are recorded as parked candidates rather than silently implemented.

---

# 4. Work-session protocol

## Before work

- recover the exact roadmap and current checkpoint;
- identify the exact requirement and work-package ID;
- recover existing internal implementation;
- inspect relevant donors, source and licences;
- define the build and public/private boundary;
- define positive, negative and recovery proof before coding;
- identify the exact repository, branch and expected outputs.

## During work

- work only on the selected slice;
- preserve unrelated and unusual existing behavior until intent is understood;
- tie outputs and evidence to exact commits and Provider Generations;
- avoid broad cleanup unless it is part of the approved task;
- record failures, limitations and blocked outcomes honestly;
- create durable intermediate checkpoints during long work.

## After work

Update in this order:

1. implementation repository source and tests;
2. implementation evidence;
3. a durable intermediate checkpoint when the task is not yet finished;
4. `AI_HANDOFF.md`;
5. `master-plan-index.json`;
6. `PROGRESS.md`;
7. `CURRENT_STATE.md`;
8. `DECISIONS.md` when architecture or governance changed;
9. `DONOR_RECOVERY.md` when donor understanding changed;
10. `MASTER_PLAN.md` only when accepted product or operating intent changed;
11. `IMPLEMENTATION_ROADMAP.md` when sequencing, dependencies or proof gates changed.

---

# 5. Save-as-you-go checkpoint rule

Substantial work must be durably checkpointed before the full task is complete.

A checkpoint records:

- repository and branch;
- exact commit;
- completed files, work packages or Activities;
- active and incomplete work;
- failed attempts and limitations;
- retained evidence;
- blockers;
- safest next action;
- runtime authorization state.

`AI_HANDOFF.md` is the concise recovery entry. `master-plan-index.json` is the machine-readable entry.

A chat or model may not say work is safely recoverable when these durable records are stale.

## 5.1 Tenfold archive formation rule

Large recovery and archive campaigns use `planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md`.

The operating rule is:

```text
private force = max(20, human-equivalent workers × 10)
```

A standard twenty-private formation handles at most ten ordinary records through ten Primary Archivist / Independent Verifier pairs. Complex sources consume more pairs or escalate to 40/60/80–100/up to 120 privates rather than receiving weaker review.

Archive privates collect and challenge bounded evidence. They cannot promote truth, adopt donors, reopen frozen architecture, expand scope or authorize implementation. Archive Officers reconcile evidence; accepted review records promote only the bounded archive result.

Mandatory formation save points:

- mission and scope before evidence collection;
- after five reconciled records;
- after ten accepted records or formation completion;
- after a scope-changing blocker;
- before switching chat, model, operator or device.

`accepted for archive` does not mean a donor is adopted or that its claims become Ptah truth.

---

# 6. Completion language

Use these meanings consistently:

- **Planned:** accepted placement and dependency order exist.
- **Built:** source exists.
- **Reviewed:** source and behavior were inspected against the accepted design.
- **Frozen:** the reviewed checkpoint is pinned.
- **Proven:** evidence confirms the frozen checkpoint satisfies the defined gate.
- **Complete:** proven and submitted, merged or shipped where required.

Never collapse these into one claim.

---

# 7. Progress updates

Only tick a progress item when its evidence can be identified.

For each completed item, record where possible:

- repository;
- branch and commit;
- tests or commands;
- Artifacts, screenshots, logs or reports;
- limitations;
- reviewer outcome;
- next dependency.

If implementation exists but proof is incomplete, leave the item active or in review.

---

# 8. Donor updates

For every donor studied, preserve:

- canonical upstream;
- contributor fork if relevant;
- pinned commit or release;
- licence;
- last meaningful activity;
- exact files or components read;
- verified capability;
- limitation;
- what Ptah may inherit;
- what Ptah must not inherit;
- integration classification;
- exit strategy;
- proof needed.

A repository is not accepted because it is popular, modern or impressive.

---

# 9. Public repository updates

`Ptah-space` should receive only:

- current implementation source;
- public-safe architecture necessary to understand and contribute to that source;
- public contracts and schemas;
- tests;
- contributor and operator documentation;
- public progress that has been earned.

It should not receive:

- the private Master Plan or implementation programme;
- internal consumers or company operating chains;
- private OS integration plans;
- private donor notes;
- customer, Device, payment or employee data;
- restricted recovery knowledge;
- credentials or deployment secrets.

---

# 10. Recovery after interruption

When work stops unexpectedly, `CURRENT_STATE.md` and `AI_HANDOFF.md` must state:

- exact active phase and work package;
- exact repository and branch;
- last known commit;
- what was attempted;
- what succeeded;
- what failed;
- incomplete files or Activities;
- evidence available;
- blockers;
- safest next action;
- runtime authorization state.

A new chat resumes from that checkpoint rather than restarting the task from memory.

---

# 11. Plan and roadmap change rule

A plan or roadmap change requires an explicit explanation of:

- the problem the change solves;
- new evidence;
- affected product scope and programmes;
- dependencies moved or added;
- existing work reused;
- work superseded;
- public/private impact;
- whether frozen contracts require reopening;
- whether the change is active, parked, researched or rejected.

After approval, update the affected authority records together:

- `MASTER_PLAN.md` when product or operating intent changes;
- `IMPLEMENTATION_ROADMAP.md` when sequencing, dependencies or proof changes;
- `DECISIONS.md` and the relevant ADR when architecture or governance changes;
- `PROGRESS.md` and `CURRENT_STATE.md`;
- `AI_HANDOFF.md` and `master-plan-index.json`.

Frozen contract changes additionally require a versioned reopening ADR, migration, fixtures and conformance evidence.
