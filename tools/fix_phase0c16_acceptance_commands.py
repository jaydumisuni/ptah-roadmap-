#!/usr/bin/env python3
"""Repair copy-safe accepted records and their accepted-state validator."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PROOF_FLAT = (
    "python3 tools/run_pinned_host_proof.py   --repo-root .   "
    "--output evidence/phase0c/pinned-host-candidate"
)
PROOF_MULTILINE = (
    "python3 tools/run_pinned_host_proof.py \\\n"
    "  --repo-root . \\\n"
    "  --output evidence/phase0c/pinned-host-candidate"
)
RETENTION_FLAT = (
    "python3 tools/retain_verified_pinned_host_evidence.py   --repo-root .   "
    "--bundle-dir evidence/phase0c/pinned-host-candidate   "
    "--output-dir evidence/phase0c/pinned-host-durable-candidate"
)
RETENTION_MULTILINE = (
    "python3 tools/retain_verified_pinned_host_evidence.py \\\n"
    "  --repo-root . \\\n"
    "  --bundle-dir evidence/phase0c/pinned-host-candidate \\\n"
    "  --output-dir evidence/phase0c/pinned-host-durable-candidate"
)

for relative in ("CURRENT_STATE.md", "AI_HANDOFF.md"):
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    for old, new, label in (
        (PROOF_FLAT, PROOF_MULTILINE, "proof"),
        (RETENTION_FLAT, RETENTION_MULTILINE, "retention"),
    ):
        count = text.count(old)
        if count != 1:
            raise SystemExit(
                f"{relative}: expected one flattened {label} command, found {count}"
            )
        text = text.replace(old, new, 1)

    if relative == "CURRENT_STATE.md":
        if "**Runtime implementation:** NOT AUTHORIZED" not in text:
            raise SystemExit("CURRENT_STATE.md: non-authorization state missing")
        if "**Runtime implementation:** AUTHORIZED" in text:
            raise SystemExit("CURRENT_STATE.md: canonical runtime authorization appeared")
    else:
        if "Runtime implementation: NOT AUTHORIZED" not in text:
            raise SystemExit("AI_HANDOFF.md: non-authorization state missing")
        if "\nRuntime implementation: AUTHORIZED\n" in text:
            raise SystemExit("AI_HANDOFF.md: current runtime authorization appeared")

    path.write_text(text, encoding="utf-8")

validator = ROOT / "tools/check_master_plan_closure.py"
text = validator.read_text(encoding="utf-8")
old = 'require_text(handoff, "Safest next action", "AI handoff next action")'
new = 'require_text(handoff, "Exact next action", "AI handoff next action")'
if text.count(old) != 1:
    raise SystemExit(
        f"accepted validator: expected one old handoff heading assertion, found {text.count(old)}"
    )
validator.write_text(text.replace(old, new, 1), encoding="utf-8")

print("accepted records and accepted-state handoff validation repaired")
