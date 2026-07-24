#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SyncError(RuntimeError):
    pass


def patch(path: str, old: str, new: str) -> None:
    target = ROOT / path
    content = target.read_text(encoding="utf-8")
    count = content.count(old)
    if count != 1:
        raise SyncError(f"{path}: expected one patch anchor, found {count}")
    target.write_text(content.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    patch(
        "tools/check_master_plan_closure.py",
        '''    require_text(master, "Version: 1.0.0", "MASTER_PLAN")
''',
        '''    phase0c19_accepted = isinstance(phase0c19, dict) and phase0c19.get("status") == "accepted_complete"
    expected_plan_version = "1.1.0" if phase0c19_accepted else "1.0.0"
    require_text(master, f"Version: {expected_plan_version}", "MASTER_PLAN")
''',
    )
    patch(
        "tools/check_master_plan_closure.py",
        '''    require_text(roadmap, "Version: 1.0.0", "IMPLEMENTATION_ROADMAP")
''',
        '''    require_text(roadmap, f"Version: {expected_plan_version}", "IMPLEMENTATION_ROADMAP")
''',
    )
    patch(
        "tools/test_check_archive_campaign_complete.py",
        '''            "**Active work unit:** Phase 0C-19 — deep Workspace study Master Plan and roadmap reconciliation; P01 paused",
            "**Active work unit:** campaign complete",
''',
        '''            "**Active work unit:** 0C-04 / P01 — physical pinned-host proof, package review, durable evidence and ADR-0033 closure",
            "**Active work unit:** campaign complete",
''',
    )
    print("Accepted Phase 0C-19 legacy validator synchronization applied")


if __name__ == "__main__":
    main()
