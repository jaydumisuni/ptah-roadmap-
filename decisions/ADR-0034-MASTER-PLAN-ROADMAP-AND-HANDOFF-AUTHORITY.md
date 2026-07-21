# ADR-0034 — Master Plan, implementation roadmap and durable handoff authority

Status: accepted — Master Plan, implementation roadmap and durable handoff are operative authorities

Recorded: 2026-07-21

## Context

Ptah has strong donor recovery, frozen WP01–WP14 contracts, executable conformance and substantial Phase 0C selection/evidence records. However, the control repository developed an authority gap:

- `MASTER_ROADMAP.md` remained an architecture-level document with a stale Phase 0B status;
- `DECISIONS.md` stopped at WP07;
- `PROGRESS.md` listed Phase 1–13 without a dependency-complete delivery programme;
- no single document defined users, product surfaces, operating modes, service ownership, release gates and the complete definition of Ptah;
- no machine-readable handoff bound the current plan, blockers and exact next action for another chat or AI.

The owner required the missing sequence to be completed and saved continuously:

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

## Proposed decision

Adopt the following authority split:

### `MASTER_PLAN.md`

Primary product and operating authority. Defines:

- Ptah purpose, scope and non-goals;
- users and participants;
- human, Hunter and replaceable-agent responsibilities;
- product surfaces and Facilities;
- operating modes;
- data, storage, context and memory model;
- security, privacy and authority;
- service ownership and operations;
- release milestones, success measures and definition of done.

### `IMPLEMENTATION_ROADMAP.md`

Primary delivery-sequencing authority. Defines:

- programme and work-package IDs;
- dependencies and critical path;
- deliverables and proof gates;
- milestone promotion;
- cross-cutting conformance, security, observability, usability and handoff tracks.

### Frozen WP01–WP14 contracts

Remain canonical technical identity, lifecycle, migration and proof authority. The Master Plan and roadmap may not silently redefine them.

### `CURRENT_STATE.md`

Remains the authority for the exact current phase, selected work package, branch/commit, blockers, authorization and next action.

### `AI_HANDOFF.md` and `master-plan-index.json`

Become the fast recovery entry points for humans, chats and software agents. They summarize rather than replace accepted decisions, contracts or evidence.

### Historical `MASTER_ROADMAP.md`

Remains retained as the architecture and phase source from which the complete plan was recovered. After this ADR is accepted it is no longer the primary product or sequencing authority.

## Recovery order

After acceptance, every new Ptah chat or agent reads:

1. `AI_HANDOFF.md`;
2. `CURRENT_STATE.md`;
3. `master-plan-index.json`;
4. `MASTER_PLAN.md`;
5. `IMPLEMENTATION_ROADMAP.md`;
6. recovery and reconciliation records;
7. `PROGRESS.md`;
8. `DECISIONS.md` and referenced ADRs;
9. `MEMORY_PROTOCOL.md`;
10. exact current `Ptah-space` source and evidence.

## Save-as-you-go rule

Substantial work must create durable checkpoints before the full task is complete.

A handoff checkpoint records:

- repository and branch;
- exact commit;
- completed work;
- active files/Activities;
- failures and limitations;
- evidence;
- blockers;
- safest next action;
- runtime authorization state.

A chat or model may never claim that work is safely recoverable when the durable records have not been updated.

## Roadmap-change rule

An accepted change must update the affected authority records together:

- Master Plan when product/operating intent changes;
- implementation roadmap when sequencing, dependencies or proof change;
- decision record when architecture or governance changes;
- progress and current state;
- handoff and machine index.

Frozen contract changes additionally require a versioned reopening ADR, migration, fixtures and conformance evidence.

## Acceptance evidence

Phase 0C-16 candidate exact head:

```text
37d23449fda9a426f56ee8b09042dda91587a6d1
```

Candidate closure workflow run: `29842137511`.

Retained artifact: `8499790872` with archive digest `sha256:82d6b452777e2c5e60c4d08bf88dd2c848d6b2570650b70a4eede633c8065d9f`.

The candidate passed twelve positive/adversarial regressions, standalone validation over seventeen authority files, complete WP01–WP14 and Phase 0C-01–16 mapping, P00/P01 and A01–A15 ordering, exact physical-host target/command checks and non-authorization checks.

Candidate squash merge:

```text
2c24f9e6b0fc98d5e03605596db75d7495796353
```

Direct review found no unresolved review threads or changed-file boundary violations. CodeRabbit review was requested but rate-limited and produced no findings.

Accepted-state exact head:

```text
5860b4bfe177aa375fb2fa4305d62dbe3d2141e1
```

Permanent accepted-state workflow run: `29844040274`.

Retained accepted-state artifact: `8500540358` with archive digest `sha256:6f5229fe850d8b6f6f083b09f2c5f53189f3edbf38d4f28b9d2878ab0c78862d`.

The accepted-state lane passed thirteen positive/adversarial regressions, standalone validation over seventeen durable authority files and all non-authorization checks.

Operative authority acceptance merge:

```text
66bd2410d4c777cd3fd3278107f40fe425e875e9
```


## Consequences

- Product planning and implementation sequencing are no longer conflated.
- A detailed roadmap can change without rewriting product purpose when intent is unchanged.
- A product-plan change cannot be hidden inside progress or code.
- Any chat or AI can recover the exact state from durable files.
- Donor completion, plan completion and owner intent remain insufficient to authorize runtime without the physical-host and ADR-0033 gates.
- `Runtime implementation` remains `NOT AUTHORIZED` until ADR-0033 is separately accepted.

## Acceptance conditions

This ADR is accepted because:

1. the recovered requirement/decision ledger is reviewed;
2. `MASTER_PLAN.md` covers product and operational scope;
3. `IMPLEMENTATION_ROADMAP.md` is dependency-complete from authorization through OS-ready foundation;
4. reconciliation confirms no silent WP01–WP14 weakening;
5. the recovery and machine-readable handoff records are consistent;
6. stale control-book records are repaired;
7. exact-head validation passes;
8. runtime authorization remains false.
