#!/usr/bin/env python3
"""Run AF02 start sync with anchored governing-validator replacements."""
from __future__ import annotations

from pathlib import Path

import apply_archive_af02_start_sync as base

ROOT = Path(__file__).resolve().parents[1]


def anchored_archive_validator() -> None:
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
            '        "completed_formation_count": 1,\n        "af02_status": "ready_not_started",\n        "af02_started": False,\n        "af02_authorized": False,\n        "accepted_state_exact_head":',
            '        "completed_formation_count": 1,\n        "af02_status": "active",\n        "af02_started": True,\n        "af02_authorized": True,\n        "af02_mission": "archive/campaign-001/af02/MISSION.md",\n        "af02_accepted_archive_record_count": 0,\n        "af02_remaining_evidence_count": 10,\n        "af03_status": "not_started",\n        "af03_started": False,\n        "af03_authorized": False,\n        "accepted_state_exact_head":',
        ),
        (
            '        "af01_acceptance_record": str(AF01_ACCEPTANCE),\n    }',
            '        "af01_acceptance_record": str(AF01_ACCEPTANCE),\n        "af01_acceptance_merge": "ea2424bb5bc2bdb698bfc1bf389601457abd3c89",\n    }',
        ),
        (
            '        "next formation: AF02 READY / NOT STARTED",',
            '        "active formation: AF02",\n        "AF02 accepted archive records: 0",\n        "AF02 remaining evidence: 10",',
        ),
        (
            '        "af01_status": "accepted_complete",\n        "af02_status": "ready_not_started",\n        "af02_started": False,\n        "af02_authorized": False,\n        "phase_0a_reopened": False,',
            '        "af01_status": "accepted_complete",\n        "af02_status": "active",\n        "af02_started": True,\n        "af02_authorized": True,\n        "af02_accepted_archive_record_count": 0,\n        "af02_remaining_evidence_count": 10,\n        "af03_status": "not_started",\n        "af03_started": False,\n        "af03_authorized": False,\n        "phase_0a_reopened": False,',
        ),
    )
    for old, new in replacements:
        base.replace_once(path, old, new, f"anchored archive validator replacement {old[:40]}")


base.sync_archive_validator = anchored_archive_validator

if __name__ == "__main__":
    raise SystemExit(base.main())
