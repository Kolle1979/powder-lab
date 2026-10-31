# Powder Lab

Browserbasierte 2D-Falling-Sand-Sandbox. Spielstand: **v1.2.2**.

[Spiel öffnen](https://kolle1979.github.io/powder-lab/) · [Testseite](https://kolle1979.github.io/powder-lab/test/) · [Quellcode](index.html) · [Änderungen](CHANGELOG.md)

Der Hauptlink zeigt den zuletzt erfolgreich aus main bereitgestellten Stand. Ein Commit allein ist kein Live-Deployment-Nachweis. Zum Spielen ist keine Anmeldung nötig. Die eigenständige index.html lässt sich auch lokal öffnen; kein Build und keine externen Laufzeitbibliotheken erforderlich.

## Bedienung
- Malen: Linksklick, Finger oder Stift setzen das gewählte Element.
- Radieren: Linksklick, Finger oder Stift löschen. Rechtsklick löscht immer.
- Halten/Ziehen zeichnet oder radiert. Mausrad oder Regler ändern die Pinselgröße.
- 1–9: Sand, Wasser, Stein, Holz, Feuer, Lava, Öl, Säure, Bombe.
- Pause / Leertaste stoppt Physik, nicht Malen/Radieren.
- Leeren entfernt alles; Zurücksetzen erzeugt eine leere Welt mit Rand.

## Neu in 1.2.2
Bombe ist statisch wie Stein. Feuer-/Lava-Kontakt zündet ohne Zufallsverzögerung. Zusammenhängende Bombenflächen und weitere Bomben im Explosionsradius werden in einem Simulationsschritt verarbeitet; entfernte außerhalb bleiben stehen. Keine verzögerten Bombenreste. Feuer und Rauch steigen danach normal auf; frisch nachgemalte Bomben können erneut zünden. Schießpulver bleibt fallendes Pulver mit bisheriger Warteschlange. Druck ist weiterhin vereinfacht.

Die offizielle Datei ist exakt die freigegebene Vorschau 1.2.2-rc.1, nur die Versionskennzeichnung wurde geändert. Oberfläche, Eingabe und Rendering bleiben erhalten. Seit 1.2.1 entfällt die untere Hinweiszeile; die linke Anleitung bleibt.

18 Materialien, 320 × 180 Physikzellen, Darstellung auf 1280 × 720 Pixel mit Fensteranpassung. Spielphysik, keine wissenschaftliche Simulation oder garantierten 60 FPS.

## Freigabe und Tests
Nutzer bestätigte am 31.10.2026 um 09:25 CET den erfolgreichen Test und erteilte die offizielle Freigabe. Geräte-/Browser-Versionen wurden dabei nicht genannt; keine allgemeine Kompatibilitätszusage.

Die Vorschau bestand 34 Chromium-Checks einschließlich deterministischem Vergleich ohne Bomben mit 1.2.1. Vor dem offiziellen Upload: exakter Vorschau/Release-Vergleich, Node.js-Syntaxprüfung und 21 bestandene Release-Checks. Kein CI- oder erfolgreicher Live-Deployment-Nachweis durch diesen Commit. Simuliertes Touch ist kein eigener echter iOS-Nachweis.

Nur für Entwicklung:
python -m pip install playwright
python -m playwright install chromium
python tests/test_v120.py
python tests/test_bombs.py

Der historische Dateiname test_v120.py prüft jetzt die offizielle 1.2.2. test_preview.py startet die aktuelle Bomben-Vorschauprüfung.

## Dokumentation
- [Startprompt](docs/STARTPROMPT.md): Anforderungen, keine Erfüllungsgarantie.
- [Architektur](docs/ARCHITEKTUR.md): historischer Engine-Stand; aktuelle Bombenänderung in [Bomben-Testhinweisen](docs/BOMB_FIX_1.2.2.md).
- [Elemente und Experimente](docs/ELEMENTE.md).
- [Testplan](docs/TESTS.md), [Freigabeprozess](docs/RELEASE_WORKFLOW.md), [KI-Regeln](AGENTS.md).
- [Roadmap](docs/ROADMAP.md): historischer Plan; [Beiträge](CONTRIBUTING.md).

## Einfacher Ablauf und Rückweg
Neue Änderungen lokal prüfen und Testdatei/Tests/Hinweise gemeinsam direkt nach main übernehmen; offizielle index.html bleibt bis zur ausdrücklichen Nutzerfreigabe unberührt. Keine zusätzlichen Branches ohne Absprache. Für diese freigegebene 1.2.2 erfolgt die offizielle Übernahme ebenfalls direkt auf main. Die Testseite bleibt separat bei 1.2.2-rc.1. Pages bleibt main / (root), der Hauptlink unverändert.

Rücksetzpunkt für 1.2.1: 5ecd1345bd35730a2644482f4a49c7578b82824a:index.html. Bei Problemen vorherige Datei per neuem Commit wiederherstellen, kein Force-Push. Ältere Versionsstände bleiben in der Historie und vorhandenen Branches erhalten; dieser Upload erstellt oder löscht keinen Branch und keinen Release-Tag.

## Herkunft und Lizenz
KI-gestützt aus einem Nutzerbriefing entwickelt, inspiriert von Powder Game und Powder Box: All Ages; keine offizielle Verbindung. Analyse betrifft eigenen Projektcode. [MIT-Lizenz](LICENSE). Keine Geheimnisse oder privaten Chatverläufe veröffentlichen.
