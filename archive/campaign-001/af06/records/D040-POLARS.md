# D040 — Polars

Status: candidate record — paired evidence complete

Primary Archivist: `AF06-P07`

Independent Verifier: `AF06-V07`

Inspected: 2026-07-23

## Canonical source identity

- source: `pola-rs/polars`;
- default branch: `main`;
- exact inspected commit: `b1268f1c0109667f8cd29c5c3975fd01a4b2f61f`;
- root licence: MIT;
- repository role: columnar DataFrame/query engine;
- archived: false.

## Primary evidence packet

Polars can support fast structured-log analysis, result aggregation, table Views, dataset processing and report generation.

## Independent verification packet

Connectors, file formats, cloud stores, SQL interfaces and optional features are separate dependencies. DataFrame results depend on schemas, null/error handling, lazy optimization and exact input Revisions; computed output is not canonical source truth by itself.

## Contradiction and supersession

Polars is a data-processing Provider/library, not Ptah's canonical Data or Evidence authority.

## Bounded outcome

`accepted_for_archive_mit_data_processing_engine_with_connector_schema_and_source_revision_boundaries`

Allowed reuse:

- use a pinned Polars library for bounded data/report Activities;
- retain exact inputs, schemas, query/plan, version and output Artifact.

Restrictions:

- preserve MIT notices and review connectors/formats separately;
- bind results to exact source Revisions and retain parse/coercion limitations;
- do not mutate canonical source bytes or treat computed tables as accepted claims;
- resource-limit large workloads and keep unrelated Activities runnable.

This outcome does not authorize implementation.