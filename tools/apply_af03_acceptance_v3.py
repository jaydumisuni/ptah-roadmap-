#!/usr/bin/env python3
"""Run AF03 acceptance with the accepted AF04 regression shape."""
from __future__ import annotations

from pathlib import Path

import apply_af03_acceptance as base
import apply_af03_acceptance_v2 as v2

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_SYNC_AF03_TESTS = v2.sync_af03_tests


def sync_af03_tests() -> None:
    ORIGINAL_SYNC_AF03_TESTS()
    path = ROOT / "tools/test_check_archive_af03.py"
    base.replace_once(
        path,
        '''    def test_af04_cannot_start(self) -> None:
        root = self.make_repo()
        self.replace(root, MANIFEST, "## AF04\\n\\n- private count: 20", "## AF04\\n\\n- status: ACTIVE\\n- private count: 20")
        self.assert_invalid(root)
''',
        '''    def test_af04_cannot_start(self) -> None:
        root = self.make_repo()
        self.replace(root, MANIFEST, "- status: READY / NOT STARTED", "- status: ACTIVE")
        self.assert_invalid(root)
''',
        "AF04 accepted-state activation regression",
    )


def main() -> int:
    v2.sync_af03_tests = sync_af03_tests
    return v2.main()


if __name__ == "__main__":
    raise SystemExit(main())
