# Donor Record — E2B

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — COMPLETION DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/e2b-dev/E2B
- Default branch: `main`
- Pinned commit: `e68b876689d20cee68c1d589802ec45c91d9f873`
- Licence: Apache-2.0
- Activity: Active at the inspected pin
- Classification: Agent-facing sandbox API and contract donor
- Ptah targets: programmatic sandbox lifecycle, command execution, files, templates and isolated execution APIs

## Files/components inspected

- `README.md`
- `LICENSE`
- public Python and JavaScript SDK examples
- self-hosting boundary referenced from `e2b-dev/infra`
- Code Interpreter SDK relationship

## Verified capabilities and patterns

- Small, direct JavaScript/TypeScript and Python APIs for creating a sandbox and running commands.
- Isolated cloud sandboxes designed for generated code and programmatic callers.
- Template-based environments.
- Separate general Sandbox and Code Interpreter SDK layers.
- Apache-2.0 licence at the inspected pin.
- Self-hosting documentation exists through a separate infrastructure repository.

## What E2B completes beyond OpenClaw, Daytona and Coder

- A cleaner agent-facing API than the larger workspace platforms.
- Simple create/run/file-oriented contracts suitable for automation clients.
- A useful separation between generic sandbox infrastructure and higher-level code-interpreter behavior.
- A reference for language SDK ergonomics.

## Missing capabilities for Ptah

- The normal public path assumes E2B API keys and E2B-hosted infrastructure.
- The documented self-host path is Terraform/cloud oriented; the README does not claim general single-Linux-machine support.
- Sandboxes are not the complete Ptah workspace, object, activity, node or session model.
- Long-lived human workspace, rich graphical application, device and firmware requirements are outside the core E2B API.
- Ptah requires local-first and THETECHGUY-owned hardware operation as a first-class path.
- Durable activity history, cross-node ownership and provider-neutral recovery remain Ptah gaps.

## Must not be inherited

- E2B cloud credentials as a mandatory Ptah dependency.
- A hosted-only assumption.
- AI-generated-code product identity.
- E2B-specific sandbox IDs or templates as canonical Ptah records.
- One sandbox lifetime equated with one Ptah workspace or session.

## Integration decision

**ADAPT API PATTERNS; OPTIONAL PROVIDER LATER.**

E2B is a completion donor for `CORE-001`, `EXEC-001`, `EXEC-002` and public SDK design. Apache-2.0 permits selective adaptation with attribution, but Ptah should first own local/OCI providers.

## Native Ptah gap

Ptah must add:

- provider-neutral lifecycle and capabilities;
- local Linux and owned-hardware execution;
- persistent workspace identity;
- concurrent activity registry;
- object and artifact registration;
- durable recovery and checkpoint semantics;
- direct human operation and facility breadth.

## Exit strategy

E2B can remain an optional provider behind Ptah's Workspace Provider contract. The same API must work with native local/OCI, remote host, VM and other providers.

## Validation required

- Run identical conformance calls against native Ptah and optional E2B-backed providers.
- Prove commands, files, cancellation and outputs map to Ptah activities and objects.
- Prove failure or removal of E2B does not break Ptah's local path.
