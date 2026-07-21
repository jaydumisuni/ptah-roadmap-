#!/usr/bin/env python3
"""Synchronize Campaign 001 and validators with an active AF02 mission."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AF01_ACCEPTANCE_MERGE = "ea2424bb5bc2bdb698bfc1bf389601457abd3c89"
AF02_MISSION = "archive/campaign-001/af02/MISSION.md"


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
        "- next formation: AF02 READY / NOT STARTED",
        "- active formation: AF02\n- AF02 accepted archive records: 0\n- AF02 remaining evidence: 10",
        "campaign AF02 totals",
    )
    replace_once(
        path,
        "## AF02\n\n- status: READY / NOT STARTED\n- private count: 20\n- assigned records: 10\n- reserve pairs: 0",
        "## AF02\n\n- status: ACTIVE\n- private count: 20\n- assigned records: 10\n- accepted archive records: 0\n- remaining evidence: 10\n- mission: `archive/campaign-001/af02/MISSION.md`\n- reserve pairs: 0",
        "AF02 manifest activation",
    )


def sync_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    replace_once(
        path,
        "- AF02: READY / NOT STARTED;",
        "- AF02: ACTIVE / ZERO RECORDS ACCEPTED;\n- AF02 mission: `archive/campaign-001/af02/MISSION.md`;\n- AF01 operative acceptance merge: `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`;",
        "current AF02 activation",
    )
    replace_once(
        path,
        "AF02 readiness does not start evidence collection or authorize source reuse. The archive campaign does not replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation.",
        "AF02 evidence collection is active under its accepted twenty-private mission, with zero records accepted. This archive authorization does not grant source reuse, start AF03, replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation.",
        "current AF02 boundary",
    )


def sync_progress() -> None:
    path = ROOT / "PROGRESS.md"
    replace_once(
        path,
        "- [ ] AF02 is READY / NOT STARTED; no AF02 source record is pre-ticked as archived.",
        "- [-] AF02 is ACTIVE under `archive/campaign-001/af02/MISSION.md`; ten paired reviews are in evidence collection and zero AF02 records are accepted.",
        "progress AF02 activation",
    )


def sync_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    replace_once(
        path,
        "AF02: READY / NOT STARTED",
        "AF02: ACTIVE / ZERO RECORDS ACCEPTED",
        "handoff AF02 activation",
    )
    replace_once(
        path,
        "AF02 is ready but not started.",
        "AF01 accepted closure merged as `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`. AF02 is active under `archive/campaign-001/af02/MISSION.md`, with ten records in evidence collection and zero accepted.",
        "handoff AF02 evidence",
    )


def sync_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise SyncError("active P01 work drifted")
    if data.get("runtime_implementation_authorized") is not False:
        raise SyncError("runtime unexpectedly authorized")
    archive = data["operational_protocols"]["tenfold_archive_formation"]
    if archive.get("af01_status") != "accepted_complete":
        raise SyncError("AF01 is not accepted complete")
    archive.update(
        {
            "status": "accepted_operational_protocol_af01_complete_af02_active",
            "af01_acceptance_merge": AF01_ACCEPTANCE_MERGE,
            "af02_status": "active",
            "af02_started": True,
            "af02_authorized": True,
            "af02_mission": AF02_MISSION,
            "af02_accepted_archive_record_count": 0,
            "af02_remaining_evidence_count": 10,
            "af03_status": "not_started",
            "af03_started": False,
            "af03_authorized": False,
        }
    )
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def sync_archive_validator() -> None:
    path = ROOT / "tools/check_archive_formation.py"
    replacements = (
        (
            'require(progress, "AF02 is READY / NOT STARTED", "progress AF02 ready state")',
            'require(progress, "AF02 is ACTIVE", "progress AF02 active state")',
        ),
        (
            'require(current_state, "AF02: READY / NOT STARTED", "current AF02 ready state")',
            'require(current_state, "AF02: ACTIVE / ZERO RECORDS ACCEPTED", "current AF02 active state")',
        ),
        (
            'require(handoff, "AF02: READY / NOT STARTED", "handoff AF02 ready state")',
            'require(handoff, "AF02: ACTIVE / ZERO RECORDS ACCEPTED", "handoff AF02 active state")',
        ),
        (
            'require(af01_acceptance, "AF02: READY / NOT STARTED", "AF01 next formation state")',
            'require(af01_acceptance, "operative AF01 acceptance merge: `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`", "AF01 operative merge")\n    require(af01_acceptance, "AF02: ACTIVE / ZERO RECORDS ACCEPTED", "AF02 subsequent state")',
        ),
        (
            '"status": "accepted_operational_protocol_af01_complete_af02_ready",',
            '"status": "accepted_operational_protocol_af01_complete_af02_active",',
        ),
        (
            '"af02_status": "ready_not_started",\n        "af02_started": False,\n        "af02_authorized": False,',
            '"af02_status": "active",\n        "af02_started": True,\n        "af02_authorized": True,\n        "af02_mission": "archive/campaign-001/af02/MISSION.md",\n        "af02_accepted_archive_record_count": 0,\n        "af02_remaining_evidence_count": 10,\n        "af03_status": "not_started",\n        "af03_started": False,\n        "af03_authorized": False,',
        ),
        (
            '"af01_acceptance_record": str(AF01_ACCEPTANCE),\n    }',
            '"af01_acceptance_record": str(AF01_ACCEPTANCE),\n        "af01_acceptance_merge": "ea2424bb5bc2bdb698bfc1bf389601457abd3c89",\n    }',
        ),
        (
            '"next formation: AF02 READY / NOT STARTED",',
            '"active formation: AF02",\n        "AF02 accepted archive records: 0",\n        "AF02 remaining evidence: 10",',
        ),
        (
            '"af02_status": "ready_not_started",\n        "af02_started": False,\n        "af02_authorized": False,\n        "phase_0a_reopened": False,',
            '"af02_status": "active",\n        "af02_started": True,\n        "af02_authorized": True,\n        "af02_accepted_archive_record_count": 0,\n        "af02_remaining_evidence_count": 10,\n        "af03_status": "not_started",\n        "af03_started": False,\n        "af03_authorized": False,\n        "phase_0a_reopened": False,',
        ),
    )
    for old, new in replacements:
        replace_once(path, old, new, f"archive validator replacement {old[:40]}")


def sync_archive_tests() -> None:
    path = ROOT / "tools/test_check_archive_formation.py"
    replacements = (
        (
            'self.assertEqual(result["af02_status"], "ready_not_started")\n        self.assertFalse(result["af02_started"])\n        self.assertFalse(result["af02_authorized"])',
            'self.assertEqual(result["af02_status"], "active")\n        self.assertTrue(result["af02_started"])\n        self.assertTrue(result["af02_authorized"])\n        self.assertEqual(result["af02_accepted_archive_record_count"], 0)\n        self.assertEqual(result["af02_remaining_evidence_count"], 10)\n        self.assertFalse(result["af03_started"])\n        self.assertFalse(result["af03_authorized"])',
        ),
        (
            '    def test_af02_cannot_start_implicitly(self) -> None:\n        root = self.make_repo()\n        path = root / "master-plan-index.json"\n        value = json.loads(path.read_text(encoding="utf-8"))\n        value["operational_protocols"]["tenfold_archive_formation"]["af02_started"] = True\n        path.write_text(json.dumps(value, indent=2) + "\\n", encoding="utf-8")\n        self.assert_invalid(root)',
            '    def test_af02_cannot_stop_implicitly(self) -> None:\n        root = self.make_repo()\n        path = root / "master-plan-index.json"\n        value = json.loads(path.read_text(encoding="utf-8"))\n        value["operational_protocols"]["tenfold_archive_formation"]["af02_started"] = False\n        path.write_text(json.dumps(value, indent=2) + "\\n", encoding="utf-8")\n        self.assert_invalid(root)\n\n    def test_af03_cannot_start_implicitly(self) -> None:\n        root = self.make_repo()\n        path = root / "master-plan-index.json"\n        value = json.loads(path.read_text(encoding="utf-8"))\n        value["operational_protocols"]["tenfold_archive_formation"]["af03_started"] = True\n        path.write_text(json.dumps(value, indent=2) + "\\n", encoding="utf-8")\n        self.assert_invalid(root)',
        ),
    )
    for old, new in replacements:
        replace_once(path, old, new, f"archive test replacement {old[:40]}")


def sync_af01_validator() -> None:
    path = ROOT / "tools/check_archive_af01.py"
    replacements = (
        (
            'require(acceptance, "AF02: READY / NOT STARTED", "AF02 next state")',
            'require(acceptance, "operative AF01 acceptance merge: `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`", "AF01 operative merge")\n    require(acceptance, "AF02: ACTIVE / ZERO RECORDS ACCEPTED", "AF02 subsequent active state")',
        ),
        (
            'require(manifest, "- status: READY / NOT STARTED", "manifest AF02 ready state")',
            'require(manifest, "- status: ACTIVE", "manifest AF02 active state")',
        ),
        (
            'require(current_state, "AF02: READY / NOT STARTED", "current AF02 ready state")',
            'require(current_state, "AF02: ACTIVE / ZERO RECORDS ACCEPTED", "current AF02 active state")',
        ),
    )
    for old, new in replacements:
        replace_once(path, old, new, f"AF01 validator replacement {old[:40]}")


def main() -> int:
    sync_manifest()
    sync_current_state()
    sync_progress()
    sync_handoff()
    sync_index()
    sync_archive_validator()
    sync_archive_tests()
    sync_af01_validator()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    donor = (ROOT / "DONOR_RECOVERY.md").read_text(encoding="utf-8")
    adr0033 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current or "**Runtime implementation:** AUTHORIZED" in current:
        raise SyncError("runtime non-authorization boundary failed")
    if "**Status:** COMPLETE AND FROZEN" not in donor:
        raise SyncError("Phase 0A donor register is not frozen")
    if "Status: proposed" not in adr0033:
        raise SyncError("ADR-0033 is not proposed")

    print("AF02 active campaign state synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
