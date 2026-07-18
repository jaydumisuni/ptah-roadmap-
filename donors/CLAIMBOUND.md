# Donor Record — ClaimBound Evidence

**Phase:** 0A / Security and reproduction completion  
**Status:** FIRST-PASS COMPLETE — PRIMARY NARROW-CLAIM, FROZEN-PROTOCOL AND EVIDENCE-CARD DONOR  
**Inspected:** 2026-07-18

## Identity

- Current canonical URL: https://github.com/ClaimBound/claimbound-evidence
- Earlier repository/discovery name: `ClaimBound/claimbound-public-benchmarks`
- Default branch: `main`
- Pinned commit: `a55bc4339f92f3b45e97e6ba4aceca2949e31f51`
- Licence: Apache-2.0
- Activity: Active
- Primary language: Python plus JSON/SVG evidence records
- Classification: narrow-claim protocol, source-boundary audit, reproducibility status, evidence-card registry and external-review donor
- Ptah targets: Claim boundaries, allowed-claim sentence, frozen protocols, result/reproduction separation, negative/blocked evidence and reviewable public-safe summaries

## Files/components inspected

- `README.md`
- `docs/registry/evidence_index.json`
- representative card `docs/evidence_cards/CLAIMBOUND-API_PARITY_D001-2026-06-15.json`
- current repository/commit activity
- documented reviewer/operator paths, source-audit, software-development and public-data workflows

## Verified capabilities and patterns

### Narrow evidence cards

- ClaimBound turns a narrow public claim into an evidence card rather than a broad certification.
- Cards retain protocol ID/version, source boundary, operator, access/verification dates, execution mode, result status, reproduction level, claim boundary, allowed claim sentence, limitations and report references/hashes.
- A representative software-development card retains frozen commands, git commit, sanitized report hash, control/gate summary and an explicit statement of what the card does not prove.
- Evidence cards can distinguish source audit, evidence result and other bounded record types.

### Result and reproduction separation

- `PASSED_UNDER_PROTOCOL` means one exact frozen gate passed; it is not universal quality or safety.
- `BLOCKED_SOURCE`, negative, drift and other non-pass outcomes are retained as first-class evidence.
- Reproduction level is separate from result status; a gate can pass while remaining single-operator and not independently reproduced.
- Verification level/count and operator identity remain visible.
- Source-byte drift can affect reproduction status without changing the narrow gate outcome.

### Registry and public-safe evidence

- The registry indexes cards by evidence ID, sequence, path, result status, protocol, domain, record type, operator, dates, verification and reproduction status.
- Raw payloads may be omitted while sanitized summaries and hashes remain public.
- Registry validation and card validation are separate from generating a scaffold/demo.
- The project explicitly states that it is not a leaderboard, certification authority, hosted review queue or proof of general model quality.

## What ClaimBound contributes

- Strong wording discipline around narrow claims.
- Frozen protocol and allowed-claim sentence patterns.
- Clear separation of result, reproduction, verification and certification.
- Negative, blocked and drift outcomes as first-class records.
- Human-readable/public evidence cards backed by structured JSON.
- Sanitized report references and hashes instead of automatically publishing raw data.
- Operator/verification-level transparency.
- A practical donor for Ptah Evidence Explorer and external/public proof summaries.

## Important limitations for Ptah

- A card remains a record produced by one repository/protocol/operator and may be wrong or incomplete.
- Single-operator validation is not independent review.
- Sanitized summaries may omit details required to audit the raw result.
- Hashes prove content identity, not correctness of source, protocol or interpretation.
- A frozen protocol can be narrowly valid while testing the wrong question or missing material cases.
- Registry consistency does not prove every card's underlying evidence.
- Result/status vocabularies are ClaimBound-specific and cannot become universal Ptah Activity state.
- Evidence IDs and registry sequence are repository-local identities.
- Source access, legal rights and online drift remain external concerns.
- Visual green/red/yellow summaries can be misread if separated from claim boundary/limitations.
- ClaimBound does not replace Ptah Activity receipts, raw Artifacts, independent Sergeant review or caller acceptance.

## Must not be inherited

- `GREEN_VALIDATED` or `PASSED_UNDER_PROTOCOL` presented as safe, certified or generally correct;
- ClaimBound evidence IDs/registry sequences as canonical Ptah identities;
- single-operator status described as independent reproduction;
- sanitized summary used when policy requires raw restricted evidence;
- frozen command exit 0 treated as proof of broader system behavior;
- allowed claim sentence detached from claim boundary, period/source scope and limitations;
- negative/blocked/drift outcomes hidden from UI;
- card/registry validation interpreted as validation of every underlying source;
- public card policy forced on private/regulated evidence;
- ClaimBound made mandatory as the only evidence presentation format.

## Integration decision

**ADAPT CLAIMBOUND'S NARROW-CLAIM, FROZEN-PROTOCOL, ALLOWED-SENTENCE AND RESULT/REPRODUCTION SEPARATION INTO PTAH CLAIM/EVIDENCE PRESENTATION; KEEP PTAH RAW ARTIFACTS, ACTIVITIES, PROOF LEVELS AND REVIEW AUTHORITATIVE.**

Recommended Ptah role:

1. every Evidence Card is a View over a Ptah Claim, protocol revision, Activity attempts, raw/restricted Artifacts and reviewer status;
2. the card states one allowed claim sentence and an explicit claim boundary;
3. result status, reproduction level, verification level and review/acceptance remain separate;
4. source/period/target/operator/protocol identity and exact hashes are mandatory;
5. negative, blocked, drifted and not-reproduced outcomes remain visible;
6. public cards reference sanitized summaries while restricted raw evidence remains access-controlled;
7. external operators can add independent verification records without rewriting the original;
8. visual status always travels with the boundary/limitations;
9. card schemas remain a presentation/export format rather than Activity truth;
10. ClaimBound can be replaced while Ptah Claim/Evidence identities remain stable.

## Native Ptah gap

Ptah must define:

- Claim and Claim Revision;
- allowed claim sentence and explicit boundary;
- Protocol and frozen Protocol Revision;
- source/target/period/operator scope;
- Result Status separate from Activity state;
- Reproduction Level, Verification Level and Review Level;
- raw, sanitized and public Evidence Artifacts;
- source/report hashes and signature/provenance;
- limitation, blocked-source and drift records;
- external verifier and independent reproduction records;
- Evidence Card View/schema and registry/export relationship;
- audience/privacy/legal-rights policy;
- supersession without historical rewrite.

## Exit strategy

Ptah's Claim/Evidence contracts remain independent. ClaimBound-style cards, signed attestations, Sergeant reports, CI summaries, public proof pages or other formats can render them without changing underlying Claims, Activities, Artifacts or reviews.

## Validation required

1. Produce cards for pass, fail, blocked-source, drift and not-independently-reproduced cases.
2. prove the visual summary cannot be rendered without the allowed claim sentence and boundary.
3. retain raw restricted evidence while publishing a hashed sanitized summary.
4. add a second independent verification without changing the first operator's record.
5. freeze a protocol, change it and create a new protocol/card revision.
6. show a passing narrow gate that intentionally does not satisfy a broader acceptance claim.
7. validate registry/card consistency while independently detecting a flawed underlying protocol.
8. preserve source-byte drift as a separate reproduction state.
9. replace the card renderer/export without identity loss.
10. prevent public evidence from exposing private/customer/security data.
