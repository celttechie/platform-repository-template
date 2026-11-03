#!/usr/bin/env python3
"""Sanity and baseline structure verification tests for platform template."""

import os
import subprocess
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class TestPlatformTemplateSanity(unittest.TestCase):
    """Validate repository layout and core template compliance."""

    def test_required_directories_exist(self):
        required_dirs = [
            "infra",
            "infra/modules",
            "infra/environments/local-kvm",
            "infra/environments/aws",
            "infra/environments/gcp",
            "platform",
            "platform/ingress",
            "platform/autoscaling",
            "platform/storage",
            "platform/observability",
            "workloads",
            "docs",
            "docs/adr",
            "docs/security",
            "docs/operations",
            "scripts",
            ".github",
            ".github/workflows",
        ]
        for d in required_dirs:
            full_path = os.path.join(REPO_ROOT, d)
            self.assertTrue(os.path.isdir(full_path), f"Required directory missing: {d}")

    def test_required_core_files_exist(self):
        required_files = [
            "Makefile",
            "README.md",
            "pyproject.toml",
            ".gitignore",
            ".pre-commit-config.yaml",
            ".github/PULL_REQUEST_TEMPLATE.md",
            ".github/workflows/ci.yml",
            "scripts/doctor.py",
            "docs/IMPLEMENTATION_PLAN.md",
            "docs/adr/0001-record-architecture-decisions.md",
            "docs/adr/0002-decoupled-monorepo-tiering.md",
            "docs/security/security-model.md",
            "docs/operations/demonstration-runbook.md",
        ]
        for f in required_files:
            full_path = os.path.join(REPO_ROOT, f)
            self.assertTrue(os.path.isfile(full_path), f"Required file missing: {f}")
            self.assertGreater(os.path.getsize(full_path), 0, f"File is empty: {f}")

    def test_doctor_script_execution(self):
        doctor_path = os.path.join(REPO_ROOT, "scripts", "doctor.py")
        res = subprocess.run([doctor_path], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, f"doctor.py failed with output:\n{res.stdout}\n{res.stderr}")
        self.assertIn("PLATFORM REPOSITORY PRE-FLIGHT AUDITOR", res.stdout)


if __name__ == "__main__":
    unittest.main()
