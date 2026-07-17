# Donor Record — in-toto

**Phase:** 0A / WP03  
**Status:** FIRST-PASS COMPLETE — SUPPLY-CHAIN MODEL DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/in-toto/in-toto
- Default branch: `develop`
- Pinned commit: `a8ce9ee2125ae5a4b041a4e37cc1cf10eed0da6b`
- Licence: Apache-2.0
- Activity: Active
- Classification: Software supply-chain layout, materials/products, functionary and verification donor
- Ptah targets: ordered Build/Package steps, expected materials/products, authorized producers, inspections and independently verifiable Artifact lineage

## Files/components inspected

- `README.md`
- `LICENSE`
- documented Layout, Step, Inspection, Link and Artifact Rule model
- `in-toto-run`, `in-toto-record`, verification and signature boundaries

## Verified capabilities and patterns

- A signed Layout defines the planned supply-chain steps, authorized functionaries, expiration and inspections.
- Functionaries execute steps and create signed Link metadata containing command, materials and products.
- Materials are inputs; products are outputs.
- Artifact Rules can CREATE, DELETE, MODIFY, ALLOW, DISALLOW, REQUIRE and MATCH materials/products across steps.
- Rules chain expected outputs from one step into later inputs.
- Multi-part/manual steps may record start materials and later stop products.
- Verification checks Layout signatures/expiration, authorized functionaries, expected commands, materials/products and inspections.
- Layout and Links can ship with the final product for independent verification.
- Signed Layout and Link identities are separate.
- The system makes explicit that only declared materials/products are recorded; undeclared file use/change is not automatically captured.

## What in-toto completes

- A mature model for expected ordered Build/package steps.
- Explicit producer/functionary authorization.
- Materials/products and command evidence.
- Rule-based continuity between pipeline stages.
- Independent verification of whether a declared supply-chain plan was followed.
- A useful standard relationship between Build recipes, step receipts and final release bundles.

## Important limitations for Ptah

- in-toto is supply-chain focused, not Ptah's universal Activity or Object graph.
- The classic Layout assumes a project owner defines authorized steps; Ptah itself must not become the authority deciding every user's policy.
- Only declared materials/products are recorded, so automatic discovery/attestors are still needed.
- File-pattern rules are path-oriented and do not replace content-addressed Ptah Object identity.
- A valid supply-chain chain does not prove software quality, runtime correctness or external acceptance.
- Long-running, interactive, device and graphical Activities need broader receipts/checkpoints.
- Layout/Link metadata is not Ptah's storage, Event or Session model.
- Functionary keys and approval policy belong to caller/project configuration.

## Must not be inherited

- Layout policy as universal Ptah policy.
- Path/pattern names treated as immutable Artifact identity.
- Only declared files silently excluding important observed dependencies without a warning/proof class.
- Valid signatures or chain verification promoted to quality approval.
- Supply-chain Step state replacing Ptah Activity state.
- One fixed authorized-functionary model imposed on all users/callers.
- Link metadata used as the only evidence or telemetry record.

## Integration decision

**ADOPT IN-TOTO COMPATIBILITY FOR BUILD/RELEASE PROVENANCE; KEEP PTAH RECEIPTS BROADER.**

Ptah Build Recipes and proof bundles should be exportable as in-toto-compatible Layout/Link or attestation records where suitable. Caller/project policy can require verification, but Ptah remains the execution world rather than the project owner.

Ptah's native Artifact/Receipt graph should support:

- planned steps and dependency order;
- declared and observed materials/products;
- exact content hashes/Object IDs;
- producer/Node/Facility identity;
- command/action reference;
- inspections/reviews;
- verification result and limitations.

## Native Ptah gap

Ptah must define:

- mapping from Build Recipe Activities to Steps/Links;
- content-addressed Object IDs in addition to paths;
- declared versus automatically observed materials/products;
- dynamic/conditional DAG branches and retries;
- Activity attempt and checkpoint relationships;
- caller-provided authorized producer/policy references;
- non-file Objects and device/application outputs;
- integration with Witness/DSSE, Cosign/Sigstore and ORAS;
- proof levels and authoritative-result semantics from ADR-0004;
- private signing/policy configuration outside public Ptah.

## Exit strategy

Ptah preserves its native Receipt/Artifact graph and can emit in-toto, SLSA-compatible or other provenance formats. in-toto is an interoperability and verification target, not the only stored representation.

## Validation required

1. Generate a signed Layout/plan for source→build→test→package.
2. Produce signed Links/attestations bound to exact Ptah Objects and Activity attempts.
3. Detect missing, modified, unauthorized and unexpected products through rules.
4. Chain one step's product into the next step's material by digest.
5. Verify a multi-part/manual step without losing operation/attempt identity.
6. Add an undeclared observed dependency and surface the coverage gap rather than silently claiming completeness.
7. Run independent verification from a clean/offline environment.
8. Prove valid in-toto verification remains separate from functional review/acceptance.
9. Preserve provenance if the caller changes signing identity or policy backend.
