import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_criterion_1_report_is_valid_json():
    """Verifies instruction.md criterion 1: /app/report.json exists and is valid JSON."""
    assert REPORT.exists(), "missing /app/report.json"
    assert REPORT.stat().st_size > 0, "/app/report.json is empty"
    with REPORT.open() as f:
        json.load(f)


def test_criterion_2_total_requests():
    """Verifies instruction.md criterion 2: total_requests equals the number of non-blank lines in access.log (6)."""
    with REPORT.open() as f:
        data = json.load(f)
    assert data["total_requests"] == 6


def test_criterion_3_unique_ips():
    """Verifies instruction.md criterion 3: unique_ips equals the number of distinct client IPs (3)."""
    with REPORT.open() as f:
        data = json.load(f)
    assert data["unique_ips"] == 3


def test_criterion_4_top_path():
    """Verifies instruction.md criterion 4: top_path is the single most-requested path (/index.html)."""
    with REPORT.open() as f:
        data = json.load(f)
    assert data["top_path"] == "/index.html"
