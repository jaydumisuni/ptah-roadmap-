#!/usr/bin/env python3
"""Run Phase 0C-18 synchronization with exact post-condition wording."""
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
    print("Phase 0C-18 exact post-condition wording synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
