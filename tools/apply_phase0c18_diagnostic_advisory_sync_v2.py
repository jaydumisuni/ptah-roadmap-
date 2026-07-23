#!/usr/bin/env python3
"""Run Phase 0C-18 synchronization with exact owner wording."""
from __future__ import annotations

from pathlib import Path

import apply_phase0c18_diagnostic_advisory_sync as base

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    base.main()
    base.replace_once(
        ROOT / "tools/check_platform_diagnostic_advisory.py",
        'require(protocol, "acknowledgement does not equal successful upgrade", "post-condition boundary")',
        'require(protocol, "Installation acknowledgement does not equal resolution", "post-condition boundary")',
        "validator post-condition wording",
    )
    base.replace_once(
        ROOT / "tools/test_check_platform_diagnostic_advisory.py",
        '"acknowledgement does not equal successful upgrade",\n                     "acknowledgement equals successful upgrade"',
        '"Installation acknowledgement does not equal resolution",\n                     "Installation acknowledgement equals resolution"',
        "regression post-condition wording",
    )
    base.replace_once(
        ROOT / "tools/check_platform_diagnostic_advisory.py",
        'require(work_package, "diagnose platform condition without deciding caller work", "owner diagnostic direction")',
        'require(work_package, "Ptah does not decide the work given", "owner diagnostic direction")',
        "validator owner diagnostic wording",
    )
    base.replace_once(
        ROOT / "tools/check_platform_diagnostic_advisory.py",
        'require(protocol, "twenty bounded worker slots", "two-worker formation capacity")',
        'require(protocol, "The ordinary two-human-equivalent formation therefore exposes twenty bounded worker slots.", "two-worker formation capacity")',
        "validator exact worker minimum sentence",
    )
    base.replace_once(
        ROOT / "tools/test_check_platform_diagnostic_advisory.py",
        '"twenty bounded worker slots",\n                     "four bounded worker slots"',
        '"The ordinary two-human-equivalent formation therefore exposes twenty bounded worker slots.",\n                     "The ordinary two-human-equivalent formation therefore exposes four bounded worker slots."',
        "regression exact worker minimum sentence",
    )
    print("Phase 0C-18 exact owner and worker wording synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
