# Phase 0A — WP02A Workspace and Execution Composition

**Status:** FIRST-PASS DONOR COMPOSITION COMPLETE  
**Date:** 2026-07-17  
**Runtime code:** NOT STARTED

## Purpose

Complete the workspace and execution side of the OpenClaw–Daytona boundary by inspecting the capabilities each lacked and assembling a stronger Ptah donor composition.

## Donors inspected and saved

- OpenClaw — Node/gateway protocol patterns
- Daytona — sandbox lifecycle and control/compute separation
- Coder — long-lived human workspaces, templates, workspace agents and secure editor access
- E2B — compact agent-facing sandbox APIs
- E2B Desktop — graphical desktop/application control and streaming
- Development Containers Specification — portable development-environment description
- Dev Container CLI — reference implementation and lockfile/lifecycle behavior
- DevPod — provider portability across local, remote, Kubernetes and cloud machines
- containerd and OCI specifications — owned execution substrate, images, runtime bundles, snapshots and distribution
- OpenHands runtime family — multi-backend computer/agent interaction, tools and frontend patterns

## Composite result

No donor is the Ptah workspace runtime by itself.

```text
OpenClaw
  Node identity, gateway and reconnect patterns

Daytona
  Lifecycle state, runner and sandbox patterns

Coder
  Persistent human workspace, template and workspace-agent patterns

E2B
  Small automation-facing sandbox API patterns

E2B Desktop
  Graphical application and display-control patterns

Dev Containers + CLI
  Portable environment definition and reproducible feature locks

DevPod
  Provider portability and local/remote/cloud equivalence

containerd + OCI
  Owned container execution, images, snapshots, content and runtime standards

OpenHands
  Tool/computer interaction and multi-backend caller/frontend patterns

Native Ptah
  Workspace, Activity, Object, Session, Node and Facility contracts that join them
```

## Provisional architecture direction

1. Ptah owns the Workspace Provider contract.
2. Ptah supports several provider families rather than one sandbox vendor.
3. Native local-process and OCI providers are the first owned implementations.
4. OCI compatibility is foundational for container providers.
5. Dev Container definitions are supported through an adapter, not used as the universal Ptah schema.
6. Coder, E2B and DevPod may later connect as optional providers or compatibility adapters.
7. Graphical application/display sessions remain separate from ordinary process and terminal activities.
8. Agent systems such as OpenHands are callers/workloads, not Ptah's identity.
9. Provider limitations such as pause, fork, memory checkpoint, multi-stream display and migration must be declared as capabilities rather than implied universally.
10. Ptah object, activity and session identity survives provider replacement.

## Remaining gaps before runtime design closure

- durable Activity history and crash recovery;
- internal live event fabric and replay;
- end-to-end observability and resource accounting;
- internal THETECHGUY process, worker, terminal and recovery patterns;
- credential-reference design;
- port/service registry;
- exact local-process and OCI provider conformance contract;
- snapshot/checkpoint semantics across unlike providers;
- large-stream transport;
- full licence review before any donor source adaptation.

## Saved evidence

- `donors/CODER.md`
- `donors/E2B.md`
- `donors/E2B-DESKTOP.md`
- `donors/DEV-CONTAINERS-SPEC.md`
- `donors/DEV-CONTAINERS-CLI.md`
- `donors/DEVPOD.md`
- `donors/CONTAINERD-OCI.md`
- `donors/OPENHANDS.md`
- earlier `donors/OPENCLAW.md`
- earlier `donors/DAYTONA.md`
- `decisions/ADR-0001-NODE-WORKSPACE-BOUNDARY.md`
- `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`

## Provisional requirement closure

- `CORE-001 Persistent workspace model` — composite candidate selected; internal recovery and contract proof remain.
- `EXEC-001 Terminal and process supervision` — donor composition identified; native implementation and recovery still open.
- `EXEC-002 OCI/container workspace provider` — mature machinery and completion donors identified; provider contract and live proof remain.
- `APP-002 Linux graphical application runtime` — donor patterns identified; display/stream contract and alternative gateway still open.
- `UI-002 Activity and multi-backend presentation` — OpenHands/Coder patterns identified; Ptah-specific Activity Centre remains native.
- `SESSION-001 Checkpoint/resume` — lifecycle donors identified, but Temporal/event/storage work must complete the closure.

## Next inspection unit

Temporal, NATS/JetStream and OpenTelemetry will complete the activity, event, recovery and observability side of the core runtime cluster.
