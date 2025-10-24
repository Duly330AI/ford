# GAMEPLAY – UO Addendum (Skill-Progression, Engagement, Dodge)

## B) Skill-Progression – Wie genau spielen die Dateien zusammen?

**Rollen der Dateien**

- `skills.json` — pro Skill `id`, `cap`, `xp_curve` (**Kurven-Profil**), optional `stats`-Affinitäten (STR/DEX/INT/STAM).
- `progression_rules.json` — zentrale **Nutzungs-basierte Gain-Formel** (0.1-Schritte, Sweet-Spot, Slowdown, Anti-Macro) und **Kurven-Profile** unter `curves` (z. B. `linear`, `slow_start`, `fast_start`).
- `combat_rules.json` — Kampfformeln (Treffer/Parry/Schaden/Initiative/Bewegung/Recovery/Dodge).

**Wichtiger Hinweis**: `xp_curve` in `skills.json` ist **kein** „XP-bis-Level“-System. Es ist ein **Profil-Schlüssel**, der in `progression_rules.json.curves` auf eine Kurve zeigt, die die **Wahrscheinlichkeit eines 0.1-Gains** über den Skillverlauf moduliert.

**Ablauf (Pseudocode)**

```
onSkillUse(skillId, context):
  s = getSkill(actor, skillId)                   # aktueller Wert 0..cap
  cap = getCap(skillId)                          # z. B. 100
  cfg = progression_rules.skill                  # Basiswerte
  curve = progression_rules.curves[ skills[skillId].xp_curve or "linear" ]

  p_success = computeSuccessChance(context)      # 0..1 (HitChance, Craft-Success etc.)
  sweet = 1.0 - abs(p_success - cfg.sweet_spot_center) / 0.5
  slowdown = slowdown_fn(s.value/cap, curve.slowdown)   # z. B. quadratic/cubic/sqrt
  anti_macro = antiMacroMultiplier(context)      # 1.0..0.2

  P = clamp(cfg.min_gain,
            cfg.base * curve.base_mult * sweet * slowdown * anti_macro,
            cfg.max_gain)

  if roll() < P:
      s.value = min(cap, s.value + cfg.increment)       # +0.1
      tryStatGains(skillId)                              # Chance je Stat nach Skill-Affinitäten
```

Damit ist klar: **`progression_rules.json` gibt die Formel vor**, `skills.json.xp_curve` **parametrisiert** sie pro Skill.

---

## C) Echtzeit-Engagement & Runden-Kampf

**Auslöser**: Gegner sieht Spieler (Radius + LOS) → **Encounter-Bubble** (Radius 12 Tiles) → **Kampfmodus**.

- **Teilnehmer**: Alle Gegner in der Bubble mit LOS. Neue Gegner, die später eintreten, joinen am **Beginn der nächsten Runde**. Beschwörungen joinen sofort.
- **Entkommen**:
  - Am **Rundenende**: Wenn **kein** Gegner LOS hat **und** Distanz ≥ *leash_break* (10 Tiles) für die gesamte Runde, steigt ein **Disengage-Countdown** (1 Runde). Hält die Bedingung über eine volle Runde → Overworld.
  - Optionale **„Flee“-Aktion** (Hauptaktion): verleiht +leash_margin (leichteres Entkommen) und +evade% bis Zugende.
- **Zeitbasis**: 1 Runde = **3 s** Sim-Zeit.
- **Crafting-Queues**: Laufen auf Rundenzeit **weiter**. Abschlüsse während des Kampfes werden **markiert** und sind nach dem Kampf abholbar (kein UI-Spam).
- **Node-Respawn**: **Pausiert** per Default (Anti-Exploit). Umschaltbar in `world_rules.json`.

---

## D) Die „Dodge-Roll“

- **Overworld**: *Space* = Dodge-Roll (i-frames), **Stamina-Kosten**.
- **Kampf**: *Space* ist an die **„Dodge“-Aktion** gebunden:
  - **Hauptaktion**, bewegt **1 Tile** („dash“) und gewährt `+evade%` bis **Zugende**.
  - **Stamina-Kosten** & Werte stehen in `combat_rules.json.dodge`.
  - Beeinflusst **recovery** nicht; blockiert, wenn „immobilized“.
