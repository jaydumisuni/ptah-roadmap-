# Donor Record — FFmpeg and ffprobe

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — MULTIMEDIA STRUCTURE/TRANSFORM FOUNDATION CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/FFmpeg/FFmpeg
- Default branch: `master`
- Pinned commit: `8d394252d80d045bd5ad473f25e85dc55556105d`
- Licence: mainly LGPL, with optional GPL and other configuration-dependent components; exact build configuration determines distribution obligations.
- Activity: Active and mature
- Classification: Multimedia container/codec/probe/filter/transcode foundation
- Ptah targets: container/stream/track/chapter/packet/frame/subtitle metadata, thumbnails, waveforms, frame/audio extraction, transcode, remux, filter graphs and media verification

## Files/components inspected

- `README.md`
- `doc/ffprobe.texi`
- documented `libavformat`, `libavcodec`, `libavfilter`, `libavutil`, `libswresample`, `libswscale`, ffmpeg and ffprobe boundaries

## Verified capabilities and patterns

- FFmpeg provides libraries and tools for audio, video, subtitles and related metadata.
- `libavformat` handles containers, streaming protocols and I/O.
- `libavcodec` implements codecs.
- `libavfilter` executes connected filter graphs.
- `libswresample` handles audio resampling/mixing; `libswscale` handles scaling/color conversion.
- ffmpeg manipulates, converts and streams media.
- ffprobe gathers machine-readable or human-readable information about containers and their streams.
- ffprobe can emit nested sections through selectable writers, including JSON.
- Format/stream metadata tags are reported separately.
- ffprobe can show:
  - container format;
  - streams;
  - programs and stream groups;
  - chapters;
  - packets;
  - decoded frames and subtitles;
  - decoder logs;
  - errors;
  - packet/extradata payload hashes;
  - program/library versions;
  - pixel formats.
- Input intervals and stream selection allow bounded/sample probing.
- `-bitexact` reduces build-dependent output where supported.
- ffprobe can count packets/frames and inspect selected intervals.
- ffmpeg/ffprobe can operate over files or URLs/protocols, depending on build/configuration.
- The library split permits direct APIs or subprocess adapters.

## What FFmpeg/ffprobe completes

- A mature normalized multimedia container/stream inventory.
- Audio/video/subtitle/chapter/packet/frame child/view foundations.
- Codec/container metadata and exact program/library version reporting.
- Frame, thumbnail, waveform, audio-track and subtitle derivatives.
- Remux versus transcode distinction.
- Directed filter graphs suitable for deterministic transform recipes.
- The optional Video Export Pack backend needed by Creative Studio.
- Machine-readable JSON output for a neutral Ptah adapter.

## Important limitations for Ptah

- Exact supported codecs, protocols, filters, hardware accelerators and licence obligations depend on build configuration.
- GPL/nonfree/third-party codecs cannot be assumed in a public LGPL-compatible package.
- ffprobe format detection/probing can be ambiguous, slow or partial on malformed/truncated/streaming inputs.
- URL/protocol input expands SSRF/network attack surface and must be controlled separately from local Object probing.
- Media metadata may contain private GPS, device, title, author and application data.
- Packet/frame dumps can be enormous; full enumeration requires explicit limits and pagination/streaming.
- Decode/transcode of hostile media remains native-code attack surface requiring isolation and updates.
- Hardware-accelerated and software encoders can produce different bytes/quality.
- Lossy transcode can never preserve original content identity.
- Container duration/frame-rate/time-base values can be inconsistent or estimated.
- Seeking/interval starts are not always exact.
- ffmpeg process success does not prove visual/audio correctness, sync, loudness or semantic equivalence.
- `-bitexact` does not guarantee universal byte-identical output across different builds/dependencies/platforms.
- FFmpeg does not own editable Creative Studio project/layer/timeline state.
- ffprobe output fields and private data need versioned normalization rather than direct public exposure.
- The inspected master commit is not the stable release choice for Phase 0C.

## Must not be inherited

- Every network protocol enabled in an untrusted media worker.
- Build feature set/licence obligations left undocumented.
- ffprobe JSON used directly as the public Ptah media schema.
- Full packet/frame dump enabled without budgets.
- Transcoded/remuxed media retaining the original Object identity.
- Decoder/encoder exit code promoted to quality or sync acceptance.
- Metadata silently stripped, trusted or published.
- Hardware and software output assumed byte-equivalent.
- FFmpeg executed inside the long-lived control plane with broad host/device access.
- Creative Studio's procedural preview path described as complete FFmpeg/timeline integration before proof.

## Integration decision

**ADOPT FFPROBE AS THE PRIMARY MULTIMEDIA INVENTORY BACKEND AND FFMPEG AS THE PRIMARY MEDIA TRANSFORM/EXPORT BACKEND, BEHIND PTAH MEDIA CONTRACTS.**

Ptah should initially invoke pinned, feature-audited binaries in bounded provider processes. Direct library integration can follow only where it materially improves streaming or performance.

Creative Studio uses the same Media Objects/Activities rather than owning separate path-based media truth.

## Native Ptah gap

Ptah must define:

- container, program, stream group, stream/track, chapter, packet sample, frame sample and subtitle relationships;
- codec, profile, level, time base, duration, frame rate, channel layout, sample rate, pixel format, color/HDR and disposition fields;
- exact probe scope, analyzed interval and completeness/estimate state;
- metadata privacy/redaction and attached-picture/cover-art relationships;
- transform recipe distinguishing remux, lossless transform and lossy transcode;
- filter graph, encoder, quality/rate-control, hardware and deterministic seed/settings receipts;
- source-to-output timestamps and A/V sync verification;
- frame/thumbnail/contact-sheet/waveform/transcript/subtitle derivative identities;
- build configuration, library versions, enabled codecs/protocols/filters and licence record;
- CPU/GPU/memory/time/output budgets, cancellation and restart behavior;
- local Object versus explicitly authorized URL input policy;
- perceptual/functional comparison separate from byte identity.

## Exit strategy

Ptah's Media Domain Pack can support FFmpeg, GStreamer, platform codecs or specialist media libraries. Media Objects, stream relationships and transform recipes remain backend-neutral.

## Validation required

1. Probe representative video, audio, subtitle, multi-program, chaptered, variable-frame-rate, HDR and malformed inputs.
2. Register container/streams/chapters/attachments as typed children/views with exact probe scope and versions.
3. Generate thumbnails, contact sheets, waveforms, extracted tracks, subtitles and frame samples as hashed derivatives.
4. Remux without re-encoding and separately transcode with explicit lossy/lossless classification.
5. Verify A/V duration/sync, timestamps, loudness/levels and output readability rather than trusting exit code.
6. Bound packet/frame enumeration and decode time/memory/output.
7. Disable unneeded network protocols/decoders in hardened workers and report missing capabilities honestly.
8. Compare software and hardware outputs using byte and perceptual/functional evidence.
9. Record exact FFmpeg build configuration, enabled components, SBOM and licence obligations.
10. Use FFmpeg export from Creative Studio only after its project timeline maps to the same Media Activity/Artifact receipts.
