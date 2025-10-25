#!/usr/bin/env python3
"""Auto-add References to tasks based on content keywords."""
import glob
import os
import re

# Mapping: keyword patterns → suggested references
KEYWORD_REFS = {
    r"(combat|damage|hit|dodge|attack|defense|armor)": [
        "docs/COMBAT_RULES.md",
        "docs/CONVENTIONS.md",
        "docs/ARCHITECTURE.md",
    ],
    r"(skill|progression|experience|magic|spell)": [
        "docs/CONVENTIONS.md",
        "docs/ARCHITECTURE.md",
    ],
    r"(ui|menu|screen|button|widget|theme)": [
        "docs/CONVENTIONS.md",
        "docs/ARCHITECTURE.md",
    ],
    r"(item|loot|inventory|equipment|gear|affix)": [
        "docs/ITEMIZATION_DESIGN.md",
        "docs/CONVENTIONS.md",
        "docs/ARCHITECTURE.md",
    ],
    r"(ai|npc|faction|behavior|engagement|pathfind)": [
        "docs/ARCHITECTURE.md",
        "docs/CONVENTIONS.md",
    ],
    r"(save|load|persist|serial|state|checkpoint)": [
        "docs/ARCHITECTURE.md",
        "docs/CONVENTIONS.md",
    ],
    r"(quest|objective|journal|event|bus)": [
        "docs/QUEST_SYSTEM.md",
        "docs/CONVENTIONS.md",
        "docs/ARCHITECTURE.md",
    ],
    r"(audio|sound|music|mixer|ambience)": [
        "docs/SOUND_DESIGN.md",
        "docs/CONVENTIONS.md",
        "docs/ARCHITECTURE.md",
    ],
    r"(input|control|rebind|keyboard|gamepad)": [
        "docs/INPUT_AND_REBIND.md",
        "docs/CONVENTIONS.md",
        "docs/ARCHITECTURE.md",
    ],
    r"(locali|i18n|translat|language)": [
        "docs/LOCALIZATION.md",
        "docs/CONVENTIONS.md",
        "docs/ARCHITECTURE.md",
    ],
    r"(dungeon|biome|generation|room|tag)": [
        "docs/DUNGEON_GENERATOR.md",
        "docs/CONVENTIONS.md",
        "docs/ARCHITECTURE.md",
    ],
    r"(ftue|tutorial|onboard|character.*creat)": [
        "docs/TUTORIAL_FTUE.md",
        "docs/CONVENTIONS.md",
        "docs/ARCHITECTURE.md",
    ],
}

DEFAULT_REFS = [
    "docs/CONVENTIONS.md",
    "docs/ARCHITECTURE.md",
]

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

    if "References:" in content:
        continue  # Already has references

    # Extract title to find keywords
    title_match = re.search(r"Title: (.+)", content)
    title = (title_match.group(1) if title_match else "").lower()
    full_text = (content + title).lower()

    # Find matching references
    refs = set()
    for pattern, ref_list in KEYWORD_REFS.items():
        if re.search(pattern, full_text):
            refs.update(ref_list)

    if not refs:
        refs = set(DEFAULT_REFS)

    refs = sorted(list(refs))

    # Add references to file
    ref_section = "  References:\n"
    for ref in refs:
        ref_section += f"  - {ref}\n"

    # Insert before final newlines
    new_content = content.rstrip() + "\n" + ref_section

    with open(file, "w") as f:
        f.write(new_content)

    count += 1
    if count % 10 == 0:
        print(f"  [+{count}] Added references to {file}")

print(f"✅ Done! Added References to {count} tasks")
