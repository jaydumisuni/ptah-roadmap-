# Phase 0A — WP10 Knowledge, Data, Search and Plugin Composition

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Runtime code:** NOT STARTED

## Purpose

Close Ptah's knowledge-source, ingestion, indexing, grounded search, structured-data, external-adapter, package/plugin and provider boundaries without turning Ptah into an agent, RAG product, analytical database, marketplace or reasoning council.

## Sources inspected and saved

### Internal foundation

- Hunter knowledge, memory, learning, local/online sync, retrieval and provider bridges.

Saved record:

- `internal/HUNTER-KNOWLEDGE-MEMORY-SEARCH.md`

### Knowledge and retrieval

- RAGFlow;
- LlamaIndex.

Saved records:

- `donors/RAGFLOW.md`
- `donors/LLAMAINDEX.md`

### Workflow/application and plugin configuration

- Dify.

Saved record:

- `donors/DIFY.md`

### Structured data and SQL

- Polars;
- DuckDB.

Saved records:

- `donors/POLARS.md`
- `donors/DUCKDB.md`

### Lightweight tool runtime

- Deno.

Saved record:

- `donors/DENO.md`

### External tool/resource protocol

- Model Context Protocol specification;
- official MCP reference servers.

Saved record:

- `donors/MCP.md`

### Registry and plugin lifecycle

- ClawHub;
- OpenClaw plugin manifest, install, activation, runtime-inspection, update and removal behavior.

Saved records:

- `donors/CLAWHUB.md`
- `donors/OPENCLAW.md`

### Boundary callers and unresolved donor recovery

- Hermes Agent;
- MiniRouter.

Saved records:

- `donors/HERMES-AGENT.md`
- `donors/MINIROUTER.md`

Hermes is classified as an optional caller/workload. MiniRouter is classified for a later routing/evaluation cluster and is not required for WP10 closure.

## Canonical pins

- Hunter: `df0bd758a2f08e5d861628be3146aeecdb9677d6`
- RAGFlow: `b7a3a2760f46dbdff1e0cce307bfb874944244b4`
- LlamaIndex: `dbdaf89dc66a6469081c9f8fddc9c1bf6c43d8a2`
- Dify: `2ec34b2cfbcf0ca1faabfff918b7e74d93aeffcf`
- Polars: `434fa104a500e2c3371fdcd5701ce829848274d1`
- DuckDB: `117e1a46be1c903c5a36ee3c881c125597f93c60`
- Deno: `c71e43af07c3392c788286e20481998f6004b68d`
- MCP specification: `26897cc322f356487da89113451bd16b520b9288`
- MCP reference servers: `d31124c982401739917fd817c2a59db344529c16`
- ClawHub: `aaa73625ed4100b1006653f49089f2a2d969a427`
- OpenClaw core pass: `73d04395defe25601ef69647e93343f38c2c9a20`
- OpenClaw plugin addendum: `05fb8e6e6190ae65b6f1c5fdc0c7dadd960fe3d4`
- Hermes Agent: `7fd419e5e6a0ac53f934a69226262c41ba130a2c`
- MiniRouter: `bf3ea957f6ef3de358528f73e0518ec51e39d8f3`

## Licence findings

- RAGFlow: Apache-2.0.
- LlamaIndex: MIT at root; optional integrations require independent review.
- Dify: modified Apache-2.0 with material source-based multi-tenant and frontend-branding restrictions.
- Polars: MIT.
- DuckDB: permissive MIT-style licence.
- Deno: MIT.
- MCP specification: MIT.
- MCP reference servers: Apache-2.0 for new contributions with existing MIT code.
- ClawHub: MIT source; published skill content uses a separate MIT-0 policy.
- OpenClaw: MIT.
- Hermes Agent: MIT.
- MiniRouter: no repository licence recovered; study-only.
- Hunter: private internal source.

## Composite result

```text
Ptah Knowledge Source
  governed origin, connector, permission, freshness and retention policy

Ptah Source Object / View Revision
  immutable retained source truth

Ptah Corpus and Source Snapshot
  versioned permitted source membership

Ptah Document Revision and Chunk
  normalized logical content and deterministic exact source ranges

Ptah Index Revision
  rebuildable lexical/vector/metadata/hybrid derived state

Ptah Query, Result and Citation
  durable query, explained ranking and exact source grounding

LlamaIndex
  primary modular local connector/transformation/retrieval foundation candidate

RAGFlow
  optional heavier end-to-end Knowledge Facility

Ptah Dataset / Table / Schema / Data Query / Transformation / Result
  stable structured-data identities and lineage

Polars
  primary DataFrame/lazy/streaming analytical engine

DuckDB
  primary embedded SQL analytical engine

Ptah Package / Package Release / Installed Plugin / Activation
  immutable release, materialized install and live runtime generations

ClawHub
  primary registry/discovery/version/pin/scan lifecycle donor

OpenClaw
  cold manifest, installed/enabled/active, source and runtime-inspection patterns

Deno
  primary lightweight permission-scoped JS/TS runtime candidate

MCP
  primary external Tool/Resource/Prompt adapter

OCI / stronger sandbox / VM
  escalation path for native, FFI, untrusted or broadly privileged code

Hunter / Hermes / Dify / OpenClaw
  optional callers or Applications that retain reasoning, memory and relationship ownership
```

Source truth, indexes, Queries, Citations, data plans, Package Releases and Activations retain separate identities.

## Accepted architecture

Saved as `decisions/ADR-0013-KNOWLEDGE-DATA-SEARCH-PLUGIN-BOUNDARY.md`.

Key decisions:

1. Conversation, Knowledge Source, source Object/View, Corpus, Document, Chunk, Index Revision and caller-owned memory remain separate.
2. Source Objects and exact revisions are truth; indexes, embeddings, summaries and caches are derived and rebuildable.
3. Parser, chunker, embedding, reranker, analyzer, source-snapshot or material-config changes create new Index Revisions.
4. Query, Result, ranking explanation and Citation remain separate.
5. Exact Citations bind to exact permitted source revisions and ranges.
6. Permissions apply during acquisition, retention, embedding, indexing, querying, ranking, citation, export and deletion.
7. Revocation/deletion uses tombstones, reconciliation and proof across partial backend failures.
8. LlamaIndex is the primary modular local foundation candidate; RAGFlow is an optional larger hosted Facility.
9. Search across Objects, Activities, Artifacts and Workspaces is native Ptah catalogue/index behavior, not only document RAG.
10. Polars and DuckDB are analytical engines behind Ptah Dataset/Query/Result identities; transactional databases remain separate Facilities.
11. Package, Package Release, Installed Plugin, Activation and Registry Entry remain separate.
12. Family and executes-code state are mandatory and visible.
13. Discovery, registry verification and scans are evidence inputs, not installation authority or runtime proof.
14. Cold manifest inspection and live runtime capability proof remain separate.
15. Pins with reasons block automatic and forced upgrades.
16. Upgrades stage compatibility, migration, health, conformance, cutover and rollback.
17. Removal covers data, credentials, processes, configuration and orphan cleanup.
18. Deno is the lightweight runtime candidate; native/FFI/untrusted/broadly privileged plugins escalate to OCI or VM isolation.
19. MCP is one external adapter protocol, not Ptah's internal Object/Activity model.
20. Hunter, Hermes and other callers retain reasoning, personal memory, skill promotion, provider choice and acceptance policy.
21. Dify is study-only or a separately licensed external Application because of its modified licence.
22. MiniRouter moves to later routing/evaluation work and remains study-only until a licence is resolved.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `SEARCH-001` unified source-grounded search and retrieval;
- `DATA-001` structured data, analytical tables and database-query Activities;
- `PLUGIN-001` Package/Plugin discovery, install, activation, upgrade, rollback and removal;
- knowledge/source/index portions of `CORE-003` and `STORE-003`;
- plugin/contribution completion portions of `CORE-004`;
- Knowledge/Data/Plugin portions of `SESSION-001`, `OBS-001` and `PROV-001`;
- provider-neutral model/data adapter direction;
- MCP adapter boundary;
- external reasoning/caller ownership boundary.

Still open elsewhere:

- strong isolation backends and secure multi-tenant execution;
- distributed placement/scheduling and routing-policy evaluation;
- reproduction/security workloads and scanner composition;
- Linux AT-SPI semantic completion;
- public documentation/research-source cluster;
- Phase 0A review/freeze across all requirements.

## Phase 0B contracts required

1. Knowledge Source, connector and cursor/checkpoint schemas.
2. Corpus, source snapshot and membership schemas.
3. Document Revision, Chunk and exact source-range schemas.
4. Index and Index Revision schemas.
5. ingestion, sync, re-index, revoke, delete and reconcile Activity types.
6. Query, Result, Result Set and Citation schemas.
7. permission, audience, freshness, retention and tombstone rules.
8. Dataset, Table, Column Schema, snapshot and lineage schemas.
9. Data Query, Transformation and Result Artifact schemas.
10. Package, Package Release, Installed Plugin and Activation schemas.
11. manifest, family, runtime, permission, resource and compatibility schemas.
12. registry source, alias/tag and immutable release-resolution schemas.
13. install, health, activate, update, migrate, rollback, quarantine and removal Activities.
14. MCP adapter mappings.
15. provider-neutral model, embedding, reranker and data-source adapter contract.
16. telemetry, proof and cross-backend conformance conventions.

## Validation set

- multi-format ingestion with exact source/parser/chunker/index revision;
- unchanged re-ingestion without identity drift;
- parser/embedding re-index without overwriting old revision;
- exact permission-bound citations;
- source revocation/deletion through partial backend failure;
- honest hosted-to-local degraded search;
- LlamaIndex/RAGFlow/backend replacement;
- metadata-filter semantic conformance;
- Polars/DuckDB cross-engine data result comparison;
- restricted UDF/extension/write/network permissions;
- alias/tag resolution to immutable signed Package Release;
- content-only, Deno, MCP and OCI plugin classes;
- reasoned pin and forced-update refusal;
- failed upgrade and rollback;
- quarantine with retained evidence;
- complete removal/credential/orphan cleanup;
- MCP Tool-to-Activity mapping;
- Hunter/Hermes caller boundary;
- provider/registry/runtime replacement;
- retained negative, partial, stale and failed evidence.

## Next Phase 0A group

Proceed with **WP11 — Strong Isolation and Distributed Placement/Scheduling**:

- gVisor;
- Kata Containers;
- Firecracker;
- youki;
- crun;
- Ray;
- Node/provider placement, leases, fencing and secure network completion;
- MiniRouter only as a routing/evaluation workload, not Core;
- Linux AT-SPI completion may be handled separately or alongside the next relevant platform pass.

No runtime implementation is approved yet.
