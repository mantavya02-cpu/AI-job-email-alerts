from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

from .config import (
    OLLAMA_BASE_URL,
    OLLAMA_MIN_FIT_SCORE,
    OLLAMA_MODEL,
    PROFILE_NOTES_FILE,
)


def get_env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def ollama_is_configured() -> bool:
    return bool(get_env("OLLAMA_API_KEY"))


def load_profile_notes(profile_notes_path: str = str(PROFILE_NOTES_FILE)) -> str:
    path = Path(profile_notes_path)
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore").strip()


def build_job_prompt(job: dict[str, str], profile_notes: str) -> str:
    description = (job.get("description") or "")[:4000]
    return (
        "You are a recruiting assistant scoring job fit for a candidate.\n"
        "Use the profile notes as the source of truth.\n"
        "Return only valid JSON with keys fit_score, should_save, reason.\n"
        "fit_score must be an integer from 0 to 10.\n"
        "Healthcare, life sciences, pharma, biotech, and health tech roles are the TOP priority — give them +3.\n"
        "Jobs at ClearView, Humana, Biogen, Novartis, or Vertex are also prioritized — give them +2.\n"
        "should_save must be true if the job is a reasonable match — err on the side of inclusion.\n"
        "Set should_save to false ONLY if the job is clearly irrelevant, requires skills the candidate lacks, "
        "or explicitly states no H1B/visa sponsorship (phrases like 'no sponsorship', 'must be a US citizen', "
        "'we do not sponsor', 'sponsorship not available').\n"
        "reason must be one short sentence.\n\n"
        f"Profile notes:\n{profile_notes}\n\n"
        f"Job title: {job.get('title', '')}\n"
        f"Company: {job.get('company', '')}\n"
        f"Location: {job.get('location', '')}\n"
        f"Posted at: {job.get('posted_at', '')}\n"
        f"Description:\n{description}\n"
    )


def extract_json_object(text: str) -> dict[str, object] | None:
    if not text:
        return None

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        return None

    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None


def score_job_with_ollama(job: dict[str, str], profile_notes: str) -> dict[str, str] | None:
    api_key = get_env("OLLAMA_API_KEY")
    if not api_key:
        return None

    base_url = get_env("OLLAMA_BASE_URL", OLLAMA_BASE_URL).rstrip("/")
    model = get_env("OLLAMA_MODEL", OLLAMA_MODEL)
    payload = {
        "model": model,
        "stream": False,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a precise recruiting assistant. "
                    "Only return valid JSON and do not include markdown fences."
                ),
            },
            {
                "role": "user",
                "content": build_job_prompt(job=job, profile_notes=profile_notes),
            },
        ],
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url}/api/chat",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            response_payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None

    message = response_payload.get("message") or {}
    content = str(message.get("content") or "")
    parsed = extract_json_object(content)
    if parsed is None:
        return None

    fit_score = parsed.get("fit_score")
    should_save = parsed.get("should_save")
    reason = str(parsed.get("reason") or "").strip()

    try:
        fit_score_int = max(0, min(10, int(fit_score)))
    except (TypeError, ValueError):
        return None

    should_save_bool = bool(should_save)
    return {
        "ollama_fit_score": str(fit_score_int),
        "ollama_should_save": "true" if should_save_bool else "false",
        "ollama_reason": reason,
    }


def rerank_jobs_with_ollama(
    job_list: list[dict[str, str]],
    shortlist_size: int,
    minimum_fit_score: int = OLLAMA_MIN_FIT_SCORE,
) -> list[dict[str, str]]:
    if not job_list or not ollama_is_configured():
        return job_list

    profile_notes = load_profile_notes()
    if not profile_notes:
        return job_list

    shortlist = job_list[:shortlist_size]
    remainder = job_list[shortlist_size:]
    reranked: list[dict[str, str]] = []

    for job in shortlist:
        ollama_result = score_job_with_ollama(job=job, profile_notes=profile_notes)
        if ollama_result is None:
            reranked.append(job)
            continue

        enriched_job = dict(job)
        enriched_job.update(ollama_result)
        ai_score = int(enriched_job.get("ollama_fit_score", "0") or 0)
        if enriched_job.get("ollama_should_save") == "true" and ai_score >= minimum_fit_score:
            reranked.append(enriched_job)

    reranked.sort(
        key=lambda job: (
            -int(job.get("ollama_fit_score", "0") or 0),
            -int(job.get("fit_score", "0") or 0),
            job.get("posted_at") == "",
            job.get("posted_at", ""),
            job.get("company", "").lower(),
        ),
    )
    return reranked + remainder


def split_jobs_with_ollama(
    job_list: list[dict[str, str]],
    shortlist_size: int,
    minimum_fit_score: int = OLLAMA_MIN_FIT_SCORE,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    if not job_list:
        return [], []

    shortlist = job_list[:shortlist_size]
    if not ollama_is_configured():
        return shortlist, []

    profile_notes = load_profile_notes()
    if not profile_notes:
        return shortlist, []

    approved: list[dict[str, str]] = []
    archived: list[dict[str, str]] = []

    for job in shortlist:
        ollama_result = score_job_with_ollama(job=job, profile_notes=profile_notes)
        if ollama_result is None:
            approved.append(job)
            continue

        enriched_job = dict(job)
        enriched_job.update(ollama_result)
        ai_score = int(enriched_job.get("ollama_fit_score", "0") or 0)

        if enriched_job.get("ollama_should_save") == "true" and ai_score >= minimum_fit_score:
            approved.append(enriched_job)
        else:
            archived.append(enriched_job)

    approved.sort(
        key=lambda job: (
            -int(job.get("ollama_fit_score", "0") or 0),
            -int(job.get("fit_score", "0") or 0),
            job.get("posted_at") == "",
            job.get("posted_at", ""),
            job.get("company", "").lower(),
        ),
    )
    archived.sort(
        key=lambda job: (
            -int(job.get("fit_score", "0") or 0),
            job.get("posted_at") == "",
            job.get("posted_at", ""),
            job.get("company", "").lower(),
        ),
    )
    return approved, archived
