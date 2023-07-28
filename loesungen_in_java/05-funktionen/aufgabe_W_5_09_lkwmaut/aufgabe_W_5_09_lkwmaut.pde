// Funktion zur Berechnung der LKW-Maut in Abhängigkeit der
// Schadstoffklasse, der Anzahl an Achsen und der gefahrenen Kilometer.
// Die Werte werden an die Funktion übergeben. Das Ergebnis der
// Berechnung wird als Fließkommazahl in Euro-Cent zurückgegeben.
float LKWMaut(char schadstoffklasse, int numAchsen, float km) {
  float kmPreis = 0.0f; // Initialisierung mit dem Wert 0.0

  // Bestimme km-Preis
  if (numAchsen <= 3) { // Wenn die Anzahl der Achsen <= 3
    switch (schadstoffklasse) { // Schadstoffklasse abfragen
      case 'A':         // handelt es sich um die Schadstoffklasse 'A'?
        kmPreis = 12.5; // setze den kmPreis auf 12.5
        break;          // und springe aus dem Switch-Block raus
      case 'B':         // analog zum Case 'A'...
        kmPreis = 14.6;
        break;
      case 'C':
        kmPreis = 15.7;
        break;
      case 'D':
        kmPreis = 18.8;
        break;
      case 'E':
        kmPreis = 19.8;
        break;
      case 'F':
        kmPreis = 20.8;
        break;
    }
  }
  else { // ab vier Achsen
    switch (schadstoffklasse) { // Schadstoffklasse abfragen
      case 'A':         // handelt es sich um die Schadstoffklasse 'A'?
        kmPreis = 13.1; // setzte den kmPreis = 13.1
        break;          // und springe aus dem Switch-Block raus
      case 'B':         // ...
        kmPreis = 15.2;
        break;
      case 'C':
        kmPreis = 16.3;
        break;
      case 'D':
        kmPreis = 19.4;
        break;
      case 'E':
        kmPreis = 20.4;
        break;
      case 'F':
        kmPreis = 21.4;
        break;
    }
  }

  return kmPreis * km; // gebe die berechnete LKW-Maut zurück
}

// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  println(
    "LKW-Maut für 13 km eines 2-Achsers der Schadstoffklasse A: " +
    LKWMaut('A', 2, 13) + " Eurocent"
  );

  println(
    "LKW-Maut für 13 km eines 5-Achsers der Schadstoffklasse D: " +
    LKWMaut('D', 5, 13) + " Eurocent"
  );
}

