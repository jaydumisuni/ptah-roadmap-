# ADR-0036 — Platform diagnostic advisory boundary

Status: proposed — review with Phase 0C-18

Recorded: 2026-07-23

## Context

Ptah is already defined as the neutral world and execution substrate, not the thinker that chooses user work. That boundary must remain intact.

The owner clarified that neutrality does not require Ptah to be blind to its own operating condition. A useful computer or operating platform can detect that something is broken, degraded, incompatible or missing and can ask its operator for an upgrade without choosing what the operator wants to accomplish.

Ptah already has frozen primitives for Node and Provider health, capability, limitation, Generation, Activity/Operation/Attempt outcomes, Events, Receipts, Evidence, Views and Artifacts. The missing clarification is how those primitives may support a small diagnostic intelligence without reintroducing task-selection or approval authority.

## Decision

Adopt `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md` as the candidate boundary for platform self-diagnostics and upgrade requests.

### Allowed behavior

Ptah may:

- compare caller- or contract-defined expected conditions with observed platform evidence;
- detect a missing capability, incompatible version, resource shortage, degraded Provider, repeated failure pattern or failed post-condition;
- preserve exact negative and partial evidence;
- emit an evidence-backed diagnostic advisory;
- ask an authorized caller for an upgrade, additional capability, replacement Provider, resource increase or operator inspection;
- mechanically refuse an operation when an explicit contract or configured Policy precondition is absent;
- recheck the condition after a caller-authorized change.

### Forbidden behavior

Ptah may not:

- choose the user's goal or work;
- infer hidden priorities;
- reprioritize Activities;
- approve, purchase, install or activate its own upgrade;
- select a vendor from hidden preference;
- treat an advisory as an accepted decision;
- mark resolution from acknowledgement alone;
- block unrelated work when its requirements remain satisfied;
- become Hunter, Sergeant or the final authority.

### Representation

No new Core entity is required.

A diagnostic advisory is a typed View or Artifact composed from frozen Node, Provider, capability, health, Activity, Attempt, Event, Receipt, Claim/Finding and Evidence records. A caller-approved upgrade is a separate caller-submitted Activity.

### Sergeant pattern borrowed

The limited borrowed pattern is:

```text
explicit obligation
→ observed evidence
→ missing condition or contradiction
→ bounded deficiency report
→ escalation to responsible caller
→ independent post-condition verification
```

Ptah does not borrow Sergeant's verdict, rank, mission-selection or approval authority.

## Consequences

- Ptah remains neutral regarding user intent while becoming more useful and maintainable.
- Missing platform capabilities can be explained instead of appearing as generic failures.
- Humans and applications receive evidence before deciding whether to upgrade.
- Hunter may interpret and recommend; Sergeant may independently review; Ptah stores both without choosing.
- Existing frozen contracts remain sufficient.
- Programme A gains explicit diagnostic proof obligations.

## Non-effects

This decision does not:

- authorize implementation;
- reopen WP01–WP14;
- accept ADR-0033;
- start AF03;
- change P01;
- claim the diagnostic subsystem already exists;
- permit autonomous self-modification.

## Acceptance conditions

ADR-0036 may be accepted when:

1. the diagnostic boundary is explicit and evidence-backed;
2. task selection and upgrade approval remain caller-owned;
3. the design maps only to frozen primitives;
4. Master Plan and implementation roadmap placement are exact;
5. missing capability, degraded Provider and repeated failure examples are covered;
6. autonomous install, self-approval and unrelated-work blocking are explicitly rejected;
7. Hunter/Sergeant roles remain external applications;
8. AF03 remains not started;
9. P01, ADR-0033 and runtime non-authorization remain unchanged;
10. exact-head validation and adversarial tests pass.
