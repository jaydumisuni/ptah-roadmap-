# D019 — TurboWebFetch

Status: candidate record — paired evidence complete

Primary Archivist: `AF04-P09`

Independent Verifier: `AF04-V09`

Inspected: 2026-07-23

## Canonical source identity

- source: `aza-ali/turbowebfetch`;
- default branch: `main`;
- exact inspected commit: `fa18a9f9db1e1640ff6111176ec49aa88ea211f4`;
- root licence: MIT;
- repository role: local MCP real-browser rendered-content fetcher;
- archived: false.

## Primary evidence packet

TurboWebFetch runs real Chrome instances for JavaScript-rendered content, exposes single and batch fetch tools, and documents up to fourteen parallel browser processes. It is useful as an implementation-pattern donor for browser-backed retrieval and batch research.

## Independent verification packet

The verifier confirmed that the tool requires Google Chrome, adds roughly five-to-ten seconds per page, uses about 200–400 MB per browser, does not handle login-required content or interactive CAPTCHAs, and is rate-limited rather than designed for bulk scraping. It explicitly limits use to content the operator has the right to access.

## Contradiction and supersession

The canonical repository is now resolved. The donor-pool limitations around browser startup, authentication, memory, latency and interaction remain materially valid. TurboWebFetch is not the primary Ptah Browser Facility foundation.

## Bounded outcome

`accepted_for_archive_mit_real_browser_retrieval_pattern_with_authentication_resource_and_lawful_access_limits`

Allowed reuse:

- study or adapt real-browser retrieval, MCP exposure and bounded batch-fetch patterns;
- use only under caller-supplied lawful-access Policy and retained browser/result evidence;
- consider selected patterns inside a persistent Ptah Browser Provider rather than adopting the lifecycle wholesale.

Restrictions:

- preserve MIT notices and review Chrome, Python, Node and MCP dependencies separately;
- do not claim authenticated, interactive or CAPTCHA-protected coverage;
- do not use challenge handling to bypass access controls, paywalls or site terms;
- do not launch unbounded browsers or hide startup, memory and failure costs;
- do not make TurboWebFetch Ptah's primary Browser identity, authority or mandatory service.

This outcome does not authorize implementation.