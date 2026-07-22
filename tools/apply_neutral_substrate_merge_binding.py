#!/usr/bin/env python3
"""Bind the exact neutral-substrate correction merge into recovery authority."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_EXACT_HEAD = "b7ab2ccad94f1cefeb4693448c2a2ca79b0b00a7"
PRIVATE_RUN = "29962459098"
PRIVATE_ARTIFACT = "8546506459"
PRIVATE_DIGEST = "sha256:ff3e1aef59f0c847964888ef460c6177bdfed181b0a6817318cbc3d2eb9e4ccb"
PRIVATE_MERGE = "fc8ac4c42a3358da37c4866879543a5d7c4d1885"
MERGE_RECORD = "planning/PTAH-NEUTRAL-SUBSTRATE-CORRECTION-MERGE.md"


class BindingError(RuntimeError):
    pass


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise BindingError(f"{label}: expected one source fragment, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def bind_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    replace_once(
        path,
        "Ptah does not select context, rank sources, approve work, issue review verdicts, promote candidates or choose the next agent/action. Full private authority record: `planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md`.",
        f"Ptah does not select context, rank sources, approve work, issue review verdicts, promote candidates or choose the next agent/action. Private correction merge `{PRIVATE_MERGE}` is bound in `{MERGE_RECORD}`.",
        "AI handoff merge binding",
    )


def bind_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    replace_once(
        path,
        "All ten exact-head workflows passed. Corrected Workspace run `29961370694` retained artifact `8546091277` with digest `sha256:04472fd4fd546fcc2420d135cdfcb517381efbe5de8b3bc14f6971207fbde819`.",
        f"All ten public exact-head workflows passed. Corrected Workspace run `29961370694` retained artifact `8546091277` with digest `sha256:04472fd4fd546fcc2420d135cdfcb517381efbe5de8b3bc14f6971207fbde819`. The private plan correction passed 18 regressions at `{PRIVATE_EXACT_HEAD}` in run `{PRIVATE_RUN}`, retained artifact `{PRIVATE_ARTIFACT}` with digest `{PRIVATE_DIGEST}`, and merged as `{PRIVATE_MERGE}`. Full merge record: `{MERGE_RECORD}`.",
        "CURRENT_STATE merge binding",
    )


def bind_index() -> None:
    path = ROOT / "master-plan-index.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    boundary = value.get("ptah_neutral_substrate_boundary")
    if not isinstance(boundary, dict) or boundary.get("status") != "accepted_correction":
        raise BindingError("neutral boundary record missing")
    if boundary.get("af03_started") is not False:
        raise BindingError("AF03 started before merge binding")
    boundary.update(
        {
            "private_exact_head": PRIVATE_EXACT_HEAD,
            "private_workflow_run": PRIVATE_RUN,
            "private_artifact_id": PRIVATE_ARTIFACT,
            "private_artifact_digest": PRIVATE_DIGEST,
            "private_correction_merge": PRIVATE_MERGE,
            "merge_evidence_record": MERGE_RECORD,
        }
    )
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def bind_validator() -> None:
    path = ROOT / "tools/check_master_plan_closure.py"
    replace_once(
        path,
        '        "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md",\n',
        '        "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md",\n        "planning/PTAH-NEUTRAL-SUBSTRATE-CORRECTION-MERGE.md",\n',
        "validator merge record requirement",
    )
    replace_once(
        path,
        '    neutral_correction = read_text(root, "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md")\n',
        '    neutral_correction = read_text(root, "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md")\n    neutral_merge = read_text(root, "planning/PTAH-NEUTRAL-SUBSTRATE-CORRECTION-MERGE.md")\n',
        "validator merge record load",
    )
    anchor = '    require(neutral_index.get("af03_started") is False, "AF03 cannot start during boundary correction")\n'
    checks = f'''    require_text(neutral_merge, "Status: accepted evidence record", "neutral merge evidence state")
    require_text(neutral_merge, "{PRIVATE_MERGE}", "neutral private correction merge")
    require(neutral_index.get("private_exact_head") == "{PRIVATE_EXACT_HEAD}", "neutral private exact head mismatch")
    require(neutral_index.get("private_workflow_run") == "{PRIVATE_RUN}", "neutral private workflow mismatch")
    require(neutral_index.get("private_artifact_id") == "{PRIVATE_ARTIFACT}", "neutral private artifact mismatch")
    require(neutral_index.get("private_artifact_digest") == "{PRIVATE_DIGEST}", "neutral private artifact digest mismatch")
    require(neutral_index.get("private_correction_merge") == "{PRIVATE_MERGE}", "neutral private merge mismatch")
    require(neutral_index.get("merge_evidence_record") == "{MERGE_RECORD}", "neutral merge evidence record mismatch")
'''
    replace_once(path, anchor, anchor + checks, "validator private merge checks")


def bind_tests() -> None:
    path = ROOT / "tools/test_check_master_plan_closure.py"
    replace_once(
        path,
        '    "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md",\n',
        '    "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md",\n    "planning/PTAH-NEUTRAL-SUBSTRATE-CORRECTION-MERGE.md",\n',
        "test merge record requirement",
    )
    insertion = r'''
    def test_private_neutral_correction_merge_cannot_drift(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["ptah_neutral_substrate_boundary"]["private_correction_merge"] = "0" * 40
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)
'''
    replace_once(
        path,
        '\n\nif __name__ == "__main__":',
        insertion + '\n\nif __name__ == "__main__":',
        "test private merge drift",
    )


def main() -> int:
    bind_handoff()
    bind_current_state()
    bind_index()
    bind_validator()
    bind_tests()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    adr33 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    index = json.loads((ROOT / "master-plan-index.json").read_text(encoding="utf-8"))
    archive = index["operational_protocols"]["tenfold_archive_formation"]
    if "**Runtime implementation:** NOT AUTHORIZED" not in current or "**Runtime implementation:** AUTHORIZED" in current:
        raise BindingError("runtime boundary changed")
    if "Status: proposed" not in adr33:
        raise BindingError("ADR-0033 changed")
    if archive.get("af03_status") != "ready_not_started" or archive.get("af03_started") is not False:
        raise BindingError("AF03 changed")
    print("neutral substrate correction merge bound")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
