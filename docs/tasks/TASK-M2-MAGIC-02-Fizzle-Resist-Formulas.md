- [ ] ID: TASK-M2-MAGIC-02-Fizzle-Resist-Formulas
  Title: Fizzle & Resist Formulas
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/magic_math.py`, `tests/systems/test_magic_formulas.py`
  DependsOn: TASK-M2-02, TASK-M2-MAGIC-01, TASK-M3-MAGIC-01
  Notes:
  Implementiere Fizzle & Resist Formeln aus MAGIC_SYSTEM.md. Fizzle-Wahrscheinlichkeit basiert auf Magery-Skill & Spell-Parametern. Resist-Check: Caster Magery vs Defender Resist_Spells. Alle Parameter in `data/combat_rules.json` (Clamps, Scales, Defaults). Pure Functions in `game/systems/magic_math.py`. Tests mit `PYTHONHASHSEED=0`. Data-driven Konfiguration, keine Hardcodes.
  Acceptance:
  - [ ] Fizzle & Resist Calculations matchen MAGIC_SYSTEM.md Referenz-Beispiele.
  - [ ] `combat_rules.json` erweitert mit `magic.fizzle.*`, `magic.resist.*` Parametern.
  - [ ] Schema-Validierung für neue Felder.
  - [ ] Tests: Min/Max-Clamps, Skill-Differentiale, Parameter-Overrides mit Determinismus.
  - [ ] Doku aktualisiert (neue Parameter, Usage).
  Tests:
  - [ ] **Fizzle-Boundary-Test**: Min/Max-Clamp-Werte, Skill-Differenz korrekt angewendet.
  - [ ] **Resist-Calculation-Test**: Magery vs Resist_Spells, Clamp-Range beachtet.
  - [ ] **Parameter-Variation-Test**: Combat_Rules-Änderungen reflektieren korrekt in Output.
  - [ ] **Determinismus-Test**: gleicher Seed, gleiche Parameter → identische Werte.
  References:
  - docs/MAGIC_SYSTEM.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
