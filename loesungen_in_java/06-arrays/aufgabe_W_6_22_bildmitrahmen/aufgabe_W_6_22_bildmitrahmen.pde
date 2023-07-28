// Funktion zum Hinzufügen einer schwarzen Umrandung um ein Array.
// An die Funktion wird das zweidimensionale Quell-Array sowie die
// Zielgröße inkl. Rahmen übergeben. Die Funktion gibt das neu berechnete
// Array zurück.
boolean[][] addFrame(boolean[][] in, int width) {
  boolean[][] out
    = new boolean[in.length + 2 * width][in[0].length + 2 * width];

  // Setze zunächst alle Array-Werte auf false
  // Damit wird das Array komplett "eingeschwärzt"
  for (int x = 0; x < out.length; x++) {
    for (int y = 0; y < out[0].length; y++) {
      out[x][y] = false;
    }
  }

  // Kopiere die Array-Werte vom Quell-Array herüber in das
  // größere Array, beginnend ab Rand
  for (int x = 0; x < in.length; x++) {
    for (int y = 0; y < in[0].length; y++) {
      out[x + width][y + width] = in[x][y];
    }
  }

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
    {true,  false, true},
    {false, false, true},
    {true,  false, false},
    {false, false, true}
  };

  //displayArray(bwImage);
  displayArray(addFrame(bwImage, 1));
}

