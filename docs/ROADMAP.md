# Roadmap

## v1.1.0 – Ausgangsstand
- Spiel als eigenständige index.html im Repository.
- Startprompt, Architektur, Regeln und Grenzen dokumentieren.
- Pages-Aktivierung und Live-Aufruf separat bestätigen.
- Release-Tag und Release-Notizen noch erstellen; diese Dokumentation legt weder Tag noch Release an.

## v1.2.0 – nächste Spielversion, noch nicht implementiert
- Touch-Schalter Malen/Radieren.
- Bessere Bedienbarkeit auf iPhone/iPad und im Hochformat.
- Desktop-Oberfläche und bewährte Steuerung erhalten.
- Reproduzierbare Browser-Tests und echter Safari-/iOS-Test.

## Später, noch nicht zugesagt
- Welten speichern/laden.
- Versuchsvorlagen und Export.
- Gezielte Performance- und Physikverbesserungen anhand von Messungen.

## Veröffentlichungspolitik
main enthält den freigegebenen Stand. Spieländerungen zunächst in einem Feature-Branch mit Pull Request. Kleine Fehlerkorrekturen: 1.1.x; neue Funktionen wie Touch: 1.2.0. Reine Dokumentationsänderungen lassen die angezeigte Spielversion bei 1.1.0. Vor Freigabe Tests und Changelog aktualisieren; nach Freigabe Deployment kontrollieren. Einen geprüften Commit als Release markieren, damit ein Rückweg klar bleibt. Branch-Schutzregeln und CI sind Empfehlungen, hierdurch noch nicht eingerichtet.
