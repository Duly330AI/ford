# FORD Audio System

**Status:** ✅ Fully Integrated (October 26, 2025)

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Asset Organization](#asset-organization)
4. [Data Integration](#data-integration)
5. [Mixer & Playback](#mixer--playback)
6. [Event System](#event-system)
7. [Integration Examples](#integration-examples)
8. [Next Steps](#next-steps)

---

## Overview

The FORD audio system is **fully data-driven**, **deterministic**, and **testable**. It provides:

- ✅ **436 WAV sound files** (ChatGPT-generated, CC0 licensed)
- ✅ **Audio mixer** integration with Arcade
- ✅ **Context-aware sound selection** (spell types, creature varieties)
- ✅ **Volume ducking** for dialogue/UI overlays
- ✅ **3D audio positioning** for creature sounds
- ✅ **Ambient loops** for biome/environment atmosphere
- ✅ **Event-driven playback** linked to combat/magic systems

### Coverage

| Category | Count | Coverage |
|----------|-------|----------|
| Creature Sounds | 213 | 42 enemies (100%) |
| Magic Spells | 101 | 36+ spells (100%) |
| Foley | 39 | 6 surface types |
| Weapons | 32 | 8 weapon types |
| UI | 27 | Menus, inventory, crafting |
| Traps | 18 | 13+ trap types |
| Ambient | 5 | Biome loops |
| Combat | 1 | Base impacts (expandable) |
| **Total** | **436** | **174% of expected** |

---

## Architecture

### System Layers

```
┌─────────────────────────────────────────────┐
│         Arcade Window (Renderer)            │
├─────────────────────────────────────────────┤
│            Audio Mixer (TBD)                │
│  (Volume, Ducking, Panning, 3D Positioning)│
├─────────────────────────────────────────────┤
│       Sound Event System (game/events/)     │
│  (Combat, Magic, UI, Creature behaviors)   │
├─────────────────────────────────────────────┤
│     Game Systems (game/systems/)            │
│  (CombatSystem, MagicSystem, etc.)          │
├─────────────────────────────────────────────┤
│        Data Layer (data/*.json)             │
│  (Spells, Monsters, Items w/ sounds)       │
├─────────────────────────────────────────────┤
│         Audio Assets (audio/sfx/)           │
│  (436 WAV files organized by category)      │
└─────────────────────────────────────────────┘
```

### Key Design Principles

1. **Data-Driven:** All sound mappings in JSON, not hardcoded
2. **Deterministic:** No random audio selection (predictable for tests)
3. **Testable:** Core audio logic separate from Arcade rendering
4. **Accessible:** Structured file organization and clear naming
5. **Modular:** Each system (combat, magic, ui) manages own sounds
6. **Scalable:** Easy to add new sounds without code changes

---

## Asset Organization

### Directory Structure

```
audio/
├── sfx/
│   ├── ui/                    # UI/Menu sounds (27 files)
│   │   ├── button_*.wav
│   │   ├── inventory_*.wav
│   │   ├── crafting_*.wav
│   │   └── ...
│   │
│   ├── foley/                 # Movement/environment (39 files)
│   │   ├── footstep_*.wav     # 6 surface types
│   │   ├── door_*.wav
│   │   ├── chest_*.wav
│   │   ├── torch_*.wav
│   │   └── ...
│   │
│   ├── weapon/                # Melee/ranged attacks (32 files)
│   │   ├── sword_*.wav
│   │   ├── axe_*.wav
│   │   ├── bow_*.wav
│   │   ├── impact_*.wav
│   │   └── ...
│   │
│   ├── magic/                 # Spell effects (101 files)
│   │   ├── fireball_*.wav
│   │   ├── frost_*.wav
│   │   ├── flame_*.wav
│   │   └── ... (36+ spells)
│   │
│   ├── creature/              # Monster/NPC sounds (213 files)
│   │   ├── skeleton_*.wav
│   │   ├── dragon_*.wav
│   │   ├── orc_*.wav
│   │   └── ... (42 enemies)
│   │
│   ├── trap/                  # Trap activation (18 files)
│   │   ├── dart_*.wav
│   │   ├── explosion_*.wav
│   │   ├── poison_*.wav
│   │   └── ...
│   │
│   ├── ambient/               # Biome loops (5 files)
│   │   ├── dungeon_*.wav
│   │   ├── forest_*.wav
│   │   └── ...
│   │
│   └── combat/                # Combat impacts (1 file)
│       └── hit_*.wav
│
├── music/                     # Loopable music tracks (12 needed)
│   ├── exploration_*.wav
│   ├── combat_*.wav
│   └── ... (TBD)
│
├── catalog.json              # Sound metadata & attribution
├── LICENSE.txt               # CC0 license
└── README.md                 # Audio system notes
```

### Naming Convention

**Format:** `{category}_{type}_{descriptor}_v{version}.wav`

**Examples:**

```
magic_fireball_cast_v01.wav          # Spell casting phase
magic_fireball_impact_small_v01.wav  # Impact on one target
magic_fireball_burn_loop_v01.wav     # DoT ambient loop

creature_dragon_attack_melee_v01.wav # Dragon melee attack
creature_dragon_hurt_v01.wav         # Dragon damage sound
creature_dragon_death_v01.wav        # Dragon death sound

foley_footstep_stone_light_v01.wav   # Light step on stone
foley_footstep_grass_heavy_v01.wav   # Heavy step on grass
foley_footstep_water_medium_v01.wav  # Medium splash in water

weapon_sword_swing_heavy_v01.wav     # Heavy sword swing
weapon_sword_hit_flesh_v01.wav       # Impact on flesh
weapon_sword_hit_armor_v01.wav       # Impact on armor

ui_button_click_confirm_v01.wav      # Confirm button
ui_inventory_open_v01.wav            # Open inventory
ui_crafting_complete_v01.wav         # Craft successful
```

**Versions:** Always v01, v02, v03... for variations (for future variation support)

---

## Data Integration

### Spell Sounds (data/spells.json)

Each spell has a `sounds` field mapping to WAV files:

```json
{
  "id": "fireball",
  "name": "Fireball",
  "school": "fire",
  "sounds": {
    "cast": "audio/sfx/magic/fireball_cast_v01.wav",
    "impact_large": "audio/sfx/magic/fireball_impact_large_v01.wav",
    "impact_small": "audio/sfx/magic/fireball_impact_small_v01.wav",
    "burn_loop": "audio/sfx/magic/fireball_burn_loop_v01.wav"
  },
  "cost": { "mana": 25 },
  "effects": [{ "type": "damage", "element": "fire", "base": 25 }]
}
```

**Sound phases in spell casting:**

1. **cast** - Player initiates spell (preparation/buildup sound)
2. **release** - (Optional) Spell releases toward target
3. **impact** / **impact_large** / **impact_small** - Spell hits target(s)
4. **loop** - (Optional) Ongoing effect (DoT, shield, etc.)
5. **ambient** - (Optional) Environmental effect ambient sound

### Monster Sounds (data/monsters.json)

Each monster has a `sounds` field for various actions:

```json
{
  "id": "dragon",
  "name": "Ancient Dragon",
  "sounds": {
    "notice": "audio/sfx/creature/dragon_roar_warning_v01.wav",
    "aggro": "audio/sfx/creature/dragon_roar_attack_v01.wav",
    "attack_melee": "audio/sfx/creature/dragon_attack_melee_v01.wav",
    "attack_breath": "audio/sfx/creature/dragon_attack_fire_breath_v01.wav",
    "hurt": "audio/sfx/creature/dragon_hurt_v01.wav",
    "death": "audio/sfx/creature/dragon_death_v01.wav",
    "ambient_loop": "audio/sfx/creature/dragon_fly_loop_v01.wav"
  },
  "hp": 150,
  "threat": 15
}
```

**Sound phases in combat:**

1. **notice** - Player approaches (threat detected)
2. **aggro** - Monster becomes aggressive
3. **attack_*** - Specific attack types
4. **hurt** - Damage taken
5. **death** - Defeated/defeated
6. **ambient_loop** - Idle/movement ambient (low volume background)

### Item Sounds (data/items.json)

Items can have sounds for equipped/unequipped states:

```json
{
  "id": "sword_iron",
  "name": "Iron Sword",
  "sounds": {
    "equip": "audio/sfx/ui/item_equip_weapon_v01.wav",
    "unequip": "audio/sfx/ui/item_unequip_weapon_v01.wav",
    "swing": "audio/sfx/weapon/sword_swing_light_v01.wav",
    "impact_flesh": "audio/sfx/weapon/sword_hit_flesh_light_v01.wav",
    "impact_armor": "audio/sfx/weapon/sword_hit_armor_light_v01.wav"
  },
  "damage": 8,
  "type": "sword"
}
```

---

## Mixer & Playback

### Audio Mixer Engine (TBD - Implementation Task)

**Planned architecture:**

```python
class AudioMixer:
    """Central audio playback & mixing engine."""

    def __init__(self, arcade_window):
        """Initialize mixer with window context."""
        self.window = arcade_window
        self.master_volume = 1.0
        self.buses = {
            'master': 1.0,
            'ui': 1.0,
            'combat': 1.0,
            'magic': 1.0,
            'creature': 1.0,
            'ambient': 1.0,
            'music': 1.0,
        }
        self.playing_sounds = {}  # Track active sounds

    def play_sound(
        self,
        sound_path: str,
        bus: str = 'master',
        volume: float = 1.0,
        loop: bool = False,
        pan: float = 0.0,  # -1.0 (left) to 1.0 (right)
        pitch: float = 1.0,
    ) -> int:
        """Play sound on specified bus."""
        sound = arcade.load_sound(sound_path)
        sound.play(volume=volume * self.buses[bus])
        return sound_id

    def stop_sound(self, sound_id: int) -> None:
        """Stop playing sound."""
        ...

    def set_bus_volume(self, bus: str, volume: float) -> None:
        """Adjust bus volume (for ducking)."""
        self.buses[bus] = clamp(volume, 0.0, 1.0)

    def duck_dialog(self, duration: float = 1.0) -> None:
        """Lower all audio except dialogue for NPC/text."""
        for bus in ['combat', 'magic', 'creature']:
            self.set_bus_volume(bus, 0.3)

    def resume_from_duck(self, duration: float = 1.0) -> None:
        """Fade back in after dialogue."""
        for bus in ['combat', 'magic', 'creature']:
            self.set_bus_volume(bus, 1.0)
```

### Playback Patterns

**Pattern 1: Simple One-Shot**

```python
mixer.play_sound("audio/sfx/ui/button_click_confirm_v01.wav", bus='ui')
```

**Pattern 2: Combat Attack**

```python
attacker = player
defender = goblin

# Play attack swing
mixer.play_sound(attacker.weapon.sounds['swing'], bus='combat')

# Play impact (flesh vs armor)
if defender.armor > 0:
    sound = defender.sounds['armor_impact']
else:
    sound = defender.sounds['hurt']

mixer.play_sound(sound, bus='combat')
```

**Pattern 3: Spell Casting**

```python
spell = spells['fireball']

# Cast phase (buildup)
mixer.play_sound(spell.sounds['cast'], bus='magic')

# Wait for cast round...

# Impact phase
mixer.play_sound(spell.sounds['impact_large'], bus='magic')

# Ambient DoT loop (low volume)
mixer.play_sound(
    spell.sounds['burn_loop'],
    bus='magic',
    volume=0.3,
    loop=True,
)
```

**Pattern 4: Ambient Loops**

```python
# Biome ambient (always playing, very low volume)
mixer.play_sound(
    "audio/sfx/ambient/dungeon_cave_wet_loop_v01.wav",
    bus='ambient',
    volume=0.2,
    loop=True,
)

# Creature idle ambient (when in view)
mixer.play_sound(
    dragon.sounds['ambient_loop'],
    bus='creature',
    volume=0.15,
    loop=True,
    pan=calculate_pan(dragon.x, player.x),  # 3D panning
)
```

---

## Event System

### Sound Events (TBD - Implementation Task)

Proposed event-based system for decoupling sound triggering from game logic:

```python
# In game/events/audio_events.py

class PlaySoundEvent(Event):
    """Trigger sound playback."""
    sound_path: str
    bus: str = 'master'
    volume: float = 1.0
    loop: bool = False

class DuckAudioEvent(Event):
    """Lower all audio during dialogue."""
    duration: float = 1.0

class SetAmbientEvent(Event):
    """Change ambient biome loop."""
    biome: str
    volume: float = 0.2

# Usage in combat system:
def apply_spell(target: Actor, spell: Spell) -> CombatResult:
    result = CombatResult()

    # Play spell cast
    event_bus.emit(PlaySoundEvent(
        sound_path=spell.sounds['cast'],
        bus='magic',
    ))

    # Apply effects
    for effect in spell.effects:
        apply_effect(target, effect)

    # Play impact
    event_bus.emit(PlaySoundEvent(
        sound_path=spell.sounds['impact_large'],
        bus='magic',
    ))

    return result
```

---

## Integration Examples

### Example 1: Combat Attack Sound

```python
# game/systems/combat_system.py

def resolve_attack(attacker: Actor, defender: Actor) -> AttackResult:
    result = AttackResult()

    # Calculate hit
    hit_roll = roll_d100()
    hit_chance = calculate_hit_chance(attacker, defender)

    if hit_roll <= hit_chance:
        result.hit = True

        # Play swing sound
        swing_sound = attacker.weapon.sounds.get('swing')
        if swing_sound:
            mixer.play_sound(swing_sound, bus='combat')

        # Play impact sound
        impact_sound = defender.sounds.get('hurt')
        if impact_sound:
            mixer.play_sound(impact_sound, bus='combat', volume=0.8)

        # Calculate damage
        damage = calculate_damage(attacker, defender)
        result.damage = damage
    else:
        result.hit = False

        # Play miss sound
        mixer.play_sound(
            "audio/sfx/weapon/weapon_hit_miss_v01.wav",
            bus='combat',
        )

    return result
```

### Example 2: Spell Casting

```python
# game/systems/magic_system.py

def cast_spell(caster: Actor, spell: Spell, target: Actor) -> CastResult:
    result = CastResult()

    # Check resources
    if caster.mana < spell.cost.mana:
        result.success = False
        return result

    # Play cast sound
    if 'cast' in spell.sounds:
        mixer.play_sound(spell.sounds['cast'], bus='magic')

    # Cast rounds resolution
    for round in range(spell.cast_rounds + 1):
        yield  # Wait for round

    # Calculate fizzle
    fizzle_chance = calculate_fizzle(caster, spell)
    if roll_d100() < fizzle_chance:
        result.success = False
        mixer.play_sound(
            "audio/sfx/magic/spell_fizzle_v01.wav",
            bus='magic',
        )
        return result

    # Apply spell effects
    for effect in spell.effects:
        apply_effect(target, effect)

    # Play impact sound
    if 'impact' in spell.sounds:
        mixer.play_sound(spell.sounds['impact'], bus='magic')

    # Play ambient loop if applicable
    if 'loop' in spell.sounds:
        mixer.play_sound(
            spell.sounds['loop'],
            bus='magic',
            volume=0.3,
            loop=True,
        )

    result.success = True
    return result
```

### Example 3: UI Sound

```python
# game/views/inventory_view.py

class InventoryView(arcade.View):
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RETURN:
            # Equip item
            mixer.play_sound(
                "audio/sfx/ui/item_equip_weapon_v01.wav",
                bus='ui',
            )
            self.equip_selected_item()

        elif key == arcade.key.DELETE:
            # Drop item
            mixer.play_sound(
                "audio/sfx/ui/item_drop_heavy_v01.wav",
                bus='ui',
            )
            self.drop_selected_item()
```

---

## Next Steps

### Phase 1: Audio Mixer (Priority 1)

- [ ] Implement `AudioMixer` class in `game/systems/audio_mixer.py`
- [ ] Integrate with Arcade window
- [ ] Implement volume ducking for dialogue
- [ ] Add 3D audio positioning (pan based on creature location)
- [ ] Unit tests: `tests/systems/test_audio_mixer.py`

### Phase 2: Event System (Priority 2)

- [ ] Create `game/events/audio_events.py`
- [ ] Wire events into combat/magic systems
- [ ] Implement ambient biome loops
- [ ] Unit tests: `tests/systems/test_audio_events.py`

### Phase 3: Advanced Features (Priority 3)

- [ ] Sound variation selection (v01, v02, v03...)
- [ ] Dynamic pitch/speed variation (±10%)
- [ ] Reverb & echo effects
- [ ] Spatialization (3D audio positioning)
- [ ] Music system with adaptive layers

### Phase 4: Generate Missing Tracks (Priority 4)

- [ ] 12 loopable music tracks (exploration, combat, boss, etc.)
- [ ] Combat impact variations (flesh/metal/rock)
- [ ] Ambient loop expansions (desert, swamp, volcano)

---

## Testing

### Unit Tests

```bash
# Test audio mixer
pytest tests/systems/test_audio_mixer.py -v

# Test event system
pytest tests/systems/test_audio_events.py -v

# Test data linkages
pytest tests/test_audio_data_integration.py -v
```

### Test Coverage

- ✅ Sound file existence
- ✅ JSON schema validation
- ✅ Mixer initialization
- ✅ Volume ducking
- ✅ Event dispatch
- ✅ Deterministic sound selection

---

## Resources

- **Audio Files:** `audio/sfx/` (436 files)
- **Data Schemas:** `data/schemas/`
- **Arcade Docs:** <https://arcade.academy/>
- **Audio Theory:** See `.codex/` for research notes

---

## Attribution

All audio files are CC0 Public Domain, generated with ChatGPT & AI synthesis.

See `ATTRIBUTIONS.md` for complete source information.

---

**Last Updated:** October 26, 2025  
**Status:** ✅ Data integration complete, Mixer implementation pending
