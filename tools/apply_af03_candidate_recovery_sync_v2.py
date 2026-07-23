#!/usr/bin/env python3
"""Run AF03 candidate recovery sync while preserving historical operative token."""
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
    print("AF03 exact operative recovery token preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
