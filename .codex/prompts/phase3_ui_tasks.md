# Phase 3 Prompt: Complete UI System Tasks (M6-UI Milestone)

## Context
You are creating **18 tasks** (1 umbrella + 17 subtasks) for the **complete UI system** based on `UI_SPEC_UO_STYLE.md`. This is the **largest gap** identified in Cross-Reference Analysis - the UI spec has **ZERO task coverage**.

## Source Documents (READ THESE FIRST)
1. **`docs/CROSS_REFERENCE_ANALYSIS.md`** (Section 11: UI_SPEC_UO_STYLE analysis)
2. **`docs/UI_SPEC_UO_STYLE.md`** (Complete 900+ line UI specification)

## Existing Task Schema (FOLLOW EXACTLY)
[Same as previous phases]

---

## Tasks to Create

### 1. **TASK-M6-UI.md** (Umbrella Task)
- **Title**: "Complete UI System (UO-Style HUD, Paperdoll, Skills, Inventory, Tooltips)"
- **Status**: Proposed
- **Priority**: P0
- **Artifacts**: Overview document
- **DependsOn**: TASK-M3-02 (Items), TASK-M3-06 (Skills), TASK-M4-02 (Crafting), TASK-M2-08 (Initiative)
- **Notes**:
  - Reference **UI_SPEC_UO_STYLE.md** (complete spec)
  - Leitprinzipien: Lesbarkeit > Ornament, datengetrieben, UO-Flair, 0.1-Skillgains sichtbar, rundenbasiert
  - Modularität: Fenster andockbar, skalierbar, per Tab gruppierbar
  - Localization-ready: alle Strings via Keys
  - Input: Maus + Tastatur (QWERTZ), optional Controller
  - Barrierefreiheit: Schriften skalierbar, Farbenblind-Profile, Kontraste konfigurierbar
  - List 17 subtasks (M6-UI-01..17)
- **Acceptance**: All 17 subtasks completed, full UI operational
- **Tests**: UI integration tests (data binding, event flow)

### 2. **TASK-M6-UI-01.md**: UI Framework & Architecture
- **Title**: "UI Framework & Architecture (React/TypeScript, Event Bus, State Management)"
- **Priority**: P0
- **Artifacts**: `game/ui/framework.py` (or React/TS setup), `game/ui/event_bus.py`, `tests/ui/test_framework.py`
- **DependsOn**: None (foundational)
- **Notes**:
  - Tech stack: React/TypeScript (or Arcade UI if simpler)
  - UI-State: Zustand/Recoil/Redux (or Python equivalent)
  - Event-Bus: Pub/Sub for game events (SKILL_GAIN, HIT_RESULT, LOOT_ADDED, CRAFT_DONE, COMBAT_TURN_START, etc.)
  - Data bindings: `ui.hp.value ← stats.hp.current`, `ui.skills["swords"].value ← skills.swords.value`
  - Tooltip engine: Markdown-fähig, Lazy Load on hover
  - Persistenz: Layout & Hotkeys in `ui_profile.json` (per save slot)
  - Reference **UI_SPEC_UO_STYLE.md § 16 (Frontend), § 13 (Event-Bus), § 17 (Mapping zu Dateien)**
- **Acceptance**:
  - [ ] UI framework initialized (React or Arcade UI)
  - [ ] Event bus operational (publish/subscribe)
  - [ ] State management working (bindings reactive)
  - [ ] Tooltip engine functional (Markdown support)
- **Tests**:
  - [ ] Event bus pub/sub tests
  - [ ] Data binding tests
  - [ ] Tooltip render tests

### 3. **TASK-M6-UI-02.md**: HUD (HP/Mana/Stamina/Buffs/Hotbar/Journal/Minimap)
- **Title**: "HUD (HP/Mana/Stamina Bars, Buff/Debuff Pips, Hotbar, Journal, Minimap)"
- **Priority**: P0
- **Artifacts**: `game/ui/hud.py`, `tests/ui/test_hud.py`
- **DependsOn**: TASK-M6-UI-01 (Framework), TASK-M2-02 (Stats), TASK-M2-05 (Effects), TASK-M3-04 (Inventory)
- **Notes**:
  - Statusleisten (oben links): HP/Mana/Stamina/Weight (Balken + Zahlen)
  - Buff/Debuff-Pips: Icons mit Restdauer (Runden oder Sekunden), Tooltip: Quelle, Effekt, Formelhinweis
  - Hotbar (unten): 10 Slots (1-0 + F-Tasten), Drag-Drop aus Inventar, Cooldown-Overlays
  - Journal/Combat-Log (links unten, einklappbar): "+0.1 in *Tinkering* (57.3)", "You miss the orc", Filter (All/System/Loot/Craft/Combat/Quests)
  - Minimap (rechts oben): Spieler-Pfeil, Gegner (rot), Verbündete (grün), Container-Marker, Encounter-Bubble-Radius (lila Rand)
  - Reference **UI_SPEC_UO_STYLE.md § 2.1-2.4**
- **Acceptance**:
  - [ ] HP/Mana/Stamina bars update in real-time
  - [ ] Buff/Debuff pips show duration & tooltip
  - [ ] Hotbar accepts Drag-Drop, triggers actions on keypress
  - [ ] Journal logs events (0.1 gains, combat outcomes)
  - [ ] Minimap displays actors & encounter bubble
- **Tests**:
  - [ ] HP/Mana update tests (data binding)
  - [ ] Buff pip tests (duration countdown)
  - [ ] Hotbar action tests (keypress → inventory use)
  - [ ] Journal filter tests

### 4. **TASK-M6-UI-03.md**: Initiative Bar (Combat)
- **Title**: "Initiative Bar (Combat Turn Order, Recovery Indicators)"
- **Priority**: P0
- **Artifacts**: `game/ui/initiative_bar.py`, `tests/ui/test_initiative_bar.py`
- **DependsOn**: TASK-M6-UI-01 (Framework), TASK-M2-08 (Initiative), TASK-M2-04 (Combat)
- **Notes**:
  - Display: Top of screen during combat
  - Shows: Actor portraits in turn order (left-to-right)
  - Indicators: Current turn highlighted, Recovery/Reload shown as **grauer Cooldown-Ring**
  - Move tiles & actions remaining visible
  - Reference **UI_SPEC_UO_STYLE.md § 2.5**
- **Acceptance**:
  - [ ] Initiative order displayed correctly
  - [ ] Current turn highlighted
  - [ ] Recovery/Reload cooldown rings animate
  - [ ] Move tiles & actions shown
- **Tests**:
  - [ ] Initiative order tests (varied DEX/rolls)
  - [ ] Cooldown ring tests (recovery countdown)

### 5. **TASK-M6-UI-04.md**: Character Window (Paperdoll + Stats)
- **Title**: "Character Window (Paperdoll, Attributes, Combat Stats, Resistances)"
- **Priority**: P0
- **Artifacts**: `game/ui/character_window.py`, `tests/ui/test_character_window.py`
- **DependsOn**: TASK-M6-UI-01 (Framework), TASK-M3-03 (Equipment), TASK-M2-02 (Stats)
- **Notes**:
  - Layout: Paperdoll left, Stats tabs right
  - Paperdoll: Drag-Drop items onto slots (Kopf, Hals, Brust, Arme, Hände, Finger, Beine, Füße, Umhang, Gürtelslot, Rucksack)
  - Context menu: Ablegen, Vergleichen, Reparieren (if tool), Färben (if dye)
  - Stats tabs:
    - **Attribute**: STR/DEX/INT/STAM (current/cap), kleine Pfeile für Stat-Gains heute
    - **Kampfwerte**: ATK/DEF, Resistenzen (slash/pierce/blunt/fire/cold/poison/energy), Initiative-Mod, Move-Tiles, Recovery-Mod
    - **Gewichte**: Gesamtgewicht, Encumbrance-Stufe (leicht/mittel/schwer), Einfluss auf Move-Tiles
  - Tooltips: Formel-Shortcuts (z.B. "ATK = weaponskill + ⌊DEX/5⌋ + Gear + Buffs")
  - Reference **UI_SPEC_UO_STYLE.md § 3**
- **Acceptance**:
  - [ ] Paperdoll accepts Drag-Drop (equip/unequip)
  - [ ] Stats tabs show all attributes/combat stats/resistances
  - [ ] Tooltips show formula hints
  - [ ] Stat gain arrows visible (today's gains)
- **Tests**:
  - [ ] Drag-Drop tests (equip item → stats update)
  - [ ] Formula tooltip tests (data-driven)
  - [ ] Stat gain arrow tests

### 6. **TASK-M6-UI-05.md**: Skills Window (0.1 resolution, Locks, Caps, Curves, Train/Use)
- **Title**: "Skills Window (0.1 Display, Locks, Caps, Curves, Train/Use)"
- **Priority**: P0
- **Artifacts**: `game/ui/skills_window.py`, `tests/ui/test_skills_window.py`
- **DependsOn**: TASK-M6-UI-01 (Framework), TASK-M3-06 (Skills), TASK-M3-23 (Skill Locks), TASK-M3-24 (Progression Formula)
- **Notes**:
  - Liste: Suchfeld, Kategorien (Combat/Craft/Gathering/Magic/Stealth/Social)
  - Display: 0.1-Auflösung (z.B. "62.7 / 100"), inkl. Gesamt-Cap-Anzeige ("654.3 / 700")
  - Skill-Locks: ▲ (UP), ■ (LOCK), ▼ (DOWN) Icons, Tooltip erklärt Auto-Drop
  - Kurven-Profil: Icon (Linear/Slow-Start/Fast-Start), Tooltip beschreibt Progression
  - Letzte Aktionen: wann genutzt, gegen wen/was, geschätztes p_success (Sweet-Spot Hint)
  - Train/Use-Button: führt ungefährliche Übung aus (z.B. "Shadowboxing" für Wrestling)
  - Skill-Detail-Panel (rechts): Beschreibung, Stat-Affinitäten (STR/DEX/INT/STAM Balken), Verlinkte Rezepte/Spells, Aktive Modi
  - Reference **UI_SPEC_UO_STYLE.md § 4**
- **Acceptance**:
  - [ ] Skills displayed with 0.1 precision
  - [ ] Lock icons (▲■▼) functional (toggle lock state)
  - [ ] Curve profile icons shown with tooltips
  - [ ] Train/Use button works (triggers shadowboxing/practice)
  - [ ] Detail panel shows affinities & linked recipes
- **Tests**:
  - [ ] 0.1 precision display tests
  - [ ] Lock toggle tests (UP/DOWN/LOCK)
  - [ ] Train/Use action tests

### 7. **TASK-M6-UI-06.md**: Inventory UI (Grid + UO-Freeform modes)
- **Title**: "Inventory UI (Grid & UO-Freeform Modes, Stack-Split, Drag-Drop)"
- **Priority**: P0
- **Artifacts**: `game/ui/inventory.py`, `tests/ui/test_inventory.py`
- **DependsOn**: TASK-M6-UI-01 (Framework), TASK-M3-04 (Inventory System)
- **Notes**:
  - Zwei Modi (umschaltbar): Grid-Inventar (komfortabel, tooltipreich), UO-Freeform-Container (Gump-Look, Items frei verschiebbar, Snap-Raster optional)
  - Backpack: Slots/Gewicht/Gold sichtbar, Filter (Waffen/Rüstung/Reagenzien/Materialien/Nahrung/Quest)
  - Stack-Split: Shift+Drag → Split-Dialog (Menge & Auto-Stacken), Ctrl+Click → Schnell-Transfer (in offenen Container)
  - Drag auf Paperdoll: rüstet aus, Drag auf Hotbar: legt Quick-Use an
  - Reparieren (Kontext): prüft Tools/Rezepte, zeigt Erfolgs-Wkeit & Haltbarkeit vorher/nachher
  - Reference **UI_SPEC_UO_STYLE.md § 5.1**
- **Acceptance**:
  - [ ] Grid & Freeform modes toggle
  - [ ] Stack-Split works (Shift+Drag)
  - [ ] Schnell-Transfer works (Ctrl+Click)
  - [ ] Drag-to-Paperdoll equips item
  - [ ] Filter works (show/hide categories)
- **Tests**:
  - [ ] Mode toggle tests
  - [ ] Stack-Split tests
  - [ ] Drag-Drop tests (to paperdoll, hotbar, container)

### 8. **TASK-M6-UI-07.md**: Container UI (Lock/Trap Status, Interactions)
- **Title**: "Container UI (Lock/Trap Status, Take All, Sort, Respawn Timer)"
- **Priority**: P0
- **Artifacts**: `game/ui/container_window.py`, `tests/ui/test_container_window.py`
- **DependsOn**: TASK-M6-UI-01 (Framework), TASK-M3-EXT-01 (Container System)
- **Notes**:
  - Kisten/Truhen/Regale: Sperr-/Fallen-Status mit Icons
  - Buttons: Lockpick, Disarm, Take All, Sort, Filter
  - Respawn-Timer Anzeige (wenn bekannt)
  - Drag-Drop zwischen Inventar ↔ Container
  - Reference **UI_SPEC_UO_STYLE.md § 5.2**
- **Acceptance**:
  - [ ] Lock/Trap icons display correctly
  - [ ] Lockpick/Disarm buttons functional (trigger actions)
  - [ ] Take All/Sort work
  - [ ] Respawn timer shows countdown
- **Tests**:
  - [ ] Icon display tests (lock/trap states)
  - [ ] Button action tests
  - [ ] Timer countdown tests

### 9. **TASK-M6-UI-08.md**: Tooltip System (Data-Driven, Formula Hints)
- **Title**: "Tooltip System (Data-Driven, Formula Hints, Markdown Support)"
- **Priority**: P0
- **Artifacts**: `game/ui/tooltips.py`, `tests/ui/test_tooltips.py`
- **DependsOn**: TASK-M6-UI-01 (Framework)
- **Notes**:
  - Tooltips: Name, Seltenheit, Gewicht, Wert
  - Waffentyp (slash/pierce/blunt), Basis-Schaden, Base-Delay-Klasse (light/medium/heavy), erwartete Recovery (mit DEX)
  - Resist-Werte (bei Rüstungen), Durability (z.B. 36/60)
  - Benötigte Skills (z.B. Magierstab → "Magery 30+")
  - Set-/Unique-Marker (später für Named Items)
  - **Formula Hints**: "ATK = weaponskill + ⌊DEX/5⌋ + Gear + Buffs", "Move = 3 + ⌊DEX/40⌋ (Tiles)"
  - Markdown-fähig, Lazy Load on Hover
  - Reference **UI_SPEC_UO_STYLE.md § 5.3, § 3.2 (Formel-Tooltips)**
- **Acceptance**:
  - [ ] Tooltips show all required fields (name, rarity, weight, stats)
  - [ ] Formula hints displayed (data-driven from combat_rules.json)
  - [ ] Markdown rendering works
  - [ ] Lazy load (no lag on hover)
- **Tests**:
  - [ ] Tooltip content tests (all fields present)
  - [ ] Formula hint tests (correct formulas)
  - [ ] Markdown render tests

### 10. **TASK-M6-UI-09.md**: Spellbook UI
- **Title**: "Spellbook UI (Circle Tabs, Mana/Reagents, Cast Rounds, Drag-to-Hotbar)"
- **Priority**: P1
- **Artifacts**: `game/ui/spellbook.py`, `tests/ui/test_spellbook.py`
- **DependsOn**: TASK-M6-UI-01 (Framework), TASK-M3-06 (Skills - magery)
- **Notes**:
  - Reiter: Circle 1-8 oder thematisch
  - Liste: Sprüche, Kosten (Mana + Reagenzien), Cast-Runden (mit INT/Meditation-Reduktion), Reichweite, Effekte
  - Drag-&-Drop auf Hotbar
  - Rechtsklick: "Als Macro" (Auto-Target-Self/Last)
  - Reference **UI_SPEC_UO_STYLE.md § 6**
- **Acceptance**:
  - [ ] Circle tabs functional
  - [ ] Spell list shows mana/reagents/cast time
  - [ ] Drag-to-Hotbar works
  - [ ] Macro creation works (right-click)
- **Tests**:
  - [ ] Tab switching tests
  - [ ] Drag-Drop tests
  - [ ] Macro creation tests

### 11. **TASK-M6-UI-10.md**: Crafting UI (Recipe List, Queue, Success Tooltip)
- **Title**: "Crafting UI (Recipe List, Detail Panel, Queue with Priorities, Success Tooltip)"
- **Priority**: P0
- **Artifacts**: `game/ui/crafting.py`, `tests/ui/test_crafting.py`
- **DependsOn**: TASK-M6-UI-01 (Framework), TASK-M4-02 (Crafting System)
- **Notes**:
  - Rezept-Liste links: Filter (Kategorie, Station, Skill-Req)
  - Detail-Panel rechts: Inputs (mit Inventar-Zahl), Tool/Station, Erfolgs-Wkeit (Sweet-Spot-Tooltip!), Zeit in Sekunden/Runden, XP-Hinweis (Gain-Chance)
  - Queue mit Prioritäten
  - Im Kampf: gesperrt (läuft in Rundenzeit weiter, UI nur Hinweis)
  - Reference **UI_SPEC_UO_STYLE.md § 7**
- **Acceptance**:
  - [ ] Recipe list filterable (category, station, skill)
  - [ ] Detail panel shows inputs/outputs/success chance/time
  - [ ] Success tooltip shows sweet-spot info
  - [ ] Queue displays jobs with priorities
  - [ ] Combat lock (UI grayed out, jobs continue)
- **Tests**:
  - [ ] Filter tests
  - [ ] Success chance tooltip tests
  - [ ] Queue tests
  - [ ] Combat lock tests

### 12. **TASK-M6-UI-11.md**: Merchant/Trade UI
- **Title**: "Merchant/Trade UI (Buy/Sell Tables, Dynamic Prices, Quick-Sell)"
- **Priority**: P2
- **Artifacts**: `game/ui/merchant.py`, `tests/ui/test_merchant.py`
- **DependsOn**: TASK-M6-UI-01 (Framework), TASK-M3-04 (Inventory)
- **Notes**:
  - Kauf/Verkauf-Tabelle
  - Dynamische Preise (Economy-Hooks, später)
  - Schnellverkauf: Ctrl+Click (mit Bestätigungs-Guard ab "rare")
  - Favoriten & Wunschliste (zeigt Marker, wenn Container/Händler Item führt)
  - Reference **UI_SPEC_UO_STYLE.md § 8**
- **Acceptance**:
  - [ ] Buy/Sell tables functional
  - [ ] Ctrl+Click quick-sell works (with confirmation for rare+)
  - [ ] Favorites/Wishlist works
- **Tests**:
  - [ ] Buy/Sell tests
  - [ ] Quick-sell tests
  - [ ] Favorites tests

### 13. **TASK-M6-UI-12.md**: Interaction Cursor & Targeting (Use-Target, ESC)
- **Title**: "Interaction Cursor & Targeting System (Use-Target, ESC Cancel, Hover LOS)"
- **Priority**: P0
- **Artifacts**: `game/ui/cursor.py`, `tests/ui/test_cursor.py`
- **DependsOn**: TASK-M6-UI-01 (Framework), TASK-M1-04 (LOS)
- **Notes**:
  - Double-Click: Benutzen/Interagieren (UO-like)
  - Rechtsklick: Kontextmenü (Use, Equip, Compare, Split, Drop, Lockpick, Disarm)
  - Use-Target-Cursor: klassischer UO-Cursor für Items/Spells/Skills, mit ESC abbrechbar
  - Hover: zeigt LOS & Reichweite (Kampf), Traps/Lock-Hints (mit Detect Hidden)
  - Reference **UI_SPEC_UO_STYLE.md § 9**
- **Acceptance**:
  - [ ] Double-click triggers use/interact
  - [ ] Right-click context menu works
  - [ ] Use-Target cursor functional (ESC cancels)
  - [ ] Hover shows LOS/range/hints
- **Tests**:
  - [ ] Double-click tests
  - [ ] Context menu tests
  - [ ] Use-Target cursor tests
  - [ ] Hover tooltip tests

### 14. **TASK-M6-UI-13.md**: Hotkey/Keybind System (Remapping, QWERTZ)
- **Title**: "Hotkey/Keybind System (Remapping, QWERTZ Default, Macro Support)"
- **Priority**: P1
- **Artifacts**: `game/ui/keybinds.py`, `tests/ui/test_keybinds.py`
- **DependsOn**: TASK-M6-UI-01 (Framework)
- **Notes**:
  - Shortcuts (QWERTZ Default): C (Charakter), K (Skills), I (Inventar), M (Map), J (Journal), G (Crafting), B (Spellbook), Space (Dodge), R (Repeat Last Action), Tab (Target Switch), Shift (Multi-Select/Stack-Split), Ctrl (Quick-Transfer), F1-F12 (Makros/Hotbar-Reiter), Alt (Tooltips erweitern)
  - Remapping: UI für Neuzuweisung, gespeichert in `ui_profile.json`
  - Makros: Sequenzen (z.B. "Cast Heal → Target Self")
  - Reference **UI_SPEC_UO_STYLE.md § 10**
- **Acceptance**:
  - [ ] QWERTZ defaults work
  - [ ] Remapping UI functional (save to ui_profile.json)
  - [ ] Macros work (sequence execution)
- **Tests**:
  - [ ] Keybind tests (all defaults)
  - [ ] Remapping tests
  - [ ] Macro tests

### 15. **TASK-M6-UI-14.md**: Window Management (Docking, Scaling, Layouts)
- **Title**: "Window Management (Andocken, Größe, Transparenz, Layouts)"
- **Priority**: P1
- **Artifacts**: `game/ui/window_manager.py`, `tests/ui/test_window_manager.py`
- **DependsOn**: TASK-M6-UI-01 (Framework)
- **Notes**:
  - Andocken, Größe, Transparenz je Fenster speicherbar (pro Profil)
  - Layouts: Overworld, Kampf, Handwerk (3 Profile, per Taste umschaltbar)
  - Reset & UI-Skalierung (80-150%)
  - Reference **UI_SPEC_UO_STYLE.md § 11**
- **Acceptance**:
  - [ ] Windows dockable (snap to edges)
  - [ ] Resize/Transparency works (per window)
  - [ ] Layouts switchable (3 profiles)
  - [ ] UI scaling works (80-150%)
- **Tests**:
  - [ ] Docking tests
  - [ ] Layout switch tests
  - [ ] Scaling tests

### 16. **TASK-M6-UI-15.md**: Accessibility (Fonts, Colorblind, Contrast)
- **Title**: "Accessibility (Font Scaling, Colorblind Modes, Contrast, Labeled Icons)"
- **Priority**: P1
- **Artifacts**: `game/ui/accessibility.py`, `tests/ui/test_accessibility.py`
- **DependsOn**: TASK-M6-UI-01 (Framework)
- **Notes**:
  - Schriftgröße (S/M/L/XL), Farbenblind-Profile, Kontrast-Boost
  - Beschriftete Icons (Labels), Tooltips zeitverzögert
  - Tastatur-Remapping, Controller (Radial-Menüs für Kontext/Hotbar)
  - Reference **UI_SPEC_UO_STYLE.md § 12**
- **Acceptance**:
  - [ ] Font scaling works (S/M/L/XL)
  - [ ] Colorblind modes implemented (profiles selectable)
  - [ ] Contrast boost works
  - [ ] Labeled icons option works
- **Tests**:
  - [ ] Font scaling tests
  - [ ] Colorblind profile tests
  - [ ] Contrast boost tests

### 17. **TASK-M6-UI-16.md**: UI Event Bus & Data Bindings
- **Title**: "UI Event Bus & Data Bindings (Game Events → UI Updates)"
- **Priority**: P0
- **Artifacts**: `game/ui/event_bus.py` (extend), `tests/ui/test_event_bindings.py`
- **DependsOn**: TASK-M6-UI-01 (Framework)
- **Notes**:
  - Event-Bus Namen: SKILL_GAIN, STAT_GAIN, HIT_RESULT, LOOT_ADDED, CRAFT_DONE, COMBAT_TURN_START, COMBAT_TURN_END, UI_TOAST, CONTAINER_RESPAWNED
  - Bindings: `ui.hp.value ← stats.hp.current`, `ui.resists.fire ← derivedResists.fire`, `ui.skills["swords"].value ← skills.swords.value` (0.1-Auflösung), `ui.weapon.recoveryPred ← fRecovery(DEX, weapon.base_delay, combat_rules)`
  - Reference **UI_SPEC_UO_STYLE.md § 13**
- **Acceptance**:
  - [ ] Event bus handles all named events
  - [ ] Data bindings reactive (game state → UI)
  - [ ] 0.1 precision for skills preserved
- **Tests**:
  - [ ] Event pub/sub tests
  - [ ] Binding reactivity tests
  - [ ] Precision tests (0.1 skills)

### 18. **TASK-M6-UI-17.md**: Error/State Messages (Toast, Feedback)
- **Title**: "Error/State Messages (Toast Notifications, Status Feedback)"
- **Priority**: P1
- **Artifacts**: `game/ui/messages.py`, `tests/ui/test_messages.py`
- **DependsOn**: TASK-M6-UI-01 (Framework)
- **Notes**:
  - Fehler- & Zustandsmeldungen: Inventar voll (+x/x kg, rote Zahl), Keine Munition (Bogen-Icon blinkt), Recovery aktiv (Angriff-Button grau + Tooltip "Erholung: 1 Runde"), Skill gelockt (Pfeil-Icon wechselt auf "■"), Diebstahlwarnung (Ownership)
  - Toast-System: Kurze Meldungen (3s), nicht blockierend
  - Reference **UI_SPEC_UO_STYLE.md § 14**
- **Acceptance**:
  - [ ] Toast notifications display correctly (3s duration)
  - [ ] Status messages shown (inventory full, no ammo, recovery, skill locked)
  - [ ] Ownership warnings displayed
- **Tests**:
  - [ ] Toast display tests (duration, queue)
  - [ ] Status message tests (all types)

---

## Critical Requirements
[Same as previous phases: follow schema, Created: 2025-10-25, Owner: Copilot Agent, cross-references, etc.]

**Special Note for UI Tasks:**
- Priority: P0 for core (HUD, Paperdoll, Skills, Inventory, Tooltips, Crafting, Cursor, Event Bus), P1 for extensions (Spellbook, Window Mgmt, Keybinds, Accessibility, Messages), P2 for nice-to-have (Merchant)
- Cross-reference **UI_SPEC_UO_STYLE.md** sections extensively (§ 2 for HUD, § 3 for Character, § 4 for Skills, etc.)
- DependsOn chains: Most UI tasks depend on TASK-M6-UI-01 (Framework) + relevant systems (M3-04 Inventory, M3-06 Skills, M4-02 Crafting, etc.)

---

## Output Format
Generate **18 separate Markdown files**:
- `docs/tasks/TASK-M6-UI.md` (umbrella)
- `docs/tasks/TASK-M6-UI-01.md..TASK-M6-UI-17.md`

---

## Validation Checklist (Run After Generation)
- [ ] All 18 files created
- [ ] All files follow schema
- [ ] Cross-references to UI_SPEC_UO_STYLE.md are comprehensive
- [ ] DependsOn chains reference M3/M4/M2 systems correctly
- [ ] Run `pre-commit run --files docs/tasks/TASK-M6-UI*.md`
