# ADR-0037 — Deep Workspace operations roadmap reconciliation

Status: proposed

Recorded: 2026-07-24

## Context

Master Plan and implementation roadmap version `1.0.0` were accepted before the later deep observable Workspace study completed. The study is now retained in `Ptah-space` and proves 22 useful mechanical capabilities with no new Core entity and no frozen-contract reopening.

Leaving those requirements only in a non-operative donor profile would force implementation packages to rediscover them and patch operation, Object, Workspace, scheduling, View, permission, recovery and proof behavior after work had already begun.

P01 proof-candidate selection was merged before this reconciliation was complete. The candidate is non-runtime and contains the deep study, but the selection must remain provisional until the complete planning load is accepted.

## Proposed decision

Adopt `planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md` and Phase 0C-19 as the candidate supplement to Master Plan and implementation roadmap version `1.0.0`.

The accepted change, if approved later, will:

1. promote Master Plan and implementation roadmap to version `1.1.0`;
2. make `ptah.workspace.operations.v2` a provider-independent behavioural profile supplement;
3. add the 22 mechanical capability requirements to the complete implementation load;
4. map them into A01/A02/A04/A06/A07/A08/A09/A11/A13/A14/A15, B01/B06/B07, D01/D02/D03/D04/D09, E04/E06/E07 and X1–X5;
5. preserve all caller-owned semantic and authority functions outside Ptah;
6. preserve WP01–WP14 without reopening;
7. require a final confirmation or supersession of the provisional P01 proof commit after acceptance;
8. keep physical-host proof, ADR-0033 and runtime authorization closed until their independent evidence passes.

## Mechanical requirements

Facilities and Providers advertise typed operations, schema versions, effect classes, limits, preconditions and expected Receipt states.

The accepted operation effect classes are:

```text
observe
draft
simulate
mutate
publish
destructive
external_side_effect
```

Object availability remains explicit:

```text
external_reference
indexed_reference
mounted_read_only
materialized_copy
generated_artifact
```

Activity and Receipt results remain explicit:

```text
succeeded
failed
declined
cancelled
not_run
partially_completed
```

Schedule kind and timing mode remain distinct:

```text
one_off / recurring / condition_watch
exact / flexible_window / condition_dependent
```

Provider access, Ptah Grant and human/application approval remain separate.

Mutation may require an exact Revision, branch head, draft version, state-machine state or Provider freshness token. Mismatch fails closed with expected/observed evidence.

Large and partial results remain retained behind stable identities and incremental Views rather than being lost to one interface or context window.

## Authority boundary

Ptah may:

- expose capability and operation metadata;
- enforce configured Grants and preconditions;
- execute caller-submitted Activities/Recipes;
- emit progress Events;
- preserve partial outputs, conflicts and result states;
- provide Views and stable result handles;
- run explicitly submitted schedules;
- retain exact provenance and limits.

Ptah may not:

- choose the caller's job;
- perform semantic context selection or source ranking;
- choose the semantically correct Provider;
- reconcile worker conclusions without a caller-supplied Recipe;
- approve protected actions;
- accept or promote results;
- issue Sergeant review verdicts;
- choose the next action or schedule purpose.

## Frozen-contract conclusion

The requirements compose from accepted WP02–WP07, WP09–WP11, WP13 and WP14 primitives. No new canonical entity family is accepted.

If implementation reveals a missing primitive, the affected work package must stop and open a versioned contract-reopening ADR with migrations, fixtures and conformance evidence.

## P01 consequence

Roadmap PR #46 and merge `675d28f5857e8fcaf16cee9dfabc6934331a009d` selected `Ptah-space` commit `23dc4b19a0189ba55e08dfa124761efa806bd68b`.

During this proposed decision:

```text
P01: PAUSED
selected proof commit: PROVISIONAL
physical-host collection: NOT STARTED
```

After ADR-0037 acceptance, the selected commit must be confirmed or superseded in a reviewed change before the physical proof command runs.

## Conditions before acceptance

ADR-0037 remains proposed until:

1. all canonical planning records are synchronized;
2. all 22 capability requirements and affected packages/tracks are present;
3. positive and adversarial validator suites pass at one exact head;
4. the candidate merge is retained;
5. an independent review confirms no Core extension or frozen-contract weakening;
6. a separate acceptance change promotes Master Plan and roadmap version `1.1.0`;
7. P01, ADR-0033 and runtime authorization remain false during the candidate phase.

## Consequences

- more proof is required before implementation;
- later patching risk is reduced;
- operation, Object, scheduling, permission, recovery, View and continuity behavior is planned consistently across programmes;
- no runtime dependency on OpenAI is introduced;
- no OpenAI private code or internal design is copied;
- the accepted Ptah/Hunter/Sergeant/human boundary remains unchanged.

## Current boundary

```text
ADR-0037: PROPOSED
Phase 0C-19: CANDIDATE
P01: PAUSED
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```