# Phase 0C-19 deep Workspace planning-load acceptance

Status: ACCEPTED COMPLETE — accepted-state proof and operative merge pending

Recorded: 2026-07-24

## Accepted decision

ADR-0037 accepts the deep Workspace operations reconciliation as part of Ptah's complete planning load.

The operative planning authorities become:

```text
MASTER_PLAN.md version 1.1.0
IMPLEMENTATION_ROADMAP.md version 1.1.0
```

Frozen WP01–WP14 remain the technical contract authority. No Core family is added and no frozen contract is reopened.

## Source study evidence

```text
Ptah-space source candidate: bf4ae98b9d492ad688644fd6a330aaf435ac70c1
Ptah-space source merge: 23dc4b19a0189ba55e08dfa124761efa806bd68b
source workflow run: 30087967851
source artifact: 8594496859
source artifact digest: sha256:aea4fde3f600a6e4c3fc2f6ff3614918a5f714c6f8ebbf6ab3fb3cb29ccaf12b
source validation SHA-256: 329262e7bb12e0841f1884664e713ab8e55a58e45a2430d4abf77ccdde65ecbe
```

## Reconciliation candidate evidence

```text
candidate exact head: 07465ec89e819b94e3ec39696d9cb8b399d97dbd
candidate workflow run: 30095125653
candidate artifact: 8597258772
candidate artifact digest: sha256:56dc1f0ef54399e9f3a6ade0f8e5e55e878086e0a2f20ccf81a4820d30416165
candidate validation SHA-256: 3a457f7bff7b992a88a278cea1137c51a3e5d05c91674e425e7238f3c6ae109c
candidate regression SHA-256: 0c361de3367a39a73c58512847bad8785562523f2ddb032338c03435bcaf96e0
candidate merge: 96d0d465fe74fb1ac2e469b69bfb3326d7d65138
```

All eight permanent roadmap lanes passed at the exact candidate head. The Phase 0C-19 suite passed 30 valid and adversarial cases.

## Accepted capability load

The complete roadmap now includes:

- typed and lazily discoverable Facility/Provider operations;
- effect classes;
- Provider permission, Ptah Grant and caller approval separation;
- external reference, indexed reference, mount, materialization and generated-Artifact truth;
- progress and retained partial outputs;
- stable large-result handles with bounded reads, paging and exact search;
- render-independent typed Views;
- one-off, recurring and condition-watch schedules;
- exact, flexible-window and condition-dependent timing;
- exact Revision/head/state/freshness preconditions and conflict Receipts;
- staged observe/draft/simulate/execute/verify lifecycles;
- distinct success, failure, decline, cancellation, not-run and partial-completion results;
- connector source/account provenance;
- explicit limits and no silent semantic scope reduction;
- cross-interface, cross-device and replaceable-agent continuity.

These requirements are mapped into A01/A02/A04/A06/A07/A08/A09/A11/A13/A14/A15, B01/B06/B07, D01/D02/D03/D04/D09, E04/E06/E07 and X1–X5.

## Preserved authority boundary

```text
Ptah = neutral Workspace and mechanical execution substrate
Hunter/caller = intelligence, context selection, planning and coordination
Sergeant = independent review
Human/calling application = intent, approval, acceptance and release
```

Ptah does not choose work, rank semantic authority, select context, issue review verdicts, accept results or choose the next action.

## P01 proof-candidate confirmation

The current `Ptah-space` main head remains:

```text
23dc4b19a0189ba55e08dfa124761efa806bd68b
```

No newer non-runtime preparation commit exists at acceptance preparation time. The same commit contains the accepted deep-study source and all prior P01 proof/retention tooling. It is therefore confirmed as the exact P01 physical-host proof candidate.

This confirmation does not prove the host and does not begin collection.

## Resulting control state

```text
Phase 0C-19: COMPLETE
ADR-0037: ACCEPTED
Master Plan: 1.1.0 / ACCEPTED
Implementation roadmap: 1.1.0 / ACCEPTED
P01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST
P01 proof commit: CONFIRMED — 23dc4b19a0189ba55e08dfa124761efa806bd68b
physical-host collection: NOT STARTED
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```

## Remaining sequence

```text
run exact physical-host proof
→ review installed package and package-artifact boundary
→ independently retain and commit durable bundle
→ explicitly accept physical evidence
→ final Phase 0C consistency review
→ accept ADR-0033
→ explicitly authorize runtime implementation
→ make A01 ready
```

## Non-claims

This acceptance does not implement a runtime, run the physical proof, accept a package manifest, accept durable host evidence, accept ADR-0033 or authorize A01.