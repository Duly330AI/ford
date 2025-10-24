- [ ] ID: TASK-M1-09
  Title: Debug-Overlay (F3): FPS, Seed, Room-Count, Coords
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Artifacts: `game/util/debug_overlay.py`, `game/assets/fonts/*`, `tests/smoke/test_debug_overlay_import.py`
  DependsOn: TASK-M1-03
  Notes:
  Ein/ausblendbar; zeigt FPS (rolling avg), aktuelle Tile-Koordinate, Seed, Raum-Anzahl, Entities sichtbar/gesamt.
  Acceptance:
  - [ ] Toggle per F3; Overlay kostet < 0.3 ms/Frame (ohne GL).
  Tests:
  - [ ] Import/Init ohne GL, Format-Funktionen Unit-getestet.
