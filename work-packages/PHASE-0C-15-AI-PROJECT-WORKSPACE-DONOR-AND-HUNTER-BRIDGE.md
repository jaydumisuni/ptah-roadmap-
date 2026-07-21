# Phase 0C-15 — AI Project Workspace donor and Hunter bridge candidate

Status: accepted as non-operative design evidence — not an ADR-0033 blocker or runtime authorization

Recorded: 2026-07-21

## Purpose

Record the successful behavioural-donor study and frozen-contract composition candidate that makes a future Ptah Workspace easier for Hunter, humans and replaceable specialist agents to continue across Sessions, files, tools, Activities and restarts.

## Source boundary

The donor is OpenAI ChatGPT Projects and Work, observed only through official public documentation for Projects, project memory, Library, Work, Canvas and Scheduled Tasks.

The accepted integration class is `Study only`:

- no source-code reuse;
- no hidden prompt, schema, policy or proprietary implementation inference;
- no OpenAI runtime dependency;
- no ChatGPT-specific Core entity;
- no model-provider ownership of Workspace truth.

## Merged implementation-repository evidence

`Ptah-space` PR `#14` exact tested head:

```text
2a2c28d17abd9ad52c8d850f8bbcdba57074194e
```

Squash merge:

```text
d05653c5948727b58ead91088447d0b8ac4d9d9b
```

## Candidate identity

```text
ptah.workspace.ai_project.v1
```

The profile composes sixteen frozen Ptah primitives:

- Workspace, Session, Activity, Event and Attempt;
- Object, Revision, View and Artifact;
- Knowledge and Policy;
- Facility, Provider and Grant;
- Recipe and Receipt.

No new Core entity or frozen-contract change is proposed.

## Gap-map conclusion

Fourteen donor behaviours were classified:

- four covered directly by existing primitives;
- eight covered by profile composition;
- zero candidate extensions;
- two rejected or deliberately not adopted.

Rejected patterns:

1. hidden provider memory — Ptah context must be inspectable, exportable and source-bound;
2. implicit global tool access — Facilities require explicit Workspace or role Grants.

Any later implementation discovery that cannot be represented by the frozen primitive set must stop and request a versioned reopening ADR with migrations, fixtures and conformance evidence.

## Hunter bridge conclusion

The candidate responsibility split is:

- **Ptah:** Workspace identity, authority, Objects, Artifacts, Activities, Grants, privacy, Receipts, handoffs and recovery;
- **Hunter:** intent interpretation, planning, coordination, context requests, Activity proposals, Provider selection and candidate Artifact production;
- **Owner:** goals, protected-action approval, authority promotion, private-release decisions and final runtime authorization.

Hunter receives bounded context packets. A model response starts as `generated_candidate` and cannot directly change canonical truth.

## Proof package

The candidate includes ten positive/negative fixtures covering:

- cross-Workspace memory isolation;
- accepted-decision inheritance;
- superseded-source conflict handling;
- model-independent resume;
- Grant stability on agent replacement;
- least-privilege scheduled Artifact access;
- private Hunter/public Workspace separation;
- archived Session context selection;
- visible failed Activities and partial Artifacts;
- Artifact-to-Activity lineage.

Ten adversarial validator regressions enforce source completeness, no contract reopening, no new Core entity, non-authorization, authority classes, fixture identity, privacy and rejected hidden-memory behaviour.

## Exact-head workflow evidence

All ten workflows passed at `2a2c28d17abd9ad52c8d850f8bbcdba57074194e`:

| Lane | Workflow run |
|---|---:|
| AI Project Workspace candidate | `29824495268` |
| Frozen contract lock | `29824495206` |
| Generated contract bindings | `29824495326` |
| Host capability evidence | `29824495178` |
| Apache-2.0 acceptance | `29824495211` |
| Rust dependency policy | `29824495244` |
| Backend artifact evidence | `29824495186` |
| Backend signature evidence | `29824495190` |
| Signer lock boundary | `29824495223` |
| Scaffold, source, Browser and WP13 | `29824495166` |

The new lane checked out the exact head, ran all ten regressions, validated the donor/profile/gap/fixture package, bound report digests and retained evidence.

## Placement in Phase 0C

This candidate is useful future architecture but is deliberately not added to ADR-0033's physical-host acceptance conditions.

It does not:

- change the active physical-host proof blocker;
- close or add an ADR-0033 condition;
- change the first-slice proof burden;
- implement a context compiler, Workspace runtime, Artifact Library or Hunter bridge;
- authorize T01 or any WP14 runtime work.

## Conclusion

Ptah now has an evidence-bound, provider-independent composition candidate for the continuing project experience demonstrated by ChatGPT Projects and Work. Runtime implementation remains `NOT AUTHORIZED`, and the immediate continuation remains the exact physical Ubuntu host proof.
