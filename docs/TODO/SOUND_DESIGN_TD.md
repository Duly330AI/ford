Analyse von SOUND_DESIGN.md
Gesamtstatus: Das Dokument beschreibt ein professionelles und detailliertes Audio-Konzept, das weit über einfache Sound-Trigger hinausgeht. Die bestehende TASK-Planung deckt jedoch nur die absolut notwendige Schnittstelle (API-Haken) ab, um ein solches System anzubinden, nicht aber die Implementierung des Sound-Systems selbst. Es handelt sich um eine Spezifikation für ein Feature, das architektonisch vorbereitet, aber noch nicht zur Umsetzung geplant ist.
✅ Abgedeckte Aspekte (Die Schnittstelle)
Der entscheidende Punkt, der in den Tasks abgedeckt ist, ist das Adapter-Muster, das die saubere Trennung von Spiellogik und Präsentation gewährleistet.
Audio-Hooks aus der Spiellogik:
TASK-M4-15 (Audio-Hooks) ist die zentrale und einzige Task, die sich direkt mit Audio befasst. Sie fordert die Erstellung einer dünnen API: play_sfx("gather_start"), "craft_complete".
Diese Task stellt sicher, dass die systems-Schicht (die reine Spiellogik) Sound-Events auslösen kann, ohne eine Abhängigkeit zu arcade oder einer Audio-Engine zu haben. Die Akzeptanzkriterien "No-ops in Tests; saubere Aufrufe aus Systems" bestätigen dies.
Dies ist der "Pass 1: Platzhalter + Mixer"-Schritt aus der Roadmap des Dokuments – die Haken sind da, der Mixer selbst aber nicht.
❌ Lücken und fehlende Tasks
Die gesamte Implementierung der Audio-Engine und der Mixing-Logik, die in diesem Dokument beschrieben wird, ist in keiner Task abgedeckt.
Audio-Engine / Mixer:
Lücke: Es gibt keine Task, die den im Dokument beschriebenen "Mixer" mit seinen Bussen (MUSIC, SFX, UI) implementiert. Die gesamte Logik zum Laden, Abspielen und Verwalten von Sounds fehlt.
Fortgeschrittene Audio-Features:
Lücke: Komplexe Features wie Snapshots/States (Reverb in Höhlen), 3D-Positionierung (Distanz-Dämpfung, Panning) und Mixing-Regeln (Side-Chaining) sind neue Anforderungen, für die es keine Tasks gibt.
Regelbasierte Sound-Auswahl:
Lücke: Die Logik, die basierend auf dem Kontext den richtigen Sound auswählt (z.B. "Schritte nach Boden-Tag"), ist nicht Teil von TASK-M4-15. Der Adapter in dieser Task würde nur ein generisches Event wie play_sfx("player_step") empfangen. Die Logik, die dann entscheidet, ob step_stone.wav oder step_wood.wav gespielt wird, müsste in der scenes-Schicht implementiert werden, wofür es keine Task gibt.
Adaptive Musik:
Lücke: Das Konzept der adaptiven Musik-Layer (Pass 3 der Roadmap) ist ein großes, neues Feature, das in keiner Task geplant ist.
Fazit
Das SOUND_DESIGN.md-Dokument ist eine Spezifikation für eine zukünftige, fortgeschrittene Implementierung der Audio-Präsentationsschicht.
Die aktuelle Task-Planung in M1-M6 ist konsistent mit der im Dokument beschriebenen "Pass 1"-Roadmap: Es werden die notwendigen API-Haken (TASK-M4-15) geschaffen, damit die Spiellogik Sound-Events "abfeuern" kann.
Die tatsächliche Implementierung der Audio-Engine, die diese Events empfängt und in hörbaren Ton umsetzt – einschließlich aller fortgeschrittenen Features wie 3D-Sound und Mixing – ist nicht Teil der aktuellen Planung. Um die Vision dieses Dokuments vollständig umzusetzen, wären mehrere neue Tasks erforderlich, die sich explizit mit der Erstellung des "Audio Mixers" und der kontextabhängigen Sound-Logik innerhalb der scenes-Schicht befassen.
