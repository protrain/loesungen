// Funktion zur Ermittlung der minimalen Distanz
// zwischen zweier Punkte. An die Funktion wird ein
// zweidimensionales Array mit Koordinaten übergeben.
// Als Ergebnis liefert die Funktion ein eindimensionales
// Array mit der Angabe der Indizes der kleinsten Distanz.
int[] minDistance(int[][] c) {
  // Ergebnis-Array für zwei Elemente initialisieren
  int[] result = new int[2];

  // Minimale Distanz soll hier am Ende stehen
  float minD = sqrt(pow(c[0][0] - c[1][0], 2) + pow(c[0][1] - c[1][1], 2));

  // Gehe jede Spalte durch (Referenzpunkt)
  for (int i = 0; i < c.length - 1; i++) {
    // Gehe jede Spalte durch ab dem Referenzpunkt (Vergleichspunkt)
    for (int j = i + 1; j < c.length; j++) {
      // Berechne Distanz dieser Spalte
      float d = sqrt(pow(c[i][0] - c[j][0], 2) + pow(c[i][1] - c[j][1], 2));

      // Wenn kleiner als aktuell minimale Distanz, dann übernehmen
      if (d < minD) {
        // Speichere Distanz
        minD = d;

        // Speichere Referenzpunkt
        result[0] = i;

        // Speichere Vergleichspunkt
        result[1] = j;
      }
    }
  }

  return result;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  int[][] c =
    {
      {  3,   7},
      { 30,  80},
      { 80, 320},
      { 15, 276},
      { 84, 298},
      { 19,  29},
      {200, 200},
      {191, 919}
    };

  println(minDistance(c));
}

