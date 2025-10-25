- [ ] ID: TASK-M2-MAGIC-03-Cast-Rounds-Integration
  Title: Cast Rounds Integration
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/cast_manager.py`, `tests/systems/test_cast_rounds.py`
  DependsOn: TASK-M2-04, TASK-M2-MAGIC-01, TASK-M2-MAGIC-02
  Notes:
  Integriere Multi-Round Casting in Turn-Manager. `cast_rounds_remaining` State pro Caster. Meditation-Modifiers & externe Effects auf Cast-Dauer (data-driven). Interruption-Regeln (Schaden, Bewegung, Stun): Cancel-Outcomes, Refund-Policy. Initiative/Turn-Sequencing zeigt Casting-Progress in Outcomes für UI. Casting-State persistiert in Combat-Save.
  Acceptance:
  - [ ] Turn-Manager trackt Casting-Progress deterministisch, resumiert nach Partial Turns.
  - [ ] Interruption-Events triggern Cleanup (Mana, Reagenzien per Design) & Skill-Progression.
  - [ ] Cast-States serialisieren in Combat-Save (Save/Load mid-fight).
  - [ ] 0-Round Instant-Casts & >1 Round Spells ohne Breaking bestehender Melee/Ranged-Intents.
  - [ ] Tests: Uninterrupted, Interrupted, Simultaneous Multi-Caster mit RNG-Seeding.
  Tests:
  - [ ] **Cast-Success-Test**: Spell mit korrekter Cast-Rounds-Verzögerung.
  - [ ] **Interruption-Test**: Schaden/Stun bricht Cast ab, korrekte Cleanup.
  - [ ] **Save-Load-Test**: Mid-Cast Save/Load erhält State.
  - [ ] **Multi-Caster-Test**: Zwei Caster gleichzeitig, korrekte Turn-Order.
  References:
  - docs/MAGIC_SYSTEM.md
  - docs/COMBAT_RULES.md
  - docs/ARCHITECTURE.md
