#!/usr/bin/env python3
"""Validate AF04-AF10 accepted-state promotion before global control-state binding."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

CANDIDATE_HEAD = "6eed78a9acca4614d9dd99c175681ba4ff476c8e"
CANDIDATE_RUN = "30076705760"
CANDIDATE_ARTIFACT = "8590135926"
CANDIDATE_DIGEST = "sha256:c7e3a9be59b5ba859b67a1b352fee32b2c43c44e774e3e70b07aaac857d8b3a7"
CANDIDATE_REPORT = "7a53cdccfb520cbc29dfb842b952dbcbca5800f02ed1ce2a67b8a3743180d247"
CANDIDATE_MERGE = "ec78db9ce5b44a5d05465a1cb6271c7e6594079e"
SERGEANT_RESULT = "pass_with_mandatory_retained_restrictions"

EXPECTED = {
    "AF04": {"assigned":10,"accepted":10,"blocked":0,"head":"ee0b78a41241a1b61a7085d6eeabf202882d2dc2"},
    "AF05": {"assigned":10,"accepted":9,"blocked":1,"head":"05975c5fbf34bd52a51ccd6ec54fd13a24dac849"},
    "AF06": {"assigned":10,"accepted":10,"blocked":0,"head":"388e3110435fe4664531756e6d9fc2d4e8910e2e"},
    "AF07": {"assigned":10,"accepted":10,"blocked":0,"head":"50b62cd8d4870eaf1a709d719a0939651fe54d80"},
    "AF08": {"assigned":10,"accepted":10,"blocked":0,"head":"e6d708798d3114b4de3230d28efb5f9a3a5733ca"},
    "AF09": {"assigned":10,"accepted":10,"blocked":0,"head":"64febc773dc62ba554a7c8a64493e84ae4d8f4b0"},
    "AF10": {"assigned":8,"accepted":3,"blocked":5,"head":"a2a58ae78b19cadf18b52e775301ed03a9d7ad67"},
}

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
    accepted = blocked = assigned = 0
    all_ids: list[str] = []
    primaries: list[str] = []
    verifiers: list[str] = []
    formations: dict[str, Any] = {}

    campaign_acceptance = root / "archive/campaign-001/ACCEPTANCE.md"
    require(campaign_acceptance.is_file(), "campaign acceptance record missing")
    campaign_text = campaign_acceptance.read_text(encoding="utf-8")
    for token in (
        "Status: ACCEPTED-STATE CANDIDATE — OPERATIVE MERGE PENDING",
        CANDIDATE_HEAD, CANDIDATE_RUN, CANDIDATE_ARTIFACT, CANDIDATE_DIGEST,
        CANDIDATE_REPORT, CANDIDATE_MERGE,
        "obligations closed: `98 of 98`",
        "accepted archive records: `91`",
        "completed blocked outcomes: `7`",
        "completed formations: `10 of 10`",
        "P01 remains the active physical-host authorization work",
        "ADR-0033 remains proposed",
        "Runtime implementation remains `NOT AUTHORIZED`",
    ):
        require(token in campaign_text, f"campaign acceptance missing: {token}")

    for formation, expected in EXPECTED.items():
        base = root / "archive/campaign-001" / formation.lower()
        result = load_json(base / "RESULT.json")
        acceptance_path = base / "ACCEPTANCE.md"
        require(acceptance_path.is_file(), f"{formation}: acceptance record missing")
        acceptance_text = acceptance_path.read_text(encoding="utf-8")

        require(result.get("formation_id") == formation, f"{formation}: identity mismatch")
        require(result.get("status") == "accepted_complete_non_authorizing", f"{formation}: not promoted")
        require(result.get("assigned_record_count") == expected["assigned"], f"{formation}: assigned count mismatch")
        require(result.get("reconciled_record_count") == expected["assigned"], f"{formation}: reconciled count mismatch")
        require(result.get("accepted_archive_record_count") == expected["accepted"], f"{formation}: accepted count mismatch")
        require(result.get("blocked_record_count") == expected["blocked"], f"{formation}: blocked count mismatch")
        require(result.get("remaining_evidence_count") == 0, f"{formation}: evidence remains")
        require(result.get("sergeant_review_target_head") == expected["head"], f"{formation}: Sergeant target drift")
        require(result.get("sergeant_review_result") == SERGEANT_RESULT, f"{formation}: Sergeant result drift")
        require(result.get("sergeant_blocking_finding_count") == 0, f"{formation}: Sergeant blocker")
        require(result.get("formation_accepted") is True, f"{formation}: accepted flag missing")
        require(result.get("campaign_complete_pending_binding") is True, f"{formation}: binding state missing")
        require(result.get("phase_0a_reopened") is False, f"{formation}: Phase 0A reopened")
        require(result.get("adr_0033_accepted") is False, f"{formation}: ADR accepted prematurely")
        require(result.get("runtime_implementation_authorized") is False, f"{formation}: runtime authorized prematurely")

        expected_metadata = {
            "candidate_exact_head": CANDIDATE_HEAD,
            "candidate_workflow_run": CANDIDATE_RUN,
            "candidate_artifact_id": CANDIDATE_ARTIFACT,
            "candidate_artifact_digest": CANDIDATE_DIGEST,
            "candidate_validation_report_sha256": CANDIDATE_REPORT,
            "candidate_merge": CANDIDATE_MERGE,
            "acceptance_record": f"archive/campaign-001/{formation.lower()}/ACCEPTANCE.md",
            "campaign_acceptance_record": "archive/campaign-001/ACCEPTANCE.md",
        }
        for key, value in expected_metadata.items():
            require(result.get(key) == value, f"{formation}: candidate binding mismatch: {key}")

        for token in (
            "Status: ACCEPTED EVIDENCE RECORD — OPERATIVE MERGE PENDING",
            CANDIDATE_HEAD, CANDIDATE_RUN, CANDIDATE_ARTIFACT, CANDIDATE_DIGEST,
            CANDIDATE_REPORT, CANDIDATE_MERGE, expected["head"], SERGEANT_RESULT,
            f"{formation} status: `ACCEPTED COMPLETE`",
            "P01 remains active", "ADR-0033 remains proposed",
            "Runtime implementation remains unauthorized",
            "separately reviewed acceptance merge",
        ):
            require(token in acceptance_text, f"{formation}: acceptance record missing: {token}")

        records = result.get("records")
        require(isinstance(records, list) and len(records) == expected["assigned"], f"{formation}: record list mismatch")
        require(len({r.get('id') for r in records}) == len(records), f"{formation}: duplicate record identity")
        require(len({r.get('primary') for r in records}) == len(records), f"{formation}: primary identity reused")
        require(len({r.get('verifier') for r in records}) == len(records), f"{formation}: verifier identity reused")
        require({r.get('primary') for r in records}.isdisjoint({r.get('verifier') for r in records}), f"{formation}: worker independence collapsed")
        observed_blocked = 0
        for record in records:
            path = root / str(record.get("path", ""))
            require(path.is_file(), f"{formation}/{record.get('id')}: record missing")
            text = path.read_text(encoding="utf-8")
            require(str(record.get("outcome")) in text, f"{formation}/{record.get('id')}: outcome mismatch")
            require("does not authorize implementation" in text, f"{formation}/{record.get('id')}: non-authorization missing")
            if str(record.get("outcome", "")).startswith("blocked_"):
                observed_blocked += 1
                require("Safe next action" in text and "prohibited" in text, f"{formation}/{record.get('id')}: unsafe block")
            all_ids.append(str(record.get("id")))
            primaries.append(str(record.get("primary")))
            verifiers.append(str(record.get("verifier")))
        require(observed_blocked == expected["blocked"], f"{formation}: observed blocked mismatch")

        accepted += expected["accepted"]
        blocked += expected["blocked"]
        assigned += expected["assigned"]
        formations[formation] = {"accepted":expected["accepted"],"blocked":expected["blocked"],"remaining":0}

    require(assigned == 68 and accepted == 62 and blocked == 6, "AF04-AF10 promotion totals mismatch")
    require(len(all_ids) == 68 and len(set(all_ids)) == 68, "campaign record identity collision")
    require(len(set(primaries)) == 68 and len(set(verifiers)) == 68, "campaign worker identity collision")
    require(set(primaries).isdisjoint(verifiers), "campaign worker independence collapsed")

    for formation, counts in {"af01":(9,1),"af02":(10,0),"af03":(10,0)}.items():
        result = load_json(root / "archive/campaign-001" / formation / "RESULT.json")
        require(result.get("status") == "accepted_complete_non_authorizing", f"{formation}: accepted baseline drift")
        require(result.get("accepted_archive_record_count") == counts[0], f"{formation}: accepted count drift")
        require(result.get("blocked_record_count") == counts[1], f"{formation}: blocked count drift")

    # Global control-state binding is deliberately deferred to a recovery-only follow-up.
    current = (root / "CURRENT_STATE.md").read_text(encoding="utf-8")
    manifest = (root / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md").read_text(encoding="utf-8")
    require("**Active work unit:** 0C-04 / P01 — physical pinned-host proof" in current, "P01 current-state field missing")
    require("**Runtime implementation:** NOT AUTHORIZED" in current, "runtime non-authorization missing")
    require("- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`." in current, "ADR proposed state missing")
    require("- completed formations: 3" in manifest, "global campaign state was bound prematurely")
    require("- next formation: AF04 READY / NOT STARTED" in manifest, "global formation state was bound prematurely")
    require(not (root / "archive/campaign-001/af11").exists(), "unexpected AF11")

    return {
        "schema_version":"1.0.0",
        "status":"campaign_acceptance_candidate_valid_non_authorizing",
        "candidate_exact_head":CANDIDATE_HEAD,
        "candidate_workflow_run":CANDIDATE_RUN,
        "candidate_artifact_id":CANDIDATE_ARTIFACT,
        "candidate_artifact_digest":CANDIDATE_DIGEST,
        "candidate_validation_report_sha256":CANDIDATE_REPORT,
        "candidate_merge":CANDIDATE_MERGE,
        "promoted_formation_count":7,
        "campaign_formation_count":10,
        "campaign_obligation_count":98,
        "campaign_accepted_archive_record_count":91,
        "campaign_blocked_record_count":7,
        "campaign_remaining_evidence_count":0,
        "global_control_state_bound":False,
        "phase_0a_reopened":False,
        "p01_closed":False,
        "adr_0033_accepted":False,
        "runtime_implementation_authorized":False,
        "formations":formations,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        report = validate(Path(args.repo_root).resolve())
    except ValidationError as exc:
        print(f"Campaign acceptance validation failed: {exc}")
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
