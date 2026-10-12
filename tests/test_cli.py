from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "passgen.py"


class CliTests(unittest.TestCase):
    def run_cli(self, *args, input=""):
        return subprocess.run([sys.executable, str(SCRIPT), *args], input=input,
                              text=True, capture_output=True)

    def test_flag_prints_only_requested_password(self):
        result = self.run_cli("--length", "24")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(len(result.stdout.strip()), 24)
        self.assertEqual(result.stderr, "")

    def test_bad_input_has_nonzero_exit_without_traceback(self):
        for args, input_value in ((["--length", "0"], ""), ([], "abc"), ([], "")):
            result = self.run_cli(*args, input=input_value)
            self.assertEqual(result.returncode, 2)
            self.assertIn("Error:", result.stderr)
            self.assertNotIn("Traceback", result.stderr)
            self.assertNotIn("Traceback", result.stdout)

    def test_interactive_mode_remains_available(self):
        result = self.run_cli(input="18\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(len(result.stdout.strip().split(": ")[-1]), 18)
