// Funktion zur Berechnung der angegebenen Reflexion
// An die Funktion wird das zu bearbeitende zwei-
// dimensionale Array übergeben. Das gespiegelte
// Ergebnis wird zurückgegeben
boolean[][] reflection(boolean[][] input) {
  // Höhe des Eingabe-Arrays
  int iHeight = input.length;

  // Kopie anlegen (ein Drittel größer)
  boolean[][] output = new boolean[iHeight + iHeight / 3][input[0].length];

  // Kopiere input in output:
  // Gehe alle Zeilen durch
  for (int y = 0; y < input.length; y++) {
    // Gehe alle Spalten durch
    for (int x = 0; x < input[0].length; x++) {
      // Kopiere Inhalt
      output[y][x] = input[y][x];
    }
  }

  // Gehe Rückwärts das letzte Drittel des Arrays durch
  int y = input.length;
  for (int i = 0; i < iHeight / 3; i++) {
    // Füge Zeile dem Array hinzu
    output[y] = input[iHeight - 1 - i];
    y = y + 1;
  }

  // Rückgabe
  return output;
}

// Funktion zur grafischen Darstellung eines zweidimensionalen
// Arrays
void displayArray(boolean[][] input) {
  // Höhe und Breite des Arrays bestimmen
  int iWidth = input[0].length;
  int iHeight = input.length;

  // Größe pro Rechteck, abhängig vom Bildschirmfenster
  int xSize = width / iWidth;
  int ySize = height / iHeight;

  // Gehe jede Zeile durch
  for (int y = 0; y < iHeight; y++) {
    // gehe jede Spalte durch
    for (int x = 0; x < iWidth; x++) {
      // Bestimme Farbe
      if (input[y][x] == true) {
        // true = Setze Farbe auf Weiß
        fill(255);
      }
      else {
        // Sonst setze Farbe auf Grau
        fill(125);
      }
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
  displayArray(reflection(bwImage));
}

