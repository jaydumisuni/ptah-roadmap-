# Donor Record — Strix

**Phase:** 0A / Security and reproduction completion  
**Status:** FIRST-PASS COMPLETE — OPTIONAL AGENTIC PENTEST/VALIDATION WORKLOAD, NOT A CORE SECURITY AUTHORITY  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/usestrix/strix
- Default branch: `main`
- Pinned commit: `7d5a67d234bd3faef34d22be8c6f5a9607de41a3`
- Licence: Apache-2.0
- Activity: Active
- Primary language: Python
- Classification: autonomous multi-agent penetration-testing, exploit-validation, reporting and remediation-proposal workload donor
- Ptah targets: optional authorized offensive-validation workload, PoC/evidence schema, target scope, agent-tool isolation, run artifacts and independent review

## Files/components inspected

- `README.md`
- `LICENSE`
- `strix/tools/reporting/tool.py`
- current repository/commit activity
- documented Docker sandbox, LLM providers, targets, scan modes, HTTP/browser/shell/Python tools, reports and CI paths

## Verified capabilities and patterns

### Agentic security workload

- Strix uses autonomous AI agents to plan, investigate and validate security issues.
- Tooling includes HTTP interception, browser automation, shell/command execution, Python exploit development, reconnaissance, static/dynamic analysis and structured reporting.
- It supports local source, repository and black-box web targets.
- Multiple targets, custom instructions, diff-scoped reviews and non-interactive CI runs are supported.
- It depends on Docker plus an external/local LLM provider.
- The first run pulls a sandbox image and results are stored under run directories.

### Finding/report structure

- The reporting tool requires title, description, impact, target, technical analysis, PoC description, actual PoC code/payload, remediation steps, concrete evidence and exploitability assumptions.
- It validates CVE/CWE shapes and computes CVSS 3.1 from explicit metrics.
- Code locations retain relative file, start/end line, snippet and optional before/after fix material.
- Findings can retain endpoint, method, CVE, CWE, CVSS, severity, fix effort, agent identity and remediation/PR text.
- Duplicate checking can reject likely duplicate reports while retaining confidence/reason.
- Report persistence can fail independently from the tool's validation/result path.
- The tool documentation explicitly says a vulnerability report should be filed only for a concrete, fully verified issue with a working PoC.

### Agent and proof boundary

- Requiring PoC and evidence raises the evidence bar relative to a speculative agent statement.
- An agent-generated PoC, CVSS score, dedupe result or remediation remains a claim produced by the workload.
- The same model/toolchain can plan, exploit, report and propose a fix, so those outputs are not independent corroboration.
- Dynamic exploit attempts may alter real systems, data or availability.
- External LLMs and search/tool providers add confidentiality, prompt-injection, availability and cost dependencies.
- One-line remote installation and automatic image pulls require independent package/provenance controls.

## What Strix contributes

- A realistic autonomous offensive-security workload for Ptah isolation and Activity testing.
- Multi-agent planning and security-tool orchestration.
- Dynamic exploit validation and PoC-oriented reporting.
- Required evidence, assumptions, impact and remediation fields.
- CVSS breakdown and source-code location structure.
- Duplicate-detection and report-persistence lessons.
- CI/non-interactive and local/black-box target modes.
- A useful stress test for browser, terminal, network, credential, Workspace, plugin and evidence Facilities.

## Important limitations for Ptah

- Strix is an AI reasoning/workload product, not a deterministic scanner or Ptah Core component.
- Agent behavior depends on model, prompt, tools, provider, temperature/retries and external content.
- PoC generation can be wrong, incomplete, unsafe or overstate impact.
- Successful exploit behavior may be destructive, environment-specific or violate target authorization.
- A reported finding can share one agent/tool lineage with its evidence and remediation.
- Dedupe uses workload-local logic and can incorrectly merge distinct vulnerabilities or separate duplicates.
- CVSS computation depends on agent-supplied metrics.
- Docker sandboxing does not by itself constrain target network, external APIs, mounted source, credentials or Docker-host authority.
- Shell/browser/Python tools create a broad attack surface.
- Results and logs may contain source, credentials, tokens, exploit payloads, personal data and sensitive infrastructure information.
- External LLM/provider requests may expose target context and source.
- Agent-generated patches are proposals and cannot bypass Code Ops/Sergeant.
- Nonzero CI exit on findings is a product policy signal, not Ptah acceptance.
- Strix cannot be trusted to authorize its own targets or decide acceptable destructive actions.

## Must not be inherited

- Strix agent/session/report IDs as canonical Ptah identities;
- autonomous target discovery interpreted as permission to test;
- remote install script or mutable sandbox image used without pin/hash/SBOM/provenance;
- Docker container described as sufficient containment without host/network/credential controls;
- agent claim plus its own PoC counted as independent review;
- generated CVSS accepted without human/policy adjudication;
- generated fix or PR merged automatically;
- exploit attempts allowed against customer/production systems without explicit authorization and cleanup plan;
- external LLMs sent sensitive source/credentials without approved data policy;
- agent run completion reported as secure/safe;
- Strix made mandatory for security closure or release approval.

## Integration decision

**HOST STRIX ONLY AS AN OPTIONAL, EXPLICITLY AUTHORIZED OFFENSIVE-VALIDATION APPLICATION/WORKLOAD BEHIND PTAH ISOLATION, SECURITY-SCOPE, ACTIVITY, EVIDENCE AND REVIEW CONTRACTS.**

Recommended Ptah role:

1. an authorized human/security owner creates a bounded Security Test Authorization;
2. target, environment, accounts, exclusions, destructive-action class, rates, time and cleanup are fixed before execution;
3. Strix runs in gVisor/Kata/Firecracker/full-VM isolation selected by tools and target risk;
4. network egress, Docker/container authority, mounts, credentials and external LLM endpoints are explicitly scoped;
5. model/provider/prompt/tool/plugin/sandbox revisions are retained;
6. every shell/browser/HTTP/exploit action maps to a receipted Ptah Activity operation;
7. raw run logs, traffic, PoCs and reports become restricted immutable Artifacts;
8. findings are normalized as agent-originated Claims with named evidence/assumptions;
9. PoCs are independently re-run or validated in an approved environment;
10. generated fixes go to Code Ops and independent Sergeant/security review;
11. target cleanup and read-back are mandatory after active tests;
12. Strix can be removed without changing Ptah Finding/Evidence identity.

## Native Ptah gap

Ptah must define:

- agentic Security Workload and model/provider revision;
- Security Test Authorization and exact target scope;
- destructive-action and exploit class;
- tool/network/credential/Object/device grants;
- prompt/instruction and untrusted-input provenance;
- operation-level action/evidence receipts;
- Agent Claim versus independently validated Finding state;
- PoC Artifact, assumptions and replay/validation result;
- CVSS input/adjudication record;
- duplicate/correlation proposal and review;
- remediation proposal, patch owner and review chain;
- sensitive output/redaction/retention policy;
- cleanup/read-back and incident-stop records;
- stochastic repeatability/evaluation corpus.

## Exit strategy

Ptah's authorized security-workload contracts remain independent. Strix, human pentesters, ZAP, Nuclei, custom agents or future offensive-validation systems can produce Claims and Evidence without changing Target, Authorization, Finding or Review identities.

## Validation required

1. Run Strix only against an intentionally vulnerable isolated target with explicit authorization.
2. prove the workload cannot reach excluded networks, host Docker authority, unrelated Workspaces or undeclared credentials.
3. retain exact model/provider/prompt/tool/sandbox identity for the run.
4. compare repeated runs and retain stochastic differences.
5. independently replay one PoC and reject one unsupported agent claim.
6. compare agent CVSS with reviewer adjudication.
7. prevent duplicate logic from erasing distinct evidence.
8. route a generated fix through Code Ops tests and Sergeant review rather than auto-merge.
9. stop a harmful run, clean target state and prove cleanup/read-back.
10. replace Strix without identity loss.
