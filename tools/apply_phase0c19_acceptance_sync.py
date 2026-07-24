#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF_COMMIT = "23dc4b19a0189ba55e08dfa124761efa806bd68b"
CANDIDATE_MERGE = "96d0d465fe74fb1ac2e469b69bfb3326d7d65138"


class SyncError(RuntimeError):
    pass


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one source fragment, found {count}")
    return text.replace(old, new, 1)


def update_master_plan() -> None:
    path = "MASTER_PLAN.md"
    text = read(path)
    text = replace_once(text, "Version: 1.0.0", "Version: 1.1.0", "Master Plan version")
    text = replace_once(
        text,
        "## 23. Phase 0C-19 candidate planning-load supplement",
        "## 23. Accepted Phase 0C-19 planning-load supplement",
        "Master Plan Phase 0C-19 heading",
    )
    text = replace_once(
        text,
        "The deep Workspace operations study is reconciled through `planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md` as a candidate supplement to accepted version `1.0.0`.",
        "The deep Workspace operations study is accepted through ADR-0037 and `planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md` as part of operative version `1.1.0`.",
        "Master Plan supplement authority",
    )
    text = replace_once(
        text,
        "It adds implementation and proof detail only. It does not change Ptah's identity, add a Core family, reopen WP01–WP14, accept ADR-0033 or authorize runtime implementation. A separate ADR-0037 acceptance change is required before this supplement becomes operative version `1.1.0`.",
        "It adds implementation and proof detail only. It does not change Ptah's identity, add a Core family, reopen WP01–WP14, accept ADR-0033 or authorize runtime implementation. ADR-0037 makes the supplement operative while retaining every independent physical-host and runtime gate.",
        "Master Plan acceptance boundary",
    )
    write(path, text)


def update_roadmap() -> None:
    path = "IMPLEMENTATION_ROADMAP.md"
    text = read(path)
    text = replace_once(text, "Version: 1.0.0", "Version: 1.1.0", "roadmap version")
    text = replace_once(
        text,
        "# 8. Phase 0C-19 candidate amendments to the delivery load",
        "# 8. Accepted Phase 0C-19 amendments to the delivery load",
        "roadmap Phase 0C-19 heading",
    )
    text = replace_once(
        text,
        "Status: candidate supplement; accepted roadmap version `1.0.0` remains operative until ADR-0037 acceptance.",
        "Status: accepted supplement under ADR-0037; roadmap version `1.1.0` is operative.",
        "roadmap supplement status",
    )
    text = replace_once(
        text,
        "P01 is paused while this candidate is reviewed. Roadmap PR #46's selected `Ptah-space` commit remains provisional. After ADR-0037 acceptance, a reviewed change must confirm or supersede that commit before physical-host collection begins.",
        f"P01 resumes after ADR-0037 acceptance. The `Ptah-space` main head remains `{PROOF_COMMIT}` and is confirmed as the exact non-runtime physical-proof candidate. Physical-host collection has not started.",
        "roadmap P01 sequencing",
    )
    text = replace_once(
        text,
        "Phase 0C-19: CANDIDATE\nADR-0037: PROPOSED\nP01: PAUSED\nADR-0033: PROPOSED\nRuntime implementation: NOT AUTHORIZED",
        "Phase 0C-19: COMPLETE\nADR-0037: ACCEPTED\nP01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST\nphysical-host collection: NOT STARTED\nADR-0033: PROPOSED\nRuntime implementation: NOT AUTHORIZED",
        "roadmap control state",
    )
    write(path, text)


def update_decision() -> None:
    path = "decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md"
    text = read(path)
    text = replace_once(text, "Status: proposed", "Status: accepted", "ADR-0037 status")
    text = replace_once(
        text,
        "## Proposed decision",
        "## Accepted decision",
        "ADR-0037 decision heading",
    )
    text = replace_once(
        text,
        "The accepted change, if approved later, will:",
        "The accepted change:",
        "ADR-0037 future language",
    )
    text = replace_once(
        text,
        "During this proposed decision:",
        "Before acceptance, the candidate state was:",
        "ADR-0037 P01 history",
    )
    text = replace_once(
        text,
        "After ADR-0037 acceptance, the selected commit must be confirmed or superseded in a reviewed change before the physical proof command runs.",
        f"At acceptance, `Ptah-space` main remains `{PROOF_COMMIT}` with no newer preparation commit. The selected commit is confirmed. Physical-host collection remains not started.",
        "ADR-0037 proof confirmation",
    )
    text = replace_once(
        text,
        "## Conditions before acceptance",
        "## Acceptance evidence and preserved gates",
        "ADR-0037 conditions heading",
    )
    text = replace_once(
        text,
        "ADR-0037 remains proposed until:",
        f"ADR-0037 is accepted after candidate exact-head validation and candidate merge `{CANDIDATE_MERGE}`. The accepted-state proof and operative merge are recorded separately before P01 execution.",
        "ADR-0037 conditions text",
    )
    text = replace_once(
        text,
        "ADR-0037: PROPOSED\nPhase 0C-19: CANDIDATE\nP01: PAUSED\nADR-0033: PROPOSED\nRuntime implementation: NOT AUTHORIZED",
        f"ADR-0037: ACCEPTED\nPhase 0C-19: COMPLETE\nMaster Plan / roadmap: 1.1.0 / ACCEPTED\nP01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST\nP01 proof commit: CONFIRMED — {PROOF_COMMIT}\nphysical-host collection: NOT STARTED\nADR-0033: PROPOSED\nRuntime implementation: NOT AUTHORIZED",
        "ADR-0037 current boundary",
    )
    write(path, text)


def update_work_package() -> None:
    path = "work-packages/PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION.md"
    text = read(path)
    text = replace_once(text, "Status: CANDIDATE / IN REVIEW", "Status: COMPLETE / ACCEPTED", "Phase 0C-19 status")
    text = replace_once(
        text,
        "## Required candidate state",
        "## Accepted state",
        "Phase 0C-19 state heading",
    )
    text = replace_once(
        text,
        "- Phase 0C-19 is candidate/in review;\n- ADR-0037 remains proposed;\n- Master Plan/roadmap `1.0.0` remain the accepted authority until a separate acceptance change;",
        "- Phase 0C-19 is complete and accepted;\n- ADR-0037 is accepted;\n- Master Plan/roadmap `1.1.0` are the accepted authorities;",
        "Phase 0C-19 accepted authority",
    )
    text = replace_once(
        text,
        "- P01 is paused pending reconciliation acceptance;\n- the PR #46 candidate selection is provisional;",
        f"- P01 is active and blocked on the exact physical host;\n- the PR #46 candidate is confirmed at `{PROOF_COMMIT}`;",
        "Phase 0C-19 P01 state",
    )
    text = replace_once(
        text,
        "ADR-0037: PROPOSED\nP01: PAUSED\nADR-0033: PROPOSED\nRuntime implementation: NOT AUTHORIZED",
        "ADR-0037: ACCEPTED\nP01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST\nphysical-host collection: NOT STARTED\nADR-0033: PROPOSED\nRuntime implementation: NOT AUTHORIZED",
        "Phase 0C-19 boundary",
    )
    write(path, text)


def update_reconciliation_record() -> None:
    path = "planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md"
    text = read(path)
    text = replace_once(
        text,
        "Status: Phase 0C-19 candidate — non-operative until ADR-0037 acceptance",
        "Status: ACCEPTED OPERATIVE PLANNING SUPPLEMENT — ADR-0037 accepted",
        "deep reconciliation status",
    )
    text = replace_once(
        text,
        "That selection remains a technically suitable non-runtime candidate because it contains the deep study itself, but it is **provisional** until Phase 0C-19 and ADR-0037 are accepted. No physical-host collection should begin before acceptance.",
        f"That selection is confirmed because `Ptah-space` main remains `{PROOF_COMMIT}`, it contains the accepted study and all proof tooling, and no newer preparation commit exists. Physical-host collection has not started.",
        "deep reconciliation proof status",
    )
    text = replace_once(
        text,
        "After Phase 0C-19 acceptance:\n\n1. confirm that the same commit remains the final proof candidate, or select a newer reviewed non-runtime preparation commit;\n2. record that confirmation in the P01 selection record;\n3. only then run the exact physical-host proof.",
        "Acceptance confirms the same commit as the final proof candidate. P01 may resume, but the exact physical-host proof must still be run and independently accepted before ADR-0033 or runtime authorization can change.",
        "deep reconciliation post-acceptance sequence",
    )
    text = replace_once(
        text,
        "Phase 0C-19: CANDIDATE\nADR-0037: PROPOSED\nP01: PAUSED pending reconciliation acceptance\nADR-0033: PROPOSED\nRuntime implementation: NOT AUTHORIZED",
        f"Phase 0C-19: COMPLETE\nADR-0037: ACCEPTED\nMaster Plan / roadmap: 1.1.0 / ACCEPTED\nP01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST\nP01 proof commit: CONFIRMED — {PROOF_COMMIT}\nphysical-host collection: NOT STARTED\nADR-0033: PROPOSED\nRuntime implementation: NOT AUTHORIZED",
        "deep reconciliation conclusion",
    )
    write(path, text)


def update_current_state() -> None:
    path = "CURRENT_STATE.md"
    text = read(path)
    text = replace_once(
        text,
        "**Active work unit:** Phase 0C-19 — deep Workspace study Master Plan and roadmap reconciliation; P01 paused  ",
        "**Active work unit:** 0C-04 / P01 — physical pinned-host proof, package review, durable evidence and ADR-0033 closure  ",
        "current active work",
    )
    text = replace_once(
        text,
        "**Production dependency/backend selection:** LOCKS MERGED — DEEP WORKSPACE PLANNING LOAD IN REVIEW — PHYSICAL PINNED-HOST PROOF PAUSED  ",
        "**Production dependency/backend selection:** LOCKS MERGED — DEEP WORKSPACE PLANNING LOAD ACCEPTED — PHYSICAL PINNED-HOST PROOF OPEN  ",
        "current production state",
    )
    text = replace_once(
        text,
        "## Active Phase 0C-19 deep Workspace reconciliation",
        "## Accepted Phase 0C-19 deep Workspace reconciliation",
        "current Phase 0C-19 heading",
    )
    text = replace_once(text, "- ADR-0037: PROPOSED;", "- ADR-0037: ACCEPTED;", "current ADR-0037")
    text = replace_once(text, "- P01: PAUSED;", "- P01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST;", "current P01")
    text = replace_once(
        text,
        "- roadmap PR #46 proof-candidate selection: PROVISIONAL;",
        f"- roadmap PR #46 proof-candidate selection: CONFIRMED at `{PROOF_COMMIT}`;",
        "current proof commit",
    )
    text = replace_once(
        text,
        "prove Phase 0C-19 candidate\n→ merge candidate evidence\n→ separately accept ADR-0037 and planning version 1.1.0\n→ confirm or supersede the P01 proof commit\n→ resume physical-host closure",
        "run exact physical-host proof\n→ review package and package-artifact manifests\n→ retain and accept durable evidence\n→ complete Phase 0C closure review\n→ accept ADR-0033 and explicitly authorize runtime",
        "current immediate sequence",
    )
    text = replace_once(
        text,
        "1. Complete and exact-head validate Phase 0C-19 deep Workspace planning-load reconciliation.\n2. Merge the candidate evidence and separately accept ADR-0037 / Master Plan and roadmap version `1.1.0`.\n3. Confirm or supersede the provisional `Ptah-space` proof commit.\n4. Install or recover the exact Ubuntu Server 24.04.4 / `6.8.0-136-generic` proof host.\n5. Run:",
        f"1. Install or recover the exact Ubuntu Server 24.04.4 / `6.8.0-136-generic` proof host.\n2. Check out confirmed `Ptah-space` commit `{PROOF_COMMIT}` and verify a clean tree.\n3. Run:",
        "current continuation order",
    )
    write(path, text)


def update_progress() -> None:
    path = "PROGRESS.md"
    text = read(path)
    text = replace_once(
        text,
        "- [?] P01 — Physical-host and ADR-0033 closure; paused pending Phase 0C-19 acceptance, then blocked on the exact external host.",
        "- [?] P01 — Physical-host and ADR-0033 closure; active and blocked on the exact external host.",
        "progress P01",
    )
    text = replace_once(text, "- [-] Phase 0C-19 canonical planning synchronization in review;", "- [x] Phase 0C-19 canonical planning synchronization accepted;", "progress Phase 0C-19")
    text = replace_once(text, "- [-] ADR-0037 proposed;", "- [x] ADR-0037 accepted;", "progress ADR-0037")
    text = replace_once(text, "- [?] P01 paused until the reconciliation is accepted;", "- [x] P01 resumed after reconciliation acceptance;", "progress P01 pause")
    text = replace_once(text, "- [ ] confirm or supersede the provisional proof commit after acceptance;", f"- [x] proof commit confirmed as `{PROOF_COMMIT}`;", "progress proof commit")
    write(path, text)


def update_handoff() -> None:
    path = "AI_HANDOFF.md"
    text = read(path)
    text = replace_once(
        text,
        "Status: Campaign 001 accepted complete — Phase 0C-19 deep Workspace planning-load reconciliation active — P01 paused — runtime implementation unauthorized",
        "Status: Master Plan and roadmap 1.1.0 accepted — Campaign 001 complete — P01 physical-host closure active — runtime implementation unauthorized",
        "handoff status",
    )
    text = replace_once(
        text,
        "## Active Phase 0C-19 planning-load reconciliation",
        "## Accepted Phase 0C-19 planning-load reconciliation",
        "handoff Phase 0C-19 heading",
    )
    text = replace_once(
        text,
        "It must be synchronized into the complete private planning load before P01 continues.",
        "It is synchronized into the complete private planning load and accepted through ADR-0037 as Master Plan and roadmap version `1.1.0`.",
        "handoff accepted text",
    )
    text = replace_once(
        text,
        "Phase 0C-19: CANDIDATE / IN REVIEW\nADR-0037: PROPOSED\nP01: PAUSED\nPR #46 proof commit: PROVISIONAL\nphysical-host collection: NOT STARTED\nADR-0033: PROPOSED\nRuntime implementation: NOT AUTHORIZED",
        f"Phase 0C-19: COMPLETE\nADR-0037: ACCEPTED\nMaster Plan / roadmap: 1.1.0 / ACCEPTED\nP01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST\nPR #46 proof commit: CONFIRMED — {PROOF_COMMIT}\nphysical-host collection: NOT STARTED\nADR-0033: PROPOSED\nRuntime implementation: NOT AUTHORIZED",
        "handoff control state",
    )
    text = replace_once(
        text,
        "Do not run the physical proof until Phase 0C-19 is accepted and the proof commit is confirmed or superseded.",
        f"The next action is to run the proof kit on the exact physical host from confirmed commit `{PROOF_COMMIT}`. Do not accept ADR-0033 or authorize runtime without the resulting reviewed evidence.",
        "handoff next action",
    )
    write(path, text)


def update_decisions() -> None:
    path = "DECISIONS.md"
    text = read(path)
    text = replace_once(
        text,
        "### D-053 — Deep Workspace operations must be reconciled before P01 resumes\n\n**PROPOSED.**",
        "### D-053 — Deep Workspace operations are part of the accepted planning load\n\n**ACCEPTED.**",
        "decision index D-053",
    )
    text = replace_once(
        text,
        "Until accepted, P01 is paused and the PR #46 proof commit remains provisional.",
        f"ADR-0037 accepts the mapping without a Core extension or WP01–WP14 reopening. P01 resumes and the PR #46 proof commit is confirmed at `{PROOF_COMMIT}`; physical collection remains not started.",
        "decision index consequence",
    )
    write(path, text)


def update_physical_closure() -> None:
    path = "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md"
    text = read(path)
    text = replace_once(
        text,
        "Status: exact closure procedure recorded — P01 paused pending Phase 0C-19 planning-load reconciliation, then blocked on access to the physical proof host",
        "Status: exact closure procedure recorded — P01 active and blocked on access to the physical proof host",
        "physical closure status",
    )
    text = replace_once(
        text,
        "Before selecting the final physical-proof commit, accept Phase 0C-19 / ADR-0037 and make Master Plan and implementation roadmap version `1.1.0` operative. The provisional selection from roadmap PR #46 cannot authorize collection.",
        f"Phase 0C-19 / ADR-0037 are accepted and Master Plan/roadmap version `1.1.0` are operative. Roadmap PR #46's commit `{PROOF_COMMIT}` is confirmed as the exact physical-proof candidate. This completion does not itself authorize collection results or runtime.",
        "physical closure Step 1A",
    )
    write(path, text)


def update_p01_selection() -> None:
    path = "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md"
    text = read(path)
    text = replace_once(
        text,
        "Status: provisional, non-authorizing — P01 paused pending Phase 0C-19 / ADR-0037 planning-load acceptance",
        "Status: CONFIRMED, non-authorizing — P01 active and blocked on the exact physical proof host",
        "P01 selection status",
    )
    text = replace_once(
        text,
        "The exact commit below was selected before the complete deep Workspace study was reconciled into the private Master Plan and roadmap. It remains technically suitable and non-runtime, but it is provisional.\n\nDo not run physical-host collection until ADR-0037 accepts Phase 0C-19 and a reviewed change confirms this commit or selects a newer non-runtime preparation commit.",
        f"The exact commit below was selected before the complete deep Workspace study was reconciled into the private Master Plan and roadmap. ADR-0037 now accepts that reconciliation. `Ptah-space` main remains `{PROOF_COMMIT}`, so the selection is confirmed. Physical-host collection has not started.",
        "P01 selection correction",
    )
    text = replace_once(
        text,
        "P01: PAUSED / provisional proof candidate",
        "P01: ACTIVE / confirmed proof candidate / blocked on exact physical host",
        "P01 selection boundary",
    )
    write(path, text)


def update_recovery_records() -> None:
    for path in [
        "planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md",
        "planning/MASTER-PLAN-RECONCILIATION.md",
    ]:
        text = read(path)
        text = text.replace(
            "Until ADR-0037 accepts the synchronized planning load, P01 is paused and the selected physical-proof commit is provisional.",
            f"ADR-0037 accepts the synchronized planning load. P01 resumes and the selected physical-proof commit is confirmed at `{PROOF_COMMIT}`; physical collection remains not started.",
        )
        text = text.replace(
            "The earlier P01 candidate selection is provisional until this reconciliation is accepted.",
            f"The earlier P01 candidate selection is confirmed after this reconciliation at `{PROOF_COMMIT}`.",
        )
        write(path, text)


def update_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["status"] = "accepted_master_plan_1_1_authority_physical_host_open"
    data["active_work_unit"] = "P01-physical-host-and-ADR-0033-closure"
    data["runtime_implementation_authorized"] = False
    data["next_action"] = f"Run the pinned-host proof kit on the exact Ubuntu Server 24.04.4 LTS / x86_64 / 6.8.0-136-generic physical host from confirmed Ptah-space commit {PROOF_COMMIT}."
    for key in ["master_plan", "implementation_roadmap"]:
        record = data.get("plan_documents", {}).get(key)
        if isinstance(record, dict):
            record["version"] = "1.1.0"
    for programme in data.get("programmes", []):
        if programme.get("id") == "P01":
            programme["status"] = "active_blocked_external_physical_host"
    candidate = data.get("phase0c19_deep_workspace_reconciliation")
    if not isinstance(candidate, dict):
        raise SyncError("machine Phase 0C-19 candidate record missing")
    candidate.update({
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
        "acceptance_record": "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md",
        "accepted_state_proof_pending": True,
        "operative_acceptance_merge_pending": True,
    })
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def validate_boundary() -> None:
    state = read("CURRENT_STATE.md")
    if "**Runtime implementation:** NOT AUTHORIZED" not in state:
        raise SyncError("runtime non-authorization missing")
    if "ADR-0033: PROPOSED" not in state:
        raise SyncError("ADR-0033 proposed state missing")
    if "physical-host collection: NOT STARTED" not in state:
        raise SyncError("physical collection not-started state missing")
    if "ADR-0037: ACCEPTED" not in state or "P01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST" not in state:
        raise SyncError("accepted Phase 0C-19 control state missing")
    index = json.loads((ROOT / "master-plan-index.json").read_text(encoding="utf-8"))
    candidate = index["phase0c19_deep_workspace_reconciliation"]
    if candidate.get("confirmed_proof_commit") != PROOF_COMMIT:
        raise SyncError("confirmed proof commit mismatch")
    if candidate.get("physical_host_collection_started") is not False:
        raise SyncError("physical collection started")
    if candidate.get("adr_0033_accepted") is not False or candidate.get("runtime_implementation_authorized") is not False:
        raise SyncError("authorization boundary changed")


def main() -> None:
    update_master_plan()
    update_roadmap()
    update_decision()
    update_work_package()
    update_reconciliation_record()
    update_current_state()
    update_progress()
    update_handoff()
    update_decisions()
    update_physical_closure()
    update_p01_selection()
    update_recovery_records()
    update_index()
    validate_boundary()
    print("Phase 0C-19 acceptance synchronization applied")


if __name__ == "__main__":
    main()
