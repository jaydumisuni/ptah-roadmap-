from __future__ import annotations

import argparse
import json
import re
import sys
from collections import deque
from pathlib import Path
from typing import Any

from ptah_conformance import Harness as BaseHarness

_VERSION_RE = re.compile(r"\.v(?P<version>[0-9]+\.[0-9]+\.[0-9]+)\.json$")


class Harness(BaseHarness):
    @staticmethod
    def machine_shape(doc: dict[str, Any]) -> tuple[str | None, str | None, list[str], list[str], list[tuple[list[str], str]]]:
        name = doc.get("name") or doc.get("state_machine_name") or doc.get("machine")
        version = doc.get("version") or doc.get("state_machine_version")
        raw_states = doc.get("states")
        states: list[str] = []
        if isinstance(raw_states, list):
            for value in raw_states:
                if isinstance(value, str):
                    states.append(value)
                elif isinstance(value, dict) and isinstance(value.get("name"), str):
                    states.append(value["name"])
        initial_raw = doc.get("initial_state")
        if isinstance(initial_raw, str):
            initials = [initial_raw]
        else:
            initials = [v for v in doc.get("initial_states", []) if isinstance(v, str)]
        transitions: list[tuple[list[str], str]] = []
        raw_transitions = doc.get("transitions", [])
        for transition in raw_transitions if isinstance(raw_transitions, list) else []:
            if not isinstance(transition, dict):
                continue
            dst = transition.get("to") or transition.get("to_state")
            raw_src = transition.get("from")
            if raw_src is None:
                raw_src = transition.get("from_states")
            if isinstance(raw_src, str):
                sources = [raw_src]
            elif isinstance(raw_src, list):
                sources = [v for v in raw_src if isinstance(v, str)]
            else:
                sources = []
            if isinstance(dst, str):
                transitions.append((sources, dst))
        return (
            name if isinstance(name, str) else None,
            version if isinstance(version, str) else None,
            states,
            initials,
            transitions,
        )

    def validate_catalogs(self) -> None:
        by_dir: dict[Path, list[Path]] = {}
        for path in self.documents:
            if "schema-catalog" in path.name:
                by_dir.setdefault(path.parent, []).append(path)
        selected = {sorted(paths)[-1] for paths in by_dir.values()}
        for path in selected:
            doc = self.documents[path]
            if not isinstance(doc, dict):
                self.add("CATALOG_OBJECT", "fail", path, "catalog root is not an object")
                continue
            catalog_id = doc.get("catalog_id")
            if not isinstance(catalog_id, str) or not catalog_id.startswith("urn:ptah:schema-catalog:"):
                self.add("CATALOG_ID", "fail", path, "missing catalog_id")
            else:
                self.add("CATALOG_ID", "pass", path, catalog_id)
            entries = doc.get("schemas", [])
            if not isinstance(entries, list) or not entries:
                self.add("CATALOG_SCHEMAS", "fail", path, "catalog has no schema entries")
                continue
            for entry in entries:
                target: Path | None = None
                declared_id: str | None = None
                compact = False
                if isinstance(entry, dict):
                    repo_path = entry.get("repository_path")
                    declared_id = entry.get("schema_id") if isinstance(entry.get("schema_id"), str) else None
                    if isinstance(repo_path, str):
                        target = self.root / repo_path
                elif isinstance(entry, str) and isinstance(doc.get("schema_path_template"), str):
                    compact = True
                    target = self.root / doc["schema_path_template"].format(name=entry)
                if target is None:
                    self.add("CATALOG_ENTRY", "fail", path, f"unsupported entry {entry!r}")
                    continue
                if not target.exists():
                    self.add("CATALOG_PATH", "fail", path, f"missing {target.relative_to(self.root)}")
                    continue
                self.add("CATALOG_PATH", "pass", path, str(target.relative_to(self.root)))
                target_doc = self.documents.get(target)
                canonical_id = target_doc.get("$id") if isinstance(target_doc, dict) else None
                if not isinstance(canonical_id, str) or canonical_id not in self.schema_ids:
                    self.add("CATALOG_TARGET_ID", "fail", path, f"target lacks canonical loaded $id: {target.relative_to(self.root)}")
                elif compact:
                    self.add("CATALOG_SCHEMA_ID", "pass", path, canonical_id)
                elif declared_id == canonical_id:
                    self.add("CATALOG_SCHEMA_ID", "pass", path, canonical_id)
                elif declared_id:
                    self.add("CATALOG_SCHEMA_ALIAS", "warning", path, f"legacy alias {declared_id} -> {canonical_id}")
                else:
                    self.add("CATALOG_SCHEMA_ID", "fail", path, f"entry lacks schema_id for {canonical_id}")

    def validate_state_machines(self) -> None:
        seen: dict[tuple[str, str], Path] = {}
        for path, doc in self.documents.items():
            if "state-machines/phase-0b" not in path.as_posix():
                continue
            if not isinstance(doc, dict):
                self.add("MACHINE_OBJECT", "fail", path, "machine root is not an object")
                continue
            name, version, states, initials, transitions = self.machine_shape(doc)
            if not name:
                self.add("MACHINE_NAME", "fail", path, "missing machine identity")
                continue
            if not version:
                match = _VERSION_RE.search(path.name)
                version = match.group("version") if match else "unversioned"
            identity = (name, version)
            if identity in seen:
                self.add("MACHINE_NAME_UNIQUE", "fail", path, f"duplicate of {seen[identity]}")
            else:
                seen[identity] = path
                self.add("MACHINE_NAME_UNIQUE", "pass", path, f"{name}@{version}")
            if not states or len(states) != len(set(states)):
                self.add("MACHINE_STATES", "fail", path, "states missing, empty or duplicated")
                continue
            state_set = set(states)
            if not initials or any(initial not in state_set for initial in initials):
                self.add("MACHINE_INITIAL", "fail", path, "initial state is not declared")
                continue
            graph = {state: set() for state in states}
            for sources, dst in transitions:
                if dst not in state_set:
                    self.add("MACHINE_TRANSITION", "fail", path, f"unknown target {dst!r}")
                    continue
                for src in sources:
                    if src == "*":
                        for state in states:
                            graph[state].add(dst)
                    elif src not in state_set:
                        self.add("MACHINE_TRANSITION", "fail", path, f"unknown source {src!r}")
                    else:
                        graph[src].add(dst)
            reachable: set[str] = set()
            queue: deque[str] = deque(initials)
            while queue:
                state = queue.popleft()
                if state in reachable:
                    continue
                reachable.add(state)
                queue.extend(graph[state] - reachable)
            missing = state_set - reachable
            if missing:
                self.add("MACHINE_REACHABILITY", "fail", path, f"unreachable states: {sorted(missing)}")
            else:
                self.add("MACHINE_REACHABILITY", "pass", path, "all states reachable")

    def validate_fixtures(self) -> None:
        ids: set[str] = set()
        accepted = {
            "valid", "invalid", "semantic_valid", "semantic_invalid",
            "structurally_valid_semantically_rejected_for_current_state",
            "disposition_required",
        }
        invalid_like = {
            "invalid", "semantic_invalid",
            "structurally_valid_semantically_rejected_for_current_state",
            "disposition_required",
        }
        for path, doc in self.documents.items():
            if "conformance/fixtures/phase-0b" not in path.as_posix():
                continue
            if not isinstance(doc, dict) or not isinstance(doc.get("cases"), list) or not doc["cases"]:
                self.add("FIXTURE_CASES", "fail", path, "fixture suite has no cases")
                continue
            for case in doc["cases"]:
                if not isinstance(case, dict) or not isinstance(case.get("id"), str):
                    self.add("FIXTURE_ID", "fail", path, "case missing id")
                    continue
                global_id = f"{doc.get('suite_id', path)}::{case['id']}"
                if global_id in ids:
                    self.add("FIXTURE_ID_UNIQUE", "fail", path, f"duplicate {case['id']}")
                ids.add(global_id)
                expected = case.get("expected")
                if expected not in accepted:
                    self.add("FIXTURE_EXPECTED", "fail", path, f"{case['id']}: unsupported expected value {expected!r}")
                elif expected in invalid_like and not isinstance(case.get("expected_code"), str):
                    self.add("FIXTURE_ERROR_CODE", "fail", path, f"{case['id']}: invalid case lacks expected_code")
                else:
                    self.add("FIXTURE_CASE", "pass", path, case["id"])

    def run(self) -> dict[str, Any]:
        report = super().run()
        report["harness_version"] = "0.1.2"
        return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run offline Ptah Phase 0B contract conformance checks")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    report = Harness(args.root).run()
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
