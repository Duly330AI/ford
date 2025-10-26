#!/usr/bin/env python3
"""Add sound asset paths to data/ JSON files."""

import json
from pathlib import Path

# Mapping of spell IDs to their sound files
spell_sounds = {
    "ember": {
        "cast": "magic/ember_cast_v01.wav",
        "impact": "magic/ember_impact_v01.wav",
    },
    "frost_nip": {
        "cast": "magic/frost_nip_cast_v01.wav",
        "impact": "magic/frost_nip_impact_v01.wav",
    },
    "spark": {
        "cast": "magic/spark_cast_v01.wav",
        "impact": "magic/spark_impact_v01.wav",
    },
    "illuminate": {"cast": "magic/illuminate_cast_v01.wav"},
    "minor_ward": {
        "cast": "magic/minor_ward_cast_v01.wav",
        "loop": "magic/minor_ward_activate_loop_v01.wav",
    },
    "minor_cure": {"cast": "magic/minor_cure_cast_v01.wav"},
    "fire_dart": {
        "cast": "magic/fire_dart_cast_v01.wav",
        "impact": "magic/fire_dart_impact_hit_v01.wav",
    },
    "ice_shards": {
        "cast": "magic/ice_shards_cast_v01.wav",
        "impact": "magic/ice_shards_impact_v01.wav",
    },
    "venom_pin": {
        "cast": "magic/venom_pin_cast_v01.wav",
        "impact": "magic/venom_pin_impact_v01.wav",
        "loop": "magic/venom_pin_dot_loop_v01.wav",
    },
    "stone_skin": {
        "cast": "magic/stone_skin_cast_v01.wav",
        "loop": "magic/stone_skin_activate_loop_v01.wav",
    },
    "mend": {"cast": "magic/mend_cast_v01.wav", "impact": "magic/mend_impact_v01.wav"},
    "detect_magic": {
        "cast": "magic/detect_magic_cast_v01.wav",
        "reveal": "magic/detect_magic_reveal_v01.wav",
    },
    "cure": {"cast": "magic/cure_cast_v01.wav"},
    "fireball": {
        "cast": "magic/fireball_cast_v01.wav",
        "impact": "magic/fireball_impact_small_v01.wav",
        "loop": "magic/fireball_burn_loop_v01.wav",
    },
    "blink": {"cast": "magic/blink_cast_v01.wav"},
    "arc_lance": {
        "cast": "magic/arc_lance_cast_v01.wav",
        "impact": "magic/arc_lance_impact_v01.wav",
    },
    "earthen_grasp": {
        "cast": "magic/earthen_grasp_cast_v01.wav",
        "impact": "magic/earthen_grasp_impact_v01.wav",
    },
    "magic_shield": {
        "cast": "magic/magic_shield_cast_v01.wav",
        "loop": "magic/magic_shield_activate_loop_v01.wav",
        "absorb": "magic/magic_shield_absorb_v01.wav",
    },
    "deep_freeze": {
        "cast": "magic/deep_freeze_cast_v01.wav",
        "impact": "magic/deep_freeze_impact_v01.wav",
    },
    "flame_wave": {
        "cast": "magic/flame_wave_cast_v01.wav",
        "release": "magic/flame_wave_release_v01.wav",
        "impact": "magic/flame_wave_impact_v01.wav",
    },
    "blizzard": {
        "cast": "magic/blizzard_cast_v01.wav",
        "release": "magic/blizzard_release_v01.wav",
        "impact": "magic/blizzard_impact_v01.wav",
    },
    "toxic_mist": {
        "cast": "magic/toxic_mist_cast_v01.wav",
        "release": "magic/toxic_mist_release_v01.wav",
        "loop": "magic/toxic_mist_loop_v01.wav",
    },
    "chain_bolt": {
        "cast": "magic/chain_bolt_cast_v01.wav",
        "impact_direct": "magic/chain_bolt_impact_direct_v01.wav",
        "impact_chain": "magic/chain_bolt_impact_chain_v01.wav",
    },
    "earth_spikes": {
        "cast": "magic/earth_spikes_cast_v01.wav",
        "release": "magic/earth_spikes_release_v01.wav",
        "impact": "magic/earth_spikes_impact_v01.wav",
    },
    "dispel_magic": {
        "cast": "magic/dispel_magic_cast_v01.wav",
        "impact": "magic/dispel_magic_impact_v01.wav",
    },
    "inferno": {
        "cast": "magic/inferno_cast_v01.wav",
        "release": "magic/inferno_release_v01.wav",
        "loop": "magic/inferno_burn_loop_v01.wav",
    },
    "virulent_cloud": {
        "cast": "magic/virulent_cloud_cast_v01.wav",
        "release": "magic/virulent_cloud_release_v01.wav",
        "loop": "magic/virulent_cloud_loop_v01.wav",
    },
    "mana_drain": {
        "cast": "magic/mana_drain_cast_v01.wav",
        "impact": "magic/mana_drain_impact_v01.wav",
    },
    "stone_ward_major": {
        "cast": "magic/stone_ward_major_cast_v01.wav",
        "loop": "magic/stone_ward_major_activate_loop_v01.wav",
    },
    "silence_field": {
        "cast": "magic/silence_field_cast_v01.wav",
        "impact": "magic/silence_field_impact_v01.wav",
        "loop": "magic/silence_field_active_loop_v01.wav",
    },
    "meteor": {
        "cast": "magic/meteor_cast_v01.wav",
        "impact": "magic/meteor_impact_explosion_v01.wav",
        "loop": "magic/meteor_burn_loop_v01.wav",
    },
    "ice_coffin": {
        "cast": "magic/ice_coffin_cast_v01.wav",
        "activate": "magic/ice_coffin_activate_v01.wav",
    },
    "storm_pillar": {
        "cast": "magic/storm_pillar_cast_v01.wav",
        "release": "magic/storm_pillar_release_v01.wav",
        "impact": "magic/storm_pillar_impact_v01.wav",
    },
    "quicksand_maw": {
        "cast": "magic/quicksand_maw_cast_v01.wav",
        "release": "magic/quicksand_maw_release_v01.wav",
        "impact": "magic/quicksand_maw_impact_v01.wav",
    },
    "plague_wind": {
        "cast": "magic/plague_wind_cast_v01.wav",
        "release": "magic/plague_wind_release_v01.wav",
        "loop": "magic/plague_wind_loop_v01.wav",
    },
    "arcane_cascade": {
        "cast": "magic/arcane_cascade_cast_v01.wav",
        "release": "magic/arcane_cascade_release_v01.wav",
        "impact": "magic/arcane_cascade_impact_v01.wav",
    },
}

# Mapping of monster IDs to sound files
monster_sounds = {
    "goblin": {
        "attack": "creature/creature_goblin_attack_v01.wav",
        "hurt": "creature/creature_goblin_hurt_v01.wav",
        "death": "creature/creature_goblin_death_v01.wav",
    },
    "skeleton": {
        "attack_sword": "creature/creature_skeleton_attack_sword_v01.wav",
        "attack_punch": "creature/creature_skeleton_attack_punch_v01.wav",
        "hurt": "creature/creature_skeleton_hurt_v01.wav",
        "death": "creature/creature_skeleton_death_v01.wav",
    },
    "zombie": {
        "attack": "creature/creature_zombie_attack_v01.wav",
        "hurt": "creature/creature_zombie_hurt_v01.wav",
        "death": "creature/creature_zombie_death_v01.wav",
    },
    "headless_one": {
        "attack": "creature/creature_headless_one_attack_v01.wav",
        "hurt": "creature/creature_headless_one_hurt_v01.wav",
        "death": "creature/creature_headless_one_death_v01.wav",
    },
    "wraith": {
        "attack_spell": "creature/creature_wraith_attack_spell_v01.wav",
        "hurt": "creature/creature_wraith_hurt_v01.wav",
        "death": "creature/creature_wraith_death_v01.wav",
    },
    "spectre": {
        "attack_close": "creature/creature_spectre_attack_close_v01.wav",
        "attack_ranged": "creature/creature_spectre_attack_ranged_v01.wav",
        "hurt": "creature/creature_spectre_hurt_v01.wav",
        "death": "creature/creature_spectre_death_v01.wav",
    },
    "lich": {
        "attack": "creature/creature_lich_attack_spell_v01.wav",
        "hurt": "creature/creature_lich_hurt_v01.wav",
        "death": "creature/creature_lich_death_v01.wav",
    },
    "lich_lord": {
        "attack": "creature/creature_lich_lord_attack_spell_v01.wav",
        "hurt": "creature/creature_lich_lord_hurt_v01.wav",
        "death": "creature/creature_lich_lord_death_v01.wav",
    },
    "mongbat": {
        "attack": "creature/creature_mongbat_attack_v01.wav",
        "hurt": "creature/creature_mongbat_hurt_v01.wav",
        "death": "creature/creature_mongbat_death_v01.wav",
    },
    "giant_rat": {
        "attack": "creature/creature_giant_rat_attack_v01.wav",
        "hurt": "creature/creature_giant_rat_hurt_v01.wav",
        "death": "creature/creature_giant_rat_death_v01.wav",
    },
    "giant_spider": {
        "attack": "creature/creature_giant_spider_attack_bite_v01.wav",
        "hurt": "creature/creature_giant_spider_hurt_v01.wav",
        "death": "creature/creature_giant_spider_death_v01.wav",
    },
    "scorpion": {
        "attack": "creature/creature_scorpion_attack_tail_v01.wav",
        "hurt": "creature/creature_scorpion_hurt_v01.wav",
        "death": "creature/creature_scorpion_death_v01.wav",
    },
    "harpy": {
        "attack": "creature/creature_harpy_attack_claw_v01.wav",
        "hurt": "creature/creature_harpy_hurt_v01.wav",
        "death": "creature/creature_harpy_death_v01.wav",
    },
    "giant_serpent": {
        "attack": "creature/creature_giant_serpent_attack_bite_v01.wav",
        "hurt": "creature/creature_giant_serpent_hurt_v01.wav",
        "death": "creature/creature_giant_serpent_death_v01.wav",
    },
    "orc": {
        "attack": "creature/creature_orc_attack_sword_v01.wav",
        "hurt": "creature/creature_orc_hurt_v01.wav",
        "death": "creature/creature_orc_death_v01.wav",
    },
    "orc_mage": {
        "attack": "creature/creature_orc_mage_attack_v01.wav",
        "hurt": "creature/creature_orc_mage_hurt_v01.wav",
        "death": "creature/creature_orc_mage_death_v01.wav",
    },
    "orc_lord": {
        "attack": "creature/creature_orc_lord_attack_crush_v01.wav",
        "hurt": "creature/creature_orc_lord_hurt_v01.wav",
        "death": "creature/creature_orc_lord_death_v01.wav",
    },
    "ratman": {
        "attack": "creature/creature_ratman_attack_v01.wav",
        "hurt": "creature/creature_ratman_hurt_v01.wav",
        "death": "creature/creature_ratman_death_v01.wav",
    },
    "ratman_archer": {
        "attack": "creature/creature_ratman_archer_attack_v01.wav",
        "hurt": "creature/creature_ratman_archer_hurt_v01.wav",
        "death": "creature/creature_ratman_archer_death_v01.wav",
    },
    "ratman_mage": {
        "attack": "creature/creature_ratman_mage_attack_v01.wav",
        "hurt": "creature/creature_ratman_mage_hurt_v01.wav",
        "death": "creature/creature_ratman_mage_death_v01.wav",
    },
    "lizardman": {
        "attack": "creature/creature_lizardman_attack_melee_v01.wav",
        "hurt": "creature/creature_lizardman_hurt_v01.wav",
        "death": "creature/creature_lizardman_death_v01.wav",
    },
    "gargoyle": {
        "attack": "creature/creature_gargoyle_attack_melee_v01.wav",
        "hurt": "creature/creature_gargoyle_hurt_v01.wav",
        "death": "creature/creature_gargoyle_death_v01.wav",
    },
    "stone_gargoyle": {
        "attack": "creature/creature_stone_gargoyle_attack_crush_v01.wav",
        "hurt": "creature/creature_stone_gargoyle_hurt_v01.wav",
        "death": "creature/creature_stone_gargoyle_death_v01.wav",
    },
    "troll": {
        "attack": "creature/creature_troll_attack_melee_v01.wav",
        "hurt": "creature/creature_troll_hurt_v01.wav",
        "death": "creature/creature_troll_death_v01.wav",
    },
    "ogre": {
        "attack": "creature/creature_ogre_attack_crush_v01.wav",
        "hurt": "creature/creature_ogre_hurt_v01.wav",
        "death": "creature/creature_ogre_death_v01.wav",
    },
    "ogre_lord": {
        "attack": "creature/creature_ogre_lord_attack_crush_v01.wav",
        "hurt": "creature/creature_ogre_lord_hurt_v01.wav",
        "death": "creature/creature_ogre_lord_death_v01.wav",
    },
    "ettin": {
        "attack": "creature/creature_ettin_attack_club_v01.wav",
        "hurt": "creature/creature_ettin_hurt_v01.wav",
        "death": "creature/creature_ettin_death_v01.wav",
    },
    "cyclops": {
        "attack": "creature/creature_cyclops_attack_melee_v01.wav",
        "hurt": "creature/creature_cyclops_hurt_v01.wav",
        "death": "creature/creature_cyclops_death_v01.wav",
    },
    "titan": {
        "attack": "creature/creature_titan_attack_melee_v01.wav",
        "hurt": "creature/creature_titan_hurt_v01.wav",
        "death": "creature/creature_titan_death_v01.wav",
    },
    "gazer": {
        "attack": "creature/creature_gazer_attack_gaze_v01.wav",
        "hurt": "creature/creature_gazer_hurt_v01.wav",
        "death": "creature/creature_gazer_death_v01.wav",
    },
    "elder_gazer": {
        "attack": "creature/creature_elder_gazer_attack_gaze_v01.wav",
        "hurt": "creature/creature_elder_gazer_hurt_v01.wav",
        "death": "creature/creature_elder_gazer_death_v01.wav",
    },
    "earth_elemental": {
        "attack": "creature/creature_earth_elemental_attack_stomp_v01.wav",
        "hurt": "creature/creature_earth_elemental_hurt_v01.wav",
        "death": "creature/creature_earth_elemental_death_v01.wav",
    },
    "fire_elemental": {
        "attack": "creature/creature_fire_elemental_attack_melee_v01.wav",
        "hurt": "creature/creature_fire_elemental_hurt_v01.wav",
        "death": "creature/creature_fire_elemental_death_v01.wav",
    },
    "air_elemental": {
        "attack": "creature/creature_air_elemental_attack_close_v01.wav",
        "hurt": "creature/creature_air_elemental_hurt_v01.wav",
        "death": "creature/creature_air_elemental_death_v01.wav",
    },
    "water_elemental": {
        "attack": "creature/creature_water_elemental_attack_melee_v01.wav",
        "hurt": "creature/creature_water_elemental_hurt_v01.wav",
        "death": "creature/creature_water_elemental_death_v01.wav",
    },
    "reaper": {
        "attack": "creature/creature_reaper_attack_melee_v01.wav",
        "hurt": "creature/creature_reaper_hurt_v01.wav",
        "death": "creature/creature_reaper_death_v01.wav",
    },
    "daemon": {
        "attack": "creature/creature_daemon_attack_melee_v01.wav",
        "hurt": "creature/creature_daemon_hurt_v01.wav",
        "death": "creature/creature_daemon_death_v01.wav",
    },
    "balron": {
        "attack": "creature/creature_balron_attack_melee_v01.wav",
        "hurt": "creature/creature_balron_hurt_v01.wav",
        "death": "creature/creature_balron_death_v01.wav",
    },
    "drake": {
        "attack": "creature/creature_drake_attack_close_v01.wav",
        "hurt": "creature/creature_drake_hurt_v01.wav",
        "death": "creature/creature_drake_death_v01.wav",
    },
    "wyvern": {
        "attack": "creature/creature_wyvern_attack_melee_v01.wav",
        "hurt": "creature/creature_wyvern_hurt_v01.wav",
        "death": "creature/creature_wyvern_death_v01.wav",
    },
    "dragon": {
        "attack": "creature/creature_dragon_attack_melee_v01.wav",
        "hurt": "creature/creature_dragon_hurt_v01.wav",
        "death": "creature/creature_dragon_death_v01.wav",
    },
    "ancient_wyrm": {
        "attack": "creature/creature_ancient_wyrm_attack_melee_v01.wav",
        "hurt": "creature/creature_ancient_wyrm_hurt_v01.wav",
        "death": "creature/creature_ancient_wyrm_death_v01.wav",
    },
}

# Process spells.json
spells_path = Path("data/spells.json")
with open(spells_path, "r") as f:
    spells = json.load(f)

for spell in spells:
    spell_id = spell["id"]
    if spell_id in spell_sounds:
        spell["sounds"] = spell_sounds[spell_id]

with open(spells_path, "w") as f:
    json.dump(spells, f, indent=2)

print(
    f"✓ Updated spells.json with {len([s for s in spells if 'sounds' in s])} spell sounds"
)

# Process monsters.json
monsters_path = Path("data/monsters.json")
with open(monsters_path, "r") as f:
    monsters = json.load(f)

for monster in monsters:
    monster_id = monster["id"]
    if monster_id in monster_sounds:
        monster["sounds"] = monster_sounds[monster_id]

with open(monsters_path, "w") as f:
    json.dump(monsters, f, indent=2)

print(
    f"✓ Updated monsters.json with {len([m for m in monsters if 'sounds' in m])} monster sounds"
)
print("\n✅ Sound assets linked to data files!")
