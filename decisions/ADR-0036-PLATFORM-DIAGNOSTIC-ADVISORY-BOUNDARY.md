# ADR-0036 — Platform diagnostic advisory and efficient worker execution boundary

Status: proposed — review with Phase 0C-18

Recorded: 2026-07-23

## Context

Ptah is already defined as the neutral world and execution substrate, not the thinker that chooses user work. That boundary must remain intact.

The owner clarified two useful platform behaviors:

1. Ptah may detect that its own operating environment is broken, degraded, incompatible or missing a required capability and may ask its operator for an upgrade without choosing what the operator wants to accomplish.
2. After a caller has supplied a job and selected an execution recipe, Ptah may use the Sergeant-derived ten-for-two worker pattern to perform that job faster and more efficiently through bounded parallel workers and independent checks.

Ptah already has frozen primitives for Node and Provider health, capability, limitation, Generation, Workspace, Activity/Operation/Attempt outcomes, Recipe/Plan/Run/Step, Reservation/Grant/Lease/Fence, Events, Receipts, Evidence, Views and Artifacts. The missing clarification is how those primitives support bounded diagnostics and efficient worker execution without reintroducing task-selection, verdict or approval authority.

## Decision

Adopt `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md` as the candidate boundary for platform self-diagnostics, upgrade requests and caller-selected ten-for-two worker execution.

### Allowed diagnostic behavior

Ptah may:

- compare caller- or contract-defined expected conditions with observed platform evidence;
- detect a missing capability, incompatible version, resource shortage, degraded Provider, repeated failure pattern or failed post-condition;
- preserve exact negative and partial evidence;
- emit an evidence-backed diagnostic advisory;
- ask an authorized caller for an upgrade, additional capability, replacement Provider, resource increase or operator inspection;
- mechanically refuse an operation when an explicit contract or configured Policy precondition is absent;
- recheck the condition after a caller-authorized change.

### Allowed worker-execution behavior

For a caller-submitted job and caller-selected Recipe or Plan, Ptah may:

- apply `worker capacity = max(20, human-equivalent workers × 10)`;
- instantiate declared worker roles and bounded Activities;
- run independent primary and verifier Attempts concurrently;
- place workers on compatible Nodes/Providers within configured Reservations, Grants, Leases and Fences;
- preserve worker inputs, outputs, failures, checkpoints, Receipts and evidence;
- retry or replace failed Attempts only where the submitted Recipe and Policy permit it;
- apply the submitted deterministic merge rule;
- return complete, partial, conflicting, failed or inconclusive formation results.

### Forbidden behavior

Ptah may not:

- choose the user's goal or work;
- invent semantic subtasks not present in the submitted job, Recipe, Plan or coordinating application;
- infer hidden priorities;
- reprioritize Activities outside submitted Policy;
- decide which worker conclusion is correct beyond configured deterministic checks;
- treat worker completion as caller acceptance;
- approve, purchase, install or activate its own upgrade;
- select a vendor from hidden preference;
- treat an advisory as an accepted decision;
- mark resolution from acknowledgement alone;
- block unrelated work when its requirements remain satisfied;
- become Hunter, Sergeant or the final authority.

### Representation

No new Core entity is required.

A diagnostic advisory is a typed View or Artifact composed from frozen Node, Provider, capability, health, Activity, Attempt, Event, Receipt, Claim/Finding and Evidence records.

A worker formation is a caller-defined Recipe/Plan/Run composed of Workspace, Activity, Operation, Attempt, Event, Receipt, Evidence, Reservation, Grant, Lease, Fence, View and Artifact records. A caller-approved upgrade is a separate caller-submitted Activity.

### Sergeant patterns borrowed

The bounded diagnostic pattern is:

```text
explicit obligation
→ observed evidence
→ missing condition or contradiction
→ bounded deficiency report
→ escalation to responsible caller
→ independent post-condition verification
```

The bounded execution pattern is:

```text
caller-submitted job and formation recipe
→ ten-for-two worker slots
→ bounded parallel Activities
→ independent checks and checkpoints
→ configured merge
→ result returned to caller or reviewer
```

Ptah does not borrow Sergeant's verdict, rank, mission-selection, scope-selection or approval authority.

## Consequences

- Ptah remains neutral regarding user intent while becoming more useful and maintainable.
- Missing platform capabilities can be explained instead of appearing as generic failures.
- Humans and applications receive evidence before deciding whether to upgrade.
- Caller-supplied jobs can use the existing concurrency model more efficiently without turning Ptah into the planner.
- Worker independence, partial failure and conflicting results remain visible.
- Hunter may define plans and recommend responses; Sergeant may define or review formations; Ptah stores and executes without choosing.
- Existing frozen contracts remain sufficient.
- Programme A gains explicit diagnostic and worker-formation proof obligations.

## Non-effects

This decision does not:

- authorize implementation;
- reopen WP01–WP14;
- accept ADR-0033;
- start AF03;
- change P01;
- claim either subsystem already exists;
- permit autonomous self-modification;
- permit Ptah to invent work or approve a result.

## Acceptance conditions

ADR-0036 may be accepted when:

1. the diagnostic boundary is explicit and evidence-backed;
2. the ten-for-two pattern applies only to caller-submitted jobs and Recipes/Plans;
3. task selection, semantic decomposition, result acceptance and upgrade approval remain caller-owned;
4. the design maps only to frozen primitives;
5. Master Plan and implementation roadmap placement are exact;
6. missing capability, degraded Provider, repeated failure and worker-failure examples are covered;
7. worker independence, checkpoint, retry and conflict-retention rules are explicit;
8. autonomous install, self-approval and unrelated-work blocking are explicitly rejected;
9. Hunter/Sergeant roles remain external applications;
10. AF03 remains not started;
11. P01, ADR-0033 and runtime non-authorization remain unchanged;
12. exact-head validation and adversarial tests pass.
