# Donor Record — E2B Desktop

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — GRAPHICAL ENVIRONMENT DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/e2b-dev/desktop
- Default branch: `main`
- Pinned commit: `e4800ef873cacc0eeb91770a419b77de0ea26903`
- Licence: Apache-2.0
- Activity: Active at the inspected pin
- Classification: Graphical desktop and application-runtime completion donor
- Ptah targets: Linux graphical workspace, application launch, remote display, input and screenshots

## Files/components inspected

- `README.md`
- `LICENSE`
- Python and JavaScript SDK examples
- desktop template relationship
- streaming, window, mouse, keyboard, screenshot, file-open and command surfaces

## Verified capabilities and patterns

- Isolated customizable Linux/Xfce desktop sandbox.
- Desktop or individual-window streaming.
- Optional stream authentication and view-only links.
- Application launch and window discovery.
- Mouse, keyboard, drag, scroll and key-combination control.
- Screenshots, file opening and ordinary command execution.
- Python and JavaScript SDK surfaces.
- Customizable desktop template.

## What E2B Desktop completes

- It adds the graphical computer/application world missing from ordinary coding sandboxes.
- It demonstrates a practical split between sandbox lifecycle, graphical desktop template and desktop-control SDK.
- It provides useful normalized operations for applications, windows, input and screenshots.

## Important limitations

- The inspected README says only one stream can run at a time; Ptah must support multiple concurrent application and display activities where the backend permits.
- It is built on E2B Sandbox and normally requires an E2B API key.
- It is Linux/Xfce oriented and does not solve Windows, macOS, Android or device-specific display.
- Stream lifetime, reconnect, recording, artifact registration and session recovery are not the complete Ptah model.
- Pixel/coordinate input is not a semantic UI model.

## Must not be inherited

- A single-stream universal restriction.
- E2B-hosted infrastructure as mandatory.
- Linux desktop as the only application runtime.
- Desktop control tied directly to one provider's sandbox identity.
- Screenshots or streams that are not registered as Ptah objects/artifacts.

## Integration decision

**ADAPT SDK AND TEMPLATE PATTERNS; OPTIONAL PROVIDER/WORKLOAD.**

E2B Desktop is a completion donor for `APP-002`, `UI-001` and remote-display/application contracts. It is not the universal Ptah Application Facility.

## Native Ptah gap

Ptah must own:

- application-session and display-stream contracts;
- concurrent display/activity model;
- stream reconnect and recording;
- window/application identity and provenance;
- platform-specific adapters;
- object/artifact registration;
- semantic action layers where available;
- provider-neutral auth and transport.

## Exit strategy

Guacamole-style gateways, native remote desktop, browser-native apps and platform-specific adapters must remain interchangeable behind Ptah's application/display contract.

## Validation required

- Launch two independent graphical applications without blocking terminals or background jobs.
- Reconnect to a running display session.
- Capture screenshot and recording artifacts with source activity identity.
- Prove optional E2B Desktop use without making E2B mandatory.
