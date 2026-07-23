# D059 — Semgrep

Status: candidate record — paired evidence complete

Primary Archivist: `AF03-P02`

Independent Verifier: `AF03-V02`

Inspected: 2026-07-23

## Canonical source identity

- source: `semgrep/semgrep`;
- default branch: `develop`;
- exact inspected commit: `b1b15360b40ec84164f077712053b88dc2c38e31`;
- root licence: GNU Lesser General Public License version 2.1;
- inspected implementation entry: `cli/src/semgrep/run_scan.py`, blob `047ce42fb7a9d28c02a9294693e5c7351837306d`;
- archived: false.

## Primary evidence packet

Semgrep Community Edition is a real local static-analysis engine and CLI rather than a documentation-only donor. The inspected scan implementation coordinates target selection, configuration, the core runner, dependency-aware rules, output handling, metrics, baseline comparison and structured findings.

Useful Ptah workload concepts include:

- running bounded repository scans as Activities;
- retaining exact rule/configuration, target selection and tool revision;
- treating findings as evidence-backed observations rather than automatic truth;
- preserving ignored, filtered, failed and partial scan outcomes;
- separating local source scanning from optional hosted orchestration;
- using security tools as replaceable workload Providers rather than Ptah Core authority.

## Independent verification packet

The verifier confirmed:

- the exact source file carries LGPL-2.1 notices and the root repository licence is LGPL-2.1;
- Community Edition performs local analysis but the README explicitly warns that its single-file/function analysis can miss true positives in security use;
- cross-file/cross-function analysis, proprietary rules, supply-chain capabilities, secrets scanning, Assistant triage and organizational policy features belong partly or wholly to Semgrep’s hosted/proprietary platform;
- a successful Semgrep process or finding emission does not prove a vulnerability exists or that remediation succeeded;
- rules, registries, proprietary rule sets and external services are separate rights and trust surfaces.

## Contradiction and supersession

The donor-pool label treated Semgrep as a security workload and stress-test donor. Current evidence supports that role, but not a claim that the open repository provides every advertised platform capability or that a finding is an accepted security verdict.

No frozen Ptah security, Claim/Finding, Evidence or approval decision is superseded. Semgrep may populate bounded Observation/Finding artifacts through an adapter; Ptah does not inherit Semgrep’s rule authority or hosted policy model.

## Bounded outcome

`accepted_for_archive_with_lgpl_and_security_finding_restrictions`

Allowed reuse:

- study and potentially adapt the local scanning workload behind a Provider boundary subject to LGPL-2.1 compliance;
- retain exact tool, rule, target, configuration, output and limitation evidence;
- use findings as inputs to separate review and remediation verification.

Restrictions:

- preserve LGPL-2.1 obligations and notices;
- do not imply proprietary Semgrep Platform, Pro engine, proprietary rules, Assistant, SCA or secrets capabilities are contained in the public repository;
- do not treat findings as final vulnerability truth, approval, remediation proof or release authority;
- do not upload private source or findings to hosted services without explicit configured authority;
- do not make Semgrep Ptah’s security authority or mandatory global scanner.

This outcome does not authorize implementation.