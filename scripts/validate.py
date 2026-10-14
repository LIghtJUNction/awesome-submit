"""Validate the shipped skill structure, not agent behavior or live submissions."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    assert skill.startswith("---\n"), "Missing YAML frontmatter"
    _, metadata, body = skill.split("---\n", 2)
    fields = dict(line.split(": ", 1) for line in metadata.strip().splitlines())
    assert fields["name"] == "awesome-submit"
    assert re.fullmatch(r"[a-z0-9-]{1,64}", fields["name"])
    assert 0 < len(fields["description"]) <= 1024
    assert "disable-model-invocation" not in fields, "Ambient invocation should be enabled"
    assert len(skill.splitlines()) < 500
    assert all(f"## {i}." in body for i in range(1, 7)), "Missing workflow step"
    for filename in ("README.md", "LICENSE", "evals/evals.json"):
        assert (root / filename).is_file(), f"Missing {filename}"
    for target in re.findall(r"\]\(([^)]+)\)", (root / "README.md").read_text()):
        if "://" not in target and not target.startswith("#"):
            assert (root / target).is_file(), f"Broken local link: {target}"
    cases = json.loads((root / "evals/evals.json").read_text())
    assert cases["skill_name"] == fields["name"]
    assert len(cases["evals"]) >= 7
    assert "awesome-awesome" in body, "Missing broad-to-specific discovery guidance"
    ids = set()
    for case in cases["evals"]:
        assert case["id"] not in ids, "Duplicate scenario ID"
        ids.add(case["id"])
        assert case["prompt"] and case["expected_output"] and case["assertions"]
        assert case["files"] == [], "Bundled scenarios require no external fixture files"
    print(f"PASS: metadata, six workflow steps, local links, license presence, {len(ids)} scenario definitions")
    print("Not tested: model behavior, Skills CLI installation, live GitHub submissions.")


if __name__ == "__main__":
    validate()
