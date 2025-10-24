- [ ] ID: TASK-M2
  Title: M2 - Gegner & Kampfgrundlagen
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Notes:
  **Scope:** Gegner-Archetypen (Melee/Ranged/Caster) mit Overworld-FSM (idle/patrol/chase/attack), Uebergang in **rundenbasierten** Kampfmodus, Initiativ-/Zuglogik, Wuerfelsystem (Treffer/Verteidigung/Krit/Block), Status-Effekte, Schaden/Resistenzen, Projektile (logisch), Trefferfeedback (Particles/Shake via Adapter), Basis-KI fuer Zugauswahl.
  **Ziel:** Stabiler rundenbasierter Kampf gegen 3 Grundgegner, deterministisch testbar, klar getrennte Logik (ohne Arcade) vs. Praesentation (Scene/Arcade). M1 (Bewegung/Licht) bleibt unveraendert nutzbar.

  ---

  ## Leitplanken (M2-weit)
  - **Tests verpflichtend** fuer Kernlogik (dice, initiative, combat, effects, AI, path, LOS).
  - **Determinismus**: injizierbarer RNG (`random.Random(seed)`); `PYTHONHASHSEED=0`.
  - **Trennung**: `systems/*`, `util/*` **ohne Arcade**. Rendering/FX nur in `scenes/*`/`entities/*`.
  - **Datengetrieben**: Gegner/Regeln/Resistenzen aus `data/*.json` mit Validierung.
  - **Performance**: 1 vollstaendige Runde (Spieler + 3 Gegner) < **2 ms** reine Logik  in CI.

  ---
  Subtasks:
  - [TASK-M2-01](./TASK-M2-01.md) - Wuerfelsystem (d20/dX, Advantage/Disadvantage, Tabellen)
  - [TASK-M2-02](./TASK-M2-02.md) - Ableitbare Werte & Formeln (ATK/DEF/CRIT/EVA/RES)
  - [TASK-M2-03](./TASK-M2-03.md) - Initiative & Turn-Order
  - [TASK-M2-04](./TASK-M2-04.md) - Combat-Core (Intents -> Outcomes)
  - [TASK-M2-05](./TASK-M2-05.md) - Status-Effekte (Buffs/Debuffs/DoT/CC)
  - [TASK-M2-06](./TASK-M2-06.md) - Overworld-FSM (idle/patrol/chase/attack) & Engagement
  - [TASK-M2-07](./TASK-M2-07.md) - Gegner-Archetypen & Daten
  - [TASK-M2-08](./TASK-M2-08.md) - Pfadfindung (A*, Kostenfelder, "keep distance")
  - [TASK-M2-09](./TASK-M2-09.md) - Combat-KI (Heuristiken fuer Melee/Ranged/Caster)
  - [TASK-M2-10](./TASK-M2-10.md) - Projektile (Logik, LOS-Treffer, Block an Waenden)
  - [TASK-M2-11](./TASK-M2-11.md) - Sichtlinie (LOS) & Reichweitenpruefung
  - [TASK-M2-12](./TASK-M2-12.md) - Schadenstypen & Resistenzen
  - [TASK-M2-13](./TASK-M2-13.md) - Trefferfeedback-Adapter (Particles/Shake Hook)
  - [TASK-M2-14](./TASK-M2-14.md) - Combat-UI Overlay (Turn Order, Action Bar, Tooltips)
  - [TASK-M2-15](./TASK-M2-15.md) - Kampf-Log & Replay (Debug)
  - [TASK-M2-16](./TASK-M2-16.md) - Integrationsszenario "Spieler vs. Trio" (Determinismus)
  - [TASK-M2-17](./TASK-M2-17.md) - Mikrobenchmarks Kampf (CI)
  - [TASK-M2-18](./TASK-M2-18.md) - Doku "Wie M2 pruefen" (README Abschnitt)
  Acceptance:
  - [ ] See docs/notes/milestone-acceptance.md#m2
  Tests:
  - [ ] Track per subtask
