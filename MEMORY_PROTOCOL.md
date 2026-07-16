# Ptah Chat Recovery and Memory Protocol

This repository is the durable memory source for continuing Ptah work across chats, models, devices, and time.

A chat must not rely on conversational memory alone.

---

# 1. Mandatory recovery order

Before evaluating, planning, designing, editing, or building Ptah:

1. Read `CURRENT_STATE.md`.
2. Read `MASTER_ROADMAP.md`.
3. Read `PROGRESS.md`.
4. Read `DECISIONS.md`.
5. Read `DONOR_RECOVERY.md`.
6. Inspect the current state of `jaydumisuni/Ptah-space`.
7. Inspect any donor or internal repository directly related to the selected work item.

Do not ask the user to re-explain information that can be recovered from these sources.

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

- present in `MASTER_ROADMAP.md`;
- ordered after its dependencies;
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
3. `PROGRESS.md`;
4. `CURRENT_STATE.md`;
5. `DECISIONS.md` if architecture changed;
6. `DONOR_RECOVERY.md` if donor understanding changed;
7. `MASTER_ROADMAP.md` only when the accepted plan changed.

---

# 5. Completion language

Use these meanings consistently:

- **Built:** source exists.
- **Reviewed:** source and behavior were inspected against the accepted design.
- **Frozen:** the reviewed checkpoint is pinned.
- **Proven:** evidence confirms the frozen checkpoint satisfies the defined gate.
- **Complete:** proven and submitted/shipped where required.

Never collapse these into one claim.

---

# 6. Progress updates

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

# 7. Donor updates

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

# 8. Public repository updates

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

# 9. Recovery after interruption

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

# 10. Roadmap-change rule

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
