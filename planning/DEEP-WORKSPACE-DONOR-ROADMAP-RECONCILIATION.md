# Deep Workspace donor to Master Plan and roadmap reconciliation

Status: Phase 0C-19 candidate — non-operative until ADR-0037 acceptance

Recorded: 2026-07-24

## Purpose

Reconcile the accepted observable Workspace deep-study evidence from `jaydumisuni/Ptah-space` into Ptah's complete planning load before P01 physical-host closure and before any runtime implementation.

This record exists because the deep donor study was merged into `Ptah-space` as non-operative design evidence after Master Plan and roadmap version `1.0.0` had already been accepted. The useful lessons must therefore be mapped into the authoritative plan and delivery packages before the implementation proof host is frozen.

The reconciliation borrows behaviour and reliability patterns only. It copies no proprietary implementation and does not infer OpenAI private internals.

## Source evidence

Deep Workspace study PR:

```text
jaydumisuni/Ptah-space PR #16
```

Candidate exact head:

```text
bf4ae98b9d492ad688644fd6a330aaf435ac70c1
```

Operative non-runtime study merge:

```text
23dc4b19a0189ba55e08dfa124761efa806bd68b
```

Exact-head study evidence:

```text
workflow run: 30087967851
artifact: 8594496859
artifact digest: sha256:aea4fde3f600a6e4c3fc2f6ff3614918a5f714c6f8ebbf6ab3fb3cb29ccaf12b
validation SHA-256: 329262e7bb12e0841f1884664e713ab8e55a58e45a2430d4abf77ccdde65ecbe
```

The source study records:

- 10 primary observation lanes;
- 10 independent contract-check lanes;
- 22 mechanical capabilities;
- 28 gap-map mappings;
- 20 proof fixtures;
- 26 valid and adversarial regression cases;
- zero new Core entities;
- zero frozen-contract reopenings.

## Fixed product boundary

The study does not change the accepted product definition:

```text
Ptah = neutral Workspace and execution substrate
Hunter or another caller = intelligence, context selection, planning and coordination
Sergeant = independent review
Human or calling application = intent, approval, acceptance and release
```

Ptah may expose, execute, retain, recover and verify configured mechanical operations. It may not choose the caller's work, rank truth, perform semantic context selection, issue review verdicts, approve results or choose the next action.

## Reconciled mechanical capability load

The following 22 capabilities become explicit planning and proof requirements:

1. bounded Workspace envelope;
2. parallel Session continuity;
3. cross-device resume;
4. reusable Artifact Library;
5. external reference versus materialized Object truth;
6. typed operation catalog;
7. lazy capability-schema discovery;
8. operation effect classification;
9. external Provider permission preservation;
10. configured confirmation policy;
11. Activity progress Events;
12. partial-output and failure retention;
13. large-result stable resource handles;
14. paged and searchable result access;
15. render-independent typed Views;
16. one-off, recurring and condition-triggered schedules;
17. exact, flexible-window and condition-dependent timing modes;
18. optimistic concurrency and exact revision/head preconditions;
19. observe/draft/simulate/execute/verify lifecycle;
20. distinct declined, failed, cancelled, not-run and partial-completion result states;
21. connector source/account provenance;
22. explicit resource, Provider and product-limit reporting.

## Operation effect classes

Facilities and Providers must expose mechanical effect metadata:

```text
observe
draft
simulate
mutate
publish
destructive
external_side_effect
```

Effect class informs Grants, confirmation requirements, UI rendering and proof. It is not a Ptah judgment about whether an action is desirable.

## Object availability and materialization truth

The following states must remain distinct:

```text
external_reference
indexed_reference
mounted_read_only
materialized_copy
generated_artifact
```

A connector reference cannot be presented as a local path or local bytes until a mount or materialization Activity succeeds and produces a Receipt. Materialized outputs retain source Provider/account, external object identity, freshness or source revision, producing Activity/Attempt, digest, destination and retention/deletion policy.

## Activity and Receipt truth

The platform must preserve these result states without collapsing them:

```text
succeeded
failed
declined
cancelled
not_run
partially_completed
```

Operation invocation is not success. Retry creates a new Attempt. Partial Artifacts remain attached to the failed or interrupted Attempt. A separate verification Activity is required where the post-condition contract demands it.

## Permissions and approval separation

Three boundaries remain separate:

```text
external Provider/account permission
Ptah Grant and execution authority
human/application approval record
```

Approval cannot manufacture external access. Missing Provider permission, missing Grant, declined approval and execution failure produce different Receipts.

## Stable large-result access

A large result may remain behind a stable retained handle with:

- result identity and digest;
- media type and size;
- bounded range or line reads;
- paging cursor where applicable;
- exact search;
- source Operation/Attempt;
- expiration and retention state.

A Session receives Views or excerpts; conversation or UI limits must not erase the complete result.

## Scheduling semantics

Schedule kind:

```text
one_off
recurring
condition_watch
```

Timing mode:

```text
exact
flexible_window
condition_dependent
```

A scheduled Activity receives exact caller-specified Workspace, Recipe revision, immutable Object/Revision inputs, Provider references, Grant, schedule and output contract. It does not silently inherit hidden transcript context.

## Exact mutation preconditions

Protected mutations should support exact preconditions such as:

- Object Revision digest;
- document draft revision;
- Git branch head;
- message or thread identity;
- calendar/event version;
- state-machine state;
- Provider freshness token.

A moved target fails closed with expected and observed identities retained in a conflict Receipt.

## Caller-owned semantic functions

The following remain outside Ptah:

- intent interpretation and job definition;
- context query, relevance and selection;
- source authority and trust judgment;
- tool/Provider selection for semantic purpose;
- semantic worker-output reconciliation;
- approval and rejection;
- result acceptance and promotion;
- next-action selection;
- schedule purpose and desired outcome.

Ptah may run a caller-submitted Recipe that performs these operations, but the caller owns the semantic rules and resulting decision record.

## Rejected patterns

The roadmap must continue to reject:

- hidden Provider memory as canonical Workspace state;
- implicit global operation access;
- transcript text as the only operational database;
- silent copying or materialization of external files;
- success inferred from invocation;
- UI cards or previews as authority;
- Ptah-owned context ranking, verdicts or next-action choice;
- provider-specific hosted assumptions as mandatory architecture.

## Master Plan impact

The Master Plan must explicitly add:

- typed discoverable operation metadata and effect classes;
- exact separation of Provider access, Grant and approval;
- object availability/materialization states;
- large-result handles and incremental access;
- schedule kind and timing semantics;
- exact mutation preconditions;
- honest Activity/Receipt result states;
- partial-output retention;
- render-independent Views;
- cross-device/interface/model continuity;
- explicit limits and no silent semantic scope reduction.

These additions compose from existing frozen primitives. They do not add a `ChatGPTProject`, `WorkspaceOperation`, `Approval`, `ResultHandle` or `Schedule` Core identity family.

## Programme A mapping

### A01 — Repository, contracts and reproducible scaffold

Add:

- lock and validate the deep-study profile, gap map and fixtures;
- operation effect metadata vocabulary;
- availability, timing and result-state enumerations as profile/configuration contracts;
- proof that no new Core schema family is introduced.

### A02 — Node identity and host truth

Add:

- capability/limit reporting usable by operation discovery;
- resource-limit evidence with no silent work-scope reduction.

### A04 — Activity runtime

Add:

- typed operation catalog and lazy schema discovery;
- effect-class projection;
- explicit result states;
- progress, partial output and stable blocker state;
- approval/Grant/Provider-access distinction in Receipts;
- schedule kind and timing mode;
- exact precondition and conflict Receipt support.

### A06 — Persistent Workspace and Session

Add:

- cross-device/interface continuation;
- exact Provider/account binding provenance;
- explicit scheduled input manifests;
- model-independent handoff and resource-handle retention.

### A07 — Object, Revision and Artifact

Add:

- explicit reference/mount/materialization states;
- provenance and freshness binding;
- large-result Object/Artifact identity and bounded access metadata.

### A08 — Transfer

Add:

- reference-to-materialization Activity path;
- incremental range/paging result delivery where applicable;
- materialization Receipt and retention policy.

### A09 — Git Provider

Add:

- exact inspected branch-head preconditions for mutations;
- expected/observed conflict Receipts;
- draft/patch does not equal merge.

### A11 — Browser Provider

Add:

- exact Page/Context freshness preconditions;
- download references versus local materialization truth;
- Provider permission and confirmation distinction.

### A13 — Recovery

Add:

- stable large-result and partial-Artifact recovery;
- retries as new Attempts;
- schedule recovery with exact inputs;
- uncertain external effects and moved-target conflicts retained.

### A14 — Human Alpha surface

Add:

- operation catalog and effect display;
- separate Provider-access, Grant and approval status;
- reference/materialization badges;
- honest result-state and partial-completion views;
- paged/searchable stable-result access;
- exact/flexible/condition scheduling controls;
- precondition-conflict and visible-limit panels;
- View styling cannot become authority.

### A15 — Alpha acceptance

Add positive and adversarial proof for all 22 capability requirements, including the 20 deep-study fixtures and contract-reopen guard.

## Programme B mapping

- B01: permission-aware remote references, explicit materialization, retained partials and limit reporting.
- B06: cross-Node and cross-interface continuity with stable resource handles and exact missing-input reports.
- B07: permission-aware source retrieval, freshness/checkpoint identity and exact distinction between index and canonical source bytes.

## Programme D mapping

- D01: mature typed Views, operation discovery, approvals, scheduling, partial results, limits and accessibility.
- D02: implement both `ptah.workspace.ai_project.v1` and the compatible `ptah.workspace.operations.v2` profile; Hunter and Sergeant remain application adapters.
- D03: indexed reference versus source truth, incremental result access and exact citations.
- D04: versioned operation descriptors, effect metadata, schedule semantics and precondition support in Recipes/services.
- D09: full-workspace acceptance must prove all deep-study fixtures under human, Hunter and Sergeant usage without Ptah authority drift.

## Programme E mapping

- E04: compatible Workspace movement retains stable handles, materialization state, schedule inputs and exact preconditions.
- E06: intermittent/offline operation exposes stale freshness, unavailable Providers, queued schedules and limits honestly.
- E07: distributed acceptance proves permission, result-state and continuity semantics across Nodes.

## Cross-programme proof tracks

### X1 — Conformance and migrations

Validate operation metadata, effect classes, availability states, schedule semantics, result states and exact-precondition compatibility without adding a new Core family.

### X2 — Security and privacy

Verify Provider/account provenance, least privilege, approval separation, no silent materialization and no hidden global access.

### X3 — Observability and evidence

Retain progress, partial outputs, result handles, exact limits, conflicts, expected/observed revisions and distinct result states.

### X4 — Human usability

Expose effects, approval boundaries, materialization truth, limits and partial completion consistently on desktop, tablet and mobile.

### X5 — Recovery and handoff

Preserve stable handles, exact source/target identities, interrupted schedules, partial Artifacts and model-independent handoffs.

## Frozen-contract review

Result:

```text
new Core entity required: false
WP01-WP14 reopening required: false
```

Primary frozen mappings:

- WP02: Operation/Attempt/Event/Receipt result and effect truth;
- WP03: Object/Revision/View/Artifact materialization and result handles;
- WP04: Facility/Provider capability and limit discovery;
- WP05: Workspace/Session continuity and recovery;
- WP06: transfer/materialization and retained partials;
- WP07: Recipe and staged operation lifecycles;
- WP09: render-independent Views and human shell;
- WP10: permission-aware retrieval and index/source separation;
- WP11: Grants, preconditions, confirmation and external access boundaries;
- WP13/WP14: executable and adversarial proof.

If implementation later proves a required behavior cannot be represented by the frozen contracts, the affected work stops and requires a versioned reopening ADR, migrations, fixtures and conformance evidence.

## P01 sequencing correction

Roadmap PR #46 selected `Ptah-space` commit `23dc4b19a0189ba55e08dfa124761efa806bd68b` before this full reconciliation was accepted.

That selection remains a technically suitable non-runtime candidate because it contains the deep study itself, but it is **provisional** until Phase 0C-19 and ADR-0037 are accepted. No physical-host collection should begin before acceptance.

After Phase 0C-19 acceptance:

1. confirm that the same commit remains the final proof candidate, or select a newer reviewed non-runtime preparation commit;
2. record that confirmation in the P01 selection record;
3. only then run the exact physical-host proof.

## Candidate conclusion

The study improves the complete implementation load without changing what Ptah is. It increases the proof burden before implementation rather than creating later patch work.

```text
Phase 0C-19: CANDIDATE
ADR-0037: PROPOSED
P01: PAUSED pending reconciliation acceptance
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```