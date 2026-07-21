# Phase 0C-16 — Master Plan and implementation roadmap closure

Status: candidate under review — runtime implementation remains unauthorized

Recorded: 2026-07-21

## Purpose

Close the planning-authority gap discovered before ADR-0033 acceptance by recovering every requirement and accepted design decision, writing the complete Ptah Master Plan, deriving a dependency-complete implementation roadmap, reconciling them against frozen WP01–WP14 and Phase 0C, and making the result recoverable by any future chat or AI.

## Owner instruction

The owner required the sequence:

```text
Recover every requirement and design decision
→ write the complete Ptah Master Plan
→ review missing product and operational scope
→ derive the detailed implementation roadmap
→ reconcile WP01–WP14 and Phase 0C
→ close physical-host evidence
→ accept ADR-0033
→ authorize implementation
```

The owner additionally required durable save-as-you-go checkpoints.

## Durable checkpoint commits

Planning branch:

```text
phase0c-master-plan-roadmap-closure
```

Committed checkpoints:

| Commit | Record |
|---|---|
| `a413dd010e248419514b50e8297154719f00fc91` | recovered requirements and decisions ledger |
| `566a166054f894a7bb9cf37d33b558c9da481e24` | complete Master Plan candidate |
| `57453b2b074cdea7cd905f0a5331d2edb7d707a0` | detailed implementation roadmap candidate |
| `85ded1c782ddd83e030319a2088b03c90054444c` | WP01–WP14 and Phase 0C reconciliation |
| `27e8b09109455f234867f05a65f6cff2b0563496` | physical-host through authorization procedure |
| `34a206449d4403e4ebf913475ffa8e846b1bf9ff` | durable AI/chat handoff |
| `5a3112b50ba699b41656c17013b9f3da5429e0e8` | machine-readable master-plan index |
| `30c4f603320fc31508116ec35a122f59048e87d3` | proposed plan/roadmap/handoff authority ADR |

## Recovered authority defects

The review found:

- stale Phase 0A/0B status in root planning documents;
- a Master Roadmap with strong architecture but insufficient product/operating and package-level execution detail;
- a decision index ending at WP07;
- a progress ledger with Phase 1–13 headings but no dependency-complete programme;
- no compact AI handoff or machine-readable plan index;
- no explicit plan-review prerequisite before ADR-0033 acceptance.

## Master Plan coverage

The candidate `MASTER_PLAN.md` now defines:

- executive product definition and problem statement;
- architecture principles;
- owner, administrator, operator, technician, developer, Hunter, Sergeant, agent and API-client roles;
- Core, Facility, Domain Pack, human shell and AI Project Workspace scope;
- explicit non-goals;
- online, local, hybrid, offline, distributed and private OS integration modes;
- canonical world model;
- storage, ledger, Git, Drive and context/memory architecture;
- Provider/adapter direction;
- security, privacy, protected action and supply-chain boundaries;
- reliability, recovery, observability and evidence;
- APIs, SDKs and integration surfaces;
- operations, ownership, upgrade and rollback;
- release milestones, success measures and product definition of done;
- parked scope and governance.

## Detailed roadmap coverage

The candidate `IMPLEMENTATION_ROADMAP.md` defines:

- Programme P00 plan closure;
- Programme P01 physical-host and ADR-0033 closure;
- Programme A Online Ptah Alpha with fifteen packages;
- Programme B Object World Beta;
- Programme C Firmware and Device Beta;
- Programme D Full Workspace Release;
- Programme E Distributed Ptah;
- Programme F OS-ready foundation;
- cross-programme conformance, security, observability, human-usability and handoff tracks;
- exact package dependencies, deliverables and proof gates;
- milestone promotion and rollback rules.

The existing fourteen Phase 0C first-slice tasks remain mapped to A01–A13 and A15. A14 adds the already-required direct human Alpha control surface without weakening any frozen proof.

## Reconciliation result

The candidate plan:

- introduces no new canonical Core entity;
- requires no immediate WP01–WP14 reopening;
- preserves all identity, lifecycle, migration, privacy and proof boundaries;
- keeps the AI Project Workspace as composition over existing primitives;
- retains Phase 0C host, dependency, source, licence, signer and evidence selections;
- retains the physical-host gate and explicit authorization sequence;
- defines a fail-closed reopening rule for implementation discoveries outside the frozen contracts.

## Recovery and handoff result

The package adds:

- `AI_HANDOFF.md` as the concise human/AI entry point;
- `master-plan-index.json` as the machine-readable status and authority index;
- an updated mandatory recovery order;
- exact checkpoint commits and next action;
- a rule that substantial work must be durably saved before the full task is complete.

## Required control-book repairs

Before acceptance, update and validate:

- `README.md`;
- `MASTER_ROADMAP.md`;
- `PROGRESS.md`;
- `DECISIONS.md`;
- `MEMORY_PROTOCOL.md`;
- `DONOR_RECOVERY.md`;
- `CURRENT_STATE.md`;
- proposed ADR-0033 conditions;
- `AI_HANDOFF.md` and `master-plan-index.json` final exact head.

## Acceptance proof

This work package can become accepted only when automated and direct review confirm:

1. all required planning files exist;
2. Master Plan and roadmap versions/profile identities agree;
3. P00 and P01 are present before Programme A;
4. A01–A15 are unique and ordered;
5. WP01–WP14 and 0C-01–0C-16 mappings are complete;
6. the physical-host commands and target remain exact;
7. current state and index report runtime authorization false;
8. ADR-0033 remains proposed;
9. no runtime implementation is claimed;
10. the next action is plan review/merge followed by physical-host proof.

## Conditions closed by this package

After reviewed merge, this package closes:

- recovery of requirements and accepted design intent into one ledger;
- complete product/operating Master Plan;
- dependency-complete implementation roadmap;
- missing product and operational scope review;
- WP01–WP14/Phase 0C reconciliation;
- durable chat/AI handoff architecture;
- planning authority and save-as-you-go governance.

## Conditions not closed

This package does not close:

- the actual physical Ubuntu host proof;
- installed package or package-artifact acceptance;
- durable host-bundle acceptance;
- final Phase 0C closure review;
- ADR-0033 acceptance;
- runtime implementation authorization;
- any Programme A runtime package.

## Current conclusion

The planning layer is being completed in the required order. Runtime implementation remains **NOT AUTHORIZED**.
