#!/usr/bin/env python3
"""Promote the exact reviewed AF03 candidate into accepted campaign state."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_HEAD = "4916f79ff3a0cbac8ee4ae53f9ac09a0065d7b7d"
CANDIDATE_RUN = "30003085272"
CANDIDATE_ARTIFACT = "8561809711"
CANDIDATE_ARTIFACT_DIGEST = "sha256:fa36506e788958d4b3d134f6f1286e4c2d47d309aa15529e6f1d384c9bdcd6a6"
CANDIDATE_REPORT_SHA256 = "e437e8785a846710e2e2434fb3e537a3566fc6baf68b420da6610dd20571f302"
CANDIDATE_MERGE = "d86218e1127c57bacfb4d88eff15b81d326995ba"
ACCEPTANCE = "archive/campaign-001/af03/ACCEPTANCE.md"


class SyncError(RuntimeError):
    pass


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one source fragment, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def replace_all(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count == 0:
        raise SyncError(f"{label}: source fragment missing")
    path.write_text(text.replace(old, new), encoding="utf-8")


def sync_acceptance_record() -> None:
    path = ROOT / ACCEPTANCE
    replace_once(
        path,
        "Status: ACCEPTANCE CANDIDATE — exact accepted-state proof pending",
        "Status: ACCEPTED EVIDENCE RECORD — operative merge binding pending",
        "acceptance record state",
    )
    replace_once(
        path,
        "This record becomes an accepted evidence record only after exact-head accepted-state validation and reviewed merge.",
        "This record accepts the reviewed AF03 candidate subject to permanent exact-head accepted-state proof. The operative merge is bound in a later recovery-only update.",
        "acceptance record effect",
    )


def sync_mission() -> None:
    path = ROOT / "archive/campaign-001/af03/MISSION.md"
    replace_once(
        path,
        "Status: CANDIDATE EVIDENCE COMPLETE — SERGEANT PASSED — PENDING EXACT-HEAD REVIEW",
        "Status: ACCEPTED COMPLETE",
        "mission accepted state",
    )
    replace_once(
        path,
        "AF03 candidate evidence and independent review are complete but AF03 is not accepted. AF04 remains NOT STARTED. P01 remains the active implementation-authorization work outside this archive campaign.",
        f"AF03 is accepted complete from candidate head `{CANDIDATE_HEAD}`, run `{CANDIDATE_RUN}`, artifact `{CANDIDATE_ARTIFACT}` and candidate merge `{CANDIDATE_MERGE}`. AF04 is READY / NOT STARTED. P01 remains the active implementation-authorization work outside this archive campaign.",
        "mission accepted conclusion",
    )


def sync_result_json() -> None:
    path = ROOT / "archive/campaign-001/af03/RESULT.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "candidate_complete_pending_exact_head_review":
        raise SyncError("AF03 result is not the reviewed candidate")
    data.update(
        {
            "status": "accepted_complete_non_authorizing",
            "candidate_exact_head": CANDIDATE_HEAD,
            "candidate_workflow_run": CANDIDATE_RUN,
            "candidate_artifact_id": CANDIDATE_ARTIFACT,
            "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
            "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,
            "candidate_merge": CANDIDATE_MERGE,
            "acceptance_record": ACCEPTANCE,
            "af03_accepted": True,
            "af04_status": "ready_not_started",
            "af04_started": False,
            "af04_authorized": False,
        }
    )
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def sync_result_md() -> None:
    path = ROOT / "archive/campaign-001/af03/RESULT.md"
    replace_once(
        path,
        "Status: CANDIDATE EVIDENCE COMPLETE — SERGEANT PASSED — PENDING EXACT-HEAD REVIEW",
        "Status: ACCEPTED COMPLETE",
        "human result accepted state",
    )
    replace_once(
        path,
        "Sergeant's pass also does not accept AF03. Exact-head closure validation and a separate owner/calling-authority promotion change remain required.",
        f"Sergeant's pass remained independent evidence. AF03 was accepted separately from exact candidate head `{CANDIDATE_HEAD}`, workflow run `{CANDIDATE_RUN}`, artifact `{CANDIDATE_ARTIFACT}` and candidate merge `{CANDIDATE_MERGE}`.",
        "human result accepted effect",
    )
    replace_once(path, "- AF04 remains not started.", "- AF04 is ready but not started.", "human result AF04 state")


def sync_manifest() -> None:
    path = ROOT / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md"
    replace_once(path, "- completed formations: 2", "- completed formations: 3", "manifest completed formations")
    replace_once(path, "- accepted archive records: 19", "- accepted archive records: 29", "manifest accepted total")
    replace_once(
        path,
        "- next formation: AF03 READY / NOT STARTED\n- AF03 candidate package: COMPLETE / SERGEANT PASSED / NOT ACCEPTED\n- AF03 candidate outcomes: 10\n- AF03 candidate remaining evidence: 0",
        "- next formation: AF04 READY / NOT STARTED",
        "manifest next formation",
    )
    replace_once(
        path,
        "- status: READY / NOT STARTED\n- candidate package: COMPLETE / SERGEANT PASSED / NOT ACCEPTED\n- candidate outcomes: 10\n- candidate remaining evidence: 0\n- candidate mission: `archive/campaign-001/af03/MISSION.md`\n- candidate result: `archive/campaign-001/af03/RESULT.json`\n- Sergeant review: `archive/campaign-001/af03/SERGEANT-REVIEW.md`\n- private count: 20\n- assigned records: 10\n- reserve pairs: 0",
        "- status: ACCEPTED COMPLETE\n- private count: 20\n- assigned records: 10\n- accepted archive records: 10\n- blocked completed outcomes: 0\n- remaining evidence: 0\n- result: `archive/campaign-001/af03/RESULT.json`\n- Sergeant review: `archive/campaign-001/af03/SERGEANT-REVIEW.md`\n- acceptance: `archive/campaign-001/af03/ACCEPTANCE.md`\n- reserve pairs: 0",
        "manifest AF03 acceptance",
    )
    replace_once(
        path,
        "## AF04\n\n- private count: 20",
        "## AF04\n\n- status: READY / NOT STARTED\n- private count: 20",
        "manifest AF04 ready",
    )


def sync_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    replace_once(path, "- accepted archive records: 19 total;", "- accepted archive records: 29 total;", "current accepted total")
    old = """- AF03: READY / NOT STARTED;
- AF03 candidate package: COMPLETE / SERGEANT PASSED / NOT ACCEPTED;
- AF03 candidate outcomes: 10;
- AF03 candidate remaining evidence: 0;
- AF03 Sergeant target: `a6a1d9aa13f619c2f8ff4c1c6c0cadea331df3d6`;
- AF03 mission/result/review: `archive/campaign-001/af03/MISSION.md`, `archive/campaign-001/af03/RESULT.json`, `archive/campaign-001/af03/SERGEANT-REVIEW.md`;
"""
    new = f"""- AF03: ACCEPTED COMPLETE;
- AF03 accepted archive records: 10;
- AF03 blocked outcomes: 0;
- AF03 remaining evidence: 0;
- AF03 candidate exact head/run/artifact: `{CANDIDATE_HEAD}` / `{CANDIDATE_RUN}` / `{CANDIDATE_ARTIFACT}`;
- AF03 candidate merge: `{CANDIDATE_MERGE}`;
- AF03 mission/result/review/acceptance: `archive/campaign-001/af03/MISSION.md`, `archive/campaign-001/af03/RESULT.json`, `archive/campaign-001/af03/SERGEANT-REVIEW.md`, `{ACCEPTANCE}`;
- AF04: READY / NOT STARTED;
"""
    replace_once(path, old, new, "current AF03 acceptance")
    replace_once(
        path,
        "AF02 is accepted complete. AF03 remains ready but not started; its candidate evidence package is complete, Sergeant-reviewed and not accepted. Candidate preparation does not grant source reuse, replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation.",
        "AF01, AF02 and AF03 are accepted complete. AF04 remains ready but not started. Archive acceptance does not grant unrestricted source reuse, replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation.",
        "current archive summary",
    )


def sync_progress() -> None:
    path = ROOT / "PROGRESS.md"
    replace_once(
        path,
        "- [x] AF03 is READY / NOT STARTED operatively; candidate evidence is prepared with ten paired records, ten bounded candidate outcomes, zero remaining evidence and independent Sergeant PASS WITH MANDATORY RETAINED RESTRICTIONS; no record is accepted yet.",
        f"- [x] AF03 accepted complete: ten paired records, ten accepted archive outcomes, zero blocks, independent Sergeant PASS WITH MANDATORY RETAINED RESTRICTIONS, candidate merge `{CANDIDATE_MERGE}`.\n- [ ] AF04 is READY / NOT STARTED; no AF04 source record is pre-accepted.",
        "progress AF03 acceptance",
    )
    replace_once(
        path,
        "- [x] AF03 candidate package uses the accepted ten-for-two execution boundary and Sergeant review; operative AF03 remains READY / NOT STARTED pending exact-head closure and separate acceptance.",
        "- [x] AF03 used the accepted ten-for-two execution boundary and independent Sergeant review, then was accepted separately; AF04 remains READY / NOT STARTED.",
        "progress diagnostic follow-on",
    )


def sync_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    replace_once(
        path,
        "AF03: READY / NOT STARTED\nAF03 candidate package: COMPLETE / SERGEANT PASSED / NOT ACCEPTED",
        "AF03: ACCEPTED COMPLETE\nAF04: READY / NOT STARTED",
        "handoff archive state",
    )
    replace_once(
        path,
        "AF02 is accepted complete with ten accepted archive records and zero blocks. Evidence: exact head `b710574b99269647cdd9029db5a2b217642aa344`, run `29875542752`, artifact `8512821506`, candidate merge `58d89dfd1d5348cc8423222e3aff256ee041dce2`, acceptance record `archive/campaign-001/af02/ACCEPTANCE.md`. AF03 remains operatively READY / NOT STARTED, but its candidate package is complete with ten paired outcomes and independent Sergeant result `pass_with_mandatory_retained_restrictions`. Read `archive/campaign-001/af03/MISSION.md`, `archive/campaign-001/af03/RESULT.json` and `archive/campaign-001/af03/SERGEANT-REVIEW.md`. No AF03 record is accepted yet.",
        f"AF02 is accepted complete with ten accepted archive records and zero blocks. AF03 is also accepted complete with ten accepted archive records and zero blocks. AF03 evidence: exact head `{CANDIDATE_HEAD}`, run `{CANDIDATE_RUN}`, artifact `{CANDIDATE_ARTIFACT}`, candidate merge `{CANDIDATE_MERGE}`, independent Sergeant result `pass_with_mandatory_retained_restrictions`, acceptance record `{ACCEPTANCE}`. AF04 is READY / NOT STARTED.",
        "handoff AF03 detail",
    )
    replace_all(path, "AF03 remains READY / NOT STARTED; its candidate package is complete but unaccepted.", "AF03 is ACCEPTED COMPLETE; AF04 is READY / NOT STARTED.", "handoff candidate summary")
    replace_all(path, "AF03 remains READY / NOT STARTED; candidate evidence and Sergeant review are complete, pending exact-head closure and separate acceptance.", "AF03 is ACCEPTED COMPLETE; AF04 is READY / NOT STARTED.", "handoff diagnostic summary")


def sync_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    archive = data["operational_protocols"]["tenfold_archive_formation"]
    if archive.get("accepted_archive_record_count") != 19 or archive.get("completed_formation_count") != 2:
        raise SyncError("pre-acceptance campaign totals drifted")
    archive.update(
        {
            "status": "accepted_operational_protocol_af03_complete_af04_ready",
            "accepted_archive_record_count": 29,
            "blocked_archive_record_count": 1,
            "completed_formation_count": 3,
            "af03_status": "accepted_complete",
            "af03_started": True,
            "af03_authorized": True,
            "af03_accepted_archive_record_count": 10,
            "af03_blocked_record_count": 0,
            "af03_remaining_evidence_count": 0,
            "af03_candidate_exact_head": CANDIDATE_HEAD,
            "af03_candidate_workflow_run": CANDIDATE_RUN,
            "af03_candidate_artifact_id": CANDIDATE_ARTIFACT,
            "af03_candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
            "af03_candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,
            "af03_candidate_merge": CANDIDATE_MERGE,
            "af03_acceptance_record": ACCEPTANCE,
            "af03_sergeant_review_result": "pass_with_mandatory_retained_restrictions",
            "af03_sergeant_blocking_finding_count": 0,
            "af04_status": "ready_not_started",
            "af04_started": False,
            "af04_authorized": False,
        }
    )
    for obsolete in (
        "af03_candidate_package_status",
        "af03_candidate_outcome_count",
        "af03_candidate_remaining_evidence_count",
        "af03_candidate_mission",
        "af03_candidate_result",
        "af03_sergeant_review",
        "af03_sergeant_review_target_head",
    ):
        archive.pop(obsolete, None)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def sync_af03_validator() -> None:
    path = ROOT / "tools/check_archive_af03.py"
    replace_once(path, 'SERGEANT_REVIEW = Path("archive/campaign-001/af03/SERGEANT-REVIEW.md")', 'SERGEANT_REVIEW = Path("archive/campaign-001/af03/SERGEANT-REVIEW.md")\nACCEPTANCE = Path("archive/campaign-001/af03/ACCEPTANCE.md")', "AF03 acceptance constant")
    replace_once(path, 'BASE_AUTHORITY = "a7186bfb45cb885c8afc7165f67641e8725cc989"', f'BASE_AUTHORITY = "a7186bfb45cb885c8afc7165f67641e8725cc989"\nCANDIDATE_HEAD = "{CANDIDATE_HEAD}"\nCANDIDATE_RUN = "{CANDIDATE_RUN}"\nCANDIDATE_ARTIFACT = "{CANDIDATE_ARTIFACT}"\nCANDIDATE_ARTIFACT_DIGEST = "{CANDIDATE_ARTIFACT_DIGEST}"\nCANDIDATE_REPORT_SHA256 = "{CANDIDATE_REPORT_SHA256}"\nCANDIDATE_MERGE = "{CANDIDATE_MERGE}"', "AF03 candidate constants")
    replace_once(path, 'sergeant = read(root, SERGEANT_REVIEW)\n    result =', 'sergeant = read(root, SERGEANT_REVIEW)\n    acceptance = read(root, ACCEPTANCE)\n    result =', "AF03 acceptance read")
    replace_once(path, 'require(mission, "CANDIDATE EVIDENCE COMPLETE — SERGEANT PASSED — PENDING EXACT-HEAD REVIEW", "mission candidate state")', 'require(mission, "Status: ACCEPTED COMPLETE", "mission accepted state")', "AF03 mission validator")
    replace_once(path, 'require(mission, "AF03 candidate evidence and independent review are complete but AF03 is not accepted", "mission non-acceptance")', 'require(mission, "AF03 is accepted complete", "mission acceptance")', "AF03 mission acceptance")
    replace_once(path, 'require(result_md, "SERGEANT PASSED — PENDING EXACT-HEAD REVIEW", "human result state")', 'require(result_md, "Status: ACCEPTED COMPLETE", "human result state")', "AF03 human state")
    replace_once(path, 'require(result_md, "Sergeant\'s pass also does not accept AF03", "human result non-acceptance")', 'require(result_md, "AF03 was accepted separately", "human result acceptance")', "AF03 human acceptance")
    insert = f'''    require(acceptance, "Status: ACCEPTED EVIDENCE RECORD", "acceptance record state")
    require(acceptance, CANDIDATE_HEAD, "acceptance candidate head")
    require(acceptance, CANDIDATE_MERGE, "acceptance candidate merge")
    require(acceptance, "AF04 status: `READY / NOT STARTED`", "acceptance AF04 state")

'''
    replace_once(path, '    expected_top = {\n', insert + '    expected_top = {\n', "AF03 acceptance checks")
    replace_once(path, '"status": "candidate_complete_pending_exact_head_review",', '"status": "accepted_complete_non_authorizing",\n        "candidate_exact_head": CANDIDATE_HEAD,\n        "candidate_workflow_run": CANDIDATE_RUN,\n        "candidate_artifact_id": CANDIDATE_ARTIFACT,\n        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,\n        "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,\n        "candidate_merge": CANDIDATE_MERGE,\n        "acceptance_record": str(ACCEPTANCE),', "AF03 result accepted fields")
    replace_once(path, '"af04_authorized": False,', '"af03_accepted": True,\n        "af04_status": "ready_not_started",\n        "af04_started": False,\n        "af04_authorized": False,', "AF03 follow-on state")
    replace_once(path, '    # Candidate must not be promoted by its own evidence package.\n    if (root / "archive/campaign-001/af03/ACCEPTANCE.md").exists():\n        raise ValidationError("AF03 acceptance record exists in candidate package")\n', '    # Accepted package must retain its separate promotion record.\n    if not (root / ACCEPTANCE).is_file():\n        raise ValidationError("AF03 acceptance record is missing")\n', "AF03 acceptance presence")
    replace_once(path, 'reject(af04, "- status: ACTIVE", "AF04 activation")\n    reject(af04, "- status: ACCEPTED", "AF04 acceptance")', 'require(af04, "- status: READY / NOT STARTED", "AF04 ready state")\n    reject(af04, "- status: ACTIVE", "AF04 activation")\n    reject(af04, "- status: ACCEPTED", "AF04 acceptance")', "AF04 ready validator")
    replace_once(path, 'if archive.get("accepted_archive_record_count") != 19 or archive.get("completed_formation_count") != 2:\n        raise ValidationError("AF03 candidate prematurely changed operative campaign totals")', 'if archive.get("accepted_archive_record_count") != 29 or archive.get("completed_formation_count") != 3:\n        raise ValidationError("AF03 accepted campaign totals are invalid")\n    if archive.get("af03_status") != "accepted_complete" or archive.get("af03_started") is not True or archive.get("af03_authorized") is not True:\n        raise ValidationError("AF03 is not accepted in the machine index")\n    if archive.get("af04_status") != "ready_not_started" or archive.get("af04_started") is not False or archive.get("af04_authorized") is not False:\n        raise ValidationError("AF04 state is invalid")', "AF03 machine accepted totals")
    replace_once(path, '"status": "candidate_complete_valid_non_authorizing",', '"status": "accepted_complete_valid_non_authorizing",', "AF03 validation status")
    replace_once(path, '"candidate_archive_outcome_count": 10,', '"accepted_archive_record_count": 10,\n        "candidate_exact_head": CANDIDATE_HEAD,\n        "candidate_workflow_run": CANDIDATE_RUN,\n        "candidate_artifact_id": CANDIDATE_ARTIFACT,\n        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,\n        "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,\n        "candidate_merge": CANDIDATE_MERGE,\n        "acceptance_record": str(ACCEPTANCE),', "AF03 validation evidence")
    replace_once(path, '"af03_accepted": False,', '"af03_accepted": True,', "AF03 accepted flag")


def sync_af03_tests() -> None:
    path = ROOT / "tools/test_check_archive_af03.py"
    replace_once(path, '    ADR0033,\n', '    ACCEPTANCE,\n    ADR0033,\n', "AF03 test acceptance import")
    replace_once(path, '    SERGEANT_REVIEW,\n    MANIFEST,', '    SERGEANT_REVIEW,\n    ACCEPTANCE,\n    MANIFEST,', "AF03 test acceptance fixture")
    replace_once(path, 'self.assertEqual(result["status"], "candidate_complete_valid_non_authorizing")', 'self.assertEqual(result["status"], "accepted_complete_valid_non_authorizing")', "AF03 valid status test")
    replace_once(path, 'self.assertEqual(result["candidate_archive_outcome_count"], 10)', 'self.assertEqual(result["accepted_archive_record_count"], 10)', "AF03 accepted count test")
    replace_once(path, 'self.assertFalse(result["af03_accepted"])', 'self.assertTrue(result["af03_accepted"])', "AF03 accepted assertion")
    old = '''    def test_result_status_cannot_be_accepted(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "status", "accepted_complete")
        self.assert_invalid(root)
'''
    new = '''    def test_result_status_cannot_revert_to_candidate(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "status", "candidate_complete_pending_exact_head_review")
        self.assert_invalid(root)
'''
    replace_once(path, old, new, "AF03 status regression")
    old = '''    def test_acceptance_record_cannot_appear(self) -> None:
        root = self.make_repo()
        path = root / "archive/campaign-001/af03/ACCEPTANCE.md"
        path.write_text("# premature acceptance\\n", encoding="utf-8")
        self.assert_invalid(root)
'''
    new = '''    def test_acceptance_record_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / ACCEPTANCE).unlink()
        self.assert_invalid(root)
'''
    replace_once(path, old, new, "AF03 acceptance regression")
    replace_once(path, 'self.mutate_index(root, "accepted_archive_record_count", 29)', 'self.mutate_index(root, "accepted_archive_record_count", 19)', "AF03 operative total regression")


def sync_af02_validator() -> None:
    path = ROOT / "tools/check_archive_af02.py"
    replace_once(path, 'require(current_state, "AF03: READY / NOT STARTED", "current AF03 ready state")', 'require(current_state, "AF03: ACCEPTED COMPLETE", "current AF03 accepted state")\n    require(current_state, "AF04: READY / NOT STARTED", "current AF04 ready state")', "AF02 current follow-on")
    replace_once(path, 'if archive.get("completed_formation_count") != 2 or archive.get("accepted_archive_record_count") != 19:\n        raise ValidationError("campaign accepted totals are invalid")', 'if archive.get("completed_formation_count") != 3 or archive.get("accepted_archive_record_count") != 29:\n        raise ValidationError("campaign accepted totals are invalid")', "AF02 current totals")
    replace_once(path, 'if archive.get("af03_status") != "ready_not_started" or archive.get("af03_started") is not False or archive.get("af03_authorized") is not False:\n        raise ValidationError("AF03 started before AF02 closure")', 'if archive.get("af03_status") != "accepted_complete" or archive.get("af03_started") is not True or archive.get("af03_authorized") is not True:\n        raise ValidationError("AF03 follow-on acceptance is invalid")\n    if archive.get("af03_accepted_archive_record_count") != 10 or archive.get("af03_remaining_evidence_count") != 0:\n        raise ValidationError("AF03 accepted counts are invalid")\n    if archive.get("af04_status") != "ready_not_started" or archive.get("af04_started") is not False or archive.get("af04_authorized") is not False:\n        raise ValidationError("AF04 follow-on state is invalid")', "AF02 follow-on machine state")
    replace_once(path, '"af03_ready": True,\n        "af03_started": False,\n        "af03_authorized": False,', '"af03_accepted": True,\n        "af03_started": True,\n        "af03_authorized": True,\n        "af04_ready": True,\n        "af04_started": False,\n        "af04_authorized": False,', "AF02 return follow-on")


def sync_af02_tests() -> None:
    path = ROOT / "tools/test_check_archive_af02.py"
    replace_once(path, 'self.assertTrue(result["af03_ready"])\n        self.assertFalse(result["af03_started"])\n        self.assertFalse(result["af03_authorized"])', 'self.assertTrue(result["af03_accepted"])\n        self.assertTrue(result["af03_started"])\n        self.assertTrue(result["af03_authorized"])\n        self.assertTrue(result["af04_ready"])\n        self.assertFalse(result["af04_started"])\n        self.assertFalse(result["af04_authorized"])', "AF02 valid follow-on assertions")
    replace_once(path, '    def test_af03_cannot_start(self) -> None:\n        root = self.make_repo()\n        self.mutate_index(root, lambda archive: archive.__setitem__("af03_started", True))\n        self.assert_invalid(root)', '    def test_af03_cannot_revert_to_unstarted(self) -> None:\n        root = self.make_repo()\n        self.mutate_index(root, lambda archive: archive.__setitem__("af03_started", False))\n        self.assert_invalid(root)', "AF02 AF03 progression regression")


def sync_af01_validator() -> None:
    path = ROOT / "tools/check_archive_af01.py"
    replace_once(path, 'require(acceptance, "AF03: READY / NOT STARTED", "AF03 subsequent ready state")', 'require(acceptance, "AF03: READY / NOT STARTED", "historical AF03 state at AF01 acceptance")', "AF01 historical acceptance wording")
    replace_once(path, 'require(manifest, "- status: READY / NOT STARTED", "manifest AF03 ready state")', 'require(manifest, "## AF03", "manifest AF03 section")\n    require(manifest, "- status: ACCEPTED COMPLETE", "manifest AF03 accepted state")\n    require(manifest, "## AF04", "manifest AF04 section")\n    require(manifest, "- status: READY / NOT STARTED", "manifest AF04 ready state")', "AF01 manifest follow-on")
    replace_once(path, 'require(current_state, "AF03: READY / NOT STARTED", "current AF03 ready state")', 'require(current_state, "AF03: ACCEPTED COMPLETE", "current AF03 accepted state")\n    require(current_state, "AF04: READY / NOT STARTED", "current AF04 ready state")', "AF01 current follow-on")


def sync_archive_validator() -> None:
    path = ROOT / "tools/check_archive_formation.py"
    replace_once(path, 'AF02_ACCEPTANCE = Path("archive/campaign-001/af02/ACCEPTANCE.md")', 'AF02_ACCEPTANCE = Path("archive/campaign-001/af02/ACCEPTANCE.md")\nAF03_ACCEPTANCE = Path("archive/campaign-001/af03/ACCEPTANCE.md")', "archive AF03 acceptance constant")
    replace_once(path, '    AF02_ACCEPTANCE,\n)', '    AF02_ACCEPTANCE,\n    AF03_ACCEPTANCE,\n)', "archive required AF03 acceptance")
    replace_once(path, 'af02_acceptance = texts[AF02_ACCEPTANCE]\n', 'af02_acceptance = texts[AF02_ACCEPTANCE]\n    af03_acceptance = texts[AF03_ACCEPTANCE]\n', "archive AF03 acceptance read")
    replace_once(path, 'require(progress, "AF03 is READY / NOT STARTED", "progress AF03 ready state")', 'require(progress, "AF03 accepted complete", "progress AF03 accepted state")\n    require(progress, "AF04 is READY / NOT STARTED", "progress AF04 ready state")', "archive progress follow-on")
    replace_once(path, 'require(current_state, "AF03: READY / NOT STARTED", "current AF03 ready state")', 'require(current_state, "AF03: ACCEPTED COMPLETE", "current AF03 accepted state")\n    require(current_state, "AF04: READY / NOT STARTED", "current AF04 ready state")', "archive current follow-on")
    replace_once(path, 'require(handoff, "AF03: READY / NOT STARTED", "handoff AF03 ready state")', 'require(handoff, "AF03: ACCEPTED COMPLETE", "handoff AF03 accepted state")\n    require(handoff, "AF04: READY / NOT STARTED", "handoff AF04 ready state")', "archive handoff follow-on")
    replace_once(path, 'require(af02_acceptance, "AF03: READY / NOT STARTED", "AF03 next state")', 'require(af02_acceptance, "AF03: READY / NOT STARTED", "historical AF03 state at AF02 acceptance")\n    require(af03_acceptance, "Status: ACCEPTED EVIDENCE RECORD", "AF03 acceptance state")\n    require(af03_acceptance, CANDIDATE_MERGE if False else "d86218e1127c57bacfb4d88eff15b81d326995ba", "AF03 candidate merge")\n    require(af03_acceptance, "AF04 status: `READY / NOT STARTED`", "AF04 next state")', "archive AF03 acceptance checks")
    replace_once(path, '"status": "accepted_operational_protocol_af02_complete_af03_ready",', '"status": "accepted_operational_protocol_af03_complete_af04_ready",', "archive index status")
    replace_once(path, '"accepted_archive_record_count": 19,', '"accepted_archive_record_count": 29,', "archive index accepted total")
    replace_once(path, '"completed_formation_count": 2,', '"completed_formation_count": 3,', "archive index completed total")
    replace_once(path, '"af03_status": "ready_not_started",\n        "af03_started": False,\n        "af03_authorized": False,', f'"af03_status": "accepted_complete",\n        "af03_started": True,\n        "af03_authorized": True,\n        "af03_accepted_archive_record_count": 10,\n        "af03_blocked_record_count": 0,\n        "af03_remaining_evidence_count": 0,\n        "af03_candidate_exact_head": "{CANDIDATE_HEAD}",\n        "af03_candidate_workflow_run": "{CANDIDATE_RUN}",\n        "af03_candidate_artifact_id": "{CANDIDATE_ARTIFACT}",\n        "af03_candidate_artifact_digest": "{CANDIDATE_ARTIFACT_DIGEST}",\n        "af03_candidate_validation_report_sha256": "{CANDIDATE_REPORT_SHA256}",\n        "af03_candidate_merge": "{CANDIDATE_MERGE}",\n        "af03_acceptance_record": str(AF03_ACCEPTANCE),\n        "af03_sergeant_review_result": "pass_with_mandatory_retained_restrictions",\n        "af03_sergeant_blocking_finding_count": 0,\n        "af04_status": "ready_not_started",\n        "af04_started": False,\n        "af04_authorized": False,', "archive index AF03 acceptance")
    replace_once(path, '"completed formations: 2",\n        "accepted archive records: 19",\n        "blocked completed outcomes: 1",\n        "next formation: AF03 READY / NOT STARTED",', '"completed formations: 3",\n        "accepted archive records: 29",\n        "blocked completed outcomes: 1",\n        "next formation: AF04 READY / NOT STARTED",', "archive manifest totals")
    replace_once(path, '"accepted_archive_record_count": 19,\n        "blocked_archive_record_count": 1,\n        "completed_formation_count": 2,', '"accepted_archive_record_count": 29,\n        "blocked_archive_record_count": 1,\n        "completed_formation_count": 3,', "archive result totals")
    replace_once(path, '"af03_status": "ready_not_started",\n        "af03_started": False,\n        "af03_authorized": False,', '"af03_status": "accepted_complete",\n        "af03_started": True,\n        "af03_authorized": True,\n        "af03_accepted_archive_record_count": 10,\n        "af03_remaining_evidence_count": 0,\n        "af04_status": "ready_not_started",\n        "af04_started": False,\n        "af04_authorized": False,', "archive result AF03")


def sync_archive_tests() -> None:
    path = ROOT / "tools/test_check_archive_formation.py"
    replace_once(path, 'self.assertEqual(result["accepted_archive_record_count"], 19)', 'self.assertEqual(result["accepted_archive_record_count"], 29)', "archive test total")
    replace_once(path, 'self.assertEqual(result["completed_formation_count"], 2)', 'self.assertEqual(result["completed_formation_count"], 3)', "archive test formations")
    replace_once(path, 'self.assertFalse(result["af03_started"])\n        self.assertFalse(result["af03_authorized"])', 'self.assertTrue(result["af03_started"])\n        self.assertTrue(result["af03_authorized"])\n        self.assertEqual(result["af03_accepted_archive_record_count"], 10)\n        self.assertEqual(result["af03_remaining_evidence_count"], 0)\n        self.assertFalse(result["af04_started"])\n        self.assertFalse(result["af04_authorized"])', "archive test AF03 state")
    replace_once(path, '"accepted_archive_record_count": 19', '"accepted_archive_record_count": 29', "archive test mutation source")
    replace_once(path, '    def test_af03_cannot_start_implicitly(self) -> None:\n        root = self.make_repo()\n        path = root / "master-plan-index.json"\n        value = json.loads(path.read_text(encoding="utf-8"))\n        value["operational_protocols"]["tenfold_archive_formation"]["af03_started"] = True\n        path.write_text(json.dumps(value, indent=2) + "\\n", encoding="utf-8")\n        self.assert_invalid(root)', '    def test_af03_cannot_revert_to_unstarted(self) -> None:\n        root = self.make_repo()\n        path = root / "master-plan-index.json"\n        value = json.loads(path.read_text(encoding="utf-8"))\n        value["operational_protocols"]["tenfold_archive_formation"]["af03_started"] = False\n        path.write_text(json.dumps(value, indent=2) + "\\n", encoding="utf-8")\n        self.assert_invalid(root)', "archive AF03 progression test")


def sync_diagnostic_validator() -> None:
    path = ROOT / "tools/check_platform_diagnostic_advisory.py"
    replace_once(path, 'require(af03, "- status: READY / NOT STARTED", "AF03 not-started state")\n    reject(af03, "- status: ACTIVE", "AF03 activation")', 'require(af03, "- status: ACCEPTED COMPLETE", "AF03 accepted state")\n    reject(af03, "- status: ACTIVE", "AF03 activation")\n    af04 = campaign.split("## AF04", 1)[1].split("## AF05", 1)[0]\n    require(af04, "- status: READY / NOT STARTED", "AF04 ready state")', "diagnostic current campaign progression")


def sync_master_plan_validator() -> None:
    path = ROOT / "tools/check_master_plan_closure.py"
    replace_once(path, 'require_text(current, "AF03 remains ready but not started", "CURRENT_STATE AF03 boundary")', 'require_text(current, "AF03: ACCEPTED COMPLETE", "CURRENT_STATE AF03 accepted state")\n    require_text(current, "AF04: READY / NOT STARTED", "CURRENT_STATE AF04 boundary")', "master plan current formation state")


def main() -> int:
    sync_acceptance_record()
    sync_mission()
    sync_result_json()
    sync_result_md()
    sync_manifest()
    sync_current_state()
    sync_progress()
    sync_handoff()
    sync_index()
    sync_af03_validator()
    sync_af03_tests()
    sync_af02_validator()
    sync_af02_tests()
    sync_af01_validator()
    sync_archive_validator()
    sync_archive_tests()
    sync_diagnostic_validator()
    sync_master_plan_validator()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    donor = (ROOT / "DONOR_RECOVERY.md").read_text(encoding="utf-8")
    adr0033 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current or "**Runtime implementation:** AUTHORIZED" in current:
        raise SyncError("runtime boundary failed")
    if "**Status:** COMPLETE AND FROZEN" not in donor:
        raise SyncError("Phase 0A is not frozen")
    if "Status: proposed" not in adr0033:
        raise SyncError("ADR-0033 is not proposed")

    print("AF03 accepted campaign state synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
