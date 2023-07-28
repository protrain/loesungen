// Funktion zur Überprüfung von Übereinstimmungen
// Die Funktion erhält die Werte für Person a und b in einem
// Array mit Wahrheitswerten und gibt die prozentuale
// Überschneidung zurück
int interestsMatch(boolean[] a, boolean[] b) {
  // Abbruch, wenn beide Profile ungleich groß sind
  if (a.length != b.length) {
    return 0;
  }

  int numMatches = 0;

  // Gehe Liste durch
  for (int i = 0; i < a.length; i++) {
    // Erhöhe Zähler, wenn es Übereinstimmung gibt
    if (a[i] == b[i]) {
      numMatches = numMatches + 1;
    }
  }

  // Prozentzahl: Übereinstimmungen / Gesamtzahl * 100
  return (int)(numMatches / (float)a.length * 100);
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  boolean[] personA = {true, true, false, false, false, true};
  boolean[] personB = {true, false, false, false, false, true};
  boolean[] personC = {false, false, true, true, true, false};
  boolean[] personD = {false, false, true, true, true};

  println(interestsMatch(personA, personA));
  println(interestsMatch(personA, personB));
  println(interestsMatch(personA, personC));
  println(interestsMatch(personA, personD));
}

