#!/usr/bin/env python3
"""Run AF03 acceptance with the accepted AF04 regression shape."""
from __future__ import annotations

import apply_af03_acceptance_v2 as v2

ORIGINAL_SYNC_AF03_TESTS = v2.sync_af03_tests


# The accepted AF04 regression shape is handled in v2. Keep this wrapper as
# the stable workflow entry point and call the saved original exactly once.
def sync_af03_tests() -> None:
    ORIGINAL_SYNC_AF03_TESTS()


def main() -> int:
    v2.sync_af03_tests = sync_af03_tests
    return v2.main()


if __name__ == "__main__":
    raise SystemExit(main())
