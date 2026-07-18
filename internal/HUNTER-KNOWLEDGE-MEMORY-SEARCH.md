# Internal Recovery Record — Hunter Knowledge, Memory and Search

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — WORKING FOUNDATIONS, MAJOR INDEX/CATALOGUE COMPLETION REQUIRED  
**Inspected:** 2026-07-18

## Identity

- Repository: `jaydumisuni/hunter`
- Visibility: Private
- Default branch: `master`
- Pinned source revision: `df0bd758a2f08e5d861628be3146aeecdb9677d6`
- Licence: no root public licence recovered; preserve internal/private status
- Ptah relevance: knowledge approval, chat/knowledge/memory separation, local/online sync, retrieval fallback, source-context restrictions, provider abstraction and memory-promotion rules

## Files/components inspected

- `README.md`
- `docs/HUNTER_KNOWLEDGE_INTAKE_V1.md`
- `docs/HUNTER_MEMORY_SEPARATION_V1.md`
- `hunter_core/knowledge_intake/__init__.py`
- `hunter_core/learning/approved_learning.py`
- `hunter_core/memory/__init__.py`
- `hunter_core/memory/store_types.py`
- `hunter_core/memory/context_builder.py`
- `hunter_core/memory/online_memory.py`
- `hunter_core/sync/sync_state.py`
- `hunter_provider_adapter.py`
- `scripts/sync_knowledge_online.py`
- `scripts/test_hunter_memory_retrieval.py`
- `cloudflare/hunter-memory-worker/src/index.ts`
- `cloudflare/hunter-memory-worker/schema.sql`
- relevant commit evidence for approved learning, retrieval, sync, provider selection and validation wiring

## Verified implemented behavior

### Store separation

- `chat`, `knowledge` and `memory` are distinct store types.
- Stored records have UUID identity, title, body, source, confidence, proof status, approval status, tags and creation time.
- Knowledge can promote to memory only after successful proof and approved/not-required approval state.
- The documented rule explicitly prevents knowledge or chat from automatically becoming durable memory.

### Knowledge intake direction

- The documented intake flow separates safety checks, classification, extraction, structured chunks, raw source, index metadata, retrieval and approved lesson promotion.
- Planned chunk boundaries include Markdown headings, code structures, log blocks and later PDF/image regions.
- The intake rules prohibit executing uploaded files, indexing secrets and treating unknown binaries as knowledge.
- The current `hunter_core/knowledge_intake` package is only a marker; general classifiers and chunk builders are not implemented there yet.

### Approved learning

- Only owner/admin roles may create approved saved lessons.
- Lessons are normalized Markdown files under `knowledge/approved`.
- Each lesson retains title, source, approving role, approval time, tags and body.
- A local JSONL sync event is appended after save.
- Local save succeeds even when online sync is unavailable; online sync status is returned separately.
- Sync credentials are loaded from local environment/config and remain outside tracked content.

### Sync and online storage

- Approved knowledge is collected from explicit allowed patterns.
- Content is normalized and SHA-256 hashed before upload.
- Sync payloads retain path, name, hash, byte count, approval flag and content.
- The online worker uses D1-backed `hunter_knowledge` and sync-event tables.
- Sync requests require a bearer key.
- Knowledge rows are keyed by normalized path and carry source, content, hash, approval, updated and synced times.
- Health, sync, list, search and context routes are separate.
- Separate sync-state helpers retain pending, synced, partial and failed states, and require proof before marking a sync successful.

### Retrieval and context

- Local search is a bounded term-overlap scan of approved Markdown files.
- Online retrieval is a separate HTTP search call.
- Local and online results are combined into context blocks.
- Online retrieval failure adds a warning while local results remain usable.
- Public website-assistant mode does not retrieve or save privileged admin memory.
- Unknown source modes default to no memory-save or internal-tool authority.
- The online worker currently scores terms over at most the latest 250 stored rows and returns bounded previews.
- A smoke script checks local/online retrieval and fails when no answer context is produced.

### Provider abstraction

- Hunter selects between Ollama/local and Cloudflare provider paths through an adapter.
- `auto` and `online_fallback` modes are explicit.
- Health reporting exposes provider, transport, status, model list, secret requirements, gateway use and missing configuration.
- Provider selection is useful adapter evidence but remains Hunter reasoning/runtime behavior, not a Ptah Core responsibility.

## Strong internal patterns for Ptah

1. Conversation, source knowledge, derived indexes and durable memory are different truth classes.
2. Knowledge promotion requires proof and approval rather than automatic conversation capture.
3. Local-first approved knowledge survives optional online-sync failure.
4. Sync uses normalized content hashes and explicit source/path metadata.
5. Local and online retrieval degrade independently.
6. Public/customer contexts have different knowledge permissions from owner/admin contexts.
7. Credentials remain local references rather than knowledge content.
8. Sync and retrieval are explicit operations, not hidden effects of rendering a chat.
9. Source, confidence, proof and approval belong in knowledge records.
10. Sync success requires evidence rather than an optimistic request result.
11. Model/provider selection can remain behind a small health-reporting adapter.
12. Human-readable approved source and a replaceable shared index can coexist.

## Important limitations

- Approved lessons are Markdown files rather than a universal Object/Corpus/Document model.
- Path is the online primary key; rename/move semantics and immutable source identity are weak.
- The sync event queue is append-only JSONL without a fully recovered durable acknowledgement/retry processor.
- Local search is simple token-presence scoring with no phrase, field, semantic, freshness or permission-aware ranking.
- Online search scans a bounded recent row set and is not a versioned multi-index contract.
- Context assembly truncates previews and does not retain exact citation ranges.
- Full document content is uploaded per record; large-corpus chunk streaming is not established.
- Deletion, tombstones, retention, re-indexing, stale-source detection and conflict handling are incomplete.
- The D1 schema is deployment-specific and cannot become mandatory Ptah storage.
- Approval is role-string based and not a generic caller-policy/receipt reference.
- There is no embedding model/version, chunker/parser/version or Index Revision record.
- Public versus private behavior is hard-coded around Hunter product source names.
- Search/list routes in the inspected worker do not themselves show caller authentication, while cross-origin response headers are broad; deployment controls require separate verification.
- The retrieval test is a useful smoke check, not proof of ranking quality, deletion correctness, permission isolation or source-range citations.
- Hunter knowledge, memory and provider behavior is private consumer logic; Ptah must not absorb Hunter's identity or reasoning policy.

## What Ptah should reuse or adapt

- separate Conversation, Knowledge Source, derived Index and durable Lesson/Memory classes;
- proof/approval gates before durable promotion;
- local-first source plus optional shared index;
- content hashes and explicit source metadata;
- independent local/remote retrieval with degradation warnings;
- permission-aware public/private retrieval boundaries;
- human-readable approved source documents;
- sync as an explicit receipted Activity;
- confidence, proof and approval metadata;
- proof-required sync completion;
- credential-reference separation;
- provider health/capability adapters where Ptah Facilities need external model or data services.

## What Ptah must not inherit

- Hunter identity, roles, personal memory or reasoning policy in public Ptah;
- path as canonical Document identity;
- a Markdown folder as the universal knowledge store;
- D1 as the mandatory public index/catalogue backend;
- simple keyword scanning as the final search architecture;
- automatic chat-to-memory promotion;
- role strings as universal approval authority;
- context snippets without exact source/citation references;
- full-corpus sync as one coarse unversioned operation;
- website-assistant product rules as generic knowledge policy;
- Hunter's model-selection policy as Ptah's reasoning layer;
- a sync HTTP success treated as proof of durable searchable reconciliation.

## Classification

**ADAPT STORE SEPARATION, APPROVAL, LOCAL-FIRST SYNC, HASHING, DEGRADED RETRIEVAL AND PROVIDER-ADAPTER PATTERNS; BUILD PTAH-NATIVE KNOWLEDGE/INDEX CONTRACTS.**

Hunter remains a private caller/consumer. Ptah supplies neutral knowledge, data and search Facilities without owning Hunter memory, learning or reasoning policy.

## Native Ptah completion required

- Knowledge Source, Corpus, Document, Chunk and Index identities;
- immutable Object/View references and source revisions;
- parser, chunker, embedding, reranker and index versions;
- source and query permission/audience scopes;
- freshness, deletion, tombstone and retention semantics;
- local/shared index location records;
- lexical, semantic, metadata and hybrid query contracts;
- exact citation ranges and retained source captures;
- Query, Result, ranking explanation and evaluation records;
- sync cursor, attempt, acknowledgement and conflict handling;
- model/provider-neutral embedding and reranking adapters;
- search across Objects, Activities, Artifacts and Workspaces;
- backend replacement and re-index migration;
- retrieval-quality, stale-data, privacy and negative-result proof.

## Validation inherited into Ptah

1. Preserve conversation, source knowledge, derived index and promoted memory as separate records.
2. Refuse durable promotion without required proof/approval.
3. Save local approved knowledge during online outage and reconcile later without duplication.
4. Rename or move a source without losing Document identity or citations.
5. Delete or revoke a source and remove it from future search while retaining receipted history.
6. Return exact source revision and range with every grounded result.
7. Degrade from shared semantic search to local lexical search without claiming equivalent ranking.
8. Rebuild an index with a new parser, chunker or embedding version while preserving the old revision.
9. Keep private/Hunter knowledge unavailable to public Workspaces.
10. Replace D1 or the search backend without changing Knowledge Source or Document identity.
11. Reject a forged role string when caller policy/identity does not authorize promotion.
12. Prove successful sync through target read-back or equivalent searchable evidence.
13. Swap a model/data provider without changing Ptah Query, Result or source identity.
