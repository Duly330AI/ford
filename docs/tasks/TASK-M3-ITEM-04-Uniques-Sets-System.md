- [ ] ID: TASK-M3-ITEM-04-Uniques-Sets-System
  Title: Uniques & Sets System (Fixed Mods, Set Bonuses)
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `data/uniques.json`, `data/sets.json`, `data/schemas/uniques.schema.json`, `game/systems/unique_sets.py`, `tests/systems/test_uniques.py`
  DependsOn: TASK-M3-ITEM-01, TASK-M3-ITEM-02, TASK-M3-ITEM-03
  Notes:
  Definiere `data/uniques.json`: Unique-Item-Templates, Fixed-Mods, Lore-Keys, Drop-Sources. Implement Item-Sets (2-4 Pieces) mit Bonus-per-Piece-Count Dataclass. Extend Loot-Pipeline: Spawn Uniques/Sets Deterministic mit Seed-Tracking & Drop-Restrictions. Systems-Logik: Set-Bonuses applizieren bei Equipment-Count erreicht, Removen bei Unequip. Gating via Data (Biom/Fraktions/Quest-Progress). Debug-Hooks für Set-Bonus-Status. Graceful Handling bei Unique-Pool-Exhaustion.
  Acceptance:
  - [ ] Unique-Items spawnen mit Fixed-Stats + Optional-Random-Rolls, Deterministic per Seed.
  - [ ] Set-Bonus-Calcs triggern korrekt (Stats, Resistances, Effects) definiert in Data.
  - [ ] Loot-Tables integren Unique/Set Entries, Break nicht Existing-Drop-Rates, Duplicates controlled.
  - [ ] Tests: Unique-Generation, Set-Bonus-Activation/Deactivation, Save/Load-Persistence.
  - [ ] Doku: Examples für Designer, Integration mit Affix/Material-Systems.
  Tests:
  - [ ] **Unique-Generation-Test**: Fixed-Stats & Optional-Random-Rolls korrekt.
  - [ ] **Set-Bonus-Activation-Test**: Bonuses trigger bei correct Piece-Count.
  - [ ] **Gating-Test**: Biom/Fraktions-Gating enforced.
  - [ ] **Save-Load-Test**: Unique-IDs, Set-Membership, Bonus-States persistent.
  References:
  - docs/ITEMIZATION_DESIGN.md
  - docs/WORLD_BIBLE.md
  - docs/CONVENTIONS.md
