# FORD • GAMEPLAY.md

> Single-Player 2D-Dungeon-Crawler in **Python + Arcade**.  
> Kern: **Erkunden in Echtzeit**, **Kämpfe rundenbasiert**, **Progression über Skills**, **datengetrieben** (Items, Rezepte, Gegner, Regeln liegen in `data/*.json`).

---

## 1) Ziel & Kern-Loop

**Kurz:** Erkunde einen prozeduralen Dungeon, sammle Ressourcen, besiege Gegner in **rundenbasierten** Gefechten, crafte Ausrüstung, steigere Skills durch Nutzung, sichere Fortschritt per Save/Load.

**Kern-Loop:**
1. **Erkunden** (Overworld, Echtzeit): Räume aufdecken, Licht & Geräusche beachten.
2. **Engagement**: Gegner sichten → Wechsel in **Kampfmodus** (Initiative).
3. **Kampf** (Runden): Aktionen planen (Move/Attack/Shoot/Cast/Use/Wait), Würfelwürfe entscheiden Treffer/Schaden.
4. **Belohnung**: Loot aufsammeln, Skills steigen (usage-based).
5. **Berufe & Crafting**: Nodes (Erz/Holz/Kräuter) ernten → an Stationen craften.
6. **Fortschritt sichern**: Save-Slot, Autosave, QuickSave/Load.

---

## 2) Steuerung & UI

### Tasten (Standard)
- **Bewegung**: `WASD` oder Pfeile (8-Wege mit Diagonalen)
- **Dodge-Roll (Overworld)**: `Leertaste` (kostet Ausdauer, iFrames kurzzeitig)
- **Interagieren / Aufheben / Station nutzen**: `E`
- **Hotbar**: `1–0` (10 Slots; Consumables/Aktionen)
- **Licht an/aus**: `L` (Debug/Style)
- **Dungeon neu seedn**: `R` (nur im Dev/Testing sinnvoll)
- **Debug-Overlay**: `F3` (FPS/Seed/Coords/Profiler)
- **QuickSave/QuickLoad**: `F5` / `F9` (wenn aktiviert; Save-Policy beachten)

> **Remapping** geplant über `game/util/input.py`. Standard-Belegung ist datengetrieben.

### HUD
- **Bars** links oben: HP / Mana / Stamina
- **Hotbar** unten: 10 Slots mit Stack-Zahl / Cooldown
- **Tooltip** (Hover): Name, Typ, Rarity, Damage/Defense, Mods, Stack/Value
- **Kampf-Overlay** (im Fight): Initiative-Leiste, aktuelle Aktion, Reichweiten-Highlight

---

## 3) Welt, Sicht & Licht

- **Tile-Größe**: 16×16 px (gerendert in **64 px** via integer Scale 4×, Pixel-Perfect).
- **Prozedural** (BSP): Räume + Korridore, Wände kollidierbar.
- **Sichtlinie (LOS)**: Bresenham-Ray. Wände/Light-Blocker stoppen Sicht & Projektile.
- **Licht**: Spieler trägt Fackel (Radius konfigurierbar). Wände werfen Schatten.  
  Licht ist **stilistisch**, **nicht** stealth-relevant (später optional).

---

## 4) Attribute & Ressourcen

- **HP** – Lebenspunkte (0 → Tod/Reload)  
- **Mana** – Zauberkosten (nur Caster/Spells)  
- **Stamina** – Overworld-Dodge-Roll & ggf. Sprint (keine Subpixelgeschwindigkeit)  
- **ATK/DEF** – Angriffs-/Verteidigungswert (Formeln datengetrieben)  
- **Resistenzen** – pro Schadenstyp `0.0..1.0` (clamped)

**Stats entstehen aus**: Basiswerte + Ausrüstung + Effekte + Skill-Boni + (später) Tränke/Mods.

---

## 5) Kampf (Rundenbasiert)

### 5.1 Einstieg & Rundenablauf
- **Engagement**: Wenn ein Gegner den Spieler **sieht** (Radius+LOS), wechselt das Spiel in den **Kampfmodus**.
- **Initiative**: pro Beteiligtem (Spieler + Gegner) gewürfelt → Zugreihenfolge pro Runde.
- **Aktionen pro Zug**:  
  - **1 Hauptaktion** (Attack / Shoot / Cast / UseItem)  
  - **Bewegung**: bis **3 Tiles** (Standard)  
  - **Warten**: freiwillig, um Position/Initiative zu halten
- **Rundenwechsel**: Nach letztem Actor beginnt Runde `+1`. Effekte ticken am konfigurierten Zeitpunkt (Start/Ende).

> **Overworld-Dodge** ist **kein** Kampfmanöver. Im Kampf existiert ggf. eine **„Dodge“-Aktion** (kurze iFrames/evade-Bonus), siehe `combat_rules.json`.

### 5.2 Würfel & Formeln (Default)
- **Trefferwurf**: `d20 + ATK >= 10 + DEF`  
- **Crit**: Basis **5%** (nat20), Multiplier **1.5×** (oder in `combat_rules.json`)  
- **Block/Parry**: optionaler Verteidigungswurf → reduziert Schaden (z. B. **−50%**)  
- **Schaden**: `weapon dice + mods`, dann `*(1 - resist[type])`, **min. 1**  
- **Reichweiten**: Melee **1**, Ranged **6**, Caster **5** Tiles  
- **Munition** (Bogen): `arrows` werden verbraucht; Verhalten ohne Pfeile konfigurierbar (`fail` vs. `fallback_melee`)

> Alle Werte sind **datengetrieben** (`data/combat_rules.json`) und können balanciert werden.

### 5.3 Status-Effekte (Auszug)
- **Bleed** (DoT phys), **Poison** (DoT poison): ticken pro Runde  
- **Stun**: blockiert **1 Zug** (oder konfiguriert)  
- **Guard**: +DEF für N Runden  
- **Haste**: +1 Move-Tile pro Zug  
- **Evade**: erhöhte Ausweichchance

Effekte definieren **apply/tick/expire** in `data/effects.json`. Stacking-Regeln: `none|add|refresh`.

### 5.4 Gegnerverhalten (KI)
- **Melee**: ranlaufen, schlagen; bei niedrigem HP **Guard**
- **Ranged**: hält **Kite-Distanz** (z. B. 4–6 Tiles), schießt, repositioniert
- **Caster**: priorisiert **CC/DoT**, verwaltet Mana, fallback Nahkampf

---

## 6) Bewegung & Kollision (Erkunden)

- **Echtzeit** (`dt`-basiert), **8-Wege**.  
- **Diagonal-Clamp**: diagonale Geschwindigkeit = orthogonal (normierter Input).  
- **AABB-Kollision** gegen **Walls** mit separater Achsenauflösung → sauberes **Slide** an Wänden.  
- **Dodge-Roll** (Overworld): kurze **iFrames**, verbraucht **Stamina**; Cooldown kurz.

---

## 7) Skills & Progression (usage-based)

**Skills**: `swords, archery, sorcery, lockpicking, mining, woodcutting, alchemy, smithing, healing`  
- **Anstieg durch Nutzung**:  
  - Treffer mit Schwert → `swords` XP  
  - Bogen → `archery` XP (mit Pfeilverbrauch)  
  - Zauber → `sorcery` XP  
  - Trank nutzen → `healing` XP  
  - Abbau/Ernte → `mining/woodcutting` XP  
  - Crafting → `smithing/alchemy` XP
- **Cap**: standard **100** (datengetrieben).  
- **Boni**: je Skill (z. B. `+ATK pro 10 swords-Level`, `archery: +Crit`, `alchemy: Potency+`).

XP-Kurven in `data/skills.json` (z. B. polynomial `a * level^p` oder Tabellen).

---

## 8) Berufe & Nodes

**Nodes**: `ore`, `tree`, `herb`  
- **Interaktion**: `E` in Nachbarschaft (1 Tile)  
- **Tool-Check**: z. B. `pickaxe_stone` für `iron_ore_vein`  
- **Dauer**: abhängig von Tier/Skill; **Skill** reduziert Zeit &/oder erhöht Yield  
- **Yield**: feste Item-Range oder **Loot-Tabelle**  
- **Depletion/Respawn**: Node verschwindet, respawnt nach `respawn_sec`

Parameter in `data/nodes.json` + Balancing in `data/balance.json`.

---

## 9) Crafting & Stationen

**Stationen**: `forge`, `alchemy`  
- **Rezepte** in `data/recipes.json` (Inputs → Outputs, `time_sec`, Skill-Min, Tool-Anforderung, Erfolg/Crit, Fail-Returns)  
- **Queue** pro Station, Jobs laufen in Overworld-Zeit (im Combat **pausiert**)  
- **Ergebnis**: ins Inventar (oder World-Drop bei Platzmangel)  
- **Skill-Hooks**: `smithing/alchemy` geben XP & Boni (Crit-Chance, Output+)

Optional: **Rezept-Freischaltung** über Drops/Scrolls.

---

## 10) Items, Ausrüstung, Hotbar

### 10.1 Item-Typen
- **Weapon** (Schadenstyp + Dice), **Armor** (DEF), **Consumable** (Use-Effekte),  
  **Material**, **Currency (`gold`)**, **Ammo (`arrows`)**

### 10.2 Inventar
- **Slots** (z. B. 30), Stacks (Default max 99), atomare Operationen (add/remove/split/merge/move).  
- Optional **Gewichtslimit** (Balance-Flag).

### 10.3 Equipment
- Slots: **weapon**, **offhand**, **armor**, **accessory**  
- Stat-Aggregation: Basis + Equip + Effekte + Skills (reproduzierbar)

### 10.4 Hotbar (10)
- **1–0** aktiviert Slot-Aktionen: Consumable nutzen, z. B. **Heiltrank**;  
  für Waffen ggf. **Special** (später).  
- Hotbar referenziert **Inventar-Slots** (kein Doppel-Item-Duplikat).

---

## 11) Loot & Raritäten

**Tabellen** in `data/loot_tables.json` (Gewichte, Mengenbereiche, **nested tables**).  
- Gegner ziehen bei Tod aus ihrer **Drop-Tabelle** (`monsters.json`).  
- **Rarity**: `common|rare|epic` (Farb-Codierung in `data/ui.json`)  
- **Gold**: als Item (stackbar), mit Komfort-APIs (`add_gold/remove_gold`).

---

## 12) Gegner

**Archetypen** in `data/monsters.json`:  
- **Melee** (HP/ATK hoch, kurze Reichweite)  
- **Ranged** (Abstand halten, Projektile)  
- **Caster** (Spells, Mana, DoT/CC)  
Felder: `hp, atk, def, speed, resist, drop_table_id, spells?, projectile?`

---

## 13) Schwierigkeitsgrad & Balance

- **Standardwerte** in `data/combat_rules.json` & `data/balance.json`.  
- Balancing erfolgt **datengetrieben** (keine Hardcodes).  
- Beispiele:
  - **Kampf**: Crit 5%, Block 50% Reduktion, MinDamage 1
  - **Overworld**: Node-Respawn T1 Erz 120 s, Baum 180 s, Kraut 90 s
  - **Crafting**: Ingot 5 s, Potion 4 s, Sword 8 s
  - **Skills**: Boni pro 10 Level (konfigurierbar)

---

## 14) Audio & Feedback

- **SFX**: Schritt, Schlag, Treffer, Pickup, Craft-Complete (Platzhalter).  
- **Trefferfeedback**: Particles, Screen-Shake (Intensität nach Crit/Schaden).  
- **UI**: Farb-Codes für Rarity & Schadenstypen; Tooltips konsistent.

---

## 15) Speichern/Laden (Kurz)

- **Slots**: `saves/slot-#/last.save`, `auto-###.save`, `quick.save`  
- **Autosave**: Raumwechsel, Craft-Abschluss, Elite-Kill (gedrosselt)  
- **Policy**: kein Save während aktiver Kampf-Auflösung/Animation (zwischen Zügen ok)  
- **Integrität**: SHA-256-Checksumme (Korruption → Recovery auf letzte gültige Datei)

Details: `SAVELOAD.md` (wenn vorhanden) & `M5`-Tasks.

---

## 16) Accessibility & Optionen (geplant)

- **Textgröße/UI-Skalierung**  
- **Farbenblind-Modi** (alternative Rarity-Farben, Schadenstyp-Icons)  
- **Key-Remap** (Input-JSON)  
- **An-/Abschaltung von Screen-Shake** und Partikelgrenzen

---

## 17) Onboarding & Tipps

- **Erste Schritte**:
  1. Bewegen, Licht testen (`L`), Karte erkunden.
  2. Erste Gegner **pullen**, nicht überziehen (1–2 max).
  3. Drops looten → **Health Potion** in **Hotbar (1)** legen.
  4. **Erzader** finden (`E`), Material für **Ingot** sammeln.
  5. **Forge** nutzen: `iron_ingot` craften → **Iron Sword** herstellen & ausrüsten.
  6. Skills steigen automatisch mit (Swords/Mining/Smithing).

- **Kampf-Hinweis**: **Position** ist König – Ecke/Engpass nutzen, Ranged auf Distanz halten.  
- **Ressourcen**: Pfeile nicht verschwenden; Caster sparen Mana für CC.

---

## 18) Debug/Dev (nur in Non-Release-Builds)

- `F3` Overlay (FPS/Seed/Coords/Profiler)  
- `R` reseeded Dungeon  
- Optional: Log-Ausgabe von Würfen/Outcomes (Combat-Log)

---

## 19) Beispielwerte (Default, anpassbar)

| Kategorie         | Default                                   |
|-------------------|-------------------------------------------|
| Crit              | 5% Basis (nat20), 1.5× Schaden            |
| Block             | an, 50% Reduktion                         |
| MinDamage         | 1                                         |
| Ranges            | melee 1 · ranged 6 · caster 5             |
| Overworld Dodge   | ~0.35 s iFrames, Stamina-Kosten moderat   |
| Node Respawn T1   | 120–180 s                                 |
| Craft Zeiten      | Ingot 5s · Potion 4s · Sword 8s           |
| Skill Cap         | 100                                       |

> Diese Vorgaben leben in `data/combat_rules.json` & `data/balance.json`.

---

## 20) Akzeptanzkriterien (Gameplay)

- **Erkunden**: Begehbarer Dungeon, Kollisionen korrekt, Kamera Pixel-Perfect.  
- **Engagement**: Sichtkontakt → Kampfmodus; Ende des Kampfes → Overworld.  
- **Kampf**: Eine Runde mit Spieler + 3 Gegnern läuft stabil; invalid actions werden abgelehnt (Reichweite/LOS/Ammo).  
- **Effekte**: DoT/Buffs/Stun wirken und ticken korrekt; Stun skippt genau 1 Zug (oder wie konfiguriert).  
- **Loot**: Drop-Tabellen liefern erwartete Items/Mengen (stochastisch plausibel).  
- **Berufe**: Node-Interaktion prüft Tools/Skill, respawned korrekt.  
- **Crafting**: Queue/Reservierungen atomar; Erfolg/Fail/Crit gemäß Rezepten.  
- **Hotbar**: Consumables nutzbar, Stacks sinken; Fehlpfade (leer) reagieren sauber.  
- **Progression**: Skills steigen bei Nutzung; Boni greifen in Formeln.  
- **Saves**: Quick/Auto/Manual arbeiten, Save-Policy wird respektiert.  
- **Performance**: Zielwerte aus ARCHITECTURE/TOOLING eingehalten.

---

## 21) Glossar

- **Intent**: beabsichtigte Aktion (Move/Attack/Shoot/Cast/Use/Wait).  
- **Outcome**: Ergebnis-Event (Hit, Damage, ApplyEffect, Death, Drop).  
- **LOS**: Line of Sight – Sichtlinie.  
- **Kite-Distanz**: Abstand, den Ranged-Gegner halten wollen.  
- **Node**: Sammelstelle (Erz/Baum/Kraut).  
- **Station**: Crafting-Ort (Forge/Alchemy).  
- **Rarity**: Seltenheit (common/rare/epic).

---

## 22) Roadmap-Hinweise (optional/future)

- **Traits/Perks**: permanente Verbesserungen außerhalb Skills  
- **Bossräume**: spezielle Muster/Mechaniken  
- **Events**: Raumfallen, Schalter, Türen/Schlösser (`lockpicking`)  
- **Handel**: NPC-Shop, Preise aus `value` Feldern der Items  
- **Shader-Polish**: Vignette/Scanlines, UI-Animations

---

## 23) Verweise

- **Architektur**: `ARCHITECTURE.md`  
- **Tooling/CI**: `TOOLING.md`  
- **Datenformate**: `data.md`  
- **Tasks**: `task.md` + `tasks/M1..M5.md`  
- **Save/Load**: `M5` + `SAVELOAD.md` (falls vorhanden)

> Dieses Dokument ist **spielmechanische Referenz**. Änderungen an Regeln passieren **datengetrieben** (JSON) und werden hier kurz dokumentiert.
