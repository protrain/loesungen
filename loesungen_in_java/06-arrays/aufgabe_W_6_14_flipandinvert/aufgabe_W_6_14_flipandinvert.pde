// Funktion zum Umdrehen und Invertieren eines zwei-
// dimensionalen Arrays. An die Funktion wird das zu
// bearbeitende Array übergeben. Die Funktion selbst
// gibt das fertig bearbeitete Array zurück
boolean[][] flipAndInvert(boolean[][] in) {
  // Ausgabe-Array mit gleicher Größe
  boolean[][] out = new boolean[in.length][in[0].length];

  // Gehe jede Zeile und Spalte durch
  for (int i = 0; i < in.length; i++) {
    for (int j = 0; j < in[0].length; j++) {
      // Oben wird unten hingeschrieben und umgekehrt
      // Der Inhalt wird invertiert
      out[in.length - 1 - i][j] = ! in[i][j];
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
  displayArray(flipAndInvert(bwImage));
}

