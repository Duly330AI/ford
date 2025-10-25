#!/usr/bin/env python3
"""Auto-fix all task IDs to match filenames."""
import glob
import os
import re

os.chdir("c:\\noc_project\\UNOC\\ford\\docs\\tasks")

count = 0

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

    # Extract correct ID from filename
    correct_id = file.replace(".md", "").replace("TASK-", "")

    # Replace old ID with new one
    new_content = re.sub(r"ID: TASK-[^\n]+", f"ID: TASK-{correct_id}", content, count=1)

    if new_content != content:
        with open(file, "w") as f:
            f.write(new_content)
        count += 1
        if count % 20 == 0:
            print(f"  [{count}] Fixed ID in {file}")

print(f"\n✅ Fixed {count} task IDs")
