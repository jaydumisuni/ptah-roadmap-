# D028 — Android UiAutomator source

Status: candidate record — paired evidence complete

Primary Archivist: `AF07-P06`

Independent Verifier: `AF07-V06`

Inspected: 2026-07-23

## Canonical source identity

- canonical source: `android.googlesource.com/platform/frameworks/testing`;
- corroborating mirror: `aosp-mirror-neo/platform_frameworks_testing`;
- branch: `main`;
- exact inspected commit: `f9b3351f18ae617ea4debddce931a9381ab76a4c`;
- source licence: Apache-2.0 notices in AOSP source;
- repository role: legacy Android framework testing/UiAutomator source;
- activity status: dormant/historical; inspected head removes Espresso source and is not a modern standalone UiAutomator2 foundation.

## Primary evidence packet

The source is useful for historical Android UI hierarchy and testing concepts.

## Independent verification packet

Modern Android automation lives across AndroidX Test, platform APIs, Appium UiAutomator2 and device/OEM behaviour. This dormant source cannot establish current API support, compatibility or semantic-action reliability.

## Contradiction and supersession

The donor is accepted as historical source study only, not the primary current Android automation implementation.

## Bounded outcome

`accepted_for_archive_historical_aosp_ui_testing_source_with_dormancy_modern_androidx_and_compatibility_limits`

Allowed reuse: study Apache-licensed historical contracts and source lineage.

Restrictions: use current official APIs/dependencies for implementation; do not claim current Android/OEM compatibility; require exact device tests and post-condition read-back; do not treat hierarchy/action IDs as canonical Ptah identity.

This outcome does not authorize implementation.