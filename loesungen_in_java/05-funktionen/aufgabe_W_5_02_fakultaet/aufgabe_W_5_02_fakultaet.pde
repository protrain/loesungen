// Die Funktion zur Berechnung endlicher Produkte erhält den
// Startwert s und den Endwert e als Integer Werte und liefert
// als Ergebnis einen Integer-Wert zurück.
int product(int s, int e) {
  if (e < 0 || s < 0) {          // ist einer der beiden Werte < 0
    return 0; // wird 0 zurückgegeben
  }
  else if (e == 0 || s == 0) {   // ist einer der beiden Werte = 0
    return 0; // wird 0 zurückgegeben
  }
  else if (e < s) {
    // Vertausche Werte, damit die for-Schleife
    // vom kleinsten zum größten Wert laufen kann
    int eTemp = e;               // Temporäres Speichern von e
    e = s;                       // Tauschen...
    s = eTemp;
  }

  // Deklaration und Initialisierung der Variablen für das Ergebnis
  // Der Startwert muss 1 sein (wegen Multiplikation)
  int result = 1;
  for (int i = s; i <= e; i++) { // Zähle vom Start- bis Endwert
    result = result * i;         // und multipliziere die Zahl mit dem
  }                              // Ergebnis

  // Das Ergebnis zurückliefern
  return result;
}

// Die Funktion zur Berechnung der Fakultät
// verwendet die Funktion zur Berechnung endlicher Produkte.
// An die Funktion wird der Wert n übergeben, für die die
// Fakultät berechnet werden soll.
int factorial(int n) {
  int result = product(1, n);    // Aufruf der Funktion
  return result;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  int result = factorial(6);
  println(result);
}

