// Funktion zum Spiegeln eines Arrays.
// Erhält das ursprüngliche zweidimensionale Array
// und gibt das gespiegelte Array zurück.
boolean[][] mirror(boolean[][] input) {
  // Ausgabe-Array gespiegelt
  boolean[][] output = new boolean[input.length][input[0].length];

  // Gehe jede Zeile im Input-Array zeilenweise durch
  for (int y = 0; y < input.length; y++) {
    // Gehe jedes Element spaltenweise durch
    for (int x = 0; x < input[0].length; x++) {
      // Schreibe Elemente umgekehrt in den Array
      output[y][x] = input[y][input[0].length - x - 1];
    }
  }

  return output;
}

// Funktion zur grafischen Darstellung eines zweidimensionalen
// Arrays, welches als Eingabewert in die Funktion verwendet wird
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
      // True = Setze Farbe auf Schwarz
      if (input[y][x] == true)
        fill(0); 
      // Sonst setze Farbe auf Weiß
      else
        fill(255);
      
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
      {false, false, false, false},
      {false, true,  false, false},
      {false, true,  false, true}
    };

  //displayArray(bwImage);
  displayArray(mirror(bwImage));
}

