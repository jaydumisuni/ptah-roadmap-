# Donor Record — DuckDB

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — SQL/ANALYTICAL DATABASE COMPLETION DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/duckdb/duckdb
- Default branch: `main`
- Pinned commit: `117e1a46be1c903c5a36ee3c881c125597f93c60`
- Licence: MIT-style permissive licence
- Activity: Active
- Primary language: C++ with multiple client bindings
- Classification: embedded analytical SQL database and file-query engine donor
- Ptah targets: `DATA-001`, SQL Query Activities, structured file/database snapshots, complex/nested types, portable analytical execution and cross-engine verification with Polars

## Files/components inspected

- `README.md`
- `LICENSE`
- current commit/repository identity
- documented SQL, CSV/Parquet, CLI and client-binding boundaries

## Verified capabilities and patterns

- Provides an embedded high-performance analytical database with a rich SQL dialect.
- Supports correlated subqueries, window functions, collations and complex values such as arrays, structs and maps.
- Supports standalone CLI use and clients for Python, R, Java and WebAssembly among others.
- Can query CSV and Parquet files directly from SQL.
- Integrates with common DataFrame ecosystems.
- Is portable enough to act as a local or embedded analytical Facility rather than requiring a separate database server.
- Maintains its own tests and benchmark machinery.

## What DuckDB completes

- A direct SQL execution path beside Polars DataFrame plans.
- An embedded analytical database option for one-Node and local Workspaces.
- Querying of structured Object files without first loading every dataset into a long-lived server database.
- Complex-type and relational semantics useful for tables, logs, result sets and analytical reports.
- A second engine for golden-corpus and cross-engine verification.
- A WebAssembly-compatible path for bounded client-side analysis where appropriate.

## Important limitations for Ptah

- DuckDB relations, tables, files and database IDs are not canonical Ptah Dataset or Table identities.
- It is an analytical database, not the universal transactional catalogue or distributed database for Ptah.
- SQL completion does not prove source freshness, lineage, privacy or analytical correctness.
- Direct file references are paths/URIs, not stable Object/View identities.
- Extensions and client bindings add independent dependency, licence and security surfaces.
- Arbitrary SQL can be expensive, disclose data, mutate database state or load extensions unless restricted.
- Embedded concurrency, persistence and crash-recovery behavior must be tested against the exact deployment mode.
- WebAssembly, native and language-binding executions may differ in available features and performance.
- A database file is mutable state and needs snapshot/revision/backup rules.
- DuckDB does not own durable Ptah Activities, permissions, resource budgets, proof or caller acceptance.

## Must not be inherited

- DuckDB database/table/relation IDs as Ptah identities;
- raw file paths used as canonical Dataset identity;
- unrestricted SQL or extension loading under ordinary read-query permission;
- DuckDB used as Ptah's universal transactional store;
- query success promoted to proof of a claim;
- mutable database files treated as immutable Artifacts;
- one language binding or native build made mandatory;
- client-side/Wasm execution allowed to bypass Object/privacy policy;
- engine-specific SQL exposed as the only Ptah Query contract.

## Integration decision

**ADOPT DUCKDB AS THE PRIMARY EMBEDDED SQL/ANALYTICAL DATABASE COMPLETION CANDIDATE BESIDE POLARS.**

Ptah owns Dataset, Table, Schema, Query, Result, snapshot, lineage and permission identities. DuckDB executes approved SQL against exact source Objects, database snapshots or bounded external connectors.

Recommended roles:

1. SQL over CSV, Parquet and Arrow-compatible Objects;
2. embedded local analytical databases;
3. joins, windows, nested/complex types and report queries;
4. Query-plan/result comparison with Polars;
5. bounded read-only access to database snapshots;
6. Result Artifact generation.

Transactional service databases remain separate provider Facilities.

## Licence decision

The permissive root licence is compatible with architecture study and adoption. Extensions, clients and transitive dependencies require independent review.

## Native Ptah gap

Ptah must define:

- Dataset, Table, Column Schema and snapshot/revision identities;
- Object/View or external database-snapshot references;
- Query and parameter records independent of SQL text alone;
- read-only, write, DDL and extension-load permission classes;
- original SQL, normalized plan and available execution-plan evidence;
- engine/version/build/client identity;
- resource budgets, cancellation, spill and partial-result behavior;
- database-file snapshots, backup, recovery and locking;
- row/column/object privacy scopes;
- Result Objects/Artifacts and lineage;
- external transactional database provider contract;
- cross-engine conformance and migration tests.

## Exit strategy

Ptah's Data contracts remain independent and can use DuckDB, Polars, PostgreSQL, SQLite, Spark, Ray or other engines without changing Dataset, Query or Result identity.

## Validation required

1. Query exact CSV and Parquet Object revisions through both DuckDB and Polars and compare Results.
2. Retain engine/version/build, SQL and source snapshot identity.
3. Enforce read-only mode and deny DDL, extension loading and external access without separate permission.
4. Cancel a resource-heavy Query and preserve failed/partial evidence.
5. Snapshot and restore an embedded database file without losing lineage.
6. Test concurrent readers/writers and crash recovery in the selected deployment mode.
7. Return Result Artifacts with schema and source-column lineage.
8. Replace DuckDB with another SQL engine without changing Ptah Dataset/Query/Result identities.
9. Prove WebAssembly/client execution cannot bypass Object/privacy policy.
10. Route transactional service writes to a separate database Facility.
