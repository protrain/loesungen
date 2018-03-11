// Globale Symbolkonstanten
char FREE = '_'; // Freier Sitz
char TAKEN = '#'; // Belegter Sitz

// Globale Arena
char[][] arena;
int minSeats = 3; // Anzahl der Sitze in der letzten Reihe

// Funktion zum Generieren einer neuen Arena. Als
// Eingabewert dient die Anzahl an Zeilen. Die Arena
// wird in einem Array von Chars zurückgegeben
char[][] createArena(int numRows) {
  // zu befüllendes Gesamt-Array
  arena = new char[numRows][numRows + (minSeats - 1)];

  // Gehe numerisch jede zu erzeugende Reihe durch
  for (int i = 0; i < numRows; i++) {
    // Anzahl der Sitze in aktueller Reihe
    int numSeats = numRows - i + (minSeats - 1);

    // Einzelne Reihe
    // Gehe numerisch jeden zu erzeugenden Sitz durch
    for (int x = 0; x < numSeats; x++) {
      // Füge Arrayelement hinzu
      arena[i][x] = FREE;
    }
  }

  return arena;
}

// Funktion, die die Arena grafisch darstellt
// Erhält ein zweidimensionales Char-Array
void visualizeArena(char[][] arena) {
  // Gehe jede Reihe durch
  for (int y = 0; y < arena.length; y++) {
    // Gehe jeden Sitz durch
    // Arraybreite = arena[0].length
    for (int x = 0; x < arena[0].length; x++) {
      // Gebe Reihenelement aus
      print(arena[y][x]);
    }

    // Mache Zeilenumbruch (für die nächste Reihe)
    println();
  }
}

// Funktion zum Buchen eines einzelnen Sitzplatzes
// Als Eingabe wird die Reihe und der Platz angegeben
void bookSeat(int row, int seat) {
  // Setze Sitzplatz auf belegt
  arena[row][seat] = TAKEN;
}

// Funktion zum zufälligen Buchen von  Sitzplätzen
// in der gesamten Arena
void fillSeats() {
  // Anzahl der Reihen
  int numRows = arena.length;

  // Gehe jede Reihe durch (von Reihe 0 bis Gesamtzahl)
  for (int y = 0; y < numRows; y++) {
    // Stuhlanzahl in einer Reihe
    int numSeats = numRows - y + (minSeats - 1);
    // Gehe jeden Sitz durch
    for (int x = 0; x < numSeats; x++) {
      // Zufallszahl zwischen 0 und 1 (Random ist Zahl
      // von 0 bis 1,9999999...)
      int randomNumber = int(random(0, 2));
      // Wenn Zufallszahl eine 1 ist, soll Sitz gebucht
      // werden
      if (randomNumber == 1) {
        bookSeat(y, x);
      }
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  arena = createArena(10);
  fillSeats();
  visualizeArena(arena);
}

