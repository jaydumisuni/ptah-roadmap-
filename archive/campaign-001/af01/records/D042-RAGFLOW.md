# D042 — RAGFlow Archive Record

Outcome: ACCEPTED FOR ARCHIVE — knowledge/RAG application donor; no canonical-knowledge or runtime-authorization claim

Campaign: `CAMPAIGN-001`

Formation: `AF01`

Primary Archivist: `AF01-P07`

Independent Verifier: `AF01-V07`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `infiniflow/ragflow`;
- owner: InfiniFlow organization;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `6a85d1c5c4f96933cd91214a080460baa9252976`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`;
- model/provider, parser, document, image, plugin and transitive-service rights require separate review;
- activity state: active; inspected head replaces a provider SDK to unblock a PyJWT vulnerability fix.

## Primary evidence packet — AF01-P07

Inspected:

- `README.md` blob `fcc4101200ca56a1d457900519fc7d8f0dbc388a`;
- `api/ragflow_server.py` blob `5f580075d66f9d85b1334e2c011ce3d9c8046bac`;
- root `LICENSE`;
- exact current head.

Verified:

- RAGFlow is a full RAG/agent application rather than a small retrieval library;
- documented features include document parsing/chunking, citations, heterogeneous sources, retrieval/reranking, APIs, agent workflows, MCP and chat channels;
- self-host prerequisites include at least 4 CPU cores, 16 GB RAM, 50 GB disk, Docker/Compose and Python 3.13;
- gVisor is required when its code-executor sandbox feature is enabled;
- the server initializes database tables/data, settings, runtime configuration, Redis-backed progress locking, plugins, MCP sessions, chat-channel threads and an HTTP application;
- startup intentionally disables a LiteLLM network fetch to avoid external startup dependence;
- current maintenance includes dependency/security remediation.

Primary conclusion:

RAGFlow remains a useful knowledge/RAG application-platform donor and optional workload. Its ingestion, chunking, citation, retrieval, plugin and operational patterns may inform Ptah, but its database records, chunks, model outputs and agent workflow state cannot become canonical Ptah Knowledge/Object/Activity truth automatically.

## Independent verification packet — AF01-V07

Repeated checks:

- canonical identity, `main` branch and exact inspected head;
- Apache-2.0 root licence;
- real server initialization path rather than README claims alone;
- database, Redis, plugin, MCP, chat-channel and HTTP boundaries;
- substantial self-host resource/dependency requirements;
- code-executor dependence on gVisor.

Challenges retained:

- “grounded citations” reduce risk but do not certify source correctness or model reasoning;
- ingested documents, generated chunks and embeddings require independent source identity, retention and deletion rules;
- application plugins/code execution expand the trust boundary;
- provider/model output rights and sensitive document handling remain external obligations;
- heavyweight application state must not replace Ptah's native Knowledge/Object index and Receipt boundaries.

Verifier conclusion: primary findings supported. No contradiction with WP10/ADR-0013 placement.

## Ptah relationship

- frozen donor group: Knowledge, data, search and plugins;
- current classification: optional application/workload plus architecture study;
- requirements supported: document ingestion/decomposition, retrieval/reranking, citation views, APIs, plugin and channel lifecycle patterns;
- prohibited inheritance: RAGFlow database/chunk IDs as canonical Ptah identity, citations as certification, model answers as truth, unrestricted plugin/code-executor authority;
- replacement/exit strategy: retain native Ptah Object/Knowledge/Receipt contracts and integrate RAGFlow only through bounded import/export or workload adapters.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current source confirms `infiniflow/ragflow` and materially expands the earlier high-level donor summary;
- exact current resource/runtime requirements supersede assumptions that RAGFlow is merely a lightweight library.

## Bounded outcome

`accepted for archive` does not approve RAGFlow as Ptah's canonical knowledge store, authorize document/model/provider use, approve code execution, reopen Phase 0A, accept ADR-0033 or authorize Ptah runtime implementation.
