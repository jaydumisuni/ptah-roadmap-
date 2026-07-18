# Donor Record — Polars

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PRIMARY LOCAL STRUCTURED TABLE/DATA QUERY ENGINE CANDIDATE  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/pola-rs/polars
- Default branch: `main`
- Pinned commit: `434fa104a500e2c3371fdcd5701ce829848274d1`
- Release represented by pinned commit: Python Polars `1.43.0`
- Licence: MIT
- Activity: Active
- Primary language: Rust, with Python, Node.js, R and SQL frontends
- Classification: analytical DataFrame query engine and structured-data Facility donor
- Ptah targets: `DATA-001`, tabular Objects, lazy/streaming transformations, query planning, large-data execution, plan evidence and Result Artifacts

## Files/components inspected

- `README.md`
- `LICENSE`
- `crates/polars-lazy/src/frame/mod.rs`
- release/current commit evidence
- lazy/eager, streaming, Arrow, SQL/frontend, feature-gate and query-plan boundaries

## Verified capabilities and patterns

### Engine and frontends

- Implements an analytical DataFrame query engine in Rust.
- Supports eager and lazy execution.
- Supports Python, Rust, Node.js, R and SQL-facing APIs.
- Uses Apache Arrow columnar concepts for data interchange and memory representation.
- Supports multithreaded and SIMD execution.
- Reader and operation support can be feature-gated at build time.
- Current binary families include modern-CPU, older-CPU compatibility and large-index variants.

### Lazy logical plans

- A `LazyFrame` is an abstraction over a logical plan rather than a materialized table.
- Operations incrementally modify the logical plan until output is collected.
- The original logical plan and optimization state are retained separately.
- Optimizations can include projection pushdown, predicate pushdown, slice pushdown, type coercion/checking, expression simplification, common-subplan/common-expression elimination, order checks and row estimates.
- Optimizations can be selectively disabled or configured.
- Original and optimized plans can be described or explained separately.
- GPU, eager and streaming execution flags exist as explicit plan/runtime choices.

### Streaming and scale

- Streaming execution can process supported queries or query portions against data larger than available RAM.
- The public Python interface exposes streaming collection as an engine choice.
- Streaming is not promised for every operation and may combine streaming and non-streaming stages.
- Large-index builds support row counts beyond the default 32-bit index boundary with a performance/memory trade-off.
- CPU-target choices affect portability and performance.

## What Polars completes

- A fast local structured-data execution engine.
- Lazy query planning and original/optimized plan inspection.
- Larger-than-memory streaming paths for supported operations.
- Multilanguage access without inventing a custom table engine.
- A strong basis for Dataset, Table, Query and Transformation Activities.
- Columnar data exchange through Arrow-compatible formats.
- A practical path for logs, metrics, reports, CSV, Parquet, JSON/NDJSON and analytical results.
- Explicit build/runtime choices that can be captured in Activity provenance.

## Important limitations for Ptah

- A Polars DataFrame or LazyFrame is process/library state, not canonical Dataset or Table identity.
- Lazy-plan success does not prove source freshness, semantic correctness or acceptance.
- Input readers, schemas, optional feature sets and behavior vary by build.
- Query optimization can change physical execution order, memory use and timing while preserving intended result semantics.
- User-defined functions can execute arbitrary code and reduce optimization, portability and reproducibility.
- Streaming does not guarantee every operation runs fully out of core.
- Polars is analytical rather than a transactional database.
- It does not own source permissions, Object storage, lineage, Activity durability or result provenance.
- Python, R and Node bindings add separate runtime and dependency surfaces.
- CPU-feature-specific binaries can fail on incompatible Nodes; compatibility builds have different performance properties.
- Large-index mode changes index width and resource behavior.
- GPU behavior and support may differ from CPU execution and require separate proof.
- Managed/distributed offerings are optional products, not required Ptah foundations.
- An optimized plan explanation is not a complete physical execution trace or independent correctness proof.

## Must not be inherited

- Polars DataFrame, LazyFrame or internal plan IDs as Ptah identities;
- eager collection of unbounded datasets by default;
- UDFs enabled under ordinary table-query permission;
- optimized plan used as the only retained Query definition;
- source paths or URLs treated as stable Dataset identity;
- output completion promoted to a verified analytical conclusion;
- one frontend language, CPU target or feature set made universal;
- Polars used as a transactional catalogue/database;
- cloud/managed Polars made mandatory;
- streaming requested and then reported as fully streaming without operator-level evidence;
- GPU/CPU or large-index results assumed equivalent without conformance checks.

## Integration decision

**ADOPT POLARS AS THE PRIMARY LOCAL STRUCTURED-DATA QUERY/TRANSFORMATION ENGINE CANDIDATE.**

Ptah owns Dataset, Table, Schema, Query, Transformation, Result and lineage identities. Polars executes approved logical plans against exact source Objects or database snapshots.

Recommended roles:

1. CSV, JSON/NDJSON, Parquet and Arrow analysis;
2. Activity, log and telemetry result analysis;
3. report/table generation;
4. dataset filtering, joins, aggregation and comparison;
5. streaming transforms for large local data;
6. SQL-compatible analytical access where useful;
7. original and optimized plan Artifact production;
8. backend-conformance comparison against SQL/DuckDB or another engine.

Transactional SQL databases remain separate Facilities.

## Licence decision

The root MIT licence is compatible with architecture study, wrapping and selective adoption. Frontend bindings, optional packages and external data connectors still require dependency-level review.

## Native Ptah gap

Ptah must define:

- Dataset, Table, Column Schema and revision identities;
- source Object or database-snapshot references;
- Query and Transformation expression/plan records;
- original, optimized and physical-plan evidence Artifacts where available;
- engine, version, build features, CPU target, index width and runtime identity;
- eager, lazy, streaming, GPU and distributed execution classes;
- resource budget, cancellation, spill and partial-result behavior;
- UDF/plugin permission, package and provenance records;
- output Object/Artifact formats and schemas;
- row/column-level privacy and permission filters;
- lineage from input fields to output fields;
- Result verification and cross-engine comparison;
- transactional database separation and snapshot semantics;
- alternate engine/backend mappings.

## Exit strategy

Ptah's Data contracts remain implementable with Polars, DuckDB, SQL engines, Spark, Ray or other analytical systems. Polars plans and DataFrames remain backend metadata rather than public Ptah identities.

## Validation required

1. Load CSV, JSON/NDJSON and Parquet Objects with exact source revisions and schemas.
2. Execute the same Transformation eagerly, lazily and streaming where supported and compare Results.
3. Retain original and optimized plans plus engine, build-feature, CPU-target and runtime identity.
4. Process a larger-than-RAM dataset under a bounded memory budget and label non-streaming stages.
5. Cancel a long Query and preserve partial/failed evidence without corrupting source Objects.
6. Restrict UDF execution behind a separate high-risk Facility permission and sandbox.
7. Produce Result Objects/Artifacts with exact table, column and source lineage.
8. Run modern-CPU and compatibility builds against a golden corpus and compare Results.
9. Run default-index and large-index builds against boundary cases.
10. Compare CPU and GPU execution where both are supported.
11. Replace Polars with another engine for one Query without changing Dataset, Query or Result identity.
12. Prove transactional write operations route to a database Facility rather than Polars.
