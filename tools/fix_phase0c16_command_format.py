#!/usr/bin/env python3
"""Repair only flattened multiline proof commands in CURRENT_STATE.md."""
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "CURRENT_STATE.md"
text = path.read_text(encoding="utf-8")

replacements = {
    "python3 tools/run_pinned_host_proof.py   --repo-root .   --output evidence/phase0c/pinned-host-candidate": (
        "python3 tools/run_pinned_host_proof.py \\\n"
        "  --repo-root . \\\n"
        "  --output evidence/phase0c/pinned-host-candidate"
    ),
    "python3 tools/retain_verified_pinned_host_evidence.py   --repo-root .   --bundle-dir evidence/phase0c/pinned-host-candidate   --output-dir evidence/phase0c/pinned-host-durable-candidate": (
        "python3 tools/retain_verified_pinned_host_evidence.py \\\n"
        "  --repo-root . \\\n"
        "  --bundle-dir evidence/phase0c/pinned-host-candidate \\\n"
        "  --output-dir evidence/phase0c/pinned-host-durable-candidate"
    ),
}

for old, new in replacements.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected one flattened command, found {count}: {old[:60]}")
    text = text.replace(old, new, 1)

if "**Runtime implementation:** NOT AUTHORIZED" not in text:
    raise SystemExit("runtime non-authorization missing")
if "**Runtime implementation:** AUTHORIZED" in text:
    raise SystemExit("runtime authorization appeared")

path.write_text(text, encoding="utf-8")
print("CURRENT_STATE.md proof-command formatting repaired")
