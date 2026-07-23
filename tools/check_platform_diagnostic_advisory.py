#!/usr/bin/env python3
"""Validate the Phase 0C-18 diagnostic and worker-execution candidate."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

PROTOCOL = Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md")
ADR = Path("decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md")
WORK_PACKAGE = Path("work-packages/PHASE-0C-18-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md")
MASTER_PLAN = Path("MASTER_PLAN.md")
ROADMAP = Path("IMPLEMENTATION_ROADMAP.md")
DECISIONS = Path("DECISIONS.md")
CURRENT_STATE = Path("CURRENT_STATE.md")
PROGRESS = Path("PROGRESS.md")
HANDOFF = Path("AI_HANDOFF.md")
MASTER_INDEX = Path("master-plan-index.json")
DONOR_REGISTER = Path("DONOR_RECOVERY.md")
CAMPAIGN_MANIFEST = Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md")
ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")

REQUIRED_FILES = (
    PROTOCOL,
    ADR,
    WORK_PACKAGE,
    MASTER_PLAN,
    ROADMAP,
    DECISIONS,
    CURRENT_STATE,
    PROGRESS,
    HANDOFF,
    MASTER_INDEX,
    DONOR_REGISTER,
    CAMPAIGN_MANIFEST,
    ADR0033,
)


class ValidationError(RuntimeError):
    pass


def read(root: Path, relative: Path) -> str:
    path = root / relative
    if not path.is_file():
        raise ValidationError(f"missing required file: {relative}")
    return path.read_text(encoding="utf-8")


def require(text: str, token: str, label: str) -> None:
    if token not in text:
        raise ValidationError(f"missing {label}: {token}")


def reject(text: str, token: str, label: str) -> None:
    if token in text:
        raise ValidationError(f"forbidden {label}: {token}")


def validate_repo(root: Path) -> dict[str, Any]:
    texts = {relative: read(root, relative) for relative in REQUIRED_FILES}
    protocol = texts[PROTOCOL]
    adr = texts[ADR]
    work_package = texts[WORK_PACKAGE]
    master_plan = texts[MASTER_PLAN]
    roadmap = texts[ROADMAP]
    decisions = texts[DECISIONS]
    current = texts[CURRENT_STATE]
    progress = texts[PROGRESS]
    handoff = texts[HANDOFF]
    donor = texts[DONOR_REGISTER]
    campaign = texts[CAMPAIGN_MANIFEST]
    adr0033 = texts[ADR0033]
    index = json.loads(texts[MASTER_INDEX])

    # Candidate and neutral authority boundary.
    require(protocol, "Status: candidate product clarification", "protocol candidate state")
    require(protocol, "not product consciousness, business judgment or task planning", "non-conscious boundary")
    require(protocol, "Caller chooses the work and supplies or selects the execution recipe", "caller work choice")
    require(protocol, "Ptah may emit a bounded diagnostic advisory", "bounded advisory")
    require(protocol, "Ptah does not borrow Sergeant's review authority", "Sergeant authority boundary")
    require(protocol, "No new Core entity is required", "frozen primitive composition")
    require(protocol, "observed facts from suggestions", "fact/suggestion separation")
    require(protocol, "Ptah may ask for:", "upgrade request allowance")
    require(protocol, "approve its own advisory", "self-approval prohibition")
    require(protocol, "install, upgrade, remove or replace software without configured authority", "autonomous install prohibition")
    require(protocol, "block unrelated work merely because an upgrade is available", "unrelated work boundary")
    require(protocol, "acknowledgement does not equal successful upgrade", "post-condition boundary")
    require(protocol, "Ptah does not decide which option the caller should choose", "example caller-choice boundary")

    # Ten-for-two worker execution boundary.
    require(protocol, "## 3. Sergeant patterns borrowed", "Sergeant patterns section")
    require(protocol, "### 3.2 Ten-for-two worker execution pattern", "worker pattern section")
    require(protocol, "worker capacity = max(20, human-equivalent workers × 10)", "worker capacity equation")
    require(protocol, "twenty bounded worker slots", "two-worker formation capacity")
    require(protocol, "caller-selected or caller-supplied formation recipe", "caller recipe boundary")
    require(protocol, "instantiate the declared worker Activities", "worker instantiation")
    require(protocol, "run independent Attempts concurrently", "worker independence")
    require(protocol, "checkpoint after configured milestones", "worker checkpoints")
    require(protocol, "retry or replace a failed worker Attempt", "bounded worker retry")
    require(protocol, "assemble outputs according to the submitted merge rule", "caller merge rule")
    require(protocol, "add semantic subtasks that were not supplied", "semantic scope prohibition")
    require(protocol, "worker completion as human/application acceptance", "worker acceptance prohibition")
    require(protocol, "Ptah manages the workers but does not invent the audit scope or issue the verdict", "worker example boundary")

    # Decision and work package.
    require(adr, "Status: proposed", "ADR-0036 proposed state")
    require(adr, "No new Core entity is required", "ADR frozen primitive boundary")
    require(adr, "apply `worker capacity = max(20, human-equivalent workers × 10)`", "ADR worker equation")
    require(adr, "caller-submitted job and caller-selected Recipe or Plan", "ADR caller job boundary")
    require(adr, "invent semantic subtasks", "ADR semantic scope prohibition")
    require(adr, "treat worker completion as caller acceptance", "ADR result acceptance prohibition")
    require(adr, "approve, purchase, install or activate its own upgrade", "ADR autonomous-upgrade prohibition")
    require(adr, "Sergeant patterns borrowed", "ADR Sergeant borrowing scope")

    require(work_package, "Status: candidate under review", "Phase 0C-18 candidate state")
    require(work_package, "diagnose platform condition without deciding caller work", "owner diagnostic direction")
    require(work_package, "borrow ten-for-two workers", "owner worker direction")
    require(work_package, "A02 — health, capability, compatibility and worker-capacity gap detection", "A02 placement")
    require(work_package, "A04 — caller-defined worker Plan execution", "A04 placement")
    require(work_package, "A06 — durable worker formation state", "A06 placement")
    require(work_package, "A14 — human-visible advisory, formation progress", "A14 placement")
    require(work_package, "A15 — proof that no autonomous upgrade, task selection or result acceptance exists", "A15 placement")

    # Master Plan and roadmap integration.
    require(master_plan, "Ptah may diagnose its own platform condition without choosing the caller's work", "Master Plan diagnostic principle")
    require(master_plan, "Caller-given work may use bounded worker formations", "Master Plan worker principle")
    require(master_plan, "caller-defined worker formation scheduling", "Master Plan Core worker composition")
    require(master_plan, "evidence-backed diagnostic advisory Views and Artifacts", "Master Plan diagnostic composition")
    require(master_plan, "worker formation, checkpoint, conflict and partial-result status", "Master Plan human worker surface")
    require(master_plan, "autonomous semantic job decomposition or result acceptance", "Master Plan worker non-goal")
    require(master_plan, "### Diagnostic advisory", "Master Plan diagnostic projection")
    require(master_plan, "### Worker formation", "Master Plan worker projection")
    require(master_plan, "It is not a new Core authority entity", "Master Plan authority boundary")
    require(master_plan, "it may not invent the job, add semantic scope or accept the result", "Master Plan worker authority boundary")
    require(master_plan, "failed worker Attempts remain distinct", "Master Plan worker reliability")
    require(master_plan, "worker completion does not equal caller acceptance", "Master Plan result boundary")
    require(master_plan, "Ptah may request an upgrade from exact diagnostic evidence", "Master Plan upgrade request")
    require(master_plan, "may not approve, purchase, install or activate it", "Master Plan upgrade approval boundary")

    require(roadmap, "bounded missing-capability and degradation advisory generation", "Roadmap A02")
    require(roadmap, "caller-defined Recipe/Plan worker formation execution", "Roadmap A04 worker execution")
    require(roadmap, "two-human-equivalent ten-for-two Recipe creates twenty bounded worker slots", "Roadmap A04 capacity proof")
    require(roadmap, "configured independent-check lanes cannot silently collapse", "Roadmap worker independence proof")
    require(roadmap, "worker completion cannot become result acceptance", "Roadmap worker acceptance proof")
    require(roadmap, "worker formation, role, checkpoint and partial-result recovery projection", "Roadmap A06")
    require(roadmap, "platform diagnostic advisory and missing-capability panel", "Roadmap A14 diagnostic surface")
    require(roadmap, "worker formation, role, checkpoint, conflict and partial-result panel", "Roadmap A14 worker surface")
    require(roadmap, "no advisory can approve or execute its own recommendation", "Roadmap A14 proof")
    require(roadmap, "ten-for-two formation tests prove bounded workers", "Roadmap A15 worker proof")
    require(roadmap, "Ptah cannot choose caller work or autonomously install an upgrade", "Roadmap A15 authority proof")
    require(roadmap, "worker formation role, independence, checkpoint, retry, conflict and partial-result evidence", "Roadmap X3")

    # Durable control-book candidate state.
    require(decisions, "### ADR-0036 — Platform diagnostic advisory and efficient worker execution boundary", "decision index")
    require(decisions, "**PROPOSED.**", "decision proposed state")
    require(current, "## Phase 0C-18 diagnostic and efficient-worker candidate", "current-state candidate section")
    require(current, "max(20, human-equivalent workers × 10)", "current worker equation")
    require(current, "does not start AF03", "current AF03 boundary")
    require(progress, "## Diagnostic advisory and efficient worker candidate", "progress candidate section")
    require(progress, "spread a caller-given job across bounded workers", "progress owner worker direction")
    require(progress, "implementation remains unauthorized", "progress runtime boundary")
    require(handoff, "## Diagnostic advisory and efficient worker candidate", "handoff candidate section")
    require(handoff, "caller-submitted job and Recipe/Plan", "handoff worker boundary")
    require(handoff, "AF03 remains READY / NOT STARTED", "handoff AF03 boundary")

    # Machine-readable authority.
    if index.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise ValidationError("P01 active work unit drifted")
    if index.get("runtime_implementation_authorized") is not False:
        raise ValidationError("master index authorized runtime")
    if str(PROTOCOL) not in index.get("recovery_order", []):
        raise ValidationError("protocol missing from recovery order")
    clarification = index.get("product_clarifications", {}).get("platform_diagnostic_and_worker_execution")
    if not isinstance(clarification, dict):
        raise ValidationError("platform diagnostic/worker clarification missing from machine index")
    expected = {
        "status": "candidate_under_review",
        "protocol": str(PROTOCOL),
        "decision": str(ADR),
        "work_package": str(WORK_PACKAGE),
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
    for key, value in expected.items():
        if clarification.get(key) != value:
            raise ValidationError(f"diagnostic/worker machine-index mismatch: {key}")

    # Unchanged gates.
    require(donor, "**Status:** COMPLETE AND FROZEN", "Phase 0A frozen")
    reject(donor, "**Status:** REOPENED", "Phase 0A reopened")
    require(campaign, "## AF03", "AF03 campaign section")
    af03 = campaign.split("## AF03", 1)[1].split("## AF04", 1)[0]
    require(af03, "- status: READY / NOT STARTED", "AF03 not-started state")
    reject(af03, "- status: ACTIVE", "AF03 activation")
    require(adr0033, "Status: proposed", "ADR-0033 proposed state")
    if re.search(r"^Status:\s+accepted", adr0033, re.MULTILINE | re.IGNORECASE):
        raise ValidationError("ADR-0033 became accepted")
    require(current, "**Runtime implementation:** NOT AUTHORIZED", "runtime non-authorization")
    reject(current, "**Runtime implementation:** AUTHORIZED", "runtime authorization")

    return {
        "schema_version": "1.0.0",
        "record_type": "ptah.phase0c.platform_diagnostic_and_worker_execution_validation",
        "status": "candidate_valid_non_authorizing",
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
        "sergeant_review_authority_borrowed": False,
        "sergeant_mission_selection_borrowed": False,
        "af03_started": False,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = validate_repo(Path(args.repo_root).resolve())
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
