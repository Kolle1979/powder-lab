# Powder Lab

Browserbasierte 2D-Falling-Sand-Sandbox. Aktueller Spielstand: **v1.1.0**.

[Spiel öffnen](https://kolle1979.github.io/powder-lab/) · [Quellcode](index.html) · [Änderungen](CHANGELOG.md)

Der Spiel-Link setzt eine erfolgreich aktivierte GitHub-Pages-Bereitstellung voraus. Diese Dokumentation bestätigt keinen Deployment-Status. Nach der Bereitstellung ist für Spieler kein GitHub-Konto erforderlich.

## Starten
Online den Spiel-Link öffnen oder `index.html` herunterladen und lokal im Browser öffnen. Keine Installation, kein Build und keine externen Bibliotheken notwendig.

## Bedienung
| Eingabe | Aktion |
|---|---|
| Linke Maustaste halten | Gewähltes Element platzieren |
| Rechte Maustaste | Löschen, auch Wände |
| Mausrad / Größenregler | Pinselgröße ändern |
| 1–9 | Sand, Wasser, Stein, Holz, Feuer, Lava, Öl, Säure, Bombe |
| Leertaste / Pause | Simulation anhalten oder fortsetzen |
| Leeren | Alle Zellen entfernen |
| Welt zurücksetzen | Leere Welt mit festem Rand herstellen |

Pausiert kann weiter gemalt werden. Platzieren ersetzt keine bestehenden Festkörper; zum Umbauen vorher radieren.

## Funktionen und Grenzen
18 auswählbare Materialien, Wärmeleitung, vereinfachte Explosionen, Pflanzenwachstum, Geschwindigkeitsregler und FPS-Anzeige. Physik: 320 × 180 Zellen, Darstellung: 1280 × 720 Pixel, passend zum Browserfenster skaliert. Spielphysik, keine wissenschaftliche Simulation. 60 FPS sind ein Ziel, keine Hardware-Garantie.

Windows-Desktop-Browser sind der bisherige Schwerpunkt. Die Entwicklung meldete Tests in Chromium. Eine umfassende Windows-/Safari-/iOS-Freigabe liegt nicht vor. Touch besitzt in v1.1.0 keinen eigenen Radier-Schalter; Verbesserungen sind für v1.2.0 vorgesehen.

## Dokumentation
- [Originaler Startprompt](docs/STARTPROMPT.md): ursprüngliche Anforderungen, nicht Erfüllungsgarantie.
- [Codeanalyse / Reverse Engineering](docs/ARCHITEKTUR.md): Aufbau der eigenen Implementierung.
- [Elemente und Experimente](docs/ELEMENTE.md).
- [Testplan und Prüfstatus](docs/TESTS.md).
- [Weiterentwicklung](docs/ROADMAP.md).
- [Beiträge](CONTRIBUTING.md) und [Regeln für KI-gestützte Änderungen](AGENTS.md).

## Veröffentlichung
GitHub Pages: Settings → Pages → Deploy from a branch → `main` → `/ (root)`. Spieladresse: https://kolle1979.github.io/powder-lab/ . Für die Konfiguration muss der Besitzer angemeldet sein; Spieler brauchen keine Anmeldung. Änderungen an der Spiel-Datei erst nach Prüfung übernehmen.

## Herkunft und Lizenz
Dieses Projekt wurde KI-gestützt aus einem Nutzerbriefing entwickelt und iterativ korrigiert. Powder Game und Powder Box: All Ages wurden im Briefing als Inspiration genannt. Keine offizielle Verbindung zu diesen Spielen; die Codeanalyse erklärt ausschließlich dieses Projekt.

[MIT-Lizenz](LICENSE). Keine Zugangsdaten, privaten Chatverläufe oder persönlichen Daten in Beiträge aufnehmen.
