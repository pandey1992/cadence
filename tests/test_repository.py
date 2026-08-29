"""Behavioral contract tests for Cadence's deterministic repository tooling."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "plugins/cadence/scripts/cadence-check.sh"


def run(*command: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)


class CadenceRepositoryTests(unittest.TestCase):
    def test_repository_validator_passes(self) -> None:
        result = run("python3", "scripts/validate-repo.py", cwd=ROOT)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_check_accepts_clean_staged_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            self.assertEqual(run("git", "init", "-q", cwd=repo).returncode, 0)
            (repo / "clean.txt").write_text("one\ntwo\n")
            self.assertEqual(run("git", "add", "clean.txt", cwd=repo).returncode, 0)

            result = run(str(CHECK), cwd=repo)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_check_rejects_staged_whitespace_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            self.assertEqual(run("git", "init", "-q", cwd=repo).returncode, 0)
            (repo / "invalid.txt").write_text("trailing space \n")
            self.assertEqual(run("git", "add", "invalid.txt", cwd=repo).returncode, 0)

            result = run(str(CHECK), cwd=repo)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("trailing whitespace", result.stdout)

    def test_both_distributions_expose_project_context_routing(self) -> None:
        standalone = ROOT / "skills/cadence/SKILL.md"
        plugin = ROOT / "plugins/cadence/skills/cadence/SKILL.md"
        for skill in (standalone, plugin):
            self.assertIn("project-context.md", skill.read_text())
        self.assertTrue((ROOT / "skills/cadence/references/project-context.md").is_file())
        self.assertTrue(
            (ROOT / "plugins/cadence/skills/cadence/references/project-context.md").is_file()
        )

    def test_claude_marketplace_points_to_self_contained_plugin(self) -> None:
        marketplace = ROOT / ".claude-plugin/marketplace.json"
        manifest = ROOT / "plugins/claude-cadence/.claude-plugin/plugin.json"
        self.assertTrue(marketplace.is_file())
        self.assertTrue(manifest.is_file())
        self.assertIn('"source": "./plugins/claude-cadence"', marketplace.read_text())
        self.assertIn('"skills": "./skills/"', manifest.read_text())


if __name__ == "__main__":
    unittest.main()
