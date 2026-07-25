#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

BINDING = "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-OPERATIVE-BINDING.md"
ACCEPTANCE_MERGE = "8f04e38f34df8c847af5548d0a31f63e8b396f6b"
BINDING_HEAD = "d5b57c7ddacd998b62f0e5d28a45e090f5bad534"
BINDING_RUN = "30155210995"
BINDING_ARTIFACT = "8618788473"
BINDING_MERGE = "d73a3c706e1c6cf326e67eb4e2f4247afbe0f69d"
PROOF_COMMIT = "23dc4b19a0189ba55e08dfa124761efa806bd68b"

REQUIRED_FILES = [
    "AI_HANDOFF.md",
    "CURRENT_STATE.md",
    "MASTER_PLAN.md",
    "IMPLEMENTATION_ROADMAP.md",
    "master-plan-index.json",
    BINDING,
]


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def read(root: Path, path: str) -> str:
    target = root / path
    require(target.is_file(), f"missing required file: {path}")
    return target.read_text(encoding="utf-8")


def validate(root: Path) -> dict:
    handoff = read(root, "AI_HANDOFF.md")
    current = read(root, "CURRENT_STATE.md")
    plan = read(root, "MASTER_PLAN.md")
    roadmap = read(root, "IMPLEMENTATION_ROADMAP.md")
    binding = read(root, BINDING)
    index = json.loads(read(root, "master-plan-index.json"))

    require("Last updated: 2026-07-25" in handoff, "AI handoff date is stale")
    require("## Current accepted planning authority" in handoff, "current authority heading missing")
    require("### Historical 1.0 base authority" in handoff, "historical base heading missing")
    require("## Accepted planning authority" not in handoff, "ambiguous old authority heading remains")
    require("Master Plan version: `1.1.0`" in handoff, "handoff current Master Plan version missing")
    require("implementation roadmap version: `1.1.0`" in handoff, "handoff current roadmap version missing")
    require("ADR-0037 — ACCEPTED" in handoff, "handoff ADR-0037 state missing")
    require("Phase 0C-19 — COMPLETE" in handoff, "handoff Phase 0C-19 state missing")
    require("3. accepted ADR-0037;" in handoff, "handoff reading list still marks ADR-0037 proposed")
    require("3. proposed ADR-0037;" not in handoff, "stale proposed ADR-0037 text remains")

    order = [
        "`AI_HANDOFF.md`",
        "`CURRENT_STATE.md`",
        "`master-plan-index.json`",
        "`MASTER_PLAN.md`",
        "`IMPLEMENTATION_ROADMAP.md`",
        f"`{BINDING}`",
        "`planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`",
    ]
    positions = [handoff.find(token) for token in order]
    require(all(position >= 0 for position in positions), "handoff recovery order item missing")
    require(positions == sorted(positions), "handoff recovery order drifted")

    for token in [ACCEPTANCE_MERGE, BINDING_HEAD, BINDING_RUN, BINDING_ARTIFACT, BINDING_MERGE, PROOF_COMMIT]:
        require(token in handoff, f"handoff evidence missing: {token}")

    require("Version: 1.1.0" in plan, "Master Plan is not 1.1.0")
    require("Version: 1.1.0" in roadmap, "roadmap is not 1.1.0")
    require("P01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST" in current, "P01 state missing")
    require("physical-host collection: NOT STARTED" in current, "physical collection boundary changed")
    require("ADR-0033: PROPOSED" in current, "ADR-0033 boundary changed")
    require("**Runtime implementation:** NOT AUTHORIZED" in current, "runtime non-authorization missing")
    require("**Runtime implementation:** AUTHORIZED" not in current, "runtime authorized prematurely")

    require("Status: OPERATIVE ACCEPTANCE BOUND" in binding, "operative binding is not bound")
    require(BINDING_MERGE in binding, "operative binding merge missing from binding record")

    phase = index.get("phase0c19_deep_workspace_reconciliation")
    require(isinstance(phase, dict), "machine Phase 0C-19 record missing")
    require(phase.get("status") == "accepted_complete", "machine Phase 0C-19 not complete")
    require(phase.get("accepted_state_proof_pending") is False, "accepted-state proof still pending")
    require(phase.get("operative_acceptance_merge_pending") is False, "operative merge still pending")
    require(phase.get("operative_acceptance_merge") == ACCEPTANCE_MERGE, "machine acceptance merge drifted")
    require(phase.get("operative_binding") == BINDING, "machine binding path drifted")
    require(phase.get("confirmed_proof_commit") == PROOF_COMMIT, "machine proof commit drifted")
    require(phase.get("physical_host_collection_started") is False, "physical collection started")
    require(phase.get("adr_0033_accepted") is False, "ADR-0033 accepted prematurely")
    require(phase.get("runtime_implementation_authorized") is False, "runtime authorized prematurely")

    return {
        "record_type": "ptah.phase0c19.ai_handoff_current_authority_validation",
        "status": "current_handoff_authority_valid_non_authorizing",
        "master_plan_version": "1.1.0",
        "implementation_roadmap_version": "1.1.0",
        "phase0c19_complete": True,
        "adr_0037_accepted": True,
        "p01_active": True,
        "physical_host_collection_started": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    report = validate(Path(args.repo_root).resolve())
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
