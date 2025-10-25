- [ ] ID: TASK-M2-MAGIC-01-Core-Magic-System
  Title: Core Magic System
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/magic_system.py`, `tests/systems/test_magic_system.py`
  DependsOn: TASK-M2-04, TASK-M3-02, TASK-M3-06
  Notes:
  Implementiere `MagicSystem` mit deterministischer Casting-Pipeline (Request → Validierung → Outcome-Events). Mana & Reagenzien verbrauchen via Inventory/Resource-Services. Fizzle & Resist Formeln aus `data/combat_rules.json`, `data/spells.json`, `data/progression_rules.json`. Keine Arcade-Deps (testbar). Cast-Intents integrieren in Combat-Core. Skill-Progression Hooks (Magery, Meditation, Resist Spells) usage-based.
  Acceptance:
  - [ ] `MagicSystem.cast()` empfängt Intent, validiert Mana/Reagenzien, emittiert deterministisches Outcome per Seed.
  - [ ] Mana, Reagenzien-Verbrauch, Cooldown/Cast-Rounds persistieren korrekt über Turns & Saves.
  - [ ] Fizzle & Resist emittieren strukturierte Events mit Payloads für UI/Log-Adapter.
  - [ ] Tests: Success-Path, Fizzle-Path, Resist-Path, Resource-Exhaustion mit seeded RNG.
  - [ ] Validation-Fehler (fehlende Spell-IDs, malformed Data) early, aussagekräftig.
  Tests:
  - [ ] **Cast-Success-Test**: Spell mit gültigen Ressourcen → Success-Event.
  - [ ] **Fizzle-Test**: Fizzle-Rate konsistent mit Magery/Resist-Formula.
  - [ ] **Resource-Exhaustion-Test**: Kein Mana → Fehler.
  - [ ] **Determinismus-Test**: gleicher Seed → identischer Outcome.
  References:
  - docs/MAGIC_SYSTEM.md
  - docs/CONVENTIONS.md
  - docs/COMBAT_RULES.md
  - docs/ARCHITECTURE.md
