#!/usr/bin/env python3
"""Fix missing required fields in tasks."""
import glob
import os
from datetime import datetime

os.chdir("c:\\noc_project\\UNOC\\ford\\docs\\tasks")

REQUIRED_FIELDS = {
    "ID:": "ID (auto-skip if present)",
    "Title:": "Title (auto-skip if present)",
    "Status:": "Status: Proposed",
    "Priority:": "Priority: P0",
    "Owner:": "Owner: Codex Agent",
    "Created:": f'Created: {datetime.now().strftime("%Y-%m-%d")}',
    "Artifacts:": "Artifacts: (auto-skip if present)",
    "DependsOn:": "DependsOn: (auto-skip if present)",
    "Notes:": "Notes: (auto-skip if present)",
    "Acceptance:": "Acceptance: (auto-skip if present)",
    "Tests:": "Tests: (auto-skip if present)",
    "References:": "References: (auto-skip if present)",
}

fixed = 0
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
        lines = f.readlines()

    if not lines or not lines[0].startswith("- [ ] ID:"):
        continue  # Skip wrong format

    # Find where to insert (after Owner: line)
    insert_idx = None
    has_created = False

    for i, line in enumerate(lines):
        if "Created:" in line:
            has_created = True
        if line.startswith("  Owner:") and insert_idx is None:
            insert_idx = i + 1

    if not has_created and insert_idx:
        lines.insert(insert_idx, f"  Created: {datetime.now().strftime('%Y-%m-%d')}\n")
        fixed += 1
        print(f"  [+] {file}: Added Created:")

    # Check for missing Tests: and Acceptance:
    has_tests = any("Tests:" in line for line in lines)
    has_acceptance = any("Acceptance:" in line for line in lines)

    if not has_acceptance:
        # Insert before Tests if exists, else before References
        for i, line in enumerate(lines):
            if "Tests:" in line or "References:" in line:
                lines.insert(
                    i, "  Acceptance:\n  - [ ] (TODO: add acceptance criteria)\n"
                )
                fixed += 1
                print(f"  [+] {file}: Added Acceptance:")
                break

    if not has_tests:
        # Insert before References
        for i, line in enumerate(lines):
            if "References:" in line:
                lines.insert(i, "  Tests:\n  - [ ] (TODO: add tests)\n")
                fixed += 1
                print(f"  [+] {file}: Added Tests:")
                break

    with open(file, "w") as f:
        f.writelines(lines)

print(f"\n✅ Fixed {fixed} files")
