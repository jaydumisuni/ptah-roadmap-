# Donor Record — RAGFlow

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PRIMARY END-TO-END DOCUMENT INGESTION AND HYBRID-RETRIEVAL DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/infiniflow/ragflow
- Default branch: `main`
- Pinned commit: `b7a3a2760f46dbdff1e0cce307bfb874944244b4`
- Stable release observed in project instructions: `v0.26.4`
- Licence: Apache-2.0
- Activity: Active
- Classification: self-hosted document ingestion, parsing, indexing, retrieval, metadata and citation platform donor
- Ptah targets: `SEARCH-001`, Corpus/Document ingestion, parsing progress, hybrid retrieval, metadata filtering, citations, derived indexes and source-grounded knowledge operations

## Files/components inspected

- `README.md`
- `LICENSE`
- `api/db/services/knowledgebase_service.py`
- `api/db/services/document_service.py`
- `api/apps/services/dataset_api_service.py`
- `agent/tools/retrieval.py`
- `rag/svr/task_executor_refactor/dataflow_service.py`
- `common/doc_store/doc_store_base.py`
- `common/metadata_infinity_filter.py`
- metadata-filter regression test and pinned commit evidence
- documented DeepDoc, task queue, document engine, API, MCP and agent/workflow boundaries

## Verified capabilities and patterns

### Dataset and permission model

- Keeps Knowledgebase/Dataset, Document, File, Task, metadata and pipeline records separately.
- Dataset visibility distinguishes team-visible datasets from user-owned datasets and filters invalid records.
- Dataset deletion checks tenant ownership before operating.
- Dataset records retain language, permission, document/token/chunk counts, parser, embedding model, pipeline and advanced-index task state.
- Cross-dataset retrieval validates embedding-model compatibility rather than silently mixing incompatible vector spaces.

### Document ingestion and operational state

- Document records expose parser/pipeline configuration, source type, size, token/chunk counts, progress, progress message, run state, status and timing.
- Parsing states include unstarted, running, cancelled, done and failed, with aggregate counts available per dataset.
- A dataset can reject chat/retrieval use while documents remain unparsed or failed.
- Dataflow execution loads a pipeline DSL, normalizes several output forms, embeds chunks when needed, processes metadata, inserts chunks, updates progress and records operation details.
- Pipeline output can be chunks, JSON, Markdown, text or HTML before normalization.
- Chunk records receive document/dataset references, creation time, tokenized fields and generated IDs before indexing.
- Billing or quota hooks are outside the pipeline core through an optional interface.

### Retrieval

- Retrieval parameters include similarity threshold, keyword/vector weighting, top-N/top-K limits, selected datasets, optional memory sources, reranker, metadata filters, language transforms, table-of-contents enhancement and knowledge-graph retrieval.
- Retrieval can combine lexical and dense-vector signals and apply reranking.
- Manual and model-assisted metadata filters are supported.
- Retrieved chunks can be enriched through child relationships, table-of-contents retrieval or knowledge-graph results.
- Internal vector/token fields are removed before final result output.
- Retrieved chunks and document aggregations are attached as references for downstream citation/prompt use.
- Retrieval and memory are separate source modes in the inspected tool.

### Search backend abstraction

- `DocStoreConnection` defines backend-neutral health, index creation/deletion/existence, search, get, bulk insert, update, delete, aggregation, highlight and SQL operations.
- Match expressions distinguish lexical text, dense vectors, sparse vectors, tensors and fusion.
- Multiple search/document-store backends can implement the same abstract interface.
- The current project still has backend-specific semantic hazards; abstractions do not guarantee identical query meaning automatically.

### Deletion and reconciliation lessons

- Dataset deletion removes documents, linked files and file-to-document records, attempts to drop the dataset index and then removes the dataset record.
- Partial cleanup errors are retained and returned instead of always reporting complete success.
- Missing link rows are treated as stale/partial data and logged while deletion continues.
- Metadata/database deletion and search-index deletion are separate operations and can diverge.
- A current regression fix explicitly disables unsafe metadata-filter push-down when an Infinity backend cannot reproduce the in-memory semantics of multi-valued negative operators.
- The regression test checks Elasticsearch and Infinity backends against the same fallback semantics.

## What RAGFlow completes

- A mature end-to-end ingestion and retrieval workflow rather than only an index library.
- Visible document parsing states, progress and errors.
- Configurable ingestion pipelines with normalization, metadata, embedding and indexing stages.
- Hybrid lexical/vector retrieval with metadata filtering and optional reranking.
- Page/chunk/source positioning and downstream reference production useful for citations.
- A practical reference for large-corpus operations, task queues, reprocessing and multiple index backends.
- Explicit deletion/error handling that exposes stale or partial cleanup risks.
- A self-hosted path independent of one hosted RAG provider.
- Useful tests for preserving semantic equivalence when query filters are pushed into different backends.

## Important limitations for Ptah

- RAGFlow is a full application/platform, not Ptah's canonical Knowledge Source, Object, Activity or permission model.
- Its Knowledgebase, Document, Task and chunk IDs are product-local.
- The default deployment is operationally heavy and typically includes SQL, Redis, Object Storage and a search/vector engine.
- Current project instructions require substantial local resources and x86-focused prebuilt images.
- A retrieved chunk or inserted citation does not prove the generated claim is correct.
- Similarity/reference insertion is not automatically an exact immutable source-range citation.
- Parser, chunker, embedding, reranker and index versions must be retained explicitly by Ptah.
- Product agent, memory, workflow and model-provider features are outside Ptah Core.
- Multi-tenant product roles do not replace Ptah Workspace/Object/source permissions.
- Full deployment requirements may be excessive for the first Ptah vertical slice.
- Indexes and embeddings are derived state and must remain rebuildable.
- Deletion from metadata, files and search/vector stores is multi-step and can partially fail.
- Backend adapters may implement subtly different filter semantics unless conformance tests guard them.
- Dataset-level compatibility checks do not provide Ptah's complete source-revision, freshness, tombstone or citation model.
- RAGFlow's references remain adapter results until bound to immutable Ptah Object/View revisions.

## Must not be inherited

- RAGFlow Knowledgebase, Document, Task or chunk IDs as canonical Ptah identities;
- one search/vector backend made mandatory;
- the full RAGFlow application used as Ptah Core;
- product agent, workflow, memory or reasoning identity embedded into Ptah;
- citation similarity promoted to exact proof;
- index presence treated as source availability;
- stale-chunk filtering used as a substitute for correct deletion/reconciliation;
- parser, chunker, embedding or reranker changes applied without a new Index Revision;
- broad product permissions replacing Ptah source/Workspace access control;
- heavy deployment made mandatory for local one-Node Ptah;
- backend push-down accepted without semantic conformance proof;
- partial dataset deletion reported as complete source revocation.

## Integration decision

**ADAPT RAGFLOW AS THE PRIMARY END-TO-END INGESTION/RETRIEVAL PLATFORM DONOR AND OPTIONAL HOSTED KNOWLEDGE FACILITY, NOT THE CANONICAL KNOWLEDGE MODEL.**

Recommended use:

1. study or wrap selected ingestion, task, metadata and retrieval APIs;
2. optionally host RAGFlow as a Knowledge Facility for larger deployments;
3. map RAGFlow datasets, documents, tasks, chunks and indexes to stable Ptah Source, Corpus, Document, Activity, Chunk and Index Revision records;
4. keep source Objects, permissions, citations, deletion and freshness authority in Ptah;
5. use Ptah Activities and Receipts to represent ingestion, re-indexing and deletion attempts;
6. require backend conformance tests for lexical, vector, metadata and deletion semantics;
7. support a lighter native/LlamaIndex path for local and first-slice deployments;
8. keep RAGFlow replaceable behind provider-neutral Query and Result contracts.

## Licence decision

Apache-2.0 is compatible with architecture study, wrapping and selective adaptation subject to retaining notices and reviewing transitive dependencies and separately licensed components before distribution.

## Native Ptah gap

Ptah must define:

- Knowledge Source, Corpus, Document, Chunk and Index Revision identities;
- source Object/View/revision relationships;
- parser, chunker, embedding, reranker and index versions;
- ingestion, parse, embed, index, re-index and deletion Activities with attempt receipts;
- permissions and audience filters enforced before retrieval;
- exact page, range, region and segment citation records;
- lexical, vector, metadata and hybrid Query contracts;
- ranking components, explanations and evaluation evidence;
- stale-index, deletion, tombstone and reconciliation states;
- local/shared index locations and replication;
- backend-neutral Result and Citation schemas;
- partial-corpus and degraded-search behavior;
- source freshness and connector cursor records;
- provider conformance and replacement/re-index migration tests.

## Exit strategy

Ptah's knowledge contracts remain implementable through RAGFlow, LlamaIndex, native lexical/vector indexes, database search or other engines. RAGFlow IDs and schemas remain adapter metadata, and every derived index remains reproducible from retained source Objects and Index Revision recipes.

## Validation required

1. Ingest several document formats and retain parser, chunker and Index Revision plus progress/error receipts.
2. Run lexical, vector, metadata and hybrid retrieval and expose the ranking components.
3. Return exact source Document revision and page/range for every Result and Citation.
4. Delete or revoke a source and prove stale chunks cannot surface after partial backend failure.
5. Re-index with a changed parser or embedding model as a new Index Revision.
6. Enforce Workspace/source permissions before retrieval and before reference rendering.
7. Continue local/lightweight search when the RAGFlow service is unavailable and label reduced capability.
8. Replace RAGFlow for one Corpus without changing Ptah Source or Document identity.
9. Run the same metadata-filter corpus against each backend and reject semantically divergent push-down.
10. Interrupt ingestion between database, object-store and index writes and reconcile from receipted source truth.
11. Preserve negative results and partial deletion evidence rather than flattening them into success.
12. Rebuild every RAGFlow-derived index from Ptah source Objects without losing citation lineage.
