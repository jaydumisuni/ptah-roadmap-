#!/usr/bin/env python3
"""Run AF03 acceptance with anchored historical/current transformations."""
from __future__ import annotations

from pathlib import Path

import apply_af03_acceptance as base

ROOT = Path(__file__).resolve().parents[1]


def sync_af03_tests() -> None:
    path = ROOT / "tools/test_check_archive_af03.py"
    base.replace_once(path, "from check_archive_af03 import (\n    ADR0033,\n", "from check_archive_af03 import (\n    ACCEPTANCE,\n    ADR0033,\n", "AF03 test acceptance import")
    base.replace_once(path, "    RESULT_MD,\n    SERGEANT_REVIEW,\n    MANIFEST,", "    RESULT_MD,\n    SERGEANT_REVIEW,\n    ACCEPTANCE,\n    MANIFEST,", "AF03 test acceptance fixture")
    base.replace_once(path, 'self.assertEqual(result["status"], "candidate_complete_valid_non_authorizing")', 'self.assertEqual(result["status"], "accepted_complete_valid_non_authorizing")', "AF03 valid status test")
    base.replace_once(path, 'self.assertEqual(result["candidate_archive_outcome_count"], 10)', 'self.assertEqual(result["accepted_archive_record_count"], 10)', "AF03 accepted count test")
    base.replace_once(path, 'self.assertFalse(result["af03_accepted"])', 'self.assertTrue(result["af03_accepted"])', "AF03 accepted assertion")
    base.replace_once(path, '''    def test_result_status_cannot_be_accepted(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "status", "accepted_complete")
        self.assert_invalid(root)
''', '''    def test_result_status_cannot_revert_to_candidate(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "status", "candidate_complete_pending_exact_head_review")
        self.assert_invalid(root)
''', "AF03 status regression")
    base.replace_once(path, '''    def test_acceptance_record_cannot_appear(self) -> None:
        root = self.make_repo()
        path = root / "archive/campaign-001/af03/ACCEPTANCE.md"
        path.write_text("# premature acceptance\\n", encoding="utf-8")
        self.assert_invalid(root)
''', '''    def test_acceptance_record_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / ACCEPTANCE).unlink()
        self.assert_invalid(root)
''', "AF03 acceptance regression")
    base.replace_once(path, '        self.replace(root, MANIFEST, "## AF04\\n\\n- private count: 20", "## AF04\\n\\n- status: ACTIVE\\n- private count: 20")', '        self.replace(root, MANIFEST, "## AF04\\n\\n- status: READY / NOT STARTED\\n- private count: 20", "## AF04\\n\\n- status: ACTIVE\\n- private count: 20")', "AF04 start regression anchor")
    base.replace_once(path, 'self.mutate_index(root, "accepted_archive_record_count", 29)', 'self.mutate_index(root, "accepted_archive_record_count", 19)', "AF03 operative total regression")


def sync_af02_validator() -> None:
    path = ROOT / "tools/check_archive_af02.py"
    base.replace_once(path, 'require(current_state, "AF03: READY / NOT STARTED", "current AF03 ready state")', 'require(current_state, "AF03: ACCEPTED COMPLETE", "current AF03 accepted state")\n    require(current_state, "AF04: READY / NOT STARTED", "current AF04 ready state")', "AF02 current follow-on")
    base.replace_once(path, 'if archive.get("completed_formation_count") != 2 or archive.get("accepted_archive_record_count") != 19:\n        raise ValidationError("campaign accepted totals are invalid")', 'if archive.get("completed_formation_count") != 3 or archive.get("accepted_archive_record_count") != 29:\n        raise ValidationError("campaign accepted totals are invalid")', "AF02 current totals")
    base.replace_once(path, 'if archive.get("af03_status") != "ready_not_started" or archive.get("af03_started") is not False or archive.get("af03_authorized") is not False:\n        raise ValidationError("AF03 started before AF02 closure")', 'if archive.get("af03_status") != "accepted_complete" or archive.get("af03_started") is not True or archive.get("af03_authorized") is not True:\n        raise ValidationError("AF03 follow-on acceptance is invalid")\n    if archive.get("af03_accepted_archive_record_count") != 10 or archive.get("af03_remaining_evidence_count") != 0:\n        raise ValidationError("AF03 accepted counts are invalid")\n    if archive.get("af04_status") != "ready_not_started" or archive.get("af04_started") is not False or archive.get("af04_authorized") is not False:\n        raise ValidationError("AF04 follow-on state is invalid")', "AF02 follow-on machine state")
    base.replace_once(path, '''        "runtime_implementation_authorized": False,
        "af03_ready": True,
        "af03_started": False,
        "af03_authorized": False,
    }


def main() -> int:''', '''        "runtime_implementation_authorized": False,
        "af03_accepted": True,
        "af03_started": True,
        "af03_authorized": True,
        "af04_ready": True,
        "af04_started": False,
        "af04_authorized": False,
    }


def main() -> int:''', "AF02 current return follow-on")


def sync_archive_validator() -> None:
    path = ROOT / "tools/check_archive_formation.py"
    base.replace_once(path, 'AF02_ACCEPTANCE = Path("archive/campaign-001/af02/ACCEPTANCE.md")', 'AF02_ACCEPTANCE = Path("archive/campaign-001/af02/ACCEPTANCE.md")\nAF03_ACCEPTANCE = Path("archive/campaign-001/af03/ACCEPTANCE.md")', "archive AF03 acceptance constant")
    base.replace_once(path, '    AF02_ACCEPTANCE,\n)', '    AF02_ACCEPTANCE,\n    AF03_ACCEPTANCE,\n)', "archive required AF03 acceptance")
    base.replace_once(path, 'af02_acceptance = texts[AF02_ACCEPTANCE]\n', 'af02_acceptance = texts[AF02_ACCEPTANCE]\n    af03_acceptance = texts[AF03_ACCEPTANCE]\n', "archive AF03 acceptance read")
    base.replace_once(path, 'require(progress, "AF03 is READY / NOT STARTED", "progress AF03 ready state")', 'require(progress, "AF03 accepted complete", "progress AF03 accepted state")\n    require(progress, "AF04 is READY / NOT STARTED", "progress AF04 ready state")', "archive progress follow-on")
    base.replace_once(path, 'require(current_state, "AF03: READY / NOT STARTED", "current AF03 ready state")', 'require(current_state, "AF03: ACCEPTED COMPLETE", "current AF03 accepted state")\n    require(current_state, "AF04: READY / NOT STARTED", "current AF04 ready state")', "archive current follow-on")
    base.replace_once(path, 'require(handoff, "AF03: READY / NOT STARTED", "handoff AF03 ready state")', 'require(handoff, "AF03: ACCEPTED COMPLETE", "handoff AF03 accepted state")\n    require(handoff, "AF04: READY / NOT STARTED", "handoff AF04 ready state")', "archive handoff follow-on")
    base.replace_once(path, 'require(af02_acceptance, "AF03: READY / NOT STARTED", "AF03 next state")', 'require(af02_acceptance, "AF03: READY / NOT STARTED", "historical AF03 state at AF02 acceptance")\n    require(af03_acceptance, "Status: ACCEPTED EVIDENCE RECORD", "AF03 acceptance state")\n    require(af03_acceptance, "d86218e1127c57bacfb4d88eff15b81d326995ba", "AF03 candidate merge")\n    require(af03_acceptance, "AF04 status: `READY / NOT STARTED`", "AF04 next state")', "archive AF03 acceptance checks")
    base.replace_once(path, '"status": "accepted_operational_protocol_af02_complete_af03_ready",', '"status": "accepted_operational_protocol_af03_complete_af04_ready",', "archive index status")
    base.replace_once(path, '''        "phase0c_17_complete": True,
        "af01_status": "accepted_complete",
        "accepted_archive_record_count": 19,
        "blocked_archive_record_count": 1,
        "completed_formation_count": 2,
''', '''        "phase0c_17_complete": True,
        "af01_status": "accepted_complete",
        "accepted_archive_record_count": 29,
        "blocked_archive_record_count": 1,
        "completed_formation_count": 3,
''', "archive expected-index totals")
    base.replace_once(path, '''        "af03_status": "ready_not_started",
        "af03_started": False,
        "af03_authorized": False,
        "accepted_state_exact_head":''', f'''        "af03_status": "accepted_complete",
        "af03_started": True,
        "af03_authorized": True,
        "af03_accepted_archive_record_count": 10,
        "af03_blocked_record_count": 0,
        "af03_remaining_evidence_count": 0,
        "af03_candidate_exact_head": "{base.CANDIDATE_HEAD}",
        "af03_candidate_workflow_run": "{base.CANDIDATE_RUN}",
        "af03_candidate_artifact_id": "{base.CANDIDATE_ARTIFACT}",
        "af03_candidate_artifact_digest": "{base.CANDIDATE_ARTIFACT_DIGEST}",
        "af03_candidate_validation_report_sha256": "{base.CANDIDATE_REPORT_SHA256}",
        "af03_candidate_merge": "{base.CANDIDATE_MERGE}",
        "af03_acceptance_record": str(AF03_ACCEPTANCE),
        "af03_sergeant_review_result": "pass_with_mandatory_retained_restrictions",
        "af03_sergeant_blocking_finding_count": 0,
        "af04_status": "ready_not_started",
        "af04_started": False,
        "af04_authorized": False,
        "accepted_state_exact_head":''', "archive expected-index AF03")
    base.replace_once(path, '''        "completed formations: 2",
        "accepted archive records: 19",
        "blocked completed outcomes: 1",
        "next formation: AF03 READY / NOT STARTED",
''', '''        "completed formations: 3",
        "accepted archive records: 29",
        "blocked completed outcomes: 1",
        "next formation: AF04 READY / NOT STARTED",
''', "archive manifest totals")
    base.replace_once(path, '''        "authority_sync_complete": True,
        "accepted_archive_record_count": 19,
        "blocked_archive_record_count": 1,
        "completed_formation_count": 2,
''', '''        "authority_sync_complete": True,
        "accepted_archive_record_count": 29,
        "blocked_archive_record_count": 1,
        "completed_formation_count": 3,
''', "archive report totals")
    base.replace_once(path, '''        "af03_status": "ready_not_started",
        "af03_started": False,
        "af03_authorized": False,
        "phase_0a_reopened": False,
''', '''        "af03_status": "accepted_complete",
        "af03_started": True,
        "af03_authorized": True,
        "af03_accepted_archive_record_count": 10,
        "af03_remaining_evidence_count": 0,
        "af04_status": "ready_not_started",
        "af04_started": False,
        "af04_authorized": False,
        "phase_0a_reopened": False,
''', "archive report AF03")


def main() -> int:
    base.sync_af03_tests = sync_af03_tests
    base.sync_af02_validator = sync_af02_validator
    base.sync_archive_validator = sync_archive_validator
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
