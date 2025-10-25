# FORD Input & Rebinding System

**Status:** Living Document • **Last Updated:** 2025-10-25

This document describes the input system, keybinding configuration, and rebinding mechanics for FORD. All input is context-aware and fully rebindable.

---

## 🎮 **Input System Architecture**

```
┌───────────────────────────────────────────────────────────────┐
│ INPUT LAYER                                                    │
│                                                                │
│  Keyboard/Mouse/Gamepad                                       │
│           ↓                                                    │
│  Raw Input Events (Arcade Input Handlers)                     │
│           ↓                                                    │
│  Input Manager (normalize & buffer)                           │
│           ↓                                                    │
│  Context Router (overworld/combat/ui)                         │
│           ↓                                                    │
│  Action Mapper (key → action)                                 │
│           ↓                                                    │
│  Game Systems (movement, combat, UI)                          │
└───────────────────────────────────────────────────────────────┘
```

---

## 📂 **Input Contexts**

FORD uses context-based input to prevent conflicts and provide intuitive controls:

| Context | When Active | Priority | Examples |
|---------|-------------|----------|----------|
| **UI** | Modal, dialog, menu open | **Highest** | ESC to close, WASD to navigate |
| **Combat** | In turn-based battle | **High** | Number keys for abilities, Space to end turn |
| **Overworld** | Exploring dungeon | **Normal** | WASD to move, E to interact, Tab for inventory |
| **Rebind** | Rebinding keys | **Exclusive** | Captures all input |

**Context Switching:**
- Contexts stack (UI > Combat > Overworld)
- Higher priority contexts block lower ones
- ESC typically pops the top context

---

## ⌨️ **Default Keybindings**

### **Overworld Context**

| Action | Primary | Secondary | Description |
|--------|---------|-----------|-------------|
| **Movement** |  |  |  |
| `move_up` | W | ↑ | Move north |
| `move_down` | S | ↓ | Move south |
| `move_left` | A | ← | Move west |
| `move_right` | D | → | Move east |
| `move_nw` | Q |  | Move northwest (diagonal) |
| `move_ne` | E |  | Move northeast (diagonal) |
| `move_sw` | Z |  | Move southwest (diagonal) |
| `move_se` | C |  | Move southeast (diagonal) |
| **Actions** |  |  |  |
| `interact` | E | Enter | Interact with objects/NPCs |
| `use_item` | U |  | Open usables menu |
| `open_inventory` | I | Tab | Open inventory |
| `open_character` | C |  | Open character sheet |
| `open_map` | M |  | Open dungeon map |
| `open_journal` | J |  | Open quest journal |
| `rest` | R |  | Rest/meditate (regen mana) |
| `auto_explore` | X |  | Auto-explore fog of war |
| **Utility** |  |  |  |
| `quick_save` | F5 |  | Quick save |
| `quick_load` | F9 |  | Quick load |
| `toggle_fps` | F3 |  | Show FPS/debug info |
| `screenshot` | F12 |  | Take screenshot |
| `menu` | ESC |  | Open main menu |

### **Combat Context**

| Action | Primary | Secondary | Description |
|--------|---------|-----------|-------------|
| **Movement** |  |  |  |
| `move_tile` | Mouse Click | WASD | Move to clicked tile |
| `confirm_move` | Enter | Space | Confirm movement |
| `cancel_move` | ESC | Right Click | Cancel movement |
| **Combat Actions** |  |  |  |
| `attack` | Left Click | A | Attack selected target |
| `target_next` | Tab | Mouse Wheel | Cycle targets forward |
| `target_prev` | Shift+Tab |  | Cycle targets backward |
| `skill_1` | 1 |  | Use skill slot 1 |
| `skill_2` | 2 |  | Use skill slot 2 |
| `skill_3` | 3 |  | Use skill slot 3 |
| `skill_4` | 4 |  | Use skill slot 4 |
| `skill_5` | 5 |  | Use skill slot 5 |
| `skill_6` | 6 |  | Use skill slot 6 |
| `skill_7` | 7 |  | Use skill slot 7 |
| `skill_8` | 8 |  | Use skill slot 8 |
| `use_item_combat` | U |  | Use consumable item |
| `defend` | D |  | Defensive stance (+parry, end turn) |
| `end_turn` | Space | Enter | End turn immediately |
| **Utility** |  |  |  |
| `show_ranges` | Alt | Hold | Show movement/attack ranges |
| `combat_log` | L |  | Toggle combat log |
| `flee` | F |  | Attempt to flee combat |

### **UI Context**

| Action | Primary | Secondary | Description |
|--------|---------|-----------|-------------|
| `ui_up` | W | ↑ | Navigate up |
| `ui_down` | S | ↓ | Navigate down |
| `ui_left` | A | ← | Navigate left |
| `ui_right` | D | → | Navigate right |
| `ui_confirm` | Enter | E | Confirm selection |
| `ui_cancel` | ESC | Backspace | Cancel/close |
| `ui_tab_next` | Tab |  | Next tab |
| `ui_tab_prev` | Shift+Tab |  | Previous tab |
| `ui_page_up` | Page Up |  | Scroll up (page) |
| `ui_page_down` | Page Down |  | Scroll down (page) |
| `ui_delete` | Delete |  | Delete item/confirm destructive action |
| `ui_sort` | R |  | Sort inventory |
| `ui_filter` | F |  | Toggle filters |

---

## 🎛️ **Input Configuration File**

Location: `config/controls.json`

### **Format:**

```json
{
  "version": "1.0",
  "contexts": {
    "overworld": {
      "move_up": {
        "keys": ["W", "UP"],
        "gamepad": ["DPAD_UP", "LEFT_STICK_UP"],
        "repeat": true,
        "repeat_delay": 0.5,
        "repeat_interval": 0.1
      },
      "interact": {
        "keys": ["E", "RETURN"],
        "gamepad": ["A"],
        "repeat": false
      },
      "open_inventory": {
        "keys": ["I", "TAB"],
        "gamepad": ["START"],
        "repeat": false
      }
    },
    "combat": {
      "skill_1": {
        "keys": ["1"],
        "gamepad": ["X"],
        "repeat": false
      },
      "end_turn": {
        "keys": ["SPACE", "RETURN"],
        "gamepad": ["A"],
        "repeat": false
      }
    },
    "ui": {
      "ui_up": {
        "keys": ["W", "UP"],
        "gamepad": ["DPAD_UP", "LEFT_STICK_UP"],
        "repeat": true,
        "repeat_delay": 0.3,
        "repeat_interval": 0.05
      },
      "ui_confirm": {
        "keys": ["RETURN", "E"],
        "gamepad": ["A"],
        "repeat": false
      }
    }
  },
  "settings": {
    "mouse_sensitivity": 1.0,
    "gamepad_deadzone": 0.15,
    "gamepad_sensitivity": 1.0,
    "double_tap_window": 0.25,
    "hold_threshold": 0.5
  }
}
```

### **Field Descriptions:**

| Field | Type | Description |
|-------|------|-------------|
| `version` | string | Config file version for migration |
| `contexts` | object | Map of context name → actions |
| `keys` | array | Primary and secondary key bindings |
| `gamepad` | array | Gamepad button/axis bindings |
| `repeat` | boolean | Whether key repeats when held |
| `repeat_delay` | float | Seconds before first repeat |
| `repeat_interval` | float | Seconds between repeats |

---

## 🔧 **Rebinding System**

### **Rebind Flow:**

```
1. Player opens Settings → Controls
2. Selects action to rebind (e.g., "move_up")
3. Clicks "Rebind Primary" or "Rebind Secondary"
4. UI enters "listening" mode (shows "Press any key...")
5. Player presses desired key
6. System validates:
   ├─> Check if key is already bound in this context
   ├─> Offer to swap bindings if conflict
   └─> Reject if reserved key (ESC, F1-F12 protected)
7. Save binding to config/controls.json
8. Reload input system
```

### **Conflict Resolution:**

**Scenario:** Player tries to bind `E` to `move_up`, but `E` is already bound to `interact`.

```
┌────────────────────────────────────────────────────┐
│ Keybinding Conflict                                │
├────────────────────────────────────────────────────┤
│ The key 'E' is already bound to 'interact'.        │
│                                                     │
│ What would you like to do?                         │
│                                                     │
│  [ Swap Bindings ]                                 │
│    move_up: W → E                                  │
│    interact: E → W                                 │
│                                                     │
│  [ Replace (unbind interact) ]                     │
│    move_up: W → E                                  │
│    interact: E → (none)                            │
│                                                     │
│  [ Cancel ]                                        │
│    Keep current bindings                           │
└────────────────────────────────────────────────────┘
```

### **Reserved Keys:**

These keys cannot be rebound (hardcoded system functions):

| Key | Function | Reason |
|-----|----------|--------|
| `ESC` | Menu/Cancel | Universal escape |
| `F1` | Help | Universal help |
| `F3` | Debug Toggle | Development |
| `F5`/`F9` | Quick Save/Load | Safety |
| `F10` | Settings | Accessibility |
| `F11` | Fullscreen | System |
| `F12` | Screenshot | System |
| `Alt+F4` | Quit Application | OS-level |

---

## 🎮 **Gamepad Support**

### **Supported Controllers:**

- Xbox Controllers (Xbox One, Xbox Series X/S)
- PlayStation Controllers (PS4, PS5 via DS4Windows)
- Generic DirectInput/XInput gamepads
- Steam Deck (native)

### **Default Gamepad Layout (Xbox):**

```
         LB              RB
         ↓               ↓
    ┌─────────────────────────┐
    │         View  Menu      │   View = Map/Journal
    │           ○    ○         │   Menu = Inventory
    │                          │
    │     Y (Skill 4)          │
    │      ↑                   │
    │  X ← ● → B               │   X = Skill 3
    │      ↓ (Skill 1)         │   Y = Skill 4
    │     A                    │   B = Skill 2
    │  (Confirm)               │   A = Confirm/Interact
    │                          │
    │   D-Pad        (A)(B)    │   D-Pad = Movement
    │    ↑          (X)(Y)     │   Right Face = Skills
    │  ← + →                   │
    │    ↓                     │
    │                          │
    │  Left Stick  Right Stick │   Left = Move
    │     ●            ●       │   Right = Camera (unused)
    │                          │
    │         LT      RT       │   LT = Defend
    │         ↓       ↓        │   RT = Attack
    └─────────────────────────┘
```

### **Gamepad-Specific Actions:**

| Button | Overworld | Combat | UI |
|--------|-----------|--------|-----|
| **A** | Interact | Confirm Action | Confirm |
| **B** | Back/Cancel | Cancel | Back |
| **X** | Use Item | Skill 3 | Sort |
| **Y** | Character Sheet | Skill 4 | Filter |
| **LB** | Prev Tab | Prev Target | Prev Tab |
| **RB** | Next Tab | Next Target | Next Tab |
| **LT** | Rest | Defend | - |
| **RT** | Auto-Attack | Attack | - |
| **View** | Map | Combat Log | - |
| **Menu** | Inventory | Inventory | - |
| **D-Pad** | Move 8-way | Move Cursor | Navigate UI |
| **Left Stick** | Move 8-way | Move Cursor | Navigate UI |
| **Right Stick** | - | - | Scroll |

---

## ⚙️ **Input Settings**

### **Mouse Settings:**

| Setting | Default | Range | Description |
|---------|---------|-------|-------------|
| `mouse_sensitivity` | 1.0 | 0.5-2.0 | Mouse movement speed |
| `invert_y` | false | bool | Invert Y-axis (camera) |
| `double_click_speed` | 0.3s | 0.1-0.5s | Double-click window |

### **Gamepad Settings:**

| Setting | Default | Range | Description |
|---------|---------|-------|-------------|
| `gamepad_deadzone` | 0.15 | 0.0-0.5 | Analog stick deadzone |
| `gamepad_sensitivity` | 1.0 | 0.5-2.0 | Stick sensitivity |
| `invert_right_stick_y` | false | bool | Invert right stick Y |
| `vibration_enabled` | true | bool | Controller vibration |
| `vibration_strength` | 0.8 | 0.0-1.0 | Vibration intensity |

### **Keyboard Settings:**

| Setting | Default | Range | Description |
|---------|---------|-------|-------------|
| `key_repeat_delay` | 0.5s | 0.1-1.0s | Time before key repeats |
| `key_repeat_interval` | 0.1s | 0.05-0.3s | Time between repeats |
| `chord_timeout` | 1.0s | 0.5-2.0s | Timeout for key chords |

---

## 🔗 **Chords & Modifiers**

### **Modifier Keys:**

| Modifier | Symbol | Usage |
|----------|--------|-------|
| `Shift` | ⇧ | Shift+Key combinations |
| `Ctrl` | ⌃ | Ctrl+Key combinations |
| `Alt` | ⌥ | Alt+Key combinations |

### **Example Chords:**

```json
{
  "quick_slot_1": {
    "keys": ["Shift+1"],
    "description": "Use quick slot item 1"
  },
  "mark_waypoint": {
    "keys": ["Ctrl+M"],
    "description": "Mark custom waypoint on map"
  },
  "show_all_tooltips": {
    "keys": ["Alt"],
    "hold": true,
    "description": "Show all item tooltips (hold)"
  }
}
```

### **Chord Validation Rules:**

1. **No Conflicts:** `Shift+1` and `1` can coexist
2. **Modifier Priority:** `Ctrl+Shift+A` > `Shift+A` > `A`
3. **Hold Modifiers:** `Alt` held shows temporary UI overlays
4. **Reserved Combos:** `Ctrl+S` (Save), `Ctrl+Q` (Quit) protected

---

## 📊 **Input State Machine**

```
┌──────────────────────────────────────────────────────┐
│ STATE: OVERWORLD                                      │
│  ├─> Press ESC → Push UI Context (Menu)              │
│  ├─> Enter Combat → Push Combat Context              │
│  └─> Press I → Push UI Context (Inventory)           │
│                                                       │
│ STATE: UI (Menu)                                      │
│  ├─> Press ESC → Pop UI Context → Return OVERWORLD   │
│  └─> Select "Quit" → Push UI Context (Confirm)       │
│                                                       │
│ STATE: COMBAT                                         │
│  ├─> End Combat → Pop Combat Context → OVERWORLD     │
│  ├─> Press I → Push UI Context (Inventory)           │
│  └─> Press ESC → Push UI Context (Pause)             │
│                                                       │
│ STATE: REBIND                                         │
│  ├─> Press Any Key → Capture → Validate → Pop        │
│  └─> Press ESC → Cancel → Pop                        │
└──────────────────────────────────────────────────────┘
```

---

## 🧪 **Testing & Accessibility**

### **Input Testing Checklist:**

- [ ] All actions bindable to any non-reserved key
- [ ] Gamepad and keyboard inputs don't conflict
- [ ] Context switching prevents input bleed
- [ ] Repeat delay/interval works correctly
- [ ] Chords (Shift/Ctrl/Alt+Key) function properly
- [ ] Config saves/loads correctly
- [ ] Invalid bindings are rejected gracefully

### **Accessibility Features:**

| Feature | Description |
|---------|-------------|
| **Fully Rebindable** | Every action can be remapped |
| **Multiple Bindings** | Primary + Secondary keys per action |
| **One-Handed Layouts** | Preset for left/right hand only |
| **Key Repeat** | Adjustable delay/interval for hold-to-repeat |
| **Gamepad Support** | Full game playable without keyboard/mouse |
| **No Timing Requirement** | Turn-based = no twitch input needed |
| **Large UI Targets** | Mouse/touch-friendly click areas |

---

## 📁 **Related Files**

- **Config:** `config/controls.json` - User keybindings
- **Code:** `game/input/input_manager.py` - Input handling
- **Code:** `game/input/context_manager.py` - Context switching
- **Code:** `game/ui/rebind_screen.py` - Rebinding UI
- **Docs:** `docs/DEVELOPMENT.md` - Input system architecture

---

## 🔧 **Implementation Notes**

### **Arcade Integration:**

```python
# Example: Registering context-aware input
class InputManager:
    def __init__(self):
        self.contexts = {}
        self.context_stack = ["overworld"]

    def register_action(self, context: str, action: str, callback):
        if context not in self.contexts:
            self.contexts[context] = {}
        self.contexts[context][action] = callback

    def on_key_press(self, key, modifiers):
        current_context = self.context_stack[-1]
        config = load_controls()

        for action, binding in config["contexts"][current_context].items():
            if key in binding["keys"]:
                callback = self.contexts[current_context].get(action)
                if callback:
                    callback()
                    return True  # Consumed

        return False  # Not handled
```

### **Save Format:**

```json
{
  "user": "player_name",
  "version": "1.0",
  "last_modified": "2025-10-25T14:30:00Z",
  "contexts": { ... },
  "settings": { ... }
}
```

---

**Questions?** Check `docs/ARCHITECTURE.md` for input system class diagram.
