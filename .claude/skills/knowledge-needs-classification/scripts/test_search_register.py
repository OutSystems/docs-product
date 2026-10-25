"""Tests for search_register.py."""

import os
import subprocess
import sys
import tempfile
import unittest

import yaml

import search_register

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "search_register.py")

REGISTER = """
knowledge-needs:
- name: Cat
  topics:
  - name: Leaf topic
    id: leaf-topic
    description: Wants to reset a password
  - name: Null subtopics
    id: null-subtopics
    subtopics:
  - name: Parent
    id: parent
    subtopics:
    - name: Child
      id: child
      description: >
        Wants to configure
        a timer
    - name: Other child
      id: other-child
"""


def search(*keywords, entry_id=None):
    return search_register.search(yaml.safe_load(REGISTER), list(keywords), entry_id)


class SearchTests(unittest.TestCase):
    def test_topic_without_subtopics_or_with_null_subtopics_is_an_entry(self):
        ids = [line.split(" | ")[0] for line in search()]
        self.assertEqual(ids, ["leaf-topic", "null-subtopics", "child", "other-child"])

    def test_parent_with_subtopics_is_not_listed_itself(self):
        self.assertFalse(any(line.startswith("parent |") for line in search()))

    def test_keywords_are_anded_and_case_insensitive(self):
        self.assertEqual(search("TIMER", "child"), ["child | Cat > Parent > Child | Wants to configure a timer"])
        self.assertEqual(search("timer", "password"), [])

    def test_keyword_matches_path_and_id(self):
        self.assertEqual(len(search("parent")), 2)
        self.assertEqual(len(search("other-child")), 1)

    def test_exact_id(self):
        self.assertEqual(len(search(entry_id="child")), 1)
        self.assertEqual(search(entry_id="chil"), [])

    def test_missing_description_is_said_so(self):
        self.assertTrue(search("other-child")[0].endswith("(no description on file)"))

    def test_malformed_register_does_not_raise(self):
        self.assertEqual(list(search_register.flatten({"knowledge-needs": ["x", {"topics": [1]}]})), [])
        self.assertEqual(list(search_register.flatten(None)), [])


class CliTests(unittest.TestCase):
    def run_cli(self, text, *args):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "kn.yaml")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            return subprocess.run(
                [sys.executable, SCRIPT, "--file", path, *args], capture_output=True, text=True, encoding="utf-8"
            )

    def test_match_and_no_match_both_exit_zero(self):
        found = self.run_cli(REGISTER, "timer")
        self.assertEqual(found.returncode, 0)
        self.assertIn("child | Cat > Parent > Child", found.stdout)
        none = self.run_cli(REGISTER, "nothing-like-this")
        self.assertEqual(none.returncode, 0)
        self.assertIn("no matching entries", none.stdout)

    def test_limit_notes_the_rest(self):
        out = self.run_cli(REGISTER, "--limit", "1").stdout
        self.assertEqual(len(out.splitlines()), 2)
        self.assertIn("4 matches, showing the first 1", out)

    def test_unreadable_file_exits_two(self):
        self.assertEqual(self.run_cli("a: [unclosed").returncode, 2)


if __name__ == "__main__":
    unittest.main()
