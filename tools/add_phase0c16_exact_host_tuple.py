#!/usr/bin/env python3
"""Add one exact machine-readable host tuple to the physical closure record."""
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md"
text = path.read_text(encoding="utf-8")
old = """The machine must report:

- Ubuntu Server `24.04.4 LTS`;
"""
new = """The machine must report:

Exact target tuple: Ubuntu Server 24.04.4 LTS | x86_64 | 6.8.0-136-generic

- Ubuntu Server `24.04.4 LTS`;
"""
if text.count(old) != 1:
    raise SystemExit(f"expected one host target insertion point, found {text.count(old)}")
text = text.replace(old, new, 1)
if "Runtime implementation: NOT AUTHORIZED" not in text:
    raise SystemExit("runtime non-authorization boundary missing")
path.write_text(text, encoding="utf-8")
print("exact physical-host tuple recorded")
