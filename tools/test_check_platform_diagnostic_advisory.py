#!/usr/bin/env python3
"""Adversarial regressions for Phase 0C-18 diagnostics and worker execution."""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from check_platform_diagnostic_advisory import REQUIRED_FILES, ValidationError, validate_repo

ROOT = Path(__file__).resolve().parents[1]
INDEX_KEY = "platform_diagnostic_and_worker_execution"


class DiagnosticAndWorkerValidationTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temporary = Path(tempfile.mkdtemp(prefix="ptah-diagnostic-worker-"))
        self.addCleanup(lambda: shutil.rmtree(temporary, ignore_errors=True))
        for relative in REQUIRED_FILES:
            source = ROOT / relative
            destination = temporary / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        return temporary

    def replace(self, root: Path, relative: Path, old: str, new: str) -> None:
        path = root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def mutate_index(self, root: Path, key: str, value: object) -> None:
        path = root / "master-plan-index.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["product_clarifications"][INDEX_KEY][key] = value
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def assert_invalid(self, root: Path) -> None:
        with self.assertRaises(ValidationError):
            validate_repo(root)

    def test_valid_candidate(self) -> None:
        result = validate_repo(self.make_repo())
        self.assertEqual(result["status"], "candidate_valid_non_authorizing")
        self.assertTrue(result["may_request_upgrade"])
        self.assertTrue(result["may_execute_caller_selected_ten_for_two"])
        self.assertEqual(result["ten_for_two_multiplier"], 10)
        self.assertEqual(result["ten_for_two_minimum_worker_slots"], 20)
        self.assertFalse(result["may_choose_caller_work"])
        self.assertFalse(result["may_invent_semantic_subtasks"])
        self.assertFalse(result["may_accept_worker_result"])
        self.assertFalse(result["may_install_upgrade_autonomously"])
        self.assertFalse(result["af03_started"])

    def test_protocol_cannot_become_consciousness_claim(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "not product consciousness, business judgment or task planning",
                     "product consciousness and autonomous planning")
        self.assert_invalid(root)

    def test_caller_work_choice_cannot_move_to_ptah(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "Caller chooses the work and supplies or selects the execution recipe",
                     "Ptah chooses the work and execution recipe")
        self.assert_invalid(root)

    def test_sergeant_review_authority_cannot_be_borrowed(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "Ptah does not borrow Sergeant's review authority",
                     "Ptah borrows Sergeant's review authority")
        self.assert_invalid(root)

    def test_new_core_entity_cannot_be_required(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "No new Core entity is required",
                     "A new autonomous Core entity is required")
        self.assert_invalid(root)

    def test_facts_and_suggestions_cannot_be_conflated(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "observed facts from suggestions",
                     "observed facts and suggestions as one decision")
        self.assert_invalid(root)

    def test_self_approval_prohibition_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "approve its own advisory",
                     "automatically accept its own advisory")
        self.assert_invalid(root)

    def test_autonomous_install_prohibition_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "install, upgrade, remove or replace software without configured authority",
                     "install and replace software without asking")
        self.assert_invalid(root)

    def test_unrelated_work_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "block unrelated work merely because an upgrade is available",
                     "block all work whenever an upgrade is available")
        self.assert_invalid(root)

    def test_acknowledgement_cannot_equal_resolution(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "acknowledgement does not equal successful upgrade",
                     "acknowledgement equals successful upgrade")
        self.assert_invalid(root)

    def test_worker_multiplier_cannot_drift(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "human-equivalent workers × 10",
                     "human-equivalent workers × 4")
        self.assert_invalid(root)

    def test_worker_minimum_cannot_drift(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "twenty bounded worker slots",
                     "four bounded worker slots")
        self.assert_invalid(root)

    def test_worker_recipe_cannot_be_optional(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "caller-selected or caller-supplied formation recipe",
                     "Ptah-invented formation recipe")
        self.assert_invalid(root)

    def test_semantic_subtasks_cannot_be_invented(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "add semantic subtasks that were not supplied",
                     "add any semantic subtasks it considers useful")
        self.assert_invalid(root)

    def test_worker_completion_cannot_equal_acceptance(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "worker completion as human/application acceptance",
                     "worker completion as automatic acceptance")
        self.assert_invalid(root)

    def test_worker_independence_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "run independent Attempts concurrently",
                     "reuse one Attempt for every worker")
        self.assert_invalid(root)

    def test_worker_retry_must_remain_policy_bounded(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "retry or replace a failed worker Attempt when the submitted recipe and Policy permit it",
                     "retry indefinitely without submitted Policy")
        self.assert_invalid(root)

    def test_submitted_merge_rule_cannot_be_replaced_by_ptah_judgment(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
                     "assemble outputs according to the submitted merge rule",
                     "choose the best answer according to Ptah judgment")
        self.assert_invalid(root)

    def test_adr_worker_equation_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md"),
                     "apply `worker capacity = max(20, human-equivalent workers × 10)`",
                     "apply an unspecified number of workers")
        self.assert_invalid(root)

    def test_master_plan_diagnostic_principle_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("MASTER_PLAN.md"),
                     "Ptah may diagnose its own platform condition without choosing the caller's work",
                     "Ptah may choose the caller's work")
        self.assert_invalid(root)

    def test_master_plan_worker_principle_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("MASTER_PLAN.md"),
                     "Caller-given work may use bounded worker formations",
                     "Ptah may invent and assign work")
        self.assert_invalid(root)

    def test_master_plan_autonomous_upgrade_cannot_appear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("MASTER_PLAN.md"),
                     "may not approve, purchase, install or activate it",
                     "may approve, purchase, install and activate it")
        self.assert_invalid(root)

    def test_roadmap_a02_cannot_lose_gap_advisory(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("IMPLEMENTATION_ROADMAP.md"),
                     "bounded missing-capability and degradation advisory generation",
                     "generic status message")
        self.assert_invalid(root)

    def test_roadmap_worker_capacity_proof_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("IMPLEMENTATION_ROADMAP.md"),
                     "two-human-equivalent ten-for-two Recipe creates twenty bounded worker slots",
                     "worker count is unspecified")
        self.assert_invalid(root)

    def test_roadmap_worker_acceptance_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("IMPLEMENTATION_ROADMAP.md"),
                     "worker completion cannot become result acceptance",
                     "worker completion automatically accepts the result")
        self.assert_invalid(root)

    def test_roadmap_a15_cannot_allow_autonomous_install(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("IMPLEMENTATION_ROADMAP.md"),
                     "Ptah cannot choose caller work or autonomously install an upgrade",
                     "Ptah can choose caller work and autonomously install an upgrade")
        self.assert_invalid(root)

    def test_machine_index_cannot_disable_ten_for_two(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "may_execute_caller_selected_ten_for_two", False)
        self.assert_invalid(root)

    def test_machine_index_multiplier_cannot_drift(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "ten_for_two_multiplier", 5)
        self.assert_invalid(root)

    def test_machine_index_minimum_slots_cannot_drift(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "ten_for_two_minimum_worker_slots", 10)
        self.assert_invalid(root)

    def test_machine_index_cannot_remove_caller_job_requirement(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "caller_job_required", False)
        self.assert_invalid(root)

    def test_machine_index_cannot_remove_recipe_requirement(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "caller_recipe_or_plan_required", False)
        self.assert_invalid(root)

    def test_machine_index_cannot_grant_work_choice(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "may_choose_caller_work", True)
        self.assert_invalid(root)

    def test_machine_index_cannot_grant_semantic_subtasks(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "may_invent_semantic_subtasks", True)
        self.assert_invalid(root)

    def test_machine_index_cannot_grant_result_acceptance(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "may_accept_worker_result", True)
        self.assert_invalid(root)

    def test_machine_index_cannot_grant_upgrade_approval(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "may_approve_upgrade", True)
        self.assert_invalid(root)

    def test_machine_index_cannot_grant_autonomous_install(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "may_install_upgrade_autonomously", True)
        self.assert_invalid(root)

    def test_machine_index_cannot_block_unrelated_work(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "may_block_unrelated_capable_work", True)
        self.assert_invalid(root)

    def test_af03_cannot_start(self) -> None:
        root = self.make_repo()
        campaign = root / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md"
        text = campaign.read_text(encoding="utf-8")
        before, after = text.split("## AF03", 1)
        af03, rest = after.split("## AF04", 1)
        self.assertIn("- status: READY / NOT STARTED", af03)
        campaign.write_text(before + "## AF03" + af03.replace("- status: READY / NOT STARTED", "- status: ACTIVE", 1) + "## AF04" + rest, encoding="utf-8")
        self.assert_invalid(root)

    def test_adr0033_cannot_be_accepted(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md"),
                     "Status: proposed", "Status: accepted")
        self.assert_invalid(root)

    def test_runtime_cannot_be_authorized(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("CURRENT_STATE.md"),
                     "**Runtime implementation:** NOT AUTHORIZED",
                     "**Runtime implementation:** AUTHORIZED")
        self.assert_invalid(root)

    def test_phase0a_cannot_reopen(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("DONOR_RECOVERY.md"),
                     "**Status:** COMPLETE AND FROZEN",
                     "**Status:** REOPENED")
        self.assert_invalid(root)


if __name__ == "__main__":
    unittest.main()
