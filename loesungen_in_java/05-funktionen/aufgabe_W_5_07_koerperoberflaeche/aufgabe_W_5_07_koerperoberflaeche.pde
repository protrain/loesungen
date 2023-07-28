// Funktion zur Berechnung der Körperoberfläche
// Das Gewicht und die Größe werden als Integer-
// Werte an die Funktion übergeben, die das
// Ergebnis der Berechnung als Fließkommazahl
// zurückliefert.
float kof(int height, int weight) {
  float a = height * weight / 3600.0;
  float b = sqrt(a);             // Berechnung der Wurzel von a
  return b;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  println(kof(180, 58));
}

