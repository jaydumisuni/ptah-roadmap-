# Donor Record — Model Context Protocol Specification and Reference Servers

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PRIMARY EXTERNAL TOOL/RESOURCE ADAPTER PROTOCOL DONOR  
**Inspected:** 2026-07-18

## Identity

### Specification and documentation

- Current canonical repository: `https://github.com/modelcontextprotocol/modelcontextprotocol`
- Historical/redirected repository path: `https://github.com/modelcontextprotocol/specification`
- Default branch: `main`
- Pinned commit: `26897cc322f356487da89113451bd16b520b9288`
- Stable protocol schema inspected: `2025-11-25`
- Licence state: project-wide transition across Apache-2.0 and MIT contributions; non-specification documentation is CC-BY-4.0
- Activity: Active

### Official reference servers

- Canonical repository: `https://github.com/modelcontextprotocol/servers`
- Default branch: `main`
- Pinned commit: `d31124c982401739917fd817c2a59db344529c16`
- Licence state: mixed Apache-2.0/MIT during transition; non-specification documentation CC-BY-4.0
- Activity: Active
- Repository classification: a small set of educational/reference implementations, not a production server catalogue

## Ptah classification

- External adapter and interoperability protocol donor
- Tool/resource/prompt schema donor
- Remote/local Facility transport donor
- Plugin/service discovery input, not canonical registry truth
- Optional client/server task bridge, not Ptah durable Activity runtime
- Authorization and security-boundary donor for HTTP-exposed Facilities

Ptah targets:

- `PLUGIN-001` external Facility adapters;
- `CORE-004` external tool/resource contributions;
- `SEARCH-001` external source/resource access;
- long-running tool-call projection into Activities;
- protocol/version/capability negotiation;
- public/private adapter boundaries;
- human and model requests mediated through Ptah policy.

## Files/components inspected

### Specification

- `README.md`
- `LICENSE`
- `schema/2025-11-25/schema.ts`
- `docs/specification/2025-11-25/basic/transports.mdx`
- `docs/specification/2025-11-25/basic/authorization.mdx`
- `docs/docs/tutorials/security/security_best_practices.mdx`

### Reference servers

- `README.md`
- `LICENSE`
- `src/filesystem/index.ts`
- `src/filesystem/lib.ts`
- current server-list and filesystem-security commit evidence

## Verified specification capabilities and patterns

### Protocol and lifecycle

- MCP uses UTF-8 JSON-RPC 2.0 messages.
- Initialization negotiates protocol version, client/server implementation metadata and capabilities.
- The client can disconnect when the server selects an unsupported protocol version.
- Capabilities are extensible rather than a closed enumeration.
- Ping, cancellation, progress and pagination are protocol-level operations.
- Cancellation is explicit; transport disconnection is not equivalent to cancelling work.
- List-change notifications exist for tools, resources and prompts.
- Resource subscriptions can notify clients when a resource changes.

### Standard server surfaces

- Servers can expose tools, resources, resource templates and prompts.
- Tool inputs and optional structured outputs use JSON Schema.
- Tool metadata includes names, human-readable titles/descriptions, icons and extension metadata.
- Tool annotations include `readOnlyHint`, `destructiveHint`, `idempotentHint` and `openWorldHint`.
- Tool execution metadata can declare task augmentation as forbidden, optional or required.
- Resources use URIs, optional MIME type, size, annotations and content blocks.
- Resource URIs may use arbitrary schemes interpreted by the server.
- Resource lists and templates are paginated and can change over time.

### Client-provided surfaces

- Clients can expose roots, sampling and elicitation capabilities.
- Roots provide server-visible filesystem or source boundaries and may emit list-change notifications.
- Sampling allows a server to request model generation through the client, subject to negotiated capability and client control.
- The client may ignore model preferences, alter or omit requested system prompts and reduce token limits.
- Elicitation allows a server to request human/client input through form or URL flows.
- These reverse-direction capabilities prove that an MCP server may request reasoning or human input, but does not own either.

### Task augmentation

- Protocol `2025-11-25` defines optional task-augmented requests.
- Capabilities must declare support for task augmentation per request family.
- Tool calls can be forbidden, optional or required to use task execution.
- Tasks expose ID, working/input-required/completed/failed/cancelled states, status message, timestamps, TTL and suggested polling interval.
- Requests exist to get, list, cancel and retrieve task results.
- Task status notifications are optional.
- MCP tasks are a useful bridge for long-running external calls but are not equivalent to Ptah Activities, attempts, checkpoints, receipts or proof.

### Transports

- Standard transports are stdio and Streamable HTTP; custom transports are allowed.
- In stdio mode the client launches the server as a subprocess and transports only MCP messages over stdin/stdout; logs belong on stderr.
- Streamable HTTP uses one POST/GET endpoint and may stream through SSE.
- Streamable HTTP supports reconnect/poll behavior, `Last-Event-ID` resumability and optional session IDs.
- Multiple streams must not receive duplicate broadcast copies of the same message.
- Session IDs must be securely generated and included in subsequent requests when issued.
- HTTP 404 for an expired session requires reinitialization rather than pretending the old session resumed.

### Authorization and security

- MCP HTTP authorization is optional, but when implemented follows an OAuth 2.1-based profile with protected-resource and authorization-server discovery.
- Stdio authorization should use environment/local process configuration rather than the HTTP OAuth profile.
- HTTP servers must validate `Origin` to prevent DNS-rebinding attacks.
- Local HTTP servers should bind to localhost rather than all interfaces.
- HTTP servers should authenticate every connection.
- Protected-resource metadata and `WWW-Authenticate` scope hints support least-privilege authorization discovery.
- Security guidance explicitly addresses confused-deputy attacks, per-client consent, redirect validation, CSRF/state handling, token passthrough, SSRF and session hijacking.
- Tokens not issued for the MCP server must not be accepted and passed through blindly.

## Verified reference-server lessons

### Repository role

- The official servers repository explicitly describes its contents as reference implementations and warns that they are not production-ready.
- The maintained set is intentionally small; broader discovery has moved to the MCP Registry and vendor/community repositories.
- Archived reference servers are separated from currently maintained examples.
- Current reference examples include Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking and Time.
- Official SDKs exist across several languages, reinforcing protocol compatibility rather than one runtime.

### Filesystem reference server

- Allowed directories come from command-line arguments and/or negotiated MCP roots.
- Allowed roots are normalized and real paths are retained to handle symlinks.
- Inaccessible directories are rejected or removed at startup.
- Every requested path is checked against allowed directories before use.
- Existing paths are resolved with `realpath` and rejected when a symlink target escapes allowed roots.
- New files validate the real parent directory before creation.
- Writes use exclusive creation or temporary-file plus atomic rename patterns to reduce symlink races.
- Tool registrations declare input/output schemas and read-only/open-world hints.
- Multi-file operations can retain per-item failures instead of failing the whole batch.
- Binary/media results are normalized into valid MCP content-block types.

## What MCP completes

- A broadly adopted external protocol for exposing tools, resources, prompts and selected client capabilities.
- Capability and protocol-version negotiation.
- Typed JSON Schema inputs and structured outputs.
- Local subprocess and remote HTTP/SSE transports.
- Progress, cancellation, pagination, subscriptions and list-change events.
- Optional long-running task projection.
- OAuth-based remote authorization direction and concrete security guidance.
- A clean adapter point for Deno, Python, Rust, Go, Java and other Facility implementations.
- Reference patterns for roots, path validation, symlink handling and structured tool results.

## Important limitations for Ptah

- MCP is an adapter protocol, not a persistent Object, Activity, Workspace, Facility, Plugin or policy model.
- Tool, resource, prompt, task, session and request IDs are connection/server-local unless Ptah maps them to stable identities.
- Tool annotations are untrusted hints and explicitly do not prove safety, non-destructiveness or idempotency.
- JSON Schema validates shape, not authorization, semantics, side effects or correctness.
- MCP task state lacks Ptah's operation/attempt/nonce/receipt/checkpoint/proof model.
- Optional task notifications and TTL do not guarantee durable recovery.
- Resource URIs are server-defined and are not immutable Ptah Object/View identities.
- Roots are path/URI boundaries, not Ptah Object-level permission grants.
- Server-provided instructions, descriptions, prompts and icons are untrusted content.
- SVG icons and remote icon URLs add content and tracking risk.
- Sampling is a server request to use a model; it must not grant the server control of Hunter or any caller's reasoning policy.
- Elicitation requests can become phishing or consent-confusion surfaces without trusted UI and caller attribution.
- Stdio servers inherit the launching process's OS authority unless separately sandboxed.
- HTTP authorization is optional in the protocol, so Ptah must not assume an MCP endpoint is authenticated.
- Stream resumability does not imply semantic idempotency or durable Activity recovery.
- Official reference servers are educational and explicitly not production-ready.
- The filesystem example remains path/process based and does not provide Object identity, transactional rollback, receipts or strong isolation.
- Mixed licence transition requires file/package-level review before copying code.

## Must not be inherited

- MCP used as Ptah's internal Object or Activity model;
- MCP task IDs used as canonical Activity IDs;
- MCP resources/URIs used as canonical Object or Knowledge Source identity;
- tool annotations trusted as permission, proof or policy;
- server descriptions/prompts/instructions injected without source and trust classification;
- sampling requests allowed to select Ptah/Hunter reasoning policy autonomously;
- elicitation rendered without clear server identity, requested data and approval scope;
- stdio processes launched with ambient host authority;
- Streamable HTTP exposed without origin validation, authentication and session protections;
- arbitrary remote/community servers installed from names or README claims alone;
- official reference servers treated as production dependencies without hardening;
- token passthrough, wildcard redirects or unbounded OAuth metadata fetching;
- path roots used instead of Ptah Object/View permissions;
- disconnection interpreted as cancellation, completion or rollback;
- protocol success interpreted as verified external side effect.

## Integration decision

**ADOPT MCP AS A FIRST-CLASS EXTERNAL FACILITY ADAPTER PROTOCOL, NEVER AS PTAH'S INTERNAL MODEL OR DURABLE RUNTIME.**

Recommended composition:

1. Ptah Plugin/Facility manifests declare an optional MCP adapter and exact protocol versions.
2. Each MCP server installation maps to a stable Ptah Plugin Package, Installation, Activation and Facility identity.
3. MCP tools/resources/prompts map to versioned external contribution records, not direct Core objects.
4. Tool calls become Ptah Activities with attempts, permissions, receipts and result/proof mapping.
5. MCP task augmentation maps to an external provider task under the owning Ptah Activity.
6. MCP resources map to Source/Object adapters with independent revision and permission checks.
7. Sampling routes to a caller-approved Model Facility; Hunter remains an external caller/consumer.
8. Elicitation routes through a trusted Ptah approval/human-input UI.
9. Stdio servers run through Deno, restricted subprocess, OCI or stronger isolation according to risk.
10. Streamable HTTP servers use explicit origin, authentication, OAuth, session and network policy.
11. Registry metadata is discovery input only; install approval requires package, licence, provenance and security verification.
12. Every MCP protocol revision is conformance-tested before activation.

## Licence decision

- The specification/project is in a mixed MIT/Apache-2.0 transition and documentation outside the specification is CC-BY-4.0.
- The reference-server repository has the same transition state.
- Protocol compatibility is unrestricted by copying implementation code.
- Any selective code reuse requires identifying the applicable licence and preserving required notices.
- Each SDK, server package and dependency requires its own licence review.

## Native Ptah gap

Ptah must define:

- MCP Adapter, Connection, Session and negotiated Capability records;
- protocol-version pin and migration/conformance policy;
- stable mapping from external tool/resource/prompt IDs to Ptah contribution identities;
- Plugin Package, Installation, Activation, Health and Removal records;
- source/package hash, signature, SBOM, provenance and licence records;
- object, workspace, credential, network and resource permissions independent of MCP hints;
- Activity/attempt/nonce/receipt mapping for every tool call;
- external-task correlation, polling, cancellation and lost-task reconciliation;
- resource revision/freshness/deletion and exact citation binding;
- trusted sampling/provider selection and budget policy;
- trusted elicitation/consent UI and sensitive-field controls;
- stdio process isolation, environment filtering and executable pinning;
- HTTP origin/auth/session/OAuth/SSRF policy;
- server instructions/prompt/resource content trust classification;
- registry discovery, pin, upgrade, rollback and removal contracts;
- adapter replacement and protocol-version migration tests.

## Exit strategy

Ptah Facilities remain callable through native APIs, CLI/stdio, HTTP, gRPC, SDKs or other protocols. Removing or replacing MCP does not change Facility, Activity, Object, Plugin or Knowledge identities. MCP-specific IDs and sessions remain adapter metadata.

## Validation required

1. Negotiate at least two supported MCP protocol versions and reject an unsupported selection cleanly.
2. Map one stdio and one Streamable HTTP server to stable Ptah Facility identities.
3. Call read-only, destructive, idempotent and open-world tools and prove annotations do not bypass policy.
4. Map a long-running MCP task to one Ptah Activity with multiple attempts and explicit external task correlation.
5. Disconnect and resume an HTTP stream without treating redelivery as a second side effect.
6. Cancel a request and a task through their distinct protocol operations.
7. Reject a resource/tool that disappears after a list-change notification without silently using stale metadata.
8. Bind an MCP resource result to an exact Ptah Source/Object revision before citation or durable use.
9. Deny a sampling request that exceeds caller-approved model, tool or token policy.
10. Render an elicitation request with clear server identity and refuse sensitive fields outside approved scope.
11. Launch a stdio server with no undeclared filesystem, environment, network or subprocess authority.
12. Reject Streamable HTTP requests with invalid Origin, missing authentication or stale session ID.
13. Test OAuth discovery against SSRF, confused-deputy, token-passthrough and redirect attacks.
14. Validate filesystem paths against traversal, symlink, race and root-change cases.
15. Install an official reference server and prove Ptah still labels it unverified for production until hardening passes.
16. Replace MCP with a native adapter for one Facility without changing Ptah identities.
