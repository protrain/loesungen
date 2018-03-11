// Funktion zur Überprüfung einer Sudoku-Lösung auf Korrektheit.
// Als Eingabe an die Funktion wird die Sudoku-Lösung in Form eines
// zweidimensionalen Arrays übergeben. Die Funktion gibt als Ergebnis
// einen Wahrheitswert zurück.
boolean checkSudoku(int[][] sudoku) {
  // Array, das die Anzahl der Vorkommnisse jeder Zahl aufschreibt.
  // Position: Zahl
  // Inhalt an Position: Anzahl der Zahl
  int[] occurrences = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

  // Aktuelle Nummer im Sudoku
  int number;

  // Aktuelle Anzahl (aus Occurrences-Array)
  int count;

  // Prüfe Zeilen
  // Gehe jede Zeile durch
  for (int y = 0; y < sudoku.length; y++) {
    // Gehe jedes Element in der Zeile durch
    int[] row = sudoku[y];
    for (int x = 0; x < row.length; x++) {
      // Erhöhe Zähler für Zahl um 1
      number = row[x];
      occurrences[number] = occurrences[number] + 1;
    }

    // Gehe Zähler-Array durch
    for (int i = 0; i < occurrences.length; i++) {
      // Hole gezählte Anzahl aus Array
      count = occurrences[i];

      // Wenn Zahl häufiger als einmal vorkommt -> Keine gültige Lösung
      if (count > 1) {
        return false;
      }
    }

    // Zähler-Array wieder auf 0 setzen
    occurrences = new int[10];
  }

  // Prüfe Spalten
  // Gehe jede Spalte durch
  for (int x = 0; x < 8; x++) {
    // Gehe jedes Element in der Spalte durch
    for (int y = 0; y < 8; y++) {
      // Hole Zahl aus Position in Sudoku
      number = sudoku[y][x];

      // Erhöhe Zähler für Zahl um 1
      occurrences[number] = occurrences[number] + 1;
    }

    // Gehe Zähler-Array durch
    for (int i = 0; i < occurrences.length; i++) {
      // Hole gezählte Anzahl aus Array
      count = occurrences[i];

      // Wenn Zahl häufiger als einmal vorkommt -> Keine gültige Lösung
      if (count > 1) {
        return false;
      }
    }

    // Zähler-Array wieder auf 0 setzen
    occurrences = new int[10];
  }

  // Prüfe 3x3 Blöcke
  // Bestimme Blocknummer
  for (int i = 0; i < 3; i++) {       // Blocknummer in x-Richtung
    for (int j = 0; i < 3; i++) {     // Blocknummer in y-Richtung
      // Gehe inneren Block durch
      for (int y = 0; y < 3; y++) {
        for (int x = 0; x < 3; x++) {
          // Bestimme globale Position
          int posX = 3 * i + x;
          int posY = 3 * j + y;

          // Bestimme Zahl
          number = sudoku[posY][posX];

          // Erhöhe Zähler für Zahl um 1
          occurrences[number] = occurrences[number] + 1;
        }
      }

      // Gehe Zähler-Array durch
      for (int k = 0; k < occurrences.length; k++) {
        // Hole gezählte Anzahl aus Array
        count = occurrences[i];

        // Wenn Zahl häufiger als einmal vorkommt -> keine gültige Lösung
        if (count > 1 && count != 0) {
          return false;
        }
      }

      // Zähler-Array wieder auf 0 setzen
      occurrences = new int[10];
    }
  }

  // Wenn das Programm bis an diese Stelle kommt, wurde keine "return"-
  // Anweisung ausgeführt. Das bedeutet, die Prüfung ist erfolgreich!
  return true;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  // Test-Sudoku
  int[][] sudoku =
    {
      {8, 3, 5, 4, 1, 6, 9, 2, 7},
      {2, 9, 6, 8, 5, 7, 4, 3, 1},
      {4, 1, 7, 2, 9, 3, 6, 5, 8},
      {5, 6, 9, 1, 3, 4, 7, 8, 2},
      {1, 2, 3, 6, 7, 8, 5, 4, 9},
      {7, 4, 8, 5, 2, 9, 1, 6, 3},
      {6, 5, 2, 7, 8, 1, 3, 9, 4},
      {9, 8, 1, 3, 4, 5, 2, 7, 6},
      {3, 7, 4, 9, 6, 2, 8, 1, 5}
    };

  println(checkSudoku(sudoku));
}

