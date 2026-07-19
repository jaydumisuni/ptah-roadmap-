# ADR-0027 — Knowledge, Data, Package and Plugin Boundary

**Status:** ACCEPTED  
**Date:** 2026-07-19

## Context

Ptah must support source-grounded knowledge, structured data, packages and extensible Plugins without allowing RAG systems, vector stores, databases, package managers, workflow frameworks, MCP servers or Plugin hosts to replace Ptah Core identity, Activity, policy or evidence truth.

## Decision

Adopt `urn:ptah:schema-catalog:knowledge:0.1.0` with 50 schemas and nine lifecycle machines.

1. Source, Source Revision, Segment, Coverage, Index, Query, Result, Citation, Generated Output and Verification remain distinct.
2. Search rank is never truth; Citations bind exact source revision/range/digest.
3. Dataset, Dataset Revision, schema/table observations, processing, live Connection Reference, immutable Snapshot, Quality Report and Export remain distinct.
4. Raw credentials remain external to records and evidence.
5. Package, Revision, Manifest, Constraint, Resolved Graph, Lock Record, Registry Source, Installation and Verification remain distinct.
6. Package coordinate, install path and package-manager ID remain scoped Aliases.
7. Plugin, Revision, Manifest, Compatibility, Installation, Activation, Instance, Health, Capability Grant, Dependency Binding, Service/Port Registration, Update Decision, Rollback and Removal remain distinct.
8. Installation never implies activation, authority, health, functionality or acceptance.
9. Grants are scoped, expiring and revocable; stale grants/generations cannot authorize work.
10. Service and port registration require current authority and explicit exposure policy.
11. Rollback and removal create new WP02 Attempts and require post-condition verification.
12. Negative, partial, stale, unsupported and inconclusive evidence remains immutable.
13. RAG/vector/database/package-manager/Plugin-host backends are replaceable adapters or workloads.

## Donor boundary

RAGFlow and LlamaIndex inform ingestion and retrieval patterns. Dify informs application/workflow and Plugin-management patterns but is not Ptah Core. Polars informs data processing. Deno informs permission-scoped script/runtime patterns. MCP is an adapter protocol, not Ptah's internal Object/Activity model. The recovered donor inventory keeps these roles explicit. fileciteturn308file0

## Consequences

Implementation teams receive exact identities, lifecycle boundaries, migration rules and proof cases rather than framework-specific assumptions. Backend replacement creates new revisions/generations/evidence without destroying canonical Ptah history.

## Deferred

Executable conformance is WP13. Dependency selection and implementation remain blocked until Phase 0C authorization.
