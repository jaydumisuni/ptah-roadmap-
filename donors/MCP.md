# Donor Record — Model Context Protocol Specification and Reference Servers

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PRIMARY EXTERNAL TOOL/RESOURCE/PROMPT INTEROPERABILITY DONOR  
**Inspected:** 2026-07-18

## Identity

### MCP specification

- Canonical URL: https://github.com/modelcontextprotocol/modelcontextprotocol
- Default branch: `main`
- Pinned commit: `26897cc322f356487da89113451bd16b520b9288`
- Inspected stable schema version: `2025-11-25`
- Licence: MIT

### Reference servers

- Canonical URL: https://github.com/modelcontextprotocol/servers
- Default branch: `main`
- Pinned commit: `d31124c982401739917fd817c2a59db344529c16`
- Licence: Apache-2.0 for new contributions with existing MIT-covered code as recorded by the repository

- Classification: JSON-RPC capability-negotiated interoperability protocol and reference-implementation donor
- Ptah targets: `PLUGIN-001`, external Facility adapters, Resources, Tools, Prompts, progress, cancellation, task augmentation and client/server interoperability

## Files/components inspected

- specification schema `schema/2025-11-25/schema.ts`
- initialization, capabilities, JSON-RPC, cancellation, progress, pagination and task-augmentation types
- reference-server `README.md`
- current filesystem reference-server tool-annotation commit
- reference server catalogue, SDK list, Registry direction and production-readiness warning

## Verified capabilities and patterns

### Base protocol

- Uses JSON-RPC 2.0 request, notification, result and error envelopes.
- Request IDs are strings or numbers and responses preserve the matching ID.
- Negotiates protocol version, client/server implementation identity and capabilities during initialization.
- A server may select a different supported protocol version; an incompatible client must disconnect.
- Server-provided instructions are explicitly described as hints that a client may add to model context.
- Supports cancellation notifications for in-flight non-task requests.
- Task cancellation is separate from ordinary request cancellation.
- Supports opaque progress tokens and pagination cursors.
- Supports open-ended `_meta` and experimental capability fields.

### Capabilities and task augmentation

- Client capabilities can include roots, sampling, elicitation and tasks.
- Server and client task support must be negotiated for the specific augmented request family.
- A task-augmented request may return a task record immediately while its eventual result is retrieved separately.
- Capability declarations describe protocol support; they do not establish caller permission, trust, health or successful execution.
- Sampling and elicitation can move reasoning or human interaction outside Ptah and therefore require explicit caller/product ownership.

### Resources, Tools and Prompts

- Resources support URI-based discovery/read contracts, templates and change notifications.
- Tools expose discoverable schemas and call operations.
- Prompts expose discoverable parameterized templates.
- Human-readable titles, descriptions and icons support UI presentation.
- Tool annotations can describe read-only, destructive, idempotent and open-world hints.
- The current filesystem reference server declares `openWorldHint: false` for local-filesystem tools and documents read/write/destructive/idempotence hints.
- These annotations are advisory metadata and do not replace Ptah permission, side-effect or proof records.

### Reference implementations and ecosystem

- Official SDKs are listed for C#, Go, Java, Kotlin, PHP, Python, Ruby, Rust, Swift and TypeScript.
- Reference servers include Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking and Time.
- The official repository explicitly states that these are educational/reference implementations, not production-ready services.
- Published-server discovery is moving to the MCP Registry; archived examples have moved to a separate repository.
- Reference configurations demonstrate package execution through `npx`, `uvx` or `pip`, scoped filesystem roots and environment-provided credentials.
- Package commands and environment credentials remain deployment examples, not safe Ptah defaults.

## What MCP completes

- A widely adopted external interoperability protocol for Tool, Resource and Prompt exposure.
- Version and capability negotiation.
- Polyglot SDK and adapter paths.
- Tool/resource discovery and invocation contracts.
- Progress, cancellation, pagination and optional task-augmentation patterns.
- Advisory tool metadata for read-only, destructive, idempotent and open-world behavior.
- A route for external AI clients, IDEs and applications to access approved Ptah Facilities.
- Reference examples for scoped filesystem roots and other servers.

## Important limitations for Ptah

- MCP is an adapter protocol, not Ptah's internal Object, Activity, Event, Facility, Permission or Receipt model.
- JSON-RPC request IDs, task IDs, resource URIs and tool names are connection/server-local rather than canonical Ptah identities.
- Server-provided instructions, descriptions, prompts and annotations are untrusted metadata until explicitly approved.
- Tools can perform arbitrary side effects depending on implementation.
- Resources can expose sensitive data and broad URIs.
- Reference servers are explicitly not production-ready and require threat-model-specific safeguards.
- Capability negotiation declares support, not authorization, trust, health or compatibility with Ptah policy.
- Progress and task support do not replace Ptah durable Activity orchestration, retry, receipts or proof.
- Sampling and elicitation can invoke external reasoning or user interaction that Ptah must not own implicitly.
- Community servers and registries vary in licence, security, maintenance, identity and provenance.
- Registry presence is discovery metadata, not approval.
- Transport security, authentication and authorization remain deployment/adapter concerns.
- Open-ended `_meta` and experimental fields require filtering, namespacing and compatibility rules.
- Tool hints such as `readOnlyHint` or `openWorldHint` are claims by the server and must be checked against actual implementation and sandbox policy.
- Package launch examples using mutable registry resolution can introduce dependency drift and supply-chain risk.
- MCP schemas evolve; version negotiation, migration and conformance testing are mandatory.

## Must not be inherited

- MCP as Ptah's internal Node Protocol or Activity/Event fabric;
- MCP request/task IDs as canonical Ptah Activity identity;
- server instructions, prompt templates, descriptions or annotations treated as trusted policy;
- every discovered Tool, Resource or Prompt exposed automatically;
- reference servers deployed to production unchanged;
- sampling/LLM capability interpreted as Ptah reasoning ownership;
- arbitrary Resource URIs mapped directly to host files, networks or credentials;
- registry presence interpreted as trusted plugin approval;
- Tool-call success promoted to a verified side effect;
- one MCP protocol version hard-coded without negotiation/migration;
- mutable `npx`, `uvx`, `pip` or registry resolution accepted without pin/hash/provenance;
- advisory destructive/idempotent/open-world hints used instead of Ptah review and runtime evidence.

## Integration decision

**ADOPT MCP AS A PRIMARY EXTERNAL FACILITY ADAPTER PROTOCOL, WHILE KEEPING PTAH-NATIVE INTERNAL CONTRACTS.**

Recommended architecture:

1. Ptah Facilities retain native manifests, permissions, Activities, Receipts and Object identities.
2. An MCP adapter maps approved Facilities to Tools, Resources and Prompts.
3. External MCP servers are installed as Plugins behind scoped identities, pinned packages and sandboxes.
4. MCP progress/cancellation maps to Ptah Events/Activity controls but does not replace them.
5. Task-augmented requests map to Ptah Activities through an adapter.
6. MCP roots/resources map to approved Workspace/Object scopes rather than arbitrary host paths.
7. Server Prompts/instructions remain untrusted metadata unless explicitly approved by the caller/product.
8. Tool annotations become review inputs, not permission or proof authority.
9. Sampling and elicitation routes name the external caller/reasoning/human owner explicitly.
10. Registry discovery is followed by licence, source, signature, provenance, permission and health review.

## Licence decision

The specification's MIT licence and reference-server mixed Apache-2.0/MIT arrangement are compatible with architecture study and adapter implementation, subject to retaining notices and reviewing each server/package and transitive dependency independently.

## Native Ptah gap

Ptah must define:

- MCP connection, server, package, plugin and trust identities;
- protocol-version and capability snapshots;
- mapping from Tool/Resource/Prompt to Facility methods and Objects;
- caller and Workspace permission filters;
- request/response mapping to Activity, operation, attempt and Receipt IDs;
- durable cancellation, progress, reconnect and task-result behavior;
- Resource URI to Object/View reference mapping;
- task augmentation to Activity mapping;
- sampling/elicitation ownership and policy boundaries;
- advisory annotation verification and override records;
- server package, source, licence, signature, SBOM and provenance records;
- Registry discovery, trust review, pinning and deprecation/replacement records;
- process/container/runtime isolation, credentials and network scopes;
- `_meta` namespace/filtering rules;
- compatibility and replacement tests.

## Exit strategy

MCP remains one external adapter. Ptah Facilities can also be exposed through SDK, CLI, HTTP, gRPC, UI or future protocols without changing internal identities.

## Validation required

1. Initialize clients/servers across at least two protocol versions and negotiate capabilities correctly.
2. Expose one scoped Ptah Object as an MCP Resource without permitting arbitrary host access.
3. Map one MCP Tool call to a durable Ptah Activity and retain operation, attempt and Receipt identity.
4. Cancel and report progress without losing native Activity state.
5. Map a task-augmented request to a Ptah Activity and keep MCP task identity adapter-local.
6. Reject unapproved Tools, Resources and Prompts from an installed server.
7. Treat server instructions, Prompts and annotations as metadata rather than trusted policy.
8. Verify `readOnlyHint`, `destructiveHint`, `idempotentHint` and `openWorldHint` against implementation and sandbox evidence.
9. Run a reference server only in an isolated test environment and document missing production safeguards.
10. Install a Registry server only from a pinned package/source with licence, hash and provenance evidence.
11. Disable or replace the MCP adapter/server without changing Facility, Object or Activity identity.
12. Filter unknown `_meta` fields and preserve compatible namespaced extensions without privilege escalation.
