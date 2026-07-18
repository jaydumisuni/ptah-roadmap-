# ADR-0013 — Knowledge Source, Index, Query, Data and Plugin Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Phase:** 0A / WP10 Knowledge, Data, Search and Plugin closure

## Context

Ptah requires a neutral knowledge, data, search and extension layer that can support humans, Hunter, other approved callers, specialist applications and future systems without becoming an agent, model provider, memory product, RAG application or plugin marketplace itself.

The inspected sources solve different layers:

- internal Hunter contributes separation of conversation, approved knowledge and durable memory; proof/approval gates; local-first sync; source hashes; degraded local/online retrieval; and provider-adapter lessons;
- RAGFlow contributes end-to-end document ingestion, visible parse state, hybrid retrieval, metadata filtering, reranking, deletion/reconciliation and search-backend abstraction;
- LlamaIndex contributes modular connectors, source/node relationships, transformation pipelines, version-sensitive caches, deduplication, upsert and deletion strategies;
- Dify contributes typed workflow/application graphs, provider configuration, plugin manifests, installation tasks, permissions/resources, marketplace policy and upgrade patterns, but its modified licence prevents it from becoming a freely rebranded multi-tenant Ptah foundation;
- Polars contributes lazy/eager/streaming DataFrame plans and structured transformation execution;
- DuckDB contributes embedded analytical SQL over files and local databases;
- Deno contributes a permission-scoped lightweight JavaScript/TypeScript tool runtime below OCI/VM isolation;
- MCP contributes external Tool, Resource and Prompt interoperability, capability negotiation, progress, cancellation and task augmentation;
- ClawHub contributes registry discovery, exact versions, fingerprints, pins, scans, compatibility, soft deletion and package-family UX;
- OpenClaw contributes cold manifest discovery, installed/enabled/active state separation, explicit install sources, runtime registration inspection and cleanup behavior;
- Hermes Agent and Hunter demonstrate the external-caller boundary: reasoning, identity, personal memory and self-improvement remain outside Ptah Core;
- MiniRouter belongs to later routing evaluation rather than this subsystem.

No donor defines Ptah's canonical Knowledge Source, Corpus, Document, Chunk, Index Revision, Query, Result, Citation, Dataset, Table, Package Release, Installed Plugin, Activation, permission or proof model.

## Decision

Ptah will own backend-neutral contracts for:

1. Knowledge Source;
2. Corpus;
3. Document and Document Revision;
4. Chunk and source range;
5. Index and Index Revision;
6. Connector and ingestion cursor;
7. Query, Result, Result Set and Citation;
8. Dataset, Table, Column Schema and snapshot/revision;
9. Data Query, Transformation and Result Artifact;
10. Package, Package Release, Installed Plugin and Plugin Activation;
11. plugin family, runtime class, permissions, resources and trust evidence;
12. registry source, aliases, tags and immutable release resolution;
13. install, activate, health, upgrade, migrate, roll back, quarantine and remove Activities;
14. model, embedding, reranking and data-provider adapters;
15. MCP and other external adapter mappings;
16. external caller/application ownership of reasoning, memory and acceptance.

No RAGFlow dataset, LlamaIndex Node, Dify workflow/plugin, Polars DataFrame, DuckDB table, MCP Resource URI, ClawHub package slug, OpenClaw plugin ID, Hunter lesson path or Hermes skill becomes canonical Ptah identity.

---

# Knowledge truth classes

Ptah keeps these classes separate:

```text
Conversation
  caller/product interaction record

Knowledge Source
  governed external or internal source definition

Source Object / View Revision
  immutable retained bytes or exact captured representation

Corpus
  governed grouping of permitted source revisions

Document Revision
  normalized logical document bound to exact source revision

Chunk
  derived bounded segment with exact source range and derivation recipe

Index Revision
  rebuildable lexical/vector/metadata/hybrid derived state

Lesson / Durable Memory
  caller-owned promoted knowledge, never automatic Ptah truth
```

Conversation, source content, derived indexes and caller-owned memory are not interchangeable.

Ptah does not automatically turn chat, retrieved text, generated summaries or successful Tasks into durable memory or approved knowledge.

---

# Knowledge Source

A Knowledge Source identifies a governed origin and acquisition contract.

```text
knowledge_source_id
source_type
owner_reference
workspace_scope
visibility_class
connector_type
connector_configuration_reference
credential_reference
permission_policy_reference
freshness_policy
retention_policy
created_at
state
```

Source types may include:

```text
ptah_object
workspace_folder
repository
website
browser_capture
cloud_drive
mailbox
api
sql_database
file_collection
manual_approved_document
external_knowledge_service
```

A Knowledge Source is not the current index and not a credential container.

States include:

```text
configured
available
degraded
auth_required
permission_denied
stale
syncing
revoked
deleting
deleted
failed
```

---

# Corpus

A Corpus is a governed grouping of source and document revisions for a purpose.

```text
corpus_id
workspace_id
name
purpose
source_membership_rules
permission_policy_reference
audience_scope
current_source_snapshot_id
current_index_revision_ids
retention_policy
state
```

Corpus membership is versioned. A later source snapshot does not silently rewrite the evidence used by an earlier Query.

---

# Document and Chunk identity

A Document Revision maps one source revision into a logical document form.

```text
document_id
document_revision_id
knowledge_source_id
source_object_or_view_revision_id
source_locator_metadata
media_type
language
parser_id_and_version
normalization_recipe_id
created_at
content_digest
state
```

A Chunk is derived and deterministic where possible:

```text
chunk_id
document_revision_id
chunker_id_and_version
segment_ordinal
source_range
page_or_region
parent_chunk_id
previous_chunk_id
next_chunk_id
content_digest
metadata_digest
```

`chunk_id` must be stable for an unchanged source revision, parser, chunker and exact range. Backend-generated UUIDs remain adapter metadata.

Source ranges may identify:

- byte range;
- character range;
- line range;
- page and bounding region;
- DOM node/range;
- table/sheet/cell range;
- audio/video time range;
- database snapshot/table/row-key range;
- repository commit/path/line range.

---

# Index and Index Revision

An Index is a logical retrieval capability. An Index Revision is one immutable derived build.

```text
index_id
index_revision_id
corpus_id
source_snapshot_id
index_type
backend_type
backend_version
parser_versions
chunker_versions
embedding_provider_and_model_revision
reranker_revision
lexical_analyzer_revision
metadata_schema_revision
build_recipe_id
build_activity_id
location_references
created_at
state
```

Index types include:

```text
lexical
vector
metadata
hybrid
knowledge_graph
structured_table
full_text_sql
```

Indexes, embeddings, summaries and caches are rebuildable derived state. Their loss does not erase source truth.

A parser, chunker, embedding, reranker, analyzer, source snapshot or material configuration change creates a new Index Revision rather than mutating the old proof record.

States include:

```text
planned
building
partial
ready
degraded
stale
superseded
deleting
deleted
failed
```

`ready` does not mean every source is fresh or every backend is reconciled. Coverage and limitations are explicit.

---

# Ingestion and synchronization

Ingestion, parsing, chunking, embedding, indexing, re-indexing, synchronization, deletion and reconciliation are Ptah Activities with attempts and Receipts.

A connector retains:

```text
connector_id
knowledge_source_id
connector_version
cursor_or_checkpoint
last_attempt_id
last_successful_snapshot_id
remote_revision_metadata
rate_limit_state
degraded_capabilities
```

Source acquisition must retain hashes, remote revision/version metadata and the exact Object/View captured where lawful and permitted.

Local-first and remote/shared indexes may coexist. Failure of one provider is reported as degraded capability rather than silently claiming equivalent results.

Deletion/revocation uses tombstones and reconciliation:

1. revoke future permission;
2. mark affected source/document/chunk/index relationships stale or deleting;
3. delete or quarantine derived records across all backends;
4. prove the source no longer appears in permitted future queries;
5. retain required Activity, Receipt, legal/audit and provenance history;
6. report partial cleanup rather than flattening it into success.

---

# Query, Result and Citation

A Query is a durable request independent of one search backend.

```text
query_id
workspace_id
caller_reference
query_type
query_text_or_expression
scope_references
permission_snapshot_reference
source_snapshot_or_freshness_requirement
requested_retrieval_modes
ranking_configuration
limit_and_budget
created_at
activity_id
```

Query types include:

```text
lexical
semantic
metadata
hybrid
structured_sql
structured_expression
object_search
activity_search
artifact_search
workspace_search
external_live_search
```

A Result records one ranked candidate and explanation:

```text
result_id
query_id
rank
score_components
backend_reference
index_revision_id
source_document_revision_id
chunk_or_range_reference
permission_decision_reference
freshness_state
result_payload_reference
limitations
```

A Citation is separate from ranking:

```text
citation_id
result_id_or_claim_reference
source_object_or_view_revision_id
document_revision_id
exact_source_range
captured_excerpt_digest
render_or_capture_reference
accessed_at
citation_state
```

Citation states include:

```text
exact
approximate
source_unavailable
permission_revoked
stale
superseded
invalid
```

Similarity, reranking and prompt insertion do not automatically create an exact Citation. Generated answers and claims remain caller-owned outputs and require their own evidence/review policy.

---

# Permission and privacy boundary

Permissions are enforced at every relevant stage:

- source acquisition;
- Object/View retention;
- parsing and metadata extraction;
- embedding and remote-provider transmission;
- index membership;
- Query scope;
- Result ranking;
- Citation rendering;
- export and sharing;
- deletion and retention.

A source may be permitted for local lexical search but forbidden from remote embedding or public Citation display.

Public/customer Workspaces cannot access private Hunter/company knowledge merely because the same index engine is used.

Credentials are references managed by a credential Facility. They are not embedded in source, connector, plugin or workflow records.

---

# Search provider composition

Initial provider direction:

```text
LlamaIndex
  primary modular local connector/transformation/retrieval foundation candidate

RAGFlow
  optional heavier end-to-end Knowledge Facility for larger deployments

Native lexical / SQL search
  minimum local fallback and cross-check path

Browser Facility
  live rendered web/source capture and citation evidence

MCP / HTTP / SDK adapters
  external interoperability only
```

Providers implement Ptah Query, Result and Citation mappings. They remain replaceable.

Search across Objects, Activities, Artifacts and Workspaces uses native Ptah catalogue/index projections, not only document RAG.

Backend abstraction requires conformance tests. A shared method signature does not prove equivalent negative filters, ranking, deletion or permission semantics.

---

# Structured data boundary

Ptah owns:

```text
Dataset
Dataset Revision or Snapshot
Table
Table Revision
Column Schema
Data Query
Transformation
Execution Plan Artifact
Result Set
Result Object or Artifact
Field/row/source lineage
```

Polars is the primary local DataFrame/lazy/streaming transformation candidate.

DuckDB is the primary embedded SQL analytical database candidate.

Transactional service databases remain separate Facilities. Polars and DuckDB do not become the universal metadata/catalogue database.

A Data Query retains:

- exact source Object or database snapshot;
- original expression or SQL;
- normalized logical plan where available;
- optimized/physical plan evidence where available;
- engine, version, build features and runtime;
- permissions;
- resource budget;
- output schema;
- lineage;
- result verification state.

User-defined code, extension loading, DDL and external network/database access are separate high-risk permissions.

---

# Package and Plugin identity

Ptah keeps these identities separate:

```text
Package
  logical named contribution

Package Release
  immutable exact bytes and metadata

Installed Plugin
  one materialization of one release in a deployment/Node/Workspace scope

Plugin Activation
  one enabled/live runtime generation

Registry Entry
  discovery and alias metadata
```

A Package Release contains:

```text
package_release_id
package_id
family
version
content_digest
source_reference
source_commit_or_tag
licence_records
manifest_revision
signature_references
sbom_reference
attestation_references
compatibility_ranges
runtime_class
permission_declarations
resource_declarations
published_at
```

Package families include:

```text
facility_plugin
domain_pack
ui_contribution
recipe
mcp_server
deno_tool
oci_service
native_service
content_bundle
skill_or_instruction_bundle
model_or_data_provider_adapter
```

`executes_code` is explicit and prominent.

Registry names, aliases, popularity, verification labels, tags and `latest` are discovery metadata. Installation resolves them to an immutable Package Release digest.

---

# Plugin lifecycle

Plugin lifecycle is Activity-driven:

```text
discovered
inspected
review_required
approved_for_install
installing
installed
disabled
activating
active
degraded
restart_required
update_available
upgrade_staged
migrating
rollback_ready
quarantined
removing
removed
failed
```

Cold manifest discovery and live runtime capability proof are separate.

An Installed Plugin records:

- exact Package Release;
- source registry/repository/bundle;
- digest and signatures;
- materialized dependencies;
- runtime and isolation class;
- granted permissions and resources;
- configuration/credential references;
- local modifications/fingerprint;
- pin and pin reason;
- installation Activity/Receipts;
- current Activation generation;
- health and limitations.

Pins block automatic and forced upgrades unless an explicit governed unpin/change occurs.

An upgrade is staged and must support:

1. compatibility check;
2. dependency and licence review;
3. data/config migration plan;
4. isolated activation/health proof;
5. dependent Recipe/Panel/Facility conformance;
6. cutover;
7. rollback;
8. retained old release and evidence under policy.

Removal includes data retention/deletion, credential revocation, process/service shutdown, registry/config cleanup and orphan-state proof.

---

# Runtime classes

Runtime class is explicit:

```text
content_only
in_process_trusted
permission_scoped_deno
wasm_or_wasi
subprocess
oci_container
strong_container_sandbox
microvm_or_vm
remote_managed_service
```

Deno is the primary lightweight JavaScript/TypeScript runtime candidate for approved permission-scoped tools.

In-process third-party code is not the default. Native modules, FFI, broad subprocess access, untrusted plugins and hostile inputs escalate to OCI, stronger container or VM isolation.

Runtime permission flags are adapter metadata. Ptah permissions bind to exact Workspace, Object/View, network, credential, process and resource scopes.

---

# MCP boundary

MCP is a primary external Facility adapter protocol.

- MCP Tool maps to approved Facility method/Activity creation.
- MCP Resource maps to permitted Object/View/Knowledge references.
- MCP Prompt remains caller-facing untrusted metadata.
- MCP task IDs, request IDs and URIs remain adapter-local.
- MCP progress and cancellation map to Ptah Events/controls but do not replace the Activity Ledger.
- MCP sampling and elicitation explicitly name the external reasoning/human owner.
- Tool annotations are advisory claims requiring verification.
- Registry discovery is followed by Package review and immutable release resolution.

Ptah remains usable without MCP.

---

# External reasoning and memory

Hunter, Hermes Agent, Dify, OpenClaw and future systems may consume Ptah.

They retain ownership of:

- reasoning;
- prompts and personalities;
- user relationship;
- agent memory;
- lesson/skill promotion;
- model choice and routing policy;
- answer generation;
- acceptance criteria.

Ptah owns the neutral world, source records, queries, Activities, Objects, plugins, evidence and permissions used by those callers.

MiniRouter and other routing systems remain optional experimental workloads evaluated through later routing/provider contracts.

---

# Licence and source boundary

- RAGFlow, LlamaIndex, Polars, Deno, DuckDB, MCP, ClawHub, OpenClaw and Hermes have compatible permissive root licences at inspected pins, subject to transitive/integration/package review.
- Dify has material additional restrictions on source-based multi-tenant hosting and frontend rebranding; it is study-only or a separately licensed external Application.
- MiniRouter has no recovered repository licence and remains study-only.
- Every connector, model, parser, plugin, dataset and transitive dependency retains its own licence/provenance decision.

---

# Consequences

## Positive

- Ptah can support local and larger hosted knowledge deployments without making one RAG platform mandatory.
- Source truth survives index replacement or loss.
- Search results remain grounded in exact permitted revisions and ranges.
- Structured-data execution can use DataFrame and SQL engines behind stable identities.
- Plugins can be discovered publicly without treating publication as approval.
- Content bundles, Deno tools, MCP servers, OCI services and UI contributions remain visibly different risk classes.
- Hunter and other callers can use the same Facilities without defining public Ptah identity.
- Provider, registry and engine replacement remains possible.

## Costs

- More identities and migration records are required.
- Permission, deletion and freshness enforcement spans several stages and backends.
- Exact Citations require retained source captures and range mapping.
- Plugin installation requires supply-chain review, staged activation and rollback machinery.
- Cross-backend semantic conformance tests are mandatory.
- Local and hosted deployments need different provider compositions while preserving the same contracts.

---

# Rejected alternatives

## Use RAGFlow as the complete knowledge model

Rejected. It is a useful optional Facility, but its product-local identities, heavy deployment and derived indexes cannot own Ptah source truth.

## Use LlamaIndex Nodes as canonical documents/chunks

Rejected. They are library objects with backend/local IDs and incomplete provenance/permission semantics.

## Use Dify as Ptah Core or universal workflow/plugin shell

Rejected. It mixes caller/application concerns with platform runtime and has material licence restrictions.

## Let chat automatically become memory

Rejected. Conversation, approved knowledge, source truth and caller memory remain separate.

## Treat similarity as citation

Rejected. Exact source revision/range is required for an exact Citation.

## Treat indexes as source truth

Rejected. Indexes are rebuildable derived state.

## Use one analytics engine for all data and transactional storage

Rejected. Polars and DuckDB are analytical providers; transactional databases remain separate Facilities.

## Treat MCP as Ptah's internal protocol/model

Rejected. MCP is one external adapter.

## Treat registry verification or scans as plugin approval

Rejected. They are evidence inputs, not authority or runtime proof.

## Run all plugins in process

Rejected. Runtime class and isolation are risk-based.

## Embed Hunter, Hermes or another agent council into Ptah

Rejected. External callers own reasoning and relationship.

---

# Phase 0B contract set

Phase 0B must define and version:

1. Knowledge Source and connector schemas;
2. Corpus and source-snapshot schemas;
3. Document Revision, Chunk and source-range schemas;
4. Index and Index Revision schemas;
5. ingestion/sync/deletion/reconciliation Activity types;
6. Query, Result, Result Set and Citation schemas;
7. permission/freshness/retention/tombstone rules;
8. Dataset, Table, Schema, Query, Transformation and lineage schemas;
9. Package, Package Release, Installed Plugin and Activation schemas;
10. plugin manifest, family, runtime, permission and resource schemas;
11. registry/alias/tag-to-release resolution;
12. install/health/upgrade/migration/rollback/removal schemas;
13. MCP adapter mappings;
14. model/data-provider adapter contract;
15. search/data/plugin telemetry and proof conventions;
16. conformance and migration corpus.

---

# Required validation

1. Ingest multiple source formats and retain exact source, parser, chunker and Index Revision identity.
2. Re-ingest unchanged content without identity drift or duplication.
3. Re-index changed parser/embedding versions without overwriting old revisions.
4. Return exact permitted source revision/range Citations.
5. Revoke/delete a source and prove it disappears from future results across partially failing backends.
6. Degrade from hosted hybrid search to local lexical/SQL search with honest capability labels.
7. Replace LlamaIndex or RAGFlow without changing Knowledge Source, Document, Query or Citation identity.
8. Run the same metadata filters across backends and reject semantic divergence.
9. Execute one transformation through Polars and DuckDB and compare schemas/results/lineage.
10. Restrict UDF, extension, write and network behavior behind separate permissions.
11. Discover, inspect and resolve a plugin alias to an immutable signed Package Release.
12. Install and activate content-only, Deno, MCP and OCI plugin classes with visibly different permissions.
13. Pin a release and reject automatic/forced upgrade.
14. Stage an incompatible upgrade, fail health/conformance and roll back.
15. Quarantine a release while retaining evidence and dependent-state visibility.
16. Remove a plugin with explicit data retention, credential revocation and orphan cleanup.
17. Map an MCP Tool call to a Ptah Activity without using MCP IDs as canonical identity.
18. Run Hunter or Hermes as a caller and prove their memory/reasoning remains outside Ptah Core.
19. Replace a provider/registry/runtime without changing Ptah identities.
20. Retain negative, stale, partial and failed evidence instead of flattening it into PASS.

## Final decision

WP10 is closed for **Phase 0B contract design**, not implementation.

No runtime, Knowledge Facility, search index, data engine, plugin manager, registry, MCP server or UI implementation is approved by this ADR alone.
