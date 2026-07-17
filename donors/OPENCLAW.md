# Donor Record — OpenClaw

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — COMPOSITE CLOSURE PENDING  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/openclaw/openclaw
- Default branch: `main`
- Pinned commit: `73d04395defe25601ef69647e93343f38c2c9a20`
- Version at pin: `2026.7.2`
- Licence: MIT
- Activity: Active at the inspected pin
- Classification: Tier A core architecture donor
- Ptah targets: Node Protocol, gateway/relay transport, capability publication, presence and reconnectable terminals

## Files inspected

- `README.md`
- `LICENSE`
- `package.json`
- `docs/gateway/protocol.md`
- `packages/gateway-protocol/src/schema/frames.ts`
- `src/gateway/server/ws-connection/connect-session.ts`
- `src/gateway/server/ws-connection.test.ts`
- `.github/workflows/ci.yml`

## Verified capabilities

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

## Patterns to adapt

1. Version and feature negotiation.
2. Stable request/response/event envelope.
3. Idempotent command invocation.
4. Node identity separate from connection identity.
5. Runtime capability refresh.
6. Presence and reconnect state.
7. Schema-driven protocol tests.
8. Separate operator, node and worker surfaces.

## Must not be inherited

- Assistant identity, personality, reasoning or memory.
- Messaging-channel architecture.
- OpenClaw's exact role and policy model.
- Its personal-gateway product assumptions.
- Product-specific capability and RPC names.
- JSON WebSocket frames for large binary and media transfer.
- A TypeScript monolith as Ptah's mandatory implementation form.

## Native Ptah gap

Ptah still needs its own neutral:

- node and resource schema;
- workspace/activity/object separation;
- command cancellation and status contract;
- event replay cursor and connection epoch;
- binary, object, PTY and screen streaming paths;
- durable activity integration;
- multi-language node SDK contract.

## Missing capabilities requiring completion donors

OpenClaw does not close the complete Ptah runtime or Node/Workspace system. The composite closure still requires:

- Daytona, Coder, E2B and Dev Containers for workspace-provider and persistent-environment comparison;
- containerd and OCI for the owned execution substrate;
- Temporal for durable activity history, retries, timers and crash recovery;
- NATS and JetStream for internal live events, replay and intermittent-node communication;
- OpenTelemetry for cross-component observability and resource correlation;
- internal THETECHGUY relay, terminal, worker and node evidence;
- native Ptah contracts joining Node, Workspace, Activity, Object and Session.

OpenClaw is therefore a primary capability donor inside a donor composition, not the complete selected architecture.

## Integration decision

**ADAPT — protocol study and selective MIT-compatible adaptation.**

OpenClaw is the first primary architecture donor for `CORE-005` and part of `RELAY-001`. It is not a direct Ptah Core dependency. No donor code has been copied.

## Exit strategy

Ptah owns its schemas and wire contract. OpenClaw can later connect through an adapter without becoming required infrastructure.

## Validation required

Prove challenge/connect negotiation, capability registration and refresh, heartbeat, idempotent invocation, cancellation, reconnect with event replay, and terminal detach/attach. Large bytes must travel outside the JSON control envelope.

The assembled runtime must also be validated against `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md` before the requirement is closed for design.
