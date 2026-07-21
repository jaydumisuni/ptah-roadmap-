# D043 — LlamaIndex Archive Record

Outcome: ACCEPTED FOR ARCHIVE WITH INTEGRATION/KNOWLEDGE-TRUTH RESTRICTIONS — framework donor only

Campaign: `CAMPAIGN-001`

Formation: `AF02`

Primary Archivist: `AF02-P09`

Independent Verifier: `AF02-V09`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `run-llama/llama_index`;
- owner: Run Llama organization;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `d88c2c9ed3cb057e056546c46800adaad16824d1`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: MIT;
- licence evidence: `LICENSE` blob `e6074042d0391061b7d7d45d21e6693ae108daec`;
- more than 300 separately packaged integrations may carry their own dependency, provider, model, database and service terms;
- LlamaParse/LlamaCloud and related hosted products are separate commercial/service boundaries requiring accounts/API keys and distinct data handling review;
- indexed documents, embeddings, model outputs and connector-fetched data retain their source rights and privacy obligations;
- activity state: active; inspected head fixes Redis KV-store byte/string key handling with expanded sync/async tests.

## Primary evidence packet — AF02-P09

Inspected:

- `README.md` blob `c1c7af8256b4d278748ea9b5c8b1a5da1858e691`;
- root `LICENSE`;
- exact commit diff for RedisKVStore integration and tests;
- current package/integration separation described by the repository.

Verified:

- LlamaIndex OSS is a framework for agentic/data/RAG applications;
- starter and customized installation paths separate `llama-index` from `llama-index-core` plus chosen integrations;
- the namespace distinguishes core abstractions from provider-specific packages;
- connectors ingest APIs, documents, SQL and other sources; indices/graphs and retrieval/query interfaces structure access to that data;
- hosted LlamaParse/LlamaCloud products are separate from OSS core;
- the inspected head demonstrates active integration-level maintenance: Redis key handling supports both byte and string keys, with synchronous/asynchronous regression tests and an integration package version bump.

Primary conclusion:

LlamaIndex is a useful framework/integration architecture donor for ingestion, indexing, retrieval, storage and provider adapters. Its nodes, indices, chunks, KV keys, embeddings and model responses cannot automatically become canonical Ptah Object/Knowledge truth, and broad integration availability must not be mistaken for reviewed trust.

## Independent verification packet — AF02-V09

Repeated checks:

- canonical identity, `main` branch and exact current head;
- MIT root licence;
- core vs integration namespace/package distinction;
- hosted Parse/Cloud boundary;
- actual integration code and tests at the inspected head;
- Python integration package requires Python 3.10+ in the changed Redis package.

Challenges retained:

- every connector/provider/vector store introduces independent credentials, privacy, licensing and availability risks;
- retrieved or model-generated content may be inaccurate, stale or unauthorized;
- chunks/embeddings can leak sensitive data and complicate deletion/retention;
- hosted parsing/extraction cannot become mandatory Ptah availability;
- framework abstractions and IDs must not replace native Ptah Object/Knowledge/Receipt identities;
- README explicitly notes documentation may be newer, so versioned source/package evidence remains required.

Verifier conclusion: primary findings supported. LlamaIndex belongs behind native Knowledge/Object and provider boundaries.

## Ptah relationship

- frozen donor group: knowledge, RAG and application-platform donors;
- current classification: optional framework/direct-core dependency plus bounded integrations;
- requirements supported: connector/adaptor design, ingestion, parsing/indexing, retrieval, storage and evaluation patterns;
- prohibited inheritance: connector data as trusted truth, LlamaIndex node/index IDs as canonical Ptah identity, hosted service as required dependency, unreviewed 300+ integration surface;
- replacement/exit strategy: preserve native Ptah Knowledge/Object/Receipt contracts and select integrations individually with exact pins and policy review.

## Contradiction and supersession

- current source clarifies the split between OSS framework, independently packaged integrations and hosted LlamaParse/LlamaCloud products;
- that separation supersedes shorthand descriptions of “LlamaIndex” as one homogeneous dependency;
- exact current integration tests confirm active maintenance without changing frozen Ptah architecture.

## Bounded outcome

`accepted for archive with integration/knowledge-truth restrictions` does not authorize document/provider/model use, hosted-service dependence, wholesale integration adoption, Phase 0A reopening, AF03 start, ADR-0033 acceptance or Ptah runtime implementation.
