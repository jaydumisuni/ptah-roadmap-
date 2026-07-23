# D060 — Trivy

Status: candidate record — paired evidence complete

Primary Archivist: `AF04-P04`

Independent Verifier: `AF04-V04`

Inspected: 2026-07-23

## Canonical source identity

- source: `aquasecurity/trivy`;
- default branch: `main`;
- exact inspected commit: `2c64b8f58b63dfd33f4bec32fc001662c705c002`;
- root licence: Apache-2.0;
- repository role: vulnerability, SBOM, secret, licence and misconfiguration scanner;
- archived: false.

## Primary evidence packet

Trivy scans container images, filesystems, Git repositories, VM images and Kubernetes targets. It can produce vulnerability, dependency/SBOM, misconfiguration, secret and licence findings. It is suitable as a specialist security workload or Provider behind Ptah's security evidence contracts.

## Independent verification packet

The verifier confirmed that scan coverage, vulnerability databases, policies, remote sources and commercial Aqua services are separate freshness and trust surfaces. A scanner finding is an Observation/Finding candidate, not proof of exploitability, remediation, safety or acceptance. Canary builds are explicitly not recommended for production.

## Contradiction and supersession

The donor pool correctly classified Trivy as a security workload. It does not define Ptah Core, security authority or canonical Finding identities.

## Bounded outcome

`accepted_for_archive_apache_security_scanner_workload_with_feed_and_finding_boundaries`

Allowed reuse:

- run or wrap Trivy as a version-pinned security workload;
- retain exact target, scanner set, database/policy revisions, output and limitations;
- translate results into Ptah-owned Observation/Finding candidates with provenance.

Restrictions:

- preserve Apache notices and review databases, plugins, policies and integrations separately;
- do not treat scanner completion or zero findings as proof of safety;
- do not automatically promote findings to accepted claims, remediation or release blocks without caller Policy;
- do not make Trivy Ptah's authority or mandatory security runtime.

This outcome does not authorize implementation.