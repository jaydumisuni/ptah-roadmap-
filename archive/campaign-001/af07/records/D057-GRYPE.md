# D057 — Grype

Status: candidate record — paired evidence complete

Primary Archivist: `AF07-P02`

Independent Verifier: `AF07-V02`

Inspected: 2026-07-23

## Canonical source identity

- source: `anchore/grype`;
- default branch: `main`;
- exact inspected commit: `4562c55cebba5fe50a0c5afc7cec50a3b2392a87`;
- root licence: Apache-2.0;
- repository role: vulnerability scanner for images, filesystems and SBOMs;
- archived: false.

## Primary evidence packet

Grype can scan exact images, filesystems or SBOM Artifacts and emit vulnerability matches suitable for Ptah security workloads.

## Independent verification packet

Results depend on database revision, matchers, package inventory, configuration and source coverage. A match is a Finding candidate; absence of matches is not proof of safety. Feed freshness and false positives/negatives must remain visible.

## Contradiction and supersession

Grype remains a specialist workload, not Ptah's security authority.

## Bounded outcome

`accepted_for_archive_apache_vulnerability_scanner_with_database_matcher_sbom_and_finding_limits`

Allowed reuse:

- run a pinned Grype workload against exact source/SBOM Revisions;
- retain database digest, matcher configuration, findings and limitations.

Restrictions:

- preserve Apache notices and review feeds/integrations separately;
- do not promote matches to accepted Claims or remediation without review;
- do not treat zero matches as proof of safety;
- bind all results to exact source and database revisions.

This outcome does not authorize implementation.