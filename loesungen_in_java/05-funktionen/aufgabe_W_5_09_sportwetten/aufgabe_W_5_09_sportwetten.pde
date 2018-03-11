// Funktion zur Berechnung der Wettpunkte. Die dazu notwendigen Werte
// werden als Integer-Werte an die Funktion übergeben. Das Ergebnis
// wird als Ganzzahlwert zurückgegeben.
int computeBetScore(int home, int guest, int betHome, int betGuest) {
  // bei genauer Voraussage
  if (home == betHome && guest == betGuest) {
    // verlasse die Funktion und gib den Wert 3 als Ergebnis zurück
    return 3;
  }

  // Tendenz nach unten richtig
  if (home > betHome && guest > betGuest) {
    // verlasse die Funktion und gib den Wert 1 als Ergebnis zurück
    return 1;
  }

  // Tendenz nach oben richtig
  if (home < betHome && guest < betGuest) {
    // verlasse die Funktion und gib den Wert 1 als Ergebnis zurück
    return 1;
  }

  // Tendenz bei Unentschieden
  if (home == guest && betHome == betGuest) {
    // verlasse die Funktion und gib den Wert 1 als Ergebnis zurück
    return 1;
  }

  // ansonsten
  return 0;
}

// Funktion zur Berechnung des Wettergebnisses für alle Wetten
// Als Eingabeparameter wird ein zweidimensionales Integer-Array
// angegeben. Das Ergebnis ist ebenfalls vom Typ Integer
int computeCompleteBetScore(int[][] data) {
  // Initialisierung der Variablen
  int result = 0;

  // Durchlaufe das Array
  for (int j = 0; j < data.length; j++) {
    // Berechne das Ergebnis als das bisherige Ergebnis + die
    // Wettpunkte für die aktuelle Wette, die mit Index [j]
    // angegeben werden.
    result = result + computeBetScore(
      data[j][0],
      data[j][1],
      data[j][2],
      data[j][3]
    );
  }

  // Gib die Summe aller erzielten Wettpunkte zurück.
  return result;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
public void setup() {
  // Das zweidimensionale Array besteht aus drei Zeilen = Wetten
  // und jeweils den Werten home, guest, betHome, betGuest
  int[][] data = {
                    {3, 2, 3, 2},
                    {1, 1, 1, 0},
                    {2, 2, 1, 1}
                 };

  println(computeCompleteBetScore(data));
}

