# Milestone Acceptance Checklists

## Milestone M2

- [ ] Spiel wechselt zuverlaessig in **rundenbasierten** Modus bei Engagement (LOS/Radien).
- [ ] Initiative & Zugfolge reproduzierbar; Aktionen invalid -> sauber abgewiesen.
- [ ] Treffer/Miss/Crit/Block folgen `data/combat_rules.json`; Resistenzen/Typen wirken.
- [ ] Status-Effekte ticken & stacken korrekt; Stun verhindert Aktion genau 1 Zug (oder konfiguriert).
- [ ] Projektile kollidieren mit Waenden; Ranged haelt Abstand; Caster setzt Spell zuerst.
- [ ] Combat-Log zeigt alle Wuerfe/Mods/Outcomes; Replay bei Seed reproduzierbar.
- [ ] Performance: Mikrobenchmarks gruen; Overhead der Logik im Budget.
- [ ] Tests: alle Unit/Integration gruen, Ruff/Black sauber.

---

## Milestone M3

- [ ] `items.json`, `skills.json`, `loot_tables.json` validieren gegen Schemas; IDs stabil & referentiell konsistent.
- [ ] Inventory: stacken/split/merge/move robust & atomar; Kapazitaetsfehler sauber.
- [ ] Equipment aggregiert Stats korrekt; Consumables loesen Effekte aus.
- [ ] Skills steigen deterministisch ueber Hooks (Combat/Use); Level-Cap & Boni wirken.
- [ ] Loot-Rolls liefern erwartete Verteilungen; Monster-Drops funktionieren.
- [ ] Hotbar (1-0) aktiviert Items/Aktionen; Tooltips zeigen korrekte Infos.
- [ ] Performance-Mikros gruen (Loot/Inventory); RNG deterministisch.
- [ ] Keine Arcade-Abhaengigkeiten in `systems/*`; UI nur Adapter-Ebene.
- [ ] README hat M3-Pruefanleitung; Tests & Linting gruen.

---

## Milestone M4

- [ ] `recipes.json`, `nodes.json` validiert; referentielle Integritaet (Items/Skills/Stations).
- [ ] Gather: Tool-Checks, Dauer, Yield, Depletion/Respawn funktionieren; Skill-Boni greifen.
- [ ] Crafting: Queue/Jobs deterministisch, atomare Reservierung, Erfolg/Fail/Crit nach Regeln; Pause im Combat.
- [ ] Stationen: Forge & Alchemy nutzbar; UI zeigt Queue/Progress; Cancel rollt korrekt zurueck.
- [ ] E2E "Erz->Barren->Schwert->Equip" deterministisch gruen.
- [ ] Performance: 2 000 Nodes Tick < 1 ms Logik; keine Frame-Drops durch Logik in CI-Mikros.
- [ ] Keine Arcade-Abhaengigkeit in `systems/*`; Adapter importierbar (Smoke).
- [ ] README M4-Abschnitt vorhanden; Tests/Lint gruen.

---

## Milestone M5

- [ ] Roundtrip: Vollstaendiger Zustand (Player, Inventory/Hotbar, Equipment, Skills, World/Seed/BSP, Nodes, Stations/Queues, Rezepte, RNG, Timekeeper) wird korrekt gespeichert/geladen.
- [ ] Determinismus: RNG-Streams liefern nach Load identische Folgesequenzen (Loot/Combat/Craft).
- [ ] Robustheit: Atomare Writes; Korruptions-Tests fuehren zu Recovery auf letzte gueltige Save-Datei.
- [ ] Policy: Kein Speichern in verbotenen Phasen; klare Fehlermeldungen fuer UI.
- [ ] Performance/Groesse: Dump + Write < 50 ms; JSON-gzip < 200 KB fuer typischen Save.
- [ ] Migration: v1->v2 Beispielmigration + Tests vorhanden.
- [ ] Validierung: Schema-/Referenz-Validatoren blocken inkonsistente Saves.
- [ ] UI: Slots/Hotkeys funktionieren (Adapter-Smoketests).
- [ ] Docs: README-M5-Abschnitt aktualisiert.

**Notizen & Default-Parameter**
- Save-Format: JSON+gzip als Default, optional MsgPack per data/config.default.json.
- Autosave: max 5 rotierende Dateien pro Slot (`auto-001.save` ... `auto-005.save`).
- Speicherort: `saves/` im Projektordner (spaeter OS-spezifische AppData).
- Timestamps: UTC ISO-8601.
- IDs: Items via stabile `item_id` + optionale `uuid`; Nodes `type@x,y` (Seed-basiert).
- Sicherheit: Keine PII, Hash dient nur Integritaet (SHA-256).
- Kompatibilitaet: Aenderungen in data/* nur additiv; Entfernen erfordert Migration.

**Tests ausfuehren**
- `poetry run pytest -q`
