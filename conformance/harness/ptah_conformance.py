from __future__ import annotations

import argparse
import json
import re
import sys
from collections import deque
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator

URN_RE = re.compile(r"^urn:ptah:schema:[a-z0-9_.:-]+:[0-9]+\.[0-9]+\.[0-9]+$")
PTAH_REF_RE = re.compile(r"^urn:ptah:schema:")


@dataclass(frozen=True)
class CheckResult:
    code: str
    status: str
    path: str
    message: str


class Harness:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.results: list[CheckResult] = []
        self.documents: dict[Path, Any] = {}
        self.schema_ids: dict[str, Path] = {}
        self.machine_names: dict[str, Path] = {}

    def add(self, code: str, status: str, path: Path | str, message: str) -> None:
        rel = str(path if isinstance(path, str) else path.relative_to(self.root))
        self.results.append(CheckResult(code, status, rel, message))

    def load_json(self, path: Path) -> Any | None:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # precise error retained in report
            self.add("JSON_PARSE", "fail", path, f"invalid JSON: {exc}")
            return None
        self.documents[path] = data
        self.add("JSON_PARSE", "pass", path, "valid JSON")
        return data

    def discover(self) -> None:
        roots = [
            self.root / "schemas" / "phase-0b",
            self.root / "state-machines" / "phase-0b",
            self.root / "conformance" / "fixtures" / "phase-0b",
        ]
        for base in roots:
            if not base.exists():
                self.add("DISCOVERY_ROOT", "fail", base, "required root missing")
                continue
            for path in sorted(base.rglob("*.json")):
                self.load_json(path)

    @staticmethod
    def walk_refs(value: Any) -> Iterable[str]:
        if isinstance(value, dict):
            ref = value.get("$ref")
            if isinstance(ref, str):
                yield ref
            for child in value.values():
                yield from Harness.walk_refs(child)
        elif isinstance(value, list):
            for child in value:
                yield from Harness.walk_refs(child)

    def validate_schemas(self) -> None:
        for path, doc in self.documents.items():
            if not path.name.endswith(".schema.json"):
                continue
            if not isinstance(doc, dict):
                self.add("SCHEMA_OBJECT", "fail", path, "schema root is not an object")
                continue
            schema_id = doc.get("$id")
            if not isinstance(schema_id, str) or not URN_RE.match(schema_id):
                self.add("SCHEMA_ID", "fail", path, "missing or invalid versioned Ptah URN")
            elif schema_id in self.schema_ids:
                self.add("SCHEMA_ID_UNIQUE", "fail", path, f"duplicate of {self.schema_ids[schema_id]}")
            else:
                self.schema_ids[schema_id] = path
                self.add("SCHEMA_ID_UNIQUE", "pass", path, schema_id)
            try:
                Draft202012Validator.check_schema(doc)
            except Exception as exc:
                self.add("SCHEMA_META", "fail", path, str(exc))
            else:
                self.add("SCHEMA_META", "pass", path, "valid JSON Schema 2020-12 structure")

        known = set(self.schema_ids)
        for path, doc in self.documents.items():
            if not path.name.endswith(".schema.json"):
                continue
            for raw_ref in self.walk_refs(doc):
                base = raw_ref.split("#", 1)[0]
                if PTAH_REF_RE.match(base) and base not in known:
                    self.add("SCHEMA_REF_LOCAL", "fail", path, f"unresolved local URN: {base}")
                elif PTAH_REF_RE.match(base):
                    self.add("SCHEMA_REF_LOCAL", "pass", path, base)

    def validate_catalogs(self) -> None:
        for path, doc in self.documents.items():
            if "schema-catalog" not in path.name:
                continue
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
                if isinstance(entry, dict):
                    repo_path = entry.get("repository_path")
                    schema_id = entry.get("schema_id")
                    if isinstance(repo_path, str):
                        target = self.root / repo_path
                    if isinstance(schema_id, str) and schema_id not in self.schema_ids:
                        self.add("CATALOG_SCHEMA_ID", "fail", path, f"unknown schema id {schema_id}")
                elif isinstance(entry, str):
                    template = doc.get("schema_path_template")
                    if isinstance(template, str):
                        target = self.root / template.format(name=entry)
                if target is None:
                    self.add("CATALOG_ENTRY", "fail", path, f"unsupported entry {entry!r}")
                elif not target.exists():
                    self.add("CATALOG_PATH", "fail", path, f"missing {target.relative_to(self.root)}")
                else:
                    self.add("CATALOG_PATH", "pass", path, str(target.relative_to(self.root)))

    def validate_state_machines(self) -> None:
        for path, doc in self.documents.items():
            if "state-machines/phase-0b" not in path.as_posix():
                continue
            if not isinstance(doc, dict):
                self.add("MACHINE_OBJECT", "fail", path, "machine root is not an object")
                continue
            name = doc.get("name")
            states = doc.get("states")
            initial = doc.get("initial_state")
            transitions = doc.get("transitions")
            if not isinstance(name, str):
                self.add("MACHINE_NAME", "fail", path, "missing name")
                continue
            if name in self.machine_names:
                self.add("MACHINE_NAME_UNIQUE", "fail", path, f"duplicate of {self.machine_names[name]}")
            else:
                self.machine_names[name] = path
                self.add("MACHINE_NAME_UNIQUE", "pass", path, name)
            if not isinstance(states, list) or not states or len(states) != len(set(states)):
                self.add("MACHINE_STATES", "fail", path, "states missing, empty or duplicated")
                continue
            state_set = set(states)
            if initial not in state_set:
                self.add("MACHINE_INITIAL", "fail", path, "initial state is not declared")
            if not isinstance(transitions, list):
                self.add("MACHINE_TRANSITIONS", "fail", path, "transitions missing")
                continue
            graph: dict[str, set[str]] = {state: set() for state in states}
            for transition in transitions:
                if not isinstance(transition, dict):
                    self.add("MACHINE_TRANSITION", "fail", path, "transition is not an object")
                    continue
                src, dst = transition.get("from"), transition.get("to")
                if dst not in state_set:
                    self.add("MACHINE_TRANSITION", "fail", path, f"unknown target {dst!r}")
                    continue
                if src == "*":
                    for state in states:
                        graph[state].add(dst)
                elif src not in state_set:
                    self.add("MACHINE_TRANSITION", "fail", path, f"unknown source {src!r}")
                else:
                    graph[src].add(dst)
            reachable: set[str] = set()
            queue: deque[str] = deque([initial]) if initial in state_set else deque()
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
        ids: dict[str, Path] = {}
        for path, doc in self.documents.items():
            if "conformance/fixtures/phase-0b" not in path.as_posix():
                continue
            if not isinstance(doc, dict):
                self.add("FIXTURE_OBJECT", "fail", path, "fixture suite root is not an object")
                continue
            cases = doc.get("cases")
            if not isinstance(cases, list) or not cases:
                self.add("FIXTURE_CASES", "fail", path, "fixture suite has no cases")
                continue
            for case in cases:
                if not isinstance(case, dict):
                    self.add("FIXTURE_CASE", "fail", path, "case is not an object")
                    continue
                case_id = case.get("id")
                expected = case.get("expected")
                if not isinstance(case_id, str) or not case_id:
                    self.add("FIXTURE_ID", "fail", path, "case missing id")
                    continue
                global_id = f"{doc.get('suite_id', path)}::{case_id}"
                if global_id in ids:
                    self.add("FIXTURE_ID_UNIQUE", "fail", path, f"duplicate {case_id}")
                else:
                    ids[global_id] = path
                if expected not in {"valid", "invalid"}:
                    self.add("FIXTURE_EXPECTED", "fail", path, f"{case_id}: expected must be valid/invalid")
                elif expected == "invalid" and not isinstance(case.get("expected_code"), str):
                    self.add("FIXTURE_ERROR_CODE", "fail", path, f"{case_id}: invalid case lacks expected_code")
                else:
                    self.add("FIXTURE_CASE", "pass", path, case_id)

    def run(self) -> dict[str, Any]:
        self.discover()
        self.validate_schemas()
        self.validate_catalogs()
        self.validate_state_machines()
        self.validate_fixtures()
        failed = sum(r.status == "fail" for r in self.results)
        passed = sum(r.status == "pass" for r in self.results)
        return {
            "harness_version": "0.1.0",
            "root": str(self.root),
            "summary": {"passed": passed, "failed": failed, "status": "pass" if failed == 0 else "fail"},
            "results": [asdict(result) for result in self.results],
        }


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
