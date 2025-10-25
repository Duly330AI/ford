#!/usr/bin/env python3
"""Find tasks with malformed Artifacts."""
import os
import glob
import re

os.chdir('c:\\noc_project\\UNOC\\ford\\docs\\tasks')

BAD_ARTIFACTS = []

for file in sorted(glob.glob("TASK-M*.md")):
    if file.startswith("TASK-M") and file not in ["TASK-M1.md", "TASK-M2.md", "TASK-M3.md", "TASK-M4.md", "TASK-M5.md", "TASK-M6.md", "TASK-M7.md", "TASK-M8.md", "TASK-BONUS-1.md", "TASK-DATA-1.md", "TASK-QUALITY-1.md", "TASK-QUALITY-2.md", "TASK-QUALITY-3.md", "TASK-SCAFFOLD-1.md", "TASK-TOOLING-1.md"]:
        with open(file) as f:
            content = f.read()

        art_match = re.search(r'Artifacts: (.+?)(?:\n  [A-Z]|$)', content)
        if art_match:
            artifacts = art_match.group(1)
            # Check for $_ or other garbage
            if '$_' in artifacts or '##' in artifacts or artifacts.strip() == '':
                BAD_ARTIFACTS.append((file, artifacts[:60]))

if BAD_ARTIFACTS:
    print(f"❌ Found {len(BAD_ARTIFACTS)} tasks with bad Artifacts:\n")
    for file, art in BAD_ARTIFACTS[:20]:
        print(f"  {file}")
        print(f"    → {art}...\n")
else:
    print("✅ All Artifacts look OK!")
