Analyse von INPUT_AND_REBIND.md
Gesamtstatus: Das Dokument beschreibt ein sehr detailliertes und robustes Input-System, das weit über die in den ursprünglichen Tasks geplante Funktionalität hinausgeht.
Die grundlegenden Keybinds für M1-Features sind abgedeckt.
Die Architektur mit kontextabhängigem Input, einem datengetriebenen Konfigurationssystem (controls.json), einem vollständigen Rebinding-UI-Flow und Gamepad-Unterstützung ist nicht in den aktuellen Tasks enthalten und stellt eine Reihe neuer, signifikanter Anforderungen dar.
✅ Abgedeckte Aspekte (Grundlagen)
Die Kernanforderungen an die Steuerung, die für die ersten Meilensteine benötigt werden, sind in den bestehenden Tasks abgedeckt:
Grundlegendes Input-System & Keybinds:
TASK-M1-10 (Input-System & Keybinds) ist die zentrale Aufgabe für die initialen Keybinds. Die Notes erwähnen explizit: "Einheitliche Keymap + Rebind-Hooks für spätere Settings." und die Acceptance-Kriterien fordern "Keymap als Daten (dict), leicht testbar.".
Dies deckt die grundlegende Anforderung ab, dass Aktionen (move_up, regenerate_dungeon) an Tasten (W, R) gebunden sind. Die im INPUT_AND_REBIND.md aufgelisteten Tasten für M1-Features (WASD, R, F3, L) sind in den DependsOn-Links von TASK-M1-10 referenziert.
Player-Controller Anbindung:
TASK-M1-05 (Player-Controller) beschreibt die Verarbeitung des Input-Vektors (WASD/Pfeile), der vom in TASK-M1-10 definierten System geliefert wird.
QuickSave/QuickLoad Tasten:
TASK-M5-09 (QuickSave/QuickLoad UI Adapter) erwähnt explizit die Keybinds F5 und F9 und deren Anbindung an den Save-Service.
❌ Lücken und fehlende Tasks
Das Dokument geht weit über ein einfaches "Keymap-Dictionary" hinaus und beschreibt eine komplette Systemarchitektur, für die es keine Tasks gibt.
Input-Kontexte (UI > Combat > Overworld):
Lücke: Dies ist die größte neue architektonische Anforderung. Das Konzept eines Kontext-Stacks, bei dem UI-Eingaben die Gameplay-Eingaben blockieren, ist in keiner Task definiert. TASK-M1-10 implementiert wahrscheinlich nur eine einzige, globale Keymap.
Benötigte Task: Eine neue Task wie Implement Context-Aware Input Manager wäre erforderlich.
Datengetriebene Konfiguration (config/controls.json):
Lücke: Das INPUT_AND_REBIND.md beschreibt eine komplexe JSON-Struktur, die nicht nur Tasten, sondern auch Gamepad-Buttons, Key-Repeat-Verhalten und globale Einstellungen (mouse_sensitivity, deadzone) enthält. TASK-M1-10 zielt auf eine einfachere In-Code- oder simple JSON-Map ab. Es gibt keine Task, die das Parsen und Anwenden dieser detaillierten controls.json beschreibt.
Vollständiges Rebinding-System (UI & Logik):
Lücke: Der gesamte im Dokument beschriebene Flow – UI zum Auswählen einer Aktion, "Listening"-Modus, Konflikterkennung mit Swap/Replace-Dialog – ist ein großes neues Feature. Während TASK-M1-10 "Rebind-Hooks" erwähnt, ist die tatsächliche Implementierung dieses komplexen Systems nirgendwo geplant.
Benötigte Tasks: Hierfür wären mindestens zwei neue Tasks notwendig: Implement Rebinding UI Screen und Implement Rebinding Logic with Conflict Resolution.
Umfassende Gamepad-Unterstützung:
Lücke: Gamepad-Support ist eine komplett neue Anforderung. Keine der bestehenden Tasks erwähnt die Implementierung von Gamepad-Input, Deadzones, Empfindlichkeit oder die Abbildung auf die verschiedenen Kontexte.
Fortgeschrittene Features (Chords, Modifiers, Input Settings):
Lücke: Konzepte wie Shift+1-Akkorde, "Hold-to-show"-Modifier (wie Alt) und die in den UI-Einstellungen beschriebenen detaillierten Konfigurationsmöglichkeiten sind neue Features, die in keiner Task abgedeckt sind.
Fazit
Das INPUT_AND_REBIND.md ist eine vollständige Design-Spezifikation für ein fortgeschrittenes Input-System, das weit über die MVP-Anforderungen der ersten Meilensteine hinausgeht.
Die bestehende TASK-M1-10 deckt nur das absolute Minimum ab: die Definition der grundlegenden Tasten für Bewegung und Debugging in einer einfachen, datengesteuerten Map.
Um die Vision dieses Dokuments vollständig umzusetzen, müsste ein neuer, dedizierter Milestone oder eine Epic-Task-Gruppe erstellt werden, die sich mit den folgenden Hauptthemen befasst:
Input Context Management
Laden und Verarbeiten von controls.json
Implementierung des Rebinding-UI-Flows
Integration von Gamepad-Support
Die aktuelle Task-Planung enthält diese umfangreichen Arbeiten nicht.
