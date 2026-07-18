# Donor Record — OWASP ZAP

**Phase:** 0A / Security and reproduction completion  
**Status:** FIRST-PASS COMPLETE — PRIMARY DYNAMIC WEB/API SECURITY-TESTING DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/zaproxy/zaproxy
- Default branch: `main`
- Pinned commit: `eef487d8d65d91f182ef6f82a26b01376872c07b`
- Root licence: Apache-2.0; file/add-on level legacy notices and dependencies still require review
- Activity: Active
- Primary language: Java with scripts/add-ons
- Classification: intercepting proxy, passive scanner, active scanner, spider, fuzzer, automation and web-security evidence donor
- Ptah targets: authorized dynamic testing, target/scope/session identity, HTTP evidence, passive/active Finding classes, Automation Plans and report/re-test workflows

## Files/components inspected

- `README.md`
- `LICENSE`
- `docker/zap-baseline.py`
- `zap/src/main/java/org/parosproxy/paros/core/scanner/Alert.java`
- alert API/source locations and current repository activity
- documented Automation Framework, passive/active/manual/tool alert and report paths

## Verified capabilities and patterns

### Dynamic web testing

- ZAP operates as an HTTP/HTTPS proxy and can observe, replay and modify traffic.
- It can crawl/spider targets and process discovered requests through passive scanners.
- Active scan, fuzzing and scripts can send modified attack traffic to the target.
- Authenticated contexts, users, session handling and target scope can be configured.
- Docker/baseline and Automation Framework paths support repeatable CI-style plans and reports.

### Alert structure

- Alert sources are distinguished as active, passive, manual, tool or unknown.
- Alerts retain scanner/plugin identity, alert reference, risk, confidence, title, description, URI, method, parameter, attack, evidence, input vector, solution, references, CWE, WASC, tags and related HTTP history.
- Risk and confidence are separate; confidence includes false-positive and user-confirmed states.
- HTTP request/response history is important evidence but can contain secrets and personal data.
- Multiple alerts can describe related instances and may be merged for presentation without erasing original request evidence.

### Automation and gate policy

- Baseline automation separates target, spidering, passive-scan wait, alert filters, output summary and report jobs.
- Reports can be produced as HTML, Markdown, XML and JSON.
- Baseline exit states distinguish success, fail, warn and other execution failure.
- Rule configuration can classify alerts as INFO, IGNORE, WARN or FAIL.
- Alert filters can mark scoped instances false positive.
- Therefore the raw scanner alert, adjudication/suppression and CI/release gate remain distinct records.

### Authorization lesson

- Passive proxying can alter trust boundaries through TLS interception and capture credentials/cookies/tokens.
- Active scanning, fuzzing and exploit scripts can mutate data, trigger workflows, create load or damage systems.
- Legal/ethical authorization, target ownership, environment, timing, rate and destructive-action limits are prerequisites rather than notes.
- A valid target URL is not proof of authorization.

## What ZAP contributes

- Mature HTTP interception and traffic evidence.
- Passive and active web vulnerability scanners.
- Spider/crawler, authenticated context, fuzzer and scripting paths.
- Structured alerts with request, attack and evidence fields.
- Automation Plans and CI-oriented baseline behavior.
- Multiple report formats and API integration.
- A primary dynamic web/API Security Facility and complement to browser/research evidence.

## Important limitations for Ptah

- Coverage depends on crawl state, authentication, test data, SPA/browser behavior, API definitions and reachable routes.
- Passive scans only inspect observed traffic.
- Active scans can cause real side effects and are not safe for arbitrary production targets.
- Risk/confidence values are scanner policy, not business impact or release acceptance.
- False positives and false negatives remain possible.
- Request/response evidence can expose passwords, tokens, cookies and private data.
- Alert IDs/history IDs/session paths are ZAP-local identities.
- Add-ons and scan rules have independent versions, licences and maturity.
- A completed scan does not prove every route, role, state or business-logic path was tested.
- Automated scanners are weak at complex authorization and business-logic flaws without tailored workflows.
- Active exploit success can still be environment-specific and may not prove broader impact.
- Authentication/session configuration can expire or drift during a run.
- ZAP is not an isolation boundary; browser/proxy/scanner processes need scoped networking and credentials.
- CI exit status can be changed by rule policy and ignored alerts.

## Must not be inherited

- target URL interpreted as authorization;
- active scan run against production/customer systems without explicit scope and approval;
- raw cookies, tokens, passwords or sensitive bodies retained unredacted;
- ZAP alert/history/plugin IDs used as canonical Ptah Finding identity;
- scanner risk/confidence used directly as release policy;
- passive no-findings described as full dynamic coverage;
- ignored/false-positive alerts deleted from evidence;
- HTTP success or exploit response treated as durable business-impact proof without read-back;
- rule/add-on versions omitted;
- an Automation Plan treated as safe merely because it is valid YAML;
- CI exit code treated as independent security review.

## Integration decision

**ADOPT ZAP AS THE PRIMARY AUTHORIZED DYNAMIC WEB/API SCANNING FACILITY; WRAP EVERY RUN IN PTAH TARGET, SCOPE, AUTHORIZATION, NETWORK, CREDENTIAL, ACTIVITY, EVIDENCE AND REVIEW CONTRACTS.**

Recommended Ptah role:

1. create an explicit Security Test Authorization before any active/fuzz/exploit job;
2. bind targets to approved deployment/service Objects and environment revisions;
3. define included/excluded hosts, paths, methods, accounts, time window, rate and destructive-action class;
4. provision dedicated short-lived credentials/test data where possible;
5. isolate the ZAP process and restrict egress to approved targets;
6. retain Automation Plan, ZAP/add-on/rule versions and exact configuration;
7. store raw session/report/request evidence as restricted Artifacts with redaction;
8. normalize each alert source/instance into Finding Observations while preserving HTTP evidence;
9. keep filter/suppression/gate decisions separate and reviewable;
10. re-test remediation through a new authorized Activity and compare findings;
11. let Sergeant/security reviewers adjudicate impact and closure independently;
12. permit replacement DAST tools without identity loss.

## Native Ptah gap

Ptah must define:

- Security Test Authorization and approver;
- exact Target/Environment/Deployment revision;
- in-scope/out-of-scope hosts/routes/accounts/actions;
- passive, active, fuzz and exploit test classes;
- network/rate/time/destructive-action budgets;
- credential/test-data references and revocation;
- Scanner/Add-on/Rule/Automation Plan revision;
- HTTP Exchange and redacted evidence Artifact;
- Dynamic Finding Observation and exploit-validation state;
- suppression/false-positive/in-progress/gate policy records;
- coverage and untested-route/role/state records;
- remediation/re-test comparison;
- emergency stop, cleanup and external side-effect receipts.

## Exit strategy

Ptah dynamic-security contracts remain independent. ZAP, Burp-compatible tools, Nuclei, custom Playwright tests, API test frameworks or human pentesting can contribute observations without changing Target, Authorization, Finding or Evidence identity.

## Validation required

1. Run passive-only and active scans against an intentionally vulnerable isolated target.
2. prove active operations cannot reach excluded hosts/paths or exceed rate budgets.
3. rotate/expire credentials mid-run and retain coverage/authentication loss.
4. capture and redact tokens/cookies while preserving request evidence.
5. mark one alert false positive and preserve original evidence, authority and reason.
6. compare raw alert risk/confidence with independent impact adjudication.
7. exercise routes requiring roles, SPA actions and API definitions and record gaps.
8. stop a destructive/unsafe test and perform cleanup/read-back.
9. remediate and run a new scan without rewriting the original result.
10. replace ZAP without identity loss.
