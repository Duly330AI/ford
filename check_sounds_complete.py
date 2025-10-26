#!/usr/bin/env python3
"""Check completeness of generated sounds against SOUND_ASSETS_LIST.md."""

import os
from pathlib import Path

# Categories and expected sound counts from SOUND_ASSETS_LIST.md
expected_sounds = {
    "ui": [
        "item_pickup", "item_drop", "inventory_open", "inventory_close",
        "button_hover", "button_click", "item_equip", "item_unequip",
        "crafting_begin", "crafting_complete", "crafting_fail",
        "quest_accept", "quest_complete", "notification"
    ],
    "foley": [
        "footstep_stone", "footstep_grass", "footstep_wood", "footstep_metal",
        "footstep_water", "footstep_sand", "dodge_roll", "dash_start", "dash_end",
        "jump", "torch_ignite", "torch_extinguish", "torch_ambient",
        "chest_open", "chest_close", "chest_locked_rattle",
        "lever_pull", "button_press", "door_open", "door_close", "door_locked"
    ],
    "weapon": [
        "sword_swing", "sword_hit_flesh", "sword_hit_armor",
        "axe_swing", "axe_hit_flesh", "axe_hit_wood",
        "hammer_swing", "hammer_hit_armor", "hammer_hit_stone",
        "staff_swing", "bow_draw", "bow_release", "arrow_flight",
        "arrow_hit_flesh", "arrow_hit_armor", "crossbow_load", "crossbow_fire",
        "parry_success", "parry_break", "hit_critical", "hit_miss"
    ],
    "magic": ["ember", "frost_nip", "spark", "illuminate", "minor_ward", "minor_cure",
              "fire_dart", "ice_shards", "venom_pin", "stone_skin", "mend", "cure", "detect_magic",
              "fireball", "deep_freeze", "arc_lance", "blink", "magic_shield", "earthen_grasp",
              "flame_wave", "blizzard", "toxic_mist", "chain_bolt", "earth_spikes", "dispel_magic",
              "inferno", "virulent_cloud", "mana_drain", "stone_ward_major", "silence_field",
              "meteor", "ice_coffin", "storm_pillar", "quicksand_maw", "plague_wind", "arcane_cascade"],
    "creature": [
        "player_hurt", "player_heal", "player_death", "npc_greet", "npc_hostile",
        "skeleton_attack", "zombie_attack", "headless_one_attack",
        "wraith_attack", "spectre_attack", "lich_attack", "lich_lord_attack",
        "mongbat_attack", "giant_rat_attack", "giant_spider_attack", "scorpion_attack",
        "harpy_attack", "giant_serpent_attack", "lizardman_attack",
        "orc_attack", "ratman_attack", "goblin_attack",
        "gargoyle_attack", "stone_gargoyle_attack",
        "troll_attack", "ogre_attack", "ettin_attack", "cyclops_attack", "titan_attack",
        "gazer_attack", "elder_gazer_attack",
        "earth_elemental_attack", "fire_elemental_attack", "air_elemental_attack", "water_elemental_attack",
        "reaper_attack", "daemon_attack", "balron_attack",
        "drake_attack", "wyvern_attack", "dragon_attack", "ancient_wyrm_attack"
    ],
    "trap": [
        "dart_fire", "poison_gas_release", "explosion_trigger", "explosion_detonate",
        "needle_prick", "fire_burst_trigger", "lava_loop", "pit_whoosh",
        "spikes_hit", "water_damage", "disarm_success", "disarm_fail", "detect_hidden"
    ],
    "ambient": [
        "dungeon_cave_loop", "forest_loop", "desert_loop",
        "rain_light", "rain_heavy", "lightning_strike"
    ],
    "combat": [
        "hit_impact_flesh", "hit_impact_metal", "hit_impact_rock", "hit_critical",
        "hit_resist", "status_poison_apply", "status_burn_apply", "status_freeze_apply",
        "status_stun_apply", "status_bleed_tick", "initiative_roll", "round_end",
        "victory", "defeat"
    ]
}

# Scan generated files
audio_sfx = Path("audio/sfx")
generated_by_category = {}

for category in expected_sounds.keys():
    category_path = audio_sfx / category
    if category_path.exists():
        files = list(category_path.glob("*.wav"))
        generated_by_category[category] = len(files)

print("=== SOUND GENERATION COMPLETENESS CHECK ===\n")

total_expected = sum(len(sounds) for sounds in expected_sounds.values())
total_generated = sum(generated_by_category.values())

print(f"Total Expected: {total_expected} sound concepts")
print(f"Total Generated: {total_generated} files")
print(f"Coverage: {total_generated / (total_expected * 1.5) * 100:.1f}% (accounting for variations)")
print()

# Category breakdown
for cat in sorted(expected_sounds.keys()):
    expected_count = len(expected_sounds[cat])
    generated_count = generated_by_category.get(cat, 0)
    status = "✓" if generated_count > 0 else "✗"
    print(f"{status} {cat:12s}: {generated_count:3d} files (expected ~{expected_count} concepts)")

print("\n=== MISSING MUSIC TRACKS ===")
music_path = Path("audio/music")
if music_path.exists():
    music_files = list(music_path.glob("*.wav"))
    print(f"Music files: {len(music_files)} (expected 12)")
else:
    print("Music directory missing!")
