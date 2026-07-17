# Donor Record — LlamaIndex

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — MODULAR DATA CONNECTOR, NODE, INGESTION AND QUERY DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/run-llama/llama_index
- Default branch: `main`
- Pinned commit: `dbdaf89dc66a6469081c9f8fddc9c1bf6c43d8a2`
- Licence: MIT
- Activity: Active
- Classification: modular data-framework, connector, ingestion-pipeline, index/retriever and integration donor
- Ptah targets: `SEARCH-001`, source connectors, Document/Node relationships, transformation pipelines, deduplication/upsert/delete strategies, vector-store abstraction and provider-neutral retrieval

## Files/components inspected

- `README.md`
- `LICENSE`
- `llama-index-core/llama_index/core/schema.py`
- `llama-index-core/llama_index/core/ingestion/pipeline.py`
- core versus integration-package architecture
- documented reader, parser, index, retriever, workflow and vector-store boundaries

## Verified capabilities and patterns

- Separates `llama-index-core` from more than three hundred optional integration packages.
- Uses connectors/readers for APIs, files, databases and other data sources.
- Models retrievable Nodes with UUIDs, hashes, embeddings, metadata and explicit SOURCE/PREVIOUS/NEXT/PARENT/CHILD relationships.
- Distinguishes text, image, multimodal, Document and Index object classes.
- Metadata can be included differently for embedding and LLM/context use.
- Transform components have synchronous and asynchronous interfaces.
- Ingestion pipelines compose readers, transformations, parsers, embeddings, caches, document stores and vector stores.
- Transformation cache keys combine node content and serialized transformation configuration.
- Pipelines support persisted cache/docstore state.
- Document-store strategies include upsert, duplicate-only handling and upsert-with-delete.
- Transformations can execute in worker processes.
- Vector-store and document-store interfaces are replaceable.
- The framework can be installed minimally or with selected provider integrations.

## What LlamaIndex completes

- A modular, lighter-weight alternative to a full RAG platform.
- Connector and integration patterns Ptah should not recreate individually.
- Explicit source/parent/child/sequence relationships for chunks and derived Nodes.
- Transformation pipelines with configuration-aware caches.
- Upsert/dedup/delete strategies and replaceable stores.
- Provider-neutral abstractions for embeddings, vector stores, LLMs and retrievers.
- A practical local/one-Node path and a foundation for custom Ptah Knowledge Facilities.

## Important limitations for Ptah

- LlamaIndex Nodes/Documents/Indexes are library-local objects, not canonical Ptah Objects or Knowledge identities.
- Its framework is oriented toward LLM/agent applications; Ptah does not own reasoning or answer generation.
- Node UUIDs can be regenerated unless explicitly mapped to stable source/revision/chunk identities.
- Transformation hashing includes serialized content/configuration but does not automatically capture every external binary/model/environment dependency.
- Pickle and broad Python integration ecosystems add trust and compatibility risk.
- Hundreds of optional connectors/integrations vary in licence, maintenance and security quality.
- Vector-store deletion/upsert semantics vary by backend.
- Metadata filtering and permissions must be enforced by Ptah before retrieval.
- A cached transformation output is derived state, not source truth or independent proof.
- LlamaParse/LlamaCloud are optional commercial platforms and cannot be mandatory.
- Node relationship vocabulary is useful but not broad enough for all Ptah Object/Artifact relationships.
- Framework query results do not automatically provide exact source-range citations or proof.

## Must not be inherited

- LlamaIndex Node, Document or Index IDs as canonical Ptah identities;
- the agent/workflow/LLM layer used as Ptah reasoning;
- every integration package installed by default;
- pickle or untrusted Python objects accepted as portable trusted state;
- hosted LlamaCloud dependencies made mandatory;
- transformation cache hits treated as verified source-grounded output;
- provider-specific metadata or vector-store schemas exposed as Ptah contracts;
- deletion/upsert behavior assumed consistent across all stores;
- metadata included in prompts/embeddings without privacy classification.

## Integration decision

**ADAPT LLAMAINDEX CORE AS THE PRIMARY MODULAR CONNECTOR/INGESTION/RETRIEVAL DONOR AND LIKELY FIRST NATIVE KNOWLEDGE-FACILITY FOUNDATION.**

Recommended role:

1. selected readers/connectors ingest approved Ptah Source Objects;
2. Ptah assigns stable Source/Document/Chunk/Index Revision identities;
3. LlamaIndex transformations/parsers/embeddings operate as versioned Activities;
4. derived Nodes map back to exact Ptah Object/View revisions;
5. optional vector/document stores remain backend adapters;
6. RAGFlow remains an optional heavier platform backend;
7. agent/query-engine output stays external to Ptah truth.

## Native Ptah gap

Ptah must define:

- stable Source/Corpus/Document/Chunk/Index Revision identity;
- deterministic chunk identity from source revision, parser and position;
- connector/read permission and credential references;
- parser, transformation, embedding and reranker provenance;
- transformation cache identity including external model/tool versions;
- lexical/vector/hybrid query contracts;
- permissions and audience filtering before retrieval;
- exact citation ranges and source snapshots;
- deletion, tombstone, freshness and re-index state;
- integration package manifest, licence, trust and health;
- safe serialization rather than arbitrary trusted pickle;
- backend migration and cross-index comparison.

## Exit strategy

Ptah's knowledge contracts remain independent of LlamaIndex. Native pipelines, RAGFlow, database search or other frameworks can implement them without changing Source, Document, Chunk or Query identity.

## Validation required

1. Ingest one source through two parser/chunker versions and retain separate Index Revisions.
2. Preserve stable source/chunk identity across a no-change re-ingestion.
3. Upsert a changed source, delete a removed source and verify all backend stores reconcile.
4. Run transformations with cache and prove model/tool/config changes invalidate affected outputs.
5. Enforce source permissions before vector/lexical retrieval.
6. Return exact Object/View/source-range citations from retrieved Nodes.
7. Load only approved connector/integration packages with pinned licences and versions.
8. Replace the vector/document store or LlamaIndex itself without changing Ptah identities.
