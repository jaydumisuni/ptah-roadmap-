# Ptah Work Item Template

Use this template before any implementation task is approved.

---

# Work item

**ID:**  
**Title:**  
**Roadmap phase:**  
**Status:** NOT STARTED  
**Owner:**  
**Target repository:**  
**Target branch:**  

## Problem

What exact problem is being solved?

## Why it matters

Why is this needed for Ptah?

## Why now

Why is this the correct dependency order?

## Existing foundation

What internal projects, code, architecture, decisions, tests, or unfinished work already exist?

## External donors

Which donors were inspected? Record pinned commits, licences, exact components, limitations, and exit strategies.

## Native Ptah gap

What must Ptah itself build that existing work does not provide?

## Public/private boundary

What may appear in the public Ptah repository? What remains private?

## Dependencies

What must be complete or frozen first?

## Build boundary

List exactly what is included.

## Explicit exclusions

List what must not be changed during this work item.

## Contracts affected

- Objects:
- Activities:
- Workspaces:
- Nodes:
- Facilities/plugins:
- Storage:
- Sessions:
- Events:
- Public API:

## Migration and compatibility impact

How will existing objects, sessions, schemas, or nodes remain compatible?

## Proof plan

Define proof before coding:

- deterministic tests;
- live runtime test;
- concurrency test;
- recovery test;
- failure test;
- artifacts/evidence;
- performance target;
- known limitations.

---

# Engineering cycle

## 1. Understand

- [ ] Recovery complete.
- [ ] Donors inspected.
- [ ] Licence decisions recorded.
- [ ] Architecture boundary approved.
- [ ] Proof plan approved.

## 2. Build

- [ ] Approved slice implemented.
- [ ] Unrelated work preserved.
- [ ] Tests added.
- [ ] Observability added.
- [ ] Failure paths handled.

## 3. Review

- [ ] Source reviewed.
- [ ] Architecture reviewed.
- [ ] Public/private boundary reviewed.
- [ ] Dependency and licence review repeated.
- [ ] Unintended changes checked.

## 4. Freeze

- [ ] Commit pinned.
- [ ] Schemas/contracts pinned.
- [ ] Build/runtime environment recorded.
- [ ] Known limitations recorded.

## 5. Prove

- [ ] Deterministic proof passed.
- [ ] Live proof passed.
- [ ] Concurrency proof passed where applicable.
- [ ] Recovery/failure proof passed where applicable.
- [ ] Artifacts, logs, screenshots, hashes, and commands saved.

## 6. Submit / Ship

- [ ] Review verdict accepted.
- [ ] Merge/release approved.
- [ ] Public implementation updated.
- [ ] `PROGRESS.md` updated.
- [ ] `CURRENT_STATE.md` updated.
- [ ] Decisions and donor records updated if necessary.

---

# Completion record

**Frozen commit:**  
**Evidence location:**  
**Verdict:**  
**Known limitations:**  
**Next dependency:**  
