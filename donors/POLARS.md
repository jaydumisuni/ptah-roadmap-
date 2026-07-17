# Donor Record — Polars

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PRIMARY STRUCTURED TABLE/DATA QUERY ENGINE CANDIDATE  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/pola-rs/polars
- Default branch: `main`
- Pinned commit: `7b67ac4ecc224fee5d9da21ba0cb026be6b5df79`
- Licence: MIT
- Activity: Active
- Primary language: Rust, with Python, Node.js, R and SQL frontends
- Classification: analytical DataFrame query engine and structured-data Facility donor
- Ptah targets: `DATA-001`, tabular Objects, lazy/streaming transformations, query planning, large-data execution and result Artifacts

## Files/components inspected

- `README.md`
- `LICENSE`
- `crates/polars-lazy/src/frame/mod.rs`
- lazy/eager, streaming, Arrow, SQL/frontend and query-plan boundaries

## Verified capabilities and patterns

- Implements an analytical DataFrame query engine in Rust.
- Supports eager and lazy execution.
- LazyFrames build logical plans that are optimized and executed only when results are collected.
- Supports plan explanation for original and optimized plans.
- Supports projection, predicate, slice and expression optimizations.
- Supports multithreaded and SIMD execution.
- Supports streaming execution for datasets larger than RAM.
- Uses Apache Arrow columnar memory concepts.
- Exposes Python, Rust, Node.js, R and SQL-facing APIs.
- Supports feature-gated readers such as CSV, JSON/NDJSON and Parquet.
- Can retain logical plans separately from materialized results.
- Provides CPU-compatibility and large-index build variants.

## What Polars completes

- A fast local structured-data execution engine.
- Lazy query planning and plan inspection.
- Larger-than-memory streaming paths.
- Multilanguage access without inventing a custom table engine.
- A strong basis for Dataset/Table/Query/Transformation Activities.
- Columnar data exchange through Arrow-compatible formats.
- A practical path for logs, metrics, reports, CSV/Parquet/JSON and analytical results.

## Important limitations for Ptah

- A Polars DataFrame/LazyFrame is process/library state, not canonical Dataset or Table identity.
- Lazy-plan success does not prove source freshness, semantic correctness or acceptance.
- Input readers, schemas and optional feature sets vary by build.
- Query optimization may change physical execution order and resource behavior.
- User-defined functions can execute arbitrary code and reduce optimization/reproducibility.
- Streaming does not guarantee every operation can run fully out of core.
- Polars is analytical rather than a transactional database.
- It does not own source permissions, Object storage, lineage, Activity durability or result provenance.
- Python/R/Node bindings introduce separate runtime and dependency surfaces.
- CPU-feature-specific builds can fail or behave differently on older Nodes.
- Distributed/managed offerings are optional products, not required Ptah foundations.

## Must not be inherited

- Polars DataFrame/LazyFrame or internal plan IDs as Ptah identities;
- eager collection of unbounded datasets by default;
- UDFs enabled under ordinary table-query permission;
- optimized plan used as the only retained query definition;
- source paths/URLs treated as stable Dataset identity;
- output completion promoted to verified analytical conclusion;
- one frontend language or build feature set made universal;
- Polars used as a transactional catalogue/database;
- cloud/managed Polars made mandatory.

## Integration decision

**ADOPT POLARS AS THE PRIMARY LOCAL STRUCTURED-DATA QUERY/TRANSFORMATION ENGINE CANDIDATE.**

Ptah owns Dataset, Table, Schema, Query, Transformation, Result and lineage identities. Polars executes approved logical plans against exact source Objects or database snapshots.

Recommended roles:

1. CSV/JSON/Parquet/Arrow analysis;
2. Activity/log/telemetry result analysis;
3. report/table generation;
4. dataset filtering, joins, aggregation and comparison;
5. streaming transforms for large local data;
6. SQL-compatible analytical access where useful.

Transactional SQL databases remain separate Facilities.

## Native Ptah gap

Ptah must define:

- Dataset, Table, Column Schema and revision identities;
- source Object/database snapshot references;
- query and transformation expression/plan records;
- original and optimized plan Artifacts;
- engine/version/build-feature/runtime identity;
- eager, lazy, streaming and distributed execution class;
- resource budget, cancellation and spill behavior;
- UDF/plugin permission and provenance;
- output Object/Artifact formats and schemas;
- row/column-level privacy and permission filters;
- lineage from input fields to output fields;
- result verification and comparison;
- alternate engine/backend mappings.

## Exit strategy

Ptah's Data contracts remain implementable with Polars, DuckDB, SQL engines, Spark/Ray or other analytical systems. Polars plans and DataFrames remain backend metadata.

## Validation required

1. Load CSV, JSON and Parquet Objects with explicit source revisions and schemas.
2. Execute the same transformation eagerly, lazily and streaming where supported and compare results.
3. Retain original and optimized plans plus engine/build identity.
4. Process a larger-than-RAM dataset under a bounded memory budget.
5. Cancel a long query and preserve partial/failed evidence without corrupting source Objects.
6. Restrict UDF execution behind a separate high-risk Facility permission.
7. Produce result Objects/Artifacts with exact input lineage.
8. Replace Polars with another engine for one query without changing Dataset/Query identity.
