# Donor Record — OpenHands Runtime Family

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — COMPUTER/AGENT INTERACTION DONOR  
**Inspected:** 2026-07-17

## Identity

### Transition repository

- Canonical URL: https://github.com/OpenHands/OpenHands
- Pinned commit: `f012a4017c27cefbc8c1f22fa0ac87aac2028d1a`
- Licence: MIT outside `enterprise/`; enterprise directory has separate terms

### Software Agent SDK

- Canonical URL: https://github.com/OpenHands/software-agent-sdk
- Pinned commit: `51c102b9c0348bbdd4e6a84b1ac4199e0d77f827`
- Licence: MIT

### Agent Canvas

- Canonical URL: https://github.com/OpenHands/agent-canvas
- Pinned commit: `6fae7348d3e1f1bbfc9dba8215d8755cd8186187`
- Licence: requires repository-level verification before code reuse; architecture studied from public source

- Activity: Active and currently split across dedicated repositories
- Classification: Agent/computer interaction, multi-backend frontend and workload donor
- Ptah targets: local/remote backend switching, terminal/file tools, event trajectories and agent-facing computer contracts

## Files/components inspected

- transition repository `README.md` and `LICENSE`
- Software Agent SDK `README.md`
- Agent Canvas `README.md`
- documented Agent Server and Automation Server boundaries
- local, Docker, VM and remote-backend deployment paths

## Verified capabilities and patterns

- Agent Canvas connects to multiple local, remote and cloud Agent Server backends.
- Frontend and backend can be run together or separately.
- Agent Server exposes a REST API and can run multiple agents on one machine.
- Software Agent SDK supports local workspaces and ephemeral Docker/Kubernetes workspaces.
- Terminal, file-editor and task-tracker tools are first-class agent tools.
- Multiple agents and long-running automation use cases are supported.
- ACP-compatible third-party agents can be connected through a common client protocol.
- The current code is actively transitioning into `software-agent-sdk` and `agent-canvas`, so the old monorepo should not be treated as the only canonical source.

## What OpenHands completes

- A useful separation between computer/workspace tools and the intelligence using them.
- Multi-backend frontend patterns.
- Event/trajectory and conversation-driven tool invocation.
- Direct local execution, Docker-backed execution and remote server paths.
- A practical human interface for switching between active backends.
- Agent-facing terminal, file and computer-use patterns.

## Important limitations

- OpenHands is primarily a coding-agent/control-center product, not a neutral universal workspace.
- The runtime normally organizes work around agents and conversations rather than Ptah Activities and Objects.
- Running directly on a host can grant broad filesystem access; Ptah must represent provider and caller isolation explicitly.
- The architecture is in transition, so exact canonical code locations must be tracked carefully.
- Device, firmware, media, document and application-world requirements remain outside its core identity.
- It does not replace Temporal-style durable activity history or Ptah's Node Protocol.

## Must not be inherited

- Agent identity, reasoning loop or model routing as Ptah Core.
- Conversation as the universal unit of work.
- Broad host access as a default without an explicit provider choice.
- OpenHands-specific backend and automation schemas as Ptah truth.
- Enterprise-only code or terms copied into public Ptah.
- A single-user or code-only workspace assumption.

## Integration decision

**ADAPT TOOL/EVENT/FRONTEND PATTERNS; HOST AS WORKLOAD.**

OpenHands is a completion donor for `EXEC-001`, `UI-002`, `CORE-004` and agent-facing facility APIs. It may later run inside Ptah or connect as a caller, but it does not define Ptah's world model.

## Native Ptah gap

- neutral activity/event contract independent of conversations;
- object/artifact registration for terminal and file outputs;
- provider-neutral isolation and workspace ownership;
- direct human operation without an agent;
- concurrency across unrelated workloads;
- durable recovery, cancellation, replay and provenance;
- facility contracts beyond coding tools.

## Exit strategy

Ptah tools remain usable through REST, SDK, CLI, MCP and direct human interfaces. OpenHands/ACP compatibility can be provided by an adapter without becoming mandatory.

## Validation required

- Connect an OpenHands-compatible caller to Ptah terminal and file facilities through a neutral adapter.
- Prove the same facilities work without any agent or conversation.
- Run two independent agent backends while unrelated Ptah activities continue.
- Capture tool invocations, outputs and trajectories as Ptah activity evidence.
- Prove OpenHands can be removed without changing Ptah's object, activity or workspace contracts.
