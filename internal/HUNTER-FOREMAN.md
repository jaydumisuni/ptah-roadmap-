# Internal Recovery Record — Hunter Foreman

**Phase:** 0A / WP02C  
**Status:** FIRST-PASS COMPLETE  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/hunter-foreman`
- Visibility: Public
- Default branch: `main`
- Pinned commit: `7b06c9c3844805fb203a0a6ad637c70769283314`
- Licence: MIT declared in `package.json`
- Ptah relevance: structured work ownership, lifecycle presentation, versioned app bridge, system health, honest connection states and proof packaging.

## Files inspected

- `README.md`
- `package.json`
- `apps/demo/server.js`
- `packages/foreman-core/index.js`
- `packages/app-bridge/index.js`

## Verified implemented behavior

- Incoming requests become structured task records containing ID, timestamp, customer/channel/message, intent, confidence, classifier/fallback information, workflow, owner, status, escalation and notification previews.
- Rule-based fallback is explicit when the configured AI provider is unavailable or invalid.
- Sensitive/urgent or low-confidence requests move to human-review status rather than silently continuing.
- A versioned App Bridge envelope uses contract `foreman.app.task.v1`, event ID, event type, source, timestamp, full task and timeline.
- App Bridge returns an explicit sent/failed result and preserves remote status/body.
- Runtime exposes configured/not-configured status, provider state, task count and last dispatch.
- Connection states distinguish not connected, dispatch failed and receiver checked.
- Public demo versus private production integration is explicitly documented and reflected in UI labels.
- The repository retains screenshots, API outputs, smoke-test evidence, Docker config validation and SHA-256 sums.
- The dashboard/Activity UI provides request, task-board, analytics, connected-app and health views.

## Important current limitations

- The inspected demo server stores tasks and dispatches in in-memory arrays; restart loses operational state.
- Task IDs and bridge event IDs are time-derived rather than globally collision-resistant operation identities.
- Bridge delivery has no idempotency key, acknowledgement receipt schema, retry classification, signature, authentication or durable outbox in the inspected implementation.
- Lifecycle entries are generated together at view time rather than retained as immutable state-transition events.
- `receiver_checked` may be shown after an HTTP success without independent proof of downstream business completion.
- The runtime is demo-focused and embeds a large UI directly in the server source.
- There is no multi-Node placement, worker lease, cancellation, checkpoint or restart reconciliation.
- Task statuses represent the business demo lifecycle, not a universal Ptah Activity state model.

## Strong internal patterns for Ptah

1. Every request becomes owned, visible and traceable work.
2. Classification/fallback source is retained with the work record.
3. Confidence and escalation are explicit rather than hidden.
4. Versioned bridge envelopes contain source, event identity and timeline.
5. Connection, implementation and planned states are labelled honestly.
6. Optional-provider failure does not erase the request or prevent safe fallback behavior.
7. Operational views include activity, task state, analytics and system health.
8. Public/private implementation boundaries are deliberately represented.
9. Claims are accompanied by proof artifacts and checksums.

## What Ptah should reuse or adapt

- Request-to-Activity intake visibility.
- Versioned external Facility/App bridge envelopes.
- Honest connected/not-connected/degraded labels.
- System-health and Activity Centre presentation patterns.
- Fallback source and failure-reason fields.
- Explicit owner/caller references without placing business ownership logic in Ptah.
- Evidence bundle/checksum practices.
- Optional backend failure continuing only the capabilities that remain available.

## What Ptah must not inherit

- Business customer/task semantics as the universal Activity model.
- ROSE, Hunter, Fireworks or company-specific identities in public Ptah.
- In-memory arrays as durable state.
- Timestamp-only IDs.
- HTTP success interpreted as complete downstream proof.
- A monolithic HTML/server source as Ptah's interface architecture.
- Demo reset and simulated lifecycle as production recovery.
- Private production integration details in the public project.

## Classification

**ADAPT STATUS, BRIDGE, HEALTH AND PROOF PATTERNS; DO NOT REUSE DEMO RUNTIME AS CORE.**

Foreman contributes internal evidence for `CORE-002`, `RELAY-001`, `UI-002`, `OBS-001`, `PROV-001` and caller-facing status honesty.

## Native Ptah completion required

- UUID/content-safe operation and event identities;
- durable Activity Ledger and append-only transition events;
- idempotent bridge delivery, receipts and retry classes;
- authenticated/signed adapter transport where required;
- durable outbox/reconciliation;
- Node/Provider/Facility correlation;
- separation of UI, control plane and worker processes;
- independent Artifact validation rather than dispatch success alone.

## Validation inherited into Ptah

- optional provider failure preserves safe work and records fallback reason;
- no connected/completed claim without evidence;
- bridge event versioning and duplicate rejection;
- restart persistence and immutable state-transition history;
- proof bundle hashes match retained outputs;
- Activity Centre remains honest during partial outages.
