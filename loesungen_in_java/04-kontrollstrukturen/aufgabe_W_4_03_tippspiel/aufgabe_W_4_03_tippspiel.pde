// Tatsächliches Endergebnis des Spiels
int home = 3;
int guest = 2;

// Getipptes Endergebnis
int betHome = 3;
int betGuest = 2;

// Berechnete Punkte
int points = 0;

// Bestimme Punktzahl
if (home == betHome && guest == betGuest) { // exakter Tipp
  points = 3;
}
else if ((home - guest) > 0 
  && (betHome - betGuest) > 0) {   // richtige Tendenz: Sieg Heim
  points = 1;
}
else if ((home - guest) < 0 
  && (betHome - betGuest) > 0) {   // richtige Tendenz: Sieg Gast
  points = 1;
}
else if ((home - guest) == 0 
  && (betHome - betGuest) == 0) {  // richtige Tendenz: Unentschieden
  points = 1;
}
else {                             // falscher Tipp
  points = 0;
}

// Gebe die durch den Tipp erreichte Punktzahl aus
println(
  "Ergebnis: " + home + ":" + guest + ", Tipp: " + betHome + ":" +
    betGuest + " -> Punkte: " + points
);
