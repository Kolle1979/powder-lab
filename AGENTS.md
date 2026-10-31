# Regeln für KI-gestützte Arbeit

- Vor Änderungen README.md, docs/ARCHITEKTUR.md, docs/TESTS.md und CHANGELOG.md lesen.
- Dokumentation und tatsächlichen Code unterscheiden. STARTPROMPT.md archiviert Anforderungen, nicht garantierte Funktionen.
- index.html bleibt selbstständig: kein notwendiger Build, keine CDN-Abhängigkeiten, kein Login und kein Backend zum Spielen.
- Bewährte dunkle Desktop-GUI, Elementgruppen und Steuerung nicht ohne Auftrag umbauen.
- Kleine, gezielte Änderungen; keine unnötige Komplettneuschreibung.
- put/swapCells/wake, Tick-Markierungen, Lebensdauer und Zähler konsistent halten.
- Keine Zugangsdaten oder privaten Chat-Inhalte committen.
- Änderungen an Spiel-Logik, UI, Versionierung und Deployment ausdrücklich benennen.
- Nur tatsächlich ausgeführte Tests als bestanden melden; Umgebung und Grenzen nennen.
- Vor Spielveröffentlichung Changelog und Version abgleichen, geprüften Stand sichern und Live-Seite kontrollieren.
- Geplante v1.2.0-Touch-Funktionen nicht stillschweigend in v1.1.0 einbauen.

## Verbindlicher Test-vor-Freigabe-Ablauf
- Jede Weiterentwicklung zuerst lokal und automatisiert prüfen, dann ausschließlich als Testfassung bereitstellen.
- Offizielle Spielfassung: /index.html. Öffentlich spielbare Testfassung: /test/index.html. Beide bleiben eigenständig.
- Pages verwendet main / (root). Ein neuer Entwicklungsbranch erzeugt allein keine Test-Webadresse. Zum Veröffentlichen einer Vorschau nur Testdateien und zugehörige Dokumentation/Tests nach main übernehmen; offizielle index.html nicht ändern.
- Nutzer testet die Test-Webadresse am PC und auf dem echten iPhone/iPad. Simuliertes Touch ist kein echter iOS-Nachweis. Ausstehende Prüfungen offen nennen.
- Eine Zustimmung zur Testveröffentlichung ist keine Freigabe für die offizielle Website. Erst nach ausdrücklicher Freigabe des getesteten Standes die offizielle Startdatei aktualisieren.
- Änderungen nach dem Nutzertest erfordern erneute Prüfung und gegebenenfalls eine neue Testfassung; keinen ungetesteten Zusatzcode bei der Übernahme einbauen.
- Vor offizieller Übernahme Rückweg sichern, Änderungen per Pull Request prüfen und nach Deployment den bisherigen Hauptlink kontrollieren.
- Version/Commit und tatsächlich ausgeführte Tests dokumentieren. Eine Testfassung bekommt eine eigene rc-Versionsnummer.
- Details und aktuelle Vorschau: docs/RELEASE_WORKFLOW.md.
