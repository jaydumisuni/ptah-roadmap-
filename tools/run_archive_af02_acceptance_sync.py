#!/usr/bin/env python3
"""Run the AF02 acceptance synchronizer with ambiguous replacements anchored."""
from __future__ import annotations

from pathlib import Path

root = Path(__file__).resolve().parents[1]
source_path = root / "tools/apply_archive_af02_acceptance_sync.py"
source = source_path.read_text(encoding="utf-8")

patches = (
    (
        '''replace_once("tools/check_archive_af02.py", '"af03_authorized": False,', '"af03_ready": True,\\n        "af03_started": False,\\n        "af03_authorized": False,',)''',
        '''replace_once("tools/check_archive_af02.py", '        "verifier_worker_count": 10,\\n        "phase_0a_reopened": False,\\n        "adr_0033_accepted": False,\\n        "runtime_implementation_authorized": False,\\n        "af03_authorized": False,\\n    }\\n    for key, value in expected_top.items():', '        "verifier_worker_count": 10,\\n        "phase_0a_reopened": False,\\n        "adr_0033_accepted": False,\\n        "runtime_implementation_authorized": False,\\n        "af03_ready": True,\\n        "af03_started": False,\\n        "af03_authorized": False,\\n    }\\n    for key, value in expected_top.items():')''',
    ),
    (
        '''replace_once("tools/check_archive_formation.py", '"accepted_archive_record_count": 9,', '"accepted_archive_record_count": 19,')''',
        '''replace_once("tools/check_archive_formation.py", '        "af01_status": "accepted_complete",\\n        "accepted_archive_record_count": 9,\\n        "blocked_archive_record_count": 1,', '        "af01_status": "accepted_complete",\\n        "accepted_archive_record_count": 19,\\n        "blocked_archive_record_count": 1,')''',
    ),
)

for old, new in patches:
    count = source.count(old)
    if count != 1:
        raise SystemExit(f"acceptance wrapper patch mismatch: expected 1, got {count}: {old[:100]}")
    source = source.replace(old, new, 1)

compiled = compile(source, str(source_path), "exec")
exec(compiled, {"__name__": "__main__", "__file__": str(source_path)})
