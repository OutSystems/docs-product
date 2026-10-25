"""Searches knowledge-needs.yaml and prints matching entries, one per line.

The register is tens of thousands of lines, so reading it whole or parsing it
with a throwaway script for every question is slow and error-prone (topics
often have no `subtopics`, which trips code that assumes they do). This prints
each entry the way the skill compares them: its id, its category > topic >
subtopic path, and its description when it has one.

Usage: search_register.py [--file PATH] [--id ID] [--limit N] [keyword ...]
Every keyword must appear (case-insensitive) in the entry's id, path or
description. `--id` matches one entry by exact id instead. With no keyword it
lists the whole register, so pass keywords unless you really want that.
Exits 0 (also when nothing matches), 2 if the file can't be read or parsed.

The register's own structure is checked by validate_register.py; this only
reads it, and tolerates anything that script would report.
"""

import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

DEFAULT_LIMIT = 40


def flatten(register):
    """Yield (id, path, description) per entry: each subtopic, or each topic without subtopics.

    Deliberately re-walks the three levels instead of sharing validate_register.py's
    traversal: that one has to stop and report on malformed entries, this one has to
    skip them silently so a search still works on a register that fails validation.
    """
    if not isinstance(register, dict):
        return
    for category in register.get("knowledge-needs") or []:
        if not isinstance(category, dict):
            continue
        for topic in category.get("topics") or []:
            if not isinstance(topic, dict):
                continue
            topic_path = f"{category.get('name')} > {topic.get('name')}"
            subtopics = [s for s in (topic.get("subtopics") or []) if isinstance(s, dict)]
            if not subtopics:
                yield topic.get("id"), topic_path, topic.get("description")
                continue
            for subtopic in subtopics:
                yield subtopic.get("id"), f"{topic_path} > {subtopic.get('name')}", subtopic.get("description")


def one_line(entry_id, path, description):
    text = " ".join(str(description).split()) if description else "(no description on file)"
    return f"{entry_id} | {path} | {text}"


def search(register, keywords, entry_id=None):
    """Return the one-line form of every entry matching all keywords (or the exact id)."""
    lowered = [k.lower() for k in keywords]
    lines = []
    for found_id, path, description in flatten(register):
        if entry_id is not None:
            if found_id != entry_id:
                continue
        else:
            haystack = f"{found_id} {path} {description or ''}".lower()
            if not all(k in haystack for k in lowered):
                continue
        lines.append(one_line(found_id, path, description))
    return lines


def parse_args(argv):
    path, entry_id, limit, keywords = "knowledge-needs.yaml", None, DEFAULT_LIMIT, []
    args = iter(argv)
    for arg in args:
        if arg == "--file":
            path = next(args, path)
        elif arg == "--id":
            entry_id = next(args, None)
        elif arg == "--limit":
            limit = int(next(args, DEFAULT_LIMIT))
        else:
            keywords.append(arg)
    return path, entry_id, limit, keywords


def main(argv):
    path, entry_id, limit, keywords = parse_args(argv)
    try:
        with open(path, encoding="utf-8") as f:
            register = yaml.safe_load(f)
    except (OSError, yaml.YAMLError) as e:
        print(f"❌ cannot read {path}: {e}")
        return 2

    lines = search(register, keywords, entry_id)
    if not lines:
        print("⚠️ no matching entries")
        return 0
    for line in lines[:limit]:
        print(line)
    if len(lines) > limit:
        print(f"📋 {len(lines)} matches, showing the first {limit}: add keywords to narrow, or pass --limit")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
