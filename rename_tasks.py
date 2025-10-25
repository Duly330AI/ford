#!/usr/bin/env python3
"""Auto-rename M3-M8 tasks with descriptive names (M2 already done)."""

import os
import shutil

os.chdir(r"C:\noc_project\UNOC\ford\docs\tasks")

# M3 (25 tasks - EXT & GEN/ITEM/MAGIC already have names)
m3_map = {
    "TASK-M3-01.md": "TASK-M3-SKILLS-01-Progression.md",
    "TASK-M3-02.md": "TASK-M3-CRAFTING-02-System.md",
    "TASK-M3-03.md": "TASK-M3-QUESTS-03-Journal.md",
    "TASK-M3-04.md": "TASK-M3-HOTSYNC-04-Hotbar.md",
    "TASK-M3-05.md": "TASK-M3-INVENTORY-05-System.md",
    "TASK-M3-06.md": "TASK-M3-EQUIPMENT-06-Slots.md",
    "TASK-M3-07.md": "TASK-M3-ABILITIES-07-Powers.md",
    "TASK-M3-08.md": "TASK-M3-LOOT-08-Tables.md",
    "TASK-M3-09.md": "TASK-M3-STASH-09-Persistence.md",
    "TASK-M3-10.md": "TASK-M3-WEIGHT-10-Encumbrance.md",
    "TASK-M3-11.md": "TASK-M3-CONSUME-11-Consumables.md",
    "TASK-M3-12.md": "TASK-M3-COMBAT-12-Integration.md",
    "TASK-M3-13.md": "TASK-M3-ECONOMY-13-Foundation.md",
    "TASK-M3-14.md": "TASK-M3-VENDOR-14-Integration.md",
    "TASK-M3-15.md": "TASK-M3-CRAFTING-15-Recipes.md",
    "TASK-M3-16.md": "TASK-M3-REPAIR-16-System.md",
    "TASK-M3-17.md": "TASK-M3-TRADE-17-Dialog.md",
    "TASK-M3-18.md": "TASK-M3-AUCTION-18-System.md",
    "TASK-M3-19.md": "TASK-M3-STORAGE-19-Bank.md",
    "TASK-M3-20.md": "TASK-M3-PLAYER-20-Customization.md",
    "TASK-M3-21.md": "TASK-M3-STATS-21-Display.md",
    "TASK-M3-22.md": "TASK-M3-INSPECTION-22-Details.md",
    "TASK-M3-23.md": "TASK-M3-COMPARE-23-Equipment.md",
    "TASK-M3-24.md": "TASK-M3-CRAFTING-24-UI.md",
    "TASK-M3-25.md": "TASK-M3-INTEGRATION-25-Determinism.md",
}

# M4 (24 tasks - AUDIO/ECON/QUEST already have names)
m4_map = {
    "TASK-M4-01.md": "TASK-M4-SAVE-01-System.md",
    "TASK-M4-02.md": "TASK-M4-LOAD-02-Restore.md",
    "TASK-M4-03.md": "TASK-M4-AUTOSAVE-03-Checkpoints.md",
    "TASK-M4-04.md": "TASK-M4-VERSION-04-Migration.md",
    "TASK-M4-05.md": "TASK-M4-SLOTS-05-Management.md",
    "TASK-M4-06.md": "TASK-M4-SETTINGS-06-Config.md",
    "TASK-M4-07.md": "TASK-M4-GRAPHICS-07-Quality.md",
    "TASK-M4-08.md": "TASK-M4-AUDIO-08-Settings.md",
    "TASK-M4-09.md": "TASK-M4-INPUT-09-Options.md",
    "TASK-M4-10.md": "TASK-M4-ACCESSIBILITY-10-Options.md",
    "TASK-M4-11.md": "TASK-M4-DIFFICULTY-11-Scaling.md",
    "TASK-M4-12.md": "TASK-M4-DIFFICULTY-12-Adjustments.md",
    "TASK-M4-13.md": "TASK-M4-DIFFICULTY-13-Balancing.md",
    "TASK-M4-14.md": "TASK-M4-DIFFICULTY-14-Testing.md",
    "TASK-M4-15.md": "TASK-M4-WORLD-15-Generation.md",
    "TASK-M4-16.md": "TASK-M4-TIMEKEEPER-16-System.md",
    "TASK-M4-17.md": "TASK-M4-DAYNIGHT-17-Cycle.md",
    "TASK-M4-18.md": "TASK-M4-WEATHER-18-System.md",
    "TASK-M4-19.md": "TASK-M4-DYNAMIC-19-Events.md",
    "TASK-M4-20.md": "TASK-M4-SEEDING-20-Determinism.md",
    "TASK-M4-21.md": "TASK-M4-DEBUG-21-Tools.md",
    "TASK-M4-22.md": "TASK-M4-CONTENT-22-Validation.md",
    "TASK-M4-23.md": "TASK-M4-INTEGRATION-23-M4-Testing.md",
    "TASK-M4-24.md": "TASK-M4-ACCEPTANCE-24-Criteria.md",
}

# M5 (18 tasks)
m5_map = {
    "TASK-M5-01.md": "TASK-M5-SAVE-01-Extended.md",
    "TASK-M5-02.md": "TASK-M5-MULTIPLAYER-02-Foundation.md",
    "TASK-M5-03.md": "TASK-M5-NETWORKING-03-Protocol.md",
    "TASK-M5-04.md": "TASK-M5-SYNC-04-State.md",
    "TASK-M5-05.md": "TASK-M5-LATENCY-05-Compensation.md",
    "TASK-M5-06.md": "TASK-M5-PVP-06-Arena.md",
    "TASK-M5-07.md": "TASK-M5-GUILDS-07-System.md",
    "TASK-M5-08.md": "TASK-M5-TRADING-08-System.md",
    "TASK-M5-09.md": "TASK-M5-MESSAGING-09-Chat.md",
    "TASK-M5-10.md": "TASK-M5-FRIENDS-10-System.md",
    "TASK-M5-11.md": "TASK-M5-LEADERBOARDS-11-Ranking.md",
    "TASK-M5-12.md": "TASK-M5-ACHIEVEMENTS-12-System.md",
    "TASK-M5-13.md": "TASK-M5-EVENTS-13-Server.md",
    "TASK-M5-14.md": "TASK-M5-MODERATION-14-Tools.md",
    "TASK-M5-15.md": "TASK-M5-SECURITY-15-Validation.md",
    "TASK-M5-16.md": "TASK-M5-TESTING-16-Multiplayer.md",
    "TASK-M5-17.md": "TASK-M5-STRESS-17-Tests.md",
    "TASK-M5-18.md": "TASK-M5-INTEGRATION-18-Acceptance.md",
}

# M6 (17 UI tasks - UI already have prefixes)
m6_map = {
    "TASK-M6-UI-01.md": "TASK-M6-UI-01-Core-Framework.md",
    "TASK-M6-UI-02.md": "TASK-M6-UI-02-Widget-Library.md",
    "TASK-M6-UI-03.md": "TASK-M6-UI-03-Theming.md",
    "TASK-M6-UI-04.md": "TASK-M6-UI-04-Layout.md",
    "TASK-M6-UI-05.md": "TASK-M6-UI-05-Animation.md",
    "TASK-M6-UI-06.md": "TASK-M6-UI-06-Events.md",
    "TASK-M6-UI-07.md": "TASK-M6-UI-07-Text-Rendering.md",
    "TASK-M6-UI-08.md": "TASK-M6-UI-08-Tooltips.md",
    "TASK-M6-UI-09.md": "TASK-M6-UI-09-Accessibility.md",
    "TASK-M6-UI-10.md": "TASK-M6-UI-10-Localization.md",
    "TASK-M6-UI-11.md": "TASK-M6-UI-11-Performance.md",
    "TASK-M6-UI-12.md": "TASK-M6-UI-12-Testing.md",
    "TASK-M6-UI-13.md": "TASK-M6-UI-13-Integration.md",
    "TASK-M6-UI-14.md": "TASK-M6-UI-14-Menu-Main.md",
    "TASK-M6-UI-15.md": "TASK-M6-UI-15-Menu-Inventory.md",
    "TASK-M6-UI-16.md": "TASK-M6-UI-16-Menu-Character.md",
    "TASK-M6-UI-17.md": "TASK-M6-UI-17-Menu-Settings.md",
}


def rename_all(mapping):
    count = 0
    for old, new in mapping.items():
        if os.path.exists(old):
            try:
                shutil.move(old, new)
                print(f"✓ {old} → {new}")
                count += 1
            except Exception as e:
                print(f"✗ {old}: {e}")
    return count


all_maps = [
    ("M3", m3_map),
    ("M4", m4_map),
    ("M5", m5_map),
    ("M6", m6_map),
]

for ms, mp in all_maps:
    print(f"\nRenaming {len(mp)} {ms} tasks...")
    count = rename_all(mp)
    print(f"{count}/{len(mp)} {ms} tasks renamed.")

print("\n✅ All done!")
