# D061 — ZAP

Status: candidate record — paired evidence complete

Primary Archivist: `AF05-P06`

Independent Verifier: `AF05-V06`

Inspected: 2026-07-23

## Canonical source identity

- source: `zaproxy/zaproxy`;
- default branch: `main`;
- exact inspected commit: `58a4e041801ba690d268f9c886d7098a9cbbe70d`;
- root licence: Apache-2.0;
- repository role: intercepting proxy and web-application security scanner;
- archived: false.

## Primary evidence packet

ZAP is useful as a specialist web-security workload for passive and active scanning, proxy/browser integration, automation plans, findings and reports.

## Independent verification packet

Active scanning can modify targets and must require explicit authorization, scope, rate and cleanup Policy. Add-ons, browsers, scripts, rules and update feeds are separate trust surfaces. Findings are candidates that require reproduction and review; a scan cannot certify safety.

## Contradiction and supersession

ZAP may run inside Ptah but cannot define Ptah Core, authorization or security truth.

## Bounded outcome

`accepted_for_archive_apache_web_security_workload_with_active_scan_authorization_and_finding_limits`

Allowed reuse:

- run or wrap a pinned ZAP workload under an explicit target and authorization record;
- retain exact add-ons, rules, configuration, browser/proxy evidence, findings and reports.

Restrictions:

- preserve Apache notices and review add-ons and update feeds separately;
- prohibit active scanning without explicit authorized scope;
- do not treat findings or zero findings as accepted truth or release approval;
- verify cleanup and external effects independently.

This outcome does not authorize implementation.