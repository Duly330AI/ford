#!/usr/bin/env python3
"""Deep validation of all task files against schema."""
import glob
import os
import re

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

ERRORS = []

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
    if file in [
        "TASK-BONUS-1.md",
        "TASK-DATA-1.md",
        "TASK-QUALITY-1.md",
        "TASK-QUALITY-2.md",
        "TASK-QUALITY-3.md",
        "TASK-SCAFFOLD-1.md",
        "TASK-TOOLING-1.md",
    ]:
        continue

    with open(file) as f:
        content = f.read()

    # Check if it's old markdown format (has # Title)
    if re.search(r"^# TASK", content, re.MULTILINE):
        ERRORS.append(f"{file}: ❌ OLD MARKDOWN FORMAT (has # Title)")
        continue

    # Check list format
    if not content.strip().startswith("- [ ]"):
        ERRORS.append(f"{file}: ❌ NOT LIST FORMAT (doesn't start with - [ ])")
        continue

    # Check required fields
    missing = []
    for field in REQUIRED_FIELDS:
        if field not in content:
            missing.append(field)

    if missing:
        ERRORS.append(f"{file}: ❌ Missing fields: {', '.join(missing)}")

if ERRORS:
    print(f"❌ FOUND {len(ERRORS)} ISSUES:\n")
    for err in ERRORS[:50]:
        print(f"  {err}")
    if len(ERRORS) > 50:
        print(f"  ... and {len(ERRORS) - 50} more")
else:
    print("✅ ALL TASKS VALID - No schema violations found!")

print(f"\nTotal tasks checked: {len(glob.glob('TASK-M*.md')) - 8 - 7}")
print(f"Issues found: {len(ERRORS)}")
