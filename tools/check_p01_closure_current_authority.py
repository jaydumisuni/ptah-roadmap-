#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

PROOF_COMMIT = "23dc4b19a0189ba55e08dfa124761efa806bd68b"
PLANNING_BINDING_MERGE = "d73a3c706e1c6cf326e67eb4e2f4247afbe0f69d"
HANDOFF_CORRECTION_MERGE = "15cb887f6fc47ff783e5700613cdf5ee40d0116e"
STALE_PREPARATION_COMMIT = "d05653c5948727b58ead91088447d0b8ac4d9d9b"

REQUIRED_FILES = [
    "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md",
    "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md",
    "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md",
    "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-OPERATIVE-BINDING.md",
    "CURRENT_STATE.md",
    "AI_HANDOFF.md",
    "master-plan-index.json",
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


def section(text: str, start: str, end: str) -> str:
    require(start in text, f"missing section: {start}")
    beginning = text.index(start)
    ending = text.index(end, beginning) if end in text[beginning:] else len(text)
    return text[beginning:ending]


def validate(root: Path) -> dict:
    docs = {path: read(root, path) for path in REQUIRED_FILES if not path.endswith(".json")}
    index = json.loads(read(root, "master-plan-index.json"))

    closure = docs["planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md"]
    selection = docs["planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md"]
    acceptance = docs["planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md"]
    binding = docs["planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-OPERATIVE-BINDING.md"]
    current = docs["CURRENT_STATE.md"]
    handoff = docs["AI_HANDOFF.md"]

    require(
        "Status: exact closure procedure recorded — P01 active and blocked on access to the physical proof host" in closure,
        "P01 closure status is not current",
    )
    require("Recorded: 2026-07-25" in closure, "P01 closure freshness date is stale")
    require("Master Plan version `1.1.0` accepted and operative" in closure, "Master Plan 1.1.0 authority missing")
    require("implementation roadmap version `1.1.0` accepted and operative" in closure, "roadmap 1.1.0 authority missing")
    require("Phase 0C-19 complete and ADR-0037 accepted" in closure, "Phase 0C-19/ADR-0037 authority missing")
    require(PLANNING_BINDING_MERGE in closure, "operative planning binding merge missing")
    require(HANDOFF_CORRECTION_MERGE in closure, "current handoff correction merge missing")
    require(PROOF_COMMIT in closure, "confirmed physical-proof commit missing")

    open_state = section(closure, "Open:\n", "## Required proof host")
    for required in [
        "execution on the exact physical Ubuntu host",
        "package and package-artifact acceptance",
        "durable host-bundle acceptance",
        "final Phase 0C consistency review",
        "ADR-0033 acceptance",
        "explicit runtime authorization",
    ]:
        require(required in open_state, f"open closure obligation missing: {required}")
    require("Master Plan closure" not in open_state, "accepted planning closure is incorrectly listed as open")
    require("Phase 0C-19" not in open_state, "accepted Phase 0C-19 is incorrectly listed as open")

    require("Ubuntu Server 24.04.4 LTS | x86_64 | 6.8.0-136-generic" in closure, "exact host tuple missing")
    require("python3 tools/run_pinned_host_proof.py" in closure, "pinned-host proof command missing")
    require("python3 tools/retain_verified_pinned_host_evidence.py" in closure, "durable-retention command missing")
    require("proof_eligible: true" in closure, "proof-eligibility requirement missing")
    require("Archive Campaign 001 and Phase 0C-01 through Phase 0C-19 records" in closure, "complete Phase 0C review range missing")
    require("A01 — Repository, contracts and reproducible scaffold" in closure, "first authorized runtime package missing")
    require("Runtime implementation: NOT AUTHORIZED" in closure, "fail-closed runtime boundary missing")

    forbidden = [
        "Phase 0C-19 / ADR-0037 planning-load reconciliation in review",
        "complete Master Plan and detailed implementation roadmap candidate prepared",
        STALE_PREPARATION_COMMIT,
        "P01 paused pending Phase 0C-19",
        "ADR-0037: PROPOSED",
        "Master Plan and implementation roadmap version `1.0.0`",
    ]
    for stale in forbidden:
        require(stale not in closure, f"stale P01 closure authority remains: {stale}")

    require("Status: CONFIRMED, non-authorizing" in selection, "P01 proof selection is not confirmed")
    require(PROOF_COMMIT in selection, "P01 selection commit mismatch")
    require("Status: ACCEPTED COMPLETE" in acceptance, "Phase 0C-19 acceptance record missing")
    require("Status: OPERATIVE ACCEPTANCE BOUND" in binding, "operative binding record missing")
    require(PLANNING_BINDING_MERGE in binding, "binding merge mismatch")
    require(HANDOFF_CORRECTION_MERGE in binding, "binding lacks current handoff correction")

    require("P01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST" in current, "CURRENT_STATE P01 boundary mismatch")
    require("physical-host collection: NOT STARTED" in current, "physical-host collection already started")
    require("ADR-0033: PROPOSED" in current, "ADR-0033 is not proposed")
    require("**Runtime implementation:** NOT AUTHORIZED" in current, "runtime non-authorization missing")
    require("**Runtime implementation:** AUTHORIZED" not in current, "runtime authorized prematurely")
    require("Master Plan / roadmap: 1.1.0 / ACCEPTED" in handoff, "AI handoff 1.1.0 authority missing")
    require(PROOF_COMMIT in handoff, "AI handoff proof commit mismatch")

    record = index.get("phase0c19_deep_workspace_reconciliation")
    require(isinstance(record, dict), "machine Phase 0C-19 authority missing")
    require(record.get("status") == "accepted_complete", "machine Phase 0C-19 state mismatch")
    require(record.get("confirmed_proof_commit") == PROOF_COMMIT, "machine proof commit mismatch")
    require(record.get("physical_host_collection_started") is False, "machine physical collection started")
    require(record.get("adr_0033_accepted") is False, "machine ADR-0033 accepted prematurely")
    require(record.get("runtime_implementation_authorized") is False, "machine runtime authorized prematurely")
    require(index.get("active_work_unit") == "P01-physical-host-and-ADR-0033-closure", "machine active work is not P01")
    require(index.get("runtime_implementation_authorized") is False, "global runtime authority changed")

    return {
        "record_type": "ptah.p01.closure_current_authority_validation",
        "status": "current_authority_valid_non_authorizing",
        "master_plan_version": "1.1.0",
        "implementation_roadmap_version": "1.1.0",
        "phase0c19_complete": True,
        "adr_0037_accepted": True,
        "p01_active": True,
        "confirmed_proof_commit": PROOF_COMMIT,
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
