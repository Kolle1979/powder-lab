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
