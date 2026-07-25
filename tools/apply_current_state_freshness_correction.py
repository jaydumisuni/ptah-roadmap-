#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "CURRENT_STATE.md"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one anchor, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    text = PATH.read_text(encoding="utf-8")
    text = replace_once(text, "**Last updated:** 2026-07-21", "**Last updated:** 2026-07-25", "last-updated date")
    text = replace_once(text, "## Phase 0C candidate decisions and evidence now recorded", "## Phase 0C decisions and evidence now recorded", "Phase 0C heading")
    text = replace_once(text, "The following records are merged or awaiting this evidence-sync merge:", "The following records are merged:", "merged-record wording")
    PATH.write_text(text, encoding="utf-8")
    print("CURRENT_STATE freshness correction applied")


if __name__ == "__main__":
    main()
