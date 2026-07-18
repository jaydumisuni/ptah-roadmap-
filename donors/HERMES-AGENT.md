# Donor Record — Hermes Agent

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — OPTIONAL CALLER/WORKLOAD, SKILL/MEMORY/PROVIDER AND SECURITY-BOUNDARY DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/NousResearch/hermes-agent
- Owner/organisation: `NousResearch`
- Default branch: `main`
- Pinned commit: `7fd419e5e6a0ac53f934a69226262c41ba130a2c`
- Licence: MIT
- Activity: Active
- Classification: self-improving agent application, provider-switching client, skills/memory system, gateway/TUI and multi-backend workload donor
- Ptah targets: optional consumer/workload integration, skill/plugin risk boundaries, external reasoning ownership, provider adapters, terminal backend selection and security-posture evidence

## Files/components inspected

- `README.md`
- `LICENSE`
- `SECURITY.md`
- current commit/repository identity
- documented provider switching, memory, skills, MCP, terminal-backend, subagent, gateway and scheduling features

## Verified capabilities and patterns

### Agent/application layer

- Presents itself as a self-improving agent with memory, skill creation/improvement and cross-session conversation search.
- Supports multiple model providers and provider switching without changing application code.
- Exposes a terminal UI and messaging gateway across several channels.
- Supports scheduled automations, isolated subagents and tool calls from generated Python scripts.
- Supports local, Docker, SSH, Singularity, Modal and Daytona terminal backends.
- Includes MCP integration and an agentskills-compatible skill system.
- Includes research-oriented trajectory generation and compression.
- Offers native Windows, Linux/macOS/WSL and Termux paths with different dependency profiles.

### Security and isolation model

- Explicitly defines Hermes as a single-tenant personal agent.
- States that the only load-bearing boundary against an adversarial LLM is OS-level isolation.
- Treats approval gates, redaction, pattern scanning and tool allowlists as heuristics, not containment.
- Distinguishes terminal-backend isolation from wrapping the whole agent process.
- Terminal-backend isolation confines shell/file operations routed through the backend but does not contain in-process plugins, hooks, skills, MCP subprocesses or every code-execution path.
- Whole-process wrapping applies filesystem, network, process and inference policy to the complete agent process tree.
- Recommends whole-process isolation for untrusted web/email/channel/MCP inputs and shared or production deployments.
- Filters credentials passed to lower-trust subprocesses, while explicitly noting this is not containment for in-process code.
- Skills and plugins may execute arbitrary code with full agent-process privileges; operator review is the current trust boundary before installation.
- External surfaces require authorization; session identifiers are routing handles rather than authorization boundaries.
- Current network adapters use caller allowlists but do not provide fine-grained per-caller capabilities within one adapter instance.

## What Hermes Agent contributes

- A realistic consumer for Ptah Workspaces, terminal backends, MCP adapters, plugins, knowledge and scheduled Activities.
- Strong evidence that provider/model choice belongs behind a caller-owned adapter rather than Ptah Core.
- A useful comparison for local, container, SSH and hosted execution backends.
- Clear separation between in-process heuristics and OS-level isolation.
- Evidence that shell-only sandboxing does not contain plugins, skills, hooks, MCP or the entire agent process.
- A strong optional workload for testing Ptah's plugin, knowledge, browser, terminal, schedule and multi-Node Facilities.
- Useful migration/adapter lessons for OpenClaw-compatible skills/settings without requiring either product to become Ptah Core.

## Important limitations for Ptah

- Hermes is an opinionated reasoning and relationship product, not a neutral digital-world substrate.
- Its memory, self-improvement, personalities, prompts, model selection and user model belong to the caller/product.
- Its security model is intentionally single-tenant and does not provide Ptah's Workspace, caller, Object or Facility permission granularity.
- Plugins and skills load in-process with full agent privileges.
- Operator review is not sufficient proof for public/shared multi-tenant execution.
- Terminal-backend isolation does not contain all execution paths.
- The default local terminal backend can reach resources available to the host user.
- Environment scrubbing does not protect against malicious in-process code.
- Messaging/gateway identities and session IDs are not Ptah authorization identities.
- Hosted providers, Portal, Modal, Daytona and external tool gateways are optional dependencies, not owned Ptah foundations.
- Self-improving skills and memory promotion can create policy, provenance and rollback risk.
- Agent-level task completion or a self-generated skill is not proof, review or caller acceptance.
- One-line remote installers and automatic dependency setup require independent source/signature/provenance controls before Ptah use.

## Must not be inherited

- Hermes identity, personality, reasoning, memory or self-improvement policy inside Ptah Core;
- automatic conversation-to-memory or task-to-skill promotion as a platform default;
- in-process skill/plugin execution under full Core privileges;
- approval regexes, redaction or allowlists described as containment;
- shell-backend isolation claimed to contain the full agent process;
- session identifiers treated as authorization;
- one single-tenant allowlist model used for multi-user Ptah Workspaces;
- provider/API keys stored or passed without Ptah credential references and scopes;
- external model/provider selection embedded into Ptah policy;
- agent task success promoted to proof or Sergeant review;
- mutable remote installation scripts accepted without pin/signature/provenance;
- Hermes-specific gateway/channel architecture made mandatory.

## Integration decision

**HOST HERMES AS AN OPTIONAL APPLICATION/CALLER/WORKLOAD AND ADAPT SELECTED SECURITY, PROVIDER AND BACKEND-SELECTION LESSONS; DO NOT USE IT AS PTAH CORE.**

Recommended relationship:

1. Hermes runs inside a Ptah Workspace or stronger isolation Provider appropriate to its input trust.
2. Ptah exposes approved terminal, browser, MCP, knowledge, schedule and Artifact Facilities.
3. Hermes retains its own reasoning, memory, skills, identity and acceptance policy.
4. Ptah maps Hermes tool/work requests to durable Activities and Receipts without trusting Hermes session/tool IDs as canonical.
5. Hermes plugins/skills are represented as Ptah Packages and run under explicit runtime/isolation classes.
6. Whole-process isolation is required when Hermes consumes untrusted external inputs or third-party plugins.
7. Provider and credential access is mediated through Ptah references/scopes rather than inherited environment access.
8. Self-improvement outputs remain proposed Package/Knowledge revisions until separately reviewed and approved.

## Licence decision

The MIT licence permits study, wrapping and selective adaptation. Every bundled/optional dependency, third-party skill, plugin, model, provider and installer Artifact requires separate licence and provenance review.

## Native Ptah gap

Ptah must define:

- external caller/application identity and permission mapping;
- provider/model capability, cost and credential adapters;
- whole-process versus terminal-only isolation classification;
- plugin/skill Package, Release, Installation and Activation identities;
- self-improvement proposal, review, approval and rollback records;
- Conversation, Knowledge Source, Lesson and caller-memory separation;
- scheduled Activity and delivery records;
- subagent/worker Activities and resource budgets;
- gateway/session routing separate from authorization;
- per-caller and per-Workspace capabilities;
- external tool/MCP response trust and citation records;
- migration/import receipts from OpenClaw or other callers;
- runtime health, checkpoint and removal behavior.

## Exit strategy

Ptah's Facilities and contracts remain independent. Hermes may be replaced by Hunter, OpenClaw, Dify, another client or a human operator without changing Workspace, Object, Activity, Plugin, Knowledge or provider identities.

## Validation required

1. Run Hermes under terminal-backend isolation and prove which paths remain outside that boundary.
2. Run the whole process inside an OCI/VM policy and verify plugins, MCP, hooks, skills and code execution are contained.
3. Map one Hermes tool request to a durable Ptah Activity and Receipt.
4. Keep Hermes reasoning/session/memory IDs adapter-local.
5. Deny one caller/provider/credential scope without affecting unrelated Workspaces.
6. Install a skill/plugin only through Ptah Package review, pinning and isolation controls.
7. Treat a self-generated skill or memory as a proposal requiring review before promotion.
8. Interrupt, resume and migrate a scheduled or long-running Hermes Activity through Ptah.
9. Remove Hermes without changing the underlying Ptah Objects, Knowledge Sources or Artifacts.
10. Replace one provider backend without changing Ptah Query/Activity identity.
