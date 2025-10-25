- [ ] ID: TASK-M1-GEN-03
  Title: Debug Tools Extended (F4 Heatmap, F5 Spawn Overlay, Ctrl+S Dump)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/views/debug_overlays.py`, `tests/views/test_debug_tools.py`
  DependsOn: TASK-M1-GEN-01, TASK-M3-GEN-01
  Notes:
  Erweitere Debug-Overlay: F4 Reachability-Heatmap (Gradient Scale), F5 Spawn-Overlay (Factions, Threat-Budget), Ctrl+S Map-Dump (`saves/runs/{seed}/map.json`). Headless-Mode Support (Log-Outputs) für CI. Performance <16ms. Schema für Map-Dump. CLI Flags für Auto-Export bei Gen-Runs.
  Acceptance:
  - [ ] F4 Heatmap zeigt erreichbare Tiles, Headless: Coverage-Stats in Log.
  - [ ] F5 Overlay unterscheidet Fraktionen/Encounter-Tiers, zeigt Threat-Totals pro Room.
  - [ ] Ctrl+S dumped JSON mit Biom/Tag/Spawn-Metadaten, deterministisch.
  - [ ] Debug-Tools <16ms Performance, togglebar, Config für Release-Builds.
  - [ ] Tests/Smoke-Checks: Command-Handler registrieren, Dump-Struktur validiert.
  Tests:
  - [ ] **Heatmap-Test**: F4 erzeugt Coverage-Stats korrekt.
  - [ ] **Spawn-Overlay-Test**: F5 zeigt Fraktionen & Threat-Totals.
  - [ ] **Dump-Test**: Ctrl+S exportiert deterministisches JSON.
  - [ ] **Headless-Test**: Debug-Tools im Headless-Mode geben Logs aus.
  References:
  - docs/DUNGEON_GENERATOR.md
  - docs/DEVELOPMENT.md
  - docs/CONVENTIONS.md
