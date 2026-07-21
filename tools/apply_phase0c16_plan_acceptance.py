#!/usr/bin/env python3
"""Apply reviewed Phase 0C-16 / ADR-0034 Master Plan acceptance."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_HEAD = "37d23449fda9a426f56ee8b09042dda91587a6d1"
CANDIDATE_MERGE = "2c24f9e6b0fc98d5e03605596db75d7495796353"
WORKFLOW_RUN = "29842137511"
ARTIFACT_ID = "8499790872"
ARTIFACT_DIGEST = "sha256:82d6b452777e2c5e60c4d08bf88dd2c848d6b2570650b70a4eede633c8065d9f"


class AcceptanceError(RuntimeError):
    pass


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AcceptanceError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def update_text(relative: str, transforms: list[tuple[str, str, str]]) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    for old, new, label in transforms:
        text = replace_once(text, old, new, f"{relative}: {label}")
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def update_master_plan() -> None:
    update_text(
        "MASTER_PLAN.md",
        [
            (
                "Status: candidate master plan for review — runtime implementation remains unauthorized",
                "Status: accepted product and operating authority — runtime implementation remains unauthorized",
                "status",
            ),
            ("Version: 1.0-candidate", "Version: 1.0.0", "version"),
            (
                "The older `MASTER_ROADMAP.md` remains historical architecture and phase source material until this candidate is reviewed and accepted. Once accepted, this document becomes the primary product-plan authority and `IMPLEMENTATION_ROADMAP.md` becomes the primary delivery-sequencing authority.",
                "The older `MASTER_ROADMAP.md` remains retained historical architecture and phase source material. Under accepted ADR-0034, this document is the primary product and operating authority and `IMPLEMENTATION_ROADMAP.md` is the primary delivery-sequencing authority.",
                "authority paragraph",
            ),
            (
                "Recovered requirements and decisions: complete for master-plan drafting.\n\nMaster Plan: this candidate requires review and acceptance.\n\nDetailed implementation roadmap: must be derived and reviewed with this plan.",
                "Recovered requirements and decisions: accepted through Phase 0C-16.\n\nMaster Plan: accepted as version `1.0.0` through ADR-0034 and merge `2c24f9e6b0fc98d5e03605596db75d7495796353`.\n\nDetailed implementation roadmap: accepted as version `1.0.0`; Programme P01 is the active pre-runtime gate.",
                "closure state",
            ),
        ],
    )


def update_roadmap() -> None:
    update_text(
        "IMPLEMENTATION_ROADMAP.md",
        [
            (
                "Status: candidate delivery authority derived from `MASTER_PLAN.md` — runtime implementation remains unauthorized",
                "Status: accepted delivery authority derived from `MASTER_PLAN.md` — runtime implementation remains unauthorized",
                "status",
            ),
            ("Version: 1.0-candidate", "Version: 1.0.0", "version"),
            (
                "1. this roadmap and the Master Plan are reviewed and accepted;",
                "1. this accepted roadmap and Master Plan remain authoritative;",
                "authorization prerequisite",
            ),
            (
                "Status: ACTIVE on planning branch.",
                "Status: COMPLETE — accepted through Phase 0C-16 and ADR-0034.",
                "P00 status",
            ),
            (
                "P00 Master-plan authority closure: ACTIVE.\n\nP01 Physical-host and ADR-0033 closure: BLOCKED on the actual pinned host.",
                "P00 Master-plan authority closure: COMPLETE.\n\nP01 Physical-host and ADR-0033 closure: ACTIVE and BLOCKED on access to the actual pinned host.",
                "programme state",
            ),
        ],
    )


def update_adr34() -> None:
    path = ROOT / "decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "Status: proposed — review with Phase 0C-16 master-plan closure",
        "Status: accepted — Master Plan, implementation roadmap and durable handoff are operative authorities",
        "ADR-0034 status",
    )
    marker = "## Consequences\n"
    if text.count(marker) != 1:
        raise AcceptanceError("ADR-0034 consequences marker mismatch")
    evidence = f"""## Acceptance evidence

Phase 0C-16 candidate exact head:

```text
{CANDIDATE_HEAD}
```

Candidate closure workflow run: `{WORKFLOW_RUN}`.

Retained artifact: `{ARTIFACT_ID}` with archive digest `{ARTIFACT_DIGEST}`.

The candidate passed twelve positive/adversarial regressions, standalone validation over seventeen authority files, complete WP01–WP14 and Phase 0C-01–16 mapping, P00/P01 and A01–A15 ordering, exact physical-host target/command checks and non-authorization checks.

Candidate squash merge:

```text
{CANDIDATE_MERGE}
```

Direct review found no unresolved review threads or changed-file boundary violations. CodeRabbit review was requested but rate-limited and produced no findings.

"""
    text = text.replace(marker, evidence + marker, 1)
    text = replace_once(
        text,
        "This ADR may be accepted when:",
        "This ADR is accepted because:",
        "ADR-0034 acceptance wording",
    )
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def update_wp16() -> None:
    path = ROOT / "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "Status: candidate under review — runtime implementation remains unauthorized",
        "Status: accepted — complete planning authority closed; runtime implementation remains unauthorized",
        "Phase 0C-16 status",
    )
    marker = "## Recovered authority defects\n"
    if text.count(marker) != 1:
        raise AcceptanceError("Phase 0C-16 evidence insertion marker mismatch")
    evidence = f"""## Acceptance evidence

- exact tested candidate head: `{CANDIDATE_HEAD}`;
- exact-head workflow run: `{WORKFLOW_RUN}`;
- retained evidence artifact: `{ARTIFACT_ID}`;
- retained archive digest: `{ARTIFACT_DIGEST}`;
- candidate squash merge: `{CANDIDATE_MERGE}`;
- twelve positive/adversarial regressions passed;
- standalone seventeen-file closure validation passed;
- direct review completed with no unresolved review threads;
- ADR-0034 accepted separately from ADR-0033;
- runtime implementation remained unauthorized.

"""
    text = text.replace(marker, evidence + marker, 1)
    text = replace_once(
        text,
        "This work package can become accepted only when automated and direct review confirm:",
        "This work package was accepted after automated and direct review confirmed:",
        "Phase 0C-16 acceptance wording",
    )
    text = replace_once(
        text,
        "After reviewed merge, this package closes:",
        "This accepted package closes:",
        "Phase 0C-16 closed conditions wording",
    )
    text = replace_once(
        text,
        "The planning layer is being completed in the required order. Runtime implementation remains **NOT AUTHORIZED**.",
        "The planning layer is accepted and complete through Phase 0C-16. Programme P01 is now the active blocker. Runtime implementation remains **NOT AUTHORIZED**.",
        "Phase 0C-16 conclusion",
    )
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def update_recovery_records() -> None:
    update_text(
        "planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md",
        [
            (
                "Status: recovered baseline for master-plan closure — runtime implementation remains unauthorized",
                "Status: accepted recovered baseline under Phase 0C-16 — runtime implementation remains unauthorized",
                "recovery status",
            ),
            (
                "Recovered requirements and decisions: COMPLETE FOR MASTER-PLAN DRAFTING.",
                "Recovered requirements and decisions: ACCEPTED THROUGH PHASE 0C-16.",
                "recovery checkpoint",
            ),
        ],
    )
    update_text(
        "planning/MASTER-PLAN-RECONCILIATION.md",
        [
            (
                "Status: candidate reconciliation — runtime implementation remains unauthorized",
                "Status: accepted reconciliation under Phase 0C-16 — runtime implementation remains unauthorized",
                "reconciliation status",
            )
        ],
    )
    update_text(
        "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md",
        [
            (
                "- review and merge of the master-plan closure package;",
                "- Master Plan closure accepted and merged as `2c24f9e6b0fc98d5e03605596db75d7495796353`;",
                "closure prerequisite state",
            ),
            (
                "## Step 1 — accept the planning closure package",
                "## Step 1 — planning closure package accepted",
                "closure step status",
            ),
            (
                "Complete and merge the Phase 0C-16 Master Plan closure package, then run the proof kit on the exact physical Ubuntu host.",
                "Run the proof kit on the exact physical Ubuntu host from the selected clean reviewed `Ptah-space` commit.",
                "closure next action",
            ),
        ],
    )


def update_decisions() -> None:
    path = ROOT / "DECISIONS.md"
    text = path.read_text(encoding="utf-8")
    old = """## Current proposed decisions

### ADR-0033 — First vertical-slice host, licence, layout and backend selections

**PROPOSED.** Selection and tooling evidence is substantially complete, but the accepted Master Plan/roadmap, physical pinned-host result, package/retention acceptance and final closure review remain open.

### ADR-0034 — Master Plan, implementation roadmap and durable handoff authority

**PROPOSED.** Establishes separate product-plan, delivery-roadmap, current-state and recovery authorities with save-as-you-go checkpoints. It may be accepted with Phase 0C-16 after exact-head review.
"""
    new = f"""## Phase 0C accepted planning authority

### D-050 — Master Plan, implementation roadmap and durable handoff have separate authorities

**ACCEPTED.** `MASTER_PLAN.md` version `1.0.0` is the product and operating authority; `IMPLEMENTATION_ROADMAP.md` version `1.0.0` is the delivery-sequencing authority; frozen WP01–WP14 remain technical contract authority; `CURRENT_STATE.md` selects the exact current work; `AI_HANDOFF.md` and `master-plan-index.json` provide durable recovery. Phase 0C-16 candidate `{CANDIDATE_HEAD}` passed exact-head validation and merged as `{CANDIDATE_MERGE}`. Runtime implementation remains unauthorized.

Full decision: `decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md`.

---

## Current proposed decisions

### ADR-0033 — First vertical-slice host, licence, layout and backend selections

**PROPOSED.** Master Plan/roadmap authority is complete. The physical pinned-host result, package and retention acceptance, final Phase 0C closure review and explicit runtime authorization remain open.
"""
    text = replace_once(text, old, new, "DECISIONS plan authority acceptance")
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def update_progress() -> None:
    update_text(
        "PROGRESS.md",
        [
            (
                "- [-] repair stale control-book records and run exact-head consistency validation;\n- [ ] review and merge Phase 0C-16;\n- [ ] accept ADR-0034 in the reviewed Phase 0C-16 merge.",
                "- [x] stale control-book records repaired and exact-head consistency validation passed;\n- [x] Phase 0C-16 reviewed and merged as `2c24f9e6b0fc98d5e03605596db75d7495796353`;\n- [x] ADR-0034 accepted; Master Plan and implementation roadmap version `1.0.0` are operative authorities.",
                "planning closure checklist",
            ),
            (
                "- [-] review and merge the complete Master Plan and implementation roadmap closure package;\n",
                "",
                "active planning blocker",
            ),
            (
                "- [-] P00 — Master-plan authority closure.\n- [?] P01 — Physical-host and ADR-0033 closure; blocked on the exact external host after P00 merge.",
                "- [x] P00 — Master-plan authority closure.\n- [?] P01 — Physical-host and ADR-0033 closure; active and blocked on the exact external host.",
                "programme status",
            ),
        ],
    )


def update_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "**Active work unit:** 0C-16 — complete Master Plan, implementation roadmap and durable AI handoff closure",
        "**Active work unit:** 0C-04 / P01 — physical pinned-host proof, package review, durable evidence and ADR-0033 closure",
        "current active work",
    )
    start = text.index("## Active Phase 0C-16 Master Plan closure")
    end = text.index("## Active Phase 0C blockers", start)
    accepted = f"""## Accepted Phase 0C-16 Master Plan closure

The complete product/operating plan, dependency-ordered implementation roadmap, WP01–WP14/Phase 0C reconciliation and durable human/AI handoff were validated at exact candidate head:

```text
{CANDIDATE_HEAD}
```

Exact-head workflow run: `{WORKFLOW_RUN}`.

Retained artifact: `{ARTIFACT_ID}` with archive digest `{ARTIFACT_DIGEST}`.

Candidate squash merge:

```text
{CANDIDATE_MERGE}
```

ADR-0034 is accepted. `MASTER_PLAN.md` and `IMPLEMENTATION_ROADMAP.md` version `1.0.0` are operative authorities. No new Core entity or current WP01–WP14 reopening was required. This closes planning authority only and does not accept the physical host, packages, retention, ADR-0033 or runtime implementation.

---

"""
    text = text[:start] + accepted + text[end:]
    old_blockers = """Implementation remains unauthorized until all of the following are merged and reviewed:

1. acceptance of the complete Master Plan, detailed implementation roadmap, reconciliation and durable handoff through Phase 0C-16 / ADR-0034;
2. a proof-eligible capability report from the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
3. the exact installed Ubuntu package manifest and package-artifact digests from that pinned host, with reviewer acceptance;
4. generation, durable commit and explicit review acceptance of that physical-host evidence bundle;
5. a Phase 0C closure review proving no frozen contract was weakened;
6. acceptance of ADR-0033;
7. explicit `Runtime implementation: AUTHORIZED` in this file in the same reviewed closure change.
"""
    new_blockers = """Implementation remains unauthorized until all of the following are merged and reviewed:

1. a proof-eligible capability report from the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
2. the exact installed Ubuntu package manifest and package-artifact digests from that pinned host, with reviewer acceptance;
3. generation, durable commit and explicit review acceptance of that physical-host evidence bundle;
4. a Phase 0C closure review proving no frozen contract was weakened;
5. acceptance of ADR-0033;
6. explicit `Runtime implementation: AUTHORIZED` in this file in the same reviewed closure change.
"""
    text = replace_once(text, old_blockers, new_blockers, "current remaining blockers")
    marker = "## Immediate continuation order\n"
    prefix = text.split(marker, 1)[0]
    tail = """## Immediate continuation order

1. Install or recover the exact Ubuntu Server 24.04.4 / `6.8.0-136-generic` proof host.
2. Select and record the exact clean reviewed `Ptah-space` preparation commit.
3. Run:

```bash
python3 tools/run_pinned_host_proof.py \
  --repo-root . \
  --output evidence/phase0c/pinned-host-candidate
```

4. Require `proof_eligible: true` with empty host, capability, package-artifact and repository failure sets.
5. Review and accept the exact installed package and package-artifact manifests.
6. From the same exact clean commit, run:

```bash
python3 tools/retain_verified_pinned_host_evidence.py \
  --repo-root . \
  --bundle-dir evidence/phase0c/pinned-host-candidate \
  --output-dir evidence/phase0c/pinned-host-durable-candidate
```

7. Commit and explicitly accept the durable candidate and repository binding.
8. Conduct the final Phase 0C closure consistency review.
9. Accept ADR-0033 and authorize runtime only when every remaining blocker passes.
"""
    path.write_text((prefix + tail).rstrip() + "\n", encoding="utf-8")


def update_adr33() -> None:
    path = ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "Status: proposed — dependency, backend, signer, proof, retention and licence governance complete; Master Plan acceptance, physical pinned-host result, package/retention acceptance and closure review remain open",
        "Status: proposed — Master Plan and governance complete; physical pinned-host result, package/retention acceptance and closure review remain open",
        "ADR-0033 status",
    )
    text = replace_once(
        text,
        "40. exact-head adversarial coverage for the operative licence acceptance.",
        "40. exact-head adversarial coverage for the operative licence acceptance;\n41. accepted Master Plan and implementation roadmap version `1.0.0`;\n42. accepted WP01–WP14 and Phase 0C reconciliation with zero current Core extensions;\n43. accepted durable human/AI handoff and save-as-you-go authority through ADR-0034.",
        "ADR-0033 completed conditions",
    )
    old = """This ADR remains proposed until all of the following are complete:

1. the complete `MASTER_PLAN.md`, `IMPLEMENTATION_ROADMAP.md`, reconciliation and durable handoff are accepted through Phase 0C-16 and ADR-0034;
2. a proof-eligible capability report is produced on the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
3. the exact installed Ubuntu package manifest and package-artifact digests are recorded from that host and accepted by review;
4. that host's exact source bundle is independently verified, durably committed and explicitly accepted through its review record;
5. a Phase 0C closure review confirms no frozen contract was weakened;
6. this ADR is changed to accepted;
7. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED` in the same reviewed closure change.
"""
    new = """This ADR remains proposed until all of the following are complete:

1. a proof-eligible capability report is produced on the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
2. the exact installed Ubuntu package manifest and package-artifact digests are recorded from that host and accepted by review;
3. that host's exact source bundle is independently verified, durably committed and explicitly accepted through its review record;
4. a Phase 0C closure review confirms no frozen contract was weakened;
5. this ADR is changed to accepted;
6. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED` in the same reviewed closure change.
"""
    text = replace_once(text, old, new, "ADR-0033 open conditions")
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def update_index_and_handoff() -> None:
    path = ROOT / "master-plan-index.json"
    index = json.loads(path.read_text(encoding="utf-8"))
    if index.get("status") != "candidate_master_plan_closure_active":
        raise AcceptanceError("master-plan index candidate status mismatch")
    if index.get("runtime_implementation_authorized") is not False:
        raise AcceptanceError("master-plan index cannot authorize runtime")
    index["status"] = "accepted_master_plan_authority_physical_host_open"
    index["planning_branch"] = "main"
    index["acceptance_source_branch"] = "phase0c-master-plan-acceptance"
    index["active_work_unit"] = "P01-physical-host-and-ADR-0033-closure"
    index["acceptance_evidence"] = {
        "candidate_exact_head": CANDIDATE_HEAD,
        "candidate_workflow_run": WORKFLOW_RUN,
        "candidate_artifact_id": ARTIFACT_ID,
        "candidate_artifact_digest": ARTIFACT_DIGEST,
        "candidate_merge": CANDIDATE_MERGE,
        "adr_0034_accepted": True,
        "phase0c_16_accepted": True,
        "runtime_implementation_authorized": False,
    }
    for key in ("requirements_and_decisions", "master_plan", "implementation_roadmap", "reconciliation"):
        index["plan_documents"][key]["status"] = "accepted"
        index["plan_documents"][key]["acceptance_merge"] = CANDIDATE_MERGE
    index["plan_documents"]["master_plan"]["version"] = "1.0.0"
    index["plan_documents"]["implementation_roadmap"]["version"] = "1.0.0"
    index["plan_documents"]["authorization_closure"]["status"] = "procedure_ready_physical_host_open"
    index["plan_documents"]["handoff"]["status"] = "active_recovery_entry_physical_host_open"
    for programme in index["programmes"]:
        if programme["id"] == "P00":
            programme["status"] = "complete"
        elif programme["id"] == "P01":
            programme["status"] = "active_blocked_external_physical_host"
    blockers = index["authorization_blockers"]
    blockers.remove("review_and_merge_master_plan_closure")
    index["next_action"] = "Run the pinned-host proof kit on the exact Ubuntu Server 24.04.4 LTS / x86_64 / 6.8.0-136-generic physical host from the selected clean reviewed Ptah-space commit."
    path.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")

    handoff = f"""# Ptah durable AI/chat handoff

Last updated: 2026-07-21

Status: Master Plan and implementation roadmap accepted — P01 physical-host closure active — runtime implementation unauthorized

## Read first

1. `AI_HANDOFF.md`
2. `CURRENT_STATE.md`
3. `master-plan-index.json`
4. `MASTER_PLAN.md`
5. `IMPLEMENTATION_ROADMAP.md`
6. `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`
7. `planning/MASTER-PLAN-RECONCILIATION.md`
8. `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`
9. `PROGRESS.md`
10. `DECISIONS.md` and the referenced ADRs
11. `MEMORY_PROTOCOL.md`
12. current source and evidence in `jaydumisuni/Ptah-space`

Do not ask the owner to repeat information recoverable from these records.

## Accepted planning authority

- Master Plan version: `1.0.0`;
- implementation roadmap version: `1.0.0`;
- accepted authority decision: ADR-0034;
- accepted work package: Phase 0C-16;
- candidate exact head: `{CANDIDATE_HEAD}`;
- exact-head workflow run: `{WORKFLOW_RUN}`;
- retained artifact: `{ARTIFACT_ID}`;
- artifact archive digest: `{ARTIFACT_DIGEST}`;
- candidate squash merge: `{CANDIDATE_MERGE}`.

The accepted programme is:

```text
P00 Master-plan authority closure — COMPLETE
P01 Physical-host and ADR-0033 closure — ACTIVE / BLOCKED ON EXACT PHYSICAL HOST
Programme A Online Ptah Alpha — PLANNED / NOT AUTHORIZED
Programmes B–F — PLANNED
```

## Exact next action

On the exact Ubuntu Server 24.04.4 LTS / x86_64 / `6.8.0-136-generic` physical proof host, check out the selected clean reviewed `Ptah-space` preparation commit and run:

```bash
python3 tools/run_pinned_host_proof.py \
  --repo-root . \
  --output evidence/phase0c/pinned-host-candidate
```

Require `proof_eligible: true`, empty failure sets and complete package/APT artifact evidence. Then independently retain the same exact bundle:

```bash
python3 tools/retain_verified_pinned_host_evidence.py \
  --repo-root . \
  --bundle-dir evidence/phase0c/pinned-host-candidate \
  --output-dir evidence/phase0c/pinned-host-durable-candidate
```

Review and explicitly accept host identity, capabilities, installed packages, package artifacts, APT sources/indexes, durable bytes and repository binding.

## Remaining authorization sequence

```text
Physical pinned-host proof
→ package/package-artifact acceptance
→ durable bundle commit and acceptance
→ final Phase 0C consistency review
→ ADR-0033 acceptance
→ explicit Runtime implementation: AUTHORIZED
→ A01 becomes READY
```

## Hard boundary

```text
Master Plan: ACCEPTED
Implementation roadmap: ACCEPTED
ADR-0034: ACCEPTED
Physical-host proof: OPEN
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```

No chat, model or owner-intent statement may replace the missing physical evidence and reviewed ADR-0033 closure.
"""
    (ROOT / "AI_HANDOFF.md").write_text(handoff, encoding="utf-8")


def update_readme() -> None:
    update_text(
        "README.md",
        [
            (
                "Phase 0A donor closure and Phase 0B contracts are frozen. Phase 0C is active. The Master Plan and detailed implementation roadmap closure package is under review. Physical pinned-host evidence, ADR-0033 acceptance and explicit runtime authorization remain open.",
                "Phase 0A donor closure and Phase 0B contracts are frozen. The Master Plan and detailed implementation roadmap version `1.0.0` are accepted through ADR-0034 and Phase 0C-16. Phase 0C Programme P01 is active: physical pinned-host evidence, package/retention acceptance, ADR-0033 and explicit runtime authorization remain open.",
                "README current position",
            )
        ],
    )


def update_validator_and_workflow() -> None:
    update_text(
        "tools/check_master_plan_closure.py",
        [
            (
                'require_text(current, "**Active work unit:** 0C-16", "CURRENT_STATE")',
                'require_text(current, "**Active work unit:** 0C-04 / P01", "CURRENT_STATE")',
                "validator current work",
            ),
            (
                'require_text(current, "acceptance of the complete Master Plan", "CURRENT_STATE blockers")',
                'require_absent(current, "acceptance of the complete Master Plan", "CURRENT_STATE closed planning blocker")',
                "validator planning blocker",
            ),
            (
                'require(index.get("active_work_unit") == "P00-master-plan-authority-closure", "master-plan index active work mismatch")',
                'require(index.get("active_work_unit") == "P01-physical-host-and-ADR-0033-closure", "master-plan index active work mismatch")',
                "validator index active work",
            ),
            (
                'require(isinstance(blockers, list) and len(blockers) == 7, "authorization blocker set must contain seven entries")\n    require("review_and_merge_master_plan_closure" in blockers, "planning closure blocker missing")',
                'require(isinstance(blockers, list) and len(blockers) == 6, "authorization blocker set must contain six entries")\n    require("review_and_merge_master_plan_closure" not in blockers, "closed planning blocker remains active")',
                "validator blocker set",
            ),
            (
                'require_text(master, "Version: 1.0-candidate", "MASTER_PLAN")\n    require_text(master, "Status: candidate master plan for review", "MASTER_PLAN")',
                'require_text(master, "Version: 1.0.0", "MASTER_PLAN")\n    require_text(master, "Status: accepted product and operating authority", "MASTER_PLAN")',
                "validator master acceptance",
            ),
            (
                'require_text(roadmap, "Version: 1.0-candidate", "IMPLEMENTATION_ROADMAP")',
                'require_text(roadmap, "Version: 1.0.0", "IMPLEMENTATION_ROADMAP")\n    require_text(roadmap, "Status: accepted delivery authority", "IMPLEMENTATION_ROADMAP")',
                "validator roadmap acceptance",
            ),
            (
                'require_text(handoff, "phase0c-master-plan-roadmap-closure", "AI handoff branch")',
                f'require_text(handoff, "{CANDIDATE_MERGE}", "AI handoff accepted merge")',
                "validator handoff merge",
            ),
            (
                'require_text(decisions, "ADR-0034", "DECISIONS proposed plan authority")',
                'require_text(decisions, "D-050", "DECISIONS accepted plan authority")',
                "validator decisions acceptance",
            ),
            (
                'require_text(adr34, "Status: proposed", "ADR-0034 status")',
                'require_text(adr34, "Status: accepted", "ADR-0034 status")',
                "validator ADR-0034 status",
            ),
            (
                'require_text(wp16, "Status: candidate under review", "Phase 0C-16 status")',
                'require_text(wp16, "Status: accepted", "Phase 0C-16 status")',
                "validator Phase 0C-16 status",
            ),
            (
                'require_text(recovery, "Recovered requirements and decisions: COMPLETE FOR MASTER-PLAN DRAFTING", "recovery checkpoint")',
                'require_text(recovery, "Recovered requirements and decisions: ACCEPTED THROUGH PHASE 0C-16", "recovery checkpoint")',
                "validator recovery acceptance",
            ),
            (
                '"status": "candidate_valid_non_authorizing",\n        "master_plan_version": "1.0-candidate",\n        "implementation_roadmap_version": "1.0-candidate",',
                '"status": "accepted_plan_authority_non_authorizing",\n        "master_plan_version": "1.0.0",\n        "implementation_roadmap_version": "1.0.0",',
                "validator output status",
            ),
        ],
    )
    update_text(
        ".github/workflows/phase0c16-master-plan-closure.yml",
        [
            (
                'if evidence["validation_status"] != "candidate_valid_non_authorizing":',
                'if evidence["validation_status"] != "accepted_plan_authority_non_authorizing":',
                "workflow validation status",
            )
        ],
    )
    update_text(
        "tools/test_check_master_plan_closure.py",
        [
            (
                'self.assertEqual(report["status"], "candidate_valid_non_authorizing")',
                'self.assertEqual(report["status"], "accepted_plan_authority_non_authorizing")',
                "test accepted status",
            ),
            (
                "    def test_adr0034_requires_save_as_you_go_authority(self) -> None:\n",
                "    def test_adr0034_must_be_accepted(self) -> None:\n        root = self.make_repo()\n        path = root / \"decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md\"\n        self.replace(path, \"Status: accepted\", \"Status: proposed\")\n        self.assert_invalid(root)\n\n    def test_adr0034_requires_save_as_you_go_authority(self) -> None:\n",
                "test ADR-0034 acceptance",
            ),
        ],
    )


def verify() -> None:
    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    adr33 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    adr34 = (ROOT / "decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md").read_text(encoding="utf-8")
    index = json.loads((ROOT / "master-plan-index.json").read_text(encoding="utf-8"))
    if "**Runtime implementation:** NOT AUTHORIZED" not in current:
        raise AcceptanceError("runtime non-authorization missing")
    if "**Runtime implementation:** AUTHORIZED" in current:
        raise AcceptanceError("runtime authorization appeared")
    if "Status: proposed" not in adr33:
        raise AcceptanceError("ADR-0033 changed from proposed")
    if "Status: accepted" not in adr34:
        raise AcceptanceError("ADR-0034 acceptance missing")
    if index.get("runtime_implementation_authorized") is not False:
        raise AcceptanceError("machine index attempted runtime authorization")
    if len(index.get("authorization_blockers", [])) != 6:
        raise AcceptanceError("remaining blocker count mismatch")


def main() -> None:
    update_master_plan()
    update_roadmap()
    update_adr34()
    update_wp16()
    update_recovery_records()
    update_decisions()
    update_progress()
    update_current_state()
    update_adr33()
    update_index_and_handoff()
    update_readme()
    update_validator_and_workflow()
    verify()
    print("Phase 0C-16 / ADR-0034 Master Plan acceptance prepared successfully")


if __name__ == "__main__":
    try:
        main()
    except AcceptanceError as exc:
        raise SystemExit(str(exc)) from exc
