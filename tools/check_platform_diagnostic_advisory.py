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
CAMPAIGN_STATE = Path("archive/campaign-001/OPERATIVE-STATE.json")
ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")
CANDIDATE_HEAD = "d2608ba7c619c1c402091edd619a4b29813ee9a7"
CANDIDATE_RUN = "29986975197"
CANDIDATE_ARTIFACT = "8555395796"
CANDIDATE_ARTIFACT_DIGEST = "sha256:72025fb0aa5a969ea73abe95d7352f7cf14f1c847943955bd768a46d964a4c61"
CANDIDATE_REPORT_SHA256 = "aff3a635d37b82c15eeb36f2f6cec780f76e2c3ce320727a18053b913b8d9171"
CANDIDATE_MERGE = "fbc4ee80284a2d7ea38a44fdbfa90f0348b875ae"
ACCEPTANCE_RECORD = "planning/PTAH-DIAGNOSTIC-WORKER-AUTHORITY-ACCEPTANCE.md"

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
    CAMPAIGN_STATE,
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
    campaign_state = json.loads(texts[CAMPAIGN_STATE])
    adr0033 = texts[ADR0033]
    index = json.loads(texts[MASTER_INDEX])

    # Candidate and neutral authority boundary.
    require(protocol, "Status: accepted product clarification", "protocol accepted state")
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
    require(protocol, "Installation acknowledgement does not equal resolution", "post-condition boundary")
    require(protocol, "Ptah does not decide which option the caller should choose", "example caller-choice boundary")

    # Ten-for-two worker execution boundary.
    require(protocol, "## 3. Sergeant patterns borrowed", "Sergeant patterns section")
    require(protocol, "### 3.2 Ten-for-two worker execution pattern", "worker pattern section")
    require(protocol, "worker capacity = max(20, human-equivalent workers × 10)", "worker capacity equation")
    require(protocol, "The ordinary two-human-equivalent formation therefore exposes twenty bounded worker slots.", "two-worker formation capacity")
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
    require(adr, "Status: accepted", "ADR-0036 accepted state")
    require(adr, "No new Core entity is required", "ADR frozen primitive boundary")
    require(adr, "apply `worker capacity = max(20, human-equivalent workers × 10)`", "ADR worker equation")
    require(adr, "caller-submitted job and caller-selected Recipe or Plan", "ADR caller job boundary")
    require(adr, "invent semantic subtasks", "ADR semantic scope prohibition")
    require(adr, "treat worker completion as caller acceptance", "ADR result acceptance prohibition")
    require(adr, "approve, purchase, install or activate its own upgrade", "ADR autonomous-upgrade prohibition")
    require(adr, "Sergeant patterns borrowed", "ADR Sergeant borrowing scope")

    require(work_package, "Status: accepted and complete", "Phase 0C-18 accepted state")
    require(work_package, "Ptah does not decide the work given", "owner diagnostic direction")
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
    require(decisions, "### D-052 — Ptah may diagnose its platform and efficiently execute caller-given worker formations", "accepted decision index")
    require(decisions, "**ACCEPTED.**", "decision accepted state")
    require(current, "## Accepted Phase 0C-18 diagnostic and efficient-worker boundary", "current-state accepted section")
    require(current, "max(20, human-equivalent workers × 10)", "current worker equation")
    require(current, "does not start AF03", "historical current AF03 boundary")
    require(progress, "## Diagnostic advisory and efficient worker boundary — accepted", "progress accepted section")
    require(progress, "spread a caller-given job across bounded workers", "progress owner worker direction")
    require(progress, "implementation remains unauthorized", "progress runtime boundary")
    require(handoff, "## Accepted diagnostic advisory and efficient worker boundary", "handoff accepted section")
    require(handoff, "caller-submitted job and Recipe/Plan", "handoff worker boundary")
    require(handoff, "Campaign 001: ACCEPTED COMPLETE", "handoff campaign accepted state")
    require(handoff, "AF01–AF10: ACCEPTED COMPLETE", "handoff ten-formation state")

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
        "status": "accepted_operational_clarification",
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
        "protocol_version": "1.0.0",
        "adr_0036_accepted": True,
        "phase0c_18_complete": True,
        "candidate_exact_head": CANDIDATE_HEAD,
        "candidate_workflow_run": CANDIDATE_RUN,
        "candidate_artifact_id": CANDIDATE_ARTIFACT,
        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
        "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,
        "candidate_merge": CANDIDATE_MERGE,
        "acceptance_record": ACCEPTANCE_RECORD,
    }
    for key, value in expected.items():
        if clarification.get(key) != value:
            raise ValidationError(f"diagnostic/worker machine-index mismatch: {key}")

    # Unchanged authority gates plus the now-operative archive campaign.
    require(donor, "**Status:** COMPLETE AND FROZEN", "Phase 0A frozen")
    reject(donor, "**Status:** REOPENED", "Phase 0A reopened")
    require(campaign, "## AF03", "AF03 campaign section")
    af03 = campaign.split("## AF03", 1)[1].split("## AF04", 1)[0]
    require(af03, "- status: ACCEPTED COMPLETE", "AF03 accepted state")
    reject(af03, "- status: ACTIVE", "AF03 activation")
    af04 = campaign.split("## AF04", 1)[1].split("## AF05", 1)[0]
    require(af04, "- status: ACCEPTED COMPLETE", "AF04 accepted state")
    reject(af04, "- status: READY / NOT STARTED", "AF04 acceptance reversion")
    reject(af04, "- status: ACTIVE", "AF04 incomplete activation")
    if campaign_state.get("status") != "accepted_complete_non_authorizing":
        raise ValidationError("Campaign 001 operative status drifted")
    expected_campaign = {
        "formation_count": 10,
        "completed_formation_count": 10,
        "obligation_count": 98,
        "accepted_archive_record_count": 91,
        "blocked_completed_outcome_count": 7,
        "remaining_evidence_count": 0,
        "p01_closed": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
    }
    for key, value in expected_campaign.items():
        if campaign_state.get(key) != value:
            raise ValidationError(f"Campaign 001 operative-state mismatch: {key}")
    require(adr0033, "Status: proposed", "ADR-0033 proposed state")
    if re.search(r"^Status:\s+accepted", adr0033, re.MULTILINE | re.IGNORECASE):
        raise ValidationError("ADR-0033 became accepted")
    require(current, "**Runtime implementation:** NOT AUTHORIZED", "runtime non-authorization")
    reject(current, "**Runtime implementation:** AUTHORIZED", "runtime authorization")

    return {
        "schema_version": "1.0.0",
        "record_type": "ptah.phase0c.platform_diagnostic_and_worker_execution_validation",
        "status": "accepted_valid_non_authorizing",
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
        "af03_accepted": True,
        "af03_started": True,
        "af03_authorized": True,
        "af04_accepted": True,
        "af04_ready": False,
        "af04_started": True,
        "af04_authorized": True,
        "archive_campaign_complete": True,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "protocol_version": "1.0.0",
        "adr_0036_accepted": True,
        "phase0c_18_complete": True,
        "candidate_exact_head": CANDIDATE_HEAD,
        "candidate_workflow_run": CANDIDATE_RUN,
        "candidate_artifact_id": CANDIDATE_ARTIFACT,
        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
        "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,
        "candidate_merge": CANDIDATE_MERGE,
        "acceptance_record": ACCEPTANCE_RECORD,
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
