# Donor Record — Deno

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PERMISSION-SCOPED LIGHTWEIGHT SCRIPT/TOOL RUNTIME CANDIDATE  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/denoland/deno
- Default branch: `main`
- Pinned commit: `c71e43af07c3392c788286e20481998f6004b68d`
- Licence: MIT
- Activity: Active
- Primary languages: Rust and TypeScript/JavaScript runtime APIs
- Classification: secure-by-default JavaScript, TypeScript and WebAssembly runtime donor
- Ptah targets: lightweight Facility/tool execution, permission-scoped scripts, MCP/plugin helpers, data transforms and portable automation tasks

## Files/components inspected

- `README.md`
- `LICENSE.md`
- `runtime/permissions/lib.rs`
- permission prompt, broker, audit and checked-path boundaries

## Verified capabilities and patterns

- Runs JavaScript, TypeScript and WebAssembly on V8 with Rust/Tokio internals.
- Denies sensitive capabilities by default unless explicitly granted.
- Supports granular permission classes such as filesystem read/write, network, environment and process execution.
- Permission state distinguishes granted, partially granted, prompt, denied, partially denied and ignored.
- Read/write checks can distinguish no-follow access classes.
- Permission requests can be audited to a file or OpenTelemetry sink, optionally with stack traces.
- Permission decisions can be mediated by a broker.
- Supports compiled standalone executables with declared permissions.
- Runs on Linux, macOS and Windows.
- Provides standard web APIs and package/runtime tooling suitable for portable small services and scripts.

## What Deno completes

- A lighter script/tool runtime between an unrestricted shell and a full container/VM.
- Explicit capability requests rather than ambient filesystem/network/environment authority.
- Audit hooks useful for Facility receipts and telemetry.
- TypeScript/JavaScript execution without a separate build step for many tasks.
- Portable local automation, small service and MCP-server implementation paths.
- A good runtime candidate for public plugins whose requirements fit its permission model.

## Important limitations for Ptah

- Deno permissions are runtime checks, not strong kernel/VM isolation.
- Native libraries, FFI, subprocesses or granted broad permissions can escape the intended lightweight boundary.
- `--allow-all` defeats the security model.
- Interactive permission prompts are unsuitable for unattended Activities unless mediated explicitly.
- Package imports, npm compatibility and remote dependencies add supply-chain risk.
- Permission audits prove attempted access, not semantic correctness or absence of all side channels.
- One script may still consume excessive CPU/RAM/disk or hang without external resource controls.
- Deno process/module/cache IDs are not Ptah Facility, Plugin or Activity identities.
- Compiled standalone binaries still require source/dependency/provenance records.
- Network permission by host does not automatically express URL/path/protocol/business restrictions.
- Deno does not provide durable Activity recovery, Object storage or plugin governance.

## Must not be inherited

- `--allow-all` as a normal plugin/tool mode;
- Deno permission flags used as the canonical Ptah permission schema;
- interactive prompts relied upon for background execution;
- remote/npm imports accepted without pin/hash/provenance;
- FFI, subprocess or unrestricted environment access bundled into ordinary script permission;
- Deno runtime/module/cache IDs as canonical Ptah identities;
- permission grant interpreted as caller approval or proof of safe behavior;
- Deno used as a substitute for container/VM isolation for untrusted native workloads.

## Integration decision

**ADOPT DENO AS THE PRIMARY LIGHTWEIGHT PERMISSION-SCOPED JAVASCRIPT/TYPESCRIPT TOOL-RUNTIME CANDIDATE, BELOW OCI/VM ISOLATION.**

Recommended role:

1. small transformation and automation Facilities;
2. MCP servers/adapters;
3. lightweight plugin/service execution;
4. structured data or Object transforms that do not need native dependencies;
5. portable scripts across Nodes.

Ptah owns the Facility/Plugin manifest, permission mapping, source/dependency hashes, resource limits, Activity/receipt identity and stronger-isolation escalation.

## Native Ptah gap

Ptah must define:

- Facility/Plugin permission vocabulary independent of Deno flags;
- mapping to exact read/write Object roots, network destinations, environment keys and subprocesses;
- non-interactive approval and permission-broker contract;
- package/source/lockfile/dependency provenance;
- runtime/version/cache identity;
- CPU/RAM/time/disk/network budgets outside the runtime;
- FFI/native/subprocess risk classes;
- audit-event to receipt/OTel mapping;
- compiled-tool Artifact and signature records;
- container/VM escalation rules;
- backend replacement tests.

## Exit strategy

Ptah's Tool Runtime contract remains implementable through Deno, Node.js sandboxes, WebAssembly/WASI, Python subprocesses, OCI containers or other runtimes. Deno-specific permissions remain adapter metadata.

## Validation required

1. Run a script with only one approved Object read and one output write scope.
2. Deny undeclared network, environment, path and subprocess access.
3. Audit permission checks into receipts/OTel without leaking sensitive values.
4. Refuse unattended interactive prompts and route additional access through a Ptah approval request.
5. Pin package/source/lockfile hashes and reject dependency drift.
6. Enforce external CPU/RAM/time limits and terminate a runaway script safely.
7. Escalate an FFI/native workload to OCI/VM isolation instead of weakening Deno permissions.
8. Replace Deno for one tool without changing Facility/Activity identity.
