#!/usr/bin/env python3
"""Record AF03 candidate preparation without promoting operative campaign state."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSION = "archive/campaign-001/af03/MISSION.md"
RESULT = "archive/campaign-001/af03/RESULT.json"
SERGEANT = "archive/campaign-001/af03/SERGEANT-REVIEW.md"
SERGEANT_TARGET = "a6a1d9aa13f619c2f8ff4c1c6c0cadea331df3d6"


class SyncError(RuntimeError):
    pass


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one source fragment, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def sync_manifest() -> None:
    path = ROOT / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md"
    replace_once(
        path,
        "- next formation: AF03 READY / NOT STARTED\n",
        "- next formation: AF03 READY / NOT STARTED\n- AF03 candidate package: COMPLETE / SERGEANT PASSED / NOT ACCEPTED\n- AF03 candidate outcomes: 10\n- AF03 candidate remaining evidence: 0\n",
        "manifest campaign candidate",
    )
    replace_once(
        path,
        "- status: READY / NOT STARTED\n- private count: 20\n- assigned records: 10\n- reserve pairs: 0\n",
        f"- status: READY / NOT STARTED\n- candidate package: COMPLETE / SERGEANT PASSED / NOT ACCEPTED\n- candidate outcomes: 10\n- candidate remaining evidence: 0\n- candidate mission: `{MISSION}`\n- candidate result: `{RESULT}`\n- Sergeant review: `{SERGEANT}`\n- private count: 20\n- assigned records: 10\n- reserve pairs: 0\n",
        "manifest AF03 candidate",
    )


def sync_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    replace_once(
        path,
        "- AF03: READY / NOT STARTED;\n- AF02 mission: `archive/campaign-001/af02/MISSION.md`;",
        f"- AF03 operative status: READY / NOT STARTED;\n- AF03 candidate package: COMPLETE / SERGEANT PASSED / NOT ACCEPTED;\n- AF03 candidate outcomes: 10;\n- AF03 candidate remaining evidence: 0;\n- AF03 Sergeant target: `{SERGEANT_TARGET}`;\n- AF03 mission/result/review: `{MISSION}`, `{RESULT}`, `{SERGEANT}`;\n- AF02 mission: `archive/campaign-001/af02/MISSION.md`;",
        "current state AF03 candidate",
    )
    replace_once(
        path,
        "AF02 is accepted complete. AF03 remains ready but not started. Archive formation state does not grant source reuse, replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation.",
        "AF02 is accepted complete. AF03 remains operatively ready but not started; its candidate evidence package is complete, Sergeant-reviewed and not accepted. Candidate preparation does not grant source reuse, replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation.",
        "current state AF03 summary",
    )


def sync_progress() -> None:
    path = ROOT / "PROGRESS.md"
    replace_once(
        path,
        "- [ ] AF03 is READY / NOT STARTED; no AF03 source record is pre-ticked as archived.",
        "- [x] AF03 candidate evidence prepared: ten paired records, ten bounded candidate outcomes, zero remaining evidence and independent Sergeant PASS WITH MANDATORY RETAINED RESTRICTIONS; operative AF03 remains READY / NOT STARTED and no record is accepted yet.",
        "progress archive AF03",
    )
    replace_once(
        path,
        "- [ ] AF03 remains READY / NOT STARTED.",
        "- [x] AF03 candidate package uses the accepted ten-for-two execution boundary and Sergeant review; operative AF03 remains READY / NOT STARTED pending exact-head closure and separate acceptance.",
        "progress diagnostic AF03",
    )


def sync_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    replace_once(
        path,
        "AF03: READY / NOT STARTED\n```",
        "AF03 operative status: READY / NOT STARTED\nAF03 candidate package: COMPLETE / SERGEANT PASSED / NOT ACCEPTED\n```",
        "handoff archive status",
    )
    replace_once(
        path,
        "AF02 is accepted complete with ten accepted archive records and zero blocks. Evidence: exact head `b710574b99269647cdd9029db5a2b217642aa344`, run `29875542752`, artifact `8512821506`, candidate merge `58d89dfd1d5348cc8423222e3aff256ee041dce2`, acceptance record `archive/campaign-001/af02/ACCEPTANCE.md`. AF03 is READY / NOT STARTED.",
        f"AF02 is accepted complete with ten accepted archive records and zero blocks. Evidence: exact head `b710574b99269647cdd9029db5a2b217642aa344`, run `29875542752`, artifact `8512821506`, candidate merge `58d89dfd1d5348cc8423222e3aff256ee041dce2`, acceptance record `archive/campaign-001/af02/ACCEPTANCE.md`. AF03 remains operatively READY / NOT STARTED, but its candidate package is complete with ten paired outcomes and independent Sergeant result `pass_with_mandatory_retained_restrictions`. Read `{MISSION}`, `{RESULT}` and `{SERGEANT}`. No AF03 record is accepted yet.",
        "handoff AF03 candidate detail",
    )
    replace_once(
        path,
        "AF03 remains READY / NOT STARTED.\n\n\n## Accepted diagnostic advisory",
        "AF03 remains READY / NOT STARTED; its candidate package is complete but unaccepted.\n\n\n## Accepted diagnostic advisory",
        "handoff neutral boundary AF03",
    )
    replace_once(
        path,
        "AF03 remains READY / NOT STARTED.\n\n## Exact next action",
        "AF03 remains READY / NOT STARTED; candidate evidence and Sergeant review are complete, pending exact-head closure and separate acceptance.\n\n## Exact next action",
        "handoff diagnostic boundary AF03",
    )


def sync_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    archive = data["operational_protocols"]["tenfold_archive_formation"]
    if archive.get("af03_status") != "ready_not_started" or archive.get("af03_started") is not False:
        raise SyncError("operative AF03 state drifted before candidate sync")
    if archive.get("accepted_archive_record_count") != 19 or archive.get("completed_formation_count") != 2:
        raise SyncError("operative archive totals drifted")
    archive.update(
        {
            "af03_candidate_package_status": "complete_sergeant_passed_not_accepted",
            "af03_candidate_outcome_count": 10,
            "af03_candidate_remaining_evidence_count": 0,
            "af03_candidate_mission": MISSION,
            "af03_candidate_result": RESULT,
            "af03_sergeant_review": SERGEANT,
            "af03_sergeant_review_target_head": SERGEANT_TARGET,
            "af03_sergeant_review_result": "pass_with_mandatory_retained_restrictions",
            "af03_sergeant_blocking_finding_count": 0,
            "af04_status": "not_started",
            "af04_started": False,
            "af04_authorized": False,
        }
    )
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    sync_manifest()
    sync_current_state()
    sync_progress()
    sync_handoff()
    sync_index()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    donor = (ROOT / "DONOR_RECOVERY.md").read_text(encoding="utf-8")
    adr0033 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current or "**Runtime implementation:** AUTHORIZED" in current:
        raise SyncError("runtime boundary failed")
    if "**Status:** COMPLETE AND FROZEN" not in donor:
        raise SyncError("Phase 0A is not frozen")
    if "Status: proposed" not in adr0033:
        raise SyncError("ADR-0033 is not proposed")

    print("AF03 candidate recovery state synchronized without operative promotion")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
