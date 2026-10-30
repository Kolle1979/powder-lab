# Codeanalyse / Reverse Engineering von v1.1.0

Referenz: `index.html`, Erstveröffentlichungs-Commit `47356ae9c8a54a4a22c317d224caca57778db327`. Dokumentation des eigenen verfügbaren Quellcodes, kein Reverse Engineering fremder Spiele. Die Abschnitte sind logisch getrennt, aber keine importierten JavaScript-Module.

## Datenfluss
Pointer-Ereignis → `paint` / `paintLine` → `put` → Aktivierung benachbarter Chunks → `simulate` → `updateCell` → `react` / Bewegung → `render` → Canvas.

## Welt und Speicher
`W=320`, `H=180`, also 57.600 Physikzellen. Zellindex: `y*W+x`.

| Array | Typ | Zweck |
|---|---|---|
| cells | Uint8Array | Material-ID pro Zelle |
| life | Uint16Array | Verbleibende Lebensdauer in Simulationsschritten |
| heat | Float32Array | Vereinfachter thermischer Zustand |
| updated | Uint32Array | Zuletzt verarbeiteter Tick |
| active / nextActive | Uint8Array | Aktive Chunk-Karten |
| explodeQueue | Int32Array | Positionen vorgemerkter Explosionen |
| explodeRadius | Uint8Array | Zugehörige Explosionsradien |

`put` setzt Material, Lebensdauer, Wärme und Tick-Markierung; es aktualisiert den Partikelzähler und weckt Chunks. `swapCells` tauscht Material samt Lebensdauer/Wärme und markiert beide Positionen als bearbeitet. Außerhalb der Welt liefert `get` eine virtuelle Wand.

## Aktivität und Reihenfolge
16 × 16 Zellen pro Chunk, 20 Spalten × 12 Reihen. `wake` aktiviert bis zu neun benachbarte Chunks. In `simulate` werden die zwei Karten getauscht und die neue Zielkarte geleert. Inaktive Chunks werden nicht physikalisch aktualisiert. Scan von unten nach oben; horizontale Richtung wechselt. Tick-Markierungen begrenzen die erneute Verarbeitung bewegter Partikel.

Ruhender Sand kann einschlafen. Flüssigkeiten, Gase, Erde, Pflanzen und thermisch aktive Zellen halten Bereiche weiter aktiv. Das ist keine perfekte Erkennung sämtlicher ruhender Zustände.

## Materialregeln
Definitionen enthalten Zustand, Dichte, Brennbarkeit, Leitfähigkeit und Schmelzpunkt. `move` erlaubt leere Zielzellen, Gasverdrängung und bestimmte dichteabhängige Flüssigkeitstausche. Pulver fällt nach unten, dann diagonal. Flüssigkeiten prüfen unten, diagonale Ziele und zusammenhängende horizontale Luftwege bis vier Zellen. Lava bewegt sich nur jeden vierten Tick.

`react` behandelt Kontaktreaktionen; Wasser/Lava-Abkühlung hat Vorrang vor allgemeiner Erwärmung. `thermal` verteilt Wärme lokal und vereinfacht die Abkühlung. Metall kann bei hoher Wärme zu Lava werden. Pflanzen entstehen probabilistisch an feuchter Erde und wachsen von Erde/Pflanzen aus nach oben.

## Explosionen
Bombe: Radius 13 Zellen; Schießpulver: Radius 5. Zündung stellt eine Explosion in die Warteschlange. Pro Simulationsschritt werden höchstens acht Explosionen abgearbeitet. Kreisflächen werden mit Feuer/Rauch überschrieben, Wand bleibt erhalten. Kurze radiale Partikelverschiebungen approximieren Druck. Kein kontinuierliches Druck- oder Geschwindigkeitsfeld. Explosionsschäden besitzen keine vollständige Sichtlinienabschirmung hinter Wänden.

## Darstellung und Timing
Ein ImageData-Puffer mit 320 × 180 Pixeln wird vollständig neu gefüllt. Zwischen-Canvas → `drawImage` auf 1280 × 720 Pixel; Glättung ist deaktiviert. CSS passt die Anzeige im Seitenverhältnis 16:9 an. Die Physik arbeitet chunkbasiert, das Rendering verwendet keine Dirty Rectangles.

`requestAnimationFrame` ruft die Hauptschleife auf. Ein Akkumulator erzeugt Schritte mit 1000/60 ms; Geschwindigkeitsregler 10–300 %. Höchstens sechs Schritte pro Bild, Begrenzung langer Rückstände. Die FPS-Anzeige misst Browser-Frames, nicht unmittelbar die Physik-Tickrate. Es gibt keine Partikelobjekt-Allokation pro Zelle, aber beispielsweise regelmäßig neu erzeugte HUD-Strings; vollständig allokationsfrei ist die Schleife nicht.

## Eingabe
Pointer-Koordinaten werden über die tatsächliche Canvas-Anzeige auf Zellen abgebildet. Pointer-Capture und Linieninterpolation verbinden schnelle Pinselbewegungen. Halten sprüht auch ohne Mausbewegung. Rechtsklick löscht, Tastatur wählt Elemente. Fokusverlust beendet das Zeichnen. Pausieren stoppt Physik, nicht Malen.

## Abweichungen vom Briefing
- 1280 × 720 Darstellung, nicht 1280 × 720 unabhängige Physikzellen.
- Dichtebasiertes Sinken statt einer vollständigen hydrodynamischen Sandverdrängung.
- Glas ist durchscheinend eingefärbt, ohne echte mehrschichtige Transparenz.
- Schmelzpunkte sind definiert, werden jedoch nicht für jedes Material als Phasenübergang ausgewertet. Wärme ist nicht wissenschaftlich kalibriert.
- Kein wissenschaftliches Strömungs-/Druckmodell; Explosionen können hinter Wänden Schäden erzeugen, obwohl Wände selbst bestehen bleiben.
- Keine Speichern/Laden-Funktion, keine garantierten 60 FPS und kein eigener Touch-Radiermodus.
- Oberfläche skaliert; echte Geräte-/Safari-Kompatibilität muss zusätzlich geprüft werden.

## Sichere Änderungen
`put`, `swapCells`, `wake`, Lebensdauer und Tick-Markierungen gemeinsam betrachten. UI und Dateiformat erhalten. Dokumentation darf Implementierungswünsche nicht als vorhandene Funktionen darstellen.
