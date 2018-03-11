// Funktion zur Berechnung der Konfektionsgröße in Abhängigkeit des
// Geschlechts, der Körpergröße und des Brustumfangs. Die Werte werden
// an die Methode übergeben. Nach der Berechnung wird das Ergebnis als
// Integer zurückgegeben.
int computeGarmentSize(boolean isFemale, int bodyHeight, int bustline) {
  int garmentSize = bustline / 2;    // Berechnung der Konfektionsgröße

  // Sonderfälle für Frauen
  if (isFemale) {                    // Wird Berechnung für eine Frau?
    garmentSize = garmentSize - 6;   // Konfektionsgröße um 6 minimieren

    if (bodyHeight > 170) {          // Ist die Frau größer als 170cm
      garmentSize = garmentSize * 2; // Konfektionsgröße verdoppeln
    }                                
    else if (bodyHeight < 164) {     // und wenn Kleiner als 164cm
      garmentSize = garmentSize / 2; // Konfektionsgröße halbieren
    }
  }

  return garmentSize;               // Rückgabe der Konfektionsgröße
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  println(computeGarmentSize(true, 167, 92));
}

