#!/usr/bin/env python3
"""Find tasks with wrong IDs."""
import glob
import os
import re

os.chdir("c:\\noc_project\\UNOC\\ford\\docs\\tasks")

WRONG_IDS = []

for file in sorted(glob.glob("TASK-M1-*.md")):
    if file in ["TASK-M1.md"]:
        continue

    with open(file) as f:
        content = f.read()

    # Extract ID from file (without TASK-)
    file_base = file.replace(".md", "").replace("TASK-", "")

    # Extract ID from content
    id_match = re.search(r"ID: (TASK-[^\n]+)", content)
    if id_match:
        content_id = id_match.group(1).replace("TASK-", "")
        if content_id != file_base:
            WRONG_IDS.append((file, content_id, file_base))

print(f"M1 Tasks with wrong IDs: {len(WRONG_IDS)}\n")
for file, wrong_id, correct_id in WRONG_IDS[:20]:
    print(f"  {file}")
    print(f"    Current ID: {wrong_id}")
    print(f"    Should be:  {correct_id}\n")
