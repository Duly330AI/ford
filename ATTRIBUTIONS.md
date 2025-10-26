# Attribution & Licenses

This document lists all assets used in FORD and their sources.

---

## Audio Assets

### CC0 Public Domain - Generated

**Source:** ChatGPT (OpenAI) + AI synthesis  
**License:** CC0 (Public Domain)  
**Count:** 436 WAV files  
**Date Generated:** October 2025

**Categories:**
- Creature Sounds (213 files) - All 42 enemies
- Magic Spell Effects (101 files) - All 36+ spells
- Foley Sounds (39 files) - Movement, doors, containers
- Weapon Sounds (32 files) - Swords, axes, bows, impacts
- UI Sounds (27 files) - Buttons, menus, inventory
- Trap Sounds (18 files) - Darts, explosions, hazards
- Ambient Loops (5 files) - Dungeon/forest biomes
- Combat Sounds (1 file) - Base hit impact

**Organization:** `audio/sfx/{ui,foley,weapon,magic,creature,trap,ambient,combat}/`

**Generated Prompts Used:**
- "Generate a high-quality WAV sound of [description]"
- "Create a fantasy RPG sound effect for [action]"
- "Synthesize a 44.1kHz mono audio file of [creature/spell/action]"

---

## Game Code & Systems

### Custom Development

**Author:** FORD Development Team (Copilot + Agents)  
**License:** TBD (See LICENSE file)  
**Location:** `game/` (Python source code)

All game systems, mechanics, and architecture are custom-built:
- Combat system
- Magic system
- Dungeon generation
- AI/Behavior trees
- Inventory & crafting
- Data validation

---

## Data Files

### Custom Game Content

**License:** TBD  
**Location:** `data/` (JSON definitions)

All game data is custom-created:
- `data/items.json` - Weapon/armor definitions
- `data/spells.json` - Magic spell definitions
- `data/monsters.json` - Enemy definitions
- `data/recipes.json` - Crafting recipes
- `data/combat_rules.json` - Game formulas
- `data/skills.json` - Skill system

---

## Game Framework

### Arcade Library

**Source:** https://arcade.academy/  
**License:** MIT License  
**Author:** Benjamin Kaehler and contributors

Python library for game development. Used for:
- Rendering and sprite management
- Collision detection
- Input handling
- Window management

---

## Development Tools

### Poetry

**Source:** https://python-poetry.org/  
**License:** MIT License  
**Purpose:** Python dependency management

### Pytest

**Source:** https://pytest.org/  
**License:** MIT License  
**Purpose:** Python unit testing framework

### Black

**Source:** https://github.com/psf/black  
**License:** MIT License  
**Purpose:** Python code formatter

### Ruff

**Source:** https://github.com/astral-sh/ruff  
**License:** MIT License  
**Purpose:** Python linter

### Pre-commit

**Source:** https://pre-commit.com/  
**License:** MIT License  
**Purpose:** Git pre-commit hooks framework

### Markdownlint

**Source:** https://github.com/DavidAnson/markdownlint  
**License:** MIT License  
**Purpose:** Markdown file linter

---

## Documentation

### Markdown Files

**Location:** `docs/` and root level  
**License:** TBD

All documentation is custom-written by the FORD development team.

---

## Icons & Visual Assets

### None Currently

Visual assets (sprites, backgrounds, UI graphics) are not yet implemented.  
When added, all will use CC0 or explicitly licensed sources.

---

## Third-Party Libraries (Python)

Listed in `pyproject.toml`:

- **arcade** - MIT License
- **pygame** (optional) - LGPL License
- **pytest** - MIT License
- **black** - MIT License
- **ruff** - MIT License
- **pre-commit** - MIT License

---

## License Summary

| Category | License | Status |
|----------|---------|--------|
| Audio Assets | CC0 (Public Domain) | ✅ Complete |
| Game Code | TBD | 🟡 Pending |
| Game Data | TBD | 🟡 Pending |
| Documentation | TBD | 🟡 Pending |
| Tools (frameworks) | MIT / LGPL | ✅ Third-party |

---

## No Copyright Infringement

FORD is designed with **zero custom artwork** and all assets used are either:

1. **Generated** (ChatGPT audio synthesis)
2. **Public Domain** (CC0 licensed)
3. **Open Source** (MIT, LGPL)

No copyrighted material is included in the repository.

---

## How to Add New Attribution

When adding new assets:

1. Identify the source and license
2. Add entry to this file with:
   - Asset name
   - Source URL
   - License type
   - Location in project
   - Purpose/usage
3. Ensure license compatibility with project

---

## Questions?

For attribution questions or clarifications, see:
- Individual README files in asset directories
- `audio/LICENSE.txt` for audio specifics
- `docs/AUDIO_SYSTEM.md` for audio details

---

**Last Updated:** October 26, 2025  
**Maintained By:** FORD Development Team
