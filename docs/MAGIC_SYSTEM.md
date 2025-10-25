# MAGIC_SYSTEM (FORD) — Schulen, Kreise, Reagenzien, Casting

## 1) Ziele
- UO‑nah, aber rundenbasiert: **Cast‑Runden**, **Fizzle**, **Reagenzien**, **Meditation**.
- Rollen: **DPS**, **CC**, **Support**, **Utility** – nicht nur „Fernkampf in anders“.

---

## 2) Kernskills
- **Magery** (Wirkerfolg/Power), **Evaluate Intelligence** (Schadensskalierung),
- **Meditation** (Mana‑Regeneration; ggf. `cast_rounds −1`, min 0),
- **Resist Spells** (Dauer/Intensität gegnerischer Effekte ↓).

---

## 3) Schulen & Kreise
**Schulen:** Feuer, Kälte, Gift, Energie, Erde (optional: Nekromantie).
**Kreise:** 1–8 (höher = mehr Mana/Reags/Cast‑Runden).

---

## 4) Reagenzien (UO‑nah)
Black Pearl • Bloodmoss • Garlic • Ginseng • Mandrake Root • Nightshade • Sulfurous Ash • Spider's Silk

---

## 5) Zauber‑Datenmodell
```json
{
  "id": "fireball",
  "name": "Fireball",
  "school": "fire",
  "circle": 3,
  "cost": { "mana": 8, "reagents": { "Black Pearl": 1, "Sulfurous Ash": 1 } },
  "cast_rounds": 1,
  "range_tiles": 5,
  "effects": [{ "type": "damage", "element": "fire", "base": 18, "variance_pct": 0.2, "scaling": { "INT": 0.15 } }],
  "fizzle": { "base": 0.15, "magery_factor": -0.001 },
  "resist_check": { "type": "resist_spells", "scale": 200 },
  "ai_tags": ["nuke"]
}
```

**Regeln:**
- **Fizzle** vor Wirkung; Magery senkt Fizzle. Meditation kann Castingdauer um 1 reduzieren (min 0).
- **Resist**: verteidigungsseitig über `resist_spells` & Element‑Resists (combat_rules).
- **Scrolls**: einmalige Casts ohne Magery‑Check (gut zum „Probefliegen“ höherer Kreise).

---

## 6) Beispiele
- **Fireball** (Fire‑3): 2d6 + INT*0.2, 1 Runde, AoE‑Splash klein (optional).
- **Ice Shackles** (Cold‑4): Root 1 Runde, Move‑Tiles −1 (resistierbar).
- **Poison Cloud** (Toxic‑5): 3×3‑AoE, DoT 3 Runden, Sichtschleier.
- **Blink** (Arcanum‑3): Teleport 3 Tiles, Cast 0, interagiert mit Dodge/Recovery nicht.
- **Stone Ward** (Earth‑2): +Resist (blunt/pierce) 2 Runden.

---

## 7) Training & Balance
- Sweet‑Spot ≈ 50% Erfolg (inkl. Fizzle); 0.1‑Gains usage‑basiert (progression_rules).
- Resist‑Decke 75%, 0‑Cast‑Spells schwächer.
- TTK Mage ≈ Melee in T1/T3 über Szenarien verproben.
