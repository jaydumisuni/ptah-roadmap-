# Phase 0B WP10 — Knowledge, Data, Package and Plugin

**Status:** CANDIDATE BLUEPRINT
**Implementation authorization:** NONE

## Required entities

- Dataset, immutable Dataset Revision, schema/profile and lineage;
- Index Definition, Index Revision, Ingestion Run, Segment and coverage;
- Query Request, Query Run, Result Set, citation/source binding and ranking evidence;
- Database Connection Reference, Snapshot and transaction/consistency evidence;
- Package, Package Revision, dependency declaration, resolved graph and lock record;
- Plugin, Plugin Revision, Manifest, Installation, Activation, Instance and health;
- Plugin capability grant, permission scope, compatibility and revocation;
- reusable Recipe publication/discovery separated from execution acceptance.

## Core laws

1. Source Object truth is separate from extracted text, chunks, embeddings, indexes and generated answers.
2. Search result relevance is not source authority or factual correctness.
3. Every result binds exact source revisions and coverage limitations.
4. Dataset schema, observations and analytical claims remain separate.
5. Package identity is not registry URL, mutable version range or installation path.
6. Plugin discovery, installation, activation, health and trust approval remain separate.
7. Plugin permissions are explicit, least-privilege, expiring and revocable.
8. Removing a Plugin cannot delete historical evidence or Objects it produced.
9. Knowledge or agent platforms may run as workloads but cannot replace Ptah Core.

## Proof cases

- re-indexing after source revision creates new index evidence without rewriting source history;
- partial ingestion exposes exact gaps;
- result citations resolve to immutable source revisions;
- mutable package ranges cannot masquerade as locked resolution;
- incompatible or revoked Plugin cannot activate;
- Plugin crash degrades only its capabilities;
- rollback restores prior Plugin Revision while retaining failed evidence;
- backend replacement preserves Dataset, Package, Plugin and source identity.

## Outputs

Conventions, entity kinds, schemas/catalog, lifecycle machines, migration, fixtures, safety net, package record and ADR-0027.
