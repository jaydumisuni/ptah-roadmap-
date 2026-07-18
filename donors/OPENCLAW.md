# Donor Record — OpenClaw

**Phase:** 0A / WP01, WP02 and WP10  
**Status:** FIRST-PASS COMPLETE — CORE NODE/GATEWAY AND PLUGIN-RUNTIME DONOR  
**Inspected:** 2026-07-17; WP10 addendum 2026-07-18

## Identity

- Canonical URL: https://github.com/openclaw/openclaw
- Default branch: `main`
- Core-runtime inspection pin: `73d04395defe25601ef69647e93343f38c2c9a20`
- WP10 plugin-lifecycle inspection pin: `05fb8e6e6190ae65b6f1c5fdc0c7dadd960fe3d4`
- Version at both inspected pins: `2026.7.2`
- Licence: MIT
- Activity: Active
- Classification: Tier A core architecture donor plus plugin-runtime/install-state donor
- Ptah targets: Node Protocol, gateway/relay transport, capability publication, presence, reconnectable terminals and `PLUGIN-001` runtime/activation/lifecycle patterns

## Files inspected

### Core/runtime pass

- `README.md`
- `LICENSE`
- `package.json`
- `docs/gateway/protocol.md`
- `packages/gateway-protocol/src/schema/frames.ts`
- `src/gateway/server/ws-connection/connect-session.ts`
- `src/gateway/server/ws-connection.test.ts`
- `.github/workflows/ci.yml`

### WP10 plugin addendum

- `docs/plugins/manage-plugins.md`
- `docs/plugins/manifest.md`
- plugin list/search/install/inspect/update/uninstall behavior
- ClawHub, npm, git, npm-pack, marketplace and local-path source handling
- plugin allow/deny, dependency status, cold inventory versus runtime inspection and restart behavior

## Verified core capabilities

- Version-negotiated WebSocket handshake.
- Client and device identity, role, platform, version and instance metadata.
- Capability, command and permission claims.
- Request, response and event frames with IDs, sequence and state-version fields.
- Structured retryable errors and retry-after hints.
- Idempotency requirements for side-effecting methods.
- Node capability and tool inventory updates after connection.
- Presence, heartbeat, last-seen and background-alive records.
- Terminal detach, list, attach and buffered-output replay.
- Protocol tests and broad platform CI.

## Verified WP10 plugin-runtime capabilities

### Discovery and inventory

- Control UI separates Installed and Discover views.
- Discovery combines bundled/official entries, curated MCP connectors and ClawHub search.
- Read-only catalogue/search access and administrative install/enable/disable/remove access use different operator permissions.
- Plugin list output exposes enabled state, format, source and dependency status.
- Cold list/inspect examines config, manifests and persisted registry state but explicitly does not prove the running Gateway loaded the plugin.
- Runtime inspection loads the module and verifies registered surfaces such as Tools, hooks, services, Gateway methods, HTTP routes and plugin-owned CLI commands.

### Installation sources and source trust

- Installs can come from ClawHub, npm, npm-pack artifacts, git, local directories/archives and compatible marketplaces.
- Explicit source prefixes provide deterministic source selection.
- Bundled and official packages use separate trust treatment from arbitrary external sources.
- New arbitrary npm, git, local path/archive, npm-pack or marketplace sources require explicit force/confirmation in non-interactive use.
- A linked development checkout is not copied or overwritten by force.
- ClawHub installs retain registry trust, integrity and install-policy checks, but those checks remain OpenClaw policy rather than Ptah proof.

### Manifest and cold metadata

- Every native plugin must ship `openclaw.plugin.json` at the plugin root.
- Missing or invalid native manifests block config validation.
- The manifest is read before executing plugin code.
- Manifest metadata can include canonical plugin ID, strict config schema, required plugins, default/platform enablement, legacy IDs, kinds/slots, channels, providers, model/catalog/auth/setup metadata, activation hints, contracts, Tools, skills, UI hints and QA runner metadata.
- Manifest metadata is deliberately separated from runtime registration behavior and package entrypoints.
- Compatible Codex, Claude and Cursor bundles retain their own manifest/layout semantics rather than being silently validated as native plugins.
- Catalogue metadata is presentation-only and does not install, enable or grant trust.

### Enablement and activation

- Installed files and enabled configuration are separate states.
- Enable/disable can update config without modifying installed files.
- An explicit deny entry remains authoritative over enablement.
- Enabling an external plugin can record explicit administrative trust in a restrictive allow list.
- Some source changes require Gateway restart; runtime-compatible enablement changes may hot apply.
- Bundled plugins can be disabled but not removed.
- Runtime registration proof is separate from manifest/config discovery.

### Update and removal

- Tracked install specs retain exact versions or mutable tags across updates.
- Targeted updates and bulk updates have different behavior for official catalogue packages.
- Dry-run is supported for updates and uninstall.
- Uninstall removes config, persisted index records, allow/deny entries and linked load paths; managed files are removed unless explicitly retained.
- Managed Gateway restart follows source-changing install/update/uninstall operations.
- Nix mode disables mutable plugin lifecycle commands and delegates state to declarative source configuration.

## Patterns to adapt

### Core/runtime

1. Version and feature negotiation.
2. Stable request/response/event envelope.
3. Idempotent command invocation.
4. Node identity separate from connection identity.
5. Runtime capability refresh.
6. Presence and reconnect state.
7. Schema-driven protocol tests.
8. Separate operator, Node and worker surfaces.

### Plugin/runtime

9. Cold discovery distinct from runtime activation proof.
10. Manifest/config validation before code execution.
11. Installed, enabled, active, denied and bundled states remain distinct.
12. Explicit source selection and source-specific trust review.
13. Dependency resolution status surfaced separately from plugin identity.
14. Runtime inspection verifies actually registered capabilities.
15. Allow/deny and administrative trust records remain explicit.
16. Dry-run, tracked install specs and restart-required reporting.
17. Declarative/Nix-managed installations cannot be mutated through ordinary runtime commands.
18. Removal cleans configuration/index/load-path state separately from optional file retention.

## Must not be inherited

- Assistant identity, personality, reasoning or memory.
- Messaging-channel architecture.
- OpenClaw's exact role, operator and policy model.
- Its personal-gateway product assumptions.
- Product-specific capability and RPC names.
- JSON WebSocket frames for large binary and media transfer.
- A TypeScript monolith as Ptah's mandatory implementation form.
- OpenClaw plugin or registry IDs as canonical Ptah identities.
- OpenClaw's bundled/official/ClawHub trust classes as universal Ptah approval.
- `--force` as sufficient authorization for arbitrary code installation.
- Manifest claims treated as runtime proof.
- Runtime registration treated as semantic correctness or side-effect proof.
- npm tags or tracked mutable specs used as immutable Package Release identity.
- plugin code loaded inside Ptah Core merely to inspect metadata.
- Gateway restart used as a substitute for staged activation and rollback.
- removal of files without a Ptah data, credential and orphan-state cleanup plan.

## Native Ptah gap

Ptah still needs its own neutral:

- Node and resource schema;
- Workspace, Activity and Object separation;
- command cancellation and status contract;
- event replay cursor and connection epoch;
- binary, Object, PTY and screen streaming paths;
- durable Activity integration;
- multi-language Node SDK contract;
- Package, Package Release, Installed Plugin and Activation identities;
- manifest, permission, source, digest, signature, SBOM and provenance records;
- cold-discovery versus live-runtime capability snapshots;
- staged install, health, activation, migration, rollback and quarantine;
- explicit source and registry trust review;
- plugin Object/Workspace/network/credential scopes;
- restart/rolling-restart and dependent-session impact records;
- removal, retained data, credential revocation and orphan cleanup;
- declarative versus mutable installation ownership.

## Missing capabilities requiring completion donors

OpenClaw does not close the complete Ptah runtime, Node/Workspace or Plugin system. Composite closure requires:

- Daytona, Coder, E2B and Dev Containers for Workspace-provider and persistent-environment comparison;
- containerd and OCI for the owned execution substrate;
- Temporal for durable Activity history, retries, timers and crash recovery;
- NATS and JetStream for internal live Events, replay and intermittent-Node communication;
- OpenTelemetry for cross-component observability and resource correlation;
- ClawHub for registry/discovery/version/pinning/security-report lifecycle;
- MCP for external Tool/Resource/Prompt interoperability;
- Deno and OCI/VM runtimes for scoped execution classes;
- ORAS, Sigstore, SBOM and attestation machinery for immutable release/provenance proof;
- internal THETECHGUY relay, terminal, worker and Node evidence;
- native Ptah contracts joining Node, Workspace, Activity, Object, Session and Plugin.

## Integration decision

**ADAPT — PROTOCOL, DISCOVERY, COLD-MANIFEST, INSTALL-STATE AND RUNTIME-INSPECTION PATTERNS; DO NOT USE OPENCLAW AS PTAH CORE.**

OpenClaw remains the first primary architecture donor for `CORE-005`, part of `RELAY-001`, and a completion donor for `PLUGIN-001`. It is not a direct Ptah Core dependency. No donor code has been copied.

## Exit strategy

Ptah owns its schemas, wire contract and Plugin lifecycle. OpenClaw can connect through a Node/Facility adapter and can consume Ptah Package/Plugin contracts without becoming required infrastructure.

## Validation required

### Core/runtime

1. Prove challenge/connect negotiation, capability registration and refresh.
2. Prove heartbeat, idempotent invocation, cancellation and reconnect with Event replay.
3. Prove terminal detach/attach and buffered output.
4. Keep large bytes outside the JSON control envelope.

### Plugin/runtime

5. Inspect a plugin without loading code and retain the manifest/config/dependency snapshot.
6. Install the same package from two explicit sources and keep source/digest identity distinct.
7. Refuse an arbitrary external source without caller approval and policy authorization.
8. Prove cold inventory does not claim runtime activation.
9. Activate in a staged runtime and verify registered surfaces separately from semantic proof.
10. Apply allow/deny policy and prove deny remains authoritative.
11. Update a pinned/exact release without silently following a mutable tag.
12. Dry-run and execute uninstall while retaining required data/evidence and cleaning credentials/orphans.
13. Treat declarative/Nix-owned install state as immutable to the runtime manager.
14. Roll back after a failed plugin activation or restart.

The assembled runtime and Plugin subsystem must also be validated against `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md` before closure for Phase 0B design.
