#!/usr/bin/env python3
from __future__ import annotations

import apply_phase0c19_deep_workspace_sync as base


def update_progress() -> None:
    path = "PROGRESS.md"
    text = base.read(path)
    text = text.replace(
        "- [?] P01 — Physical-host and ADR-0033 closure; active and blocked on the exact external host.",
        "- [?] P01 — Physical-host and ADR-0033 closure; paused pending Phase 0C-19 acceptance, then blocked on the exact external host.",
    )
    base.write(path, text)
    base.append_section(
        path,
        "## Deep Workspace operations planning-load reconciliation",
        """
## Deep Workspace operations planning-load reconciliation

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

- [x] deep observable Workspace study merged into `Ptah-space` as `23dc4b19a0189ba55e08dfa124761efa806bd68b`;
- [x] 22 capabilities, 28 mappings, 20 fixtures and 26 original cases recovered;
- [x] no new Core entity and no WP01–WP14 reopening identified;
- [-] Phase 0C-19 canonical planning synchronization in review;
- [-] ADR-0037 proposed;
- [?] P01 paused until the reconciliation is accepted;
- [ ] confirm or supersede the provisional proof commit after acceptance;
- [ ] runtime implementation authorized.
""",
    )


def update_handoff() -> None:
    path = "AI_HANDOFF.md"
    text = base.read(path)
    if "Status: Campaign 001 accepted complete — Phase 0C-19 deep Workspace planning-load reconciliation active — P01 paused — runtime implementation unauthorized" not in text:
        text = base.replace_once(
            text,
            "Status: Master Plan and implementation roadmap accepted — Campaign 001 accepted complete — P01 physical-host closure active — runtime implementation unauthorized\n",
            "Status: Campaign 001 accepted complete — Phase 0C-19 deep Workspace planning-load reconciliation active — P01 paused — runtime implementation unauthorized\n",
            "handoff status",
        )
    base.write(path, text)
    base.append_section(
        path,
        "## Active Phase 0C-19 planning-load reconciliation",
        """
## Active Phase 0C-19 planning-load reconciliation

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

The deep Workspace donor study merged in `Ptah-space` as `23dc4b19a0189ba55e08dfa124761efa806bd68b` after 26/26 study cases and all eleven exact-head workflows passed.

It must be synchronized into the complete private planning load before P01 continues. Read:

1. `planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md`;
2. `work-packages/PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION.md`;
3. proposed ADR-0037;
4. the Phase 0C-19 validator and regressions.

Current boundary:

```text
Phase 0C-19: CANDIDATE / IN REVIEW
ADR-0037: PROPOSED
P01: PAUSED
PR #46 proof commit: PROVISIONAL
physical-host collection: NOT STARTED
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```

Do not run the physical proof until Phase 0C-19 is accepted and the proof commit is confirmed or superseded.
""",
    )


def main() -> None:
    base.update_master_plan()
    base.update_roadmap()
    base.update_recovery_ledger()
    base.update_reconciliation()
    base.update_physical_closure()
    base.update_p01_selection()
    base.update_current_state()
    update_progress()
    update_handoff()
    base.update_decisions()
    base.update_index()
    base.validate_boundary()
    print("Phase 0C-19 deep Workspace planning-load synchronization applied")


if __name__ == "__main__":
    main()
