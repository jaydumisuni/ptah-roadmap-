#!/usr/bin/env python3
"""Run AF03 candidate recovery sync while preserving historical operative tokens."""
from __future__ import annotations

from pathlib import Path

import apply_af03_candidate_recovery_sync as base

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    base.main()
    base.replace_once(
        ROOT / "CURRENT_STATE.md",
        "- AF03 operative status: READY / NOT STARTED;\n- AF03 candidate package:",
        "- AF03: READY / NOT STARTED;\n- AF03 candidate package:",
        "current state exact operative token",
    )
    base.replace_once(
        ROOT / "PROGRESS.md",
        "- [x] AF03 candidate evidence prepared: ten paired records, ten bounded candidate outcomes, zero remaining evidence and independent Sergeant PASS WITH MANDATORY RETAINED RESTRICTIONS; operative AF03 remains READY / NOT STARTED and no record is accepted yet.",
        "- [x] AF03 is READY / NOT STARTED operatively; candidate evidence is prepared with ten paired records, ten bounded candidate outcomes, zero remaining evidence and independent Sergeant PASS WITH MANDATORY RETAINED RESTRICTIONS; no record is accepted yet.",
        "progress exact operative token",
    )
    print("AF03 exact operative recovery tokens preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
