# ADR-0026 — Application, Browser, Semantic UI and Human Shell Boundary

**Status:** ACCEPTED  
**Date:** 2026-07-19

## Context

Ptah must run and recover applications, browsers and graphical surfaces; expose semantic and visual interaction safely; and give humans a direct responsive Workspace Shell. Mature backends expose useful process, window, browser-target, element-handle and UI-state mechanics, but those identifiers and status models are unstable and often collapse acknowledgement, presentation and functional truth.

Without a fixed WP09 boundary, implementation would be forced to invent or conflate:

- Application versus executable/package/path identity;
- install acknowledgement versus verified installed state;
- Session, Process, Window, Display and application readiness;
- Browser Binary, Profile, Process, Context, Page, Frame, Popup and Navigation;
- download event versus accepted bytes/Object truth;
- challenge resolution versus credential/identity-provider authority;
- Selector, Target, fresh Target Result and backend element handle;
- input acknowledgement versus verified postcondition;
- human/automation control ownership and stale fences;
- Shell layout/projection versus canonical runtime state;
- desktop, tablet and phone presentation behavior;
- checkpoint bytes versus functional recovery;
- public evidence versus private profile, clipboard, text, screenshot and trace data.

## Decision

Adopt WP09 catalog `urn:ptah:schema-catalog:application:0.1.0` and its candidate boundary.

### Application

- stable Application plus immutable Revision;
- target-specific Compatibility;
- separate Installation lifecycle and verification;
- Application Session bound to canonical `runtime.process` and exact Provider/materialization generations;
- Window and Window Observation separate from Session/readiness;
- Display Session and Display Observation separate from Window/application function;
- Checkpoint component and Recovery Verification separate from checkpoint integrity/compatibility and runtime restore.

### Browser

- Binary and immutable Binary Revision;
- Profile and immutable Profile Revision with explicit privacy, storage and writable-sharing policy;
- Process, Context, Page, Frame and Popup identities;
- immutable Navigation revisions;
- Download integrated with WP06 Transfer and WP03 Content/Object truth;
- Challenge plus immutable Challenge State, with automation fencing for human/external completion;
- Browser Evidence Bundle preserving multiple evidence classes;
- Browser Checkpoint and Recovery Verification with new generations and live authentication/function checks.

### Semantic UI

- Context, immutable Snapshot, Node Snapshot and Event;
- immutable Selector and durable Target;
- fresh, generation-bound Target Result;
- Action, physical Action Attempt linked to canonical WP02 Attempt, and verified Action Result;
- Visual Evidence as bounded evidence, not universal truth;
- explicit ambiguity/staleness invalidation and reacquisition;
- canonical `runtime.lease`/fencing for human and automation control;
- provider ACK distinct from post-condition success;
- explicit fallback method and assurance reduction.

### Human Shell

- Client, Session and Client Observation;
- Panel Type, Panel and Panel Binding;
- Layout Profile, immutable Layout Revision and View State;
- Projection and derived responsive projection;
- Control Transfer quiescing/fencing old authority before new Lease/fence issuance;
- Shell presentation never canonical runtime truth;
- disconnect/background/panel closure never implicit runtime stop;
- accessibility, localization, safe-area and low-bandwidth behavior as conformance requirements.

### Cross-cutting

- paths, package IDs, PIDs, window/surface/browser/element/panel IDs remain scoped Aliases;
- backend replacement preserves stable identity and creates new Compatibility, Provider bindings, generations, Snapshots, Target Results and Attempts;
- profile, cookies, credentials, clipboard, semantic text/value, screenshots, video, traces, logs and client caches carry explicit audience/privacy/redaction/retention policy;
- negative, stale, ambiguous, challenged, failed, partial and inconclusive outcomes remain immutable evidence.

## Consequences

### Positive

- Application and Browser adapters can be replaced without changing Ptah identity.
- UI automation cannot silently act on stale or ambiguous targets.
- human takeover and return to automation are safely fenced.
- Browser downloads and recovered sessions cannot bypass existing transfer/object/recovery proof.
- mobile and desktop Shells share one runtime contract while presenting different derived layouts.
- implementation teams receive exact readiness, recovery, privacy, accessibility and postcondition gates.

### Cost

- More typed records and generation correlations are required than backend-native handles/status fields.
- Providers must expose enough evidence to separate readiness, acknowledgement and postcondition truth.
- Some legacy UI logs and saved sessions remain observation-only or inconclusive.
- Accessibility and responsive behavior require dedicated fixtures and conformance.

## Rejected alternatives

1. **Use process/window/browser target IDs as canonical identity** — unstable across restart, reconnect and backend replacement.
2. **Treat visible pixels as application readiness** — display and function are different claims.
3. **Use browser profile/process/page as one session object** — destroys persistence, isolation and recovery boundaries.
4. **Treat download-complete browser event as Object truth** — bypasses byte/digest/Location verification.
5. **Treat element handles as durable targets** — stale and backend-specific.
6. **Treat provider click ACK as success** — does not prove intended effect.
7. **Allow automatic hidden fallback to coordinates/keystrokes** — hides assurance loss and increases wrong-target risk.
8. **Use Shell panel/layout state as runtime truth** — UI disconnects and projections would corrupt real work state.
9. **Let human and automation control concurrently without canonical Lease/fence** — split-brain mutation risk.
10. **Treat accessibility/responsive behavior as later polish** — would require architecture changes after implementation.

## Acceptance evidence

- 51 unique schema URNs and 18 unique lifecycle machines;
- explicit reuse of canonical Process, Lease, recovery, execution, Object/evidence and Transfer families;
- 37 cross-machine invariants;
- directional migration/backend-replacement record;
- 92 positive/negative/adversarial scenarios with typed error codes;
- consolidated structural, lifecycle, semantic, privacy, accessibility and replacement safety net;
- final consistency review passed.

## Constraint

This decision authorizes candidate contract use only. It does not select Playwright, CDP, WebDriver, Appium, remote-display, native-runtime or Shell framework dependencies, and it does not authorize runtime implementation. Executable conformance remains WP13 work; implementation begins only after Phase 0C approval.
