# D029 — TouchPilot

Status: candidate record — paired evidence complete

Primary Archivist: `AF07-P08`

Independent Verifier: `AF07-V08`

Inspected: 2026-07-23

## Canonical source identity

- source: `touchpilot/touchpilot`;
- default branch: `main`;
- exact inspected commit: `3dedb1deda373a8202e95953119a773ca130503d`;
- root licence: MIT;
- repository role: local-first Android agent runtime using AccessibilityService and typed tools;
- archived: false.

## Primary evidence packet

TouchPilot implements normalized screen context, tap/type/scroll/app actions, typed risk levels, approval prompts, local routing, encrypted API-key storage, audit logs, skills and compatibility testing.

## Independent verification packet

AccessibilityService state may be incomplete or stale; OEM/API compatibility is manual-first and currently scoped to documented matrices. Model routing, cloud fallback, approvals, Android permissions and tool outcomes are separate trust surfaces. Agent decisions and tool acknowledgements do not prove semantic post-conditions.

## Contradiction and supersession

The canonical repository is resolved and matches the expected semantic Android donor role. It remains an application/workload donor, not Ptah Device identity, authority or mandatory agent runtime.

## Bounded outcome

`accepted_for_archive_mit_semantic_android_agent_donor_with_accessibility_model_approval_compatibility_and_postcondition_limits`

Allowed reuse: study or adapt typed Android tools, normalized screen context, local routing, approval and audit patterns behind Ptah Device/Application Session boundaries.

Restrictions: preserve MIT notices; require exact API/OEM/device tests, Lease/Fence and post-condition read-back; keep model/provider decisions separate from authority; do not inherit agent identity or make TouchPilot Ptah Core.

This outcome does not authorize implementation.