#!/usr/bin/env python3
"""Run AF03 acceptance with accepted follow-on validator shapes."""
from __future__ import annotations

from pathlib import Path

import apply_af03_acceptance as base
import apply_af03_acceptance_v2 as v2

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_SYNC_AF03_TESTS = v2.sync_af03_tests
ORIGINAL_SYNC_DIAGNOSTIC_VALIDATOR = base.sync_diagnostic_validator


def sync_af03_tests() -> None:
    ORIGINAL_SYNC_AF03_TESTS()
    path = ROOT / "tools/test_check_platform_diagnostic_advisory.py"
    base.replace_once(
        path,
        '''    def test_af03_cannot_start(self) -> None:
        root = self.make_repo()
        campaign = root / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md"
        text = campaign.read_text(encoding="utf-8")
        before, after = text.split("## AF03", 1)
        af03, rest = after.split("## AF04", 1)
        self.assertIn("- status: READY / NOT STARTED", af03)
        campaign.write_text(before + "## AF03" + af03.replace("- status: READY / NOT STARTED", "- status: ACTIVE", 1) + "## AF04" + rest, encoding="utf-8")
        self.assert_invalid(root)
''',
        '''    def test_af04_cannot_start(self) -> None:
        root = self.make_repo()
        campaign = root / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md"
        text = campaign.read_text(encoding="utf-8")
        before, after = text.split("## AF04", 1)
        af04, rest = after.split("## AF05", 1)
        self.assertIn("- status: READY / NOT STARTED", af04)
        campaign.write_text(before + "## AF04" + af04.replace("- status: READY / NOT STARTED", "- status: ACTIVE", 1) + "## AF05" + rest, encoding="utf-8")
        self.assert_invalid(root)
''',
        "diagnostic AF04 follow-on regression",
    )


def sync_diagnostic_validator() -> None:
    ORIGINAL_SYNC_DIAGNOSTIC_VALIDATOR()
    path = ROOT / "tools/check_platform_diagnostic_advisory.py"
    base.replace_once(
        path,
        'require(handoff, "AF03 remains READY / NOT STARTED", "handoff AF03 boundary")',
        'require(handoff, "AF03: ACCEPTED COMPLETE", "handoff AF03 accepted state")\n    require(handoff, "AF04: READY / NOT STARTED", "handoff AF04 boundary")',
        "diagnostic handoff formation progression",
    )


def main() -> int:
    v2.sync_af03_tests = sync_af03_tests
    base.sync_diagnostic_validator = sync_diagnostic_validator
    return v2.main()


if __name__ == "__main__":
    raise SystemExit(main())
