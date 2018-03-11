// Funktion zum Vergrößern eines quadratisches Arrays um den Faktor f
// Eingabe ist ein zweidimensionales Array mit boolean-Werten sowie
// der Faktor, um den das Array vergrößert werden soll
boolean[][] magnify(boolean[][] input, int f) {
  // die aktuelle Größe entspricht der Anzahl an Array-Elementen
  // einer Dimension
  int inputSize = input.length;

  // Berechnen der Ergebnisgröße des Arrays
  int outputSize = f * inputSize;

  // Generiere leeren Output-Array in der neuen Größe
  boolean[][] output = new boolean[outputSize][outputSize];

  // Gehe jedes Element in Input durch und schreibe es in die skalierten
  // Felder im Output
  for (int y = 0; y < inputSize; y++) { // Iteration durch Zeilen
    for (int x = 0; x < inputSize; x++) { // Iteration durch Spalten
      for (int j = 0; j < f; j++) { // Iteration für den Zeilenfaktor
        for (int i = 0; i < f; i++) { // Iteration für den Spaltenfaktor
          output[x * f + j][y * f + i] = input[x][y]; // Schreiben des Werts
        }
      }
    }
  }

  return output;
}

// Funktion, die das Array grafisch im Ausgabefenster darstellt
// Als Eingabe erfolgt das Array.
void drawArray(boolean[][] input) {
  // Array-Größe. Da Array quadratisch sein soll, reicht die Höhe
  // des Arrays aus
  int inputSize = input.length;

  // Höhe und Breite jedes Rechtecks (definiert durch Fenstergröße)
  int rectWidth = width / inputSize;
  int rectHeight = height / inputSize;

  for (int y = 0; y < inputSize; y++) {
    for (int x = 0; x < inputSize; x++) {
      // Setze Farbe nach Array-Inhalt
      // Um einzelne Elemente sichtbar zu machen, ist die Linienfarbe
      // stets das Gegenteil der Füllfarbe
      if (input[y][x] == false) {
        stroke(0);
        fill(255);
      }
      else {
        stroke(255);
        fill(0);
      }
      // Zeichne Rechteck
      // startX,startY: Obere linke Ecke des Rechtecks
      // startX+rectWidth, startY+rectHeight: Untere linke Ecke
      // des Rechtecks
      int startX = x * rectWidth;
      int startY = y * rectHeight;
      rect(startX, startY, startX + rectWidth, startY + rectHeight);
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(200, 200);
  background(255);
  boolean[][] eingabe = {{true, false}, {false, false}};
  drawArray(magnify(eingabe, 1));
}

