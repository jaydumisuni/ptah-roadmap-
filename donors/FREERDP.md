# Donor Record — FreeRDP

**Phase:** 0A / WP07B  
**Status:** FIRST-PASS COMPLETE — PRIMARY RDP CLIENT/LIBRARY DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/FreeRDP/FreeRDP
- Default branch: `master`
- Pinned commit: `7310b73581594b09c2db895b7b8e840144c444e6`
- Licence: Apache-2.0
- Classification: Remote Desktop Protocol implementation and Windows display/input/channel donor
- Ptah targets: `APP-003`, Windows VM/native Node display, RDP session presentation, audio, clipboard, drive/device channels and browser-gateway integration

## Files/components inspected

- `README.md`
- build/CI/security references
- protocol and API documentation entry points
- Guacamole's FreeRDP dependency boundary from the related donor pass

## Verified capabilities and patterns

- Implements Microsoft's Remote Desktop Protocol as an open, cross-platform client/library stack.
- Builds on several operating systems and architectures.
- Provides a programmatic API in addition to command-line clients.
- Serves as the RDP backend used by Apache Guacamole.
- Tracks Microsoft Open Specifications and protocol reference documentation.
- Supports display, keyboard/mouse and RDP virtual-channel concepts through the broader project.
- Can connect from non-Windows Nodes to Windows hosts/VMs.

## What FreeRDP completes

- An Apache-licensed RDP implementation for Windows VM/native-host presentation.
- A lower-level library/backend beneath Guacamole rather than requiring one gateway product.
- Cross-platform native RDP client possibilities.
- Protocol/channel separation needed for display, input, clipboard, audio and redirected resources.
- A clean exit path from proprietary RDP client dependencies.

## Important limitations for Ptah

- FreeRDP is a client/protocol implementation, not a Windows VM, native Node or Application Provider.
- RDP connection success does not prove desktop login, application launch or expected state.
- RDP virtual channels may expose clipboard, drives, printers, smartcards, audio and devices; each has a distinct risk profile.
- Credential, certificate and server-identity validation must be deployment-scoped.
- Full desktop RDP does not provide semantic Windows UI elements.
- Session reconnection behavior depends on the Windows host and account/session configuration.
- A captured RDP frame/recording is visual evidence, not functional verification.
- The protocol/library feature surface and build options affect capability availability.
- Multi-monitor, GPU and codec behavior require exact host/client proof.

## Must not be inherited

- RDP session/channel IDs as canonical Ptah Application Session identity.
- disabled certificate validation or silent trust-on-first-use in production.
- credentials stored in command lines, URLs, logs or public recipes.
- all virtual channels enabled under one generic remote-display permission.
- connection/login status promoted to application readiness.
- arbitrary host targets reachable through the RDP adapter.
- full-desktop pixels treated as semantic UI truth.

## Integration decision

**WRAP FREERDP AS THE PRIMARY RDP PROTOCOL BACKEND, DIRECTLY OR THROUGH GUACAMOLE.**

Ptah owns the target Windows Provider/Application Session, approved endpoint, short-lived credential references, display/input/channel permissions, recordings and receipts.

Use paths:

1. Guacamole RDP backend for browser access;
2. native FreeRDP client/library adapter where lower latency or richer client integration is useful;
3. RDP only when the Windows host explicitly advertises it.

## Native Ptah gap

Ptah must define:

- RDP endpoint and server-identity record;
- scoped credential/certificate references;
- display, input and virtual-channel capability matrix;
- Session/logon/reconnect state separate from Application Session;
- first-frame and login-ready receipts;
- recording/privacy/retention metadata;
- network isolation and approved-target mapping;
- semantic Windows UI adapter independent of RDP pixels;
- backend/library version and build-feature record;
- alternate gateway/client path.

## Exit strategy

Ptah's Windows display contract remains implementable through FreeRDP, Guacamole, Microsoft clients, VNC, WebRTC or platform-native streaming. FreeRDP IDs and channel details remain adapter metadata.

## Validation required

1. Connect to approved Windows VM and native Node endpoints with certificate/server-identity validation.
2. Distinguish TCP/RDP connected, authenticated/logged in, first frame and target-application visible states.
3. Permission clipboard, drive, audio, printer and device channels independently.
4. Reconnect to the same Windows user session after browser/client interruption.
5. Reject stale credentials, unapproved endpoints and certificate mismatch.
6. Record a session and link the protected recording Artifact to exact Session/Activity IDs.
7. Compare direct FreeRDP and Guacamole paths under the same Ptah display contract.
8. Keep Windows semantic automation independent from RDP presentation.
