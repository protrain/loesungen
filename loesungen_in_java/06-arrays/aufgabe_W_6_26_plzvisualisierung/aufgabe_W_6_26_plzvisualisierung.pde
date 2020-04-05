// Anzahl der gespeicherten PLZ-Orte im Array
int placeCount = 0;

// Maximale Werte der x-und y-Koordinaten
float minX,
maxX;
float minY, maxY;

// Zeichenbereich-Abmessungen der Karte
float mapX1,
mapY1;
float mapX2, mapY2;

// Array, in dem wir die x- und y-Koordinaten
// speichern werden
float[] x;
float[] y;


void setup() {
  // Setze Fenstergröße
  size(380, 450);

  // Setze Zeichenbereich für die Karte:
  // Obere linke Ecke
  mapX1 = 30;
  mapY1 = 20;
  // Untere rechte Ecke
  mapX2 = width - mapX1;
  mapY2 = height - mapY1;

  // Lese die Koordinaten ein
  readData();
}

void draw() {
  // Setze schwarzen Hintergrund
  background(0);

  // Setze weiße Kreisfarbe
  stroke(255);
  fill(255);
  for (int i = 0; i < placeCount; i = i + 1) {
    // Setze x- und y-Koordinaten in Abhängigkeit vom
    // Zeichenbereich
    float xDraw = map(x[i], minX, maxX, mapX1, mapX2);
    float yDraw = map(y[i], minY, maxY, mapY2, mapY1);

    // Male Kreis
    ellipse(xDraw, yDraw, 1, 1);
  }
}

// Funktion, die die Postleitzahldaten und 2D-Koordinaten
// aus einer CSV-Datei einliest und in einem Array speichert
void readData() {
  // Lese die CSV-Datei ein
  String[] lines = loadStrings("zip_de_prep.csv");

  // Setze die Minimal- und Maximalwerte der Koordinaten in
  // der CSV-Datei
  minX = -0.056436524;
  maxX = 0.044636916;
  minY = 0.7982389;
  maxY = 0.9287888;

  // Jetzt lesen wir die x- und y-Koordinaten
  // aller Postleitzahlen ein
  x = new float[lines.length];
  y = new float[lines.length];
  for (int i = 0; i < lines.length; i = i + 1) {
    // Trenne die Werte bei jedem Tabulatorwert ab
    // und füge sie in einen Array ein
    String[] pieces = split(lines[i], TAB);

    // Haben wir Werte in der Zeile?
    if (pieces.length > 1) {
      // Dann lesen wir die Koordinaten ein, die
      // in der 2. und 3. Spalte der Zeile gespeichert
      // sind
      x[placeCount] = float(pieces[1]);
      y[placeCount] = float(pieces[2]);
    }

    // Erhöhe die Anzahl der gespeicherten Orte um 1
    placeCount = placeCount + 1;
  }
}
