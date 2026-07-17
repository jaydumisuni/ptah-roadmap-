# Internal Recovery Record — TechGuy Relay

**Phase:** 0A / WP02C  
**Status:** FIRST-PASS COMPLETE  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/techguy-relay`
- Visibility: Public
- Default branch: `main`
- Pinned commit: `6015a91383582945b27ab71a8a338379c08c8adf`
- Licence: No root licence file was recovered during this pass; do not reuse code until ownership/licence is documented.
- Ptah relevance: short connection-code registration, heartbeat, expiry, resolution and health experiments.

## Files inspected

- latest commit and changed paths
- `relay_server/server.py`

No root README or package manifest was found at the inspected pin.

## Verified implemented behavior

- Flask server with an in-memory connection registry protected by a thread lock.
- Cryptographically random short connection codes prefixed with `TG-`.
- Registration records host, port, timestamp and label.
- Private-address hints are rejected in favor of the observed remote address.
- Resolve endpoint maps a valid code to host and port.
- Heartbeat refreshes the registration timestamp.
- Unregister removes a code.
- Background cleanup removes registrations older than a 60-second TTL.
- Health and stats endpoints expose active-code counts and session labels.
- Payment, user activation and Telegram bot functions are present in the same service.

## Strong internal lessons for Ptah

1. Human-friendly pairing codes are useful as a bootstrap surface.
2. Registration, resolution, heartbeat and expiry are separate operations.
3. Stale registrations must be removed automatically.
4. Health and active-session visibility should exist from the beginning.
5. Stable Node identity must be different from temporary pairing or connection identity.

## Important limitations

- Registry state is entirely in memory and disappears on restart.
- Pairing codes are the only proof presented by registration/resolve endpoints.
- No Node identity key, signed challenge, device attestation, authentication or authorization is present.
- Resolve exposes direct host/port information.
- No capability, version, architecture, connection epoch or last-known durable Node record.
- No command/event transport, event replay, durable outbox or stream routing.
- No NAT traversal, tunnel establishment, TLS termination or certificate lifecycle.
- Heartbeat is only a timestamp update and has no sequence or stale-connection protection.
- Relay, payment, users and Telegram bot concerns are mixed into one service.
- Broad exception swallowing can hide failures.
- User state is stored in a local JSON file without transactional or concurrent-write protection.

## What Ptah should reuse or adapt

- Pairing-code UX as an optional bootstrap flow.
- Separate register/resolve/heartbeat/unregister concepts.
- TTL-based stale-presence cleanup.
- Health and session-count visibility.
- The lesson that connection identity and durable Node identity must remain separate.

## What Ptah must not inherit

- In-memory registry as source of truth.
- Pairing code as durable authentication.
- Public host/port resolution without a secure tunnel/identity layer.
- Payment, user, bot and Node relay concerns in one service.
- Timestamp-only heartbeat with no connection epoch.
- Bare HTTP Node registration.
- Relay success interpreted as Node capability or activity proof.
- Silent exception handling around critical relay behavior.

## Classification

**STUDY AND REBUILD CLEANLY.**

TechGuy Relay is useful internal evidence for `CORE-005`, `RELAY-001`, `DIST-001` and `OFFLINE-001`, but none of its current runtime should become Ptah's relay foundation unchanged.

## Native Ptah completion required

- stable cryptographic Node identity;
- challenge-response pairing and revocable credentials;
- version/capability negotiation;
- connection epoch and replay cursor;
- durable Node catalogue and last-seen state;
- NATS/Event Fabric and dedicated stream integration;
- local outbox and reconnect reconciliation;
- secure tunnel/network transport;
- separation of relay from billing and messaging;
- structured failure and telemetry.

## Validation inherited into Ptah

- stale temporary pairing records expire;
- restart does not lose durable Node identity;
- old heartbeats from a previous connection epoch are rejected;
- duplicate pairing/register attempts cannot create phantom Nodes;
- revoked credentials cannot reconnect;
- relay/telemetry failure does not silently claim Node availability;
- no private deployment address is exposed through a public bootstrap surface.
