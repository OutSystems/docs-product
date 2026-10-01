"""Validates the structure of knowledge-needs.yaml.

Single source of truth for the register's schema, shared by three callers so
they can never disagree: the knowledge-needs-classification skill (which runs
it on its own edit and fixes any error before opening a PR), metadata-refresh.yml
(which refuses to open a tk-cicd sync PR for an invalid register), and
validate-metadata.yml (the PR-time check on tk-cicd itself).

The schema is exactly 3 levels -- category > topic > subtopic -- and a subtopic
is always a leaf. Every topic (or, if it has subtopics, each subtopic) needs a
unique `id`; every category/topic/subtopic needs a `name`.

Usage: validate_register.py [path] [--github-annotations]
Exits 0 when valid, 1 (listing every problem) when not, 2 if the file can't be
read or parsed as YAML. Prints plain lines by default; --github-annotations
prefixes each with `::error::` for GitHub Actions.
"""

import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


def validate(register):
    """Return a list of human-readable problems found in the parsed register."""
    errors = []
    seen_ids = {}

    if not isinstance(register, dict) or "knowledge-needs" not in register:
        return ["missing top-level 'knowledge-needs' key"]

    def check_id(entry, label):
        entry_id = entry.get("id")
        if not entry_id:
            errors.append(f"{label} is missing an 'id'")
        elif entry_id in seen_ids:
            errors.append(f"duplicate id '{entry_id}' ({label} and {seen_ids[entry_id]})")
        else:
            seen_ids[entry_id] = label

    for category in register["knowledge-needs"] or []:
        if not isinstance(category, dict):
            errors.append("a category entry is not a mapping")
            continue
        category_name = category.get("name") or "<unnamed category>"
        if not category.get("name"):
            errors.append("a category is missing a 'name'")
        for topic in category.get("topics") or []:
            if not isinstance(topic, dict):
                errors.append(f"a topic under '{category_name}' is not a mapping")
                continue
            topic_label = f"{category_name} > {topic.get('name') or '<unnamed topic>'}"
            if not topic.get("name"):
                errors.append(f"a topic under '{category_name}' is missing a 'name'")
            subtopics = topic.get("subtopics") or []
            if not subtopics:
                check_id(topic, topic_label)
                continue
            for subtopic in subtopics:
                if not isinstance(subtopic, dict):
                    errors.append(f"a subtopic under '{topic_label}' is not a mapping")
                    continue
                sub_label = f"{topic_label} > {subtopic.get('name') or '<unnamed subtopic>'}"
                if not subtopic.get("name"):
                    errors.append(f"a subtopic under '{topic_label}' is missing a 'name'")
                if subtopic.get("subtopics"):
                    errors.append(
                        f"subtopic '{sub_label}' has its own 'subtopics' — the schema is "
                        "exactly 3 levels (category > topic > subtopic) and a subtopic must "
                        "be a leaf; either add the entries as siblings under the same topic, "
                        "or promote the subtopic to a topic of its own"
                    )
                check_id(subtopic, sub_label)
    return errors


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    prefix = "::error::knowledge-needs.yaml: " if "--github-annotations" in argv else ""
    path = args[0] if args else "knowledge-needs.yaml"
    try:
        with open(path, encoding="utf-8") as f:
            register = yaml.safe_load(f)
    except (OSError, yaml.YAMLError) as e:
        print(f"{prefix}cannot read {path}: {e}")
        return 2

    errors = validate(register)
    for error in errors:
        print(f"{prefix}{error}")
    if errors:
        return 1
    print(f"✅ {path} schema is valid (unique ids, required names present, 3 levels max)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
