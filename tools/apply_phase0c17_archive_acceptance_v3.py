#!/usr/bin/env python3
"""Run accepted archive transform with accepted decision-index regression target."""
from __future__ import annotations

from pathlib import Path

import apply_phase0c17_archive_acceptance as base
import apply_phase0c17_archive_acceptance_v2 as v2

ROOT = Path(__file__).resolve().parents[1]


def accepted_validator_and_tests() -> None:
    v2.fixed_accept_validator_and_tests()
    tests = ROOT / "tools/test_check_archive_formation.py"
    base.replace_once(
        tests,
        '            "### ADR-0035 — Tenfold archive formation and evidence promotion",\n'
        '            "### Archive idea without decision authority",',
        '            "### D-051 — Tenfold archive formation separates parallel evidence from promotion authority",\n'
        '            "### Archive idea without decision authority",',
        "accepted decision-index mutation target",
    )


base.accept_validator_and_tests = accepted_validator_and_tests

if __name__ == "__main__":
    raise SystemExit(base.main())
