from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ptah_conformance import Harness


class HarnessTests(unittest.TestCase):
    def make_root(self) -> Path:
        root = Path(tempfile.mkdtemp())
        for rel in ("schemas/phase-0b/x", "state-machines/phase-0b", "conformance/fixtures/phase-0b/wp"):
            (root / rel).mkdir(parents=True, exist_ok=True)
        return root

    def write(self, root: Path, rel: str, value: object) -> None:
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def valid_schema(self) -> dict:
        return {"$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "urn:ptah:schema:test:item:0.1.0", "type": "object"}

    def test_valid_minimal_tree_passes(self) -> None:
        root = self.make_root()
        self.write(root, "schemas/phase-0b/x/item.v0.1.0.schema.json", self.valid_schema())
        self.write(root, "schemas/phase-0b/x/schema-catalog.v0.1.0.json", {
            "catalog_id": "urn:ptah:schema-catalog:test:0.1.0",
            "schemas": [{"schema_id": "urn:ptah:schema:test:item:0.1.0", "repository_path": "schemas/phase-0b/x/item.v0.1.0.schema.json"}],
        })
        self.write(root, "state-machines/phase-0b/test.json", {
            "name": "test.item.lifecycle", "initial_state": "new", "states": ["new", "done"],
            "transitions": [{"from": "new", "to": "done"}],
        })
        self.write(root, "conformance/fixtures/phase-0b/wp/cases.json", {
            "suite_id": "test", "cases": [{"id": "OK", "expected": "valid"}, {"id": "BAD", "expected": "invalid", "expected_code": "EXPECTED"}],
        })
        report = Harness(root).run()
        self.assertEqual(report["summary"]["failed"], 0, report)

    def test_duplicate_schema_id_fails(self) -> None:
        root = self.make_root()
        self.write(root, "schemas/phase-0b/x/a.v0.1.0.schema.json", self.valid_schema())
        self.write(root, "schemas/phase-0b/x/b.v0.1.0.schema.json", self.valid_schema())
        report = Harness(root).run()
        self.assertTrue(any(r["code"] == "SCHEMA_ID_UNIQUE" and r["status"] == "fail" for r in report["results"]))

    def test_unreachable_state_fails(self) -> None:
        root = self.make_root()
        self.write(root, "state-machines/phase-0b/test.json", {
            "name": "test.item.lifecycle", "initial_state": "new", "states": ["new", "done", "orphan"],
            "transitions": [{"from": "new", "to": "done"}],
        })
        report = Harness(root).run()
        self.assertTrue(any(r["code"] == "MACHINE_REACHABILITY" and r["status"] == "fail" for r in report["results"]))

    def test_invalid_fixture_requires_error_code(self) -> None:
        root = self.make_root()
        self.write(root, "conformance/fixtures/phase-0b/wp/cases.json", {
            "suite_id": "test", "cases": [{"id": "BAD", "expected": "invalid"}],
        })
        report = Harness(root).run()
        self.assertTrue(any(r["code"] == "FIXTURE_ERROR_CODE" and r["status"] == "fail" for r in report["results"]))


if __name__ == "__main__":
    unittest.main()
