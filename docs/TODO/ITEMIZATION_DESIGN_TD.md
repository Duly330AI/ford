Analyse von ITEMIZATION_DESIGN.md
Gesamtstatus: Das Dokument beschreibt ein sehr fortgeschrittenes, dynamisches Item-Generierungssystem, das weit über das in Milestone M3 geplante System hinausgeht.
Die Grundlagen (Items mit Typen, Mods und Raritäten) sind abgedeckt.
Die prozedurale Generierung von Items mit zufälligen Affixen (Prefix/Suffix), die auf einem Budget-System basiert und von Materialien beeinflusst wird, ist nicht abgedeckt und stellt eine große neue Anforderung dar.
✅ Abgedeckte Aspekte (Grundlagen)
Die fundamentalen Bausteine, auf denen dieses erweiterte System aufbauen würde, sind in den bestehenden Tasks von Milestone M3 geplant:
Item-Datenmodell mit Mods und Raritäten:
TASK-M3-02 (Items-Datenmodell) definiert die Kernstruktur von Items. Die Notes erwähnen explizit Felder wie id, name, type, rarity und mods (z.B. +ATK, resist.fire). Dies deckt die Basis-Anforderung ab, dass Items feste oder variable Eigenschaften haben können.
Raritäten (common, rare, epic):
TASK-M3-02 führt das rarity-Feld ein.
TASK-M3-15 (Loot-Rarity & Farbkonvention) behandelt die visuelle Repräsentation dieser Raritäten.
Loot-Tabellen als Quelle:
TASK-M3-08 (Loot-Tabellen) implementiert das System, das bestimmt, welches Basis-Item überhaupt droppt. Das hier beschriebene Itemization-System würde nachgelagert auf den Output dieser Tabellen angewendet werden.
❌ Lücken und fehlende Tasks
Das Dokument beschreibt ein komplexes System zur dynamischen Item-Erstellung zur Laufzeit. Die aktuelle Task-Planung in M3 geht von statisch definierten Items aus, die in data/items.json vollständig beschrieben sind. Die folgenden Konzepte sind neu und nicht abgedeckt:
Prozeduraler Affix-Generator:
Lücke: Dies ist die größte Lücke. Es gibt keine Task, die einen "Item-Generator" implementiert, der zur Laufzeit ein Basis-Item nimmt, eine Rarität auswürfelt und dann basierend auf einem "Budget" zufällige Affixe (Prefixe/Suffixe) aus data/affixes.json hinzufügt. Das aktuelle System würde nur ein Item mit fest definierten Mods laden, wie z.B. "mods": {"atk": 1}.
Datenstrukturen für Affixe (data/affixes.json):
Lücke: Es gibt keine Task, die das Erstellen, Validieren und Laden von Affix-Definitionen aus einer separaten Datei beschreibt. TASK-M3-01 plant Schemas für items.json, aber nicht für affixes.json.
Material-System & Tiers:
Lücke: Das Konzept, dass das Material eines Items (Eisen vs. Valorite) dessen Basis-Werte und mögliche Affixe beeinflusst, ist eine neue und komplexe Anforderung. Es gibt keine Task, die ein solches Material-System oder dessen Integration in die Item-Generierung oder das Crafting beschreibt.
Uniques & Sets (data/uniques.json):
Lücke: Während man "Unique"-Items als statische Einträge in items.json definieren könnte, beschreibt das Dokument ein dediziertes System (uniques.json), das auf Basis-Items aufbaut. Dies ist eine spezielle Form der Item-Generierung, die nicht geplant ist. Set-Boni sind ebenfalls ein komplett neues Feature.
Qualitäts-Modifikatoren (quality_mod):
Lücke: Das Konzept, dass Items eine "Qualität" (worn, fine, masterwork) haben, die ihre Stats beeinflusst, ist nicht Teil der aktuellen Planung in TASK-M3-02.
Fazit
Das ITEMIZATION_DESIGN.md beschreibt im Wesentlichen ein "Diablo-style" oder "ARPG-style" Lootsystem, während die aktuelle Task-Planung für Milestone M3 ein klassischeres, statisches RPG-Lootsystem (wie in vielen JRPGs oder älteren CRPGs) implementiert.
Die aktuelle M3-Planung erlaubt es, ein Item wie "Schwert des Bären" mit festem +5 STR zu erstellen.
Das Design-Dokument beschreibt ein System, das ein "Schwert" generieren kann, das dann zufällig den Prefix "Keen" (+1-3 ATK) und das Suffix "of Guarding" (+2-6% Parry) erhält.
Um die Vision dieses Dokuments vollständig umzusetzen, wäre ein neuer, umfangreicher Milestone (vermutlich nach M4) erforderlich, der sich ausschließlich der prozeduralen Item-Generierung widmet. Die wichtigsten neuen Tasks wären:
Implementierung des Affix-Generators (Budget-System, Prefix/Suffix-Logik).
Erstellung und Laden von data/affixes.json.
Implementierung des Material- und Qualitätssystems.
Integration dieses Generators in das Loot-System (TASK-M3-08) und das Crafting-System (TASK-M4-02).
Die aktuelle Task-Planung deckt diese fortgeschrittenen Features nicht ab.
