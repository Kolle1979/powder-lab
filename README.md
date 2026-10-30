# Powder Lab

Browserbasierte 2D-Falling-Sand-Sandbox. Spielstand dieses Branches: **v1.2.0**.

[Spiel öffnen](https://kolle1979.github.io/powder-lab/) · [Quellcode](index.html) · [Änderungen](CHANGELOG.md)

Der öffentliche Link zeigt den zuletzt erfolgreich aus main bereitgestellten Stand. Ein Commit im Entwicklungsbranch allein aktualisiert die Website noch nicht. Für Spieler ist nach Bereitstellung keine Anmeldung erforderlich.

## Starten
Spiel-Link öffnen oder index.html herunterladen und lokal im Browser öffnen. Kein Build, keine Installation und keine externen Laufzeitbibliotheken notwendig.

## Bedienung
- Malen wählen: Linksklick, Finger oder Stift setzen das gewählte Element.
- Radieren wählen: Linksklick, Finger oder Stift löschen.
- Rechtsklick löscht immer, unabhängig vom gewählten Werkzeug.
- Halten und Ziehen zeichnet bzw. radiert. Mausrad oder Regler ändern die Pinselgröße.
- 1–9: Sand, Wasser, Stein, Holz, Feuer, Lava, Öl, Säure, Bombe.
- Pause / Leertaste stoppt die Physik; Malen und Radieren bleiben möglich.
- Leeren entfernt alle Zellen. Welt zurücksetzen erzeugt eine leere Welt mit Rand.

## Neu in 1.2.0
Einheitlicher Malen-/Radieren-Schalter für Maus und Touch, sichtbarer Werkzeugstatus und größere, gegliederte Kurzanleitung unter Sonstiges. Seitenleistenbreite, Farben, Elementgruppen, Physik und Rendering bleiben erhalten.

18 auswählbare Materialien; Physik mit 320 × 180 Zellen, Darstellung auf 1280 × 720 Pixel, passend zum Browserfenster skaliert. Vereinfachte Spielphysik, keine wissenschaftliche Simulation und keine garantierten 60 FPS.

## Prüfstatus
Die Entwicklung prüfte die korrigierte Fassung zuvor mit 29 Checks; der beigefügte kompakte Chromium-Test wurde vor diesem Commit mit 17 bestandenen Prüfungen ausgeführt. Dazu zählen Engine-Vergleich, Maus-Radieren, Touch, Bedienung und Layout. Der Nutzer bestätigte den lokalen Maustest der neuen Fassung. Echtes iOS/Safari für 1.2.0 ist noch zu prüfen. Für 1.1.0 meldete der Nutzer erfolgreiche Tests in Edge, Firefox und iOS Safari. Keine umfassende Browserfreigabe.

Nur für Entwicklung:
```sh
python -m pip install playwright
python -m playwright install chromium
python tests/test_v120.py
```

## Dokumentation
- [Originaler Startprompt](docs/STARTPROMPT.md): Anforderungen, keine Erfüllungsgarantie.
- [Architektur der unveränderten 1.1.0-Engine](docs/ARCHITEKTUR.md). Die dort beschriebene alte Eingabe wurde durch die oben erklärte 1.2.0-Bedienung ergänzt.
- [Elemente und Experimente](docs/ELEMENTE.md).
- [Ursprünglicher Testplan](docs/TESTS.md); aktuelle ausführbare Checks: tests/test_v120.py.
- [Roadmap](docs/ROADMAP.md): historischer Plan; die Touch-Funktionen sind in diesem Branch jetzt umgesetzt.
- [Beiträge](CONTRIBUTING.md) und [KI-Arbeitsregeln](AGENTS.md).

## Veröffentlichung und Rückweg
Pages-Einstellungen bleiben main und / (root). Nach geprüfter Übernahme dieses Branches nach main und erfolgreicher Bereitstellung liefert derselbe Spiel-Link 1.2.0. Kein neuer Link und keine Versionsauswahl nötig.

Der vorherige vollständige Stand ist im Branch release/1.1.0 gesichert. Bei Problemen kann dessen index.html mit einem neuen Commit nach main zurückgespielt werden. Kein Force-Push erforderlich. Sicherungsbranch ist kein Release-Tag.

## Herkunft und Lizenz
KI-gestützt aus einem Nutzerbriefing entwickelt. Powder Game und Powder Box: All Ages wurden als Inspiration genannt; keine offizielle Verbindung. Die Codeanalyse betrifft nur dieses Projekt. [MIT-Lizenz](LICENSE). Keine Zugangsdaten oder privaten Chatverläufe veröffentlichen.
