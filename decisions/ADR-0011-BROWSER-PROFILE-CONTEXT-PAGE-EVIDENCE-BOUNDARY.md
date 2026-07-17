# ADR-0011 — Browser Profile, Process, Context, Page and Evidence Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Phase:** 0A / WP08 browser and live-research closure

## Context

Ptah needs a browser that behaves like part of a capable operating environment:

- persistent logged-in sessions;
- isolated temporary sessions;
- interactive human control;
- programmatic automation;
- concurrent research and QA;
- downloads;
- screenshots, video and traces;
- source-grounded rendered extraction;
- crash/restart recovery;
- external adapters such as MCP;
- use by outside reasoning systems without embedding reasoning inside Ptah.

The inspected sources solve complementary parts:

- Playwright supplies browser process, Context, Page, locator, download and evidence machinery across Chromium, Firefox and WebKit.
- Playwright MCP supplies an external accessibility-snapshot tool adapter.
- Browser-Use supplies real-profile reuse, profile-cloning, persistent session, agent-oriented trajectory and production resource patterns.
- TurboWebFetch supplies concise single/batch rendered-retrieval contracts, JS rendering and parallel research, but currently starts and closes a browser for each fetch.
- internal Lumi and Hunter records contribute Transfer/Object landing, credential secrecy, optional-backend degradation and receipt rules.

No donor defines Ptah's Browser Profile ownership, Workspace isolation, Page identity, evidence, citation or research-result truth.

## Decision

Ptah will own separate backend-neutral contracts for:

1. Browser Provider;
2. Browser Binary/Engine;
3. Browser Profile;
4. Browser Process;
5. Browser Context;
6. Page/Tab;
7. Frame and Popup;
8. Navigation and Action;
9. Download;
10. Browser View and Evidence Artifact;
11. Rendered Retrieval Activity;
12. Live Research Result and Source Citation;
13. Challenge, Authentication and Human Completion;
14. browser resource pool, lease and recovery.

No Playwright, CDP, MCP, Browser-Use, nodriver or Chrome identifier becomes canonical Ptah identity.

---

# Browser Provider

A Browser Provider is a Node-attached Facility that supervises browser binaries/processes and exposes supported engines and capabilities.

```text
browser_provider_id
node_id
provider_type
supported_engines
installed_binaries
runtime_versions
profile_storage_classes
supported_extensions
network_capabilities
headless_and_headed_modes
resource_capacity
health
worker_generation
```

Provider types may include:

```text
local_native
oci_browser
remote_browser_service
application_provider_browser
existing_user_browser_bridge
```

The provider owns process launch, local paths, ports, OS integration and cleanup. Ptah owns identities, leases, Activities, Objects, privacy and receipts.

---

# Browser Binary and engine

A browser binary record contains:

```text
browser_binary_id
engine
product
version
build_revision
platform
architecture
executable_or_image_reference
source_and_signature
feature_capabilities
security_patch_state
```

Engines include Chromium, Firefox and WebKit. Browser/product/version differences are retained rather than hidden behind one generic compatibility claim.

---

# Browser Profile

A Browser Profile is durable user/browser identity and state.

```text
browser_profile_id
workspace_id_or_owner_reference
provider_compatibility
engine_and_product
storage_object_or_volume_reference
created_at
updated_at
lease_state
encryption_reference
privacy_class
extension_manifest_references
authentication_state_summary
retention_policy
```

Profile contents may include:

- cookies;
- local/session storage;
- IndexedDB;
- cache/history;
- saved permissions;
- certificates;
- extensions;
- browser settings;
- passkey/provider state where exportable;
- sensitive personal/account data.

## Profile rules

- mutable Profiles require an exclusive write lease;
- unrelated Workspaces/callers never share a Profile silently;
- profile cloning excludes lock, journal and transient process files;
- clones receive new identity and provenance;
- encryption and access control apply at rest;
- exported storage state is a derivative credential Artifact, not the complete Profile;
- Profile deletion/cleanup is a verified Activity;
- personal existing-browser attachment requires explicit caller consent and scoped capabilities.

---

# Browser Process

A Browser Process is one running browser backend instance.

```text
browser_process_id
provider_id
browser_binary_id
profile_id_or_ephemeral_profile
provider_process_reference
backend_endpoint_reference
worker_generation
started_at
state
resource_usage
```

States include:

```text
starting
ready
degraded
recovering
closing
closed
crashed
failed
```

One process may host many isolated ephemeral Contexts. A persistent mutable Profile normally has an exclusive compatible process/lease.

## Pooling

Ptah may maintain supervised warm browser processes. Pooling rules include:

- process ownership and exact generation;
- maximum Contexts/Pages/resources;
- Context isolation and cleanup tests;
- no profile/cookie/storage leakage across Workspaces;
- pressure-based scaling and shutdown;
- separate pools for unsafe browser flags or trust classes;
- owned-process termination only, never global process-name cleanup.

---

# Browser Context

A Browser Context is an isolated browser session within a Process.

```text
browser_context_id
browser_process_id
workspace_id
profile_or_storage_state_reference
context_type
created_at
state
locale_timezone_geolocation
proxy_and_network_reference
permissions
extension_state
page_ids
```

Context types include:

```text
ephemeral
persistent_profile
profile_clone
existing_browser_attachment
remote_provider_context
```

Context isolation is not assumed equivalent to VM/OS isolation. The provider advertises its isolation and network/file-system boundaries.

---

# Page, Frame and Popup

A Page/Tab record contains:

```text
page_id
browser_context_id
backend_page_reference
creation_cause
opener_page_id
initial_url
current_url
canonical_url_claim
navigation_epoch
state
title_claim
frame_ids
active_download_ids
```

Page states include:

```text
creating
loading
interactive
stable
waiting_for_user
challenged
crashed
closed
stale
unknown
```

A Frame has separate origin, URL, parent frame and backend reference. Cross-origin/frame restrictions and visibility are retained.

A Popup is a new Page linked to its opener and triggering operation.

## Epoch and stale references

Navigation, process reconnect or backend recreation advances Page/navigation generation. Locators, element references and frame references from an earlier incompatible generation are rejected or re-resolved from stable selector intent.

---

# Navigation and actions

Every navigation/action is a Ptah operation:

```text
operation_id
attempt_id
page_id
navigation_epoch
action_type
selector_intent_or_coordinates
requested_url_or_value
before_view_references
after_view_references
backend_acknowledgement
verification_state
```

Proof levels include:

```text
requested
page_created
navigation_started
response_received
dom_content_loaded
load_event
network_quiet_claim
interactive
stable_claim
action_acknowledged
state_change_observed
expected_state_verified
```

No lower level implies a higher one. Fixed sleeps alone are not page readiness proof.

---

# Browser Views

One Page may produce several competing Views:

```text
source_response
response_headers
raw_html
rendered_dom
accessibility_tree
visible_text
readability_article
markdown_derivative
screenshot
pdf
video
trace
console_log
network_log
har
storage_snapshot
```

Each View retains:

- Page/Context/Profile reference;
- capture time and navigation epoch;
- final URL and response references where applicable;
- producer/backend/version;
- content hash/Object ID;
- completeness and limitation claims;
- privacy/redaction class.

DOM, accessibility, visible pixels and response source can disagree. Ptah retains the disagreement.

---

# Downloads

A browser Download is a transfer handoff, not a completed file.

```text
download_id
page_id
trigger_operation_id
suggested_filename
source_url
response_headers
browser_temp_reference
transfer_activity_id
landing_object_id
state
```

States include:

```text
started
browser_receiving
handed_to_transfer
verifying
finalizing
completed
failed
cancelled
```

Downloads enter ADR-0006's Transfer/Object pipeline. Browser temporary paths and suggested names never define Object identity.

---

# Evidence and trace

Screenshots, video, trace, console, network, HAR, source and DOM snapshots are separate Artifacts.

A Browser Evidence bundle may reference all of them but does not merge their claims.

Trace/evidence records include:

```text
evidence_id
page_context_profile_activity_ids
capture_start_and_end
navigation_epochs
browser_binary_and_backend
artifact_ids
redaction_profile
coverage
limitations
```

Evidence may contain credentials, tokens, form data, account details and private content. Capture, retention, sharing and export are separately controlled.

---

# Rendered Retrieval Activity

A Rendered Retrieval Activity is optimized for reading one or more URLs rather than maintaining an interactive browser Session.

```text
retrieval_id
url_requests
retrieval_class
context_policy
parallelism
wait_conditions
output_view_types
source_evidence_requirements
rate_policy_reference
partial_result_policy
```

Retrieval classes include:

```text
plain_http_preferred
rendered_ephemeral
rendered_authenticated
interactive_continuation
batch_rendered
```

## TurboWebFetch adaptation

TurboWebFetch's single/batch contract and Readability/Markdown conversion are adapted over Ptah Browser pools.

Default implementation direction:

- reuse supervised browser Processes;
- create fresh isolated ephemeral Contexts for ordinary retrieval;
- use leased Profiles for authenticated retrieval;
- retain partial batch results;
- avoid process-per-fetch startup and global process cleanup;
- preserve source, DOM, accessibility, screenshot and network evidence;
- mark login/challenge/human-required state honestly.

---

# Live Research Result and citation

Ptah does not reason about which conclusion should be accepted. It records source-grounded research outputs for callers.

A Live Research Result contains:

```text
research_result_id
activity_id
query_or_request_reference
source_records
claim_records
citation_records
retrieval_times
coverage
conflicts
limitations
produced_view_and_artifact_ids
```

A source record includes:

```text
source_id
requested_url
final_url
canonical_url_claim
publisher_or_origin_claim
response_time
response_status
content_hashes
page_and_view_ids
access_class
```

A citation binds a claim/range/summary to exact source/View/Object references and capture time.

Research results remain claims. External callers/councils decide interpretation and acceptance.

---

# Authentication, challenges and human completion

States include:

```text
authentication_required
credentials_required
mfa_required
passkey_required
human_confirmation_required
captcha_or_interactive_challenge
access_restricted
paywall_or_subscription_required
permission_denied
completed_by_human
```

Ptah does not claim bypass capability or authorization. Caller/deployment permissions and website terms remain external constraints.

Credentials are opaque references. Cookies/storage/profile bytes are protected data, not ordinary telemetry.

A human may take control of an existing Page/Context, complete a challenge and return control. Handoff and resulting context generation are receipted.

---

# MCP, CLI and caller boundary

- Playwright MCP is an optional external adapter.
- Playwright CLI/skills, SDKs and direct UI are alternative adapters.
- Browser-Use may run as a caller/workload above Ptah.
- TurboWebFetch may remain an optional rendered-fetch adapter.
- Ptah native Browser contracts remain internal truth.
- Reasoning, agent prompts, model selection and research acceptance stay outside Ptah Core.

---

# Security and network boundary

Browser Providers enforce explicit deployment/caller network boundaries, including:

- approved Internet access;
- local/private network access class;
- redirect and DNS-rebinding protection in hosted contexts;
- proxy/certificate/credential references;
- downloads and file chooser roots;
- extension permissions;
- browser unsafe-flag profiles;
- CDP/WebSocket endpoint isolation.

Browser access is normally available, but one Workspace/caller cannot use the Browser Facility to cross another Workspace, Node management network or private credential boundary.

---

# Failure and recovery

Failure classes include:

```text
browser_process_crashed
context_closed
page_crashed
navigation_timeout
renderer_hung
profile_locked
profile_corrupt
backend_disconnected
download_interrupted
challenge_required
network_denied
resource_exhausted
```

Recovery rules:

1. advance Process/Context/Page generation;
2. reject stale backend/element references;
3. preserve completed evidence and partial batch results;
4. restore Profile state only from verified storage;
5. recreate ephemeral Contexts when safe;
6. do not replay form submissions, purchases, uploads or other non-idempotent actions blindly;
7. reconcile downloads through the Transfer Activity;
8. report reduced/unknown state when a Page cannot be restored exactly.

---

# Donor decisions

- **Playwright:** primary Browser Facility foundation.
- **Playwright MCP:** optional external adapter, not internal object model.
- **Browser-Use:** adapt profile/session/recovery/trajectory/resource patterns; agent layer remains external.
- **TurboWebFetch:** adapt rendered batch retrieval over Ptah's pooled browser architecture; not primary foundation.
- **internal Lumi/Hunter:** retain Transfer, secret, degradation and receipt rules; no dedicated browser provider credited.

---

# Consequences

## Positive

- Persistent login and isolated batch research coexist without profile leakage.
- Browser processes can be reused efficiently while Contexts remain Workspace-scoped.
- Human, SDK, MCP and external agent callers share one neutral contract.
- Rendered results retain exact source and evidence rather than only extracted text.
- Downloads use the existing Object/Transfer system.
- Browser crash/reconnect and stale-page behavior become explicit.
- Ptah can supply live Internet capability without becoming the reasoning council.

## Costs

- Browser Profile encryption/locking and lifecycle are security-sensitive.
- Process pools and Context isolation require conformance testing.
- Trace/video/network evidence can be large and private.
- Browser engines and website behavior change frequently.
- Source/citation and human-challenge flows require additional schemas/UI.
- Full exact recovery of arbitrary live Pages is often impossible and must be reported honestly.

## Do-not-break rule

> Never treat a browser process, profile directory, Context, Page, URL, locator, click acknowledgement, extracted Markdown, screenshot, download path or MCP session as universal Ptah truth. Profile ownership, Process, Context, Page generation, source Views, evidence, downloaded Objects and research claims have separate identities and guarantees.

---

# Required proof before freeze

1. Run multiple isolated Contexts concurrently without cookie/storage/profile leakage.
2. Lease, restart and safely reuse one persistent authenticated Profile.
3. Clone a Profile while excluding transient locks and retaining provenance.
4. Crash a browser process and reject stale Page/Frame/element references.
5. Resume safe read-only work but refuse blind replay of non-idempotent actions.
6. Run batch rendered retrieval through pooled Contexts and preserve partial failures.
7. Capture and correlate response source, DOM, accessibility, screenshot, video, trace, console and network Views.
8. Route browser downloads through Transfer/Object finalization and verify hashes.
9. Handoff to a human for MFA/challenge and return control with a new context generation.
10. Produce source/citation records bound to exact content hashes and capture times.
11. Expose the same Page through native SDK and MCP without leaking other Workspaces.
12. Replace TurboWebFetch/Browser-Use/Playwright adapter paths without changing public Browser identities.
