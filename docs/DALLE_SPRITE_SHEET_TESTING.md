# 🎨 DALL-E Sprite Sheet Prompts - Testing Guide

**Date:** October 26, 2025  
**Goal:** Generate actual sprite sheets (not single sprites) with DALL-E

---

## ❌ WAS IST FALSCH (Mein erster Prompt)

```
"32x32 pixel art sprite of a fantasy warrior 
with sword and shield, retro RPG style, 
transparent background, top-down view"
```

**Problem:**
- ❌ Nur 1 Sprite (nicht animiert)
- ❌ Zu klein (32x32)
- ❌ Keine Grid/Layout Info
- ❌ DALL-E macht einfach was es will

---

## ✅ KORREKTE PROMPTS FÜR SPRITE SHEETS

### **Prompt 1: Direkt Sprite Sheet Format ansprechen**

```
"Create a 512x256 pixel art sprite sheet in a 4x2 grid layout 
with 64x64 pixel frames of a fantasy warrior in retro RPG top-down style:

Top row: Idle animation - 4 frames of a standing warrior 
(frame 1: relaxed, frame 2-4: slight breathing animation)

Bottom row: Walking animation - 4 frames of a warrior walking left 
(frame 1-4: walking cycle, 4 frames of locomotion)

Style: 
- Retro 16-bit RPG pixel art
- Consistent color palette (greens, browns, reds, golds)
- Transparent background
- Top-down perspective
- Grid lines between frames visible for clarity

Equipment: Sword and shield visible in all frames"
```

### **Prompt 2: Multi-Row Sprite Sheet (Better for DALL-E)**

```
"Generate a 512x512 pixel sprite sheet grid (8x8 = 64px frames):

Row 1 (IDLE): 8 frames - static warrior idle pose, varying subtle animations
Row 2 (WALK): 8 frames - walking animation cycle (4 frames looped twice)
Row 3 (ATTACK): 8 frames - sword attack animation (swing and return)
Row 4 (HURT): 4 frames + 4 empty - damage reaction animation
Row 5 (DEATH): 2 frames + 6 empty - death/fall animation
Row 6 (CAST): 6 frames + 2 empty - magic casting pose
Row 7 (BLOCK): 2 frames + 6 empty - shield block pose
Row 8 (EMPTY): all frames empty/transparent

Character: Medieval fantasy warrior with sword and shield
Art style: 16-bit retro RPG pixel art (like Ultima Online)
Colors: Limited palette - greens, browns, oranges, silvers
Transparency: Checkered background to show transparency
Labels: Small frame numbers in corner (1-8) for identification"
```

### **Prompt 3: Direction-Based Sprite Sheet (Most Practical)**

```
"Create a 256x512 pixel sprite sheet with 64x64 pixel frames arranged 
for a top-down RPG character:

Layout (4 columns × 8 rows):

Facing DOWN:
- Row 1 (Idle): 4 frames of standing idle (subtle breathing)
- Row 2 (Walk): 4 frames of walking down (full gait cycle)

Facing UP:
- Row 3 (Idle): 4 frames of standing idle (facing up)
- Row 4 (Walk): 4 frames of walking up (full gait cycle)

Facing LEFT:
- Row 5 (Idle): 4 frames of standing idle (facing left)
- Row 6 (Walk): 4 frames of walking left (full gait cycle)

Facing RIGHT:
- Row 7 (Idle): 4 frames of standing idle (facing right)
- Row 8 (Walk): 4 frames of walking right (full gait cycle)

Character: Medieval warrior with green tunic, sword, shield
Art style: Classic 16-bit pixel art (retro RPG)
Background: Transparent (show as checkerboard)
Grid: Visible thin black lines between all frames
Color palette: Restricted to ~12 colors for authentic pixel art"
```

### **Prompt 4: Combat Actions Sprite Sheet**

```
"Create a 512x384 pixel sprite sheet (64x64 frames, 8x6 grid) 
for a fantasy warrior combat sprite:

Row 1: IDLE (8 frames) - Relaxed stance with subtle breathing
Row 2: WALK (8 frames) - Full walking animation cycle
Row 3: RUN (8 frames) - Fast movement animation  
Row 4: ATTACK (8 frames) - Sword swing attack animation
Row 5: HURT (4 frames) - Damage/knockback reaction, then 4 empty
Row 6: DEATH (3 frames) - Falling animation, then 5 empty

Requirements:
- Pixel art style: 16-bit retro (Ultima Online era)
- Character: Warrior with sword and shield
- Perspective: Top-down view (looking down at character)
- Colors: Limited pixel art palette (greens, browns, oranges, grays)
- Background: Transparent (show checkerboard pattern)
- Frame separators: Thin black grid lines visible
- Frame numbers: Small labels (1-8) in each frame corner
- Consistency: Character size and proportions identical across all frames"
```

---

## 🧪 **TESTING STRATEGY**

### **Test 1: Simple 2x2 Grid (Easiest)**

```
"Create a 128x128 pixel pixel art sprite sheet 
in a 2x2 grid (64px frames each):

Top-left: Warrior idle pose
Top-right: Warrior walking right
Bottom-left: Warrior attacking
Bottom-right: Warrior hurt/damaged

Style: 16-bit retro pixel art, transparent background
Grid lines visible between frames"
```

**Why simple first?**
- Less complex = higher chance DALL-E gets it right
- Easy to see if grid/layout works
- Can iterate from there

### **Test 2: 4x4 Grid (Moderate)**

```
"Create a 256x256 pixel sprite sheet grid (4x4, 64px frames):

Row 1: IDLE - 4 frames of warrior standing (slight animation)
Row 2: WALK - 4 frames of walking animation
Row 3: ATTACK - 4 frames of sword swing
Row 4: HURT - 1 frame damaged, 3 frames empty

16-bit pixel art style, warrior with sword/shield, 
transparent background with visible grid lines"
```

### **Test 3: Full Combat Sheet (Advanced)**

Prompt 4 above (8x6 grid)

---

## 💡 **KEY TRICKS FÜR DALL-E**

### **1. Explizit über GRID sprechen**

❌ FALSCH:
```
"Create a warrior sprite sheet"
```

✅ RICHTIG:
```
"Create a sprite sheet in a 4x2 grid layout 
(64x64 pixel frames, 256x128 total)"
```

### **2. Frames deutlich beschreiben**

❌ FALSCH:
```
"Animation frames of a warrior"
```

✅ RICHTIG:
```
"Top row: IDLE - 4 frames 
 (frame 1: arms down, frame 2-3: breathing, frame 4: arms at rest)"
```

### **3. Visual Separator erwähnen**

❌ FALSCH:
```
"Grid of warrior sprites"
```

✅ RICHTIG:
```
"Grid with thin BLACK LINES between frames
Frame numbers visible in corner (1, 2, 3...)"
```

### **4. Pixel Art Stil spezifizieren**

❌ FALSCH:
```
"Pixel art style"
```

✅ RICHTIG:
```
"16-bit retro pixel art 
(Ultima Online / Diablo style)
Limited color palette: ~12 colors
Authentic chunky pixels visible"
```

### **5. Hintergrund & Transparenz**

❌ FALSCH:
```
"Transparent background"
```

✅ RICHTIG:
```
"Transparent background 
(show as CHECKERBOARD PATTERN to prove transparency)
Character is solid, background is empty/checkered"
```

### **6. Perspektive & Richtung**

❌ FALSCH:
```
"Top-down view"
```

✅ RICHTIG:
```
"Top-down perspective (camera looking down at character)
All poses show character from above
Sword visible at bottom (towards camera)"
```

---

## 🎯 **BEST PROMPT FOR FORD (Meine Recommendation)**

```
"Create a 256x256 pixel sprite sheet with 4x4 grid layout 
(64x64 pixel frames each):

Layout description:

ROW 1 - IDLE ANIMATION (4 frames):
  Frame 1: Warrior standing relaxed
  Frame 2: Slight lean forward (breathing)
  Frame 3: Slight lean back (breathing)
  Frame 4: Neutral stance (loop point)

ROW 2 - WALK ANIMATION (4 frames):
  Frame 1-4: Complete walking cycle (left foot forward, right foot forward)
  Shows natural locomotion

ROW 3 - ATTACK ANIMATION (4 frames):
  Frame 1: Pre-swing stance
  Frame 2: Mid-swing (sword extended)
  Frame 3: Post-swing follow-through
  Frame 4: Return to stance

ROW 4 - SPECIAL POSES (4 frames):
  Frame 1: Hurt/damage reaction
  Frame 2: Block/defend pose
  Frame 3: Death/fallen pose
  Frame 4: Empty/transparent

CHARACTER SPECS:
- Medieval fantasy warrior with sword and shield
- Green tunic, brown boots, medieval armor
- Top-down perspective (looking down)

VISUAL STYLE:
- Retro 16-bit pixel art (Ultima Online / early RPG era)
- Limited color palette (~12 colors max)
- Authentic pixelated appearance
- Transparent background shown as GRAY CHECKERBOARD

TECHNICAL:
- Thin BLACK LINES visible between all 16 frames
- Frame numbers (1-16) small but visible in corners
- Consistent character size and proportions across all frames
- No scaling artifacts - pure pixel art"
```

---

## 📋 **EXPECTED RESULTS**

### ✅ GOOD OUTPUT (What we want):
- PNG with 256x256 dimensions
- Clear 4x4 grid of frames
- Each frame 64x64 pixels
- Checkerboard for transparency
- Grid lines visible
- Same character in all frames
- Animations make sense

### ❌ BAD OUTPUT (What might happen):
- Creates 4 separate images (not grid)
- Wrong dimensions
- No grid lines
- Inconsistent character appearance
- Transparent areas filled with weird colors
- Frames overlap or misaligned

---

## 🧪 **TESTING PLAN**

### **Phase 1: Validate DALL-E Capability**

1. **Use Prompt 1 (Simple 2x2)**
   - If works → proceed to Phase 2
   - If fails → try Prompt 2 variation
   - If both fail → DALL-E probably can't do it

2. **Check output:**
   - Open PNG in image editor
   - Verify grid layout
   - Check frame separation
   - Validate transparency

### **Phase 2: Scale Up**

3. **Use Prompt 2 (4x4 Grid)**
   - Test if larger grid still works
   - Check if animations look right
   - Validate frame consistency

4. **Iterate:**
   - Refine prompt based on results
   - Adjust colors, style, details
   - Get feedback on pixel quality

### **Phase 3: Production**

5. **If works:** Create sprite sheets for all characters
6. **If doesn't work:** Evaluate alternatives:
   - Midjourney (better at grids?)
   - Stable Diffusion API
   - Python Pillow generation
   - Commission pixel artist

---

## 🤔 **HONEST ASSESSMENT**

| Tool | Grid Support | Animation | Quality | Cost |
|------|--------------|-----------|---------|------|
| DALL-E 3 | 🟡 Maybe | 🟡 Uncertain | ✅ Good | 💰 ~$0.02 per image |
| Midjourney | 🟢 Likely | 🟢 Good | ✅ Excellent | 💰 $10-60/month |
| Stable Diffusion | 🟡 Maybe | 🟡 Uncertain | 🟡 OK | 💰 Free or $0.001/image |
| Python + Pillow | 🟢 Yes | 🟢 Yes | 🟡 Simple | 💰 Free |
| Commission Artist | 🟢 Yes | 🟢 Yes | 🟢 Best | 💰 $$$$ |

---

## ✅ **MY RECOMMENDATION FOR FORD**

**Do this:**

1. **Test DALL-E with Prompt from "BEST PROMPT FOR FORD" above**
   - Cost: ~$0.02 per test
   - Time: 2 minutes
   - Result: Definitive answer

2. **If works:** Use it for all character sprites
   - Fast iteration
   - Consistent style
   - Easy updates

3. **If doesn't work:** Fallback to **Python Pillow generation**
   - Deterministic
   - Testable
   - Good enough for gameplay
   - Can generate 100s of sprites instantly

---

**Next:** Wanna test the DALL-E prompt or go straight to Python generation?
