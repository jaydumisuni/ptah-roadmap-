#!/usr/bin/env python3
"""Run AF01 acceptance sync without modifying workflow files in the bot commit."""
from __future__ import annotations

import apply_archive_af01_acceptance_sync as base


def no_workflow_write() -> None:
    """The permanent workflow is updated by the authenticated branch edit."""


base.sync_workflow = no_workflow_write

if __name__ == "__main__":
    raise SystemExit(base.main())
