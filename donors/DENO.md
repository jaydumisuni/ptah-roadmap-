# Donor Record — Deno

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PRIMARY PERMISSION-SCOPED LIGHTWEIGHT SCRIPT/TOOL RUNTIME CANDIDATE  
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
- current commit/activity evidence
- permission prompt, broker, audit, checked-path, no-follow and standalone-compile boundaries

## Verified capabilities and patterns

### Runtime

- Runs JavaScript, TypeScript and WebAssembly on V8 with Rust and Tokio internals.
- Runs on Linux, macOS and Windows.
- Standard web APIs, JSR/npm compatibility and runtime tooling support portable small services and scripts.
- Sensitive operations require explicit runtime permissions; a networked server example requires `--allow-net`.
- Standalone executables can be compiled with declared permission flags.

### Permission model

- Permission state distinguishes granted, partially granted, prompt, denied, partially denied and ignored.
- A permission broker can independently return allow or deny, including a custom denial message.
- Interactive prompting is a separate component rather than being embedded in each operation.
- Permission errors retain requested access, permission name, custom message and effective permission state.
- File-open access distinguishes read, write, read/write and no-follow variants.
- Checked-path wrappers retain whether a path was canonicalized and restrict ordinary construction outside the permission crate.
- A fully granted permission can take a fast path, but attempted access is still written to the configured audit sink first.

### Audit and observability

- Permission checks can emit JSON-line audit records to a file.
- Audit records include version, time, permission, requested value and an optional captured stack.
- The same permission events can be sent to an OpenTelemetry callback.
- Audit failure or absence does not itself revoke permissions; Ptah must treat audit delivery and execution authority as separate concerns.

## What Deno completes

- A lighter script/tool runtime between an unrestricted shell and a full container or VM.
- Explicit capability requests rather than ambient filesystem, network, environment and subprocess authority.
- Permission-state, broker and prompt concepts useful for Facility approval mapping.
- Checked-path and no-follow distinctions useful for safer Object-root access.
- Audit hooks useful for Activity Receipts and OpenTelemetry.
- TypeScript/JavaScript execution without a separate build step for many tasks.
- Portable local automation, small-service and MCP-server implementation paths.
- A strong runtime candidate for approved plugins whose needs fit its lightweight permission model.

## Important limitations for Ptah

- Deno permissions are runtime checks, not strong kernel or VM isolation.
- Native libraries, FFI, subprocesses or broadly granted permissions can escape the intended lightweight boundary.
- `--allow-all` defeats the least-authority model.
- Interactive permission prompts are unsuitable for unattended Activities unless mediated explicitly.
- Package imports, npm compatibility, JSR and remote dependencies add supply-chain and network risk.
- Permission audits prove attempted access, not semantic correctness, data purpose or absence of side channels.
- Audit payloads may contain paths, hosts, environment names or stack data and therefore require privacy filtering.
- One script may still consume excessive CPU, RAM, disk, file descriptors or time without external resource controls.
- Deno process, module and cache IDs are not Ptah Facility, Plugin or Activity identities.
- Compiled standalone binaries still require source, dependency, lockfile, permission and provenance records.
- Network permission by host does not automatically express URL path, protocol, method or business restrictions.
- Canonicalized paths and no-follow checks do not replace Ptah Object identity or Workspace-root policy.
- Deno does not provide durable Activity recovery, Object storage, package governance or plugin migration/rollback.
- A broker allow decision is runtime authority, not caller approval, policy proof or acceptance.

## Must not be inherited

- `--allow-all` as a normal plugin/tool mode;
- Deno permission flags used as the canonical Ptah permission schema;
- interactive prompts relied upon for background execution;
- remote, JSR or npm imports accepted without pin, hash, lockfile and provenance;
- FFI, subprocess or unrestricted environment access bundled into ordinary script permission;
- Deno runtime, module or cache IDs as canonical Ptah identities;
- permission grant interpreted as caller approval or proof of safe behavior;
- audit delivery interpreted as complete operation proof;
- Deno used as a substitute for container/VM isolation for untrusted native workloads;
- raw path permission used in place of scoped Ptah Object/View access;
- compile-time permissions changed without a new tool Artifact revision.

## Integration decision

**ADOPT DENO AS THE PRIMARY LIGHTWEIGHT PERMISSION-SCOPED JAVASCRIPT/TYPESCRIPT TOOL-RUNTIME CANDIDATE, BELOW OCI/VM ISOLATION.**

Recommended role:

1. small transformation and automation Facilities;
2. MCP servers and adapters;
3. lightweight plugin/service execution;
4. structured-data or Object transforms that do not need native dependencies;
5. portable scripts across Nodes;
6. generated standalone tool Artifacts with pinned permissions and dependencies.

Ptah owns the Facility/Plugin manifest, permission mapping, source/dependency hashes, resource limits, Activity/receipt identity, policy approval and stronger-isolation escalation.

## Licence decision

The MIT licence is compatible with architecture study, wrapping and adoption. Imported packages, npm/JSR dependencies and generated bundles require independent licence and provenance review.

## Native Ptah gap

Ptah must define:

- Facility/Plugin permission vocabulary independent of Deno flags;
- mapping to exact Object/View read/write scopes, Workspace roots, network destinations, environment keys and subprocess identities;
- non-interactive approval and permission-broker contract;
- package, source, lockfile and dependency provenance;
- runtime, version, cache and standalone-binary identity;
- CPU, RAM, time, disk, file-descriptor and network budgets outside the runtime;
- FFI, native-module and subprocess risk classes;
- audit-event to Receipt/OpenTelemetry mapping with sensitive-value redaction;
- compiled-tool Artifact, permission-set, signature and SBOM records;
- container/VM escalation rules;
- activation, health, upgrade, rollback and removal semantics;
- backend replacement tests.

## Exit strategy

Ptah's Tool Runtime contract remains implementable through Deno, Node.js sandboxes, WebAssembly/WASI, Python subprocesses, OCI containers or other runtimes. Deno-specific permissions remain adapter metadata.

## Validation required

1. Run a script with only one approved Object read scope and one output Object write scope.
2. Deny undeclared network, environment, path, FFI and subprocess access.
3. Audit permission checks into Receipts/OpenTelemetry without leaking sensitive values.
4. Refuse unattended interactive prompts and route additional access through a Ptah approval request.
5. Pin package, source and lockfile hashes and reject dependency drift.
6. Enforce external CPU, RAM, time, disk and descriptor limits and terminate a runaway script safely.
7. Escalate an FFI/native workload to OCI/VM isolation instead of weakening Deno permissions.
8. Test symlink and no-follow access against Workspace/Object-root escape attempts.
9. Compile a standalone tool and prove its permission set, source, dependency and binary Artifact revisions match.
10. Deny a broker request even when the script would otherwise prompt for access.
11. Replace Deno for one tool without changing Facility or Activity identity.
12. Remove a Deno plugin and prove dependent Recipes become explicitly unavailable rather than silently switching runtimes.
