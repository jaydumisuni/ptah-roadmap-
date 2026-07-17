# Donor Record — Daytona

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/daytonaio/daytona
- Last public release studied: `v0.190.0`
- Pinned release commit: `01c502bb1f1ff8f2885d0cd490e043736083dca8`
- Release date: 2026-06-23
- Licence at pin: AGPL-3.0
- Activity: Public repository is no longer maintained; core development moved private in June 2026
- Classification: Tier A architecture-history donor, not a selected foundation dependency
- Ptah targets: Workspace Provider contract, environment lifecycle, snapshots, runner placement and control/compute separation

## Files and changes inspected

- `README.md`
- `LICENSE` at `v0.190.0`
- `apps/runner/cmd/runner/main.go` at `v0.190.0`
- PR `#4714` — pause/resume lifecycle
- PR `#5087` — sandbox-class selection and schedulable-runner validation

## Verified capabilities and patterns

- Interface, control and compute plane separation.
- Programmatic sandbox lifecycle through API, SDK and CLI.
- Filesystem, process, code execution, Git, PTY, preview, VNC and log-streaming surfaces.
- Persistent environments, volumes, snapshots and archive/recovery concepts.
- Runner services, Docker event monitoring, health checks and resource metrics.
- OpenTelemetry logging and tracing.
- Runner selection by environment class and region.
- Lifecycle state-machine work for pause, resume, archive, restore, resize, fork and snapshot.
- CI and end-to-end validation around runner and API changes.

## Important limits discovered

- The public codebase is no longer maintained.
- New core development is private, preventing Ptah from relying on its future direction.
- AGPL-3.0 creates a strong licence boundary that requires formal review before code reuse or modification.
- Pause support was not universal across runners at the inspected checkpoint.
- The platform carries organisation, billing, quota and hosted-service assumptions that are not Ptah's core identity.
- Daytona models a sandbox platform; Ptah must also support native processes, remote hosts, full VMs, devices and platform-specific nodes.
- Its full deployment stack is much larger than Ptah's first vertical slice requires.

## Patterns to study

1. Provider lifecycle and state transitions.
2. Control-plane and runner separation.
3. Resource-class and runner-capability matching.
4. Snapshot, fork, archive and restore semantics.
5. SDK/API parity across languages.
6. Runner health, metrics and periodic state reconciliation.
7. Filesystem, process, PTY, preview and VNC toolbox surfaces.
8. Structural availability checks before accepting work.

## Must not be inherited

- AGPL source copied into Ptah Core without explicit licence approval.
- Dependence on an unmaintained public codebase.
- Daytona-specific organisation, SaaS, billing and quota models.
- A universal assumption that every Ptah workspace is a Daytona sandbox.
- Unsupported lifecycle operations presented as universally available.
- The complete production stack as a requirement for Ptah v1.

## Native Ptah gap

Ptah needs a provider-neutral contract that supports:

- local process, container, remote Linux host, VM and device providers;
- explicit capability flags for pause, fork, memory snapshot and migration;
- activity IDs and idempotency keys for lifecycle operations;
- object, storage and session references independent of provider filesystems;
- connection to the Ptah Node Protocol;
- cross-provider validation tests and an exit strategy.

## Integration decision

**STUDY ONLY — architecture and protocol patterns.**

Daytona is a strong historical donor for `CORE-001` and `EXEC-002`, but it is not selected as a direct Ptah dependency or source-code foundation.

## Primary implementation direction

Ptah will own the Workspace Provider contract. The first implementation should use native Ptah code over local Linux and OCI/container machinery. Coder, E2B, Dev Containers and other providers remain comparison and exit donors.

## Validation required

Create one provider conformance suite covering create, start, stop, pause when supported, resume, snapshot, archive, restore, fork when supported, resize, destroy, terminal, process, files, ports and status. Prove two independent workspaces can run concurrently without Ptah depending on Daytona schemas.