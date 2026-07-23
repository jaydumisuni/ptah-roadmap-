# Phase 0C-18 — Platform diagnostic advisory boundary

Status: candidate under review — runtime implementation remains unauthorized

Recorded: 2026-07-23

## Purpose

Clarify the narrow platform intelligence Ptah may use to detect that its own execution environment is degraded, incompatible or missing a required capability and to ask an authorized caller for an upgrade without deciding the caller's work.

## Owner direction

```text
Ptah does not decide the work given.
Ptah may tell someone that it is not working correctly or is missing something.
Ptah may ask for an upgrade so it can better perform the requested work.
The useful part borrowed from Sergeant is evidence-backed deficiency detection and escalation.
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
- Activity, Operation, Attempt and Event;
- Receipt, Claim/Finding and Evidence;
- View and Artifact;
- caller-configured Policy, Grant, Lease and Fence;
- Package, Plugin and Provider revision records.

A diagnostic advisory is a typed View or Artifact. A caller-approved upgrade is a separate caller-submitted Activity.

## Allowed conditions

The candidate may detect:

- missing requested capability;
- Provider or Node health degradation;
- incompatible or outdated revision under an explicit support rule;
- insufficient CPU, memory, storage, GPU, network or Device access;
- repeated evidenced failure pattern;
- failed post-condition after an acknowledgement;
- missing compatible Provider or Node;
- operator inspection required because evidence is inconclusive.

## Prohibited authority

The candidate must not let Ptah:

- choose user goals;
- infer business priority;
- choose the next task;
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
- independent post-condition verification.

Not borrowed:

- verdict authority;
- rank;
- mission selection;
- review acceptance;
- final approval.

## Roadmap placement

- A02 — health, capability and compatibility gap detection;
- A04 — repeated Attempt correlation and exact diagnostic Events/Receipts;
- A14 — human-visible advisory and caller response controls;
- A15 — proof that no autonomous upgrade or task-selection authority exists;
- E05/E06 — later multi-Node capacity and compatibility advisories.

## Acceptance proof

The exact-head validator must prove:

- missing capability produces an advisory rather than invented work;
- observed facts and suggestions are separated;
- every advisory retains exact evidence, expected condition and uncertainty;
- autonomous installation and self-approval are forbidden;
- caller action creates a separate Activity;
- acknowledgement is not resolution;
- unrelated work remains available;
- Hunter and Sergeant remain external applications;
- no new Core entity is introduced;
- WP01–WP14 remain frozen;
- AF03 remains ready/not started;
- P01 remains active;
- ADR-0033 remains proposed;
- runtime implementation remains unauthorized.

## Completion effect

When accepted, this package clarifies planned product behavior and adds future implementation proof obligations. It does not implement the diagnostic subsystem or authorize any runtime work.
