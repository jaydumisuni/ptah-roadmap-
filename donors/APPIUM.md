# Donor Record — Appium Core

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — CROSS-PLATFORM SEMANTIC AUTOMATION PROTOCOL HOST, NOT A DEVICE PROVIDER  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/appium/appium
- Default branch: `master`
- Pinned commit: `b9ad1f17125051494484e295c106019669e30530`
- Pinned package version: `3.5.2`
- Licence: Apache-2.0 for Appium core; package-specific exceptions such as `@appium/logger` must remain separately tracked
- Primary language/runtime: TypeScript/Node.js
- Activity: Active
- Classification: W3C WebDriver-compatible automation server, driver/plugin extension host and cross-platform semantic-control donor
- Ptah targets: `DEVICE-002`, `APP-002`, `APP-003`, `APP-004`, application-session commands, semantic element interaction, driver/plugin lifecycle and external protocol compatibility

## Files/components inspected

- `README.md`
- `packages/appium/package.json`
- `packages/base-driver/lib/protocol/protocol.ts`
- repository licence declarations

## Verified capabilities and patterns

### Modular core/driver separation

- Appium core cannot automate a platform by itself.
- Platform support is installed through separately versioned drivers.
- Plugins extend or override server behavior without changing the core.
- Driver and plugin installation/update/removal are managed through an extension CLI.
- Drivers may target Android, iOS, macOS, Windows and other platforms.

### Protocol and session host

- Exposes a W3C WebDriver-compatible HTTP API.
- Normalizes and validates session IDs, routes and request payloads.
- Separates no-session commands from commands requiring an active session.
- Validates required/optional command parameters and rejects malformed requests.
- Registers standard and extension routes from a method map.
- Dispatches commands to a selected driver through `executeCommand`/`execute`.
- Preserves driver cleanup authority for `deleteSession` rather than blindly proxying it.
- Supports legacy-protocol compatibility alongside W3C selection, though Ptah should prefer W3C.

### Cross-platform and hybrid automation

- Uses one protocol model for native, hybrid, mobile-web and desktop applications.
- Drivers may bridge native contexts and WebView/browser contexts.
- Language clients exist across Java, Python, Ruby, C# and other ecosystems.
- Appium Inspector provides a visual page-source/element-inspection workflow.

### Concurrency and extension lifecycle

- Supports multiple server processes and, depending on driver support, parallel sessions within one server.
- Installed drivers are enabled by default; plugins require explicit startup enablement.
- Safe driver updates avoid major-version changes unless an unsafe update is explicitly requested.
- Core package owns extension schemas, types and driver/plugin interfaces.

## What Appium completes

- A mature cross-platform semantic automation protocol and session model.
- Driver/plugin separation that aligns with Ptah provider-neutral Facilities.
- Element/action compatibility across native and web contexts.
- Existing clients and tooling useful as external Ptah adapters.
- Explicit session creation/deletion and driver-owned cleanup.
- A broad application-automation ecosystem for Android, iOS, macOS and Windows.

## Important limitations for Ptah

- Appium is designed primarily for test automation, not long-lived concurrent digital workspaces.
- WebDriver session ID is not a Ptah Device, Application Session, Activity, lease or proof identity.
- Core trusts installed drivers/plugins to implement powerful commands correctly.
- Extension installation from npm/other sources is a supply-chain and code-execution boundary.
- A driver may select the first available device unless exact capabilities are supplied.
- Command success generally reflects driver/protocol completion, not authoritative physical or visible-state proof.
- Driver-specific reset, install, permission, cleanup and concurrency semantics vary.
- Parallel session safety is driver-specific rather than guaranteed by core.
- HTTP server exposure requires authentication, TLS, network policy and multi-tenant isolation outside default Appium assumptions.
- Plugins can alter command behavior and therefore require exact enablement/provenance receipts.
- Legacy JSON Wire compatibility broadens complexity and should not define new Ptah contracts.
- Appium commands can expose screenshots, page sources, clipboard, logs and sensitive application data.
- Appium's extension home and installed package state are not Ptah Artifact or Facility identity.
- Node.js process/session state is not durable across host failure without Ptah orchestration.

## Must not be inherited

- WebDriver session ID used as Ptah Device/Application/Activity identity;
- first-device selection in a multi-device provider;
- driver/plugin installation from mutable package tags without hashes, SBOM and approval;
- all installed drivers automatically authorized for all workspaces;
- protocol success promoted to visible/semantic/authoritative result;
- driver-specific reset/cleanup behavior assumed universal;
- Appium server exposed without authentication, TLS and scoped capability policy;
- one semantic automation permission granting package install, files, shell, clipboard, input and device policy;
- legacy protocol compatibility embedded in native Ptah contracts;
- page source or element identifier assumed stable after UI generation changes;
- automatic retry of semantic actions after timeout/disconnect;
- driver/plugin logs treated as safe telemetry without redaction.

## Integration decision

**SUPPORT AS A MAJOR EXTERNAL PROTOCOL/FACILITY HOST AND DRIVER ECOSYSTEM; DO NOT MAKE APPIUM CORE THE PTAH ACTIVITY OR DEVICE CORE.**

Ptah should implement:

- an Appium Adapter Facility exposing selected W3C sessions to callers;
- driver/plugin installation as pinned, reviewed Facility Artifacts;
- mapping between Appium session IDs and Ptah Application/Device Sessions;
- exact device lease/fencing and provider ownership outside Appium;
- command receipts and post-action verification around driver calls.

Appium may run as a supervised service inside a Workspace/Node, with its HTTP endpoint private to Ptah or explicitly exported under policy.

## Native Ptah gap

Ptah must define:

- Application Session identity independent of WebDriver session;
- Device/desktop provider and exact target lease;
- driver/plugin Facility manifest, version, digest, source, licence, SBOM and health;
- session capability normalization and policy validation;
- command classification: read/observe, semantic input, application lifecycle, package/file/device mutation;
- operation/attempt/nonce/epoch correlation and durable receipts;
- semantic tree/view generation and stale-element handling;
- post-command display/semantic/authoritative verification;
- session restart/reconnect and driver-host failure recovery;
- capability-scoped authentication/TLS/network exposure;
- Artifact registration for screenshots, page sources, logs, recordings and reports;
- redaction and sensitive-data handling;
- conformance across UIAutomator2, XCUITest, mac2, Windows and future drivers;
- backend replacement without changing Ptah contracts.

## Exit strategy

The Semantic Application Facility remains independent of Appium. Native UIAutomator/Accessibility, XCUITest, Playwright-like desktop APIs, Windows UI Automation, TouchPilot-like providers or OEM/cloud automation services can implement the same Ptah semantic contracts. Appium remains a high-value compatibility adapter.

## Validation required

1. Pin and verify Appium core plus one driver/plugin set as immutable Facility Artifacts.
2. Create an Appium session only after acquiring the exact Ptah target lease.
3. Map session capabilities to a normalized Ptah Application Session and reject unknown/unsafe capability combinations.
4. Run parallel sessions on separate targets and prove no port/session/driver cross-talk.
5. Expire a lease and reject commands even if the Appium WebDriver session remains alive.
6. Kill/restart the Appium service and reconcile or close sessions without reissuing non-idempotent actions.
7. Reject stale element references after semantic-tree generation changes.
8. Verify an important click/type action through later semantic/display observation rather than HTTP success alone.
9. Restrict screenshots/page sources/clipboard/logs under sensitive-data policy.
10. Replace one Appium driver with a native provider while preserving Ptah Application Session semantics.
