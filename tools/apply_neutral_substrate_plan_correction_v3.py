#!/usr/bin/env python3
"""Apply the neutral correction with copy-safe tests and exact Phase 0C-15 wording."""
from __future__ import annotations

from pathlib import Path

import apply_neutral_substrate_plan_correction as base
import apply_neutral_substrate_plan_correction_v2 as v2

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_CORRECT_VALIDATOR = base.correct_validator


def correct_validator_exact_wording() -> None:
    ORIGINAL_CORRECT_VALIDATOR()
    path = ROOT / "tools/check_master_plan_closure.py"
    base.replace_once(
        path,
        '    require_text(wp15, "Ptah is the neutral Workspace and execution substrate", "Phase 0C-15 correction")',
        '    require_text(wp15, "**Ptah:** neutral Workspace, storage, execution, Facility, configured-access, Event, Receipt, checkpoint and recovery substrate", "Phase 0C-15 correction")',
        "Phase 0C-15 neutral boundary wording",
    )


base.correct_tests = v2.correct_tests_copy_safe
base.correct_validator = correct_validator_exact_wording

if __name__ == "__main__":
    raise SystemExit(base.main())
