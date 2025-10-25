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
- **Creatures & Interactions** (136+ sounds - ALL 42 enemies from monsters.json!)
- **Traps & Hazards** (20 sounds)
- **Environmental** (Ambience, Weather) (11 sounds)
- **Combat Events** (Impact, Status, Mechanics) (14 sounds)
- **Music** (Loopable, Adaptive) (12 pieces)

**Total:** ~291+ individual sounds + 12 music tracks

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

### Undead (Skeleton, Zombie, Headless One)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/skeleton_attack` | Skeleton attack | Hollow rattle, bone clash | 2 (sword, punch) |
| `creature/skeleton_hurt` | Skeleton takes damage | Bone cracking, hollow cry | 1 |
| `creature/skeleton_death` | Skeleton dies | Bones collapse, final clang | 1 |
| `creature/zombie_attack` | Zombie attack | Slow groan, wet hit | 1 |
| `creature/zombie_hurt` | Zombie takes damage | Gurgling, flesh tear | 1 |
| `creature/zombie_death` | Zombie dies | Final moan, body thud | 1 |
| `creature/headless_one_attack` | Headless One attack | Wet slash, armor crash | 1 |
| `creature/headless_one_hurt` | Headless One takes damage | Hollow impact, disoriented sound | 1 |
| `creature/headless_one_death` | Headless One dies | Final collision, body falls | 1 |

### Spirit Undead (Wraith, Spectre)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/wraith_attack` | Wraith attack (magic) | Spectral whoosh, supernatural | 2 (spell cast, touch) |
| `creature/wraith_hurt` | Wraith takes damage | Dissipating wail, ethereal scream | 1 |
| `creature/wraith_death` | Wraith dies | Fading wail, supernatural dissolution | 1 |
| `creature/wraith_appear` | Wraith materializes | Ghostly emergence, chilling tone | 1 |
| `creature/spectre_attack` | Spectre attack (magic) | Otherworldly zap, spectral burst | 2 (ranged, close) |
| `creature/spectre_hurt` | Spectre takes damage | Sharp supernatural cry | 1 |
| `creature/spectre_death` | Spectre dies | Fading scream, dissolution | 1 |
| `creature/spectre_appear` | Spectre materializes | Ominous emergence, unsettling tone | 1 |

### Liches (Lich, Lich Lord)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/lich_attack` | Lich attack (magic) | Powerful magical surge, dark energy | 2 (spell, touch) |
| `creature/lich_hurt` | Lich takes damage | Magical backlash, bone rattle | 1 |
| `creature/lich_death` | Lich dies | Magical explosion, bone shattering | 1 |
| `creature/lich_spell_prep` | Lich casting (loopable) | Dark energy buildup, ominous hum | 1 |
| `creature/lich_lord_attack` | Lich Lord attack (magic) | Massive magical surge, apocalyptic | 2 (spell, touch) |
| `creature/lich_lord_hurt` | Lich Lord takes damage | Catastrophic magical backlash | 1 |
| `creature/lich_lord_death` | Lich Lord dies | Massive magical explosion, reality tear | 1 |

### Vermin (Mongbat, Giant Rat)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/mongbat_attack` | Mongbat attack | Chittering screech, fluttering | 1 |
| `creature/mongbat_hurt` | Mongbat takes damage | High-pitched yelp | 1 |
| `creature/mongbat_death` | Mongbat dies | Final screech, body falls | 1 |
| `creature/mongbat_fly_loop` | Mongbat flying (loopable) | Fluttering wings, chittering | 1 |
| `creature/giant_rat_attack` | Giant Rat attack | Angry squeak, teeth chattering | 1 |
| `creature/giant_rat_hurt` | Giant Rat takes damage | Pain squeal | 1 |
| `creature/giant_rat_death` | Giant Rat dies | Final squeak, body collapse | 1 |

### Arachnids (Giant Spider, Scorpion)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/giant_spider_attack` | Giant Spider attack | Chittering hiss, fang strike | 2 (bite, web) |
| `creature/giant_spider_hurt` | Giant Spider takes damage | Clicking shriek | 1 |
| `creature/giant_spider_death` | Giant Spider dies | Final screech, legs collapse | 1 |
| `creature/giant_spider_crawl_loop` | Spider crawling (loopable) | Skittering legs, chittering | 1 |
| `creature/scorpion_attack` | Scorpion attack | Chittering snap, tail strike | 2 (tail sting, claw) |
| `creature/scorpion_hurt` | Scorpion takes damage | Sharp hiss | 1 |
| `creature/scorpion_death` | Scorpion dies | Final click, tail collapses | 1 |
| `creature/scorpion_venom_apply` | Scorpion poison proc | Sizzling venom injection | 1 |

### Flying Humanoids (Harpy)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/harpy_attack` | Harpy attack | Screeching slash, claw rend | 2 (claw, aerial) |
| `creature/harpy_hurt` | Harpy takes damage | Agonized scream | 1 |
| `creature/harpy_death` | Harpy dies | Final shriek, body crashes | 1 |
| `creature/harpy_fly_loop` | Harpy flying (loopable) | Wing fluttering, harsh cries | 1 |
| `creature/harpy_vocalize` | Harpy vocalization | Demonic screech, territorial | 1 |

### Reptiles (Giant Serpent, Lizardman)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/giant_serpent_attack` | Giant Serpent attack | Hissing strike, fang impact | 2 (bite, constrict) |
| `creature/giant_serpent_hurt` | Giant Serpent takes damage | Angry hiss/hissing wail | 1 |
| `creature/giant_serpent_death` | Giant Serpent dies | Final thrashing, collapse | 1 |
| `creature/giant_serpent_slither_loop` | Serpent slithering (loopable) | Sliding scales, occasional hiss | 1 |
| `creature/lizardman_attack` | Lizardman attack | Snarling slash, claws/weapon | 2 (melee, roar) |
| `creature/lizardman_hurt` | Lizardman takes damage | Hissing pain sound | 1 |
| `creature/lizardman_death` | Lizardman dies | Dying hiss, body thud | 1 |

### Humanoid Warriors (Orc, Ratman, Goblin)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/orc_attack` | Orc attack | Aggressive roar, weapon impact | 2 (sword, club) |
| `creature/orc_hurt` | Orc takes damage | Angry bellowing | 1 |
| `creature/orc_death` | Orc dies | Dying roar, body falls | 1 |
| `creature/orc_vocalize` | Orc vocalization | Intimidating growl, challenge | 1 |
| `creature/orc_mage_attack` | Orc Mage attack (magic) | Magical surge + warrior growl | 1 |
| `creature/orc_mage_hurt` | Orc Mage takes damage | Magical feedback + pain | 1 |
| `creature/orc_mage_death` | Orc Mage dies | Magical explosion + death cry | 1 |
| `creature/orc_lord_attack` | Orc Lord attack | Massive roar, heavy weapon impact | 2 (charge, crush) |
| `creature/orc_lord_hurt` | Orc Lord takes damage | Deep pain bellow | 1 |
| `creature/orc_lord_death` | Orc Lord dies | Final roar, heavy collapse | 1 |
| `creature/ratman_attack` | Ratman attack | Squeaking snarl, blade/claw | 1 |
| `creature/ratman_hurt` | Ratman takes damage | Pain squeak | 1 |
| `creature/ratman_death` | Ratman dies | Final death squeak | 1 |
| `creature/ratman_archer_attack` | Ratman Archer attack (ranged) | Twang + squeaking | 1 |
| `creature/ratman_archer_hurt` | Ratman Archer takes damage | Pained screech | 1 |
| `creature/ratman_archer_death` | Ratman Archer dies | Final death cry | 1 |
| `creature/ratman_mage_attack` | Ratman Mage attack (magic) | Magical surge + squeaking | 1 |
| `creature/ratman_mage_hurt` | Ratman Mage takes damage | Magical feedback + squeal | 1 |
| `creature/ratman_mage_death` | Ratman Mage dies | Magical explosion + death squeak | 1 |
| `creature/goblin_attack` | Goblin attack | Chittering yell, quick strike | 1 |
| `creature/goblin_hurt` | Goblin takes damage | Shrieking cry | 1 |
| `creature/goblin_death` | Goblin dies | Final squeal | 1 |

### Stone/Elemental (Gargoyle, Stone Gargoyle)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/gargoyle_attack` | Gargoyle attack | Stone grinding, claw swipe | 2 (ranged, melee) |
| `creature/gargoyle_hurt` | Gargoyle takes damage | Stone cracking, impact | 1 |
| `creature/gargoyle_death` | Gargoyle dies | Stone shattering, collapse | 1 |
| `creature/gargoyle_vocalize` | Gargoyle vocalization | Creepy stone groan | 1 |
| `creature/stone_gargoyle_attack` | Stone Gargoyle attack | Heavy stone grinding, impact | 2 (ranged, crush) |
| `creature/stone_gargoyle_hurt` | Stone Gargoyle takes damage | Heavy stone cracking | 1 |
| `creature/stone_gargoyle_death` | Stone Gargoyle dies | Massive stone shattering | 1 |
| `creature/stone_gargoyle_stomp` | Stone Gargoyle stomp (attack/movement) | Earth-shaking thud | 1 |

### Giant Humanoids (Troll, Ogre, Ogre Lord, Ettin)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/troll_attack` | Troll attack | Guttural roar, heavy weapon/claw | 2 (melee, grab) |
| `creature/troll_hurt` | Troll takes damage | Pained bellow | 1 |
| `creature/troll_death` | Troll dies | Dying roar, massive fall | 1 |
| `creature/troll_regenerate` | Troll regenerating (passive) | Flesh knitting, unsettling sound | 1 |
| `creature/ogre_attack` | Ogre attack | Deep roar, massive club/fist impact | 2 (crush, sweep) |
| `creature/ogre_hurt` | Ogre takes damage | Deep pain bellow | 1 |
| `creature/ogre_death` | Ogre dies | Final roar, earth-shaking fall | 1 |
| `creature/ogre_lord_attack` | Ogre Lord attack | Catastrophic roar, building impact | 2 (charge, crush) |
| `creature/ogre_lord_hurt` | Ogre Lord takes damage | Deep enraged roar | 1 |
| `creature/ogre_lord_death` | Ogre Lord dies | Massive death roar, ground shake | 1 |
| `creature/ettin_attack` | Ettin attack | Dual roars + double weapon impact | 2 (charge, club swing) |
| `creature/ettin_hurt` | Ettin takes damage | Bellowing dual pain sounds | 1 |
| `creature/ettin_death` | Ettin dies | Dual dying roars, crash | 1 |
| `creature/ettin_vocalize` | Ettin vocalization | Dual-headed argument/growl | 1 |

### Mythic Giants (Cyclops, Titan)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/cyclops_attack` | Cyclops attack | Deep thunderous roar, impact | 2 (melee, throw) |
| `creature/cyclops_hurt` | Cyclops takes damage | Enraged bellow | 1 |
| `creature/cyclops_death` | Cyclops dies | Final roar, apocalyptic fall | 1 |
| `creature/cyclops_stomp` | Cyclops stomp/movement | Earth-shattering thud | 1 |
| `creature/cyclops_eye_attack` | Cyclops eye attack (ranged) | Energy burst, magical zap | 1 |
| `creature/titan_attack` | Titan attack (magic/melee) | Apocalyptic roar + magical surge | 2 (melee, spell) |
| `creature/titan_hurt` | Titan takes damage | World-shaking cry | 1 |
| `creature/titan_death` | Titan dies | Massive magical explosion, death roar | 1 |
| `creature/titan_stomp` | Titan stomp/movement | World-shaking impact | 1 |

### Gazer/Eye Creatures

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/gazer_attack` | Gazer attack (magic/gaze) | Disorienting hum, eye beam zap | 2 (gaze, spell) |
| `creature/gazer_hurt` | Gazer takes damage | Pained wail | 1 |
| `creature/gazer_death` | Gazer dies | Disintegration sound, death cry | 1 |
| `creature/gazer_vocalize` | Gazer vocalization | Unsettling alien sound | 1 |
| `creature/elder_gazer_attack` | Elder Gazer attack (magic) | Powerful disorienting hum, beam | 2 (gaze, spell) |
| `creature/elder_gazer_hurt` | Elder Gazer takes damage | Pained screech | 1 |
| `creature/elder_gazer_death` | Elder Gazer dies | Magical disintegration, death | 1 |

### Elementals (Earth, Fire, Air, Water)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/earth_elemental_attack` | Earth Elemental attack | Stone grinding, ground shake | 2 (stomp, throw) |
| `creature/earth_elemental_hurt` | Earth Elemental takes damage | Cracking stone, rumble | 1 |
| `creature/earth_elemental_death` | Earth Elemental dies | Massive stone collapse | 1 |
| `creature/earth_elemental_move_loop` | Earth Elemental moving (loopable) | Heavy grinding, rumbling | 1 |
| `creature/fire_elemental_attack` | Fire Elemental attack | Roaring flames, sizzle | 2 (melee, ranged) |
| `creature/fire_elemental_hurt` | Fire Elemental takes damage | Sizzling, reduced roar | 1 |
| `creature/fire_elemental_death` | Fire Elemental dies | Final roar, extinguishing sound | 1 |
| `creature/fire_elemental_ambient_loop` | Fire Elemental ambient (loopable) | Crackling fire, roaring | 1 |
| `creature/air_elemental_attack` | Air Elemental attack | Shrieking wind, impact | 2 (ranged, close) |
| `creature/air_elemental_hurt` | Air Elemental takes damage | Wind dissipation, fading | 1 |
| `creature/air_elemental_death` | Air Elemental dies | Final wind gust, dispersal | 1 |
| `creature/air_elemental_move_loop` | Air Elemental moving (loopable) | Howling wind, whistling | 1 |
| `creature/water_elemental_attack` | Water Elemental attack | Splashing surge, drowning sound | 2 (melee, ranged) |
| `creature/water_elemental_hurt` | Water Elemental takes damage | Water bubbling, distortion | 1 |
| `creature/water_elemental_death` | Water Elemental dies | Water draining away | 1 |
| `creature/water_elemental_move_loop` | Water Elemental moving (loopable) | Sloshing water, flowing | 1 |

### Death Creatures (Reaper, Daemon, Balron)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/reaper_attack` | Reaper attack (scythe) | Deathly whoosh, supernatural impact | 2 (melee, instant death) |
| `creature/reaper_hurt` | Reaper takes damage | Unsettling wail, reality distortion | 1 |
| `creature/reaper_death` | Reaper dies | Massive supernatural discharge, dissolution | 1 |
| `creature/reaper_vocalize` | Reaper vocalization | Haunting death knell | 1 |
| `creature/daemon_attack` | Daemon attack (magic/claw) | Demonic roar + magical surge | 2 (melee, spell) |
| `creature/daemon_hurt` | Daemon takes damage | Demonic screech | 1 |
| `creature/daemon_death` | Daemon dies | Demonic explosion, otherworldly dissolution | 1 |
| `creature/daemon_laugh` | Daemon laugh (taunt) | Evil laugh, demonic | 1 |
| `creature/balron_attack` | Balron attack (ultimate demon) | Apocalyptic roar + massive magical surge | 3 (melee, spell, world-shaking) |
| `creature/balron_hurt` | Balron takes damage | Demonic world-shaking scream | 1 |
| `creature/balron_death` | Balron dies | Apocalyptic explosion, massive fire, demonic wail | 1 |
| `creature/balron_summon` | Balron summoned/appears | Reality-tearing emergence, demonic roar | 1 |

### Dragons & Flying Dragons (Drake, Wyvern, Dragon, Ancient Wyrm)

| Sound ID | Enemy Type | Characteristics | Variations |
|----------|-----------|-----------------|------------|
| `creature/drake_attack` | Drake attack (magic/fire) | Dragon roar + magical surge | 2 (ranged, close) |
| `creature/drake_hurt` | Drake takes damage | Angry dragon screech | 1 |
| `creature/drake_death` | Drake dies | Dying roar, crash | 1 |
| `creature/drake_fly_loop` | Drake flying (loopable) | Wing fluttering, occasional roar | 1 |
| `creature/drake_breath` | Drake breath attack | Building magical surge + fire breath | 1 |
| `creature/wyvern_attack` | Wyvern attack (melee/bite) | Hissing roar, bite/claw impact | 2 (melee, aerial) |
| `creature/wyvern_hurt` | Wyvern takes damage | Pained roar | 1 |
| `creature/wyvern_death` | Wyvern dies | Dying roar, aerial crash | 1 |
| `creature/wyvern_fly_loop` | Wyvern flying (loopable) | Wing fluttering, hissing | 1 |
| `creature/dragon_attack` | Dragon attack (magic/fire) | Majestic roar + massive magical surge | 2 (fire breath, close melee) |
| `creature/dragon_hurt` | Dragon takes damage | Enraged roar, scales rattling | 1 |
| `creature/dragon_death` | Dragon dies | Long dying wail, crash, fire extinction | 1 |
| `creature/dragon_fly_loop` | Dragon flying (loopable) | Powerful wing fluttering, occasional roar | 1 |
| `creature/dragon_breath` | Dragon breath attack (fire) | Building inferno, massive fire breath | 1 |
| `creature/dragon_roar_warning` | Dragon roar/vocalization | Majestic, threatening, territorial | 2 (warning, attack) |
| `creature/ancient_wyrm_attack` | Ancient Wyrm attack (ultimate dragon) | Apocalyptic roar + catastrophic magic | 3 (breath, melee, world-shaking) |
| `creature/ancient_wyrm_hurt` | Ancient Wyrm takes damage | World-shaking enraged roar | 1 |
| `creature/ancient_wyrm_death` | Ancient Wyrm dies | Apocalyptic death roar, massive explosion, fire extinction | 1 |
| `creature/ancient_wyrm_fly_loop` | Ancient Wyrm flying (loopable) | Thunderous wing fluttering, apocalyptic aura | 1 |
| `creature/ancient_wyrm_breath` | Ancient Wyrm breath (mega) | Catastrophic inferno buildup, apocalyptic fire breath | 1 |
| `creature/ancient_wyrm_roar` | Ancient Wyrm roar (taunt) | Ancient, powerful, reality-shaking | 1 |

### Enemy Detection & Reactions

| Sound ID | Description | Characteristics | Variations |
|----------|-------------|-----------------|------------|
| `creature/enemy_notice` | Enemy spots player | Alert sound, low growl | 2 (aggressive, cautious) |
| `creature/enemy_lose_sight` | Enemy loses target | Uncertain question tone, departure | 1 |
| `creature/enemy_aggro` | Enemy becomes aggressive | Growl/roar/vocalization escalation | 3 (melee, caster, boss) |
| `creature/taunt` | Enemy taunting player | Varies by creature type | 3 (laugh, roar, shriek) |

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
| Creatures | **136+** | **Player (3), NPCs (2), Undead (9), Spirits (8), Liches (7), Vermin (7), Arachnids (8), Harpies (5), Reptiles (5), Humanoids (21), Gargoyles (8), Giants (12), Gazers (6), Elementals (12), Death creatures (12), Dragons (21), Detection (4)** |
| Traps | 20 | Mechanisms (9), hazards (4), disarm/detection (3) |
| Environmental | 11 | Biome ambience (6), weather (2) |
| Combat Events | 14 | Impacts (4), status (5), flow (5) |
| **Music** | **12** | **Exploration (3), Combat (3), Special (6)** |
| **TOTAL** | **~291+ sounds + 12 tracks** | **NEW: 100+ creature sounds added!** |

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

### Example Request

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
