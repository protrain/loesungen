// Funktion, die ein zweidimensionales rechteckiges
// boolean-Array um 90 Grad nach links dreht. An die
// Funktion wird das zu bearbeitende Array übergeben.
// Zum Schluss gibt die Funktion das gedrehte Array
// zurück.
boolean[][] negativeRotation(boolean[][] bwImage) {
  // Neues Array anlegen (Höhe und Breite vertauscht)
  boolean[][] rotatedImage = new boolean[bwImage[0].length][bwImage.length];

  // Gehe jedes Element durch
  // Zunächst in der Zeile
  for (int i = 0; i < bwImage.length; i++) {
    // dann in der Spalte
    for (int j = 0; j < bwImage[i].length; j++) {
      // Kopiere Quellinhalt der Zelle [i,j]
      // an die gedrehte Position
      rotatedImage[bwImage[i].length - 1 - j][i] = bwImage[i][j];
    }
  }

  return rotatedImage;
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
      // true = Setze Farbe auf Weiß
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
  displayArray(negativeRotation(bwImage));
}

