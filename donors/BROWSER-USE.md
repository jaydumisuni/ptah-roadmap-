# Donor Record — Browser-Use

**Phase:** 0A / WP08  
**Status:** FIRST-PASS COMPLETE — AGENT-ORIENTED BROWSER SESSION AND RECOVERY DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/browser-use/browser-use
- Default branch: `main`
- Pinned commit: `950eb03617e67548d759c02beac1ad122c6b6458`
- Pinned package version: `0.13.6`
- Licence: MIT
- Runtime: Python 3.11+ with browser-use-core/harness and CDP/browser dependencies
- Classification: browser-agent interaction, profile, session, action loop and production-scaling donor
- Ptah targets: persistent browser connections, real Chrome profile reuse, browser event loops, recovery, structured state, remote browser adapters and evaluation patterns

## Files/components inspected

- `README.md`
- `pyproject.toml`
- `browser_use/browser/profile.py`
- browser profile locking/transient-file, extension, rendering, URL-validation and security option boundaries
- local/cloud browser and custom-tool relationships

## Verified capabilities and patterns

- Provides a Python library and CLI for browser tasks, form filling, data extraction and QA.
- Supports local/self-hosted use and optional hosted remote browsers.
- Can use existing real Chrome profiles with saved authentication.
- Browser profile code distinguishes transient lock/journal files that should not be copied into cloned temporary profiles.
- Defines browser arguments for headless, Docker, deterministic rendering, extension behavior and long-running background tabs.
- Includes profile and platform behavior across Linux, macOS and Windows.
- Supports custom tools and structured outputs around browser sessions.
- Supports parallel/scheduled browser tasks and production resource-management concerns.
- Has explicit URL validation helpers and browser configuration models.
- Exposes browser action/history patterns suitable for trajectory/evaluation records.
- Recognizes that Chrome memory use and parallel-agent scaling need active management.

## What Browser-Use completes

- Strong practical patterns for connecting to existing browsers and reusing profiles/cookies/extensions.
- Profile-cloning lessons, including exclusion of lock/journal/transient files.
- Long-running browser session/event-loop and recovery patterns beyond short test cases.
- Production resource, remote-browser and parallel-task considerations.
- Agent-facing structured action/history patterns useful for evaluation and replay.
- Browser abstraction and configuration ideas complementary to Playwright's lower-level API.

## Important limitations for Ptah

- Browser-Use is an agent product/library; its LLM, prompt, memory, decision loop and cloud identity are not Ptah responsibilities.
- Agent task history is not Ptah Activity or proof truth.
- Real browser profiles contain sensitive credentials, cookies, extensions and personal state.
- Profile copying while Chrome is active can fail or create inconsistent state.
- Several browser flags reduce security/isolation or ignore certificate errors and must never become safe defaults.
- Disabling site isolation/web security is unsuitable for shared or untrusted workloads.
- Hosted stealth, proxy rotation and CAPTCHA services are provider products, not required Ptah foundations.
- Browser-Use's browser/profile IDs remain backend-local.
- Model success claims/benchmarks do not prove Ptah Browser correctness.
- Agent action success does not prove the page reached the intended state.
- A profile connected from a personal browser must not be shared across unrelated Workspaces or callers.

## Must not be inherited

- Browser-Use's agent identity, LLM providers, system prompts, memory or policy as Ptah Core.
- hosted-cloud dependency or API key as mandatory architecture.
- `--disable-web-security`, ignored certificate errors or reduced site isolation as default Browser Profiles.
- personal Chrome profile copied or opened without explicit ownership, lease and encryption rules.
- Browser-Use action history used as the canonical Activity ledger.
- captcha/stealth behavior treated as authorization to bypass access controls or website terms.
- browser profile IDs/configuration exposed as Ptah's public schema.
- model benchmark claims promoted to Browser Facility proof.

## Integration decision

**ADAPT PROFILE, SESSION, RECOVERY, ACTION-HISTORY AND PRODUCTION-SCALING PATTERNS; HOST BROWSER-USE AS AN OPTIONAL CALLER/WORKLOAD.**

Playwright remains the primary Browser Facility foundation. Browser-Use may operate through Ptah's Browser adapter or run as a workload inside Ptah, while the reasoning/agent layer stays outside the core.

Useful adaptation areas:

- profile cloning with transient-file exclusion;
- connection to existing Chrome/CDP sessions;
- persistent browser/event-loop recovery;
- action/observation trajectory capture;
- resource/memory management for concurrent sessions;
- remote-browser provider abstraction;
- custom tool integration above native Browser contracts.

## Native Ptah gap

Ptah must define:

- Browser Profile ownership, encryption, lease and cloning rules;
- safe default browser flags and explicitly unsafe capability classes;
- existing-browser attachment consent and isolation;
- Process/Context/Page generations and reconnect state;
- trajectory records linked to Activities/receipts rather than agent memory;
- profile portability and extension compatibility;
- provider-neutral local/remote browser adapter;
- resource placement and pressure policies;
- challenge/human-completion states;
- caller-supplied reasoning/tool loops above the Browser Facility.

## Exit strategy

Browser-Use remains an optional caller/workload. Its profile and action patterns can be implemented natively or replaced without changing Ptah Browser identities.

## Validation required

1. Attach to an existing approved Chrome profile without affecting unrelated browser instances.
2. Clone a profile while excluding transient lock/journal files and verify cookie/extension scope.
3. Reject concurrent exclusive use of one mutable profile.
4. Exercise safe versus explicitly unsafe browser flags under separate capability profiles.
5. Restart a browser and reconnect an action loop while rejecting stale Page references.
6. Run several browser workloads under bounded RAM/CPU limits.
7. Record an action/observation trajectory without treating the agent's conclusion as proof.
8. Run Browser-Use as a workload through Ptah and remove it without changing the underlying Browser Session.
