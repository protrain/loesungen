// Funktion zur Prüfung, ob ein angegebenes Jahr ein Schaltjahr ist
// Die Funktion erhält die Jahreszahl als Integer-Wert und gibt
// einen Wahrheitswert {true || false} als Ergebnis zurück.
boolean checkLeapYear(int yearInput) {
  if (yearInput % 400 == 0) { // Jahreszahl glatt durch 400 teilbar?
    return true;              // Rückgabe: es ist ein Schaltjahr!
  }
  else                        // sonst prüfe,
  // ob Jahreszahl glatt durch 4, aber nicht durch 100 teilbar
  if (yearInput % 4 == 0 && yearInput % 100 != 0) {
    return true;              // Rückgabe: es ist ein Schaltjahr!
  }
  else {                      // sonst nicht
    return false;             // Rückgabe: kein Schaltjahr!
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  println("War 1800 ein Schaltjahr? -> " + checkLeapYear(1800));
  println("War 2016 ein Schaltjahr? -> " + checkLeapYear(2016));
  println("Wird 2020 ein Schaltjahr sein? -> " + checkLeapYear(2020));
}

