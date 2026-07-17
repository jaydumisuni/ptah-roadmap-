# Phase 0A Work Package 01 — OpenClaw and Daytona

**Status:** COMPLETE FOR FIRST-PASS DONOR RECOVERY  
**Date:** 2026-07-17

## Objective

Inspect OpenClaw and Daytona side by side to determine the boundary between:

- Ptah Node Protocol;
- Ptah Workspace Provider Contract;
- live relay transport;
- terminals and reconnect;
- OCI/container environments.

No runtime implementation or donor code copying was permitted.

## Outputs

- `donors/OPENCLAW.md`
- `donors/DAYTONA.md`
- `decisions/ADR-0001-NODE-WORKSPACE-BOUNDARY.md`
- populated first closure paths in `REQUIREMENT_CLOSURE_MATRIX.md`
- updated `PROGRESS.md`
- updated `CURRENT_STATE.md`

## Result

### OpenClaw

Selected as the primary architecture donor for versioned node/gateway protocol patterns. Ptah will adapt narrow MIT-compatible ideas but will not depend on OpenClaw Core or inherit its assistant, channel, reasoning or memory identity.

### Daytona

Selected as an architecture-history donor for provider lifecycle, runner separation, snapshots and environment APIs. It is not selected as a dependency or code foundation because the public repository is unmaintained and the inspected release is AGPL-3.0.

### Boundary

- Node connects a capability host.
- Workspace Provider creates and manages environments on a node.
- Activity tracks operations.
- Object/Storage owns durable data identity.
- Session Vault references all of the above.

These concepts must remain separate.

## Evidence gate

This work package completed donor understanding and candidate design placement. It did not freeze the public contract.

The boundary becomes freeze-eligible only after Phase 0B schemas and the ADR proof checklist are reviewed and passed.

## Next work package

Phase 0A WP02:

- Temporal;
- NATS Server and JetStream;
- selected client SDKs.

The next decision must separate live event transport from durable activity history and recovery.