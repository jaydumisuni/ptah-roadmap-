# WP11 Consolidated Safety Net

WP11 passes only when offline structural validation, lifecycle validation and semantic checks all agree.

## Required checks

- every catalog path resolves without network access;
- every schema `$id`, schema name and entity kind is unique;
- lifecycle states and transitions are reachable and namespaced;
- Placement Candidate cannot satisfy Placement Decision or Admission Decision;
- expired capacity, health, Lease, grant or generation evidence is rejected;
- Reservation and Consumption remain separate;
- every retry or migration execution uses new WP02 Attempt identity;
- silent isolation downgrade is rejected;
- stale fences and split-brain holders are rejected;
- raw secrets are rejected in all records, logs, evidence and fixtures;
- secret delivery cannot satisfy cleanup verification;
- public network exposure requires explicit grant and audience;
- Device access requires exact connection epoch and Device Lease;
- read-only filesystem grants cannot mutate;
- checkpoint integrity cannot satisfy functional recovery;
- target verification precedes migration cutover and source cleanup;
- forced, partial, failed and uncertain outcomes remain visible;
- backend replacement advances generation and fence while preserving stable Ptah identity.

Executable enforcement is implemented by WP13; this file freezes expected semantics now.
