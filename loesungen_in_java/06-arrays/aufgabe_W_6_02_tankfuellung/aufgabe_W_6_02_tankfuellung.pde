// Funktion zur Berechnung des durchschnittlichen Verbrauchs
// An die Funktion wird ein Array mit Integer-Werten übergeben,
// die die gefahrenen Kilometer bis zum nächsten Tankstopp
// enthalten. Die Funktion gibt den Durchschnittswert als
// Fließkommazahl zurück.
float averageFuelComsumption(int[] kilometersPerTankful) {
  // Initialisierung der Variablen
  float averageConsumption = 0.0f;
  int sumKilometers = 0;

  // Summiere alle Kilometer
  for (int i = 0; i < kilometersPerTankful.length; i++) {
    sumKilometers = sumKilometers + kilometersPerTankful[i];
  }

  // Teile durch Gesamtzahl
  averageConsumption = float(sumKilometers) / kilometersPerTankful.length;

  return averageConsumption;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  int[] kilometers = { 123, 134, 120, 122 };

  println(averageFuelComsumption(kilometers));
}

