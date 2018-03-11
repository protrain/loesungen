// Funktion zur Überprüfung eines Strings auf eine gültige
// E-Mail-Adresse. Die Funktion erhält die E-Mail-Adresse und
// liefert als Ergebnis einen Wahrheitswert zurück.
boolean isEmail(String email) {
  int stage = 0;
  int cCount = 0; // gezählte Characters im Bereich

  // Gehe jedes Zeichen durch
  for (int i = 0; i < email.length(); i++) {
    char c = email.charAt(i);
    if (c == '@') {
      // Nur erhöhen, wenn kein vorheriges @ erkannt wurde
      if (stage == 0 && cCount > 0) {
        stage = 1;
        cCount = 0;
      }
      else {
        // Sonst ungültige Mail-Adresse
        return false;
      }
    }
    else if (c == '.') {
      // Nur erhöhen, wenn bereits @ erkannt wurde
      if (stage == 1 && cCount > 0) {
        stage = 2;
        cCount = 0;
      }
      else {
        // Sonst ungültige Mail-Adresse
        return false;
      }
    }
    else {
      // Sonst Zeichenzähler erhöhen
      cCount = cCount + 1;
    }
  }

  // Alle Zeichen durchgegangen
  // Endergebnis ist wahr, wenn Zeichen am Ende 2 oder 3 sind
  return (cCount == 2 || cCount == 3);
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  //println(isEmail("john@doe.net"));
  //println(isEmail("john@doe.de"));
  //println(isEmail("john@doe.shop"));
  //println(isEmail("john@.net"));
  println(isEmail("@.net"));
}

