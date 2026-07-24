#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SyncError(RuntimeError):
    pass


def patch(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{path}: expected one patch anchor, found {count}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    patch(
        "tools/check_master_plan_closure.py",
        '    require_text(current, "**Active work unit:** 0C-04 / P01", "CURRENT_STATE")\n',
        '''    phase0c19 = index.get("phase0c19_deep_workspace_reconciliation")
    phase0c19_candidate = isinstance(phase0c19, dict) and phase0c19.get("status") == "candidate_in_review"
    if phase0c19_candidate:
        require_text(
            current,
            "**Active work unit:** Phase 0C-19 — deep Workspace study Master Plan and roadmap reconciliation; P01 paused",
            "CURRENT_STATE",
        )
        require(phase0c19.get("p01_paused") is True, "Phase 0C-19 must pause P01")
        require(phase0c19.get("physical_host_collection_started") is False, "physical-host collection started during Phase 0C-19")
    else:
        require_text(current, "**Active work unit:** 0C-04 / P01", "CURRENT_STATE")
''',
    )
    patch(
        "tools/check_master_plan_closure.py",
        '    require(index.get("active_work_unit") == "P01-physical-host-and-ADR-0033-closure", "master-plan index active work mismatch")\n',
        '''    if phase0c19_candidate:
        require(
            index.get("active_work_unit") == "Phase-0C-19-deep-workspace-roadmap-reconciliation",
            "master-plan index Phase 0C-19 active work mismatch",
        )
    else:
        require(index.get("active_work_unit") == "P01-physical-host-and-ADR-0033-closure", "master-plan index active work mismatch")
''',
    )

    patch(
        "tools/check_archive_campaign_complete.py",
        '    require("**Active work unit:** 0C-04 / P01 — physical pinned-host proof" in current, "P01 current-state authority missing")\n',
        '''    phase0c19_active = "**Active work unit:** Phase 0C-19 — deep Workspace study Master Plan and roadmap reconciliation; P01 paused" in current
    p01_active = "**Active work unit:** 0C-04 / P01 — physical pinned-host proof" in current
    require(phase0c19_active or p01_active, "current implementation-authorization work authority missing")
    if phase0c19_active:
        require("P01: PAUSED" in current, "Phase 0C-19 current state does not pause P01")
        require("physical-host collection: NOT STARTED" in current, "physical-host collection started during Phase 0C-19")
''',
    )
    patch(
        "tools/test_check_archive_campaign_complete.py",
        '            "**Active work unit:** 0C-04 / P01 — physical pinned-host proof",\n            "**Active work unit:** campaign complete",\n',
        '            "**Active work unit:** Phase 0C-19 — deep Workspace study Master Plan and roadmap reconciliation; P01 paused",\n            "**Active work unit:** campaign complete",\n',
    )

    patch(
        "tools/check_platform_diagnostic_advisory.py",
        '''    if index.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise ValidationError("P01 active work unit drifted")
''',
        '''    phase0c19 = index.get("phase0c19_deep_workspace_reconciliation")
    phase0c19_candidate = isinstance(phase0c19, dict) and phase0c19.get("status") == "candidate_in_review"
    if phase0c19_candidate:
        if index.get("active_work_unit") != "Phase-0C-19-deep-workspace-roadmap-reconciliation":
            raise ValidationError("Phase 0C-19 active work unit drifted")
        if phase0c19.get("p01_paused") is not True:
            raise ValidationError("Phase 0C-19 must pause P01")
        if phase0c19.get("physical_host_collection_started") is not False:
            raise ValidationError("physical-host collection started during Phase 0C-19")
    elif index.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise ValidationError("P01 active work unit drifted")
''',
    )

    print("Phase 0C-19 legacy validator synchronization applied")


if __name__ == "__main__":
    main()
