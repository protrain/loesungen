// Funktion zum Heraustrennen eines Teilbereichs aus
// einem Array. An die Funktion wird ein zweidimensionales
// Array sowie Ausschnitthöhe und -weite übergeben
boolean[][] extractCenter(boolean[][] in, int w, int h) {
  // Startreihe im Array
  // Gehe von Mitte h/2-Schritte zurück
  int startRow = ( in.length - h) / 2;

  // Startspalte im Array
  // Gehe von Mitte w/2-Schritte zurück
  int startColumn = ( in[0].length - w) / 2;

  // Generiere Ausgabe-Array
  boolean[][] out = new boolean[h][w];

  // Gehe jedes Element im Ziel-Array durch
  for (int y = 0; y < h; y++) {
    // pro Zeile
    for (int x = 0; x < w; x++) {
      // pro Spalte
      // kopiere Elemente aus Quellbereich
      out[y][x] = in[startRow + y][startColumn + x];
    }
  }

  // Gebe Bildausschnitt zurück
  return out;
}

// Funktion zur grafischen Darstellung eines
// zweidimensionalen Arrays, welches an die
// Funktion übergeben wird
void displayArray(boolean[][] input) {
  // Höhe und Breite des Arrays bestimmen
  int iWidth = input[0].length;
  int iHeight = input.length;

  // Größe pro Rechteck, abhängig vom Bildschirmfenster
  int xSize = width / iWidth;
  int ySize = height / iHeight;

  // Gehe jede Zeile und Spalte durch
  for (int y = 0; y < iHeight; y++) {
    for (int x = 0; x < iWidth; x++) {
      // Bestimme Farbe
      // true = setze Farbe auf Weiß
      if (input[y][x] == true)
        fill(255);
      // Sonst setze Farbe auf Grau
      else
        fill(125);
       
      // Male Kasten auf Bildschirm
      rect(x * xSize, y * ySize, xSize, ySize);
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(800, 800);

  boolean[][] bwImage =
    {
      {false, false, false, true,  true},
      {false, false, false, true,  true},
      {false, false, false, true,  true},
      {true,  true,  false, false, false},
      {true,  false, false, false, true},
      {false, false, false, true,  true}
    };

  //displayArray(bwImage);
  displayArray(extractCenter(bwImage, 3, 2));
}

