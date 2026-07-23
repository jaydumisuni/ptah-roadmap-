# D006 — OpenTelemetry Collector

Status: candidate record — paired evidence complete

Primary Archivist: `AF06-P05`

Independent Verifier: `AF06-V05`

Inspected: 2026-07-23

## Canonical source identity

- source: `open-telemetry/opentelemetry-collector`;
- default branch: `main`;
- exact inspected commit: `52e6bf4aaabab74fbe7fae0b3984e983ec847f93`;
- root licence: Apache-2.0;
- repository role: vendor-neutral telemetry receive/process/export service;
- archived: false.

## Primary evidence packet

The Collector provides receiver, processor, exporter, connector and pipeline patterns for traces, metrics and logs across Nodes, Providers and Activities.

## Independent verification packet

Components, contrib distributions, exporters and remote vendors have separate compatibility, privacy and licence surfaces. Telemetry is observation evidence and may be sampled, delayed, dropped, transformed or redacted; it cannot replace canonical Receipts or prove external effects.

## Contradiction and supersession

OpenTelemetry remains observability infrastructure, not Ptah's ledger or truth authority.

## Bounded outcome

`accepted_for_archive_apache_observability_pipeline_with_component_privacy_sampling_and_receipt_boundaries`

Allowed reuse:

- run a pinned Collector distribution behind Ptah telemetry Providers;
- retain exact components, configuration, sampling, redaction and export destinations.

Restrictions:

- review contrib components/exporters separately;
- prevent secrets/private data from entering unauthorized telemetry;
- keep dropped, sampled and transformed limitations explicit;
- do not treat telemetry delivery as immutable Receipt or post-condition proof.

This outcome does not authorize implementation.