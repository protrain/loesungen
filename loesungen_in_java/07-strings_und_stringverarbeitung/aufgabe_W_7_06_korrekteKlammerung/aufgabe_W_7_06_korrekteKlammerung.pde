// Funktion zur Überprüfung eines Strings auf eine gültige
// Klammerung. Der String wird an die Funktion übergeben.
// Diese liefert am Ende einen Wahrheitswert, der angibt,
// ob eine korrekte Klammerung vorliegt.
boolean checkBrackets(String input) {
  // Anzahl der noch geöffneten Klammern
  int openBrackets = 0;

  // Ist die letzte Klammer eine geschlossene?
  boolean lastBracketClosed = true;

  // Gehe Zeichen für Zeichen durch
  for (int i = 0; i < input.length(); i++) {
    // Hole Zeichen
    char c = input.charAt(i);

    // Offene Klammer gefunden
    if (c == '(') {
      // Offene Klammeranzahl erhöhen
      openBrackets = openBrackets + 1;

      // Letzte Klammer ist somit nicht geschlossen
      lastBracketClosed = false;
    }

    // Geschlossene Klammer gefunden
    if (c == ')') {
      // gibt es eine geöffnete Klammer hierzu
      if (openBrackets > 0) {
        // Offene Klammeranzahl reduzieren
        openBrackets = openBrackets - 1;
      }
      else { // sonst ist Klammerung nicht korrekt
        return false;
      }

      // Letzte Klammer ist damit geschlossen
      lastBracketClosed = true;
    }
  }

  // Wenn keine offenen Klammern mehr vorhanden sind und die
  // letzte Klammer geschlossen ist, wird true zurückgegeben
  return openBrackets == 0 && lastBracketClosed == true;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  println(checkBrackets("(()(a)(()((c))))"));
}

