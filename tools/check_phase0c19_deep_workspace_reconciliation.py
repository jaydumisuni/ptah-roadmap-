#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

MARKER = "PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION"

REQUIRED_FILES = [
    "MASTER_PLAN.md",
    "IMPLEMENTATION_ROADMAP.md",
    "CURRENT_STATE.md",
    "PROGRESS.md",
    "AI_HANDOFF.md",
    "DECISIONS.md",
    "master-plan-index.json",
    "planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md",
    "planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md",
    "planning/MASTER-PLAN-RECONCILIATION.md",
    "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md",
    "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md",
    "work-packages/PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION.md",
    "decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md",
]

CAPABILITIES = [
    "bounded Workspace envelope",
    "parallel Session continuity",
    "cross-device resume",
    "reusable Artifact Library",
    "external reference versus materialized Object truth",
    "typed operation catalog",
    "lazy capability-schema discovery",
    "operation effect classification",
    "external Provider permission preservation",
    "configured confirmation policy",
    "Activity progress Events",
    "partial-output and failure retention",
    "large-result stable resource handles",
    "paged and searchable result access",
    "render-independent typed Views",
    "one-off, recurring and condition-triggered schedules",
    "exact, flexible-window and condition-dependent timing modes",
    "optimistic concurrency and exact revision/head preconditions",
    "observe/draft/simulate/execute/verify lifecycle",
    "distinct declined, failed, cancelled, not-run and partial-completion result states",
    "connector source/account provenance",
    "explicit resource, Provider and product-limit reporting",
]

EFFECT_CLASSES = [
    "observe",
    "draft",
    "simulate",
    "mutate",
    "publish",
    "destructive",
    "external_side_effect",
]

AVAILABILITY_STATES = [
    "external_reference",
    "indexed_reference",
    "mounted_read_only",
    "materialized_copy",
    "generated_artifact",
]

RESULT_STATES = [
    "succeeded",
    "failed",
    "declined",
    "cancelled",
    "not_run",
    "partially_completed",
]

SCHEDULE_KINDS = ["one_off", "recurring", "condition_watch"]
TIMING_MODES = ["exact", "flexible_window", "condition_dependent"]

PACKAGE_IDS = [
    "A01", "A02", "A04", "A06", "A07", "A08", "A09", "A11", "A13", "A14", "A15",
    "B01", "B06", "B07",
    "D01", "D02", "D03", "D04", "D09",
    "E04", "E06", "E07",
    "X1", "X2", "X3", "X4", "X5",
]


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def load_text(root: Path, path: str) -> str:
    target = root / path
    require(target.is_file(), f"missing required file: {path}")
    return target.read_text(encoding="utf-8")


def validate(root: Path) -> dict[str, Any]:
    texts = {path: load_text(root, path) for path in REQUIRED_FILES if not path.endswith(".json")}
    index = json.loads(load_text(root, "master-plan-index.json"))

    study = texts["planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md"]
    plan = texts["MASTER_PLAN.md"]
    roadmap = texts["IMPLEMENTATION_ROADMAP.md"]
    state = texts["CURRENT_STATE.md"]
    handoff = texts["AI_HANDOFF.md"]
    decision = texts["decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md"]
    package = texts["work-packages/PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION.md"]
    p01 = texts["planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md"]

    for path in ["MASTER_PLAN.md", "IMPLEMENTATION_ROADMAP.md", "CURRENT_STATE.md", "AI_HANDOFF.md"]:
        require(MARKER in texts[path], f"{path}: missing Phase 0C-19 marker")

    require("23dc4b19a0189ba55e08dfa124761efa806bd68b" in study, "missing source merge")
    require("bf4ae98b9d492ad688644fd6a330aaf435ac70c1" in study, "missing source exact head")
    require("30087967851" in study and "8594496859" in study, "missing source run/artifact")
    require("sha256:aea4fde3f600a6e4c3fc2f6ff3614918a5f714c6f8ebbf6ab3fb3cb29ccaf12b" in study, "missing source artifact digest")
    require("329262e7bb12e0841f1884664e713ab8e55a58e45a2430d4abf77ccdde65ecbe" in study, "missing source validation digest")

    for capability in CAPABILITIES:
        require(capability in study, f"missing capability: {capability}")
    for token in EFFECT_CLASSES + AVAILABILITY_STATES + RESULT_STATES + SCHEDULE_KINDS + TIMING_MODES:
        require(token in study or token in plan or token in roadmap, f"missing required vocabulary: {token}")

    require("### 6.6 Deep Workspace operations profile" in plan, "Master Plan profile section missing")
    require("Operational truth must be explicit" in plan, "Master Plan operational-truth principle missing")
    require("No new Core entity family is introduced" in plan, "Master Plan no-Core-extension conclusion missing")

    require("# 8. Phase 0C-19 candidate amendments to the delivery load" in roadmap, "roadmap candidate amendment section missing")
    for package_id in PACKAGE_IDS:
        require(package_id in roadmap, f"roadmap mapping missing: {package_id}")
    require("operation effect class, exact precondition" in roadmap, "universal work-package gate not deepened")

    for phrase in [
        "Provider access, Ptah Grant and human/application approval remain separate",
        "Retry creates a new Attempt",
        "View style never creates authority",
        "Ptah cannot gain semantic context, review, approval, acceptance or next-action authority",
    ]:
        require(phrase in study or phrase in roadmap or phrase in decision, f"missing boundary: {phrase}")

    require("Status: proposed" in decision, "ADR-0037 must remain proposed in candidate")
    require("Status: CANDIDATE / IN REVIEW" in package, "Phase 0C-19 candidate status missing")
    require("P01: PAUSED" in state, "P01 pause missing")
    require("ADR-0037: PROPOSED" in state, "ADR-0037 proposed state missing")
    require("physical-host collection: NOT STARTED" in state, "physical-host not-started boundary missing")
    require("**Runtime implementation:** NOT AUTHORIZED" in state, "runtime authorization boundary changed")
    require("ADR-0033: PROPOSED" in state, "ADR-0033 must remain proposed")
    require("provisional" in p01.lower(), "P01 selected commit must be provisional")
    require("Do not run physical-host collection" in p01, "P01 pause instruction missing")
    require("P01 is paused" in handoff or "P01: PAUSED" in handoff, "handoff does not pause P01")

    candidate = index.get("phase0c19_deep_workspace_reconciliation")
    require(isinstance(candidate, dict), "machine candidate record missing")
    require(candidate.get("status") == "candidate_in_review", "machine candidate status mismatch")
    require(candidate.get("mechanical_capability_count") == 22, "machine capability count mismatch")
    require(candidate.get("mapping_count") == 28, "machine mapping count mismatch")
    require(candidate.get("fixture_count") == 20, "machine fixture count mismatch")
    require(candidate.get("original_regression_count") == 26, "machine regression count mismatch")
    require(candidate.get("new_core_entity_required") is False, "new Core entity must remain false")
    require(candidate.get("frozen_contract_reopen_required") is False, "contract reopen must remain false")
    require(candidate.get("p01_paused") is True, "machine P01 pause missing")
    require(candidate.get("physical_host_collection_started") is False, "physical collection must remain false")
    require(candidate.get("adr_0033_accepted") is False, "ADR-0033 accepted prematurely")
    require(candidate.get("runtime_implementation_authorized") is False, "runtime authorized prematurely")
    require(index.get("runtime_implementation_authorized") is False, "global runtime authorized prematurely")
    require(index.get("active_work_unit") == "Phase-0C-19-deep-workspace-roadmap-reconciliation", "active work unit mismatch")

    require("Hunter or another caller" in plan and "Sergeant" in plan, "participant boundary missing")
    require("Ptah may not" in decision and "choose the caller's job" in decision, "Ptah authority prohibition missing")
    require("new Core entity required: false" in study, "human no-Core conclusion missing")
    require("WP01-WP14 reopening required: false" in study, "human contract-reopen conclusion missing")

    return {
        "record_type": "ptah.phase0c19.deep_workspace_roadmap_reconciliation_validation",
        "status": "candidate_valid_non_authorizing",
        "source_merge": "23dc4b19a0189ba55e08dfa124761efa806bd68b",
        "mechanical_capability_count": 22,
        "roadmap_mapping_count": len(PACKAGE_IDS),
        "new_core_entity_required": False,
        "frozen_contract_reopen_required": False,
        "p01_paused": True,
        "physical_host_collection_started": False,
        "adr_0037_status": "proposed",
        "adr_0033_status": "proposed",
        "runtime_implementation_authorized": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    report = validate(Path(args.repo_root).resolve())
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(encoded, encoding="utf-8")
    print(encoded, end="")


if __name__ == "__main__":
    main()
