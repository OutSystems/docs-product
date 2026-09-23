#!/usr/bin/env python3
"""Shared owner-resolution helpers for image target collectors.

Used by validate-screenshots/scripts/collect_targets.py,
validate-svgs/scripts/collect_targets.py, and
.github/scripts/image-target-grouping/plan_targets.py, so screenshot and
SVG handling stay in lockstep instead of drifting apart.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Bumped when the on-disk validation record layout changes. A validation record written under a
# different schema is discarded rather than migrated — it only costs a
# re-validation, and migration code for a cache is never worth its bugs.
RECORD_SCHEMA = 1


def file_sha256(path: Path) -> str | None:
    try:
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return None


def git_blob_sha1(path: Path) -> str | None:
    """Git's blob object id: sha1(b"blob <len>\\0" + content).

    Deliberately the same hash space GitHub's REST API exposes as `sha` on
    `pulls/N/files[]` and `git/trees` entries, so the workflow's pre-checkout
    cache gate and this post-checkout collector agree on a file without
    anyone having to clone the repo first. That is the whole reason the
    validation cache keys on this rather than on `file_sha256`, which stays
    where it is for byte-identical duplicate detection.

    Not a security hash; collisions are irrelevant for a cache key.
    """
    try:
        size = path.stat().st_size
        h = hashlib.sha1(b"blob %d\0" % size)
        read = 0
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
                read += len(chunk)
    except OSError:
        return None
    if read != size:
        # The file changed under us between stat and read, so the length
        # prefix no longer matches the content. Report "unknown" instead of a
        # hash that would be wrong: a miss costs a re-validation, a wrong hash
        # would silently pin a stale verdict.
        return None
    return h.hexdigest()


def load_validation_record(path: str | None) -> dict:
    """The restored validation record's entries, or `{}` when unusable.

    Every failure mode — unset path, missing file, truncated JSON, a schema
    from another version — degrades to "nothing is cached". That costs a
    re-validation and can never produce a wrong verdict, which is the only
    acceptable direction for a cache to fail in.
    """
    if not path:
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        return {}
    if not isinstance(data, dict) or data.get("schema") != RECORD_SCHEMA:
        return {}
    entries = data.get("entries")
    return entries if isinstance(entries, dict) else {}


def repo_relpath(path: Path, root: Path | None) -> str:
    """Repo-relative POSIX path — the validation record's key space.

    Falls back to the absolute path when `path` is outside `root`, which is
    workspace-specific and so can only ever miss. Deliberate: the alternative
    fallback of a bare basename would let two same-named files in different
    directories share a cache entry.
    """
    resolved = Path(path).resolve()
    if root is not None:
        try:
            return resolved.relative_to(Path(root).resolve()).as_posix()
        except ValueError:
            pass
    return resolved.as_posix()


def record_hit(entries: dict, rel: str, blob_sha: str | None) -> dict | None:
    """The validation record entry for `rel`, but only if recorded at exactly `blob_sha`.

    A file with no entry, a changed hash, or an unreadable hash is a miss.
    """
    if not blob_sha:
        return None
    entry = entries.get(rel)
    if not isinstance(entry, dict) or entry.get("hash") != blob_sha:
        return None
    return entry


# Every skip or re-run the cache decides gets one of these reasons, and the
# same string is used by the pre-checkout gate, the post-checkout filter, the
# collectors, and the job summary. Grep a run's logs for a path and you get
# the same vocabulary back whichever layer made the call.
CACHE_REASONS = {
    "hit": "unchanged since it last passed",
    "never-validated": "never validated by this skill",
    "content-changed": "content changed since it last passed",
    "rubric-changed": "the skill, rubric, checkers, or model changed",
    "unreadable": "file could not be read, so it could not be matched",
    "expired": "last validated too long ago",
    "not-cached-yet": "nothing recorded for this skill yet (first run)",
    "disabled": "cache not switched on for this skill",
}


def cache_decision(
    entries: dict,
    rel: str,
    blob_sha: str | None,
    *,
    skill_version: str | None = None,
    max_age_days: int | None = None,
    now: datetime | None = None,
    record_present: bool = True,
) -> dict:
    """Whether `rel` can be skipped, and — always — why.

    Returns `{cached, reason, detail, entry}`. `reason` is a key of
    CACHE_REASONS; `detail` is a one-line human explanation safe to print in a
    workflow log. Callers must log `detail` for *every* file, hit or miss:
    a cache that silently skips work is one nobody can debug.

    `skill_version` identifies the thing that produced the verdict — the skill
    definition, its rubric and checker scripts, the model, and a manual epoch,
    hashed together. An entry recorded under different skill_version is not
    trustworthy and is re-validated.

    That comparison is deliberately made *here*, against a restored validation record,
    rather than by baking the skill_version into the cache key. Keying on it would
    also work, but the old validation record would then be unreachable and the log could
    only ever say "cold cache" — this way every affected file can say exactly
    which version replaced which.
    """
    def out(cached, reason, detail, entry=None):
        return {"cached": cached, "reason": reason, "detail": detail, "entry": entry}

    if not record_present:
        return out(False, "not-cached-yet", CACHE_REASONS["not-cached-yet"])
    if not blob_sha:
        return out(False, "unreadable", CACHE_REASONS["unreadable"])

    entry = entries.get(rel)
    if not isinstance(entry, dict):
        return out(False, "never-validated", CACHE_REASONS["never-validated"])

    # Checked before the content hash on purpose: when the skill changes,
    # every file re-runs, and saying so on every line makes it obvious from
    # the log that the cause is global rather than something about this file.
    recorded_sem = entry.get("skill_version")
    if skill_version is not None and recorded_sem != skill_version:
        return out(
            False,
            "rubric-changed",
            f"validated by a different skill version "
            f"({_short(recorded_sem)} -> {_short(skill_version)})",
        )

    recorded = entry.get("hash")
    if recorded != blob_sha:
        when = entry.get("validated_at") or "an earlier run"
        return out(
            False,
            "content-changed",
            f"content changed since {when} ({_short(recorded)} -> {_short(blob_sha)})",
        )

    when = entry.get("validated_at")
    if max_age_days is not None and when:
        age = _age_days(when, now)
        if age is not None and age > max_age_days:
            return out(
                False,
                "expired",
                f"last passed {age}d ago at {when}, past the {max_age_days}d max age",
            )

    verdict = entry.get("verdict", "clean")
    findings = entry.get("findings") or []
    suffix = (
        f", re-emitting {len(findings)} cached finding(s)"
        if verdict == "findings" and findings
        else ""
    )
    return out(
        True,
        "hit",
        f"unchanged since {when or 'its last pass'} (run {entry.get('run_id', '?')}){suffix}",
        entry,
    )


def format_decision_line(rel: str, decision: dict, width: int = 0) -> str:
    """One log line for one file's cache decision.

    Shared so the pre-checkout gate, the post-checkout filter and the
    collectors all print the same thing. The gate runs before the repo exists
    on disk and so cannot import this module from the working tree — it
    fetches this file through the GitHub API, the same trick the workflow
    already uses for the skill file. Keep this function dependency-free.
    """
    marker = "⏭️ " if decision.get("cached") else "▶️ "
    return f"{marker} {rel.ljust(width)} — {decision.get('detail', '')}".rstrip()


def summary_table(skill: str, rows: list[tuple[str, dict]]) -> str:
    """A GitHub job-summary table of every cache decision, counts first.

    `rows` is [(repo-relative path, decision)]. Rendered into
    $GITHUB_STEP_SUMMARY so the answer to "why was this skipped?" is on the
    run page without opening step logs.
    """
    skipped = sum(1 for _, d in rows if d.get("cached"))
    total = len(rows)
    out = [
        f"### {skill} — cache decisions",
        "",
        f"**{skipped} of {total} target(s) skipped (cache), {total - skipped} validated**",
        "",
        "| File | Decision | Why | Last validated | Run |",
        "| --- | --- | --- | --- | --- |",
    ]
    for rel, decision in rows:
        entry = decision.get("entry") or {}
        verdict = "skipped" if decision.get("cached") else "validated"
        out.append(
            f"| `{rel}` | {verdict} | {decision.get('reason', '?')}: "
            f"{decision.get('detail', '')} | {entry.get('validated_at', '—')} "
            f"| {entry.get('run_id', '—')} |"
        )
    return "\n".join(out) + "\n"


def annotate_cache(
    entries: list[dict],
    *,
    repo_root: Path | None = None,
    record_path: str | None = None,
    skill_version: str | None = None,
    max_age_days: int | None = None,
    log: bool = True,
) -> list[tuple[str, dict]]:
    """Tag each collector entry with its cache decision, in place.

    Adds `blob_sha`, `cached`, `cache_reason` and `cache_detail` to every
    entry, and returns `[(rel, decision)]` for the job summary.

    **Entries are never dropped.** Duplicate detection in the skills is
    set-scoped — it groups the whole target set by `sha256` — so it must still
    see every target, cached or not. Only the expensive per-image work
    (the vision read and the checker scripts) is skipped on a hit.

    Logs every decision to **stderr**: stdout carries the JSON the skill
    parses, so anything written there would corrupt it.
    """
    if record_path is None:
        record_path = os.environ.get("AI_SKILL_VALIDATION_RECORD")
    if skill_version is None:
        skill_version = os.environ.get("AI_SKILL_CACHE_SEMANTICS") or None
    if max_age_days is None:
        raw = os.environ.get("AI_SKILL_CACHE_MAX_AGE_DAYS", "").strip()
        max_age_days = int(raw) if raw.isdigit() else None

    # An unset validation record path means the feature is off for this skill; a set one
    # that yields nothing means the cache is merely cold. Same outcome, but
    # the log should not blame a cold cache when the cache was never on.
    enabled = bool(record_path)
    records = load_validation_record(record_path)
    record_present = enabled and bool(records)

    rows: list[tuple[str, dict]] = []
    for entry in entries:
        path = Path(entry["image_path"])
        rel = repo_relpath(path, repo_root)
        blob = git_blob_sha1(path)
        if not enabled:
            decision = {
                "cached": False, "reason": "disabled",
                "detail": CACHE_REASONS["disabled"], "entry": None,
            }
        else:
            decision = cache_decision(
                records, rel, blob,
                skill_version=skill_version,
                max_age_days=max_age_days,
                record_present=record_present,
            )
        entry["blob_sha"] = blob
        entry["cached"] = decision["cached"]
        entry["cache_reason"] = decision["reason"]
        entry["cache_detail"] = decision["detail"]
        if decision["cached"]:
            hit = decision["entry"] or {}
            entry["cached_findings"] = list(hit.get("findings") or [])
        rows.append((rel, decision))

    if log and rows:
        width = max(len(rel) for rel, _ in rows)
        print("::group::Cache decisions", file=sys.stderr)
        for rel, decision in rows:
            print(format_decision_line(rel, decision, width), file=sys.stderr)
        print("::endgroup::", file=sys.stderr)

    _write_manifest(entries, repo_root)
    return rows


def _write_manifest(entries: list[dict], repo_root: Path | None) -> None:
    """Record what this invocation resolved, for the workflow's write path.

    The workflow can see which *target* it handed the skill, but only the
    skill knows which files that target pulled in — an article's images are
    resolved inside the collector. Writing them out here is what lets the
    validation record record a dependency closure, and so lets the next run's
    pre-checkout gate prove an untouched article's images are untouched too.
    """
    path = os.environ.get("AI_SKILL_RECORD_MANIFEST")
    if not path:
        return
    manifest = {
        repo_relpath(Path(e["image_path"]), repo_root): e.get("blob_sha")
        for e in entries
    }
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(manifest, f)
    except OSError:
        pass


def _short(sha: object) -> str:
    return str(sha)[:8] if sha else "none"


def _age_days(timestamp: str, now: datetime | None) -> int | None:
    try:
        parsed = datetime.fromisoformat(str(timestamp).replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return ((now or datetime.now(timezone.utc)) - parsed).days


def git_repo_root(start: Path) -> Path | None:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return Path(out.decode().strip())


def extract_image_refs(md_path: Path, image_re) -> list[Path]:
    """Every image `md_path` references via `image_re`, resolved and deduped."""
    text = md_path.read_text(encoding="utf-8")
    seen: set[str] = set()
    refs: list[Path] = []
    for match in image_re.finditer(text):
        ref = match.group(1)
        img = (md_path.parent / ref).resolve()
        key = str(img)
        if key in seen:
            continue
        seen.add(key)
        refs.append(img)
    return refs


def find_article_for_image(image_re, image_path: Path, repo_root: Path) -> Path | None:
    """The first markdown file anywhere in the repo that references image_path."""
    try:
        rel = image_path.relative_to(repo_root).as_posix()
    except ValueError:
        rel = image_path.name
    basename = image_path.name

    try:
        out = subprocess.check_output(
            [
                "git", "-C", str(repo_root),
                "grep", "--files-with-matches", "--null",
                "-e", basename, "--",
                "*.md",
            ],
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    candidates = [repo_root / p for p in out.decode().split("\0") if p]
    for cand in candidates:
        text = cand.read_text(encoding="utf-8", errors="ignore")
        for match in image_re.finditer(text):
            ref = match.group(1)
            if ref.endswith(basename) and (
                ref == basename
                or (cand.parent / ref).resolve() == image_path.resolve()
                or ref.endswith("/" + basename)
                or rel.endswith(ref)
            ):
                return cand
    return candidates[0] if candidates else None
