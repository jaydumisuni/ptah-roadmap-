# ADR-0021A — WP04 Catalog and Proof-Vocabulary Correction

**Status:** ACCEPTED CORRECTION TO ADR-0021  
**Date:** 2026-07-19  
**Implementation authorization:** NONE

## Context

ADR-0021 and the WP04 work package were accepted while the record schemas and first six lifecycle candidates were cataloged as `ptah.runtime` `0.1.0`.

The final acceptance review compared every `required_receipt_proof_levels` value with `contracts/PHASE-0B-WP02-PROOF-LEVEL-REGISTRY.md` and found three lifecycle drafts using convenience labels that were not registered:

- `request_recorded`;
- `operation_started`;
- `operation_failed`;
- `runtime_started`;
- `runtime_stopped`.

No record schema or architectural boundary changed.

## Decision

The active WP04 catalog is:

- `schemas/phase-0b/runtime/schema-catalog.v0.1.1.json`.

The 19 runtime record schemas remain version `0.1.0`.

The active lifecycle machines are:

- `node.enrollment.lifecycle` `0.1.1`;
- `node.lifecycle` `0.1.0`;
- `facility.lifecycle` `0.1.0`;
- `facility.instance.lifecycle` `0.1.1`;
- `provider.lifecycle` `0.1.0`;
- `provider.instance.lifecycle` `0.1.1`.

The corrected machines use only registered WP02 proof levels, including:

- `requested`;
- `dispatched`;
- `process_started`;
- `operation_completed`;
- `output_created`;
- `external_result_recorded`.

The original `0.1.0` machine files and catalog remain superseded candidate history. They are not silently rewritten or selected by downstream work.

## Effect on ADR-0021 and WP04

Where ADR-0021, D-036 or the WP04 work package references `schemas/phase-0b/runtime/schema-catalog.v0.1.0.json` as the active catalog, interpret and migrate that reference to `schemas/phase-0b/runtime/schema-catalog.v0.1.1.json`.

The accepted Node, Facility, Provider, capability, resource, locality, lifecycle/health and dispatch-eligibility architecture remains unchanged.

No runtime, backend or dependency selection is authorized by this correction.