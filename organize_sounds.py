#!/usr/bin/env python3
"""Organize generated sounds into proper audio/ structure."""

import os
import shutil
from pathlib import Path

sfx_tmp = Path("SFX_TMP")
audio_sfx = Path("audio/sfx")

# Ensure directories exist
for cat in ["ui", "foley", "weapon", "magic", "creature", "trap", "ambient", "combat"]:
    (audio_sfx / cat).mkdir(parents=True, exist_ok=True)
(Path("audio") / "music").mkdir(parents=True, exist_ok=True)

# Mapping of filename patterns to target folder
category_map = {
    "ui_": "ui",
    "foley_": "foley",
    "weapon_": "weapon",
    "magic_": "magic",
    "creature_": "creature",
    "trap_": "trap",
    "ambient_": "ambient",
    "combat_": "combat",
}

# Special cases (exact filename -> folder)
special_map = {
    "coin_pickup_01.wav": "ui",
    "fireball_01.wav": "magic",
    "heal_01.wav": "magic",
    "hit_01.wav": "combat",
    "menu_close_01.wav": "ui",
    "menu_open_01.wav": "ui",
    "quest_complete_01.wav": "ui",
    "sword_swing_01.wav": "weapon",
    "magic_cast_01.wav": "magic",
    "ui_click_01.wav": "ui",
}

moved = 0
skipped = 0
errors = []

# Process all WAV files
for src_file in sfx_tmp.glob("*.wav"):
    filename = src_file.name

    # Determine target folder
    target_folder = None
    if filename in special_map:
        target_folder = special_map[filename]
    else:
        for prefix, folder in category_map.items():
            if filename.startswith(prefix):
                target_folder = folder
                break

    if target_folder:
        dst_path = audio_sfx / target_folder / filename
        try:
            shutil.copy2(str(src_file), str(dst_path))
            moved += 1
            print(f"✓ {target_folder}: {filename}")
        except Exception as e:
            errors.append(f"✗ {filename}: {str(e)}")
    else:
        skipped += 1
        print(f"⚠ UNCATEGORIZED: {filename}")

# Also copy catalog.json and README.md and LICENSE.txt
for special_file in ["catalog.json", "README.md", "LICENSE.txt"]:
    src = sfx_tmp / special_file
    if src.exists():
        dst = Path("audio") / special_file
        shutil.copy2(str(src), str(dst))
        print(f"✓ root: {special_file}")

print(f"\n=== SUMMARY ===")
print(f"Moved: {moved} files")
print(f"Skipped: {skipped} files")
if errors:
    print(f"Errors: {len(errors)}")
    for err in errors[:5]:
        print(f"  {err}")
