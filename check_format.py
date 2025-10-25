#!/usr/bin/env python3
"""Check how many tasks are still in old markdown format."""
import glob
import os

os.chdir("c:\\noc_project\\UNOC\\ford\\docs\\tasks")

old_format = []
new_format = []

for file in sorted(glob.glob("TASK-M*.md")):
    with open(file) as f:
        first_line = f.readline()

    if first_line.startswith("# TASK-"):
        old_format.append(file)
    elif first_line.startswith("- [ ] ID:"):
        new_format.append(file)

print(f"🔴 OLD MARKDOWN FORMAT: {len(old_format)}")
for f in old_format[:20]:
    print(f"  {f}")
if len(old_format) > 20:
    print(f"  ... and {len(old_format) - 20} more")

print(f"\n✅ NEW LIST FORMAT: {len(new_format)}")

print(f"\n📊 TOTAL: {len(old_format) + len(new_format)} tasks")
