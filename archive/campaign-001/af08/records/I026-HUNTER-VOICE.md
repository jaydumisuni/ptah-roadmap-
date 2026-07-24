# I026 — Hunter Voice

Status: candidate record — paired private module evidence complete

Primary Archivist: `AF08-P05`
Independent Verifier: `AF08-V05`
Inspected: 2026-07-23

## Canonical source identity
- private parent source: `jaydumisuni/hunter`;
- branch: `master`;
- exact repository pin: `0c1e9154367e48afb807d4cf5ec6713df94c9ff0`;
- module role: Hunter speech input/output and self-hosted voice-service integration;
- private THETECHGUY source; no public reuse grant.

## Evidence and boundary
Voice is an I/O layer over Hunter's existing brain/context, with local STT, F5-TTS target and Edge TTS fallback. The verifier confirmed that voice models, reference audio, provider terms, latency and platform clients are separate evidence surfaces; spoken output is not Ptah authority.

## Bounded outcome
`accepted_for_archive_private_hunter_voice_module_with_model_audio_provider_privacy_and_io_boundaries`

Restrictions: keep private source/reference voice assets/secrets private; do not claim voice identity or ownership beyond approved assets; retain model/provider revisions and consent; do not let voice I/O alter Hunter/Ptah authority boundaries.

This outcome does not authorize implementation.