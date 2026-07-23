# Phase 0C-18 — Platform diagnostic advisory and efficient worker execution boundary

Status: candidate under review — runtime implementation remains unauthorized

Recorded: 2026-07-23

## Purpose

Clarify two bounded Ptah platform capabilities:

1. detect that its own execution environment is degraded, incompatible or missing a required capability and ask an authorized caller for an upgrade without deciding the caller's work;
2. after a caller supplies a job and execution recipe, use the Sergeant-derived ten-for-two worker pattern to finish that job faster and efficiently through bounded parallel workers and independent checks.

## Owner direction

```text
Ptah does not decide the work given.
Ptah may tell someone that it is not working correctly or is missing something.
Ptah may ask for an upgrade so it can better perform the requested work.
When Ptah is working on a caller-given job, it may borrow ten-for-two workers
so the work finishes faster and efficiently.
The useful Sergeant borrowing is evidence-backed deficiency detection,
bounded worker spreading, independent checking and post-condition proof.
```

## Deliverables

- `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md`;
- proposed ADR-0036;
- Master Plan clarification;
- detailed roadmap placement in Programme A and later Programme E;
- current-state, progress, handoff and machine-index records;
- read-only validator and adversarial regression suite;
- exact-head evidence workflow.

## Existing frozen primitives

The design must use only:

- Node, Facility, Provider, Generation, capability, limitation and health;
- Workspace, Activity, Operation, Attempt and Event;
- Recipe, Plan, Run and Step;
- Reservation, Policy, Grant, Lease and Fence;
- Receipt, Claim/Finding and Evidence;
- View and Artifact;
- Package, Plugin and Provider revision records.

A diagnostic advisory is a typed View or Artifact. A ten-for-two formation is a caller-defined Recipe/Plan/Run composed of bounded Activities and Attempts. A caller-approved upgrade is a separate caller-submitted Activity.

## Allowed diagnostic conditions

The candidate may detect:

- missing requested capability;
- Provider or Node health degradation;
- incompatible or outdated revision under an explicit support rule;
- insufficient CPU, memory, storage, GPU, network, Device or worker capacity;
- repeated evidenced failure pattern;
- failed post-condition after an acknowledgement;
- missing compatible Provider or Node;
- operator inspection required because evidence is inconclusive.

## Allowed worker execution

For a caller-submitted job and caller-selected Recipe or Plan, the candidate may let Ptah:

- apply `worker capacity = max(20, human-equivalent workers × 10)`;
- instantiate declared worker roles and independent-check lanes;
- run bounded worker Activities concurrently;
- place workers on compatible Nodes/Providers within configured authority;
- preserve worker inputs, outputs, failures, checkpoints, Receipts and evidence;
- retry failed workers only where submitted Policy permits and as new Attempts;
- apply a submitted deterministic merge rule;
- return complete, partial, conflicting, failed or inconclusive results.

## Prohibited authority

The candidate must not let Ptah:

- choose user goals;
- invent semantic subtasks not present in the job, Recipe, Plan or coordinating application;
- infer business priority;
- choose the next task;
- decide which worker conclusion is correct beyond deterministic checks;
- treat worker completion as caller acceptance;
- approve its own advisory;
- buy, install, upgrade, activate, remove or replace a Provider without configured authority;
- silently redirect work to another vendor or Node;
- mark the upgrade successful from acknowledgement alone;
- block unrelated Activities whose requirements are satisfied;
- become Hunter or Sergeant.

## Sergeant borrowing boundary

Borrowed:

- obligation-versus-evidence comparison;
- negative-evidence retention;
- missing-condition detection;
- bounded escalation;
- uncertainty and falsifier reporting;
- independent post-condition verification;
- ten-for-two worker scaling for a caller-submitted job;
- primary/verifier independence;
- checkpointed parallel execution;
- partial/conflicting result retention.

Not borrowed:

- verdict authority;
- rank authority;
- mission or goal selection;
- semantic scope invention;
- review acceptance;
- final approval.

## Roadmap placement

- A02 — health, capability, compatibility and worker-capacity gap detection;
- A04 — caller-defined worker Plan execution, repeated Attempt correlation and exact Events/Receipts;
- A06 — durable worker formation state inside Workspace/Session recovery;
- A14 — human-visible advisory, formation progress and caller response controls;
- A15 — proof that no autonomous upgrade, task selection or result acceptance exists;
- E05/E06 — later multi-Node worker placement, capacity and compatibility advisories.

## Acceptance proof

The exact-head validator must prove:

- missing capability produces an advisory rather than invented work;
- observed facts and suggestions are separated;
- every advisory retains exact evidence, expected condition and uncertainty;
- autonomous installation and self-approval are forbidden;
- caller action creates a separate Activity;
- acknowledgement is not resolution;
- unrelated work remains available;
- a caller-selected ten-for-two Recipe creates twenty bounded worker slots for two human-equivalent workers;
- worker roles, Attempts, checkpoints and evidence remain distinct;
- failed worker retry creates a new Attempt and requires submitted Policy authority;
- conflicting worker results remain visible;
- worker completion does not equal acceptance;
- Hunter and Sergeant remain external applications;
- no new Core entity is introduced;
- WP01–WP14 remain frozen;
- AF03 remains ready/not started;
- P01 remains active;
- ADR-0033 remains proposed;
- runtime implementation remains unauthorized.

## Completion effect

When accepted, this package clarifies planned product behavior and adds future implementation proof obligations. It does not implement either capability, start AF03 or authorize runtime work.
