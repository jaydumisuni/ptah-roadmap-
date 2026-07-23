#!/usr/bin/env python3
"""Synchronize the Phase 0C-18 diagnostic and worker-execution candidate."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SyncError(RuntimeError):
    pass


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one source fragment, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def sync_master_plan() -> None:
    path = ROOT / "MASTER_PLAN.md"
    replace_once(
        path,
        "15. **Completion is evidence-backed.** Source presence and UI claims are insufficient.\n",
        "15. **Completion is evidence-backed.** Source presence and UI claims are insufficient.\n"
        "16. **Ptah may diagnose its own platform condition without choosing the caller's work.** Missing capability, degradation or incompatibility may produce an evidence-backed advisory, but upgrade approval and task choice remain caller-owned.\n"
        "17. **Caller-given work may use bounded worker formations.** A caller-selected Recipe or Plan may apply the Sergeant-derived ten-for-two pattern for efficient parallel execution, while scope, semantic decomposition and result acceptance remain caller-owned.\n",
        "master plan diagnostic and worker principles",
    )
    replace_once(
        path,
        "- caller-defined Recipe, Plan, Run and Step records plus Receipt and Evidence storage;\n"
        "- migrations, retention, supersession, tombstones and recovery projections;\n"
        "- neutral APIs and event envelopes.",
        "- caller-defined Recipe, Plan, Run and Step records plus Receipt and Evidence storage;\n"
        "- caller-defined worker formation scheduling, checkpoint and evidence projections;\n"
        "- migrations, retention, supersession, tombstones and recovery projections;\n"
        "- evidence-backed diagnostic advisory Views and Artifacts over platform health, capability and execution records;\n"
        "- neutral APIs and event envelopes.",
        "master plan Core diagnostics and workers",
    )
    replace_once(
        path,
        "- Node, Provider and health status;\n- approvals and security boundaries;",
        "- Node, Provider and health status;\n"
        "- platform diagnostic advisories, missing-capability explanations and caller-controlled upgrade responses;\n"
        "- worker formation, checkpoint, conflict and partial-result status;\n"
        "- approvals and security boundaries;",
        "master plan human diagnostics and workers",
    )
    replace_once(
        path,
        "- autonomous release approval;\n- universal policy decisions for every user;",
        "- autonomous release approval;\n"
        "- autonomous self-upgrade, purchasing, vendor selection or task reprioritization;\n"
        "- autonomous semantic job decomposition or result acceptance;\n"
        "- universal policy decisions for every user;",
        "master plan non-goals",
    )
    replace_once(
        path,
        "### Receipt and Evidence\n\n"
        "A Receipt is immutable producer evidence. Evidence may support a bounded Claim but does not automatically equal review, acceptance or authoritative truth.\n",
        "### Receipt and Evidence\n\n"
        "A Receipt is immutable producer evidence. Evidence may support a bounded Claim but does not automatically equal review, acceptance or authoritative truth.\n\n"
        "### Diagnostic advisory\n\n"
        "A diagnostic advisory is a typed View or Artifact over exact Node, Provider, capability, health, Activity, Attempt, Event, Receipt and Evidence records. It may identify a missing capability, degradation, incompatibility or repeated failure and ask a caller for an upgrade or inspection. It is not a new Core authority entity, does not choose caller work and cannot approve or execute its own recommendation.\n\n"
        "### Worker formation\n\n"
        "A worker formation is a caller-defined Recipe, Plan or Run composed of bounded Activities and Attempts. A caller may select the Sergeant-derived `max(20, human-equivalent workers × 10)` execution pattern. Ptah may allocate, place, run, checkpoint, retry and evidence the declared workers within configured authority, but it may not invent the job, add semantic scope or accept the result.\n",
        "master plan world-model diagnostic and worker projections",
    )
    replace_once(
        path,
        "- optional Facility failure does not collapse unrelated Activities;\n"
        "- events and logs may be incomplete without manufacturing success;",
        "- optional Facility failure does not collapse unrelated Activities;\n"
        "- a missing or degraded capability produces a bounded diagnostic advisory without inventing a new user goal;\n"
        "- unrelated Activities continue when their configured requirements remain satisfied;\n"
        "- failed worker Attempts remain distinct, and conflicting formation outputs remain visible;\n"
        "- worker completion does not equal caller acceptance;\n"
        "- events and logs may be incomplete without manufacturing success;",
        "master plan reliability diagnostics and workers",
    )
    replace_once(
        path,
        "- limitations, truncation and privacy filtering;\n"
        "- immutable Receipts and retained Artifacts;",
        "- limitations, truncation and privacy filtering;\n"
        "- expected-condition, missing-capability, degradation and compatibility-gap evidence;\n"
        "- diagnostic advisory revisions, uncertainty and recheck state;\n"
        "- worker formation roles, independence, checkpoints, conflicts and partial-result evidence;\n"
        "- immutable Receipts and retained Artifacts;",
        "master plan observability diagnostics and workers",
    )
    replace_once(
        path,
        "Responsible for truthful host capability, local Provider lifecycle, Activity execution, local storage, evidence generation and reconnect.",
        "Responsible for truthful host capability, local Provider lifecycle, Activity execution, caller-defined worker formation execution, local storage, evidence generation, bounded platform diagnostics and reconnect. Diagnostic output may request caller action, and scheduling may manage declared workers, but neither may select caller work or authorize an upgrade or result.",
        "master plan node agent boundary",
    )
    replace_once(
        path,
        "- dependency and image updates;\n- evidence retention;",
        "- dependency and image updates;\n"
        "- evidence-backed diagnostic and upgrade advisories;\n"
        "- worker formation progress, independence, partial failures and conflicts;\n"
        "- evidence retention;",
        "master plan operator diagnostics and workers",
    )
    replace_once(
        path,
        "- dependency/security updates rerun the affected proof suites;\n"
        "- no upgrade erases failed or uncertain external effects.",
        "- dependency/security updates rerun the affected proof suites;\n"
        "- Ptah may request an upgrade from exact diagnostic evidence but may not approve, purchase, install or activate it without caller-configured authority;\n"
        "- upgrade acknowledgement does not equal resolution: the affected condition is rechecked and retained as resolved, still present or inconclusive;\n"
        "- no upgrade erases failed or uncertain external effects.",
        "master plan upgrade boundary",
    )
    replace_once(
        path,
        "- failures remain visible and scoped;\n"
        "- a Workspace survives client and runtime interruption with verified recovery;",
        "- failures remain visible and scoped;\n"
        "- a missing or degraded platform capability produces an evidence-backed advisory while leaving task choice and upgrade approval with the caller;\n"
        "- a caller-selected ten-for-two Recipe can run bounded parallel workers with distinct evidence, checkpoints and visible conflicts;\n"
        "- a Workspace survives client and runtime interruption with verified recovery;",
        "master plan success measures",
    )


def sync_roadmap() -> None:
    path = ROOT / "IMPLEMENTATION_ROADMAP.md"
    replace_once(
        path,
        "- Node health, readiness, reachability and pressure projections;\n"
        "- Event and Receipt correlation.",
        "- Node health, readiness, reachability and pressure projections;\n"
        "- configured capability, compatibility, resource and worker-capacity baselines;\n"
        "- bounded missing-capability and degradation advisory generation;\n"
        "- Event and Receipt correlation.",
        "roadmap A02 deliver",
    )
    replace_once(
        path,
        "- health and capability claims are evidence-bound.\n\nDependencies: A01.",
        "- health and capability claims are evidence-bound;\n"
        "- a missing capability produces an advisory that identifies evidence, expected condition, impact and uncertainty without inventing a user goal;\n"
        "- worker-capacity claims are tied to exact Node/Provider evidence;\n"
        "- advisory creation cannot install or approve an upgrade.\n\nDependencies: A01.",
        "roadmap A02 proof",
    )
    replace_once(
        path,
        "- immutable Receipt generation;\n"
        "- resource and timing evidence.",
        "- immutable Receipt generation;\n"
        "- caller-defined Recipe/Plan worker formation execution;\n"
        "- primary/verifier and other declared independence projections;\n"
        "- worker checkpoint, partial-result and conflict evidence;\n"
        "- repeated-failure correlation and diagnostic Event/Artifact emission;\n"
        "- resource and timing evidence.",
        "roadmap A04 deliver",
    )
    replace_once(
        path,
        "- acknowledgement-only completion fails;\n"
        "- failed and cancelled work remains queryable.\n\nDependencies: A02, A03.",
        "- acknowledgement-only completion fails;\n"
        "- failed and cancelled work remains queryable;\n"
        "- a caller-selected two-human-equivalent ten-for-two Recipe creates twenty bounded worker slots;\n"
        "- each failed retry creates a distinct Attempt and requires submitted Policy authority;\n"
        "- configured independent-check lanes cannot silently collapse into one worker;\n"
        "- conflicting worker outputs remain visible rather than being forced into agreement;\n"
        "- worker completion cannot become result acceptance;\n"
        "- repeated failures may produce a bounded advisory, but no new job or upgrade begins without a caller submission;\n"
        "- unrelated Activities remain runnable when their requirements are satisfied.\n\nDependencies: A02, A03.",
        "roadmap A04 proof",
    )
    replace_once(
        path,
        "- restart recovery projection;\n- basic handoff record.",
        "- restart recovery projection;\n"
        "- worker formation, role, checkpoint and partial-result recovery projection;\n"
        "- basic handoff record.",
        "roadmap A06 deliver",
    )
    replace_once(
        path,
        "- cross-Workspace retrieval fails without Grant;\n"
        "- agent replacement preserves authority and handoff state.\n\nDependencies: A03, A04, A05.",
        "- cross-Workspace retrieval fails without Grant;\n"
        "- agent replacement preserves authority and handoff state;\n"
        "- interrupted worker formations recover without losing role, independence, checkpoint or conflict evidence.\n\nDependencies: A03, A04, A05.",
        "roadmap A06 proof",
    )
    replace_once(
        path,
        "- Provider/Node health view;\n- checkpoint/reconnect controls;",
        "- Provider/Node health view;\n"
        "- platform diagnostic advisory and missing-capability panel;\n"
        "- worker formation, role, checkpoint, conflict and partial-result panel;\n"
        "- caller controls to dismiss, defer, choose an alternative or submit an authorized upgrade Activity;\n"
        "- checkpoint/reconnect controls;",
        "roadmap A14 deliver",
    )
    replace_once(
        path,
        "- mobile/tablet projection does not hide critical status or approval controls.\n\nDependencies: A05–A13.",
        "- mobile/tablet projection does not hide critical status or approval controls;\n"
        "- Ptah presents observed facts separately from upgrade suggestions;\n"
        "- worker completion is visually separate from caller/reviewer acceptance;\n"
        "- no advisory can approve or execute its own recommendation.\n\nDependencies: A05–A13.",
        "roadmap A14 proof",
    )
    replace_once(
        path,
        "- green status without reports fails;\n"
        "- human operator and Hunter handoff tests pass.\n\nDependencies: A01–A14.",
        "- green status without reports fails;\n"
        "- human operator and Hunter handoff tests pass;\n"
        "- missing capability and degraded Provider advisories pass positive, false-positive, stale-evidence and unresolved-upgrade tests;\n"
        "- ten-for-two formation tests prove bounded workers, independent evidence, checkpoint recovery, visible conflicts and no automatic result acceptance;\n"
        "- exact-head proof confirms Ptah cannot choose caller work or autonomously install an upgrade.\n\nDependencies: A01–A14.",
        "roadmap A15 proof",
    )
    replace_once(
        path,
        "- immutable Receipt/Artifact retention;\n"
        "- limitations and negative evidence.\n\n## Track X4",
        "- immutable Receipt/Artifact retention;\n"
        "- limitations and negative evidence;\n"
        "- diagnostic advisory evidence, expected conditions, uncertainty and post-upgrade recheck state;\n"
        "- worker formation role, independence, checkpoint, retry, conflict and partial-result evidence.\n\n## Track X4",
        "roadmap X3 diagnostics and workers",
    )


def sync_decisions() -> None:
    path = ROOT / "DECISIONS.md"
    old = """### ADR-0033 — First vertical-slice host, licence, layout and backend selections

**PROPOSED.** Master Plan/roadmap authority is complete. The physical pinned-host result, package and retention acceptance, final Phase 0C closure review and explicit runtime authorization remain open.
"""
    new = old + """
### ADR-0036 — Platform diagnostic advisory and efficient worker execution boundary

**PROPOSED.** Ptah may compare configured platform expectations with observed health, capability and execution evidence and emit a bounded upgrade or inspection advisory. For a caller-submitted job and Recipe/Plan, Ptah may apply the Sergeant-derived ten-for-two pattern to run bounded parallel workers and independent checks. Ptah may not choose caller work, invent semantic scope, approve a result or install its own upgrade.

Full decision: `decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md`.
"""
    replace_once(path, old, new, "decisions ADR-0036")


def sync_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    marker = "\n---\n\n## Active Phase 0C blockers\n"
    section = """
---

## Phase 0C-18 diagnostic and efficient-worker candidate

The owner clarified that Ptah remains neutral regarding caller intent while retaining two bounded platform capabilities.

Candidate authority:

- `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md`;
- proposed ADR-0036;
- `work-packages/PHASE-0C-18-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md`.

Allowed diagnostic behavior: detect missing capability, degradation, incompatibility, resource shortage, repeated failure or failed post-condition and emit an evidence-backed advisory asking an authorized caller for an upgrade or inspection.

Allowed execution behavior: after a caller submits a job and selects a Recipe/Plan, apply `max(20, human-equivalent workers × 10)` to run bounded worker Activities, independent checks, checkpoints and configured merge/recovery mechanics.

Forbidden: choose caller work, invent semantic subtasks, reprioritize outside submitted Policy, approve a result, approve/purchase/install an upgrade, mark acknowledgement as resolution, block unrelated capable work or become Hunter/Sergeant authority.

This candidate uses frozen primitives only, does not start AF03 and does not change P01, ADR-0033 or runtime authorization.

---

## Active Phase 0C blockers
"""
    replace_once(path, marker, "\n" + section, "current state Phase 0C-18 section")


def sync_progress() -> None:
    path = ROOT / "PROGRESS.md"
    marker = "\n## Active Phase 0C closure work\n"
    section = """
## Diagnostic advisory and efficient worker candidate

- [x] owner boundary recovered: diagnose platform condition without deciding caller work;
- [x] owner ten-for-two boundary recovered: spread a caller-given job across bounded workers for speed and efficiency;
- [x] frozen Node/Provider health, Recipe/Plan/Run/Step, Workspace/Activity/Attempt, Reservation/Grant/Lease/Fence, Event/Receipt, Claim/Evidence and View/Artifact primitives mapped;
- [x] diagnostic advisory, upgrade-request and worker-execution boundaries written;
- [x] proposed ADR-0036 and Phase 0C-18 work package written;
- [x] Programme A02/A04/A06/A14/A15 proof placement added;
- [-] exact-head validator, adversarial tests and review pending;
- [ ] accept ADR-0036 and Phase 0C-18;
- [ ] implementation remains unauthorized.

## Active Phase 0C closure work
"""
    replace_once(path, marker, "\n" + section, "progress Phase 0C-18 section")


def sync_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    marker = "\n## Exact next action\n"
    section = """
## Diagnostic advisory and efficient worker candidate

Ptah remains neutral regarding caller intent. The Phase 0C-18 candidate permits two bounded platform behaviors:

```text
configured expected platform condition
→ observed health/capability/execution evidence
→ missing capability or degradation advisory
→ human/calling application chooses whether to upgrade, replace, defer or continue
```

```text
caller-submitted job and Recipe/Plan
→ max(20, human-equivalent workers × 10)
→ bounded parallel Activities, independent checks and checkpoints
→ configured merge or partial/conflicting result
→ caller or external reviewer decides acceptance
```

Read:

- `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md`;
- proposed ADR-0036;
- Phase 0C-18 work package.

Ptah may manage declared workers and ask for an upgrade, but may not choose caller work, invent semantic scope, approve a result, approve/install the upgrade or treat acknowledgement as resolution. AF03 remains READY / NOT STARTED.

## Exact next action
"""
    replace_once(path, marker, "\n" + section, "handoff Phase 0C-18 section")


def sync_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("runtime_implementation_authorized") is not False:
        raise SyncError("runtime unexpectedly authorized")
    if data.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise SyncError("P01 active work drifted")
    protocol = "planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"
    if protocol not in data["recovery_order"]:
        data["recovery_order"].append(protocol)
    data.setdefault("product_clarifications", {})["platform_diagnostic_and_worker_execution"] = {
        "status": "candidate_under_review",
        "protocol": protocol,
        "decision": "decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md",
        "work_package": "work-packages/PHASE-0C-18-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md",
        "uses_frozen_primitives_only": True,
        "new_core_entity_required": False,
        "may_detect_missing_capability": True,
        "may_detect_degradation": True,
        "may_request_upgrade": True,
        "may_execute_caller_selected_ten_for_two": True,
        "ten_for_two_multiplier": 10,
        "ten_for_two_minimum_worker_slots": 20,
        "caller_job_required": True,
        "caller_recipe_or_plan_required": True,
        "may_choose_caller_work": False,
        "may_invent_semantic_subtasks": False,
        "may_accept_worker_result": False,
        "may_approve_upgrade": False,
        "may_install_upgrade_autonomously": False,
        "may_block_unrelated_capable_work": False,
        "af03_started": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
    }
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    sync_master_plan()
    sync_roadmap()
    sync_decisions()
    sync_current_state()
    sync_progress()
    sync_handoff()
    sync_index()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    donor = (ROOT / "DONOR_RECOVERY.md").read_text(encoding="utf-8")
    adr0033 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    manifest = (ROOT / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md").read_text(encoding="utf-8")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current or "**Runtime implementation:** AUTHORIZED" in current:
        raise SyncError("runtime boundary failed")
    if "**Status:** COMPLETE AND FROZEN" not in donor:
        raise SyncError("Phase 0A is not frozen")
    if "Status: proposed" not in adr0033:
        raise SyncError("ADR-0033 is not proposed")
    if "## AF03" not in manifest:
        raise SyncError("AF03 section missing")
    af03 = manifest.split("## AF03", 1)[1].split("## AF04", 1)[0]
    if "- status: READY / NOT STARTED" not in af03 or "- status: ACTIVE" in af03:
        raise SyncError("AF03 is not ready/not started")
    print("Phase 0C-18 diagnostic and worker-execution candidate synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
