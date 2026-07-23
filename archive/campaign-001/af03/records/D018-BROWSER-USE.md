# D018 — browser-use

Status: candidate record — paired evidence complete

Primary Archivist: `AF03-P07`

Independent Verifier: `AF03-V07`

Inspected: 2026-07-23

## Canonical source identity

- source: `browser-use/browser-use`;
- default branch: `main`;
- exact inspected commit: `96ec5dc1378d26f7dd155df0cef9d6c3e32752dc`;
- root licence: MIT;
- archived: false.

## Primary evidence packet

browser-use is an open-source Python library and CLI for model-directed browser interaction. It supports browser navigation, clicking, typing, form completion, structured extraction, QA workflows, custom tools and multiple model providers.

Useful Ptah donor concepts include:

- separating browser control from the coordinating model or application;
- explicit task, tool and model/provider configuration;
- browser action histories and structured outputs;
- custom tool registration and repeatable automation;
- distinguishing local/open-source execution from hosted browser and agent services.

## Independent verification packet

The verifier confirmed:

- the inspected public source is MIT licensed;
- operation commonly depends on an LLM API, browser binaries, browser profiles and websites outside the repository;
- the README separately promotes Browser Use Cloud, hosted agents, optimized hosted models, cloud browsers, stealth, proxies, captcha solving, integrations, persistent filesystem and memory;
- browser actions can cause real external effects, so action acknowledgement or model confidence cannot establish post-condition success or authorization;
- benchmark and leaderboard claims are separate evidence sets and cannot be treated as universal reliability guarantees;
- website changes, anti-bot controls, authentication, personal data and model behavior remain unstable external surfaces.

## Contradiction and supersession

The donor pool classified browser-use as a browser and live-research donor. Current evidence supports an optional agent/browser workload adapter, but not replacing Ptah’s deterministic Browser Provider, evidence, approval, privacy or post-condition contracts.

No frozen Ptah browser or authority decision is superseded. Model-directed browsing remains caller/application logic using Ptah resources, not intelligence owned by Ptah Core.

## Bounded outcome

`accepted_for_archive_mit_agent_browser_adapter_with_model_and_external_effect_restrictions`

Allowed reuse:

- study or adapt the MIT-licensed local library/CLI behind a replaceable workload adapter;
- retain exact task, model, tool, browser, page, action, screenshot, output and failure evidence;
- use it for bounded research, QA or automation under caller-supplied authority.

Restrictions:

- preserve MIT notices and separately review browser binaries, models, providers, cloud browsers, proxies, captcha services and integrations;
- do not treat hosted Browser Use capabilities as present in the public repository;
- require explicit approval and post-condition evidence for consequential external actions;
- do not expose credentials, personal data or private sessions without configured Grants and privacy policy;
- do not make model output, benchmark claims or browser action completion Ptah truth or acceptance authority;
- do not make browser-use Ptah’s mandatory Browser Provider.

This outcome does not authorize implementation.