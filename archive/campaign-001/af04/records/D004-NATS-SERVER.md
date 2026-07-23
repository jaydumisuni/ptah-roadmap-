# D004 — NATS Server

Status: candidate record — paired evidence complete

Primary Archivist: `AF04-P07`

Independent Verifier: `AF04-V07`

Inspected: 2026-07-23

## Canonical source identity

- source: `nats-io/nats-server`;
- default branch: `main`;
- exact inspected commit: `4ec9e8d85af2c4121b9f75ffda68341c3847adf7`;
- root licence: Apache-2.0;
- repository role: secure high-performance messaging server for cloud, edge and devices;
- archived: false.

## Primary evidence packet

NATS demonstrates lightweight publish/subscribe, request/reply, service and edge communication patterns. JetStream and server clustering can inform live event transport, progress streams, capability announcements and intermittent-node communication behind Ptah's Event/Provider boundaries.

## Independent verification packet

The verifier confirmed that clients, CLI, deployment charts, operators, hosted Synadia services, persistence configuration and JetStream operational guarantees are separate dependencies or surfaces. NATS subjects, stream names, sequence numbers, acknowledgements and consumer IDs are transport evidence, not canonical Ptah identities or proof of external completion.

## Contradiction and supersession

The donor pool correctly identified NATS as an event-fabric donor. No frozen Ptah Event, Receipt, Activity, Node or authority contract is superseded.

## Bounded outcome

`accepted_for_archive_apache_event_transport_donor_with_identity_delivery_and_persistence_boundaries`

Allowed reuse:

- study or integrate NATS behind a replaceable Event/transport Provider;
- retain exact server, client, stream, consumer, configuration and delivery evidence;
- use JetStream only under separately proven persistence and recovery policy.

Restrictions:

- preserve Apache notices and review clients, CLI, operators, charts and hosted services separately;
- do not map NATS subjects, stream sequence or acknowledgements onto canonical Ptah identities or completion;
- do not treat message delivery or persistence acknowledgement as independent proof of external side effects;
- do not make NATS Ptah's authority, ledger or mandatory world model.

This outcome does not authorize implementation.