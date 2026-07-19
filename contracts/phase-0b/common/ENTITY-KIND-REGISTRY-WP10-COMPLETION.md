# WP10 Entity-Kind Registry Completion

**Status:** CANDIDATE  
**Date:** 2026-07-19

This completion registers the implementation-ready Knowledge, Data, Package and Plugin identities required by WP10. Registration does not authorize implementation, dependency selection or public visibility.

## Knowledge

- `knowledge.source` — stable logical source role over exact Objects/revisions.
- `knowledge.source_revision` — immutable source version and extraction policy context.
- `knowledge.ingestion_request` — caller intent and bounded ingestion requirements.
- `knowledge.ingestion_run` — logical ingestion execution mapped to WP02 work.
- `knowledge.segment` — immutable derived source span/chunk with exact lineage.
- `knowledge.coverage` — bounded ingested/skipped/unsupported/error scope.
- `knowledge.index` — stable index role.
- `knowledge.index_revision` — immutable index version over exact source/segment revisions.
- `knowledge.embedding_record` — immutable embedding observation with exact model/config lineage.
- `knowledge.query` — immutable query intent and acceptance constraints.
- `knowledge.query_run` — one logical retrieval/search execution.
- `knowledge.result_set` — immutable ranked result collection.
- `knowledge.result` — one bounded result binding exact source/segment evidence.
- `knowledge.citation` — exact source revision/range/digest citation.
- `knowledge.generated_output` — generated answer/summary/report separate from sources/results.
- `knowledge.verification` — policy-bounded verification of citations, coverage and claims.

## Data

- `data.dataset` — stable logical dataset role.
- `data.dataset_revision` — immutable dataset version over exact Objects/Locations.
- `data.schema_observation` — producer/detector observation about structure and types.
- `data.processing_run` — deterministic or bounded data transformation/analysis run.
- `data.database_connection_reference` — secret-free reference to an external/live database connection.
- `data.database_snapshot` — immutable bounded database snapshot/export.
- `data.table_observation` — immutable table/view/schema/statistics observation.
- `data.quality_report` — bounded quality/completeness/error report.
- `data.export` — explicit export of dataset/query/processing outputs with audience/privacy policy.

## Package

- `package.package` — stable package identity within an exact ecosystem/namespace/source.
- `package.revision` — immutable package version/content revision.
- `package.manifest` — immutable declared package metadata and dependency claims.
- `package.dependency_constraint` — declared acceptable dependency range/condition.
- `package.resolved_graph` — exact resolved dependency graph for one environment/policy.
- `package.lock_record` — immutable lock/pin record with exact digests and sources.
- `package.registry_source` — versioned package source/registry trust and resolution policy.
- `package.installation` — installation/materialization lifecycle for one resolved package graph.
- `package.verification` — integrity, provenance, policy and installed-state verification.

## Plugin

- `plugin.plugin` — stable Plugin identity.
- `plugin.revision` — immutable Plugin code/config revision.
- `plugin.manifest` — declared facilities, tools, events, schemas, permissions and dependencies.
- `plugin.compatibility` — target-specific compatibility with exact Ptah/runtime/provider context.
- `plugin.installation` — package/object materialization and verification lifecycle.
- `plugin.activation` — policy and grant decision enabling one Plugin Revision.
- `plugin.instance` — one running/loaded generation bound to exact Provider/Node/workspace context.
- `plugin.health_observation` — expiring scoped health/readiness observation.
- `plugin.capability_grant` — scoped, expiring, revocable permission/capability grant.
- `plugin.dependency_binding` — exact resolved dependency/service/facility binding.
- `plugin.service_registration` — versioned service/tool/facility exposure registration.
- `plugin.port_registration` — explicit exposed-port/network-listener registration.
- `plugin.update_decision` — reviewed update/hold/rollback/reject decision.
- `plugin.rollback` — explicit rollback execution and verification record.
- `plugin.removal` — disable/uninstall/revoke/cleanup lifecycle and proof.

## Existing canonical families reused

- WP02 Activity/Operation/Attempt/Event/Receipt/Review/Verdict remain canonical execution and proof identities.
- WP03 Content/Object/Object Revision/Relationship/Artifact/Location remain canonical byte, source, output and storage identities.
- WP04 Facility/Provider/Capability/Dispatch Eligibility/health remain canonical runtime identities.
- WP05 Workspace/Session/checkpoint/restore remain canonical world/recovery identities.
- WP06 Transfer/sync/export/backup primitives remain canonical movement/storage identities.
- WP07 Recipe/Plan/Build/Attestation/Signature/Proof Bundle remain canonical deterministic execution and provenance identities.
- `runtime.lease` remains canonical ownership/fencing authority.
- Credentials and raw secrets are never Plugin, Package, Dataset or Connection identity.

## Non-collapse rules

1. Source Object is not Segment, Index, Result, Citation or Generated Output.
2. Index existence is not source coverage, correctness, freshness or authority.
3. Search rank is not truth, acceptance or a verified claim.
4. Citation identity binds exact source revision/range/digest; filename/URL alone is insufficient.
5. Dataset Snapshot is not live database truth.
6. Package name/version/coordinate is not exact revision without namespace/source/digest.
7. Constraint, Resolved Graph and Lock Record remain separate.
8. Plugin installed, activated, running, healthy, authorized and accepted remain separate.
9. Signature/integrity does not imply Plugin safety, functionality or release acceptance.
10. Backend IDs, vector-store IDs, index shard IDs, package-manager IDs, process IDs, plugin handles and port numbers remain scoped Aliases/evidence.
11. Negative, stale, unsupported, partial and inconclusive results remain immutable history.
