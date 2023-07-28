// Funktion zum Erzeugen eines Memory-Felds
// An die Funktion wird die zu erstellende
// Größe übergeben. Die Funktion gibt als Ergebnis
// das generierte Spielfeld als zweidimensionales Array
// zurück.
int[][] generateMemoryField(int fieldSize) {
  // Anzahlnummer der Karten
  int numElements = fieldSize * fieldSize;

  // Gültige Spielfeldgröße?
  if (numElements % 2 == 0 && numElements > 0) {
    // Erzeuge leeres Spielfeld (fieldSize x fieldSize)
    int[][] memoryField = new int[fieldSize][fieldSize];

    int numPaare = numElements / 2;

    // Belege Feld mit möglichen Zahlen
    for (int number = 1; number < numPaare + 1; number = number + 1) {
      // Immer zweimal (= 1 Paar) durchführen
      for (int j = 0; j < 2; j++) {
        // Wähle zufällige Position
        int randomX = int(random(0, fieldSize));
        int randomY = int(random(0, fieldSize));

        // Solange Position schon belegt, neue Position wählen
        while (memoryField[randomX][randomY] != 0) {
          randomX = int(random(0, fieldSize));
          randomY = int(random(0, fieldSize));
        }

        // Setze Zahl
        memoryField[randomX][randomY] = number;
      }
    }

    return memoryField;
  }
  else {
    // ungültige Spielfeldgröße
    return new int[0][0];
  }
}

// Funktion zur Visualisierung des berechneten Spielfelds
// An die Funktion wird das generierte Spielfeld als
// zweidimensionales Array übergeben.
void visualizeMemoryField(int[][] memoryField) {
  int fieldSize = memoryField.length;

  if (fieldSize != 0) {
    // Pixel pro Schritt
    int stepSize = width / fieldSize;

    // Halbe Größe einer Karte
    int stepMiddle = stepSize / 2;

    int x = 0;
    int y = 0;
    for (int i = 0; i < fieldSize; i++) {
      int[] row = memoryField[i];
      x = 0;
      for (int j = 0; j < row.length; j++) {
        int element = row[j];

        // Karte als Rechteck zeichnen
        fill(255);
        stroke(0);
        rect(x, y, x + stepSize, y + stepSize);

        // Zahlen einzeichnen
        fill(0);
        textSize(stepMiddle);
        text(element, x + stepMiddle / 2, y + stepMiddle + stepMiddle / 4);
        x = x + stepSize;
      }
      y = y + stepSize;
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(600, 600);
  background(255, 255, 255);

  int[][] memoryField = generateMemoryField(4);
  visualizeMemoryField(memoryField);
}

