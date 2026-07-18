# Donor Record — Semgrep

**Phase:** 0A / Security and reproduction completion  
**Status:** FIRST-PASS COMPLETE — PRIMARY SOURCE/PATTERN/DATAFLOW STATIC-ANALYSIS DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/semgrep/semgrep
- Default branch: `develop`
- Pinned commit: `1f15ff4eb9f56f5a3b6a9afb958bdc82b5b6bcb0`
- Licence: LGPL-2.1-or-later for the inspected open-source engine repository
- Activity: Active
- Primary implementation: OCaml engine with Python/CLI components
- Classification: syntax-aware pattern, taint/dataflow, dependency-aware and policy-rule static-analysis donor
- Ptah targets: source/static scan Activities, exact source spans, rule/ruleset revision, dataflow evidence, structured errors/skips, suppressions and SARIF/JSON interoperability

## Files/components inspected

- `README.md`
- `LICENSE`
- `cli/src/semgrep/semgrep_interfaces/semgrep_output_v1.proto`
- current repository/commit activity
- documented open-source/community versus proprietary/advanced analysis boundaries

## Verified capabilities and patterns

### Source and rule analysis

- Semgrep applies syntax-aware rules to supported source languages and related configuration formats.
- Rules can describe local patterns and, depending on engine/tier/configuration, taint/dataflow and dependency-related findings.
- Findings bind to exact file, start/end positions and matched source content.
- Rule metadata can carry category, technology, confidence, references, CWE/OWASP mapping and remediation guidance.
- Rule ID, rule hash/ruleset origin and engine kind are necessary to interpret a result.

### Structured output

- The inspected output schema distinguishes matches, errors, skipped targets, skipped rules and profiling/engine metadata.
- Match records can retain rule/check identity, path, source range, metavariables, message, severity, metadata, fingerprint and optional validation state.
- Dataflow traces can retain sources, intermediate variables/calls and sink paths.
- Dependency-aware results can retain matched dependency, lockfile/package metadata and reachability information.
- Errors and skipped analysis remain first-class output rather than being flattened into an empty findings list.
- SARIF/JSON output provides interoperability but does not replace the native raw report.

### Engine and coverage boundary

- The open-source engine and community rules provide useful local analysis, but advanced interfile/interprocedural/proprietary capabilities differ by engine and product tier.
- Single-file analysis can miss flows that cross files, frameworks, generated code, configuration or runtime behavior.
- Rule quality and coverage vary by language, framework and source.
- A result's engine/ruleset/feature tier must therefore be retained alongside every Finding.

## What Semgrep contributes

- Fast syntax-aware source/configuration scanning.
- Human-readable rules that can be versioned and reviewed.
- Exact source spans, metavariables and rule metadata.
- Taint/dataflow trace structure.
- Structured scanner errors, skipped targets and skipped rules.
- Findings fingerprints and SARIF/JSON output.
- A strong primary static-analysis Facility for Code Ops and security review.
- A useful custom-rule path for THETECHGUY-specific source policies without writing a compiler front end.

## Important limitations for Ptah

- Rule match is a detector Claim, not proof of exploitability or business impact.
- Rule quality can produce false positives and false negatives.
- Language parsing, preprocessing, generated code, macros and framework behavior can limit accuracy.
- Open/community analysis can have materially less reach than advanced interfile/proprietary engines.
- Engine/rule updates can change findings on unchanged source.
- A skipped file, parse error or unsupported language can make a no-findings report misleading.
- Fingerprints may change as code/rule algorithms evolve and are not universal Finding identity.
- Autofix or suggested edits may be incomplete, unsafe or semantically wrong.
- Dependency reachability is analysis evidence, not runtime proof.
- Rule severity/confidence metadata reflects rule authorship and policy, not automatic Ptah acceptance.
- Semgrep Cloud/product services and proprietary rules cannot be mandatory public Ptah dependencies.
- Scanning proprietary source requires Workspace/privacy controls.

## Must not be inherited

- Semgrep check IDs/fingerprints as canonical Ptah Finding identity;
- community/open engine results presented as equivalent to advanced interfile analysis;
- no findings reported without skipped/error/coverage context;
- rule severity used directly as release policy;
- matched code span treated as proven exploit path;
- autofix applied automatically to protected source;
- third-party rules fetched/executed without source, licence, hash and review;
- proprietary/cloud service made mandatory;
- scan output used to replace Code Ops ownership or Sergeant review;
- changed findings after rule updates used to rewrite historical evidence.

## Integration decision

**ADOPT SEMGREP AS THE PRIMARY SOURCE-LEVEL STATIC ANALYSIS FACILITY; NORMALIZE ITS MATCHES, ERRORS AND SKIPS INTO PTAH SCAN, FINDING, CLAIM, EVIDENCE AND REVIEW CONTRACTS.**

Recommended Ptah role:

1. bind every scan to an immutable source Object/repository commit and defined path scope;
2. retain exact Semgrep binary/build, engine kind, ruleset source/digest/licence and configuration;
3. keep the native raw JSON/SARIF report as an immutable Artifact;
4. normalize matches into Finding Observations with exact source ranges and rule evidence;
5. retain dataflow traces, dependency information, errors, skipped files/rules and timeouts;
6. separate scanner severity, confidence, exploitability, impact and release policy;
7. correlate recurring findings without erasing independent rule/scanner disagreement;
8. route proposed fixes to Code Ops as patches and to Sergeant for independent proof;
9. re-scan after source/rule/engine changes as new report revisions;
10. permit alternate SAST engines without changing Ptah Finding identity.

## Native Ptah gap

Ptah must define:

- Source Scan Target and exact repository/Object revision;
- Scanner, Engine and Ruleset Revision;
- rule source/licence/hash/trust records;
- raw Scanner Report Artifact;
- Finding Observation and exact Source Range Evidence;
- dataflow/reachability evidence representation;
- parse error, skipped target/rule and coverage records;
- scanner fingerprint aliases and stable Finding correlation;
- severity, confidence, exploitability, impact and acceptance separation;
- suppression, exception, accepted-risk and expiry records;
- remediation proposal, patch, review and re-scan closure;
- privacy/audience scope for source and findings.

## Exit strategy

Ptah's source-scan and Finding contracts remain independent. Semgrep, CodeQL, compiler/static analyzers, language-specific tools or future scanners can contribute observations without changing source, Finding, Claim or Evidence identity.

## Validation required

1. Scan a pinned multi-language repository with a frozen ruleset and retain engine/rule/tool identity.
2. trigger local and cross-file vulnerabilities and show the capability difference between engine tiers.
3. introduce parse errors, unsupported files and timeouts and preserve them in coverage evidence.
4. compare JSON and SARIF with native field preservation.
5. update the ruleset with unchanged source and retain a new report revision.
6. correlate two rules finding the same source issue without discarding either observation.
7. validate one suggested autofix through Code Ops tests and Sergeant review before acceptance.
8. deny unreviewed remote/community rules.
9. prove a no-findings report includes exact scanned/skipped scope.
10. replace Semgrep without changing Ptah Finding identity.
