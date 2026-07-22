#!/usr/bin/env python3
"""Restore the accepted neutral Ptah substrate boundary across plan authority."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_CORRECTION_MERGE = "8a8d620c5227a6508145cd4a30f4f45142bfabe9"
PUBLIC_CORRECTION_HEAD = "5a95c577edf366bad1d8949ee37c17b81f296254"
PUBLIC_CORRECTION_RUN = "29961370694"
PUBLIC_CORRECTION_ARTIFACT = "8546091277"
PUBLIC_CORRECTION_DIGEST = "sha256:04472fd4fd546fcc2420d135cdfcb517381efbe5de8b3bc14f6971207fbde819"
CORRECTION_RECORD = "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md"


class CorrectionError(RuntimeError):
    pass


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise CorrectionError(f"{label}: expected one source fragment, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def correct_master_plan() -> None:
    path = ROOT / "MASTER_PLAN.md"
    replace_once(
        path,
        """The product must answer at any time:

- What Workspace are we in?
- What Objects, Revisions and Artifacts exist?
- What Activities are running, waiting, failed or complete?
- Which Node and Provider Generation performed each action?
- What evidence proves the claimed outcome?
- What can be safely resumed after interruption?
- What authority does this user, agent or scheduled Activity have?
- Which source is canonical, superseded, private or only a generated candidate?
- Can the same work continue on another compatible Node or with another model/provider?
""",
        """The platform must expose enough exact state for an authorized caller to answer questions such as:

- What Workspace are we in?
- What Objects, Revisions and Artifacts exist?
- What Activities are running, waiting, failed or complete?
- Which Node and Provider Generation performed each action?
- What Receipts and evidence were retained?
- What mechanically recoverable state exists after interruption?
- What configured Grants, Leases and Fences apply to this caller or Activity?
- What caller-supplied labels and provenance are stored on each record?
- Can the same stored work continue on another compatible Node or with another model/provider?

Ptah exposes and preserves the records. The caller decides meaning, relevance, authority, correctness and next action.
""",
        "Master Plan problem questions",
    )
    replace_once(
        path,
        "14. **Model and provider replacement must not erase project truth or authority.**",
        "14. **Model and provider replacement must not erase caller-owned records, configured access or provenance.**",
        "Master Plan principle 14",
    )
    replace_once(
        path,
        """Hunter is the primary internal planning and coordination participant for THETECHGUY use. Hunter:

- interprets owner or operator intent;
- requests bounded Workspace context;
- proposes plans and Activities;
- selects suitable Providers within granted authority;
- produces candidate Artifacts and handoffs;
- requests protected-action approval;
- never directly rewrites canonical truth from a model response.
""",
        """Hunter is the primary internal planning and coordination participant for THETECHGUY use. Hunter:

- interprets owner or operator intent;
- requests records from Ptah and constructs Hunter-owned bounded context;
- selects relevant sources and applies Hunter or owner-defined trust labels;
- proposes plans and caller-defined Activities;
- selects suitable Providers within configured access;
- produces candidate Artifacts and handoffs;
- requests protected-action approval from the applicable human or application;
- proposes next actions and never assigns those decisions to Ptah.
""",
        "Master Plan Hunter role",
    )
    replace_once(
        path,
        """Sergeant or another reviewer:

- receives independently selected evidence and context;
- challenges claims, unsafe shortcuts and incomplete proof;
- records review outcomes without silently mutating Hunter’s result;
- cannot promote a result beyond the authority granted by the owner and accepted process.
""",
        """Sergeant or another reviewer:

- independently selects or requests the frozen candidate and review evidence;
- uses Ptah compute, storage and Facilities without becoming part of Ptah;
- challenges claims, unsafe shortcuts and incomplete proof;
- records Sergeant's review outcome without silently mutating Hunter’s result;
- issues no Ptah verdict: a human or calling application decides what to do with the review.
""",
        "Master Plan Sergeant role",
    )
    replace_once(
        path,
        """- Policy, Grant, Lease, Fence and authority records;
- Recipe, Plan, Run, Step, Receipt and Evidence records;
""",
        """- caller-configured Policy, Grant, Lease and Fence records with mechanical enforcement;
- caller-defined Recipe, Plan, Run and Step records plus Receipt and Evidence storage;
""",
        "Master Plan Core records",
    )
    replace_once(
        path,
        """### 6.5 AI Project Workspace experience

The `ptah.workspace.ai_project.v1` composition profile adds:

- Workspace purpose and objective;
- project instructions and Policies;
- source-authority classes;
- parallel Sessions or work threads;
- reusable Artifact Library views;
- bounded context compilation;
- visible memory and source selection;
- model-independent handoffs;
- scheduled Activities with least-privilege Artifact access;
- explicit candidate-to-canonical promotion.

This is a composition of frozen Ptah primitives, not a new ChatGPT-specific Core entity.
""",
        """### 6.5 AI Project Workspace substrate and application experience

The `ptah.workspace.ai_project.v1` profile composes neutral Ptah capabilities for applications:

- durable Workspace and Session identities;
- caller-owned instruction, purpose, objective and label Artifacts;
- parallel Sessions or work threads;
- reusable Artifact Library views;
- exact caller-requested record retrieval;
- model-independent stored state and caller-produced handoffs;
- caller-submitted scheduled Activities with configured mechanical access;
- failure, provenance, checkpoint and recovery retention.

Hunter, Sergeant, humans or other applications perform context selection, source ranking, review, approval, candidate promotion and next-action choice. Ptah stores and executes the requested operations but does not make those decisions.

This is a composition of frozen Ptah primitives, not a new ChatGPT-specific Core entity.
""",
        "Master Plan AI Workspace section",
    )
    replace_once(
        path,
        """### 10.6 Workspace knowledge and memory

Project memory is stored as inspectable Objects, Artifacts, Knowledge Sources, Index Revisions, decisions and handoffs. Models receive bounded context packets. Hidden provider memory cannot become canonical project truth.

Source authority classes:

- canonical;
- accepted evidence;
- recovery copy;
- reference;
- generated candidate;
- temporary context;
- rejected;
- superseded.

## 11. Context compiler and agent handoff

Before an agent participates, Ptah compiles a bounded packet containing, as applicable:

- Workspace purpose and objective;
- participant role and authority;
- current canonical state;
- selected accepted decisions;
- active Activities and blockers;
- relevant authoritative Objects and Artifacts;
- recent relevant Sessions;
- available Facilities and Grants;
- evidence and privacy requirements;
- previous handoff and exact next action.

The compiler must expose which sources were selected and why. It must deny cross-Workspace private retrieval without an explicit Grant.

Every substantial work Session ends with a durable handoff containing:

- completed work;
- exact source and evidence commits;
- current state;
- blockers;
- active branch or Activity;
- next safe action;
- unresolved questions;
- limitations and failed attempts.
""",
        """### 10.6 Workspace knowledge and caller-owned memory

Ptah stores inspectable Objects, Artifacts, Knowledge Sources, Index Revisions and caller-produced decision or handoff records. Hidden provider memory cannot replace durable caller-owned records.

Applications may attach labels such as `canonical`, `accepted_evidence`, `recovery_copy`, `reference`, `generated_candidate`, `temporary_context`, `rejected` or `superseded`. Ptah preserves the label, author, revision and provenance but does not interpret, rank or enforce the label's meaning.

## 11. Application-owned context and agent handoff

Before an agent participates, Hunter, Sergeant, a human-facing application or another caller may request exact Workspace records and construct its own bounded packet.

The caller decides whether to include:

- purpose or objective records;
- participant-role metadata;
- caller-accepted decisions;
- Activities and caller-identified blockers;
- selected Objects and Artifacts;
- selected Sessions;
- Facility and Grant records;
- evidence or privacy instructions;
- a previous caller-produced handoff or proposed next action.

Ptah returns records the caller is mechanically permitted to read and preserves exact source revisions and provenance. Ptah does not select context, rank authority, infer blockers, approve work or choose a next action.

A human, Hunter, Sergeant or another application may create a durable handoff containing:

- completed work;
- exact source and evidence commits;
- current state;
- blockers;
- active branch or Activity;
- proposed next action;
- unresolved questions;
- limitations and failed attempts.

Ptah stores and versions the handoff Artifact. It does not verify its conclusions or decide that it is authoritative.
""",
        "Master Plan memory and context sections",
    )


def correct_roadmap() -> None:
    path = ROOT / "IMPLEMENTATION_ROADMAP.md"
    replace_once(
        path,
        """## D02 — AI Project Workspace and context compiler

Deliver:

- `ptah.workspace.ai_project.v1` manifest;
- source-authority service;
- bounded context compiler;
- visible selected sources;
- parallel Session/thread projections;
- reusable Artifact Library;
- model-independent handoff;
- candidate-to-canonical review flow;
- scheduled Activity context with least privilege.

Proof:

- no cross-Workspace leakage;
- superseded source cannot outrank canonical source;
- model replacement preserves authority and state;
- scheduled Activity sees only granted Artifacts;
- private Hunter memory cannot enter public Workspace without explicit lawful promotion.

Dependencies: B06, B07, D01, WP10/11 implementation.
""",
        """## D02 — AI Project Workspace substrate and application adapters

Deliver:

- `ptah.workspace.ai_project.v1` neutral manifest;
- exact Workspace, Session, Activity, Object and Artifact retrieval APIs;
- caller-metadata round-trip without Ptah interpretation;
- parallel Session/thread projections;
- reusable Artifact Library;
- model-independent stored state and handoff Artifacts;
- exact caller-submitted scheduled Activity inputs;
- Hunter adapter for Hunter-owned context selection and coordination;
- Sergeant adapter for independent review execution and retained Sergeant results.

Proof:

- no cross-Workspace leakage under configured Grants;
- conflicting caller authority labels remain stored with no Ptah-selected winner;
- model replacement preserves stored state, provenance and configured access;
- scheduled Activity sees only caller-specified, mechanically granted inputs;
- private Hunter records cannot be read from a public Workspace without configured release and Grant;
- Sergeant findings remain Sergeant Artifacts and never become a Ptah verdict;
- Ptah Core performs no context selection, approval, review, promotion or next-action choice.

Dependencies: B06, B07, D01, WP10/11 implementation.
""",
        "Implementation roadmap D02",
    )


def correct_phase0c15() -> None:
    path = ROOT / "work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md"
    text = f"""# Phase 0C-15 — AI Project Workspace donor and neutral platform correction

Status: accepted non-operative design evidence, corrected to restore the original Ptah boundary

Recorded: 2026-07-21

Corrected: 2026-07-22

## Purpose

Retain ChatGPT Projects and Work as an application-experience donor while preserving the Master Plan's original rule: Ptah is the world and machinery, not the thinker.

## Donor boundary

The donor is observed only through official public documentation. Integration remains `Study only`:

- no source-code or proprietary implementation reuse;
- no OpenAI runtime dependency;
- no ChatGPT-specific Core entity;
- no provider ownership of caller records;
- no transfer of context selection, source authority, review, approval or coordination into Ptah.

## Original candidate evidence

`Ptah-space` PR #14 tested head `2a2c28d17abd9ad52c8d850f8bbcdba57074194e` and merged as `d05653c5948727b58ead91088447d0b8ac4d9d9b`.

The profile identity remains:

```text
ptah.workspace.ai_project.v1
```

It composes sixteen frozen primitives and requires no new Core entity or WP01–WP14 reopening.

## Drift correction

The original candidate incorrectly described Ptah as owning source authority, context compilation, blockers, approvals, candidate promotion and review-packet construction. That language contradicted the already accepted Master Plan foundation and is superseded.

Correct responsibility split:

- **Ptah:** neutral Workspace, storage, execution, Facility, configured-access, Event, Receipt, checkpoint and recovery substrate;
- **Hunter:** intelligence, context selection, source judgments, planning, coordination, Provider choice and next-action proposals;
- **Sergeant:** independent reviewer using Ptah resources, issuing Sergeant's result;
- **Human or caller application:** intent, configured authority, approval, acceptance, rejection, release and final authorization.

Ptah may store caller-owned labels and records. It does not interpret, rank, approve or promote them.

## Corrected implementation-repository evidence

`Ptah-space` PR #15 exact tested head:

```text
{PUBLIC_CORRECTION_HEAD}
```

All ten workflows passed. The corrected Workspace lane was run `{PUBLIC_CORRECTION_RUN}` and retained artifact `{PUBLIC_CORRECTION_ARTIFACT}` with digest `{PUBLIC_CORRECTION_DIGEST}`.

Correction squash merge:

```text
{PUBLIC_CORRECTION_MERGE}
```

The corrected suite contains 17 adversarial regressions and ten fixtures proving mechanical isolation, caller-label preservation, no Ptah source winner, exact scheduled inputs, failed-work retention and Sergeant review without a Ptah verdict.

## Placement and non-effects

This correction:

- restores an existing product principle rather than adding a new architecture;
- does not reopen Phase 0A or WP01–WP14;
- does not add or close an ADR-0033 condition;
- does not implement a Workspace runtime or application adapter;
- does not start AF03;
- does not authorize runtime implementation.

## Conclusion

ChatGPT Projects remains useful for application experience. Ptah supplies the neutral platform. Hunter, Sergeant, humans and other applications decide what the platform is used for and what their results mean.
"""
    path.write_text(text, encoding="utf-8")


def correct_progress() -> None:
    path = ROOT / "PROGRESS.md"
    replace_once(
        path,
        """## AI Project Workspace behavioural donor and Hunter bridge candidate

- [x] ChatGPT Projects, project memory, Library, Work, Canvas and Scheduled Tasks recorded from official public documentation as behavioural sources only;
- [x] code reuse fixed at none and OpenAI excluded as a runtime dependency;
- [x] `ptah.workspace.ai_project.v1` candidate profile recorded over sixteen existing Ptah primitives;
- [x] fourteen behaviours mapped with zero frozen-contract extensions;
- [x] hidden provider memory and implicit global tool access explicitly rejected;
- [x] bounded context, source authority, Workspace isolation, Facility Grants and model-independent handoff requirements recorded;
- [x] Hunter–Ptah bridge responsibilities and candidate-to-truth promotion boundary recorded;
- [x] ten positive/negative fixtures and ten adversarial validator regressions passed;
- [x] all ten workflows passed at exact head `2a2c28d17abd9ad52c8d850f8bbcdba57074194e`;
- [x] donor/profile package squash-merged as `d05653c5948727b58ead91088447d0b8ac4d9d9b`;
- [x] candidate remains non-operative, non-blocking and runtime implementation remains unauthorized.
""",
        f"""## AI Project Workspace behavioural donor — neutral substrate correction

- [x] ChatGPT Projects, Library, Work, Canvas and Scheduled Tasks retained as application-experience sources only;
- [x] code reuse fixed at none and OpenAI excluded as a runtime dependency;
- [x] `ptah.workspace.ai_project.v1` remains a composition of sixteen existing Ptah primitives with zero Core extensions;
- [x] drift assigning context, source authority, review, approval or promotion to Ptah identified and removed;
- [x] Hunter owns intelligence/context/coordination, Sergeant owns independent review, and humans/calling applications own acceptance;
- [x] ten corrected fixtures and 17 adversarial regressions enforce the neutral boundary;
- [x] all ten workflows passed at exact correction head `{PUBLIC_CORRECTION_HEAD}`;
- [x] retained artifact `{PUBLIC_CORRECTION_ARTIFACT}` with digest `{PUBLIC_CORRECTION_DIGEST}`;
- [x] correction squash-merged as `{PUBLIC_CORRECTION_MERGE}`;
- [x] no AF03 start, contract reopening or runtime authorization introduced.
""",
        "PROGRESS donor correction",
    )
    replace_once(
        path,
        "- [x] AI Project Workspace donor/profile remains non-operative and provider-independent;",
        "- [x] AI Project Workspace donor/profile remains non-operative, provider-independent and mechanically neutral;",
        "PROGRESS no-build correction",
    )


def correct_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    old = """## Merged AI Project Workspace behavioural donor and Hunter bridge candidate

`Ptah-space` PR `#14` was tested at exact head:

```text
2a2c28d17abd9ad52c8d850f8bbcdba57074194e
```

and squash-merged at:

```text
d05653c5948727b58ead91088447d0b8ac4d9d9b
```

The merged non-operative design package records:

- OpenAI ChatGPT Projects and Work as a public-documentation behavioural donor only;
- no OpenAI source-code reuse, proprietary implementation claim or runtime dependency;
- profile identity `ptah.workspace.ai_project.v1`;
- sixteen existing Ptah primitives composed into a human-and-agent project Workspace;
- fourteen donor behaviours: four directly covered, eight covered by profile composition, zero Core extensions and two rejected patterns;
- explicit rejection of hidden provider memory and implicit global tool access;
- a Hunter–Ptah bridge where Ptah owns durable truth and Grants while Hunter coordinates through bounded context packets;
- ten positive/negative proof fixtures for isolation, authority, provider replacement, scheduled access, handoff and Artifact lineage;
- ten fail-closed regressions and exact-head evidence under immutable Action pins;
- a corrected public README licence statement while retaining the non-claiming runtime boundary.

All ten exact-head workflows passed, including the new AI Project Workspace candidate lane, source/no-build, Rust policy, frozen contracts, generated bindings, host, licence, backend artifact, backend signature and signer-lock gates.

This candidate is a non-blocking future composition design. It neither closes nor adds an ADR-0033 acceptance condition, changes a frozen WP01–WP14 contract, implements a Workspace/context runtime or authorizes Hunter integration.
"""
    new = f"""## Corrected AI Project Workspace behavioural donor boundary

Original donor package:

```text
PR #14 merge: d05653c5948727b58ead91088447d0b8ac4d9d9b
```

Neutral-boundary correction:

```text
PR #15 exact head: {PUBLIC_CORRECTION_HEAD}
PR #15 merge: {PUBLIC_CORRECTION_MERGE}
```

All ten exact-head workflows passed. Corrected Workspace run `{PUBLIC_CORRECTION_RUN}` retained artifact `{PUBLIC_CORRECTION_ARTIFACT}` with digest `{PUBLIC_CORRECTION_DIGEST}`.

Canonical boundary:

- Ptah is the neutral Workspace and execution substrate;
- Hunter owns intelligence, context selection, source judgments, planning and coordination;
- Sergeant independently reviews frozen candidates and issues Sergeant's result;
- humans or calling applications own intent, configured authority, approval, acceptance and release;
- Ptah stores and mechanically enforces configured records but does not select context, rank authority, review, approve, promote or choose a next action.

The donor remains application-experience study only, requires zero Core extensions and does not change ADR-0033, AF03 or runtime authorization.
"""
    replace_once(path, old, new, "CURRENT_STATE donor correction")
    replace_once(
        path,
        """- AF02: ACCEPTED COMPLETE
AF03: READY / NOT STARTED;
""",
        """- AF02: ACCEPTED COMPLETE;
- accepted archive records: 19 total;
- AF02 remaining evidence: 0;
- AF02 acceptance merge: d1d6b47e935e79790db319ad234b4abccafa4d3f;
- AF03: READY / NOT STARTED;
""",
        "CURRENT_STATE AF02/AF03 state",
    )
    replace_once(
        path,
        "AF02 evidence collection is active under its accepted twenty-private mission, with zero records accepted. This archive authorization does not grant source reuse, start AF03, replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation.",
        "AF02 is accepted complete. AF03 remains ready but not started. Archive formation state does not grant source reuse, replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation.",
        "CURRENT_STATE stale AF02 sentence",
    )


def correct_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    anchor = """P01 physical-host closure remains the exact next authorization action.

## Exact next action
"""
    insertion = f"""P01 physical-host closure remains the exact next authorization action.

## Neutral Ptah substrate correction

The Workspace donor was corrected and merged as `{PUBLIC_CORRECTION_MERGE}` after all ten exact-head workflows passed at `{PUBLIC_CORRECTION_HEAD}`.

Use this boundary:

```text
Ptah = neutral platform and mechanical access enforcement
Hunter = intelligence, context selection and coordination
Sergeant = independent reviewer producing Sergeant results
Human/calling application = intent, approval, acceptance and release
```

Ptah does not select context, rank sources, approve work, issue review verdicts, promote candidates or choose the next agent/action. Full private authority record: `{CORRECTION_RECORD}`.

AF03 remains READY / NOT STARTED.

## Exact next action
"""
    replace_once(path, anchor, insertion, "AI_HANDOFF correction")


def correct_index() -> None:
    path = ROOT / "master-plan-index.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("runtime_implementation_authorized") is not False:
        raise CorrectionError("master-plan index unexpectedly authorizes runtime")
    archive = value.get("operational_protocols", {}).get("tenfold_archive_formation", {})
    if archive.get("af03_status") != "ready_not_started" or archive.get("af03_started") is not False:
        raise CorrectionError("AF03 state drifted before correction")
    value["ptah_neutral_substrate_boundary"] = {
        "status": "accepted_correction",
        "correction_record": CORRECTION_RECORD,
        "public_candidate_exact_head": PUBLIC_CORRECTION_HEAD,
        "public_candidate_workflow_run": PUBLIC_CORRECTION_RUN,
        "public_candidate_artifact_id": PUBLIC_CORRECTION_ARTIFACT,
        "public_candidate_artifact_digest": PUBLIC_CORRECTION_DIGEST,
        "public_correction_merge": PUBLIC_CORRECTION_MERGE,
        "ptah_role": "neutral_workspace_and_execution_substrate",
        "context_selection_owner": "caller_application",
        "source_authority_owner": "caller_application",
        "review_authority_owner": "reviewer_application",
        "approval_authority_owner": "human_or_calling_application",
        "next_action_owner": "caller_application",
        "ptah_decision_authority": False,
        "ptah_review_authority": False,
        "af03_started": False,
        "runtime_implementation_authorized": False,
    }
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def correct_validator() -> None:
    path = ROOT / "tools/check_master_plan_closure.py"
    replace_once(
        path,
        '        "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md",\n',
        '        "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md",\n        "work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md",\n        "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md",\n',
        "validator required files",
    )
    replace_once(
        path,
        '    wp16 = read_text(root, "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md")\n',
        '    wp16 = read_text(root, "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md")\n    wp15 = read_text(root, "work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md")\n    neutral_correction = read_text(root, "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md")\n',
        "validator loaded files",
    )
    replace_once(
        path,
        '        "## 11. Context compiler and agent handoff",',
        '        "## 11. Application-owned context and agent handoff",',
        "validator Master Plan heading",
    )
    anchor = '    require_text(master, "Runtime implementation: **NOT AUTHORIZED**", "MASTER_PLAN boundary")\n'
    checks = f'''    require_text(master, "Ptah is the world, not the thinker", "MASTER_PLAN neutral principle")
    require_text(master, "The caller decides meaning, relevance, authority, correctness and next action", "MASTER_PLAN caller authority")
    require_text(master, "Ptah does not select context, rank authority, infer blockers, approve work or choose a next action", "MASTER_PLAN application context boundary")
    require_absent(master, "Before an agent participates, Ptah compiles a bounded packet", "MASTER_PLAN forbidden context compiler")
    require_absent(master, "source-authority service", "MASTER_PLAN forbidden authority service")
'''
    replace_once(path, anchor, anchor + checks, "validator neutral Master Plan checks")
    anchor2 = '    require_text(roadmap, "A15 — Exact-head Online Ptah Alpha acceptance", "roadmap Alpha gate")\n'
    roadmap_checks = '''    require_text(roadmap, "D02 — AI Project Workspace substrate and application adapters", "roadmap neutral D02")
    require_text(roadmap, "Ptah Core performs no context selection, approval, review, promotion or next-action choice", "roadmap neutral proof")
    require_absent(roadmap, "D02 — AI Project Workspace and context compiler", "roadmap forbidden D02")
    require_absent(roadmap, "source-authority service", "roadmap forbidden authority service")
'''
    replace_once(path, anchor2, anchor2 + roadmap_checks, "validator neutral roadmap checks")
    anchor3 = '    require_text(handoff, "Exact next action", "AI handoff next action")\n'
    handoff_checks = f'''    require_text(handoff, "Neutral Ptah substrate correction", "AI handoff correction")
    require_text(handoff, "{PUBLIC_CORRECTION_MERGE}", "AI handoff public correction merge")
    require_text(current, "Corrected AI Project Workspace behavioural donor boundary", "CURRENT_STATE correction")
    require_absent(current, "AF02 evidence collection is active", "CURRENT_STATE stale AF02 state")
    require_text(current, "AF03 remains ready but not started", "CURRENT_STATE AF03 boundary")
    require_text(progress, "AI Project Workspace behavioural donor — neutral substrate correction", "PROGRESS correction")
    require_text(wp15, "Ptah is the neutral Workspace and execution substrate", "Phase 0C-15 correction")
    require_text(neutral_correction, "That language did not represent a new owner decision", "neutral correction provenance")
    neutral_index = index.get("ptah_neutral_substrate_boundary")
    require(isinstance(neutral_index, dict), "neutral substrate machine boundary missing")
    require(neutral_index.get("public_correction_merge") == "{PUBLIC_CORRECTION_MERGE}", "neutral substrate correction merge mismatch")
    require(neutral_index.get("ptah_role") == "neutral_workspace_and_execution_substrate", "neutral Ptah role mismatch")
    require(neutral_index.get("ptah_decision_authority") is False, "Ptah decision authority must remain false")
    require(neutral_index.get("ptah_review_authority") is False, "Ptah review authority must remain false")
    require(neutral_index.get("af03_started") is False, "AF03 cannot start during boundary correction")
'''
    replace_once(path, anchor3, anchor3 + handoff_checks, "validator recovery boundary checks")
    replace_once(
        path,
        '        "runtime_implementation_authorized": False,\n        "files": report_files,',
        '        "runtime_implementation_authorized": False,\n        "neutral_substrate_boundary_restored": True,\n        "ptah_decision_authority": False,\n        "ptah_review_authority": False,\n        "af03_started": False,\n        "files": report_files,',
        "validator report fields",
    )


def correct_tests() -> None:
    path = ROOT / "tools/test_check_master_plan_closure.py"
    replace_once(
        path,
        '    "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md",\n',
        '    "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md",\n    "work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md",\n    "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md",\n',
        "test required files",
    )
    replace_once(
        path,
        '        self.assertEqual(report["programme_a_package_count"], 15)\n',
        '        self.assertEqual(report["programme_a_package_count"], 15)\n        self.assertTrue(report["neutral_substrate_boundary_restored"])\n        self.assertFalse(report["ptah_decision_authority"])\n        self.assertFalse(report["ptah_review_authority"])\n        self.assertFalse(report["af03_started"])\n',
        "test valid correction assertions",
    )
    insertion = '''
    def test_master_plan_cannot_restore_ptah_context_compiler(self) -> None:
        root = self.make_repo()
        path = root / "MASTER_PLAN.md"
        self.replace(
            path,
            "Before an agent participates, Hunter, Sergeant, a human-facing application or another caller may request exact Workspace records and construct its own bounded packet.",
            "Before an agent participates, Ptah compiles a bounded packet.",
        )
        self.assert_invalid(root)

    def test_roadmap_cannot_restore_source_authority_service(self) -> None:
        root = self.make_repo()
        path = root / "IMPLEMENTATION_ROADMAP.md"
        self.replace(
            path,
            "- exact Workspace, Session, Activity, Object and Artifact retrieval APIs;",
            "- source-authority service;",
        )
        self.assert_invalid(root)

    def test_machine_index_cannot_give_ptah_review_authority(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["ptah_neutral_substrate_boundary"]["ptah_review_authority"] = True
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_af03_cannot_start_during_boundary_correction(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["ptah_neutral_substrate_boundary"]["af03_started"] = True
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_stale_af02_active_sentence_is_rejected(self) -> None:
        root = self.make_repo()
        path = root / "CURRENT_STATE.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\nAF02 evidence collection is active under its accepted twenty-private mission.\n",
            encoding="utf-8",
        )
        self.assert_invalid(root)
'''
    replace_once(path, '\n\nif __name__ == "__main__":', insertion + '\n\nif __name__ == "__main__":', "neutral tests")


def main() -> int:
    correct_master_plan()
    correct_roadmap()
    correct_phase0c15()
    correct_progress()
    correct_current_state()
    correct_handoff()
    correct_index()
    correct_validator()
    correct_tests()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    adr33 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    donors = (ROOT / "DONOR_RECOVERY.md").read_text(encoding="utf-8")
    index = json.loads((ROOT / "master-plan-index.json").read_text(encoding="utf-8"))
    if "**Runtime implementation:** NOT AUTHORIZED" not in current or "**Runtime implementation:** AUTHORIZED" in current:
        raise CorrectionError("runtime non-authorization boundary failed")
    if "Status: proposed" not in adr33:
        raise CorrectionError("ADR-0033 is no longer proposed")
    if "COMPLETE AND FROZEN" not in donors:
        raise CorrectionError("Phase 0A donor state is no longer frozen")
    archive = index["operational_protocols"]["tenfold_archive_formation"]
    if archive.get("af03_status") != "ready_not_started" or archive.get("af03_started") is not False:
        raise CorrectionError("AF03 changed during neutral-boundary correction")
    print("neutral Ptah substrate plan boundary restored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
