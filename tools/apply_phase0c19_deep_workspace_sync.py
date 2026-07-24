#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION"


class SyncError(RuntimeError):
    pass


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one source fragment, found {count}")
    return text.replace(old, new, 1)


def append_section(path: str, heading: str, body: str) -> None:
    text = read(path)
    if heading in text:
        return
    write(path, text.rstrip() + "\n\n" + body.strip() + "\n")


def update_master_plan() -> None:
    path = "MASTER_PLAN.md"
    text = read(path)
    if "### 6.6 Deep Workspace operations profile" not in text:
        text = replace_once(
            text,
            "17. **Caller-given work may use bounded worker formations.** A caller-selected Recipe or Plan may apply the Sergeant-derived ten-for-two pattern for efficient parallel execution, while scope, semantic decomposition and result acceptance remain caller-owned.\n",
            "17. **Caller-given work may use bounded worker formations.** A caller-selected Recipe or Plan may apply the Sergeant-derived ten-for-two pattern for efficient parallel execution, while scope, semantic decomposition and result acceptance remain caller-owned.\n18. **Operational truth must be explicit at every boundary.** Operation effects, external access, Grants, approvals, reference/materialization state, preconditions, progress, partial outputs, result states, limits and post-condition proof may not be collapsed into optimistic success or hidden UI state.\n",
            "master-plan principle",
        )
        text = replace_once(
            text,
            "- evidence-backed diagnostic advisory Views and Artifacts over platform health, capability and execution records;\n- neutral APIs and event envelopes.\n",
            "- evidence-backed diagnostic advisory Views and Artifacts over platform health, capability and execution records;\n- typed and lazily discoverable Facility/Provider operation descriptors, including effect class, schema version, limits, preconditions and expected Receipt states;\n- explicit external-reference, indexed-reference, mounted, materialized and generated-Artifact projections;\n- exact schedule kind/timing projections, stable large-result handles and incremental result Views;\n- neutral APIs and event envelopes.\n",
            "master-plan core services",
        )
        text = replace_once(
            text,
            "- worker formation, checkpoint, conflict and partial-result status;\n- approvals and security boundaries;\n",
            "- worker formation, checkpoint, conflict and partial-result status;\n- operation effect, Provider-access, Grant and approval status shown as separate facts;\n- reference/materialization, schedule timing, exact-precondition conflict, partial-completion, stable-result and visible-limit panels;\n- approvals and security boundaries;\n",
            "master-plan human shell",
        )
        anchor = "This is a composition of frozen Ptah primitives, not a new ChatGPT-specific Core entity.\n"
        addition = """This is a composition of frozen Ptah primitives, not a new ChatGPT-specific Core entity.\n\n### 6.6 Deep Workspace operations profile\n\nThe compatible `ptah.workspace.operations.v2` profile supplements the AI Project Workspace profile with mechanical reliability requirements recovered from the deep observable Workspace study:\n\n- typed and lazily discoverable Facility/Provider operations;\n- effect classes `observe`, `draft`, `simulate`, `mutate`, `publish`, `destructive` and `external_side_effect`;\n- external Provider permission, Ptah Grant and caller approval as separate boundaries;\n- `external_reference`, `indexed_reference`, `mounted_read_only`, `materialized_copy` and `generated_artifact` availability states;\n- stable large-result handles with bounded reads, paging, exact search, digest and retention state;\n- progress Events and retained partial Artifacts;\n- one-off, recurring and condition-watch schedules with exact, flexible-window or condition-dependent timing;\n- exact Revision/head/freshness preconditions and expected/observed conflict Receipts;\n- observe/draft/simulate/execute/verify lifecycles;\n- distinct `succeeded`, `failed`, `declined`, `cancelled`, `not_run` and `partially_completed` results;\n- connector account/source provenance, freshness and visible limits;\n- continuity across interfaces, devices and replaceable intelligence providers.\n\nPtah exposes and mechanically enforces these records. The caller still chooses the work, operation for semantic purpose, context, approval, acceptance, reconciliation and next action. No new Core entity family is introduced.\n"""
        text = replace_once(text, anchor, addition, "master-plan profile section")
        write(path, text)

    append_section(
        path,
        "## 23. Phase 0C-19 candidate planning-load supplement",
        """
## 23. Phase 0C-19 candidate planning-load supplement

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

The deep Workspace operations study is reconciled through `planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md` as a candidate supplement to accepted version `1.0.0`.

It adds implementation and proof detail only. It does not change Ptah's identity, add a Core family, reopen WP01–WP14, accept ADR-0033 or authorize runtime implementation. A separate ADR-0037 acceptance change is required before this supplement becomes operative version `1.1.0`.
""",
    )


def update_roadmap() -> None:
    path = "IMPLEMENTATION_ROADMAP.md"
    text = read(path)
    if "operation effect class, exact precondition" not in text:
        text = replace_once(
            text,
            "- limitations and unsupported cases;\n- reviewer outcome;\n",
            "- limitations and unsupported cases;\n- operation effect class, exact precondition, Provider-access, Grant and approval boundaries where applicable;\n- Object/reference materialization state, schedule kind/timing mode, partial-output and result-state evidence where applicable;\n- explicit resource, Provider and product limits with no silent semantic scope reduction;\n- reviewer outcome;\n",
            "roadmap universal gate",
        )
        write(path, text)

    append_section(
        path,
        "# 8. Phase 0C-19 candidate amendments to the delivery load",
        """
# 8. Phase 0C-19 candidate amendments to the delivery load

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

Status: candidate supplement; accepted roadmap version `1.0.0` remains operative until ADR-0037 acceptance.

The following requirements are added to the named packages. They are not optional later enhancements; after acceptance they are part of each package's definition of done.

## A01 amendment

Lock the `ptah.workspace.operations.v2` profile, gap map and fixtures; validate all effect, availability, result, schedule and timing vocabularies; prove zero new Core family and zero frozen-contract reopening.

## A02 amendment

Expose exact capability and limit evidence used by operation discovery and scheduling. Resource shortage or unavailable capability is reported without silently shrinking caller scope.

## A04 amendment

Deliver typed/lazy operation discovery, effect-class projection, schedule kind and timing mode, explicit progress/partial state, distinct result states, approval/Grant/Provider-access Receipts, exact preconditions and expected/observed conflict evidence.

## A06 amendment

Deliver cross-device and cross-interface continuation, exact Provider/account binding provenance, scheduled input manifests, model-independent handoff records and stable resource-handle retention.

## A07 amendment

Deliver explicit `external_reference`, `indexed_reference`, `mounted_read_only`, `materialized_copy` and `generated_artifact` projections; retain source freshness/provenance; model stable large-result identity and incremental access metadata.

## A08 amendment

Deliver the explicit reference-to-materialization Activity path, materialization Receipts, retention/deletion policy, and incremental delivery for large transfer results without conflating remote references with local bytes.

## A09 amendment

Require exact inspected branch-head or Revision preconditions for protected mutations. Draft/patch creation is not merge; moved targets fail closed with expected and observed identities.

## A11 amendment

Require exact Browser Context/Page freshness, separate download references from local materialization, preserve external account permission separately from configured confirmation and verify navigation/post-condition truth.

## A13 amendment

Recover stable result handles, partial Artifacts, schedule inputs and conflict Receipts. Retry creates a new Attempt; uncertain external effects and moved-target conflicts remain visible.

## A14 amendment

Expose typed operations and effect classes; separate external access, Grant and approval; show reference/materialization state, exact/flexible/condition schedules, honest result states, partial completion, stable paged/searchable results, precondition conflicts and explicit limits. View style never creates authority.

## A15 amendment

Run the deep-study positive and adversarial corpus: 22 capabilities, 20 fixtures and the profile's 26 original cases, plus proof that Ptah cannot gain semantic context, review, approval, acceptance or next-action authority.

## Programme B amendments

- **B01:** permission-aware remote references, explicit materialization, retained partials, stable result handles and visible transfer/provider limits.
- **B06:** cross-Node/interface continuity with stable handles, exact scheduled inputs, conflict state and missing-capability evidence.
- **B07:** permission-aware retrieval, freshness/sync checkpoints, incremental results and exact index-versus-canonical-source distinction.

## Programme D amendments

- **D01:** mature operation discovery, typed Views, approvals, scheduling, partial results, stable handles, conflicts, limits and accessibility.
- **D02:** implement both `ptah.workspace.ai_project.v1` and compatible `ptah.workspace.operations.v2`; Hunter and Sergeant remain caller adapters.
- **D03:** indexed references, exact citations, source freshness, incremental result access and canonical-source separation.
- **D04:** versioned operation descriptors, effect metadata, staged observe/draft/simulate/execute/verify Recipes, schedules and preconditions.
- **D09:** prove the complete deep-study corpus under human, Hunter and Sergeant use without Ptah authority drift.

## Programme E amendments

- **E04:** preserve stable result handles, availability/materialization state, scheduled inputs and exact preconditions during Workspace movement.
- **E06:** expose stale freshness, unavailable Providers, queued schedules, partial state and limits honestly during intermittent/offline operation.
- **E07:** prove permission, result-state, conflict, scheduling and continuity semantics across multiple Nodes.

## Cross-programme track amendments

- **X1:** conformance for operation descriptors, effect classes, availability states, schedule/timing modes, result states and precondition compatibility.
- **X2:** Provider/account provenance, least privilege, approval separation, no silent materialization and no implicit global access.
- **X3:** progress, partial outputs, stable handles, limits, conflicts, expected/observed revisions and distinct result states.
- **X4:** consistent presentation of effects, approval boundaries, materialization truth, limits and partial completion on desktop/tablet/mobile.
- **X5:** recovery of handles, source/target identities, interrupted schedules, partial Artifacts and model-independent handoffs.

## P01 sequencing amendment

P01 is paused while this candidate is reviewed. Roadmap PR #46's selected `Ptah-space` commit remains provisional. After ADR-0037 acceptance, a reviewed change must confirm or supersede that commit before physical-host collection begins.

```text
Phase 0C-19: CANDIDATE
ADR-0037: PROPOSED
P01: PAUSED
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```
""",
    )


def update_recovery_ledger() -> None:
    append_section(
        "planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md",
        "## Recovered deep Workspace operations supplement",
        """
## Recovered deep Workspace operations supplement

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

`Ptah-space` PR #16 and merge `23dc4b19a0189ba55e08dfa124761efa806bd68b` add the provider-independent `ptah.workspace.operations.v2` behavioural profile.

Recovered requirements include typed/lazy operation discovery, effect classes, permission/Grant/approval separation, reference/materialization truth, progress and partial retention, large-result handles, render-independent Views, exact/flexible/condition schedules, exact mutation preconditions, staged operation lifecycles, distinct result states, connector provenance, explicit limits and cross-interface continuity.

The profile introduces no Core family and requires no WP01–WP14 reopening. Semantic context selection, Provider choice for purpose, reconciliation, approval, acceptance and next action remain caller-owned.

Until ADR-0037 accepts the synchronized planning load, P01 is paused and the selected physical-proof commit is provisional.
""",
    )


def update_reconciliation() -> None:
    append_section(
        "planning/MASTER-PLAN-RECONCILIATION.md",
        "## Phase 0C-19 deep Workspace operations reconciliation",
        """
## Phase 0C-19 deep Workspace operations reconciliation

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

The deep study maps to frozen WP02–WP07, WP09–WP11, WP13 and WP14. No new canonical family is required.

| Deep requirement | Frozen authority | Roadmap load |
|---|---|---|
| typed operation/effect metadata | WP02, WP04, WP07, WP11 | A01, A04, D04, X1 |
| Provider access / Grant / approval separation | WP02, WP04, WP11 | A04, A14, D01, D02, X2 |
| reference / materialization truth | WP03, WP04, WP06 | A07, A08, A11, B01, X2 |
| progress, partial output and result states | WP02, WP03, WP05 | A04, A13, A14, X3 |
| stable large-result handles | WP03, WP05, WP10 | A06–A08, B06, B07, D03 |
| typed render-independent Views | WP03, WP09 | A14, D01, D02, X4 |
| schedule kind/timing and exact inputs | WP02, WP05, WP07, WP11 | A04, A06, A13, A14, D04 |
| exact revision/head preconditions | WP01–WP03, WP07, WP11 | A04, A09, A11, A13, X1 |
| permission-aware retrieval/freshness | WP04, WP05, WP10, WP11 | B07, D02, D03, E06 |
| cross-interface/Node continuity | WP03–WP06, WP11 | A06, A13, B06, E04–E07, X5 |

The profile's enumerations and operation metadata are composition/conformance requirements, not new entity families. Any contrary implementation discovery triggers the existing versioned reopening rule.

The earlier P01 candidate selection is provisional until this reconciliation is accepted.
""",
    )


def update_physical_closure() -> None:
    path = "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md"
    text = read(path)
    if "Phase 0C-19 / ADR-0037 planning-load reconciliation" not in text:
        text = replace_once(
            text,
            "Status: exact closure procedure recorded — blocked on access to the physical proof host\n",
            "Status: exact closure procedure recorded — P01 paused pending Phase 0C-19 planning-load reconciliation, then blocked on access to the physical proof host\n",
            "physical closure status",
        )
        text = replace_once(
            text,
            "- AI Project Workspace donor/profile recorded;\n- complete Master Plan and detailed implementation roadmap candidate prepared on `phase0c-master-plan-roadmap-closure`.\n",
            "- AI Project Workspace donor/profile recorded;\n- deep Workspace operations study merged in `Ptah-space` and Phase 0C-19 / ADR-0037 planning-load reconciliation in review;\n- complete Master Plan and detailed implementation roadmap candidate prepared on `phase0c-master-plan-roadmap-closure`.\n",
            "physical closure prerequisites",
        )
        text = replace_once(
            text,
            "## Step 2 — select the exact implementation candidate commit\n",
            "## Step 1A — accept the complete planning load\n\nBefore selecting the final physical-proof commit, accept Phase 0C-19 / ADR-0037 and make Master Plan and implementation roadmap version `1.1.0` operative. The provisional selection from roadmap PR #46 cannot authorize collection.\n\n## Step 2 — select the exact implementation candidate commit\n",
            "physical closure step",
        )
        write(path, text)


def update_p01_selection() -> None:
    path = "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md"
    text = read(path)
    if "## Phase 0C-19 sequencing correction" not in text:
        text = replace_once(
            text,
            "Status: selected, non-authorizing — blocked on execution on the exact physical proof host\n",
            "Status: provisional, non-authorizing — P01 paused pending Phase 0C-19 / ADR-0037 planning-load acceptance\n",
            "p01 selection status",
        )
        anchor = "## Required proof-host identity\n"
        note = """## Phase 0C-19 sequencing correction\n\nThe exact commit below was selected before the complete deep Workspace study was reconciled into the private Master Plan and roadmap. It remains technically suitable and non-runtime, but it is provisional.\n\nDo not run physical-host collection until ADR-0037 accepts Phase 0C-19 and a reviewed change confirms this commit or selects a newer non-runtime preparation commit.\n\n## Required proof-host identity\n"""
        text = replace_once(text, anchor, note, "p01 selection sequencing")
        text = text.replace("P01: OPEN / selected proof candidate", "P01: PAUSED / provisional proof candidate")
        write(path, text)


def update_current_state() -> None:
    path = "CURRENT_STATE.md"
    text = read(path)
    text = replace_once(
        text,
        "**Active work unit:** 0C-04 / P01 — physical pinned-host proof, package review, durable evidence and ADR-0033 closure  \n",
        "**Active work unit:** Phase 0C-19 — deep Workspace study Master Plan and roadmap reconciliation; P01 paused  \n",
        "current active work",
    )
    text = replace_once(
        text,
        "**Production dependency/backend selection:** EXACT RUST, DISTRIBUTED ARTIFACT, PROOF AND RETENTION TOOL LOCKS MERGED — APACHE-2.0 BOUNDARY ACCEPTED — PHYSICAL PINNED-HOST PROOF OPEN  \n",
        "**Production dependency/backend selection:** LOCKS MERGED — DEEP WORKSPACE PLANNING LOAD IN REVIEW — PHYSICAL PINNED-HOST PROOF PAUSED  \n",
        "current production state",
    )
    if "## Active Phase 0C-19 deep Workspace reconciliation" not in text:
        section = """
## Active Phase 0C-19 deep Workspace reconciliation

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

- deep study source merge: `23dc4b19a0189ba55e08dfa124761efa806bd68b`;
- 22 mechanical capabilities, 28 mappings, 20 fixtures and 26 original cases;
- zero new Core entities;
- zero WP01–WP14 reopenings;
- Master Plan and roadmap candidate supplement mapped across A, B, D, E and X1–X5;
- ADR-0037: PROPOSED;
- P01: PAUSED;
- roadmap PR #46 proof-candidate selection: PROVISIONAL;
- physical-host collection: NOT STARTED;
- ADR-0033: PROPOSED;
- runtime implementation: NOT AUTHORIZED.

Immediate order:

```text
prove Phase 0C-19 candidate
→ merge candidate evidence
→ separately accept ADR-0037 and planning version 1.1.0
→ confirm or supersede the P01 proof commit
→ resume physical-host closure
```
"""
        insert = "## Active Phase 0C blockers\n"
        text = replace_once(text, insert, section + "\n---\n\n" + insert, "current phase0c19 section")

    old_order = """## Immediate continuation order

1. Install or recover the exact Ubuntu Server 24.04.4 / `6.8.0-136-generic` proof host.
2. Select and record the exact clean reviewed `Ptah-space` preparation commit.
3. Run:
"""
    new_order = """## Immediate continuation order

1. Complete and exact-head validate Phase 0C-19 deep Workspace planning-load reconciliation.
2. Merge the candidate evidence and separately accept ADR-0037 / Master Plan and roadmap version `1.1.0`.
3. Confirm or supersede the provisional `Ptah-space` proof commit.
4. Install or recover the exact Ubuntu Server 24.04.4 / `6.8.0-136-generic` proof host.
5. Run:
"""
    if old_order in text:
        text = replace_once(text, old_order, new_order, "current continuation order")
    write(path, text)


def update_progress() -> None:
    path = "PROGRESS.md"
    text = read(path)
    text = text.replace(
        "- [?] P01 — Physical-host and ADR-0033 closure; active and blocked on the exact external host.",
        "- [?] P01 — Physical-host and ADR-0033 closure; paused pending Phase 0C-19 acceptance, then blocked on the exact external host.",
    )
    append_section(
        path,
        "## Deep Workspace operations planning-load reconciliation",
        """
## Deep Workspace operations planning-load reconciliation

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

- [x] deep observable Workspace study merged into `Ptah-space` as `23dc4b19a0189ba55e08dfa124761efa806bd68b`;
- [x] 22 capabilities, 28 mappings, 20 fixtures and 26 original cases recovered;
- [x] no new Core entity and no WP01–WP14 reopening identified;
- [-] Phase 0C-19 canonical planning synchronization in review;
- [-] ADR-0037 proposed;
- [?] P01 paused until the reconciliation is accepted;
- [ ] confirm or supersede the provisional proof commit after acceptance;
- [ ] runtime implementation authorized.
""",
    )
    write(path, text)


def update_handoff() -> None:
    path = "AI_HANDOFF.md"
    text = read(path)
    text = replace_once(
        text,
        "Status: Master Plan and implementation roadmap accepted — Campaign 001 accepted complete — P01 physical-host closure active — runtime implementation unauthorized\n",
        "Status: Campaign 001 accepted complete — Phase 0C-19 deep Workspace planning-load reconciliation active — P01 paused — runtime implementation unauthorized\n",
        "handoff status",
    )
    append_section(
        path,
        "## Active Phase 0C-19 planning-load reconciliation",
        """
## Active Phase 0C-19 planning-load reconciliation

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

The deep Workspace donor study merged in `Ptah-space` as `23dc4b19a0189ba55e08dfa124761efa806bd68b` after 26/26 study cases and all eleven exact-head workflows passed.

It must be synchronized into the complete private planning load before P01 continues. Read:

1. `planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md`;
2. `work-packages/PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION.md`;
3. proposed ADR-0037;
4. the Phase 0C-19 validator and regressions.

Current boundary:

```text
Phase 0C-19: CANDIDATE / IN REVIEW
ADR-0037: PROPOSED
P01: PAUSED
PR #46 proof commit: PROVISIONAL
physical-host collection: NOT STARTED
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```

Do not run the physical proof until Phase 0C-19 is accepted and the proof commit is confirmed or superseded.
""",
    )
    write(path, text)


def update_decisions() -> None:
    append_section(
        "DECISIONS.md",
        "### D-053 — Deep Workspace operations must be reconciled before P01 resumes",
        """
### D-053 — Deep Workspace operations must be reconciled before P01 resumes

**PROPOSED.** ADR-0037 maps the `ptah.workspace.operations.v2` deep-study profile into the complete Master Plan and roadmap load. The profile adds typed operations, effect classes, permission/Grant/approval separation, materialization truth, progress/partial retention, stable result handles, scheduling semantics, exact preconditions, honest result states, provenance, limits and cross-interface continuity without adding a Core family or reopening WP01–WP14.

Until accepted, P01 is paused and the PR #46 proof commit remains provisional.

Full decision: `decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md`.
""",
    )


def update_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["active_work_unit"] = "Phase-0C-19-deep-workspace-roadmap-reconciliation"
    data["runtime_implementation_authorized"] = False
    data["next_action"] = "Complete and accept Phase 0C-19 deep Workspace planning-load reconciliation, then confirm or supersede the provisional Ptah-space physical-proof commit before P01 resumes."
    for programme in data.get("programmes", []):
        if programme.get("id") == "P01":
            programme["status"] = "paused_pending_phase0c19_acceptance_then_external_physical_host"
    data["phase0c19_deep_workspace_reconciliation"] = {
        "status": "candidate_in_review",
        "source_repository": "jaydumisuni/Ptah-space",
        "source_candidate_exact_head": "bf4ae98b9d492ad688644fd6a330aaf435ac70c1",
        "source_merge": "23dc4b19a0189ba55e08dfa124761efa806bd68b",
        "source_workflow_run": "30087967851",
        "source_artifact_id": "8594496859",
        "source_artifact_digest": "sha256:aea4fde3f600a6e4c3fc2f6ff3614918a5f714c6f8ebbf6ab3fb3cb29ccaf12b",
        "source_validation_sha256": "329262e7bb12e0841f1884664e713ab8e55a58e45a2430d4abf77ccdde65ecbe",
        "mechanical_capability_count": 22,
        "mapping_count": 28,
        "fixture_count": 20,
        "original_regression_count": 26,
        "new_core_entity_required": False,
        "frozen_contract_reopen_required": False,
        "adr_0037_status": "proposed",
        "p01_paused": True,
        "provisional_proof_commit": "23dc4b19a0189ba55e08dfa124761efa806bd68b",
        "physical_host_collection_started": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
    }
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def validate_boundary() -> None:
    required = [
        "MASTER_PLAN.md",
        "IMPLEMENTATION_ROADMAP.md",
        "CURRENT_STATE.md",
        "PROGRESS.md",
        "AI_HANDOFF.md",
        "DECISIONS.md",
        "planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md",
        "planning/MASTER-PLAN-RECONCILIATION.md",
        "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md",
        "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md",
    ]
    for path in required:
        text = read(path)
        if path in {"MASTER_PLAN.md", "IMPLEMENTATION_ROADMAP.md", "CURRENT_STATE.md", "AI_HANDOFF.md"} and MARKER not in text:
            raise SyncError(f"{path}: missing Phase 0C-19 marker")
    state = read("CURRENT_STATE.md")
    if "**Runtime implementation:** NOT AUTHORIZED" not in state:
        raise SyncError("runtime authorization boundary changed")
    if "ADR-0037: PROPOSED" not in state or "P01: PAUSED" not in state:
        raise SyncError("candidate state boundary missing")
    index = json.loads((ROOT / "master-plan-index.json").read_text(encoding="utf-8"))
    candidate = index.get("phase0c19_deep_workspace_reconciliation", {})
    if candidate.get("new_core_entity_required") is not False:
        raise SyncError("new Core entity unexpectedly required")
    if candidate.get("frozen_contract_reopen_required") is not False:
        raise SyncError("frozen contract reopening unexpectedly required")
    if candidate.get("physical_host_collection_started") is not False:
        raise SyncError("physical-host collection must remain false")
    if candidate.get("runtime_implementation_authorized") is not False:
        raise SyncError("candidate must remain non-authorizing")


def main() -> None:
    update_master_plan()
    update_roadmap()
    update_recovery_ledger()
    update_reconciliation()
    update_physical_closure()
    update_p01_selection()
    update_current_state()
    update_progress()
    update_handoff()
    update_decisions()
    update_index()
    validate_boundary()
    print("Phase 0C-19 deep Workspace planning-load synchronization applied")


if __name__ == "__main__":
    main()
