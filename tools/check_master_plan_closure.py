#!/usr/bin/env python3
"""Validate the Phase 0C-16 Master Plan and implementation-roadmap closure."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

EXPECTED_HOST = {
    "os": "Ubuntu Server 24.04.4 LTS",
    "architecture": "x86_64",
    "kernel": "6.8.0-136-generic",
}
EXPECTED_PROOF_COMMAND = (
    "python3 tools/run_pinned_host_proof.py \\\n"
    "  --repo-root . \\\n"
    "  --output evidence/phase0c/pinned-host-candidate"
)
EXPECTED_RETENTION_COMMAND = (
    "python3 tools/retain_verified_pinned_host_evidence.py \\\n"
    "  --repo-root . \\\n"
    "  --bundle-dir evidence/phase0c/pinned-host-candidate \\\n"
    "  --output-dir evidence/phase0c/pinned-host-durable-candidate"
)
EXPECTED_PROGRAMME_A = [f"A{i:02d}" for i in range(1, 16)]
EXPECTED_WPS = [f"WP{i:02d}" for i in range(1, 15)]
EXPECTED_PHASE0C = [f"0C-{i:02d}" for i in range(1, 17)]


class ClosureError(RuntimeError):
    """Raised when the planning closure violates its accepted boundary."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ClosureError(message)


def require_text(text: str, needle: str, label: str) -> None:
    require(needle in text, f"{label}: missing required text: {needle}")


def require_absent(text: str, needle: str, label: str) -> None:
    require(needle not in text, f"{label}: forbidden text present: {needle}")


def read_text(root: Path, relative: str) -> str:
    path = root / relative
    require(path.is_file(), f"required file missing: {relative}")
    return path.read_text(encoding="utf-8")


def read_json(root: Path, relative: str) -> dict[str, Any]:
    path = root / relative
    require(path.is_file(), f"required file missing: {relative}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ClosureError(f"invalid JSON: {relative}") from exc
    require(isinstance(value, dict), f"top-level JSON object required: {relative}")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def positions(text: str, tokens: list[str], label: str) -> list[int]:
    found: list[int] = []
    for token in tokens:
        count = text.count(token)
        require(count == 1, f"{label}: expected one occurrence of {token}, found {count}")
        found.append(text.index(token))
    require(found == sorted(found), f"{label}: required order is not preserved")
    return found


def validate(root: Path) -> dict[str, Any]:
    root = root.resolve()
    required_files = [
        "README.md",
        "AI_HANDOFF.md",
        "CURRENT_STATE.md",
        "MASTER_PLAN.md",
        "IMPLEMENTATION_ROADMAP.md",
        "MASTER_ROADMAP.md",
        "PROGRESS.md",
        "DECISIONS.md",
        "MEMORY_PROTOCOL.md",
        "DONOR_RECOVERY.md",
        "master-plan-index.json",
        "planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md",
        "planning/MASTER-PLAN-RECONCILIATION.md",
        "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md",
        "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md",
        "decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md",
        "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md",
    ]
    for relative in required_files:
        require((root / relative).is_file(), f"required file missing: {relative}")

    readme = read_text(root, "README.md")
    handoff = read_text(root, "AI_HANDOFF.md")
    current = read_text(root, "CURRENT_STATE.md")
    master = read_text(root, "MASTER_PLAN.md")
    roadmap = read_text(root, "IMPLEMENTATION_ROADMAP.md")
    historical = read_text(root, "MASTER_ROADMAP.md")
    progress = read_text(root, "PROGRESS.md")
    decisions = read_text(root, "DECISIONS.md")
    memory = read_text(root, "MEMORY_PROTOCOL.md")
    donors = read_text(root, "DONOR_RECOVERY.md")
    recovery = read_text(root, "planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md")
    reconciliation = read_text(root, "planning/MASTER-PLAN-RECONCILIATION.md")
    closure = read_text(root, "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md")
    adr33 = read_text(root, "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")
    adr34 = read_text(root, "decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md")
    wp16 = read_text(root, "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md")
    index = read_json(root, "master-plan-index.json")

    # Non-authorization and current state.
    require_text(current, "**Active work unit:** 0C-16", "CURRENT_STATE")
    require_text(current, "**Runtime implementation:** NOT AUTHORIZED", "CURRENT_STATE")
    require_absent(current, "**Runtime implementation:** AUTHORIZED", "CURRENT_STATE")
    require_text(current, EXPECTED_PROOF_COMMAND, "CURRENT_STATE proof command")
    require_text(current, EXPECTED_RETENTION_COMMAND, "CURRENT_STATE retention command")
    require_text(current, "acceptance of the complete Master Plan", "CURRENT_STATE blockers")
    require_text(current, "acceptance of ADR-0033", "CURRENT_STATE blockers")

    require(index.get("record_type") == "ptah.master_plan_index", "master-plan index record type mismatch")
    require(index.get("phase") == "0C", "master-plan index phase mismatch")
    require(index.get("active_work_unit") == "P00-master-plan-authority-closure", "master-plan index active work mismatch")
    require(index.get("runtime_implementation_authorized") is False, "master-plan index cannot authorize runtime")
    host = index.get("physical_host_target")
    require(isinstance(host, dict), "physical host target missing from master-plan index")
    for key, value in EXPECTED_HOST.items():
        require(host.get(key) == value, f"physical host target mismatch: {key}")
    require(host.get("proof_command") == EXPECTED_PROOF_COMMAND.replace(" \\\n  ", " "), "index proof command mismatch")
    require(host.get("retention_command") == EXPECTED_RETENTION_COMMAND.replace(" \\\n  ", " "), "index retention command mismatch")
    blockers = index.get("authorization_blockers")
    require(isinstance(blockers, list) and len(blockers) == 7, "authorization blocker set must contain seven entries")
    require("review_and_merge_master_plan_closure" in blockers, "planning closure blocker missing")
    require("ADR_0033_acceptance" in blockers, "ADR-0033 blocker missing")

    # Master Plan scope.
    require_text(master, "Version: 1.0-candidate", "MASTER_PLAN")
    require_text(master, "Status: candidate master plan for review", "MASTER_PLAN")
    for heading in [
        "## 3. Problem Ptah solves",
        "## 5. Intended users and participants",
        "## 6. Product scope",
        "## 8. Operating modes",
        "## 10. Data, storage and memory architecture",
        "## 11. Context compiler and agent handoff",
        "## 13. Security, privacy and authority",
        "## 17. Operations and service ownership",
        "## 18. Product surfaces and release boundaries",
        "## 20. Definition of product completion",
        "## 22. Planning and implementation governance",
    ]:
        require_text(master, heading, "MASTER_PLAN scope")
    for role in ["Human owner or administrator", "Human operator", "Technician or specialist", "Hunter", "Sergeant or independent reviewer", "Replaceable software agent or model"]:
        require_text(master, role, "MASTER_PLAN roles")
    require_text(master, "Runtime implementation: **NOT AUTHORIZED**", "MASTER_PLAN boundary")

    # Detailed roadmap order and uniqueness.
    require_text(roadmap, "Version: 1.0-candidate", "IMPLEMENTATION_ROADMAP")
    positions(roadmap, ["## P00 —", "## P01 —", "# PROGRAMME A —"], "programme critical order")
    positions(roadmap, [f"## {package} —" for package in EXPECTED_PROGRAMME_A], "Programme A packages")
    positions(
        roadmap,
        [
            "# PROGRAMME B —",
            "# PROGRAMME C —",
            "# PROGRAMME D —",
            "# PROGRAMME E —",
            "# PROGRAMME F —",
        ],
        "later programmes",
    )
    require_text(roadmap, "Runtime implementation: **NOT AUTHORIZED**", "roadmap boundary")
    require_text(roadmap, "A14 — Human Alpha control surface", "roadmap human surface")
    require_text(roadmap, "A15 — Exact-head Online Ptah Alpha acceptance", "roadmap Alpha gate")

    # Frozen contract and Phase 0C reconciliation.
    for wp in EXPECTED_WPS:
        require_text(reconciliation, wp, "reconciliation WP coverage")
    for record in EXPECTED_PHASE0C:
        require_text(reconciliation, record, "reconciliation Phase 0C coverage")
    require_text(reconciliation, "introduces no new canonical Core entity", "reconciliation conclusion")
    require_text(reconciliation, "requires no immediate WP01–WP14 reopening", "reconciliation conclusion")
    for task in [f"I{i:03d}" for i in range(1, 15)]:
        require_text(reconciliation, task, "first-slice task reconciliation")

    # Recovery protocol and handoff.
    recovery_tokens = [
        "1. `AI_HANDOFF.md`",
        "2. `CURRENT_STATE.md`",
        "3. `master-plan-index.json`",
        "4. `MASTER_PLAN.md`",
        "5. `IMPLEMENTATION_ROADMAP.md`",
    ]
    positions(readme, recovery_tokens, "README recovery order")
    for number, title in [
        (1, "Mandatory recovery order"),
        (2, "Truth hierarchy"),
        (3, "Work-selection rule"),
        (4, "Work-session protocol"),
        (5, "Save-as-you-go checkpoint rule"),
        (6, "Completion language"),
        (7, "Progress updates"),
        (8, "Donor updates"),
        (9, "Public repository updates"),
        (10, "Recovery after interruption"),
        (11, "Plan and roadmap change rule"),
    ]:
        heading = f"# {number}. {title}"
        require(memory.count(heading) == 1, f"MEMORY_PROTOCOL heading invalid: {heading}")
    require_text(memory, "durably checkpointed before the full task is complete", "save-as-you-go rule")
    require_text(handoff, "phase0c-master-plan-roadmap-closure", "AI handoff branch")
    require_text(handoff, "Runtime implementation: NOT AUTHORIZED", "AI handoff boundary")
    require_text(handoff, "Safest next action", "AI handoff next action")

    # Decision and historical authority repair.
    for decision in [f"D-{i:03d}" for i in range(40, 50)]:
        require_text(decisions, decision, "DECISIONS completion")
    require_text(decisions, "ADR-0034", "DECISIONS proposed plan authority")
    require_text(donors, "COMPLETE AND FROZEN", "DONOR_RECOVERY status")
    require_absent(donors, "FINAL CONSISTENCY REVIEW ACTIVE", "DONOR_RECOVERY stale status")
    require_text(historical, "Historical Architecture and Phase Roadmap", "MASTER_ROADMAP status")
    require_text(historical, "superseded as primary planning authority", "MASTER_ROADMAP authority")

    # ADR and closure boundaries.
    require_text(adr33, "Status: proposed", "ADR-0033 status")
    require_text(adr33, "PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md", "ADR-0033 planning condition")
    require_text(adr33, "the complete `MASTER_PLAN.md`", "ADR-0033 acceptance condition")
    require_text(adr34, "Status: proposed", "ADR-0034 status")
    require_text(adr34, "Save-as-you-go rule", "ADR-0034 handoff authority")
    require_text(wp16, "Status: candidate under review", "Phase 0C-16 status")
    require_text(wp16, "Runtime implementation remains **NOT AUTHORIZED**", "Phase 0C-16 boundary")
    require_text(closure, EXPECTED_PROOF_COMMAND, "physical closure proof command")
    require_text(closure, EXPECTED_RETENTION_COMMAND, "physical closure retention command")
    for value in EXPECTED_HOST.values():
        require_text(closure, value, "physical closure host target")
    require_text(closure, "Owner intent cannot replace missing evidence", "physical closure fail-closed rule")

    # Progress and planning recovery.
    require_text(progress, "P00 — Master-plan authority closure", "PROGRESS P00")
    require_text(progress, "P01 — Physical-host and ADR-0033 closure", "PROGRESS P01")
    positions(progress, [f"A{i:02d} —" for i in range(1, 16)], "PROGRESS Programme A")
    for programme in ["Programme B", "Programme C", "Programme D", "Programme E", "Programme F"]:
        require_text(progress, programme, "PROGRESS later programme")
    require_text(recovery, "Recovered requirements and decisions: COMPLETE FOR MASTER-PLAN DRAFTING", "recovery checkpoint")
    require_text(recovery, "Runtime implementation: NOT AUTHORIZED", "recovery boundary")

    report_files: dict[str, dict[str, Any]] = {}
    for relative in required_files:
        path = root / relative
        report_files[relative] = {
            "size_bytes": path.stat().st_size,
            "sha256": sha256(path),
        }

    return {
        "schema_version": "1.0.0",
        "record_type": "ptah.phase0c.master_plan_closure_validation",
        "status": "candidate_valid_non_authorizing",
        "master_plan_version": "1.0-candidate",
        "implementation_roadmap_version": "1.0-candidate",
        "frozen_work_package_count": len(EXPECTED_WPS),
        "phase0c_record_count": len(EXPECTED_PHASE0C),
        "programme_a_package_count": len(EXPECTED_PROGRAMME_A),
        "new_core_entity_required": False,
        "frozen_contract_reopen_required": False,
        "physical_host_evidence_accepted": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "files": report_files,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = validate(args.repo_root)
    except ClosureError as exc:
        raise SystemExit(str(exc)) from exc
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
