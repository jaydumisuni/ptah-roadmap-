#!/usr/bin/env python3
"""Validate the durably bound, non-authorizing Archive Campaign 001 state."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

CANDIDATE = {
    "candidate_exact_head":"6eed78a9acca4614d9dd99c175681ba4ff476c8e",
    "candidate_workflow_run":"30076705760",
    "candidate_artifact_id":"8590135926",
    "candidate_artifact_digest":"sha256:c7e3a9be59b5ba859b67a1b352fee32b2c43c44e774e3e70b07aaac857d8b3a7",
    "candidate_validation_report_sha256":"7a53cdccfb520cbc29dfb842b952dbcbca5800f02ed1ce2a67b8a3743180d247",
    "candidate_merge":"ec78db9ce5b44a5d05465a1cb6271c7e6594079e",
}
ACCEPTED = {
    "accepted_state_exact_head":"03e027b5b2898b096652688157623ad31d3c16d7",
    "accepted_state_workflow_run":"30078410676",
    "accepted_state_artifact_id":"8590777774",
    "accepted_state_artifact_digest":"sha256:9a9948862f7c8af5f6551a239a19091c2e37a5565442be0ff9c90459932a2398",
    "accepted_state_validation_report_sha256":"f78ebcbe2781480ce90472b5d373cc282cb13628acc3e7dcc853f8abe6ebab7f",
    "operative_acceptance_merge":"f7280e4af1323096196ab0534e5f76b9375fd6d7",
}
EXPECTED = {
    "AF01":(10,9,1), "AF02":(10,10,0), "AF03":(10,10,0),
    "AF04":(10,10,0), "AF05":(10,9,1), "AF06":(10,10,0),
    "AF07":(10,10,0), "AF08":(10,10,0), "AF09":(10,10,0),
    "AF10":(8,3,5),
}
BLOCKED_IDS = ["D047","D065","I018","I008","I019","I024","I025"]
SERGEANT_RESULT = "pass_with_mandatory_retained_restrictions"
HISTORICAL_FORMATIONS = {"AF01", "AF02", "AF03"}

class ValidationError(RuntimeError):
    pass

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)

def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValidationError(f"cannot load {path}: {exc}") from exc

def validate(root: Path) -> dict[str, Any]:
    state_path = root / "archive/campaign-001/OPERATIVE-STATE.json"
    binding_path = root / "archive/campaign-001/OPERATIVE-BINDING.md"
    campaign_acceptance_path = root / "archive/campaign-001/ACCEPTANCE.md"
    manifest_path = root / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md"
    for path in (state_path, binding_path, campaign_acceptance_path, manifest_path):
        require(path.is_file(), f"missing operative campaign file: {path}")

    state = load_json(state_path)
    require(state.get("status") == "accepted_complete_non_authorizing", "operative campaign status invalid")
    expected_state = {
        "formation_count":10,
        "completed_formation_count":10,
        "obligation_count":98,
        "accepted_archive_record_count":91,
        "blocked_completed_outcome_count":7,
        "remaining_evidence_count":0,
        "blocked_record_ids":BLOCKED_IDS,
        "af11_exists":False,
        "phase_0a_reopened":False,
        "p01_closed":False,
        "adr_0033_accepted":False,
        "runtime_implementation_authorized":False,
        "operative_binding_record":"archive/campaign-001/OPERATIVE-BINDING.md",
        "campaign_acceptance_record":"archive/campaign-001/ACCEPTANCE.md",
    }
    for key, value in {**CANDIDATE, **ACCEPTED, **expected_state}.items():
        require(state.get(key) == value, f"operative state mismatch: {key}")

    binding = binding_path.read_text(encoding="utf-8")
    campaign_acceptance = campaign_acceptance_path.read_text(encoding="utf-8")
    manifest = manifest_path.read_text(encoding="utf-8")
    for token in (
        "Status: OPERATIVE ACCEPTANCE MERGE BOUND — RECOVERY CONTROL STATE",
        CANDIDATE["candidate_exact_head"], CANDIDATE["candidate_workflow_run"],
        CANDIDATE["candidate_artifact_id"], CANDIDATE["candidate_artifact_digest"],
        CANDIDATE["candidate_validation_report_sha256"], CANDIDATE["candidate_merge"],
        ACCEPTED["accepted_state_exact_head"], ACCEPTED["accepted_state_workflow_run"],
        ACCEPTED["accepted_state_artifact_id"], ACCEPTED["accepted_state_artifact_digest"],
        ACCEPTED["accepted_state_validation_report_sha256"], ACCEPTED["operative_acceptance_merge"],
        "formations: `10 of 10 accepted complete`", "obligations: `98 of 98 closed`",
        "accepted archive records: `91`", "completed blocked outcomes: `7`",
        "P01 remains the active physical pinned-host work", "ADR-0033 remains proposed",
        "Runtime implementation remains `NOT AUTHORIZED`",
    ):
        require(token in binding, f"operative binding missing: {token}")

    for token in (
        "Status: ACCEPTED COMPLETE — OPERATIVE MERGE BOUND",
        ACCEPTED["accepted_state_exact_head"], ACCEPTED["accepted_state_workflow_run"],
        ACCEPTED["accepted_state_artifact_id"], ACCEPTED["accepted_state_artifact_digest"],
        ACCEPTED["accepted_state_validation_report_sha256"], ACCEPTED["operative_acceptance_merge"],
        "obligations closed: `98 of 98`", "accepted archive records: `91`",
        "completed blocked outcomes: `7`", "completed formations: `10 of 10`",
        "P01 remains the active physical-host authorization work",
        "Runtime implementation remains `NOT AUTHORIZED`",
    ):
        require(token in campaign_acceptance, f"campaign acceptance missing: {token}")

    manifest_tokens = (
        "Status: ACCEPTED COMPLETE — 98 obligations closed, non-authorizing archive authority",
        "- completed formations: 10", "- accepted archive records: 91",
        "- blocked completed outcomes: 7", "- remaining evidence: 0",
        "- next formation: NONE — AF11 DOES NOT EXIST",
        "- operative state: `archive/campaign-001/OPERATIVE-STATE.json`",
        "- operative binding: `archive/campaign-001/OPERATIVE-BINDING.md`",
    )
    for token in manifest_tokens:
        require(token in manifest, f"manifest missing: {token}")
    require(manifest.count("- status: ACCEPTED COMPLETE") == 10, "manifest does not accept exactly ten formations")
    require("READY / NOT STARTED" not in manifest, "stale ready formation remains in operative manifest")

    total_assigned = total_accepted = total_blocked = 0
    all_ids: list[str] = []
    all_primaries: list[str] = []
    all_verifiers: list[str] = []
    observed_blocked: list[str] = []
    formation_summary: dict[str, Any] = {}

    state_formations = state.get("formations")
    require(isinstance(state_formations, dict) and set(state_formations) == set(EXPECTED), "operative formation map mismatch")

    for formation, (assigned, accepted, blocked) in EXPECTED.items():
        lower = formation.lower()
        result_path = root / f"archive/campaign-001/{lower}/RESULT.json"
        acceptance_path = root / f"archive/campaign-001/{lower}/ACCEPTANCE.md"
        require(result_path.is_file(), f"{formation}: result missing")
        require(acceptance_path.is_file(), f"{formation}: acceptance missing")
        result = load_json(result_path)
        require(result.get("formation_id") == formation, f"{formation}: identity mismatch")
        require(result.get("status") == "accepted_complete_non_authorizing", f"{formation}: not accepted")
        require(result.get("assigned_record_count") == assigned, f"{formation}: assigned count mismatch")
        require(result.get("reconciled_record_count") == assigned, f"{formation}: reconciled count mismatch")
        require(result.get("accepted_archive_record_count") == accepted, f"{formation}: accepted count mismatch")
        require(result.get("blocked_record_count") == blocked, f"{formation}: blocked count mismatch")
        require(result.get("remaining_evidence_count") == 0, f"{formation}: evidence remains")
        require(result.get("phase_0a_reopened") is False, f"{formation}: Phase 0A reopened")
        require(result.get("adr_0033_accepted") is False, f"{formation}: ADR accepted prematurely")
        require(result.get("runtime_implementation_authorized") is False, f"{formation}: runtime authorized prematurely")
        mapped = state_formations.get(formation)
        require(mapped.get("status") == "accepted_complete", f"{formation}: operative map status mismatch")
        require(mapped.get("accepted") == accepted and mapped.get("blocked") == blocked and mapped.get("remaining") == 0, f"{formation}: operative map counts mismatch")

        acceptance_text = acceptance_path.read_text(encoding="utf-8")
        if formation not in HISTORICAL_FORMATIONS:
            for token in (
                "Status: ACCEPTED COMPLETE — OPERATIVE MERGE BOUND",
                ACCEPTED["accepted_state_exact_head"], ACCEPTED["accepted_state_workflow_run"],
                ACCEPTED["accepted_state_artifact_id"], ACCEPTED["accepted_state_artifact_digest"],
                ACCEPTED["accepted_state_validation_report_sha256"], ACCEPTED["operative_acceptance_merge"],
                "P01 remains active", "ADR-0033 remains proposed",
                "Runtime implementation remains unauthorized",
                "archive/campaign-001/OPERATIVE-BINDING.md",
            ):
                require(token in acceptance_text, f"{formation}: bound acceptance missing: {token}")

        records = result.get("records")
        require(isinstance(records, list) and len(records) == assigned, f"{formation}: record list mismatch")
        require(len({r.get('id') for r in records}) == assigned, f"{formation}: duplicate record IDs")
        require(len({r.get('primary') for r in records}) == assigned, f"{formation}: primary IDs reused")
        require(len({r.get('verifier') for r in records}) == assigned, f"{formation}: verifier IDs reused")
        require({r.get('primary') for r in records}.isdisjoint({r.get('verifier') for r in records}), f"{formation}: worker independence collapsed")
        local_blocked = 0
        for record in records:
            record_id = str(record.get("id"))
            record_path = root / str(record.get("path", ""))
            require(record_path.is_file(), f"{formation}/{record_id}: record missing")
            text = record_path.read_text(encoding="utf-8")
            if formation not in HISTORICAL_FORMATIONS:
                require(str(record.get("outcome")) in text, f"{formation}/{record_id}: outcome mismatch")
                require("does not authorize implementation" in text, f"{formation}/{record_id}: non-authorizing statement missing")
            outcome = str(record.get("outcome", ""))
            if outcome.startswith("blocked_"):
                local_blocked += 1
                observed_blocked.append(record_id)
                if formation in HISTORICAL_FORMATIONS:
                    require("## Reopening criteria" in text and "prohibited" in text, f"{formation}/{record_id}: unsafe historical block")
                else:
                    require("Safe next action" in text and "prohibited" in text, f"{formation}/{record_id}: unsafe block")
            all_ids.append(record_id)
            all_primaries.append(str(record.get("primary")))
            all_verifiers.append(str(record.get("verifier")))
        require(local_blocked == blocked, f"{formation}: observed blocked count mismatch")

        total_assigned += assigned
        total_accepted += accepted
        total_blocked += blocked
        formation_summary[formation] = {"assigned":assigned,"accepted":accepted,"blocked":blocked,"remaining":0}

    require(total_assigned == 98, "campaign assigned total mismatch")
    require(total_accepted == 91, "campaign accepted total mismatch")
    require(total_blocked == 7, "campaign blocked total mismatch")
    require(total_accepted + total_blocked == total_assigned, "campaign closure arithmetic mismatch")
    require(len(all_ids) == 98 and len(set(all_ids)) == 98, "campaign record identities collide")
    require(len(set(all_primaries)) == 98 and len(set(all_verifiers)) == 98, "campaign worker identities collide")
    require(set(all_primaries).isdisjoint(all_verifiers), "campaign primary/verifier independence collapsed")
    require(observed_blocked == BLOCKED_IDS, "blocked record identity/order mismatch")
    require(not (root / "archive/campaign-001/af11").exists(), "unexpected AF11")

    current = (root / "CURRENT_STATE.md").read_text(encoding="utf-8")
    require("**Active work unit:** 0C-04 / P01 — physical pinned-host proof" in current, "P01 current-state authority missing")
    require("**Runtime implementation:** NOT AUTHORIZED" in current, "runtime non-authorization missing")
    require("- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`." in current, "ADR-0033 proposed state missing")
    require("**Runtime implementation:** AUTHORIZED" not in current, "runtime authorized prematurely")

    return {
        "schema_version":"1.0.0",
        "status":"campaign_001_complete_bound_non_authorizing",
        "formation_count":10,
        "obligation_count":98,
        "accepted_archive_record_count":91,
        "blocked_completed_outcome_count":7,
        "remaining_evidence_count":0,
        "blocked_record_ids":BLOCKED_IDS,
        "candidate_exact_head":CANDIDATE["candidate_exact_head"],
        "candidate_workflow_run":CANDIDATE["candidate_workflow_run"],
        "candidate_artifact_id":CANDIDATE["candidate_artifact_id"],
        "candidate_artifact_digest":CANDIDATE["candidate_artifact_digest"],
        "candidate_validation_report_sha256":CANDIDATE["candidate_validation_report_sha256"],
        "candidate_merge":CANDIDATE["candidate_merge"],
        "accepted_state_exact_head":ACCEPTED["accepted_state_exact_head"],
        "accepted_state_workflow_run":ACCEPTED["accepted_state_workflow_run"],
        "accepted_state_artifact_id":ACCEPTED["accepted_state_artifact_id"],
        "accepted_state_artifact_digest":ACCEPTED["accepted_state_artifact_digest"],
        "accepted_state_validation_report_sha256":ACCEPTED["accepted_state_validation_report_sha256"],
        "operative_acceptance_merge":ACCEPTED["operative_acceptance_merge"],
        "phase_0a_reopened":False,
        "p01_closed":False,
        "adr_0033_accepted":False,
        "runtime_implementation_authorized":False,
        "formations":formation_summary,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        report = validate(Path(args.repo_root).resolve())
    except ValidationError as exc:
        print(f"Campaign completion validation failed: {exc}")
        return 1
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
