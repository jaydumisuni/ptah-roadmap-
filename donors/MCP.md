# Donor Record — Model Context Protocol Specification and Reference Servers

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — EXTERNAL TOOL/RESOURCE/PROMPT INTEROPERABILITY DONOR  
**Inspected:** 2026-07-18

## Identity

### MCP specification

- Canonical URL: https://github.com/modelcontextprotocol/modelcontextprotocol
- Default branch: `main`
- Pinned commit: `26897cc322f356487da89113451bd16b520b9288`
- Inspected schema version: `2025-11-25`
- Licence: MIT

### Reference servers

- Canonical URL: https://github.com/modelcontextprotocol/servers
- Default branch: `main`
- Pinned commit: `d31124c982401739917fd817c2a59db344529c16`
- Licence: Apache-2.0 for new contributions with existing MIT-covered code as recorded by the repository

- Classification: JSON-RPC capability-negotiated interoperability protocol and reference-implementation donor
- Ptah targets: `PLUGIN-001`, external Facility adapters, resources, tools, prompts, progress, cancellation, task augmentation and client/server interoperability

## Files/components inspected

- specification `README.md`
- `schema/2025-11-25/schema.ts`
- initialization, capabilities, JSON-RPC, cancellation, progress, pagination, resources, tools, prompts and task-augmentation types
- reference-server `README.md`
- reference server catalogue and production-readiness warning

## Verified capabilities and patterns

- Uses JSON-RPC 2.0 request, notification, result and error envelopes.
- Negotiates protocol version, client/server implementation identity and capabilities during initialization.
- Supports cancellation and progress notifications.
- Supports opaque pagination cursors.
- Supports Resources with URIs, metadata, list/read, templates, subscribe/unsubscribe and update notifications.
- Supports Tools with discoverable schemas and call operations.
- Supports Prompts as discoverable parameterized templates.
- Supports logging, completions and experimental capability extensions.
- Supports task-augmented requests when both sides negotiate task capabilities.
- Distinguishes client capabilities such as roots, sampling, elicitation and tasks from server capabilities.
- Includes human-readable names/titles/descriptions/icons for UI presentation.
- Official SDKs exist in several languages.
- Reference servers demonstrate filesystem, Git, fetch, memory, time and comprehensive test/everything patterns.
- The official server repository explicitly warns that examples are educational/reference implementations rather than production-ready services.
- Published server discovery is moving toward an MCP Registry rather than one monolithic examples repository.

## What MCP completes

- A widely adopted external interoperability protocol for tool/resource/prompt exposure.
- Version and capability negotiation.
- Polyglot SDK and adapter paths.
- Tool/resource discovery and invocation contracts.
- Progress, cancellation and pagination patterns.
- A route for external AI clients, IDEs and applications to access approved Ptah Facilities.
- Reference examples for secure filesystem roots and other scoped servers.

## Important limitations for Ptah

- MCP is an adapter protocol, not Ptah's internal Object, Activity, Event, Facility, Permission or Receipt model.
- JSON-RPC request IDs, resource URIs and tool names are connection/server-local rather than canonical Ptah identities.
- Server-provided instructions/descriptions are hints to callers and must not become trusted policy or system authority.
- Tools can perform arbitrary side effects depending on implementation.
- Resources can expose sensitive data and broad URIs.
- Reference servers are explicitly not production-ready and require threat-model-specific safeguards.
- Capability negotiation declares support, not authorization, trust or health.
- Progress and task support do not replace Ptah durable Activity orchestration.
- Sampling and elicitation features can involve external reasoning/user interaction that Ptah must not own implicitly.
- Community servers and registries vary in licence, security, maintenance and provenance.
- Transport security, authentication and authorization are deployment/adaptor concerns beyond the base object schemas.
- MCP schemas evolve; version negotiation and compatibility testing are mandatory.

## Must not be inherited

- MCP as Ptah's internal Node Protocol or Activity/Event fabric;
- MCP request/task IDs as canonical Ptah Activity identity;
- server instructions, prompt templates or descriptions treated as trusted policy;
- every discovered tool/resource exposed automatically;
- reference servers deployed to production unchanged;
- sampling/LLM capability interpreted as Ptah reasoning ownership;
- arbitrary resource URIs mapped directly to host files, networks or credentials;
- registry presence interpreted as trusted plugin approval;
- tool-call success promoted to verified side effect;
- one MCP protocol version hard-coded without negotiation/migration.

## Integration decision

**ADOPT MCP AS A PRIMARY EXTERNAL FACILITY ADAPTER PROTOCOL, WHILE KEEPING PTAH-NATIVE INTERNAL CONTRACTS.**

Recommended architecture:

1. Ptah Facilities retain native manifests, permissions, Activities, receipts and Object identities.
2. An MCP adapter maps approved Facilities to tools/resources/prompts.
3. External MCP servers may be installed as plugins behind scoped identities and sandboxes.
4. MCP progress/cancellation maps to Ptah Events/Activity controls but does not replace them.
5. task-augmented requests map to Ptah Activities through an adapter.
6. MCP roots/resources map to approved Workspace/Object scopes rather than arbitrary host paths.
7. server prompts/instructions remain untrusted metadata unless explicitly approved by the caller/product.

## Native Ptah gap

Ptah must define:

- MCP connection/server/plugin identity and trust record;
- protocol-version and capability snapshot;
- mapping from tool/resource/prompt to Facility methods and Objects;
- caller/Workspace permission filters;
- request/response mapping to Activity/operation/receipt IDs;
- durable cancellation/progress/reconnect behavior;
- resource URI to Object/View reference mapping;
- task augmentation to Activity mapping;
- sampling/elicitation ownership and policy boundaries;
- server package/source/licence/signature/provenance records;
- registry discovery, trust review and pinning;
- process/container/runtime isolation and credentials;
- compatibility and replacement tests.

## Exit strategy

MCP remains one external adapter. Ptah Facilities can also be exposed through SDK, CLI, HTTP, gRPC, UI or future protocols without changing internal identities.

## Validation required

1. Initialize clients/servers across at least two protocol versions and negotiate capabilities correctly.
2. Expose one scoped Ptah Object as an MCP Resource without permitting arbitrary host access.
3. Map one MCP Tool call to a durable Ptah Activity and retain operation/receipt identity.
4. Cancel and report progress without losing the native Activity state.
5. Reject unapproved tools/resources/prompts from an installed server.
6. Treat server instructions/prompts as metadata rather than trusted policy.
7. Run a reference server only in an isolated test environment and document missing production safeguards.
8. Upgrade or replace the MCP adapter/server without changing Facility/Object/Activity identity.
