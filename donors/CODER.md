# Donor Record — Coder

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — COMPLETION DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/coder/coder
- Default branch: `main`
- Pinned commit: `2ac2295b1eb02c978e4e75708a9b6bd2d596f154`
- Licence: AGPL-3.0
- Activity: Active at the inspected pin
- Classification: Workspace completion donor; architecture and protocol study
- Ptah targets: persistent human workspaces, templates, workspace agents, secure access, idle lifecycle and editor integration

## Files/components inspected

- `README.md`
- `LICENSE`
- `agent/agent.go`
- `agent/agent_test.go`
- `coderd/workspaceagents.go`
- `codersdk/workspacesdk/workspacesdk.go`
- current workspace-create WebSocket tests at the pinned commit

## Verified capabilities and patterns

- Self-hosted control plane for long-lived development workspaces.
- Terraform-defined templates capable of provisioning VMs, Kubernetes pods, containers and other infrastructure.
- Workspace agent installed inside the environment rather than assuming the control plane directly owns every process.
- Secure workspace access through a tunnel/agent model.
- IDE/editor integration and direct human access.
- Idle shutdown and restart lifecycle.
- PostgreSQL-backed server state and broad workspace-management surfaces.
- Dynamic workspace parameters and WebSocket-driven creation UX.
- Active source, tests, CI and release process at the inspected pin.

## What Coder completes beyond OpenClaw and Daytona

- A stronger long-lived human workspace model than an agent gateway alone.
- A template-based description of workspace infrastructure.
- Editor and developer access patterns.
- A workspace-resident agent that bridges the environment back to the control plane.
- Idle lifecycle and workspace ownership concepts.

## Missing capabilities for Ptah

- Coder is development-workspace centric; Ptah must also host media, firmware, devices, graphical applications and arbitrary facilities.
- Terraform templates are too infrastructure-oriented to become Ptah's universal workspace definition.
- Object, activity, artifact and session graphs are not Ptah-equivalent.
- Coder does not replace Ptah's Node Protocol, durable activity runtime or universal decomposition model.
- Its policy, user, governance and commercial feature split are not Ptah's public identity.
- AGPL-3.0 prevents casual source extraction into Ptah Core.

## Must not be inherited

- Coder-specific organisations, roles, premium boundaries and AI-agent product model.
- Terraform as the only provider contract.
- The assumption that every Ptah environment is primarily a coding workspace.
- AGPL source copied into Ptah without formal licence approval.
- Tight coupling between workspace UX and Coder's generated API/database models.

## Integration decision

**STUDY AND PROTOCOL-COMPATIBILITY ONLY.**

Coder is a completion donor for `CORE-001`, `EXEC-001`, `UI-001` and `SESSION-001`. Ptah will not depend on Coder as its control plane. Coder workspaces may later be supported through a Workspace Provider adapter.

## Native Ptah gap

Ptah must own:

- provider-neutral workspace and template contracts;
- workspace-to-node placement;
- object/activity/session separation;
- facility-aware workspace capabilities;
- direct human and system access;
- cross-provider conformance tests;
- checkpoint and recovery semantics independent of Coder.

## Exit strategy

The Ptah contracts remain implementable by local-process, OCI, Dev Container, VM, remote-host, Coder or other providers. No Coder schema becomes canonical Ptah truth.

## Validation required

- Connect an optional Coder-backed provider through the same conformance suite as native providers.
- Prove long-lived workspace stop/start without losing Ptah object and activity identity.
- Prove direct human terminal/editor access while independent background activities continue.
- Prove Coder can be removed without changing Ptah's public contracts.
