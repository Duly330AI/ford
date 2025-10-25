#!/usr/bin/env python3
import glob
import os

os.chdir("c:\\noc_project\\UNOC\\ford\\docs\\tasks")
missing_refs = []
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
        if "References:" not in content:
            missing_refs.append(file)

print(f"Tasks missing References: {len(missing_refs)}\n")
for f in missing_refs[:30]:
    print(f"  {f}")
if len(missing_refs) > 30:
    print(f"  ... and {len(missing_refs) - 30} more")
