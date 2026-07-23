#!/usr/bin/env python3
"""Run AF03 acceptance with the accepted AF04 regression shape."""
from __future__ import annotations

import apply_af03_acceptance_v2 as v2


# The accepted AF04 regression shape is now handled in v2. Keep this wrapper
# as the stable workflow entry point without applying the same transform twice.
def sync_af03_tests() -> None:
    v2.sync_af03_tests()


def main() -> int:
    v2.sync_af03_tests = sync_af03_tests
    return v2.main()


if __name__ == "__main__":
    raise SystemExit(main())
