# FORD • Sound Assets - Complete Generation List

**Purpose:** Comprehensive sound effects and music requirements for FORD audio generation.
**Status:** Generation Reference
**Format:** Organized by category for ChatGPT/AI generation
**Last Updated:** 2025-10-26

---

## 📋 Overview

This document lists **all required sounds** for FORD, organized by functional category:
- **UI Sounds** (14 sounds)
- **Foley** (Footsteps, Materials) (28 sounds)
- **Weapons** (Melee, Ranged) (24 sounds)
- **Magic & Spells** (32 sounds)
- **Creatures & Interactions** (36 sounds)
- **Traps & Hazards** (20 sounds)
- **Environmental** (Ambience, Weather) (20 sounds)
- **Combat Events** (Impact, Status, Mechanics) (18 sounds)
- **Music** (Loopable, Adaptive) (12 pieces)

**Total:** ~204 individual sounds + 12 music tracks

---

## 🎮 **Category 1: UI Sounds**

### Inventory & Item Management
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `ui/item_pickup` | Item picked up | Bright, satisfying, ~0.3s | 2 (light, heavy) |
| `ui/item_drop` | Item dropped on ground | Thud, softer than pickup | 2 (light, heavy) |
| `ui/inventory_open` | Menu opens (inventory, character, etc.) | Whoosh, modern UI tone | 1 |
| `ui/inventory_close` | Menu closes | Reverse whoosh or gentle pop | 1 |
| `ui/button_hover` | Mouse hovers over button | Subtle beep/ping | 1 |
| `ui/button_click` | Button clicked/selected | Satisfying click or chirp | 2 (confirm, cancel) |
| `ui/item_equip` | Item equipped (armor/weapon) | Metallic clink or whoosh | 3 (armor, weapon, shield) |
| `ui/item_unequip` | Item unequipped | Reverse of equip, lighter | 3 (armor, weapon, shield) |
| `ui/crafting_begin` | Crafting starts | Positive chime, gathering tools | 1 |
| `ui/crafting_complete` | Crafting successful | Triumphant ping/bell | 1 |
| `ui/crafting_fail` | Crafting failed | Sad buzzer or clunk | 1 |
| `ui/quest_accept` | Quest accepted | Uplifting chime/notification | 1 |
| `ui/quest_complete` | Quest completed | Celebratory jingle | 1 |
| `ui/notification` | Generic notification/alert | Soft bell or beep | 2 (positive, neutral) |

---

## 🚶 **Category 2: Foley (Movement & Materials)**

### Footsteps (by Surface Tag)
| Sound ID | Surface | Characteristics | Variations |
|----------|---------|-----------------|------------|
| `foley/footstep_stone` | Tile, Corridor, Cavern (stone) | Solid click/clack, reverb in caves | 4 (light, medium, heavy, running) |
| `foley/footstep_grass` | Grass, vegetation | Soft shuffle, rustle | 3 (light, medium, heavy) |
| `foley/footstep_wood` | Wooden floors (bridges, decks) | Hollow thud, creaky | 3 (light, medium, heavy) |
| `foley/footstep_metal` | Metal grates, platforms | Rang, metallic clink | 3 (light, medium, heavy) |
| `foley/footstep_water` | Shallow water, puddles | Splish/splash, squishy | 3 (light, medium, heavy) |
| `foley/footstep_sand` | Desert/sandy areas | Soft crunch | 2 (light, heavy) |

### Movement & Interactions
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `foley/dodge_roll` | Dodge-roll performed (Spacebar) | Whoosh, armor jingle | 1 |
| `foley/dash_start` | Sprint/boost start | Quick intake of breath or burst | 1 |
| `foley/dash_end` | Sprint ends | Breathing, recovery | 1 |
| `foley/jump` | Jump (if applicable) | Impact on landing | 1 |
| `foley/torch_ignite` | Torch lit/brought out | Match strike, flame whoosh | 1 |
| `foley/torch_extinguish` | Torch blown out | Sudden silence/sizzle | 1 |
| `foley/torch_ambient` | Torch crackling (loopable) | Steady crackle, ~30s loop | 3 (small, medium, roaring) |

### Container & Furniture
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `foley/chest_open` | Chest/container opens | Creaky hinges, wood settling | 2 (small, large) |
| `foley/chest_close` | Chest/container closes | Soft thud, lid settling | 2 (small, large) |
| `foley/chest_locked_rattle` | Attempt to open locked container | Keys rattle inside | 1 |
| `foley/lever_pull` | Lever activated | Mechanical clunk, stone rumble | 1 |
| `foley/button_press` | Button/switch pressed | Click, mechanical | 1 |
| `foley/door_open` | Door opens (stone/wood) | Creak, possible stone scrape | 2 (normal, dungeon) |
| `foley/door_close` | Door closes | Thud, possible lock | 2 (normal, dungeon) |
| `foley/door_locked` | Try to open locked door | Rattle, denial tone | 1 |

---

## ⚔️ **Category 3: Weapons (Melee & Ranged)**

### Melee Attacks
| Sound ID | Weapon Type | Characteristics | Variations |
|----------|------------|-----------------|------------|
| `weapon/sword_swing` | Swords | Whoosh, clean arc | 3 (light swing, heavy swing, clash) |
| `weapon/sword_hit_flesh` | Sword → Flesh | Wet impact, organic | 2 (light, heavy) |
| `weapon/sword_hit_armor` | Sword → Armor/Metal | Metallic clang | 2 (light, glancing) |
| `weapon/axe_swing` | Axes | Heavier whoosh, cutting intent | 2 (light, heavy) |
| `weapon/axe_hit_flesh` | Axe → Flesh | Thud + wet sound | 1 |
| `weapon/axe_hit_wood` | Axe → Wood/doors | Solid chunk | 1 |
| `weapon/hammer_swing` | Hammers, Maces | Weighty whoosh | 2 (light, heavy) |
| `weapon/hammer_hit_armor` | Hammer → Metal | Ringing impact | 2 (light, heavy) |
| `weapon/hammer_hit_stone` | Hammer → Stone | Percussive clunk | 1 |
| `weapon/staff_swing` | Staves | Swishy whoosh, wood resonance | 2 (light, casting) |

### Ranged Attacks
| Sound ID | Weapon Type | Characteristics | Variations |
|----------|------------|-----------------|------------|
| `weapon/bow_draw` | Bow draw (on fire) | Twang, arrow nocking | 1 |
| `weapon/bow_release` | Arrow released | Clean snap | 1 |
| `weapon/arrow_flight` | Arrow in flight | Whistle, whoosh (if close) | 1 |
| `weapon/arrow_hit_flesh` | Arrow → Flesh | Wet thunk | 1 |
| `weapon/arrow_hit_armor` | Arrow → Metal/Hard surface | Ping, deflection | 2 (penetrate, ricochet) |
| `weapon/crossbow_load` | Crossbow cocking | Mechanical click/clunk | 1 |
| `weapon/crossbow_fire` | Crossbow release | Heavier twang than bow | 1 |

### Impacts & Parry
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `weapon/parry_success` | Successful parry/block | Metallic clang, satisfying | 2 (metal, wood) |
| `weapon/parry_break` | Parry overwhelmed | Harsher clash, cracking | 1 |
| `weapon/hit_critical` | Critical hit indicator | Distinctive sharp crack + chime | 1 |
| `weapon/hit_miss` | Attack misses | Whoosh, impact in air/ground | 1 |

---

## 🔥 **Category 4: Magic & Spells**

### Fire School
| Sound ID | Spell | Characteristics | Variations |
|----------|-------|-----------------|------------|
| `magic/fireball_cast` | Fireball | Powerful ignition whoosh + roar | 1 |
| `magic/fireball_impact` | Fireball explosion | Boom, crackling, resonant | 2 (small, large area) |
| `magic/flamewave_cast` | Flame Wave | Sweeping fire rush | 1 |
| `magic/flamewave_impact` | Flame Wave hits | Crackling sweep, ongoing burn | 1 |
| `magic/fireblast_cast` | Fire Blast (beam) | High-pitched ignition | 1 |

### Cold/Frost School
| Sound ID | Spell | Characteristics | Variations |
|----------|-------|-----------------|------------|
| `magic/frost_bolt_cast` | Frost Bolt | Crystalline shimmer + crackle | 1 |
| `magic/frost_bolt_impact` | Frost Bolt hits | Shattering ice, freeze proc | 1 |
| `magic/ice_storm_cast` | Ice Storm | Swirling wind + ice crackling | 1 |
| `magic/ice_storm_impact` | Ice Storm AoE hits | Multiple shatters, sustained cold | 1 |

### Poison/Toxic School
| Sound ID | Spell | Characteristics | Variations |
|----------|-------|-----------------|------------|
| `magic/poison_cloud_cast` | Poison Cloud | Sickly hiss, gurgling | 1 |
| `magic/poison_cloud_impact` | Cloud engulfs | Toxic bubbling, DoT indicator | 1 |

### Energy/Lightning School
| Sound ID | Spell | Characteristics | Variations |
|----------|-------|-----------------|------------|
| `magic/lightning_bolt_cast` | Lightning Bolt | Crackling charge-up + zap | 1 |
| `magic/lightning_bolt_impact` | Lightning hits | Sharp crack, electrical buzz | 2 (direct, chain) |
| `magic/chain_lightning_cast` | Chain Lightning | Multiple crackles, building energy | 1 |

### Healing & Support
| Sound ID | Spell | Characteristics | Variations |
|----------|-------|-----------------|------------|
| `magic/healing_cast` | Heal/Cure Spell | Gentle shimmer, positive chime | 2 (minor, major) |
| `magic/healing_complete` | Healing received | Warm glow tone, restoration | 1 |
| `magic/buff_cast` | Buff spell (str/dex/int) | Empowering chime, ascending note | 3 (physical, agility, intellect) |
| `magic/dispel_cast` | Dispel Magic | Unraveling shimmer | 1 |

### Casting Mechanics
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `magic/spell_fizzle` | Spell fizzled (failed) | Sad trombone, failed energy burst | 1 |
| `magic/casting_loop` | Casting in progress (loopable) | Humming energy, building tension | 1 |
| `magic/mana_deplete` | Mana exhausted | Sad buzzer, energy cutoff | 1 |
| `magic/reagent_consumed` | Reagents consumed | Quick whoosh/sparkle | 1 |

---

## 👹 **Category 5: Creatures & Interactions**

### Player & NPC Vocalizations
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `creature/player_hurt` | Player takes damage (vocalization) | Grunt, pain sound, variable | 3 (light, medium, heavy) |
| `creature/player_heal` | Player heals/recovers | Satisfied sigh, relief | 1 |
| `creature/player_death` | Player defeated | Final gasp or yelp | 1 |
| `creature/npc_greet` | NPC greeting/speech | Generic mumble or "hello" | 2 (friendly, neutral) |
| `creature/npc_hostile` | NPC becomes hostile | Aggressive growl or warning | 1 |

### Common Enemy Types
| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/skeleton_attack` | Skeleton attack | Hollow rattle, bone clash | 2 (sword, punch) |
| `creature/skeleton_hurt` | Skeleton takes damage | Bone cracking, hollow cry | 1 |
| `creature/skeleton_death` | Skeleton dies | Bones collapse, final clang | 1 |
| `creature/zombie_attack` | Zombie attack | Slow groan, wet hit | 1 |
| `creature/zombie_hurt` | Zombie takes damage | Gurgling, flesh tear | 1 |
| `creature/zombie_death` | Zombie dies | Final moan, body thud | 1 |
| `creature/goblin_attack` | Goblin/Imp attack | Chittering yell, quick strike | 1 |
| `creature/goblin_hurt` | Goblin takes damage | Shrieking cry | 1 |
| `creature/goblin_death` | Goblin dies | Final squeal | 1 |
| `creature/ettin_attack` | Ettin/Large creature attack | Deep roar + weapon impact | 2 (charge, club swing) |
| `creature/ettin_hurt` | Ettin takes damage | Bellowing pain sound | 1 |
| `creature/ettin_death` | Ettin dies | Dying roar, crash | 1 |
| `creature/dragon_roar` | Dragon roar/vocalization | Majestic, threatening roar | 2 (warning, attack) |
| `creature/dragon_hurt` | Dragon takes damage | Angry shriek, scales rattle | 1 |
| `creature/dragon_death` | Dragon dies | Long dying wail, crash | 1 |

### Enemy Detection
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `creature/enemy_notice` | Enemy spots player | Alert sound, low growl | 1 |
| `creature/enemy_lose_sight` | Enemy loses target | Uncertain question tone, departure | 1 |

---

## 🪤 **Category 6: Traps & Hazards**

### Trap Mechanisms
| Sound ID | Trap Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `trap/dart_fire` | Dart trap fires | Mechanical click + dart whiz | 1 |
| `trap/dart_hit` | Dart hits player | Sharp sting, minimal impact | 1 |
| `trap/poison_gas_release` | Poison gas trigger | Hissing release, toxic bubble | 1 |
| `trap/poison_gas_tick` | Poison damage tick | Sickly gurgle (loopable) | 1 |
| `trap/explosion_trigger` | Explosion trap activates | Fuse burn sizzle | 1 |
| `trap/explosion_detonate` | Explosion detonates | Boom, ringing aftermath | 2 (small, large) |
| `trap/needle_prick` | Needle trap triggers | Light sting sound | 1 |
| `trap/fire_burst_trigger` | Fire burst releases | Quick ignition whoosh | 1 |
| `trap/fire_burst_flame` | Fire burst active | Crackling, roaring fire | 1 |

### Environmental Hazards
| Sound ID | Hazard | Characteristics | Variations |
|----------|--------|-----------------|------------|
| `trap/lava_loop` | Lava ambience (loopable) | Bubbling, crackling heat | 1 |
| `trap/pit_whoosh` | Falling into pit | Wind rush, impact at bottom | 2 (small, deep) |
| `trap/spikes_hit` | Spike trap damage | Sharp puncture, cry | 1 |
| `trap/water_damage` | Water hazard damage (drain) | Sizzle, drain sound | 1 |

### Trap Disarm
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `trap/disarm_success` | Trap successfully disarmed | Satisfying click, mechanics stop | 1 |
| `trap/disarm_fail` | Trap disarm failed | Trap still triggers anyway | 1 |
| `trap/detect_hidden` | Hidden object detected | Discovery chime, reveal sound | 1 |

---

## 🌍 **Category 7: Environmental & Ambience**

### Biome Ambience (Loopable)
| Sound ID | Biome | Characteristics | Variations |
|----------|-------|-----------------|------------|
| `ambient/dungeon_cave_loop` | Dungeon/Cave | Distant drips, hollow echo, air movement | 3 (wet cave, dry crypt, stone dungeon) |
| `ambient/forest_loop` | Forest Biome | Birds, wind through trees, rustling | 2 (day, night) |
| `ambient/desert_loop` | Desert Biome | Wind howl, sand shift, desolate | 1 |
| `ambient/ancient_temple_loop` | Ruins/Ancient Temple | Creaks, settling stone, mystery tone | 1 |
| `ambient/underground_city_loop` | Underground City/Settlement | Distant machinery, echoes, activity hum | 1 |
| `ambient/necropolis_loop` | Necropolis/Undead Lair | Eerie silence, distant wails, supernatural | 1 |

### Weather & Dynamic (if applicable)
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `ambient/rain_light` | Light rain (loopable) | Soft patter, background | 1 |
| `ambient/rain_heavy` | Heavy rain (loopable) | Loud downpour, thunder distant | 1 |
| `ambient/lightning_strike` | Lightning strike | Instant crack, boom reverb | 2 (close, distant) |

---

## ⚡ **Category 8: Combat Events & Status**

### Hit & Damage Feedback
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `combat/hit_impact_flesh` | General hit on flesh | Organic impact, pain indicator | 2 (light, heavy) |
| `combat/hit_impact_metal` | General hit on metal/armor | Metallic ring | 2 (light, heavy) |
| `combat/hit_impact_rock` | General hit on stone | Percussive thud | 1 |
| `combat/hit_critical` | Critical hit **visual** feedback | Distinctive "pop" or sharp chime | 1 |
| `combat/hit_resist` | Damage resisted/blocked | Protective shimmer sound | 1 |

### Status Effects Applied
| Sound ID | Effect | Characteristics | Variations |
|----------|--------|-----------------|------------|
| `combat/status_poison_apply` | Poison applied | Hissing, toxicity tone | 1 |
| `combat/status_burn_apply` | Burn effect applied | Quick sizzle | 1 |
| `combat/status_freeze_apply` | Freeze/chill applied | Crystalline crackle | 1 |
| `combat/status_stun_apply` | Stun effect applied | Disorienting buzz, impact | 1 |
| `combat/status_bleed_tick` | Bleeding damage tick (loopable) | Steady drip, pain tone | 1 |

### Combat Flow
| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `combat/initiative_roll` | Initiative rolled (turn starts) | Quick dice roll or attention chime | 1 |
| `combat/round_end` | Combat round ends | Transition chime, turn over | 1 |
| `combat/victory` | Combat victory | Triumphant fanfare, short | 1 |
| `combat/defeat` | Combat defeat | Sad theme, game over | 1 |

---

## 🎵 **Category 9: Music (Loopable Tracks)**

### Ambient/Exploration
| Track ID | Purpose | BPM | Characteristics | Length |
|----------|---------|-----|-----------------|--------|
| `music/exploration_default` | General dungeon exploration | ~80–100 | Mysterious, ambient, non-intrusive | 3–4 min loop |
| `music/exploration_forest` | Forest biome exploration | ~90–110 | Nature-inspired, calming yet alert | 3–4 min loop |
| `music/exploration_desert` | Desert biome exploration | ~85–100 | Desolate, echoing, sparse instrumentation | 3–4 min loop |

### Combat
| Track ID | Purpose | BPM | Characteristics | Length |
|----------|---------|-----|-----------------|--------|
| `music/combat_default` | Standard combat encounter | ~120–140 | Energetic, driving rhythm, heroic | 2–3 min loop |
| `music/combat_boss` | Boss/named encounter | ~130–160 | Threatening, epic, memorable motif | 3–4 min loop |
| `music/combat_wave` | Wave/multi-enemy combat | ~110–130 | Rising tension, rhythmic build | 2–3 min loop |

### Special Scenarios
| Track ID | Purpose | BPM | Characteristics | Length |
|----------|---------|-----|-----------------|--------|
| `music/boss_final` | Final boss / climax | ~140–180 | Intense, personal, heroic struggle | 4–5 min loop |
| `music/victory_fanfare` | After combat victory | ~120 | Celebratory, satisfying, brief | 0:30–1:00 |
| `music/death_theme` | Upon player death / defeat | ~60–80 | Mournful, resigned, short | 1–2 min |
| `music/menu_theme` | Main menu / ambient idle | ~90–110 | Welcoming, mysterious, immersive | 3–4 min loop |
| `music/tutorial_theme` | Tutorial / FTUE overlay | ~100–120 | Instructive, light, encouraging | 2–3 min loop |

---

## 📊 Summary Table

| Category | Count | Notes |
|----------|-------|-------|
| UI Sounds | 14 | Menu, inventory, buttons |
| Foley | 28 | Footsteps (6 surfaces), movement, containers |
| Weapons | 24 | Melee (10), ranged (6), impacts (4) |
| Magic | 32 | Fire (5), Frost (4), Poison (2), Energy (4), Healing (4), Casting (4) |
| Creatures | 36 | Player vocalizations (3), NPCs (2), enemies (16), detection (2) |
| Traps | 20 | Mechanisms (9), hazards (4), disarm/detection (3) |
| Environmental | 11 | Biome ambience (6), weather (2) |
| Combat Events | 14 | Impacts (4), status (5), flow (5) |
| **Music** | **12** | **Exploration (3), Combat (3), Special (6)** |
| **TOTAL** | **~191 sounds + 12 tracks** | |

---

## 🎯 Generation Guidelines for ChatGPT

When requesting sound generation, use this structure:

```
Category: [UI / Foley / Weapons / Magic / Creatures / Traps / Environmental / Combat]
Sound ID: [e.g., weapon/sword_swing]
Description: [What the sound does / when heard]
Characteristics: [Tone, duration, unique qualities]
Variations: [Number of versions needed, different flavors]
Reference Files: [If applicable, existing CC0 sounds to match]
```

### Example Request:
```
Category: Weapons
Sound ID: weapon/sword_swing
Description: Sword swing sound effect (clean arc through air)
Characteristics: Whoosh, clean transient attack, ~0.3s, metallic undertone
Variations: 3 (light swing, heavy swing, armor clash variant)
Target: Retro RPG / pixel art fantasy game
```

---

## 📝 Notes

- **All sounds must be CC0 / royalty-free** for use in public release.
- **Variations** are important for avoiding repetition in gameplay.
- **Loopable tracks** should have clean attack/decay to allow seamless looping.
- **Volume normalized** to -18 LUFS (SFX) and -14 LUFS (Music) where applicable.
- **Biome tagging** in filenames (e.g., `footstep_stone_cave_v01.wav` vs. `footstep_stone_crypt_v02.wav`) helps designers switch context-based sounds.

---

## 📌 Asset Organization Structure

```
audio/
├── sfx/
│   ├── ui/
│   │   ├── item_pickup_v01.wav
│   │   ├── button_click_v01.wav
│   │   └── ...
│   ├── foley/
│   │   ├── footstep_stone_light_v01.wav
│   │   ├── footstep_grass_heavy_v02.wav
│   │   └── ...
│   ├── weapon/
│   │   ├── sword_swing_light_v01.wav
│   │   ├── sword_hit_flesh_v01.wav
│   │   └── ...
│   ├── magic/
│   │   ├── fireball_cast_v01.wav
│   │   ├── frost_bolt_impact_v01.wav
│   │   └── ...
│   ├── creature/
│   │   ├── skeleton_attack_v01.wav
│   │   ├── dragon_roar_warning_v01.wav
│   │   └── ...
│   ├── trap/
│   │   ├── dart_fire_v01.wav
│   │   ├── explosion_detonate_large_v01.wav
│   │   └── ...
│   ├── ambient/
│   │   ├── dungeon_cave_wet_v01.wav
│   │   ├── rain_heavy_v01.wav
│   │   └── ...
│   └── combat/
│       ├── hit_impact_flesh_light_v01.wav
│       ├── status_poison_apply_v01.wav
│       └── ...
└── music/
    ├── exploration_default_v01.wav
    ├── combat_boss_v01.wav
    ├── victory_fanfare_v01.wav
    └── ...
```

---

**Prepared by:** FORD Development Team
**For:** Audio asset generation via AI tools (ChatGPT, Suno, ElevenLabs, etc.)
**Last Updated:** 2025-10-26
