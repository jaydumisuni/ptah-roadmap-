# D039 — FFmpeg

Status: candidate record — paired evidence complete

Primary Archivist: `AF06-P02`

Independent Verifier: `AF06-V02`

Inspected: 2026-07-23

## Canonical source identity

- source: `FFmpeg/FFmpeg`;
- default branch: `master`;
- exact inspected commit: `9347affa3dc3aa35e90661a4a7564328f3db7972`;
- default combined licence: LGPL-2.1-or-later;
- optional GPL/version3/external-library configuration can change effective binary licence;
- repository role: multimedia probing, decoding, encoding, filtering and streaming toolkit;
- archived: false.

## Primary evidence packet

FFmpeg can support media probes, thumbnails, recordings, frame/waveform Views, controlled conversion and stream handling.

## Independent verification packet

The verifier confirmed that configure flags and external libraries materially alter licensing. Codec/container support is build-dependent. Successful decode or duration reporting may still be partial for corrupt or truncated media, and transcoding creates new Artifacts rather than modifying canonical source bytes.

## Contradiction and supersession

FFmpeg remains a media Provider/workload, not Ptah Core or a universal completeness oracle.

## Bounded outcome

`accepted_for_archive_media_provider_with_build_specific_lgpl_gpl_codec_and_coverage_boundaries`

Allowed reuse:

- run a pinned, inventoried FFmpeg build behind Ptah media Provider boundaries;
- retain exact configuration, libraries, codecs, source digest, command, output and limitations.

Restrictions:

- determine effective licence from the exact build; do not assume generic LGPL after enabling GPL/version3/external components;
- preserve source bytes and register transformations as new Artifacts/Revisions;
- do not claim complete duration or coverage for malformed, unsupported or partial media;
- resource-limit heavy transcodes and keep unrelated Activities runnable.

This outcome does not authorize implementation.