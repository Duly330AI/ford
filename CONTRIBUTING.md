# Contributing to FORD

Thank you for your interest in contributing to FORD! This document outlines our development workflow and contribution guidelines.

## Prerequisites

- **Operating System:** Windows, macOS, or Linux
- **Git:** https://git-scm.com/
- **Conda:** Miniconda or Anaconda (https://conda.io/)
- **Python:** 3.12+
- **Editor:** VS Code recommended (with Python extension)

## Setup

### 1. Clone Repository

```bash
git clone https://github.com/Duly330AI/ford.git
cd ford
```

### 2. Create Conda Environment

```bash
conda create -n ford python=3.12
conda activate ford
```

### 3. Install Dependencies

```bash
poetry install --no-root
pre-commit install
```

### 4. Verify Setup

```bash
source dev.sh  # Git Bash / macOS / Linux
dev-status
```

Or on PowerShell:

```powershell
. .\dev.ps1
dev-status
```

## Development Workflow

### 1. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b fix/your-bug-fix
```

**Branch naming convention:**
- `feature/short-description` - New features
- `fix/short-description` - Bug fixes
- `refactor/short-description` - Refactoring
- `docs/short-description` - Documentation
- `test/short-description` - Tests

### 2. Make Changes

Work on your feature or fix. Keep commits small and focused.

### 3. Run Tests & Linting

```bash
# Fast feedback loop
pytest -m "not slow" --ff -x

# Auto-fix formatting issues
lint-fix

# Run all tests before commit
test-all
```

### 4. Commit Changes

```bash
git add .
git commit -m "feat: add new spell effects"
```

**Commit message format** (Conventional Commits):

```
feat:     New feature
fix:      Bug fix
refactor: Code restructuring (no behavior change)
test:     Add/update tests
docs:     Documentation changes
chore:    Build, tooling, dependencies
perf:     Performance improvements
```

**Example:**
```
feat: implement audio mixer with ducking

- Add Arcade audio mixer integration
- Implement volume ducking for dialogue
- Add 3D audio positioning for creatures
- Closes #123
```

### 5. Push & Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub:
- Link related issues
- Describe changes clearly
- Reference task IDs if applicable (e.g., `TASK-M4-AUDIO-01`)

## Code Standards

### Python Code

All Python code must follow these standards:

- **Formatter:** Black (line length: 88)
- **Linter:** Ruff (see `pyproject.toml`)
- **Type Hints:** Required (see PEP 484)
- **Tests:** Required for core logic (minimum 70% coverage)

```python
# ✅ Good
def calculate_damage(
    attacker_str: int,
    weapon_damage: int,
    defender_armor: int,
) -> int:
    """Calculate weapon damage after armor mitigation."""
    base = attacker_str + weapon_damage
    reduction = defender_armor * 0.5
    return max(1, base - reduction)


# ❌ Bad
def calc_dmg(a, w, d):
    return max(1, a + w - d * 0.5)
```

### Tests

- Location: `tests/` directory (mirrors `game/` structure)
- Framework: `pytest`
- Naming: `test_<module>.py` with `test_<function>()` functions
- Determinism: Use seeded RNG (`PYTHONHASHSEED=0`)

```python
# ✅ Good test
def test_hit_chance_with_skill_difference():
    """Verify skill difference affects hit chance."""
    attacker = create_test_actor(weapon_skill=50)
    defender = create_test_actor(weapon_skill=30)
    chance = calculate_hit_chance(attacker, defender)
    assert chance > 0.5  # Attacker should have advantage


# ❌ Bad test
def test_hit_chance():
    x = 10
    y = 20
    assert x < y
```

### Documentation

- **Module docstrings:** Describe purpose and public API
- **Function docstrings:** Describe arguments, return, and exceptions
- **Inline comments:** Explain "why," not "what"
- **Markdown files:** Follow `.markdownlint.json` rules

```python
# ✅ Good docstring
def apply_spell_effect(
    target: Actor,
    spell: Spell,
) -> CombatResult:
    """Apply spell effect to target actor.

    Calculates fizzle chance, resistance checks, and applies
    damage/healing/status effects based on spell data.

    Args:
        target: Actor receiving spell effect
        spell: Spell data with effects array

    Returns:
        CombatResult with success flag and effect details

    Raises:
        ValueError: If spell has no effects
    """
```

### Data Files (JSON)

All JSON data must validate against schemas in `data/schemas/`:

```bash
# Validate manually
python -c "
import json
from jsonschema import validate
with open('data/items.json') as f:
    items = json.load(f)
with open('data/schemas/items.schema.json') as f:
    schema = json.load(f)
validate(items, schema)
print('✅ Valid')
"
```

## Pre-Commit Checks

Hooks run automatically on `git commit`:

- **end-of-file-fixer** - Ensures files end with newline
- **trailing-whitespace** - Removes trailing spaces
- **black** - Formats Python code
- **ruff** - Lints Python code
- **markdownlint** - Validates Markdown
- **jsonlint** - Validates JSON
- **commitlint** - Enforces Conventional Commits

**If a hook fails:**

1. Read the error message
2. Fix the issue
3. Commit again (usually auto-fixed by hooks)

**Emergency: Skip hooks**

```bash
git commit --no-verify
# ⚠️ Only for critical situations
```

## Architecture Guidelines

### Testable Core Systems

Systems in `game/systems/` must:

- ✅ Import only from `game/models/`, `data/`, standard library
- ❌ NOT import Arcade, pygame, or other rendering libraries
- ✅ Accept all configuration from data files or parameters
- ✅ Return deterministic results with seeded RNG

```python
# ✅ Good: Pure logic, testable
def calculate_hit_chance(attacker_skill: int, defender_skill: int) -> float:
    base = 0.5
    diff = (attacker_skill - defender_skill) / 100
    return clamp(base + diff, 0.0, 1.0)


# ❌ Bad: Tightly coupled to rendering
def calculate_hit_chance(attacker_actor):
    return arcade.get_random() > (attacker_actor.dexterity * 0.01)
```

### Data-Driven Design

- Configuration lives in `data/` (JSON files)
- Systems load and validate data at startup
- Changes to data don't require code changes
- See `docs/DATA_SCHEMAS.md` for structure

### Architectural Boundaries

See `docs/ARCHITECTURE_UO_ADDENDUM.md` for:

- System boundaries and dependencies
- Layer diagram (Game → Systems → Models → Data)
- Rendering vs. Logic separation
- Audio integration points

## Audio System

The audio system is data-driven and integrated into game and combat systems.

**Key files:**
- `audio/sfx/{ui,foley,weapon,magic,creature,trap,ambient,combat}/` - Sound files
- `data/spells.json` - Spell sounds mappings
- `data/monsters.json` - Creature sounds mappings
- `docs/AUDIO_SYSTEM.md` - Complete audio documentation

**Adding new sounds:**

1. Place WAV file in appropriate `audio/sfx/` subdirectory
2. Update JSON file (`spells.json`, `monsters.json`, etc.)
3. Reference in sound field:
   ```json
   "sounds": {
     "cast": "audio/sfx/magic/fireball_cast_v01.wav",
     "impact": "audio/sfx/magic/fireball_impact_v01.wav"
   }
   ```

See `docs/AUDIO_SYSTEM.md` for mixer integration details.

## Testing Checklist

Before submitting PR:

- [ ] `pytest -v` passes (all tests green)
- [ ] `lint-all` passes (no linting errors)
- [ ] New code has tests (minimum 70% coverage)
- [ ] Code follows Python standards (type hints, docstrings)
- [ ] Data files validate against schemas
- [ ] Documentation updated if needed
- [ ] Commit messages follow Conventional Commits
- [ ] Branch is up-to-date with `main`

## Submitting a Pull Request

1. **Push your branch** to GitHub
2. **Create Pull Request** with:
   - Clear title: `feat: implement audio mixer` (not "Fix things")
   - Description: Why this change, what it does
   - Link related issues: `Closes #123`
   - Reference tasks: `Implements TASK-M4-AUDIO-01`
3. **CI checks pass** (linting, tests)
4. **Code review:** Address feedback
5. **Merge:** Squash commits and merge to `main`

## Need Help?

- **Questions?** Open an issue or ask in comments
- **Unclear guidance?** See `docs/` directory
- **Setup issues?** Check `DEVELOPMENT.md` troubleshooting
- **For LLM Agents:** See `docs/LLM_AGENT_GUIDELINES.md`

## Code of Conduct

- Be respectful and inclusive
- Give constructive feedback
- Help others learn and improve
- Report issues privately if needed

---

Thank you for contributing to FORD! 🎮

Last Updated: October 26, 2025
