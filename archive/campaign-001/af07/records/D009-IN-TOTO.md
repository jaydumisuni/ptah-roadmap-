# D009 — in-toto

Status: candidate record — paired evidence complete

Primary Archivist: `AF07-P05`

Independent Verifier: `AF07-V05`

Inspected: 2026-07-23

## Canonical source identity

- source: `in-toto/in-toto`;
- default branch: `develop`;
- exact inspected commit: `a8ce9ee2125ae5a4b041a4e37cc1cf10eed0da6b`;
- root licence: Apache-2.0;
- repository role: software supply-chain layout/link metadata and verification implementation;
- archived: false.

## Primary evidence packet

in-toto provides step definitions, materials/products, command metadata, actors and verification patterns for how artifacts were produced.

## Independent verification packet

Layouts, keys, functionaries, link metadata and command records are trust inputs. Passing verification proves conformance to the selected layout and metadata, not general safety or semantic correctness. External effects and source truth need separate evidence.

## Contradiction and supersession

in-toto can inform Ptah provenance bundles but cannot replace canonical Activity, Receipt, Artifact or acceptance authority.

## Bounded outcome

`accepted_for_archive_apache_supply_chain_provenance_with_layout_key_metadata_and_truth_boundaries`

Allowed reuse: generate or verify pinned in-toto-compatible provenance from Ptah records.

Restrictions: preserve notices; pin layouts, keys and functionaries; retain negative/partial verification; never equate layout pass with general correctness or release approval.

This outcome does not authorize implementation.