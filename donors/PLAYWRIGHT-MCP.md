# Donor Record — Playwright MCP

**Phase:** 0A / WP08  
**Status:** FIRST-PASS COMPLETE — EXTERNAL BROWSER TOOL ADAPTER DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/microsoft/playwright-mcp
- Default branch: `main`
- Pinned commit: `55679f5f3d4b4f3e2534ec0ce2fc5683ba2eaf3f`
- Licence: Apache-2.0
- Classification: Model Context Protocol adapter over Playwright
- Ptah targets: external Browser tool contracts, accessibility snapshots, normalized actions and interoperable caller access

## Files/components inspected

- `README.md`
- documented MCP versus CLI distinction
- accessibility snapshot/action model
- client installation/configuration examples
- Playwright foundation relationship

## Verified capabilities and patterns

- Exposes Playwright browser automation through MCP.
- Uses structured accessibility snapshots instead of requiring screenshots or visual models.
- Supplies element references for deterministic actions such as click and type.
- Supports navigation, form filling, screenshots, network mocking and storage operations.
- Maintains persistent browser state suitable for iterative agent loops.
- Explicitly distinguishes rich persistent MCP workflows from more token-efficient CLI/skills for coding agents.
- Can be consumed by many independent MCP clients.

## What Playwright MCP completes

- A standard external adapter for AI/caller browser control.
- A useful normalized accessibility snapshot/tool contract.
- Interoperability with existing MCP clients.
- A donor for Browser Facility tool granularity and descriptions.
- Evidence that different callers may prefer CLI/skill or MCP surfaces over the same Browser backend.

## Important limitations for Ptah

- MCP is an adapter protocol, not Ptah's internal Browser/Profile/Context/Page model.
- Element references are snapshot/backend-local and can become stale.
- Accessibility snapshots are not complete visual or source truth.
- Exposing every tool gives broad browser authority, including storage and network actions.
- Client configuration does not provide Ptah lease, Workspace, credential or proof semantics.
- Large accessibility trees and tool schemas can consume significant caller context.
- MCP session continuity does not prove browser process, Context or Page recovery.
- Playwright MCP does not own research citations, source authority or Artifact registration.

## Must not be inherited

- MCP tool/ref IDs as canonical Ptah identity.
- MCP as Ptah's internal Event or Activity transport.
- wildcard exposure of all Browser capabilities to every caller.
- accessibility action acknowledgement promoted to intended outcome.
- browser credentials/storage exposed through generic MCP resource calls.
- one MCP server instance shared across unrelated Workspaces without isolation.
- Playwright MCP's tool schemas frozen as the only Browser API.

## Integration decision

**SUPPORT AS AN EXTERNAL ADAPTER OVER PTAH'S NATIVE BROWSER FACILITY.**

Ptah should expose approved Browser Profile/Context/Page operations through an MCP adapter when useful, while preserving native contracts underneath.

CLI/skill, SDK and direct human UI adapters may expose the same operations differently.

## Native Ptah gap

Ptah must define:

- mapping from MCP session/tools/refs to stable Browser/Profile/Context/Page identities;
- caller identity, Workspace and capability scope;
- element/snapshot generation and stale-reference handling;
- credential/storage redaction;
- download/evidence Object references;
- tool receipts and proof levels;
- server restart and browser-state reconciliation;
- per-caller rate/resource limits;
- alternative CLI/SDK adapters.

## Exit strategy

MCP remains one optional adapter. Ptah Browser contracts can be exposed through CLI, SDK, UI, WebSocket or future protocols without changing internal identities.

## Validation required

1. Expose one approved Context/Page through MCP without revealing other Profiles or Workspaces.
2. Reject stale accessibility element references after navigation.
3. Scope network, storage, download and input capabilities independently.
4. Restart the MCP adapter without falsely claiming browser continuity.
5. Run the same Browser operation through MCP and native SDK with one Activity identity.
6. Prove sensitive cookies/storage state never enter ordinary tool responses or logs.
