from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Callable

Rule = Callable[[dict[str, Any]], tuple[bool, str]]
SECRET_KEYS = {"password", "secret", "token", "private_key", "credential_value", "api_key"}


def _walk(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield f"{path}.{key}", key, child
            yield from _walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _walk(child, f"{path}[{index}]")


def no_raw_secret(payload: dict[str, Any]) -> tuple[bool, str]:
    for path, key, value in _walk(payload):
        if key.lower() in SECRET_KEYS and value not in (None, "", "REDACTED"):
            return False, f"raw secret-like value at {path}"
    return True, "no raw secret-like values"


def current_generation(payload: dict[str, Any]) -> tuple[bool, str]:
    expected = payload.get("expected_generation")
    observed = payload.get("observed_generation")
    ok = isinstance(expected, int) and observed == expected
    return ok, f"expected={expected!r} observed={observed!r}"


def current_fence(payload: dict[str, Any]) -> tuple[bool, str]:
    expected = payload.get("expected_fence_token")
    observed = payload.get("observed_fence_token")
    ok = isinstance(expected, int) and observed == expected
    return ok, f"expected={expected!r} observed={observed!r}"


def retry_attempt_unique(payload: dict[str, Any]) -> tuple[bool, str]:
    attempts = payload.get("attempt_refs")
    ok = isinstance(attempts, list) and len(attempts) == len(set(attempts)) and len(attempts) >= 1
    return ok, "attempt identities must be present and unique"


def acknowledgement_not_verification(payload: dict[str, Any]) -> tuple[bool, str]:
    acknowledged = payload.get("acknowledged") is True
    verified = payload.get("verified") is True
    evidence = payload.get("verification_evidence_refs")
    ok = not verified or (acknowledged and isinstance(evidence, list) and len(evidence) > 0)
    return ok, "verified success requires evidence beyond acknowledgement"


def exact_citation(payload: dict[str, Any]) -> tuple[bool, str]:
    required = ("source_revision_ref", "range", "digest")
    ok = all(payload.get(key) not in (None, "") for key in required)
    return ok, "citation requires exact revision, range and digest"


def accepted_risk_current(payload: dict[str, Any]) -> tuple[bool, str]:
    raw = payload.get("expires_at")
    if not isinstance(raw, str):
        return False, "expires_at missing"
    try:
        expiry = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return False, "expires_at invalid"
    return expiry > datetime.now(timezone.utc), f"expires_at={expiry.isoformat()}"


def independent_reproduction(payload: dict[str, Any]) -> tuple[bool, str]:
    original = payload.get("original_environment_ref")
    reproduced = payload.get("reproduction_environment_ref")
    attempts = payload.get("attempt_refs")
    cache_shared = payload.get("shared_mutable_cache") is True
    ok = original and reproduced and original != reproduced and isinstance(attempts, list) and len(set(attempts)) == len(attempts) and not cache_shared
    return bool(ok), "reproduction requires distinct environment, unique Attempts and no shared mutable cache"


RULES: dict[str, Rule] = {
    "no_raw_secret": no_raw_secret,
    "current_generation": current_generation,
    "current_fence": current_fence,
    "retry_attempt_unique": retry_attempt_unique,
    "acknowledgement_not_verification": acknowledgement_not_verification,
    "exact_citation": exact_citation,
    "accepted_risk_current": accepted_risk_current,
    "independent_reproduction": independent_reproduction,
}


def evaluate(name: str, payload: dict[str, Any]) -> tuple[bool, str]:
    rule = RULES.get(name)
    if rule is None:
        return False, f"unknown semantic rule {name!r}"
    return rule(payload)
