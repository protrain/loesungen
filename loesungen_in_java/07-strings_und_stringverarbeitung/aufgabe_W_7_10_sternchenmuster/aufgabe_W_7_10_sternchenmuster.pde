// Funktion zum Zeichnen von Sternchenmustern in der Kommandozeile
// An die Funktion wird die Anzahl an Zeilen übergeben.
void drawStars(int rows) {
  // Zeilen von oben bis Mitte
  for (int numStars = 1; numStars < rows; numStars = numStars + 1) {
    // Anzahl der auszugebenden Sternchen wächst
    // mit jedem Schleifendurchlauf
    printStars(numStars);
  }

  // In der Mitte werden (fast) doppelt so viele
  // ausgegeben
  printStars(rows * 2 - 1);

  // Für die nachfolgenden Zeilen ...
  for (int i = 1; i < rows; i++) {
    // ... immer ein Sternchen weniger ausgeben
    int numStars = rows - i;
    // Aufruf mit zwei Parametern, damit die Leerzeichen
    // berücksichtigt werden
    printStars(numStars, rows);
  }
}

// Zeichnet angegebene Nummer an Sternchen in eine Reihe
// Funktion zum Zeichnen der Anzahl angegebener Sternchen
// mit Berücksichtigung von Leerzeichen.
// Die Funktion erhält die Anzahl der auszugebenden Sternchen
// sowie die Anzahl von Leerzeichen.
void printStars(int numStars, int numSpace) {
  // Füge ggf. Leerzeichen hinzu
  for (int i = 0; i < numSpace; i++) {
    print(" ");
  }

  for (int i = 0; i < numStars; i++) {
    print("*");
  }

  println();
}

// Überladung der Funktion, falls printStars nur mit
// einem Parameter aufgerufen wird. Die Funktion erhält
// die Anzahl zu druckender Sterne und verwendet die
// Basis-Funktion mit geeigneten Werten.
void printStars(int numStars) {
  printStars(numStars, 0);
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  drawStars(4);
}

