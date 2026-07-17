# Donor Record — OpenTelemetry Collector and Specification

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — OBSERVABILITY FOUNDATION DONOR  
**Inspected:** 2026-07-17

## Identity

### OpenTelemetry Collector

- Canonical URL: https://github.com/open-telemetry/opentelemetry-collector
- Default branch: `main`
- Pinned commit: `47267b188b260e1c4123de9d89bdc886f05d4d3e`
- Licence: Apache-2.0
- Activity: Active CNCF project

### Collector Contrib

- Canonical URL: https://github.com/open-telemetry/opentelemetry-collector-contrib
- Pinned commit: `0193109060aa80f0f9c42c33501b4d64b655a86b`
- Licence: Apache-2.0 subject to component dependency review

### OpenTelemetry Specification

- Canonical URL: https://github.com/open-telemetry/opentelemetry-specification
- Pinned commit: `b59c1f71e6419483e243ce386325d411f1ca9a75`
- Licence: Apache-2.0

- Classification: Vendor-neutral telemetry specification, pipeline and Collector donor
- Ptah targets: traces, metrics, logs, resource identity, Activity correlation, Node health and exporter neutrality

## Files/components inspected

- Collector `README.md`
- Collector service/config and component graph source locations
- receiver, processor, exporter, extension and connector pipeline model
- internal Collector telemetry and monitoring references
- OTLP stability statement
- Collector image-signing verification path
- current specification and Contrib source pins

## Verified capabilities and patterns

- Vendor-neutral receipt, processing and export of telemetry.
- Unified traces, metrics and logs in one deployable Collector.
- Agent or centralized Collector deployment modes.
- Extensibility without changing Collector core.
- Receiver, processor and exporter pipelines with extensions/connectors.
- Stable OTLP protocol version at the inspected pin.
- Collector is intended to be observable itself.
- Broad integration through the Contrib distribution.
- Security guidance, fuzzing, CI and component stability/versioning records.
- Published Collector images are signed and can be verified with Cosign.

## What OpenTelemetry completes

- Standard correlation across Ptah control plane, Nodes, Providers, Facilities and external services.
- Vendor-independent export rather than hard-coding one log or metrics backend.
- A shared language-neutral trace context for polyglot Facilities.
- Resource identity and service health signals.
- Pipeline processing for sampling, batching, enrichment, filtering and export.
- A bridge between live operational events, durable Activity history and proof artifacts.

## Important limitations for Ptah

- Telemetry is evidence about execution; it is not canonical Workspace, Activity, Object, Session or Artifact state.
- Collector pipelines can drop, sample, delay or transform data and therefore cannot be the sole audit ledger.
- High-cardinality labels can create cost and performance problems.
- Logs, metrics and traces do not automatically prove a side effect or artifact is correct.
- Collector Contrib components vary in stability and bring separate dependencies/security risk.
- OpenTelemetry does not schedule Activities, recover workflows or transport large Objects and display streams.
- Resource and attribute naming must be governed by Ptah-owned semantic conventions.

## Must not be inherited

- Telemetry backend/vendor identity exposed in Ptah's public contracts.
- Trace IDs used as the only Activity or operation identity.
- Sampling enabled on proof-critical evidence without explicit classification.
- Sensitive credentials, document content, customer data or raw secrets emitted as attributes/logs.
- Every Contrib component bundled by default.
- Telemetry success interpreted as operation or artifact acceptance.
- Unbounded metric labels for Object IDs, file paths or user-provided values.

## Integration decision

**ADOPT OTLP AND OPEN TELEMETRY SEMANTICS; WRAP THE COLLECTOR AS PTAH'S TELEMETRY PIPELINE.**

OpenTelemetry is the primary machinery candidate for `OBS-001`. Ptah should emit OTLP-compatible traces, metrics and logs from the control plane, Node agent, Workspace Providers, Facilities and Activity workers.

The Collector remains a replaceable deployment component. Ptah owns correlation semantics and the link from telemetry to durable records and proof artifacts.

## Native Ptah gap

Ptah must define semantic conventions for:

- `ptah.project.id`;
- `ptah.workspace.id`;
- `ptah.activity.id`;
- `ptah.operation.id` and idempotency key;
- `ptah.node.id` and connection epoch;
- `ptah.provider.id`;
- `ptah.facility.id` and version;
- `ptah.object.id` and content hash where safe;
- `ptah.artifact.id`;
- `ptah.session.id`;
- caller/request correlation without exposing private identities.

Ptah must also own:

- proof-critical versus sampled operational telemetry classes;
- log redaction and secret filtering;
- resource accounting for CPU, RAM, GPU, disk, network and storage;
- Activity receipts and error taxonomy;
- links between traces, NATS events, Temporal history and retained artifacts;
- local buffering when the Collector is unavailable;
- retention/export profiles for online and local Nodes.

## Exit strategy

Ptah emits standard OTLP and preserves durable receipts independently. Collectors and export backends can be changed without modifying Ptah's Activity or Object contracts.

## Validation required

1. Trace one operation from public request through control plane, NATS event, Node, Provider, Facility, Temporal Activity and Artifact creation.
2. Confirm logs, metrics and traces share Ptah correlation IDs.
3. Disconnect the Collector; local buffering and core execution continue, followed by recovery/export.
4. Apply redaction tests proving credentials and file content are not leaked.
5. Stress high concurrency and verify bounded telemetry overhead.
6. Demonstrate unsampled proof-critical receipts while ordinary telemetry may be sampled.
7. Replace one exporter/backend without changing Ptah instrumentation.
8. Verify signed Collector images and pin enabled components.
