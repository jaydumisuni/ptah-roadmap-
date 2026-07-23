#!/usr/bin/env python3
"""Synchronize the Phase 0C-18 platform diagnostic advisory candidate."""
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
        "15. **Completion is evidence-backed.** Source presence and UI claims are insufficient.\n16. **Ptah may diagnose its own platform condition without choosing the caller's work.** Missing capability, degradation or incompatibility may produce an evidence-backed advisory, but upgrade approval and task choice remain caller-owned.\n",
        "master plan diagnostic principle",
    )
    replace_once(
        path,
        "- migrations, retention, supersession, tombstones and recovery projections;\n- neutral APIs and event envelopes.",
        "- migrations, retention, supersession, tombstones and recovery projections;\n- evidence-backed diagnostic advisory Views and Artifacts over platform health, capability and execution records;\n- neutral APIs and event envelopes.",
        "master plan core diagnostics",
    )
    replace_once(
        path,
        "- Node, Provider and health status;\n- approvals and security boundaries;",
        "- Node, Provider and health status;\n- platform diagnostic advisories, missing-capability explanations and caller-controlled upgrade responses;\n- approvals and security boundaries;",
        "master plan human diagnostics",
    )
    replace_once(
        path,
        "- autonomous release approval;\n- universal policy decisions for every user;",
        "- autonomous release approval;\n- autonomous self-upgrade, purchasing, vendor selection or task reprioritization;\n- universal policy decisions for every user;",
        "master plan non-goal",
    )
    replace_once(
        path,
        "### Receipt and Evidence\n\nA Receipt is immutable producer evidence. Evidence may support a bounded Claim but does not automatically equal review, acceptance or authoritative truth.\n",
        "### Receipt and Evidence\n\nA Receipt is immutable producer evidence. Evidence may support a bounded Claim but does not automatically equal review, acceptance or authoritative truth.\n\n### Diagnostic advisory\n\nA diagnostic advisory is a typed View or Artifact over exact Node, Provider, capability, health, Activity, Attempt, Event, Receipt and Evidence records. It may identify a missing capability, degradation, incompatibility or repeated failure and ask a caller for an upgrade or inspection. It is not a new Core authority entity, does not choose caller work and cannot approve or execute its own recommendation.\n",
        "master plan world model diagnostic advisory",
    )
    replace_once(
        path,
        "- optional Facility failure does not collapse unrelated Activities;\n- events and logs may be incomplete without manufacturing success;",
        "- optional Facility failure does not collapse unrelated Activities;\n- a missing or degraded capability produces a bounded diagnostic advisory without inventing a new user goal;\n- unrelated Activities continue when their configured requirements remain satisfied;\n- events and logs may be incomplete without manufacturing success;",
        "master plan reliability diagnostics",
    )
    replace_once(
        path,
        "- limitations, truncation and privacy filtering;\n- immutable Receipts and retained Artifacts;",
        "- limitations, truncation and privacy filtering;\n- expected-condition, missing-capability, degradation and compatibility-gap evidence;\n- diagnostic advisory revisions, uncertainty and recheck state;\n- immutable Receipts and retained Artifacts;",
        "master plan observability diagnostics",
    )
    replace_once(
        path,
        "Responsible for truthful host capability, local Provider lifecycle, Activity execution, local storage, evidence generation and reconnect.",
        "Responsible for truthful host capability, local Provider lifecycle, Activity execution, local storage, evidence generation, bounded platform diagnostics and reconnect. Diagnostic output may request caller action but may not select caller work or authorize an upgrade.",
        "master plan node agent diagnostics",
    )
    replace_once(
        path,
        "- dependency and image updates;\n- evidence retention;",
        "- dependency and image updates;\n- evidence-backed diagnostic and upgrade advisories;\n- evidence retention;",
        "master plan operator diagnostics",
    )
    replace_once(
        path,
        "- dependency/security updates rerun the affected proof suites;\n- no upgrade erases failed or uncertain external effects.",
        "- dependency/security updates rerun the affected proof suites;\n- Ptah may request an upgrade from exact diagnostic evidence but may not approve, purchase, install or activate it without caller-configured authority;\n- upgrade acknowledgement does not equal resolution: the affected condition is rechecked and retained as resolved, still present or inconclusive;\n- no upgrade erases failed or uncertain external effects.",
        "master plan upgrade boundary",
    )
    replace_once(
        path,
        "- failures remain visible and scoped;\n- a Workspace survives client and runtime interruption with verified recovery;",
        "- failures remain visible and scoped;\n- a missing or degraded platform capability produces an evidence-backed advisory while leaving task choice and upgrade approval with the caller;\n- a Workspace survives client and runtime interruption with verified recovery;",
        "master plan success measure",
    )


def sync_roadmap() -> None:
    path = ROOT / "IMPLEMENTATION_ROADMAP.md"
    replace_once(
        path,
        "- Node health, readiness, reachability and pressure projections;\n- Event and Receipt correlation.",
        "- Node health, readiness, reachability and pressure projections;\n- configured capability, compatibility and resource baselines;\n- bounded missing-capability and degradation advisory generation;\n- Event and Receipt correlation.",
        "roadmap A02 deliver",
    )
    replace_once(
        path,
        "- health and capability claims are evidence-bound.\n\nDependencies: A01, A02.",
        "- health and capability claims are evidence-bound;\n- a missing capability produces an advisory that identifies evidence, expected condition, impact and uncertainty without inventing a user goal;\n- advisory creation cannot install or approve an upgrade.\n\nDependencies: A01, A02.",
        "roadmap A03 dependency anchor diagnostic proof",
    )
    replace_once(
        path,
        "- resource and timing evidence.\n\nProof:",
        "- resource and timing evidence;\n- repeated-failure correlation and diagnostic Event/Artifact emission without collapsing distinct Attempts.\n\nProof:",
        "roadmap A04 deliver diagnostics",
    )
    replace_once(
        path,
        "- failed and cancelled work remains queryable.\n\nDependencies: A02, A03.",
        "- failed and cancelled work remains queryable;\n- repeated failures may produce a bounded advisory, but no new Activity or upgrade begins without a caller submission;\n- unrelated Activities remain runnable when their requirements are satisfied.\n\nDependencies: A02, A03.",
        "roadmap A04 proof diagnostics",
    )
    replace_once(
        path,
        "- Provider/Node health view;\n- checkpoint/reconnect controls;",
        "- Provider/Node health view;\n- platform diagnostic advisory and missing-capability panel;\n- caller controls to dismiss, defer, choose an alternative or submit an authorized upgrade Activity;\n- checkpoint/reconnect controls;",
        "roadmap A14 deliver diagnostics",
    )
    replace_once(
        path,
        "- mobile/tablet projection does not hide critical status or approval controls.\n\nDependencies: A05–A13.",
        "- mobile/tablet projection does not hide critical status or approval controls;\n- Ptah presents observed facts separately from upgrade suggestions;\n- no advisory can approve or execute its own recommendation.\n\nDependencies: A05–A13.",
        "roadmap A14 proof diagnostics",
    )
    replace_once(
        path,
        "- human operator and Hunter handoff tests pass.\n\nDependencies: A01–A14.",
        "- human operator and Hunter handoff tests pass;\n- missing capability and degraded Provider advisories pass positive, false-positive, stale-evidence and unresolved-upgrade tests;\n- exact-head proof confirms Ptah cannot choose caller work or autonomously install an upgrade.\n\nDependencies: A01–A14.",
        "roadmap A15 diagnostics",
    )
    replace_once(
        path,
        "- limitations and negative evidence.\n\n## Track X4",
        "- limitations and negative evidence;\n- diagnostic advisory evidence, expected conditions, uncertainty and post-upgrade recheck state.\n\n## Track X4",
        "roadmap X3 diagnostics",
    )


def sync_decisions() -> None:
    path = ROOT / "DECISIONS.md"
    old = """### ADR-0033 — First vertical-slice host, licence, layout and backend selections

**PROPOSED.** Master Plan/roadmap authority is complete. The physical pinned-host result, package and retention acceptance, final Phase 0C closure review and explicit runtime authorization remain open.
"""
    new = old + """
### ADR-0036 — Platform diagnostic advisory boundary

**PROPOSED.** Ptah may compare configured platform expectations with observed health, capability and execution evidence and emit a bounded upgrade or inspection advisory. Ptah may not choose caller work, approve or install its own upgrade, block unrelated capable work or become Hunter/Sergeant authority.

Full decision: `decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md`.
"""
    replace_once(path, old, new, "decisions ADR-0036")


def sync_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    marker = "\n---\n\n## Active Phase 0C blockers\n"
    section = """
---

## Phase 0C-18 platform diagnostic advisory candidate

The owner clarified that Ptah remains neutral regarding caller intent while retaining a small bounded intelligence for its own platform condition.

Candidate authority:

- `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md`;
- proposed ADR-0036;
- `work-packages/PHASE-0C-18-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md`.

Allowed: detect missing capability, degradation, incompatibility, resource shortage, repeated failure or failed post-condition and emit an evidence-backed advisory asking an authorized caller for an upgrade or inspection.

Forbidden: choose caller work, reprioritize Activities, approve/purchase/install an upgrade, mark acknowledgement as resolution, block unrelated capable work or become Hunter/Sergeant authority.

This candidate uses frozen primitives only, does not start AF03 and does not change P01, ADR-0033 or runtime authorization.

---

## Active Phase 0C blockers
"""
    replace_once(path, marker, "\n" + section, "current state diagnostic section")


def sync_progress() -> None:
    path = ROOT / "PROGRESS.md"
    marker = "\n## Active Phase 0C closure work\n"
    section = """
## Platform diagnostic advisory candidate

- [x] owner boundary recovered: diagnose platform condition without deciding caller work;
- [x] frozen Node/Provider health, capability, Activity/Attempt, Event/Receipt, Claim/Evidence and View/Artifact primitives mapped;
- [x] diagnostic advisory and upgrade-request boundary written;
- [x] proposed ADR-0036 and Phase 0C-18 work package written;
- [x] Programme A02/A04/A14/A15 proof placement added;
- [-] exact-head validator, adversarial tests and review pending;
- [ ] accept ADR-0036 and Phase 0C-18;
- [ ] implementation remains unauthorized.

## Active Phase 0C closure work
"""
    replace_once(path, marker, "\n" + section, "progress diagnostic section")


def sync_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    marker = "\n## Exact next action\n"
    section = """
## Platform diagnostic advisory candidate

Ptah remains neutral regarding caller intent. The Phase 0C-18 candidate permits bounded self-diagnostics only:

```text
configured expected platform condition
→ observed health/capability/execution evidence
→ missing capability or degradation advisory
→ human/calling application chooses whether to upgrade, replace, defer or continue
```

Read:

- `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md`;
- proposed ADR-0036;
- Phase 0C-18 work package.

Ptah may ask for an upgrade but may not choose caller work, approve or install the upgrade, or treat acknowledgement as resolution. AF03 remains READY / NOT STARTED.

## Exact next action
"""
    replace_once(path, marker, "\n" + section, "handoff diagnostic section")


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
    data.setdefault("product_clarifications", {})["platform_diagnostic_advisory"] = {
        "status": "candidate_under_review",
        "protocol": protocol,
        "decision": "decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md",
        "work_package": "work-packages/PHASE-0C-18-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md",
        "uses_frozen_primitives_only": True,
        "new_core_entity_required": False,
        "may_detect_missing_capability": True,
        "may_detect_degradation": True,
        "may_request_upgrade": True,
        "may_choose_caller_work": False,
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
    if "AF03" not in manifest or "- status: READY / NOT STARTED" not in manifest:
        raise SyncError("AF03 is not ready/not started")
    print("Phase 0C-18 diagnostic advisory candidate synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
