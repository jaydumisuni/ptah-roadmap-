# Internal Recovery Record — Hunter Knowledge, Memory and Search

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — WORKING FOUNDATIONS, MAJOR INDEX/CATALOGUE COMPLETION REQUIRED  
**Inspected:** 2026-07-18

## Identity

- Repository: `jaydumisuni/hunter`
- Visibility: Private
- Branch: `master`
- Pinned source revision: `68bc23c15623e8e7cc05f8be8c9bc1fe51af15c4`
- Licence: no root public licence recovered; preserve internal/private status
- Ptah relevance: knowledge approval, local/online sync, store separation, retrieval fallback, public/private source restrictions and memory-promotion rules

## Files/components inspected

- `hunter_core/learning/approved_learning.py`
- `scripts/sync_knowledge_online.py`
- `hunter_core/memory/store_types.py`
- `hunter_core/memory/context_builder.py`
- `hunter_core/memory/online_memory.py`
- online memory-worker schema and sync/search commit evidence
- Hunter README and existing runtime/storage records

## Verified implemented behavior

### Store separation

- `chat`, `knowledge` and `memory` are distinct store types.
- Stored records have stable UUIDs, title, body, source, confidence, proof status, approval status, tags and creation time.
- Knowledge can promote to memory only after successful proof and approved/not-required approval state.

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

### Retrieval and context

- Local search is a simple term-overlap scan of approved Markdown files.
- Online retrieval is a separate HTTP search call.
- Local and online results are combined into context blocks.
- Online retrieval failure adds a warning while local results remain usable.
- Public website-assistant mode does not retrieve/save privileged admin memory.
- Query length and result limits are bounded.

## Strong internal patterns for Ptah

1. Chat, knowledge and durable memory are different truth classes.
2. Knowledge promotion requires proof and approval rather than automatic conversation capture.
3. Local-first approved knowledge survives optional online-sync failure.
4. Sync uses normalized content hashes and explicit source/path metadata.
5. Local and online retrieval degrade independently.
6. Public/customer contexts have different memory permissions from owner/admin contexts.
7. Credentials remain local references rather than knowledge content.
8. Sync and retrieval are explicit operations, not hidden effects of rendering a chat.
9. Source, confidence, proof and approval belong in knowledge records.
10. Large online storage and local human-readable source can coexist.

## Important limitations

- Approved lessons are Markdown files rather than a universal Object/Corpus/Document model.
- Path is the online primary key; rename/move semantics and immutable source identity are weak.
- The sync event queue is append-only JSONL without durable acknowledgement/update processing in the inspected local implementation.
- Local search is simple token-presence scoring with no phrase, field, semantic, freshness or permission-aware ranking.
- Online search is HTTP keyword retrieval rather than a versioned multi-index contract.
- Context assembly truncates previews and does not retain exact citation ranges.
- Full document content is uploaded in one payload; large-corpus/chunk/stream behavior is not established.
- Deletion, tombstones, retention, re-indexing, stale-source detection and conflict handling are incomplete.
- D1 schema is deployment-specific and cannot become mandatory Ptah storage.
- Approval is role-string based and not a generic caller-policy/receipt reference.
- There is no embedding model/version, chunker/parser/version or index-revision record.
- Public versus private behavior is hard-coded around Hunter product source names.
- `knowledge`, `memory` and chat records are Hunter-specific; Ptah must not absorb Hunter's personal reasoning/memory identity.

## What Ptah should reuse or adapt

- separate Source/Knowledge/Memory/Conversation classes;
- proof/approval gate before durable promotion;
- local-first source plus optional shared index;
- content hashes and explicit source metadata;
- independent local/remote retrieval with degradation warnings;
- permission-aware public/private retrieval boundaries;
- human-readable approved source documents;
- sync as an explicit receipted Activity;
- confidence, proof and approval metadata;
- credential-reference separation.

## What Ptah must not inherit

- Hunter identity, roles, personal memory or reasoning policy in public Ptah;
- path as canonical Document identity;
- Markdown folder as the universal knowledge store;
- D1 as mandatory public index/catalogue backend;
- simple keyword scan as final search architecture;
- automatic chat-to-memory promotion;
- role strings as universal approval authority;
- context snippets without exact source/citation references;
- full-corpus sync as one coarse unversioned operation;
- website-assistant product rules as generic knowledge policy.

## Classification

**ADAPT STORE SEPARATION, APPROVAL, LOCAL-FIRST SYNC, HASHING AND DEGRADATION PATTERNS; BUILD PTAH-NATIVE KNOWLEDGE/INDEX CONTRACTS.**

Hunter remains a private caller/consumer. Ptah supplies neutral knowledge and search Facilities without owning Hunter memory or learning policy.

## Native Ptah completion required

- Knowledge Source, Corpus, Document, Chunk and Index identities;
- immutable Object/View references and source revisions;
- parser/chunker/embedding/index versions;
- permissions and audience scopes;
- freshness, deletion, tombstone and retention semantics;
- local/shared index location records;
- lexical, semantic, metadata and hybrid query contracts;
- exact citation ranges and source captures;
- query/result/ranking explanation records;
- sync cursor, attempt, acknowledgement and conflict handling;
- model/provider-neutral embedding and reranking adapters;
- search across Objects, Activities, Artifacts and Workspaces;
- backend replacement and re-index migration.

## Validation inherited into Ptah

1. Preserve chat, source knowledge, derived index and promoted memory as separate records.
2. Refuse durable promotion without required proof/approval.
3. Save local approved knowledge during online outage and reconcile later without duplication.
4. Rename/move a source without losing Document identity or citations.
5. Delete/revoke a source and remove it from future search while retaining receipted history.
6. Return exact source revision/range with every grounded result.
7. Degrade from shared semantic search to local lexical search without claiming equivalent ranking.
8. Rebuild an index with a new parser/chunker/embedding version while preserving the old revision.
9. Keep private/Hunter knowledge unavailable to public Workspaces.
10. Replace D1 or the search backend without changing Knowledge Source/Document identity.
