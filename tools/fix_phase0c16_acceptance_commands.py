#!/usr/bin/env python3
"""Restore copy-safe multiline proof commands after the acceptance transform."""
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
    if "Runtime implementation: AUTHORIZED" in text:
        raise SystemExit(f"{relative}: runtime authorization appeared")
    path.write_text(text, encoding="utf-8")

print("accepted CURRENT_STATE.md and AI_HANDOFF.md commands restored")
