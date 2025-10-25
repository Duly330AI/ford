- [ ] ID: TASK-M1-GEN-04-Biome-Content-Alignment
  Title: Biome Content Alignment (WORLD_BIBLE Integration)
  Status: Proposed
  Priority: P2
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `docs/biome_guides/*.md`, `tools/validate_biome_loot.py`
  DependsOn: TASK-M1-GEN-01, TASK-M3-GEN-01, TASK-M3-08
  Notes:
  Kuriere Biom-Reference-Docs: WORLD_BIBLE Fraktionen → Biom-Defs (Tiles, Encounters, Loot-Tables). Audit bestehender Loot/Encounter-Tables, Fraktions-Signatures matchen Lore (Ressourcen, Reagenzien). Alignment-Checklist pro Biom (Assets, Loot, Audio, Quest-Seeds). Templates für Designer, um neue Biom-Content hinzufügen ohne Schema-Breaking. Validation-Script für Loot-Korrektheit.
  Acceptance:
  - [ ] Jede Biom-Def cross-referenced Fraktions-IDs, Loot-Tables, Encounter-Sets aligned mit WORLD_BIBLE.
  - [ ] Alignment-Checklist unter `docs/biome_guides/` (Assets, Loot, Audio, Quests).
  - [ ] Review identifiziert Mismatches, erstellt Follow-up-Issues/Tasks.
  - [ ] Designer können neue Biom-Content per Template hinzufügen ohne Engineer-Guidance.
  - [ ] Doku updated: Biom-System ↔ World-Bible Interplay.
  Tests:
  - [ ] **Loot-Validation-Test**: Loot-Tables matchen Fraktions-Signatures.
  - [ ] **Faction-Reference-Test**: Biom-Defs referenzieren existierende Fraktions-IDs.
  - [ ] **Encounter-Consistency-Test**: Encounter-Sets match Biom-Lore.
  References:
  - docs/WORLD_BIBLE.md
  - docs/DUNGEON_GENERATOR.md
  - docs/ART_STYLE_GUIDE.md
