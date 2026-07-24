#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

PROOF_COMMIT = "23dc4b19a0189ba55e08dfa124761efa806bd68b"
CANDIDATE_HEAD = "07465ec89e819b94e3ec39696d9cb8b399d97dbd"
CANDIDATE_RUN = "30095125653"
CANDIDATE_ARTIFACT = "8597258772"
CANDIDATE_ARTIFACT_DIGEST = "sha256:56dc1f0ef54399e9f3a6ade0f8e5e55e878086e0a2f20ccf81a4820d30416165"
CANDIDATE_VALIDATION_SHA = "3a457f7bff7b992a88a278cea1137c51a3e5d05c91674e425e7238f3c6ae109c"
CANDIDATE_REGRESSION_SHA = "0c361de3367a39a73c58512847bad8785562523f2ddb032338c03435bcaf96e0"
CANDIDATE_MERGE = "96d0d465fe74fb1ac2e469b69bfb3326d7d65138"

REQUIRED_FILES = [
    "MASTER_PLAN.md",
    "IMPLEMENTATION_ROADMAP.md",
    "CURRENT_STATE.md",
    "PROGRESS.md",
    "AI_HANDOFF.md",
    "DECISIONS.md",
    "master-plan-index.json",
    "planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md",
    "planning/MASTER-PLAN-RECONCILIATION.md",
    "planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md",
    "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md",
    "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md",
    "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md",
    "decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md",
    "work-packages/PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION.md",
]

PACKAGE_MARKERS = [
    "## A01 amendment", "## A02 amendment", "## A04 amendment", "## A06 amendment",
    "## A07 amendment", "## A08 amendment", "## A09 amendment", "## A11 amendment",
    "## A13 amendment", "## A14 amendment", "## A15 amendment",
    "- **B01:**", "- **B06:**", "- **B07:**",
    "- **D01:**", "- **D02:**", "- **D03:**", "- **D04:**", "- **D09:**",
    "- **E04:**", "- **E06:**", "- **E07:**",
    "- **X1:**", "- **X2:**", "- **X3:**", "- **X4:**", "- **X5:**",
]


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def text(root: Path, path: str) -> str:
    target = root / path
    require(target.is_file(), f"missing required file: {path}")
    return target.read_text(encoding="utf-8")


def validate(root: Path) -> dict:
    docs = {path: text(root, path) for path in REQUIRED_FILES if not path.endswith(".json")}
    index = json.loads(text(root, "master-plan-index.json"))
    plan = docs["MASTER_PLAN.md"]
    roadmap = docs["IMPLEMENTATION_ROADMAP.md"]
    current = docs["CURRENT_STATE.md"]
    handoff = docs["AI_HANDOFF.md"]
    decision = docs["decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md"]
    work_package = docs["work-packages/PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION.md"]
    reconciliation = docs["planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md"]
    p01 = docs["planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md"]
    acceptance = docs["planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md"]

    require("Version: 1.1.0" in plan, "Master Plan version is not 1.1.0")
    require("## 23. Accepted Phase 0C-19 planning-load supplement" in plan, "Master Plan accepted supplement missing")
    require("Version: 1.1.0" in roadmap, "roadmap version is not 1.1.0")
    require("# 8. Accepted Phase 0C-19 amendments to the delivery load" in roadmap, "roadmap accepted amendments missing")
    require("Status: accepted supplement under ADR-0037" in roadmap, "roadmap acceptance status missing")
    for marker in PACKAGE_MARKERS:
        require(marker in roadmap, f"accepted roadmap marker missing: {marker}")

    require("Status: accepted" in decision, "ADR-0037 is not accepted")
    require("## Accepted decision" in decision, "ADR-0037 accepted heading missing")
    require("Status: COMPLETE / ACCEPTED" in work_package, "Phase 0C-19 not complete")
    require("Status: ACCEPTED OPERATIVE PLANNING SUPPLEMENT" in reconciliation, "reconciliation not operative")

    require("**Active work unit:** 0C-04 / P01" in current, "P01 is not active")
    require("DEEP WORKSPACE PLANNING LOAD ACCEPTED" in current, "accepted planning load not in current state")
    require("## Accepted Phase 0C-19 deep Workspace reconciliation" in current, "accepted current-state section missing")
    require("ADR-0037: ACCEPTED" in current, "ADR-0037 accepted state missing")
    require("P01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST" in current, "P01 active blocked state missing")
    require("physical-host collection: NOT STARTED" in current, "physical collection must remain not started")
    require("ADR-0033: PROPOSED" in current, "ADR-0033 must remain proposed")
    require("**Runtime implementation:** NOT AUTHORIZED" in current, "runtime must remain unauthorized")
    require("**Runtime implementation:** AUTHORIZED" not in current, "runtime authorized prematurely")

    require("Status: CONFIRMED, non-authorizing" in p01, "P01 proof selection not confirmed")
    require(PROOF_COMMIT in p01, "confirmed proof commit missing from P01 selection")
    require("physical-host collection has not started" in p01.lower(), "P01 collection not-started statement missing")

    for token in [
        CANDIDATE_HEAD, CANDIDATE_RUN, CANDIDATE_ARTIFACT, CANDIDATE_ARTIFACT_DIGEST,
        CANDIDATE_VALIDATION_SHA, CANDIDATE_REGRESSION_SHA, CANDIDATE_MERGE, PROOF_COMMIT,
    ]:
        require(token in acceptance, f"acceptance evidence missing: {token}")
    require("Phase 0C-19: COMPLETE" in acceptance, "acceptance result missing Phase 0C-19")
    require("ADR-0037: ACCEPTED" in acceptance, "acceptance result missing ADR-0037")
    require("Master Plan: 1.1.0 / ACCEPTED" in acceptance, "accepted Master Plan version missing")
    require("Implementation roadmap: 1.1.0 / ACCEPTED" in acceptance, "accepted roadmap version missing")
    require("physical-host collection: NOT STARTED" in acceptance, "acceptance must retain not-started state")
    require("ADR-0033: PROPOSED" in acceptance, "acceptance prematurely accepts ADR-0033")
    require("Runtime implementation: NOT AUTHORIZED" in acceptance, "acceptance authorizes runtime")

    require("## Accepted Phase 0C-19 planning-load reconciliation" in handoff, "handoff accepted section missing")
    require("Master Plan / roadmap: 1.1.0 / ACCEPTED" in handoff, "handoff accepted versions missing")
    require(PROOF_COMMIT in handoff, "handoff proof commit missing")
    require("P01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST" in handoff, "handoff P01 state missing")

    candidate = index.get("phase0c19_deep_workspace_reconciliation")
    require(isinstance(candidate, dict), "machine Phase 0C-19 record missing")
    expected = {
        "status": "accepted_complete",
        "candidate_merge": CANDIDATE_MERGE,
        "adr_0037_status": "accepted",
        "phase0c19_complete": True,
        "master_plan_version": "1.1.0",
        "implementation_roadmap_version": "1.1.0",
        "p01_paused": False,
        "p01_status": "active_blocked_external_physical_host",
        "provisional_proof_commit": None,
        "confirmed_proof_commit": PROOF_COMMIT,
        "proof_commit_confirmed": True,
        "physical_host_collection_started": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "accepted_state_proof_pending": True,
        "operative_acceptance_merge_pending": True,
    }
    for key, value in expected.items():
        require(candidate.get(key) == value, f"machine Phase 0C-19 mismatch: {key}")
    require(index.get("active_work_unit") == "P01-physical-host-and-ADR-0033-closure", "machine active work is not P01")
    require(index.get("runtime_implementation_authorized") is False, "machine runtime authorized")
    for key in ["master_plan", "implementation_roadmap"]:
        require(index.get("plan_documents", {}).get(key, {}).get("version") == "1.1.0", f"machine {key} version mismatch")

    require("no Core family" in acceptance, "Core-extension boundary missing")
    require("no frozen contract is reopened" in acceptance, "frozen-contract boundary missing")
    require("Ptah does not choose work" in acceptance, "neutral Ptah boundary missing")
    require("The next action is to run the proof kit" in handoff, "handoff next action mismatch")

    return {
        "record_type": "ptah.phase0c19.deep_workspace_roadmap_acceptance_validation",
        "status": "accepted_state_valid_non_authorizing",
        "master_plan_version": "1.1.0",
        "implementation_roadmap_version": "1.1.0",
        "adr_0037_accepted": True,
        "phase0c19_complete": True,
        "p01_active": True,
        "p01_proof_commit_confirmed": True,
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
