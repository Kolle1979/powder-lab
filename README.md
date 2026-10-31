# Powder Lab

Browserbasierte 2D-Falling-Sand-Sandbox. Spielstand dieses Branches: **v1.2.1**.

[Spiel öffnen](https://kolle1979.github.io/powder-lab/) · [Testseite](https://kolle1979.github.io/powder-lab/test/) · [Quellcode](index.html) · [Änderungen](CHANGELOG.md)

Der Hauptlink zeigt den zuletzt erfolgreich aus main bereitgestellten Stand. Ein Entwicklungscommit allein aktualisiert die Website nicht. Zum Spielen ist keine Anmeldung nötig.

## Starten und Bedienung
Spiel-Link öffnen oder index.html lokal im Browser öffnen. Kein Build und keine externen Laufzeitbibliotheken nötig.
- Malen: Linksklick, Finger oder Stift setzen das Element.
- Radieren: Linksklick, Finger oder Stift löschen. Rechtsklick löscht immer.
- Halten und Ziehen zeichnet bzw. radiert; Mausrad oder Regler ändern die Pinselgröße.
- 1–9: Sand, Wasser, Stein, Holz, Feuer, Lava, Öl, Säure, Bombe.
- Pause / Leertaste stoppt die Physik, nicht Malen/Radieren.
- Leeren entfernt alles; Welt zurücksetzen erzeugt eine leere Welt mit Rand.

## Neu in 1.2.1
Die untere Hinweiszeile an der Spielfläche entfällt. Die linke Kurzanleitung bleibt. Exakt die vom Nutzer freigegebene Testfassung 1.2.1-rc.1; nur die Versionskennzeichnung wurde für das Release geändert.

Seit 1.2.0: gemeinsamer Malen-/Radieren-Schalter für Maus und Touch, Werkzeugstatus und größere, gegliederte linke Anleitung. Physik, Rendering, Farben und Elementgruppen bleiben erhalten.

18 auswählbare Materialien, 320 × 180 Physikzellen, Darstellung auf 1280 × 720 Pixel mit Fensteranpassung. Vereinfachte Spielphysik; keine wissenschaftliche Simulation oder garantierten 60 FPS.

## Prüfstatus und Freigabe
Nutzer meldete am 31.10.2026 die Testfassung als vollständig getestet und gab die offizielle 1.2.1 frei. Einzelne Geräte- und Browser-Versionen wurden dabei nicht genannt; daraus wird keine allgemeine Kompatibilitätszusage abgeleitet.

Vor dem Release-Commit: Node.js-Syntaxprüfung und 29 bestandene Chromium-Checks (17 Release, 12 Vorschau). Der Dateivergleich prüft, dass sich Vorschau und Release nur in der Versionskennzeichnung unterscheiden. Browser-Touch-Prüfungen sind kein eigenständiger echter iOS-Nachweis. Kein CI- oder Live-Deployment-Nachweis durch diesen Commit.

Nur für Entwicklung:
```sh
python -m pip install playwright
python -m playwright install chromium
python tests/test_v120.py
python tests/test_preview.py
```
Der historische Dateiname test_v120.py bleibt bestehen; er prüft jetzt die offizielle 1.2.1.

## Dokumentation
- [Startprompt](docs/STARTPROMPT.md): Anforderungen, keine Erfüllungsgarantie.
- [Architektur](docs/ARCHITEKTUR.md): unveränderte Engine; alte Eingabebeschreibung durch die aktuelle Anleitung ergänzt.
- [Elemente und Experimente](docs/ELEMENTE.md).
- [Testplan](docs/TESTS.md) und [Test-/Freigabeprozess](docs/RELEASE_WORKFLOW.md).
- [Roadmap](docs/ROADMAP.md): historischer Plan; Touch ist inzwischen umgesetzt.
- [Beiträge](CONTRIBUTING.md) und [KI-Regeln](AGENTS.md).

## Veröffentlichung und Rückweg
Pages bleibt main / (root). Nach geprüftem Merge und erfolgreichem Deployment liefert derselbe Hauptlink 1.2.1. Die Testseite bleibt separat als 1.2.1-rc.1 erhalten. Jede Weiterentwicklung zuerst testen und erst nach Nutzerfreigabe offiziell übernehmen.

Rücksetzpunkt für die bisherige 1.2.0: Commit a73d7f4424519856836903bbb639ababeac9932f, Datei index.html. Deren Spielstand liegt auch im Branch version/1.2.0. Bei Problemen mit einem neuen Commit wiederherstellen, kein Force-Push. release/1.1.0 bleibt ebenfalls erhalten. Diese Branches sind keine Release-Tags.

## Herkunft und Lizenz
KI-gestützt aus einem Nutzerbriefing entwickelt. Powder Game und Powder Box: All Ages wurden als Inspiration genannt; keine offizielle Verbindung. Die Analyse betrifft eigenen Projektcode. [MIT-Lizenz](LICENSE). Keine Geheimnisse oder privaten Chatverläufe veröffentlichen.
