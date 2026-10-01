"""Tests for validate_register.py."""

import os
import subprocess
import sys
import tempfile
import unittest

import yaml

import validate_register

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "validate_register.py")

VALID = """
knowledge-needs:
- name: Cat
  topics:
  - name: Leaf topic
    id: leaf-topic
  - name: Parent
    id: parent
    subtopics:
    - name: Child
      id: child
"""

NESTED = """
knowledge-needs:
- name: Cat
  topics:
  - name: Parent
    id: parent
    subtopics:
    - name: Child
      id: child
      subtopics:
      - name: Grandchild
        id: grandchild
"""


def errors_for(text):
    return validate_register.validate(yaml.safe_load(text))


class ValidateTests(unittest.TestCase):
    def test_valid_register(self):
        self.assertEqual(errors_for(VALID), [])

    def test_subtopic_with_subtopics_is_rejected(self):
        errors = errors_for(NESTED)
        self.assertEqual(len(errors), 1)
        self.assertIn("Cat > Parent > Child", errors[0])
        self.assertIn("must be a leaf", errors[0])

    def test_duplicate_id(self):
        errors = errors_for(VALID.replace("id: child", "id: leaf-topic"))
        self.assertTrue(any("duplicate id 'leaf-topic'" in e for e in errors))

    def test_missing_id_and_name(self):
        text = "knowledge-needs:\n- name: Cat\n  topics:\n  - description: x\n"
        errors = errors_for(text)
        self.assertTrue(any("missing a 'name'" in e for e in errors))
        self.assertTrue(any("missing an 'id'" in e for e in errors))

    def test_missing_top_level_key(self):
        self.assertEqual(validate_register.validate({"other": []}), ["missing top-level 'knowledge-needs' key"])


class CliTests(unittest.TestCase):
    def run_cli(self, text, *flags):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "kn.yaml")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            return subprocess.run([sys.executable, SCRIPT, path, *flags], capture_output=True, text=True, encoding="utf-8")

    def test_exit_codes(self):
        self.assertEqual(self.run_cli(VALID).returncode, 0)
        self.assertEqual(self.run_cli(NESTED).returncode, 1)
        self.assertEqual(self.run_cli("a: [unclosed").returncode, 2)

    def test_github_annotations_prefix(self):
        out = self.run_cli(NESTED, "--github-annotations").stdout
        self.assertTrue(out.startswith("::error::knowledge-needs.yaml: "))
        self.assertNotIn("::error::", self.run_cli(NESTED).stdout)


if __name__ == "__main__":
    unittest.main()
