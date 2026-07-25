#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CorrectionError(RuntimeError):
    pass


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise CorrectionError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    path = ROOT / "AI_HANDOFF.md"
    text = path.read_text(encoding="utf-8")

    text = replace_once(
        text,
        "Last updated: 2026-07-24",
        "Last updated: 2026-07-25",
        "handoff date",
    )

    old_order = """1. `AI_HANDOFF.md`
2. `CURRENT_STATE.md`
3. `master-plan-index.json`
4. `MASTER_PLAN.md`
5. `IMPLEMENTATION_ROADMAP.md`
6. `archive/campaign-001/OPERATIVE-BINDING.md`
7. `archive/campaign-001/OPERATIVE-STATE.json`
8. `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`
9. `planning/MASTER-PLAN-RECONCILIATION.md`
10. `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`
11. `PROGRESS.md`
12. `DECISIONS.md` and the referenced ADRs
13. `MEMORY_PROTOCOL.md`
14. current source and evidence in `jaydumisuni/Ptah-space`"""
    new_order = """1. `AI_HANDOFF.md`
2. `CURRENT_STATE.md`
3. `master-plan-index.json`
4. `MASTER_PLAN.md`
5. `IMPLEMENTATION_ROADMAP.md`
6. `planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-OPERATIVE-BINDING.md`
7. `archive/campaign-001/OPERATIVE-BINDING.md`
8. `archive/campaign-001/OPERATIVE-STATE.json`
9. `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`
10. `planning/MASTER-PLAN-RECONCILIATION.md`
11. `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`
12. `PROGRESS.md`
13. `DECISIONS.md` and the referenced ADRs
14. `MEMORY_PROTOCOL.md`
15. current source and evidence in `jaydumisuni/Ptah-space`"""
    text = replace_once(text, old_order, new_order, "handoff recovery order")

    old_authority = """## Accepted planning authority

- Master Plan version: `1.0.0`;
- implementation roadmap version: `1.0.0`;
- accepted authority decision: ADR-0034;
- accepted work package: Phase 0C-16;
- candidate exact head: `37d23449fda9a426f56ee8b09042dda91587a6d1`;
- exact-head workflow run: `29842137511`;
- retained artifact: `8499790872`;
- artifact archive digest: `sha256:82d6b452777e2c5e60c4d08bf88dd2c848d6b2570650b70a4eede633c8065d9f`;
- candidate squash merge: `2c24f9e6b0fc98d5e03605596db75d7495796353`;
- accepted-state exact head: `5860b4bfe177aa375fb2fa4305d62dbe3d2141e1`;
- permanent accepted-state workflow run: `29844040274`;
- retained accepted-state artifact: `8500540358`;
- accepted-state archive digest: `sha256:6f5229fe850d8b6f6f083b09f2c5f53189f3edbf38d4f28b9d2878ab0c78862d`;
- operative authority acceptance merge: `66bd2410d4c777cd3fd3278107f40fe425e875e9`."""
    new_authority = """## Current accepted planning authority

- Master Plan version: `1.1.0`;
- implementation roadmap version: `1.1.0`;
- current supplement decision: ADR-0037 — ACCEPTED;
- current supplement work package: Phase 0C-19 — COMPLETE;
- reconciliation candidate exact head: `07465ec89e819b94e3ec39696d9cb8b399d97dbd`;
- reconciliation workflow run: `30095125653`;
- reconciliation artifact: `8597258772`;
- reconciliation candidate merge: `96d0d465fe74fb1ac2e469b69bfb3326d7d65138`;
- accepted-state exact head: `02e3ea2d26e39362ac8a90ad0bb7b248396476a6`;
- accepted-state workflow run: `30097738203`;
- accepted-state artifact: `8598283488`;
- planning-load acceptance merge: `8f04e38f34df8c847af5548d0a31f63e8b396f6b`;
- operative-binding exact head: `d5b57c7ddacd998b62f0e5d28a45e090f5bad534`;
- operative-binding workflow run: `30155210995`;
- operative-binding artifact: `8618788473`;
- operative recovery-binding merge: `d73a3c706e1c6cf326e67eb4e2f4247afbe0f69d`.

### Historical 1.0 base authority

The original accepted base remains retained as historical provenance beneath operative version `1.1.0`:

- Master Plan version: `1.0.0`;
- implementation roadmap version: `1.0.0`;
- accepted base decision: ADR-0034;
- accepted base work package: Phase 0C-16;
- candidate exact head: `37d23449fda9a426f56ee8b09042dda91587a6d1`;
- exact-head workflow run: `29842137511`;
- retained artifact: `8499790872`;
- candidate squash merge: `2c24f9e6b0fc98d5e03605596db75d7495796353`;
- accepted-state exact head: `5860b4bfe177aa375fb2fa4305d62dbe3d2141e1`;
- permanent accepted-state workflow run: `29844040274`;
- retained accepted-state artifact: `8500540358`;
- operative base-authority acceptance merge: `66bd2410d4c777cd3fd3278107f40fe425e875e9`."""
    text = replace_once(text, old_authority, new_authority, "handoff authority block")

    text = replace_once(
        text,
        "3. proposed ADR-0037;",
        "3. accepted ADR-0037;",
        "handoff ADR-0037 reading state",
    )

    path.write_text(text, encoding="utf-8")
    print("Phase 0C-19 AI handoff authority correction applied")


if __name__ == "__main__":
    main()
