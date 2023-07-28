// Funktion zum Erzeugen eines Schlagschattens in einem
// zweidimensionalen Array, welches an die Funktion
// übergeben wird. Als Ergebnis liefert die Funktion
// das Array mit dem erzeugten Schatten zurück
boolean[][] addShadow(boolean[][] in) {
  // Vergrößere Ausgabebild um jeweils einen Pixel
  // nach rechts und unten
  boolean[][] t = new boolean[in.length + 1][in[0].length + 1];

  // Kopiere alle Elemente des Eingabe-Arrays.
  // Durchlaufe das Array für jede Zeile
  for (int i = 0; i < in.length; i++) {
    // und jede Spalte
    for (int j = 0; j < in[i].length; j++) {
      // kopiere Inhalt
      t[i][j] = in[i][j];
    }
  }

  // Letzte Zeile: unten links auf Weiß
  t[t.length - 1][0] = true;

  // Setze den Rest der letzten Zeile auf Schwarz
  for (int i = 1; i < t[t.length - 1].length; i++) {
    t[t.length - 1][i] = false;
  }

  // Letzte Spalte: oben rechts auf Weiß
  t[0][t[0].length - 1] = true;

  // Setze den Rest der letzten Spalte auf Schwarz
  for (int i = 1; i < t.length - 1; i++) {
    t[i][t[i].length - 1] = false;
  }

  return t;
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
      // True = Setze Farbe auf Weiß
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
      {false, true,  true},
      {true,  false, true},
      {true,  true,  false},
      {true,  false, true}
    };

  //displayArray(bwImage);
  displayArray(addShadow(bwImage));
}

