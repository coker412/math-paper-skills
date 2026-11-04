"""Portable checks for skill helpers."""

import importlib.util
import json
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


sys.dont_write_bytecode = True  # Keep distributable skill folders free of test caches.


for parent in Path(__file__).resolve().parents:
    ROOT = parent if (parent / "math-paper-writing").is_dir() else parent / ".agents/skills"
    if (ROOT / "math-paper-writing").is_dir():
        break
SCRIPTS = ROOT / "math-paper-writing/scripts"


def module(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + ".py"))
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


pdf = module("pdf_pages")
logs = module("check_tex_log")
text_reader = module("read_text")
language_rules = module("language_rules")


class Helpers(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_tool(self, script, *args):
        return subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)],
                              capture_output=True, text=True)

    def make_pdf(self, name="paper with spaces.pdf", text="Alpha\nBeta"):
        try:
            import fitz
        except ImportError:
            self.skipTest("PyMuPDF required for PDF integration tests")
        path = self.root / name
        with fitz.open() as document:
            document.new_page().insert_text((50, 50), text)
            document.new_page()
            document.new_page().insert_text((50, 50), "Gamma")
            document.save(path)
        return path

    def test_standalone_copies_identical(self):
        for name in ["pdf_pages.py", "check_tex_log.py"]:
            self.assertEqual((SCRIPTS / name).read_bytes(),
                             (ROOT / "math-paper-study-guide/scripts" / name).read_bytes())

    def test_language_view_preserves_rules_and_selects_language(self):
        source = "Rule: keep conditions.\r\nBefore:\r\n> padding\r\nAfter:\r\n> direct\r\nRule: preserve uncertainty.\r\n中文规则：保留条件。\r\n"
        path = self.root / "SKILL.md"
        path.write_bytes(source.encode("utf-8"))
        catalog = {"test": {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                            "line_count": 7, "examples": [[2, 5]],
                            "languages": {"en": [[1, 6]], "zh": [[7, 7]], "both": [[1, 7]]}}}
        _, english = language_rules.rule_view(path, "en", catalog)
        self.assertIn("Rule: keep conditions.\r\n", english)
        self.assertIn("Rule: preserve uncertainty.\r\n", english)
        self.assertNotIn("> padding", english)
        self.assertNotIn("中文", english)
        self.assertIn("source lines 2-5", english)
        _, chinese = language_rules.rule_view(path, "zh", catalog)
        self.assertEqual(chinese, "中文规则：保留条件。\r\n")
        _, both = language_rules.rule_view(path, "both", catalog)
        self.assertEqual(both, english + chinese)

    def test_language_view_unknown_revision_fails_without_filtering(self):
        path = self.root / "SKILL.md"
        path.write_text("A new rule must not be silently omitted.\n")
        with self.assertRaisesRegex(ValueError, "Unrecognized source revision"):
            language_rules.rule_view(path)
        result = self.run_tool("language_rules.py", path, "--language", "en")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("Read the original", result.stderr)
        self.assertEqual(self.run_tool("language_rules.py", self.root / "missing").returncode, 2)

    def test_language_view_catalog_ranges_are_valid(self):
        catalog = json.loads((SCRIPTS / "language-skill-ranges.json").read_text())
        for item in catalog.values():
            self.assertEqual(len(item["sha256"]), 64)
            groups = [item["examples"], *item["languages"].values()]
            for ranges in groups:
                previous = 0
                for start, end in ranges:
                    self.assertTrue(previous < start <= end <= item["line_count"])
                    previous = end
            both = {n for a, b in item["languages"]["both"] for n in range(a, b + 1)}
            self.assertEqual(both, set(range(1, item["line_count"] + 1)))

    def test_text_slices_roundtrip_with_unicode_and_long_lines(self):
        source = "定义\r\n" + "x" * 30001 + "\nλ ≤ 1：🙂\n"
        path = self.root / "source with spaces.txt"
        path.write_bytes(source.encode("utf-8"))
        start, digest, slices = 0, None, []
        while True:
            header, body = text_reader.read_slice(path, start, 127, digest)
            self.assertLessEqual(len(body), 127)
            self.assertEqual(header["start"], start)
            self.assertEqual(header["end"], start + len(body))
            self.assertEqual(header["total_chars"], len(source))
            digest = header["sha256"]
            slices.append(body)
            if header["next_start"] is None:
                break
            start = header["next_start"]
        self.assertEqual("".join(slices), source)

    def test_text_reader_rejects_changed_source_and_bad_cursors(self):
        path = self.root / "text.txt"
        path.write_text("abc", encoding="utf-8")
        header, _ = text_reader.read_slice(path)
        for start, chars in [(-1, 1), (4, 1), (0, 0), (0, 24001)]:
            with self.assertRaises(ValueError):
                text_reader.read_slice(path, start, chars)
        path.write_text("def", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Source changed"):
            text_reader.read_slice(path, 1, 1, header["sha256"])
        path.write_bytes(b"\xff")
        with self.assertRaises(UnicodeError):
            text_reader.read_slice(path)

    def test_text_reader_cli_exact_payload_and_empty_source(self):
        path = self.root / "text.txt"
        path.write_bytes("中\r\nlast".encode("utf-8"))
        result = subprocess.run([sys.executable, str(SCRIPTS / "read_text.py"), str(path)],
                                capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        header, body = result.stdout.split(b"\n", 1)
        self.assertIsNone(json.loads(header)["next_start"])
        self.assertEqual(body, path.read_bytes())
        path.write_bytes(b"")
        header, body = text_reader.read_slice(path)
        self.assertEqual(body, "")
        self.assertIsNone(header["next_start"])
        self.assertEqual(self.run_tool("read_text.py", path, "--start", "1").returncode, 2)
        self.assertEqual(self.run_tool("read_text.py", self.root / "missing.txt").returncode, 2)

    def test_page_selection(self):
        self.assertEqual(pdf.select_pages("3,1-2,2", 3), [1, 2, 3])
        self.assertEqual(pdf.select_pages("all", 3), [1, 2, 3])
        for bad in ["0", "2-1", "4", "1,", "", "1-999999999"]:
            with self.assertRaises(ValueError):
                pdf.select_pages(bad, 3)

    def test_exact_text_search_and_blank_pages(self):
        source = self.make_pdf()
        import fitz
        cache = self.root / "cache/pages.json"
        data, hit = pdf.load_pages(source, cache)
        self.assertFalse(hit)
        with fitz.open(source) as document:
            self.assertEqual(data["pages"], [p.get_text(sort=True) for p in document])
        output = self.run_tool("pdf_pages.py", source, "--cache", cache, "--find", "alpha beta")
        self.assertEqual(output.returncode, 0, output.stderr)
        report = json.loads(output.stdout)
        self.assertEqual(report["matching_pages"], [1])
        self.assertEqual(report["empty_text_pages"], [2])
        output = self.run_tool("pdf_pages.py", source, "--cache", cache, "--pages", "3")
        self.assertEqual(output.returncode, 0, output.stderr)
        self.assertEqual(output.stdout.split("=== PDF PAGE 3 ===\n")[1], data["pages"][2] + "\n")
        self.assertEqual(self.run_tool("pdf_pages.py", source, "--cache", cache, "--pages", "9").returncode, 2)

    def test_cache_reuse_invalidation_and_safe_destination(self):
        source = self.make_pdf()
        cache = self.root / "cache.json"
        first, _ = pdf.load_pages(source, cache)
        with patch.dict(sys.modules, {"fitz": None}):
            self.assertEqual(pdf.load_pages(source, cache), (first, True))
        source.write_bytes(self.make_pdf("replacement.pdf", "Changed").read_bytes())
        second, hit = pdf.load_pages(source, cache)
        self.assertFalse(hit)
        self.assertNotEqual(first["source_sha256"], second["source_sha256"])
        self.assertIn("Changed", second["pages"][0])
        before = source.read_bytes()
        with self.assertRaises(ValueError):
            pdf.load_pages(source, source)
        self.assertEqual(source.read_bytes(), before)
        cache.write_text('{"user_data": true}', encoding="utf-8")
        before = cache.read_bytes()
        with self.assertRaises(ValueError):
            pdf.load_pages(source, cache)
        self.assertEqual(cache.read_bytes(), before)

    def test_diagnostics_are_counted_even_when_examples_limited(self):
        path = self.root / "main.log"
        path.write_text(r"""LaTeX Warning: Reference `eq:missing' on page 1 undefined on input line 8.
Package hyperref Warning: Token not allowed in a PDF string:
(hyperref)                removing `math shift' on input line 10.
Overfull \hbox (2.0pt too wide) in paragraph at lines 12--13
Underfull \vbox (badness 10000) has occurred while output is active
LaTeX Warning: Label `same' multiply defined.
Missing character: There is no 中 in font nullfont!
! Undefined control sequence.
./main.tex:22: Undefined control sequence.
""", encoding="utf-8")
        result = logs.scan(path, 1)
        self.assertEqual((result["warnings"], result["errors"]), (6, 2))
        self.assertEqual(len(result["warning_examples"]), 1)
        self.assertEqual(len(result["error_examples"]), 1)
        self.assertEqual(self.run_tool("check_tex_log.py", path).returncode, 1)
        path.write_text("Warning--I didn't find a database entry for missing\n[12] Biber.pm:55> WARN - Missing entry\n[13] Utils.pm:20> ERROR - Cannot find file\n")
        result = logs.scan(path, 3)
        self.assertEqual((result["warnings"], result["errors"]), (2, 1))

    def test_clean_missing_and_empty_logs(self):
        path = self.root / "main.log"
        path.write_text("Output written on main.pdf (1 page).\n")
        self.assertEqual(self.run_tool("check_tex_log.py", path).returncode, 0)
        self.assertEqual(self.run_tool("check_tex_log.py", path, self.root / "missing.blg").returncode, 2)
        path.write_text("")
        self.assertEqual(self.run_tool("check_tex_log.py", path).returncode, 2)


if __name__ == "__main__":
    unittest.main()
