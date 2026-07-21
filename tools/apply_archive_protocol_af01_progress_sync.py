#!/usr/bin/env python3
"""Synchronize the governing archive validator with accepted AF01 progress."""
from __future__ import annotations

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


def sync_validator() -> None:
    path = ROOT / "tools/check_archive_formation.py"
    replacements = (
        (
            'ACCEPTANCE_RECORD = Path("planning/TENFOLD-ARCHIVE-AUTHORITY-ACCEPTANCE-MERGE.md")',
            'ACCEPTANCE_RECORD = Path("planning/TENFOLD-ARCHIVE-AUTHORITY-ACCEPTANCE-MERGE.md")\nAF01_ACCEPTANCE = Path("archive/campaign-001/af01/ACCEPTANCE.md")',
        ),
        (
            '    ACCEPTANCE_RECORD,\n)',
            '    ACCEPTANCE_RECORD,\n    AF01_ACCEPTANCE,\n)',
        ),
        (
            '    acceptance_record = texts[ACCEPTANCE_RECORD]\n',
            '    acceptance_record = texts[ACCEPTANCE_RECORD]\n    af01_acceptance = texts[AF01_ACCEPTANCE]\n',
        ),
        (
            '    require(progress, "AF01 is READY but not started", "progress AF01 state")\n    require(progress, "no source record is pre-ticked as archived", "progress earned-completion rule")',
            '    require(progress, "AF01 completed ten paired source reviews", "progress AF01 accepted state")\n    require(progress, "AF02 is READY / NOT STARTED", "progress AF02 ready state")',
        ),
        (
            '    require(current_state, "AF01 is READY but not started", "current AF01 state")',
            '    require(current_state, "AF01: ACCEPTED COMPLETE", "current AF01 accepted state")\n    require(current_state, "AF02: READY / NOT STARTED", "current AF02 ready state")',
        ),
        (
            '    require(handoff, "AF01: READY / NOT STARTED", "handoff AF01 state")',
            '    require(handoff, "AF01: ACCEPTED COMPLETE", "handoff AF01 accepted state")\n    require(handoff, "AF02: READY / NOT STARTED", "handoff AF02 ready state")',
        ),
        (
            '    require(acceptance_record, "accepted archive record count `0`", "zero accepted archive records")\n',
            '    require(acceptance_record, "accepted archive record count `0`", "initial zero accepted archive records")\n    require(af01_acceptance, "Status: ACCEPTED EVIDENCE RECORD", "AF01 acceptance record state")\n    require(af01_acceptance, "0a35a8a904bdf235fa4989ea05b684443d5a879a", "AF01 candidate merge")\n    require(af01_acceptance, "AF02: READY / NOT STARTED", "AF01 next formation state")\n',
        ),
        (
            '        "status": "accepted_operational_protocol_af01_ready",',
            '        "status": "accepted_operational_protocol_af01_complete_af02_ready",',
        ),
        (
            '        "af01_status": "ready_not_started",\n        "accepted_archive_record_count": 0,',
            '        "af01_status": "accepted_complete",\n        "accepted_archive_record_count": 9,\n        "blocked_archive_record_count": 1,\n        "completed_formation_count": 1,\n        "af02_status": "ready_not_started",\n        "af02_started": False,\n        "af02_authorized": False,',
        ),
        (
            '        "acceptance_record": str(ACCEPTANCE_RECORD),\n    }',
            '        "acceptance_record": str(ACCEPTANCE_RECORD),\n        "af01_candidate_exact_head": "f60e340cb856d50e88b4279147a933d838fce759",\n        "af01_candidate_workflow_run": "29862087745",\n        "af01_candidate_artifact_id": "8507695005",\n        "af01_candidate_artifact_digest": "sha256:4ea6bf77131834b48b9e35ad5eb88538a87b6f376f2be4984f077eb3eeed1267",\n        "af01_candidate_validation_report_sha256": "4a8cf20f3aacf8628c1de1b774cc93018705d0aa256a65208a8abf4311edc691",\n        "af01_candidate_merge": "0a35a8a904bdf235fa4989ea05b684443d5a879a",\n        "af01_acceptance_record": str(AF01_ACCEPTANCE),\n    }',
        ),
        (
            '        "no runtime authorization",\n    ):',
            '        "no runtime authorization",\n        "completed formations: 1",\n        "accepted archive records: 9",\n        "blocked completed outcomes: 1",\n        "next formation: AF02 READY / NOT STARTED",\n    ):',
        ),
        (
            '        "authority_sync_complete": True,\n        "phase_0a_reopened": False,',
            '        "authority_sync_complete": True,\n        "accepted_archive_record_count": 9,\n        "blocked_archive_record_count": 1,\n        "completed_formation_count": 1,\n        "af01_status": "accepted_complete",\n        "af02_status": "ready_not_started",\n        "af02_started": False,\n        "af02_authorized": False,\n        "phase_0a_reopened": False,',
        ),
    )
    for old, new in replacements:
        replace_once(path, old, new, f"validator replacement {old[:44]}")


def sync_tests() -> None:
    path = ROOT / "tools/test_check_archive_formation.py"
    replacements = (
        (
            '    def test_valid_candidate(self) -> None:',
            '    def test_valid_accepted_campaign_progress(self) -> None:',
        ),
        (
            '        self.assertTrue(result["authority_sync_complete"])\n        self.assertFalse(result["runtime_implementation_authorized"])',
            '        self.assertTrue(result["authority_sync_complete"])\n        self.assertEqual(result["accepted_archive_record_count"], 9)\n        self.assertEqual(result["blocked_archive_record_count"], 1)\n        self.assertEqual(result["completed_formation_count"], 1)\n        self.assertEqual(result["af01_status"], "accepted_complete")\n        self.assertEqual(result["af02_status"], "ready_not_started")\n        self.assertFalse(result["af02_started"])\n        self.assertFalse(result["af02_authorized"])\n        self.assertFalse(result["runtime_implementation_authorized"])',
        ),
        (
            '    def test_af01_cannot_be_precompleted(self) -> None:\n        root = self.make_repo()\n        self.replace(\n            root,\n            Path("master-plan-index.json"),\n            \'"accepted_archive_record_count": 0\',\n            \'"accepted_archive_record_count": 10\',\n        )\n        self.assert_invalid(root)',
            '    def test_af01_accepted_count_cannot_drift(self) -> None:\n        root = self.make_repo()\n        self.replace(\n            root,\n            Path("master-plan-index.json"),\n            \'"accepted_archive_record_count": 9\',\n            \'"accepted_archive_record_count": 10\',\n        )\n        self.assert_invalid(root)\n\n    def test_af01_acceptance_record_cannot_disappear(self) -> None:\n        root = self.make_repo()\n        (root / "archive/campaign-001/af01/ACCEPTANCE.md").unlink()\n        self.assert_invalid(root)\n\n    def test_af02_cannot_start_implicitly(self) -> None:\n        root = self.make_repo()\n        path = root / "master-plan-index.json"\n        value = json.loads(path.read_text(encoding="utf-8"))\n        value["operational_protocols"]["tenfold_archive_formation"]["af02_started"] = True\n        path.write_text(json.dumps(value, indent=2) + "\\n", encoding="utf-8")\n        self.assert_invalid(root)',
        ),
    )
    for old, new in replacements:
        replace_once(path, old, new, f"test replacement {old[:44]}")


def main() -> int:
    sync_validator()
    sync_tests()
    print("archive protocol validator synchronized with AF01 acceptance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
