#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

SOURCE_HEAD = "bf4ae98b9d492ad688644fd6a330aaf435ac70c1"
SOURCE_MERGE = "23dc4b19a0189ba55e08dfa124761efa806bd68b"
CANDIDATE_HEAD = "07465ec89e819b94e3ec39696d9cb8b399d97dbd"
CANDIDATE_MERGE = "96d0d465fe74fb1ac2e469b69bfb3326d7d65138"
ACCEPTED_HEAD = "02e3ea2d26e39362ac8a90ad0bb7b248396476a6"
ACCEPTED_RUN = "30097738203"
ACCEPTED_ARTIFACT = "8598283488"
ACCEPTED_ARTIFACT_DIGEST = "sha256:1d571edbe7da273c98c01ec452c005d86dfda723f9483c44f54403d40ad7747c"
ACCEPTED_VALIDATION_SHA = "258a0ea7aa8bf20ca744dbca546d2de34ab0f7cb61cfa9e7d780d1401717158f"
ACCEPTED_REGRESSION_SHA = "39ac2470fa7140e9c0b3c65cc687d79838a70ddb6286a869da218cf8d36b1d23"
OPERATIVE_MERGE = "8f04e38f34df8c847af5548d0a31f63e8b396f6b"
PROOF_COMMIT = SOURCE_MERGE
BINDING_PATH = "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-OPERATIVE-BINDING.md"

REQUIRED_FILES = [
    "MASTER_PLAN.md",
    "IMPLEMENTATION_ROADMAP.md",
    "CURRENT_STATE.md",
    "AI_HANDOFF.md",
    "master-plan-index.json",
    "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md",
    BINDING_PATH,
    "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md",
    "decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md",
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
    docs = {path: read(root, path) for path in REQUIRED_FILES if not path.endswith(".json")}
    index = json.loads(read(root, "master-plan-index.json"))

    plan = docs["MASTER_PLAN.md"]
    roadmap = docs["IMPLEMENTATION_ROADMAP.md"]
    current = docs["CURRENT_STATE.md"]
    handoff = docs["AI_HANDOFF.md"]
    acceptance = docs["planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md"]
    binding = docs[BINDING_PATH]
    p01 = docs["planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md"]
    decision = docs["decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md"]

    require("Version: 1.1.0" in plan, "Master Plan 1.1.0 authority missing")
    require("Version: 1.1.0" in roadmap, "roadmap 1.1.0 authority missing")
    require("Status: accepted" in decision, "ADR-0037 is not accepted")
    require("Status: ACCEPTED COMPLETE — accepted-state proof and operative merge bound" in acceptance, "acceptance record is not bound")
    require("Status: OPERATIVE ACCEPTANCE BOUND" in binding, "operative binding status missing")

    all_tokens = [
        SOURCE_HEAD,
        SOURCE_MERGE,
        CANDIDATE_HEAD,
        CANDIDATE_MERGE,
        ACCEPTED_HEAD,
        ACCEPTED_RUN,
        ACCEPTED_ARTIFACT,
        ACCEPTED_ARTIFACT_DIGEST,
        ACCEPTED_VALIDATION_SHA,
        ACCEPTED_REGRESSION_SHA,
        OPERATIVE_MERGE,
        BINDING_PATH,
    ]
    for token in all_tokens:
        require(token in binding, f"binding record missing: {token}")

    for token in [
        ACCEPTED_HEAD,
        ACCEPTED_RUN,
        ACCEPTED_ARTIFACT,
        ACCEPTED_ARTIFACT_DIGEST,
        ACCEPTED_VALIDATION_SHA,
        ACCEPTED_REGRESSION_SHA,
        OPERATIVE_MERGE,
        BINDING_PATH,
    ]:
        require(token in acceptance, f"acceptance record missing binding: {token}")

    require(
        f"- accepted-state exact head: `{ACCEPTED_HEAD}`;" in handoff,
        "handoff current accepted exact head missing",
    )
    require(
        f"- accepted-state workflow run: `{ACCEPTED_RUN}`;" in handoff,
        "handoff current accepted workflow run missing",
    )
    require(
        f"- accepted-state artifact: `{ACCEPTED_ARTIFACT}`;" in handoff,
        "handoff current accepted artifact missing",
    )
    require(
        f"artifact digest: {ACCEPTED_ARTIFACT_DIGEST}" in handoff,
        "handoff accepted artifact digest missing",
    )
    require(
        f"validation SHA-256: {ACCEPTED_VALIDATION_SHA}" in handoff,
        "handoff accepted validation digest missing",
    )
    require(
        f"regression SHA-256: {ACCEPTED_REGRESSION_SHA}" in handoff,
        "handoff accepted regression digest missing",
    )
    require(
        f"- planning-load acceptance merge: `{OPERATIVE_MERGE}`;" in handoff,
        "handoff current operative acceptance merge missing",
    )
    require(
        f"operative binding: {BINDING_PATH}" in handoff,
        "handoff operative binding path missing",
    )

    require("P01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST" in current, "P01 active blocked state missing")
    require("physical-host collection: NOT STARTED" in current, "physical collection must remain not started")
    require("ADR-0033: PROPOSED" in current, "ADR-0033 must remain proposed")
    require("**Runtime implementation:** NOT AUTHORIZED" in current, "runtime non-authorization missing")
    require("**Runtime implementation:** AUTHORIZED" not in current, "runtime authorized prematurely")
    require("Status: CONFIRMED, non-authorizing" in p01, "P01 proof commit not confirmed")
    require(PROOF_COMMIT in p01, "confirmed P01 proof commit missing")

    record = index.get("phase0c19_deep_workspace_reconciliation")
    require(isinstance(record, dict), "machine Phase 0C-19 record missing")
    expected = {
        "status": "accepted_complete",
        "candidate_merge": CANDIDATE_MERGE,
        "accepted_state_exact_head": ACCEPTED_HEAD,
        "accepted_state_workflow_run": ACCEPTED_RUN,
        "accepted_state_artifact_id": ACCEPTED_ARTIFACT,
        "accepted_state_artifact_digest": ACCEPTED_ARTIFACT_DIGEST,
        "accepted_state_validation_sha256": ACCEPTED_VALIDATION_SHA,
        "accepted_state_regression_sha256": ACCEPTED_REGRESSION_SHA,
        "operative_acceptance_merge": OPERATIVE_MERGE,
        "operative_binding": BINDING_PATH,
        "accepted_state_proof_pending": False,
        "operative_acceptance_merge_pending": False,
        "confirmed_proof_commit": PROOF_COMMIT,
        "proof_commit_confirmed": True,
        "physical_host_collection_started": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
    }
    for key, value in expected.items():
        require(record.get(key) == value, f"machine binding mismatch: {key}")

    require(index.get("active_work_unit") == "P01-physical-host-and-ADR-0033-closure", "active work unit is not P01")
    require(index.get("runtime_implementation_authorized") is False, "global runtime authorized")
    require(BINDING_PATH in index.get("recovery_order", []), "operative binding missing from recovery order")
    for key in ["master_plan", "implementation_roadmap"]:
        plan_record = index.get("plan_documents", {}).get(key, {})
        require(plan_record.get("version") == "1.1.0", f"{key} version mismatch")
        require(plan_record.get("phase0c19_operative_acceptance_merge") == OPERATIVE_MERGE, f"{key} operative merge binding missing")

    require("ADR-0037: ACCEPTED" in binding, "binding lacks ADR-0037 authority")
    require("Phase 0C-19: COMPLETE" in binding, "binding lacks Phase 0C-19 completion")
    require("physical-host collection: NOT STARTED" in binding, "binding starts physical collection")
    require("ADR-0033: PROPOSED" in binding, "binding accepts ADR-0033")
    require("Runtime implementation: NOT AUTHORIZED" in binding, "binding authorizes runtime")

    return {
        "record_type": "ptah.phase0c19.deep_workspace_roadmap_operative_binding_validation",
        "status": "operative_binding_valid_non_authorizing",
        "master_plan_version": "1.1.0",
        "implementation_roadmap_version": "1.1.0",
        "adr_0037_accepted": True,
        "phase0c19_complete": True,
        "operative_acceptance_merge": OPERATIVE_MERGE,
        "confirmed_proof_commit": PROOF_COMMIT,
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
