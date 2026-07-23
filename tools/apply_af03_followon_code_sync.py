#!/usr/bin/env python3
"""Advance Phase 0C-18 follow-on checks after accepted AF03 closure."""
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


def replace_exact_count(path: Path, old: str, new: str, count_expected: int, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != count_expected:
        raise SyncError(f"{label}: expected {count_expected} source fragments, found {count}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def patch_validator() -> None:
    path = ROOT / "tools/check_platform_diagnostic_advisory.py"
    replace_exact_count(
        path,
        '''        "may_block_unrelated_capable_work": False,
        "af03_started": False,
        "adr_0033_accepted": False,
''',
        '''        "may_block_unrelated_capable_work": False,
        "af03_accepted": True,
        "af03_started": True,
        "af03_authorized": True,
        "af04_ready": True,
        "af04_started": False,
        "af04_authorized": False,
        "adr_0033_accepted": False,
''',
        2,
        "diagnostic machine and report formation progression",
    )


def patch_tests() -> None:
    path = ROOT / "tools/test_check_platform_diagnostic_advisory.py"
    replace_once(
        path,
        '        self.assertFalse(result["af03_started"])',
        '''        self.assertTrue(result["af03_accepted"])
        self.assertTrue(result["af03_started"])
        self.assertTrue(result["af03_authorized"])
        self.assertTrue(result["af04_ready"])
        self.assertFalse(result["af04_started"])
        self.assertFalse(result["af04_authorized"])''',
        "diagnostic valid follow-on assertions",
    )
    replace_once(
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
        "diagnostic AF04 activation regression",
    )


def main() -> int:
    patch_validator()
    patch_tests()
    print("AF03 follow-on diagnostic code synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
