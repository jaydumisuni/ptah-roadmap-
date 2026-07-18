# Donor Record — Model Context Protocol Specification and Reference Servers

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PRIMARY EXTERNAL TOOL/RESOURCE/PROMPT INTEROPERABILITY DONOR  
**Inspected:** 2026-07-18

## Identity

### MCP specification and documentation

- Current canonical URL: https://github.com/modelcontextprotocol/modelcontextprotocol
- Historical/redirected path: https://github.com/modelcontextprotocol/specification
- Default branch: `main`
- Pinned commit: `26897cc322f356487da89113451bd16b520b9288`
- Inspected stable schema version: `2025-11-25`
- Licence state: project-wide transition across MIT and Apache-2.0 contributions; non-specification documentation is CC-BY-4.0

### Reference servers

- Canonical URL: https://github.com/modelcontextprotocol/servers
- Default branch: `main`
- Pinned commit: `d31124c982401739917fd817c2a59db344529c16`
- Licence state: mixed Apache-2.0/MIT during the same transition; non-specification documentation CC-BY-4.0

- Activity: Active
- Classification: JSON-RPC capability-negotiated interoperability protocol and reference-implementation donor
- Ptah targets: `PLUGIN-001`, external Facility adapters, Resources, Tools, Prompts, progress, cancellation, task augmentation, local/remote transport, authorization and client/server interoperability

## Files/components inspected

- `README.md`
- `LICENSE`
- `schema/2025-11-25/schema.ts`
- `docs/specification/2025-11-25/basic/transports.mdx`
- `docs/specification/2025-11-25/basic/authorization.mdx`
- `docs/docs/tutorials/security/security_best_practices.mdx`
- reference-server `README.md`
- reference-server `LICENSE`
- `src/filesystem/index.ts`
- `src/filesystem/lib.ts`
- current filesystem reference-server tool-annotation and path-security evidence
- reference server catalogue, SDK list, Registry direction and production-readiness warning

## Verified capabilities and patterns

### Base protocol and lifecycle

- Uses UTF-8 JSON-RPC 2.0 request, notification, result and error envelopes.
- Request IDs are strings or numbers and responses preserve the matching ID.
- Negotiates protocol version, client/server implementation identity and capabilities during initialization.
- A server may select a different supported protocol version; an incompatible client must disconnect.
- Capabilities and `_meta` fields are extensible rather than a closed enumeration.
- Server-provided instructions are explicitly hints that a client may choose to add to model context.
- Supports ping, cancellation, progress and pagination.
- Cancellation notifications apply to in-flight non-task requests; task cancellation is a separate operation.
- Transport disconnection is not equivalent to cancellation, completion or rollback.
- List-change notifications exist for Tools, Resources and Prompts.
- Resource subscriptions can notify clients when content changes.

### Capabilities and reverse-direction requests

- Client capabilities can include roots, sampling, elicitation and tasks.
- Server and client task support must be negotiated for the specific augmented request family.
- Sampling allows a server to request model generation through the client, while the client retains control over model choice, system prompt handling and token limits.
- Elicitation allows a server to request client/human input through form or URL flows.
- These capabilities can move reasoning or human interaction outside Ptah and therefore require explicit caller/product ownership and trusted UI attribution.
- Capability declarations describe support; they do not establish caller permission, trust, health or successful execution.

### Resources, Tools and Prompts

- Resources support URI-based discovery/read contracts, templates, annotations, MIME types, size metadata, subscriptions and change notifications.
- Resource URI schemes are server-defined rather than canonical Ptah Object identities.
- Tools expose discoverable JSON Schema inputs, optional structured outputs and call operations.
- Prompts expose discoverable parameterized templates.
- Human-readable titles, descriptions and icons support UI presentation.
- Tool annotations can claim read-only, destructive, idempotent and open-world behavior.
- Task support can be forbidden, optional or required per Tool family.
- The filesystem reference server declares open-world/read-write/destructive/idempotence hints for local tools.
- These annotations are advisory metadata and do not replace Ptah permission, side-effect or proof records.

### Task augmentation

- Protocol `2025-11-25` defines optional task-augmented requests.
- Tasks expose ID, working/input-required/completed/failed/cancelled states, status message, creation/last-update times, TTL and suggested polling interval.
- Requests exist to get, list, cancel and retrieve task results.
- Task status notifications are optional.
- MCP task state is a useful external-provider projection but lacks Ptah's operation/attempt/nonce/checkpoint/Receipt/proof model.

### Standard transports

- Standard transports are stdio and Streamable HTTP; custom transports are allowed.
- Stdio launches a server as a subprocess and reserves stdout for MCP messages while logs belong on stderr.
- Streamable HTTP uses one POST/GET endpoint and may stream through SSE.
- Streamable HTTP supports event IDs, `Last-Event-ID` resumability and optional session IDs.
- Session IDs must be securely generated and sent on subsequent requests when issued.
- HTTP 404 for an expired session requires reinitialization rather than pretending the old session resumed.
- Multiple streams must not receive duplicate broadcast copies of one message.

### Authorization and transport security

- HTTP authorization is optional, but when implemented follows an OAuth 2.1-oriented protected-resource profile.
- Stdio authorization should use local process/environment configuration rather than the remote OAuth profile.
- HTTP servers must validate `Origin` to prevent DNS-rebinding attacks.
- Local HTTP servers should bind to localhost rather than all interfaces.
- HTTP servers should authenticate every connection.
- Protected-resource metadata and `WWW-Authenticate` scope hints support least-privilege authorization discovery.
- Security guidance covers confused-deputy attacks, per-client consent, redirect validation, CSRF/state handling, token passthrough, SSRF and session hijacking.
- Tokens issued for another resource must not be blindly accepted and forwarded.

### Reference implementations and ecosystem

- Official SDKs are listed for C#, Go, Java, Kotlin, PHP, Python, Ruby, Rust, Swift and TypeScript.
- Reference servers include Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking and Time.
- The official repository explicitly states that these are educational/reference implementations, not production-ready services.
- Published-server discovery is moving to the MCP Registry; archived examples have moved to a separate repository.
- Reference configurations demonstrate package execution through `npx`, `uvx` or `pip`, scoped filesystem roots and environment-provided credentials.
- Package commands and environment credentials remain deployment examples, not safe Ptah defaults.

### Filesystem reference-server lessons

- Allowed directories come from command-line arguments and/or negotiated roots.
- Paths are normalized and real paths are retained to handle symlinks.
- Inaccessible directories are rejected or removed during startup.
- Existing paths resolve through `realpath` and are rejected when a symlink target escapes allowed roots.
- New files validate the real parent directory before creation.
- Writes use exclusive creation or temporary-file plus atomic rename patterns to reduce symlink races.
- Multi-file operations can retain per-item failures rather than collapsing the entire batch.
- Binary/media results are normalized into valid MCP content-block types.

## What MCP completes

- A widely adopted external interoperability protocol for Tool, Resource and Prompt exposure.
- Version and capability negotiation.
- Polyglot SDK and adapter paths.
- Tool/resource discovery and invocation contracts.
- Progress, cancellation, pagination, subscriptions and list-change events.
- Optional long-running task projection.
- Local subprocess and remote HTTP/SSE transport patterns.
- OAuth-oriented authorization direction and concrete transport-security guidance.
- Advisory tool metadata for read-only, destructive, idempotent and open-world behavior.
- A route for external AI clients, IDEs and applications to access approved Ptah Facilities.
- Reference patterns for roots, path validation, symlink handling and structured Tool results.

## Important limitations for Ptah

- MCP is an adapter protocol, not Ptah's internal Object, Activity, Event, Facility, Permission, Plugin or Receipt model.
- JSON-RPC request IDs, task IDs, resource URIs and Tool names are connection/server-local rather than canonical Ptah identities.
- Server-provided instructions, descriptions, Prompts, icons and annotations are untrusted metadata until explicitly approved.
- JSON Schema validates shape, not authorization, semantic meaning, side effects or correctness.
- Tools can perform arbitrary side effects depending on implementation.
- Resources can expose sensitive data and broad URIs.
- Roots are path/URI boundaries, not Ptah Object-level permission grants.
- Reference servers are explicitly not production-ready and require threat-model-specific safeguards.
- Capability negotiation declares support, not authorization, trust, health or compatibility with Ptah policy.
- Progress and task support do not replace Ptah durable Activity orchestration, retry, checkpoint, Receipt or proof.
- Task notifications and TTL do not guarantee durable recovery.
- Sampling and elicitation can invoke external reasoning or human interaction that Ptah must not own implicitly.
- Community servers and registries vary in licence, security, maintenance, identity and provenance.
- Registry presence is discovery metadata, not approval.
- HTTP authorization is optional in the protocol, so Ptah must not assume an endpoint is authenticated.
- Stdio servers inherit the launching process's OS authority unless separately isolated.
- Stream resumability does not imply semantic idempotency or durable Activity recovery.
- Open-ended `_meta` and experimental fields require filtering, namespacing and compatibility rules.
- Tool hints such as `readOnlyHint` or `openWorldHint` are claims by the server and must be checked against implementation and sandbox policy.
- Package launch examples using mutable registry resolution can introduce dependency drift and supply-chain risk.
- SVG/remote icons and URL-based elicitation can create tracking, phishing and content risks.
- MCP schemas evolve; version negotiation, migration and conformance testing are mandatory.
- Mixed licence transition requires file/package-level review before copying implementation code.

## Must not be inherited

- MCP as Ptah's internal Node Protocol, Object model or Activity/Event fabric;
- MCP request/task IDs as canonical Ptah Activity identity;
- Resource URIs as canonical Object or Knowledge Source identity;
- server instructions, Prompt templates, descriptions, icons or annotations treated as trusted policy;
- every discovered Tool, Resource or Prompt exposed automatically;
- reference servers deployed to production unchanged;
- sampling capability interpreted as Ptah/Hunter reasoning ownership;
- elicitation rendered without clear server identity, requested data and approval scope;
- arbitrary Resource URIs mapped directly to host files, networks or credentials;
- roots used instead of Ptah Object/View permissions;
- Registry presence interpreted as trusted Plugin approval;
- Tool-call success promoted to a verified side effect;
- one MCP protocol version hard-coded without negotiation/migration;
- mutable `npx`, `uvx`, `pip` or Registry resolution accepted without pin/hash/provenance;
- advisory destructive/idempotent/open-world hints used instead of Ptah review and runtime evidence;
- stdio processes launched with ambient host authority;
- Streamable HTTP exposed without Origin validation, authentication and session protections;
- token passthrough, wildcard redirects or unbounded authorization-metadata fetching;
- disconnection interpreted as cancellation, completion or rollback.

## Integration decision

**ADOPT MCP AS A PRIMARY EXTERNAL FACILITY ADAPTER PROTOCOL, WHILE KEEPING PTAH-NATIVE INTERNAL CONTRACTS.**

Recommended architecture:

1. Ptah Facilities retain native manifests, permissions, Activities, Receipts and Object identities.
2. An MCP adapter maps approved Facilities to Tools, Resources and Prompts.
3. Each MCP server installation maps to stable Ptah Package, Installed Plugin, Activation and Facility identities.
4. MCP progress/cancellation maps to Ptah Events/Activity controls but does not replace them.
5. Task-augmented requests map to an external provider task under the owning Ptah Activity.
6. MCP roots/resources map to approved Workspace/Object/View scopes rather than arbitrary host paths.
7. Server Prompts/instructions remain untrusted metadata unless explicitly approved by the caller/product.
8. Tool annotations become review inputs, not permission or proof authority.
9. Sampling routes to a caller-approved Model Facility; Hunter and other callers retain reasoning ownership.
10. Elicitation routes through a trusted Ptah approval/human-input UI.
11. Stdio servers run through Deno, restricted subprocess, OCI or stronger isolation according to risk.
12. Streamable HTTP servers use explicit Origin, authentication, OAuth, session and network policy.
13. Registry discovery is followed by licence, source, signature, provenance, permission and health review.
14. Every supported protocol revision receives conformance testing before activation.

## Licence decision

The specification/project and reference-server repositories are in a mixed MIT/Apache-2.0 transition, while non-specification documentation is CC-BY-4.0. Protocol compatibility does not require copying implementation code. Any selective reuse must identify the applicable file/package licence, preserve required notices and review each SDK/server dependency independently.

## Native Ptah gap

Ptah must define:

- MCP Adapter, Connection, Session and negotiated Capability identities;
- protocol-version pin and migration/conformance policy;
- mapping from Tool/Resource/Prompt IDs to Facility methods, Contributions and Objects;
- caller and Workspace permission filters;
- request/response mapping to Activity, operation, attempt and Receipt IDs;
- durable cancellation, progress, reconnect and task-result behavior;
- external-task correlation, polling and lost-task reconciliation;
- Resource URI to Object/View revision mapping;
- source freshness, deletion and exact citation binding;
- sampling/elicitation ownership, budget and trusted-UI policy;
- advisory annotation verification and override records;
- server package, source, licence, signature, SBOM and provenance records;
- Registry discovery, trust review, pinning, upgrade, rollback and deprecation/replacement records;
- stdio process isolation, environment filtering and executable pinning;
- HTTP Origin/auth/session/OAuth/SSRF policy;
- `_meta` namespace/filtering rules;
- adapter replacement and protocol-version migration tests.

## Exit strategy

MCP remains one external adapter. Ptah Facilities can also be exposed through SDK, CLI, HTTP, gRPC, UI or future protocols without changing internal Facility, Activity, Object, Plugin or Knowledge identities.

## Validation required

1. Initialize clients/servers across at least two protocol versions and reject an unsupported selection correctly.
2. Map one stdio and one Streamable HTTP server to stable Ptah Facility identities.
3. Expose one scoped Ptah Object as an MCP Resource without permitting arbitrary host access.
4. Map one MCP Tool call to a durable Ptah Activity and retain operation, attempt and Receipt identity.
5. Call read-only, destructive, idempotent and open-world Tools and prove annotations do not bypass policy.
6. Map a task-augmented request to a Ptah Activity and keep MCP task identity adapter-local.
7. Disconnect and resume an HTTP stream without treating redelivery as a second side effect.
8. Cancel an ordinary request and an external task through their distinct operations.
9. Reject unapproved or disappeared Tools, Resources and Prompts instead of silently using stale metadata.
10. Bind an MCP Resource result to an exact permitted Object/View revision before citation or durable use.
11. Deny a sampling request outside caller-approved model, Tool or budget policy.
12. Render elicitation with clear server identity and reject sensitive fields outside approved scope.
13. Launch a stdio server with no undeclared filesystem, environment, network or subprocess authority.
14. Reject Streamable HTTP requests with invalid Origin, missing authentication or stale session ID.
15. Test OAuth discovery against SSRF, confused-deputy, token-passthrough and redirect attacks.
16. Validate filesystem traversal, symlink, race and root-change cases.
17. Run a reference server only in isolated testing and retain its missing production safeguards.
18. Disable or replace the MCP adapter/server without changing Facility, Object, Plugin or Activity identity.
