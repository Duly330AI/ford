- [ ] ID: TASK-M1-16
  Title: M1-Abnahme: Kriterien & Benchmarks (CI + Lokal)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Artifacts: `tests/perf/test_m1_benchmarks.py`, `.github/workflows/ci.yml`
  DependsOn: TASK-M1-01..08
  Notes:
  CI führt Logik-Benchmarks (ohne GL) aus; lokal wird visuell geprüft.
  Acceptance (M1 gesamt):
  - [ ] **BSP:** 128×128 in < 50 ms Ø (100 Läufe, CI).
  - [ ] **Movement/Collision:** Fuzz 10k Schritte ohne Penetration/Exception.
  - [ ] **Kamera & Licht:** Pixel-Perfect; Togglen ohne Hänger.
  - [ ] **Performance lokal:** 1280×720 Test-Map mit 2000 Deko-Entities fühlt sich ≥ 60 FPS an (manuelle Sichtprüfung); CI bestätigt Culling/CPU-Budget.
  - [ ] **Stil/Tests:** Ruff clean; Black; alle Tests grün.
  References:
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
  - .github/workflows/ci.yml
