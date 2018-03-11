// Funktion zur Bestimmung der minimalen Distanz zweier
// benachbarter Zahlen in einem eindimensionalen Array.
// Es wird das zu überprüfende Array in die Funktion hineingegeben,
// und der Index der ersten Zahl des Paares mit der minimalen
// Distanz soll zurückgegeben werden.
int minDist(int[] input) {
  // Die kleinste Distanz mit der größten erlaubten Integer-Zahl
  // initialisieren
  int smallestDist = 2147483647;

  // Ein Zeiger auf die kleinste Distanz initialisieren und der
  // noch auf kein Array-Element zeigt.
  int smallestDistPos = -1;

  // Die aktuelle Array-Größe merken
  int arraySize = input.length;

  // Gehe jedes Element durch
  for (int i = 0; i < arraySize - 1; i++) {
    // Berechne Distanz zum Nachbarn
    int distTemp = abs(input[i] - input[i + 1]);

    // Wenn Distanz kleiner als aktuell kleinste Distanz
    if (distTemp < smallestDist) {
      // Dann ersetzen
      smallestDist = distTemp;
      // und die Position im Array merken
      smallestDistPos = i;
    }
  }

  return smallestDistPos;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  int[] array = { 4, 8, 6, 1, 2, 9, 4 };
  println(minDist(array));
}

