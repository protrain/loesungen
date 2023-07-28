// Funktion zum Zeichnen von Kreisausschnitten. Die
// Anzahl an Kreisen(= Spalten) wird als ganzzahliger
// Wert an die Funktion übergeben.
void drawArcs(int numArcsPerRow) {
  // Setze Radius für jeden Kreis,
  // nutze dabei gegebenen Platz bestmöglich aus.
  int radius = 0;

  // Den kleineren Wert des Ausgabebereichs bestimmen
  // und für diesen den Radius bestimmen.
  if (width > height) {
    radius = height / numArcsPerRow;
  }
  else {
    radius = width / numArcsPerRow;
  }

  // Winkelschritt pro Kreis (360 Grad entspricht 2*PI)
  float winkelStep = 2 * PI / (numArcsPerRow * numArcsPerRow);
  float winkel = 0; // Startwert

  // Durchlaufe nun alle Zeilen
  for (int y = 0; y < numArcsPerRow; y++) {
    // und pro Zeile für alle Spalten
    for (int x = 0; x < numArcsPerRow; x++) {
      // Setze zufällige Farbe
      int colorR = int(random(0, 255));
      int colorG = int(random(0, 255));
      int colorB = int(random(0, 255));
      fill(colorR, colorG, colorB);
      stroke(colorR, colorG, colorB);

      // Erhöhe Kreiswinkel um Winkelschritt
      winkel = winkel + winkelStep;

      // Zeichne Kreis
      arc(
        radius * x + (radius / 2),
        radius * y + (radius / 2),
        radius,
        radius,
        0,
        winkel
      );
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(600, 600);
  background(255, 255, 255);

  drawArcs(16);
}

