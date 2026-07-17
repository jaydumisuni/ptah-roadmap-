# Donor Record — RAGFlow

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — END-TO-END DOCUMENT INGESTION AND HYBRID-RETRIEVAL DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/infiniflow/ragflow
- Default branch: `main`
- Pinned commit: `1c0432a81644cd89a670ab3d32b2bd2d8f3b2b92`
- Licence: Apache-2.0
- Activity: Active
- Classification: self-hosted document ingestion, parsing, indexing, retrieval and citation platform donor
- Ptah targets: `SEARCH-001`, Corpus/Document ingestion, parsing progress, hybrid retrieval, metadata filtering, citations and source-grounded knowledge operations

## Files/components inspected

- `README.md`
- `LICENSE`
- `api/db/services/document_service.py`
- `rag/nlp/search.py`
- documented DeepDoc, task queue, document engine, API, MCP and agent/workflow boundaries

## Verified capabilities and patterns

- Ingests many document/data formats through a visible parsing pipeline.
- Keeps Knowledgebase/Dataset, Document, File, Task and metadata records separately.
- Document records expose parser/pipeline configuration, source type, size, token/chunk counts, progress, message, status and timing.
- Parsing progress and failure states are queryable rather than hidden.
- Metadata fields can be attached to documents and used for filtering/aggregation.
- Retrieval supports lexical full-text and dense vector matching.
- Hybrid retrieval combines text and vector signals and can rerank/filter results.
- Search results retain document IDs, chunk IDs, positions/pages, highlights, keywords and metadata fields.
- Citation insertion compares answer segments with retrieved chunk text/vector evidence.
- Deleted-document safety filtering exists to prevent stale chunks from surfacing when backend cleanup is incomplete.
- Supports several document-store/vector backends through an abstraction.
- Provides APIs and MCP compatibility in addition to the product UI.
- The project includes multi-tenant/user/knowledgebase concepts and a full operational deployment.

## What RAGFlow completes

- A mature end-to-end ingestion and retrieval workflow rather than only an index library.
- Visible document parsing states, progress and errors.
- Hybrid lexical/vector retrieval with metadata filtering.
- Page/chunk/source positioning useful for citations.
- A practical reference for large-corpus operations, task queues and reprocessing.
- Source-grounded citation and stale-index cleanup lessons.
- A self-hosted path independent of one hosted RAG provider.

## Important limitations for Ptah

- RAGFlow is a full application/platform, not Ptah's canonical Knowledge Source, Object, Activity or permission model.
- Its Knowledgebase, Document and chunk IDs are product-local.
- The default deployment is operationally heavy and typically includes SQL, Redis, Object Storage and a search/vector engine.
- Document-store/index backends can leave stale chunks, as shown by defensive pruning logic.
- A retrieved chunk or inserted citation does not prove the generated claim is correct.
- Citation insertion based on text/vector similarity is not the same as an exact source-range citation.
- Parser, chunker, embedding, reranker and index versions must be retained explicitly by Ptah.
- Product agent/workflow/model-provider features are outside Ptah Core.
- Multi-tenant product roles do not replace Ptah Workspace/Object permissions.
- Full deployment requirements may be excessive for the first Ptah vertical slice.
- Indexes and embeddings are derived state and must remain rebuildable.
- Deletion from metadata and deletion from search/vector stores can diverge.

## Must not be inherited

- RAGFlow Knowledgebase/Document/chunk IDs as canonical Ptah identities;
- one search/vector backend made mandatory;
- the full RAGFlow application used as Ptah Core;
- product agent/workflow/reasoning identity embedded into Ptah;
- citation similarity promoted to exact proof;
- index presence treated as source availability;
- stale-chunk filtering used as a substitute for correct deletion/reconciliation;
- parser/chunker/embedding changes applied without a new Index Revision;
- broad product permissions replacing Ptah source/Workspace access control;
- heavy deployment made mandatory for local one-Node Ptah.

## Integration decision

**ADAPT RAGFLOW AS THE PRIMARY END-TO-END INGESTION/RETRIEVAL PLATFORM DONOR AND OPTIONAL HOSTED FACILITY, NOT THE CANONICAL KNOWLEDGE MODEL.**

Recommended use:

1. study or wrap selected parsing/task/retrieval APIs;
2. optionally host RAGFlow as a Knowledge Facility for large deployments;
3. map RAGFlow datasets/documents/chunks/indexes to stable Ptah Source/Corpus/Document/Chunk/Index Revision records;
4. keep source Objects, permissions, citations and deletion authority in Ptah;
5. support a lighter native/LlamaIndex path for local and first-slice deployments.

## Native Ptah gap

Ptah must define:

- Knowledge Source, Corpus, Document, Chunk and Index Revision identities;
- source Object/View/revision relationships;
- parser/chunker/embedding/reranker/model versions;
- ingestion Activity and progress/attempt receipts;
- permissions and audience filters enforced before retrieval;
- exact page/range/segment citation records;
- lexical/vector/hybrid query and ranking explanations;
- stale-index, deletion, tombstone and reconciliation states;
- local/shared index locations and replication;
- backend-neutral result and citation schemas;
- partial-corpus/degraded-search behavior;
- replacement/reindex migration tests.

## Exit strategy

Ptah's knowledge contracts remain implementable through RAGFlow, LlamaIndex, native lexical/vector indexes, database search or other engines. RAGFlow IDs and schemas remain adapter metadata.

## Validation required

1. Ingest several document formats and retain parser/chunker/index version plus progress/error receipts.
2. Run lexical, vector and hybrid retrieval and expose the ranking components.
3. Return exact source Document revision and page/range for every result/citation.
4. Delete/revoke a source and prove stale chunks cannot surface.
5. Re-index with a changed parser/embedding model as a new Index Revision.
6. Enforce Workspace/source permissions before retrieval.
7. Continue local/lightweight search when the RAGFlow service is unavailable and label reduced capability.
8. Replace RAGFlow for one Corpus without changing Ptah Source/Document identity.
