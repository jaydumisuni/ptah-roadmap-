# Ptah Chat Recovery and Memory Protocol

This repository is the durable memory source for continuing Ptah work across chats, models, devices, and time.

A chat must not rely on conversational memory alone.

---

# 1. Mandatory recovery order

Before evaluating, planning, designing, editing, or building Ptah:

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

1. accepted decision records;
2. current state;
3. frozen/proven implementation evidence;
4. current public implementation source;
5. master roadmap;
6. progress ledger;
7. donor records;
8. old chat text or memory.

A newer date does not automatically make a source more authoritative. Determine whether the content represents an accepted change or merely an edit.

---

# 3. Work-selection rule

No build work begins unless the exact item is:

- present in `MASTER_PLAN.md`;
- placed and ordered after its dependencies in `IMPLEMENTATION_ROADMAP.md`;
- selected as current work in `CURRENT_STATE.md`;
- unticked or active in `PROGRESS.md`;
- approved by the user.

Ideas that are useful but not approved are recorded as parked candidates rather than silently implemented.

---

# 4. Work-session protocol

## Before work

- recover the roadmap and current checkpoint;
- identify the exact requirement;
- recover existing internal implementation;
- inspect relevant donors and licences;
- define the build boundary;
- define proof before coding;
- confirm the public/private boundary.

## During work

- work only on the selected slice;
- preserve unrelated and unusual existing behavior until intent is understood;
- keep outputs and evidence tied to the exact checkpoint;
- avoid broad cleanup unless it is part of the approved task;
- record blockers honestly.

## After work

Update in this order:

1. implementation repository source and tests;
2. implementation evidence;
3. a durable intermediate checkpoint when the task is not yet finished;
4. `AI_HANDOFF.md`;
5. `master-plan-index.json`;
6. `PROGRESS.md`;
7. `CURRENT_STATE.md`;
8. `DECISIONS.md` if architecture or governance changed;
9. `DONOR_RECOVERY.md` if donor understanding changed;
10. `MASTER_PLAN.md` only when accepted product/operating intent changed;
11. `IMPLEMENTATION_ROADMAP.md` when sequencing, dependencies or proof gates changed.

---

# 5. Save-as-you-go checkpoint rule

Substantial work must be durably checkpointed before the full task is complete.

A checkpoint records:

- repository and branch;
- exact commit;
- completed files or work packages;
- active and incomplete work;
- failures and limitations;
- retained evidence;
- blockers;
- safest next action;
- runtime authorization state.

`AI_HANDOFF.md` is the concise recovery entry. `master-plan-index.json` is the machine-readable entry. They summarize but do not replace accepted decisions, contracts or evidence.

A chat or model may not say work is safely recoverable when these durable records are stale.

---

# 11. Completion language

Use these meanings consistently:

- **Built:** source exists.
- **Reviewed:** source and behavior were inspected against the accepted design.
- **Frozen:** the reviewed checkpoint is pinned.
- **Proven:** evidence confirms the frozen checkpoint satisfies the defined gate.
- **Complete:** proven and submitted/shipped where required.

Never collapse these into one claim.

---

# 11. Progress updates

Only tick a progress item when its evidence can be identified.

For each completed item, record where possible:

- repository;
- branch and commit;
- tests or commands;
- artifacts/screenshots/logs;
- limitations;
- reviewer outcome;
- next dependency.

If implementation exists but proof is incomplete, leave the item active or in review.

---

# 11. Donor updates

For every donor studied, preserve:

- canonical upstream;
- contributor fork if relevant;
- pinned commit or release;
- licence;
- last meaningful activity;
- exact files/components read;
- verified capability;
- limitation;
- what Ptah may inherit;
- what Ptah must not inherit;
- integration classification;
- exit strategy;
- proof needed.

A repository is not accepted because it is popular, modern, or impressive.

---

# 11. Public repository updates

`Ptah-space` should receive only:

- current implementation source;
- public-safe architecture necessary to understand and contribute to that source;
- public contracts and schemas;
- tests;
- contributor and operator documentation;
- public progress that has been earned.

It should not receive:

- private master roadmap;
- internal consumers;
- private OS integration plans;
- company operation chains;
- private donor notes;
- credentials or deployment secrets.

---

# 11. Recovery after interruption

When work stops unexpectedly, `CURRENT_STATE.md` must state:

- exact active phase;
- exact repository and branch;
- last known commit;
- what was attempted;
- what succeeded;
- what failed;
- incomplete files or activities;
- evidence available;
- safest next action.

A new chat resumes from that checkpoint rather than restarting the task from memory.

---

# 11. Roadmap-change rule

A roadmap change requires an explicit explanation of:

- the problem the change solves;
- new evidence;
- affected phases;
- dependencies moved or added;
- existing work reused;
- work superseded;
- public/private impact;
- whether the change is active, parked, researched, or rejected.

After approval, update `MASTER_ROADMAP.md`, `DECISIONS.md`, `PROGRESS.md`, and `CURRENT_STATE.md` together.
