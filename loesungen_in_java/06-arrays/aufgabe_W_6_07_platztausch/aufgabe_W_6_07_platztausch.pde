// Funktion zum Tauschen von Sitzplätzen
int[] switchSeats(int[] seats) {
  // Anzahl der Sitze ergibt sich aus Array-Größe
  int numSeats = seats.length;

  // Gehe Array bis zur Hälfte durch (bei komplettem Durchgang
  // wäre die gleiche Reihenfolge wie vorher)
  for (int i = 0; i < numSeats / 2; i++) {
    // Hole zu tauschende Plätze
    int seatA = seats[i];
    int seatB = seats[numSeats - i - 1];

    // Vertausche beide Plätze
    seats[i] = seatB;
    seats[numSeats - (i + 1)] = seatA;
  }

  return seats;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  int[] seats = { 0, 1, 2, 3, 4, 5, 6 };
  int[] seatSwitched = switchSeats(seats);

  // Gebe Array aus
  for (int i = 0; i < seatSwitched.length; i++) {
    print(seatSwitched[i] + " ");
  }
  println();
}

