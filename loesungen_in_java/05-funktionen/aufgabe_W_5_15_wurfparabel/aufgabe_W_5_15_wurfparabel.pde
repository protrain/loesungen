// Deklaration der Konstanten g für die Fallbeschleunigung
float g = 9.81;

// Funktion zum Zeichnen der Koordinaten der Wurfparabel für
// Anfangsgeschwindigkeit v0 und -winkel beta, die als
// Fließkommazahl an die Funktion übergeben werden. Da die
// Funktion das Berechnen und Zeichnen übernimmt, hat sie
// keinen Rückgabewert.
void drawTrajectory(float v0, float beta) {
  // Umwandlung von Grad in Radians
  beta = radians(beta);

  // Berechne und zeichne in einer Skalierung von 0.25
  for (float t = 0.0; t < 20.0; t = t + 0.25) {
    // Startpunkt für Zeichnung ist Fensterhöhe = unterer Rand
    int yStart = height;

    // Berechne Werte für x und y
    float x = v0 * t * cos(beta);
    float y = v0 * t * sin(beta) - (g / 2) * t * t;

    // Zeichne Parabelpunkte
    // y muss horizontal gedreht werden (s. Hinweise)
    ellipse(x, -y + yStart, 2, 2);
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(400, 400);
  stroke(255, 0, 0);
  fill(255, 0, 0);
  background(0, 0, 0);
  drawTrajectory(60, 45);
}

