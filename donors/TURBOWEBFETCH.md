# Donor Record — TurboWebFetch

**Phase:** 0A / WP08  
**Status:** FIRST-PASS COMPLETE — CANONICAL REPOSITORY RESOLVED, RENDERED BATCH-RETRIEVAL DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/aza-ali/turbowebfetch
- Default branch: `main`
- Pinned commit: `fa18a9f9db1e1640ff6111176ec49aa88ea211f4`
- Pinned package version: `1.1.0`
- Licence: MIT
- Runtime: Node.js MCP server plus Python/nodriver Chrome fetcher
- Classification: real-browser rendered content retrieval and concurrent batch-fetch implementation donor
- Ptah targets: `BROWSE-002`, batch research, JavaScript-rendered extraction, MCP fetch contracts, browser challenge state and rendered text/Markdown/HTML Views

## Files/components inspected

- `README.md`
- `package.json`
- `src/index.ts`
- `python/fetcher.py`
- environment validation, process cleanup, concurrency, nodriver, human-behavior and content-extraction boundaries

## Verified capabilities and patterns

- Runs real Chrome rather than plain HTTP fetch.
- Exposes `fetch` and `fetch_batch` through MCP.
- Supports text, Markdown and HTML output.
- Runs several URLs concurrently in separate browser processes; the documented default maximum is fourteen.
- Uses a Node MCP process to launch Python fetch workers.
- Uses nodriver, Readability and Markdownify.
- Detects/handles some broad JavaScript/browser challenge flows and can retry in headed/human-like mode.
- Implements operation timeouts for navigation, evaluation and DOM serialization.
- Uses random local debugging ports to reduce parallel collision.
- Creates a temporary user-data directory when no profile is provided.
- Validates and can recreate its Python virtual environment and dependencies.
- Implements periodic orphan Chrome cleanup using process inspection.
- Applies per-domain rate limiting and documents that it is not intended for high-volume harvesting.
- Explicitly states that each fetch is isolated, the browser closes and cookies/state do not persist.

## What TurboWebFetch completes

- A concise MCP contract for rendered single and batch retrieval.
- Real-browser extraction when plain HTTP returns empty client-rendered shells.
- Practical concurrent multi-source research behavior.
- Readability/Markdown conversion patterns.
- Browser challenge, slow-load and explicit-wait states.
- Environment self-check/repair and orphan-process cleanup lessons.
- Evidence that batch research can be a specialized Browser Facility operation rather than one Page at a time.

## Important limitations for Ptah

- Each request starts and closes a browser/process, causing documented startup latency and high memory use.
- No persistent authentication, cookies, profile ownership or interactive continuation exists by default.
- Browser process cleanup uses platform process-list matching and `SIGKILL`, which is unsafe as a general multi-tenant lifecycle manager.
- One cleanup strategy can kill long-running headless Chrome processes older than five minutes and therefore risks affecting non-TurboWebFetch workloads if process classification is imperfect.
- Temporary browser profiles are implementation state rather than durable Browser Profiles.
- Content extraction collapses rich page state into text/Markdown/HTML without a native DOM/network/source evidence graph.
- Challenge-handling and human-like behavior do not authorize bypassing paywalls, access controls or site terms.
- The fetcher advertises Cloudflare/DataDome handling but capability varies by site and cannot be treated as guaranteed.
- URL/network safety, redirect/DNS behavior and internal-network access require a stronger deployment boundary.
- Browser startup, extraction and shutdown are one coarse operation with limited interactive recovery.
- Result success does not prove completeness, source authority or citation quality.
- Chrome/nodriver and Python environment patching create dependency/version risk.

## Must not be inherited

- one new browser process per request as Ptah's primary Browser architecture.
- global process-name/age cleanup or blind `SIGKILL` across a shared Node.
- challenge handling treated as permission to circumvent restricted access.
- result text treated as complete source or research proof.
- temporary profile/debug-port IDs as canonical Browser identity.
- MCP fetch result used as the only evidence record.
- direct caller URLs allowed to reach unapproved private/internal network destinations in hosted deployments.
- Google Chrome-only requirement embedded in Ptah's generic Browser contract.
- no-cookie/no-session limitation carried into interactive Browser Profiles.

## Integration decision

**ADAPT AS A RENDERED BATCH-RETRIEVAL FACILITY ON TOP OF PTAH'S PLAYWRIGHT BROWSER POOL; DO NOT USE AS THE PRIMARY BROWSER FOUNDATION.**

Ptah should preserve the useful external contract and extraction flow while replacing process-per-fetch behavior with:

1. reusable supervised browser processes;
2. isolated ephemeral Contexts for ordinary batch fetches;
3. leased persistent Profiles/Contexts for authenticated retrieval;
4. Ptah-native process ownership rather than process-list cleanup;
5. source-response, DOM, accessibility, screenshot and network evidence;
6. bounded parallel scheduling and resource-aware placement;
7. rendered-result Objects/Views with citations and limitations.

TurboWebFetch itself may remain an optional MCP/workload adapter.

## Native Ptah gap

Ptah must define:

- batch retrieval request and result schemas;
- Browser Process/Context pool and ownership;
- ephemeral versus persistent/authenticated retrieval classes;
- allowed-network/redirect/DNS/SSRF boundary;
- per-domain concurrency/rate policy as caller/deployment configuration;
- rendered content View linked to exact URL, response, DOM and capture time;
- screenshots/network/console/trace evidence;
- completeness/challenge/login/human-required states;
- source/citation identity and canonical/final URL;
- process crash/retry and partial-batch results;
- resource accounting and backpressure;
- dependency/runtime pinning and clean exit path.

## Exit strategy

Ptah's rendered retrieval contract remains implementable with Playwright, TurboWebFetch, Browser-Use, plain HTTP or other browser engines. TurboWebFetch MCP and nodriver details remain adapter metadata.

## Validation required

1. Fetch several JavaScript-heavy pages concurrently through reusable isolated Contexts.
2. Compare process-per-request and pooled-context memory/latency under the same result contract.
3. Preserve partial batch results when one page times out or requires human verification.
4. Fetch authenticated content only through an explicitly leased Profile and keep cookies secret.
5. Retain final URL, response status, source HTML, rendered DOM, accessibility and screenshot Views.
6. Reject unapproved private/internal network destinations in hosted mode.
7. Kill only the exact owned browser process/generation and never another workload's browser.
8. Mark login, CAPTCHA, paywall/restricted-access and incomplete extraction honestly.
9. Replace TurboWebFetch with native Playwright retrieval without changing public result identity.
