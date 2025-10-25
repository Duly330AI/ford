#!/usr/bin/env python3
"""Ultra-deep validation: check content quality."""
import glob
import os
import re

os.chdir("c:\\noc_project\\UNOC\\ford\\docs\\tasks")

WARNINGS = []

for file in sorted(glob.glob("TASK-M*.md")):
    if file.startswith("TASK-M") and not file.endswith(".md"):
        continue
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

    # Extract ID from file
    id_match = re.search(r"ID: (TASK-\S+)", content)
    file_id = file.replace(".md", "").replace("TASK-", "")

    # Check if ID matches filename
    if id_match:
        content_id = id_match.group(1).replace("TASK-", "")
        # For old format, ID might be M1-01 but filename is M1-BSP-01
        # That's OK - but let's flag it
        if content_id not in file and len(content_id) < len(file_id):
            WARNINGS.append(
                f"{file}: ⚠️ ID mismatch - ID is '{id_match.group(1)}' but filename suggests '{file_id}'"
            )

    # Check Notes field - should not be empty
    notes_match = re.search(
        r"Notes:\s*\n\s*(.+?)(?=\n\s*Acceptance:|$)", content, re.DOTALL
    )
    if not notes_match or len(notes_match.group(1).strip()) < 20:
        WARNINGS.append(f"{file}: ⚠️ Notes field too short or empty")

    # Check if References are real paths
    ref_match = re.search(r"References:\s*\n(.*?)(?:\n\n|$)", content, re.DOTALL)
    if ref_match:
        refs = ref_match.group(1)
        if "- docs/" not in refs:
            WARNINGS.append(
                f"{file}: ⚠️ References don't look like real paths (missing 'docs/')"
            )
    else:
        WARNINGS.append(f"{file}: ⚠️ No References section found")

    # Check if Artifacts list is reasonable
    art_match = re.search(r"Artifacts: (.*)", content)
    if art_match:
        artifacts = art_match.group(1)
        if "`" not in artifacts or len(artifacts) < 10:
            WARNINGS.append(
                f"{file}: ⚠️ Artifacts field looks suspicious: {artifacts[:50]}"
            )

if WARNINGS:
    print(f"⚠️ FOUND {len(WARNINGS)} WARNINGS:\n")
    for w in WARNINGS[:30]:
        print(f"  {w}")
    if len(WARNINGS) > 30:
        print(f"  ... and {len(WARNINGS) - 30} more")
else:
    print("✅ NO CONTENT WARNINGS - All tasks look good!")

print(f"\nWarnings: {len(WARNINGS)}")
