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

## Accepted requirement

Which exact Ptah requirement or closure-matrix row does this work satisfy?

## Internal foundation

What internal projects, code, architecture, decisions, tests, intentional constraints, or unfinished work already exist?

## Primary capability donor

Which inspected donor provides the strongest central capability? Record pinned commit or release, licence, exact components, verified strengths and known missing capabilities.

## Completion donor set

Which additional donors close the primary donor's missing capabilities? For each one record:

- exact gap it closes;
- pinned commit or release;
- licence;
- files/components studied;
- limitations;
- integration boundary.

A subsystem may not proceed with this section empty unless evidence proves the primary donor and native Ptah layer already cover the complete requirement.

## Mature upstream machinery

Which standards, runtimes, protocols or engines should Ptah use rather than recreate?

## Fallback or exit donor

What replacement path exists if the selected donor, service or engine becomes unsuitable, abandoned, incompatible or incorrectly licensed?

## Native Ptah gap

What must Ptah itself build that the internal and external donor composition does not provide?

## Donor completeness check

Evaluate the assembled set where relevant:

- [ ] Core engine or machinery
- [ ] Stable API or adapter boundary
- [ ] Persistence
- [ ] Concurrency
- [ ] Restart and reconnect recovery
- [ ] Cancellation and failure handling
- [ ] Logs, metrics, traces and evidence
- [ ] Local/owned deployment
- [ ] Online deployment
- [ ] Future multi-node operation
- [ ] Cross-platform requirements
- [ ] Credential/security boundary
- [ ] Licence compatibility
- [ ] Maintained upstream or exit strategy
- [ ] Deterministic and live validation

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
- donor-composition proof;
- artifacts/evidence;
- performance target;
- known limitations.

---

# Engineering cycle

## 1. Understand

- [ ] Recovery complete.
- [ ] Primary donor inspected.
- [ ] Primary donor gaps recorded.
- [ ] Completion donors inspected against those gaps.
- [ ] Internal overlap recovered.
- [ ] Mature upstream machinery selected.
- [ ] Exit strategy recorded.
- [ ] Licence decisions recorded.
- [ ] Native Ptah boundary isolated.
- [ ] Architecture boundary approved.
- [ ] Proof plan approved.
- [ ] Roadmap and current state saved.

## 2. Build

- [ ] Approved slice implemented.
- [ ] Unrelated work preserved.
- [ ] Tests added.
- [ ] Observability added.
- [ ] Failure paths handled.

## 3. Review

- [ ] Source reviewed.
- [ ] Architecture reviewed.
- [ ] Donor composition reviewed.
- [ ] Public/private boundary reviewed.
- [ ] Dependency and licence review repeated.
- [ ] Unintended changes checked.

## 4. Freeze

- [ ] Commit pinned.
- [ ] Donor versions pinned.
- [ ] Schemas/contracts pinned.
- [ ] Build/runtime environment recorded.
- [ ] Known limitations recorded.

## 5. Prove

- [ ] Deterministic proof passed.
- [ ] Live proof passed.
- [ ] Donor-composition proof passed.
- [ ] Concurrency proof passed where applicable.
- [ ] Recovery/failure proof passed where applicable.
- [ ] Exit path remains possible.
- [ ] Artifacts, logs, screenshots, hashes, and commands saved.

## 6. Submit / Ship

- [ ] Review verdict accepted.
- [ ] Merge/release approved.
- [ ] Public implementation updated.
- [ ] `PROGRESS.md` updated.
- [ ] `CURRENT_STATE.md` updated.
- [ ] Requirement Closure Matrix updated.
- [ ] Decisions and donor records updated if necessary.

---

# Completion record

**Frozen commit:**  
**Evidence location:**  
**Donor composition used:**  
**Verdict:**  
**Known limitations:**  
**Exit strategy:**  
**Next dependency:**  
