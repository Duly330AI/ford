#!/usr/bin/env python3
"""Validate all tasks against schema requirements."""
import glob
import os

os.chdir("c:\\noc_project\\UNOC\\ford\\docs\\tasks")

REQUIRED_FIELDS = [
    "ID:",
    "Title:",
    "Status:",
    "Priority:",
    "Owner:",
    "Created:",
    "Artifacts:",
    "DependsOn:",
    "Notes:",
    "Acceptance:",
    "Tests:",
    "References:",
]

issues = {
    "missing_format": [],
    "missing_fields": [],
    "other_issues": [],
}

for file in sorted(glob.glob("TASK-M*.md")):
    if file in [
        "TASK-M1.md",
        "TASK-M2.md",
        "TASK-M3.md",
        "TASK-M4.md",
        "TASK-M5.md",
        "TASK-M6.md",
        "TASK-M7.md",
        "TASK-M8.md",
    ]:
        continue

    with open(file) as f:
        content = f.read()

    # Check format
    if not content.startswith("- [ ] ID:"):
        issues["missing_format"].append(file)
        continue

    # Check required fields
    missing = []
    for field in REQUIRED_FIELDS:
        if field not in content:
            missing.append(field)

    if missing:
        issues["missing_fields"].append((file, missing))

    # Check specific issues
    if "References:\n  - " not in content:
        issues["other_issues"].append(f"{file}: References format issue")

print("📋 VALIDATION REPORT\n")

if issues["missing_format"]:
    print(f"🔴 WRONG FORMAT ({len(issues['missing_format'])}): NOT list-based")
    for f in issues["missing_format"][:10]:
        print(f"  {f}")

if issues["missing_fields"]:
    print(f"\n⚠️  MISSING FIELDS ({len(issues['missing_fields'])}):")
    for f, fields in issues["missing_fields"][:10]:
        print(f"  {f}: missing {', '.join(fields[:3])}")

if issues["other_issues"]:
    print(f"\n⚠️  OTHER ISSUES ({len(issues['other_issues'])})")
    for issue in issues["other_issues"][:10]:
        print(f"  {issue}")

print(
    f"\n✅ Total: {len([f for f in glob.glob('TASK-M*.md') if f not in ['TASK-M1.md', 'TASK-M2.md', 'TASK-M3.md', 'TASK-M4.md', 'TASK-M5.md', 'TASK-M6.md', 'TASK-M7.md', 'TASK-M8.md']])} tasks checked"
)
