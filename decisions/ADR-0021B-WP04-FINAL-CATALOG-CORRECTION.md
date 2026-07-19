# ADR-0021B — WP04 Final Catalog Correction

**Status:** ACCEPTED; SUPERSEDES ADR-0021A CATALOG POINTER  
**Date:** 2026-07-19  
**Implementation authorization:** NONE

## Context

After the WP02 proof-vocabulary correction recorded by ADR-0021A, the Provider Instance lifecycle received one additional precision review for:

- exact local-Node versus approved remote-service locality;
- startup/binding wording;
- durable exact-generation failure versus transient health;
- stop/unbind behavior and cleanup evidence.

## Decision

The final active WP04 candidate catalog is:

- `schemas/phase-0b/runtime/schema-catalog.v0.1.2.json`.

It retains the same 19 record schemas at version `0.1.0`.

Active lifecycle versions are:

- `node.enrollment.lifecycle` `0.1.1`;
- `node.lifecycle` `0.1.0`;
- `facility.lifecycle` `0.1.0`;
- `facility.instance.lifecycle` `0.1.1`;
- `provider.lifecycle` `0.1.0`;
- `provider.instance.lifecycle` `0.1.2`.

The `0.1.2` Provider Instance lifecycle supersedes `0.1.1` because the latter corrected proof vocabulary but retained imprecise locality and failure wording.

Where ADR-0021, D-036, the WP04 work package or ADR-0021A points to runtime catalog `0.1.0` or `0.1.1` as active, the canonical active reference is `0.1.2`.

All earlier catalogs and machine versions remain superseded candidate history. The Node/Facility/Provider architecture and implementation boundary are unchanged.