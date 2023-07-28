// Funktion zur Ausgabe der Buchstaben in umgekehrter Reihenfolge
// An die Funktion wird ein Array mit char-Werten übergeben
void printBackwards(char[] charArray) {
  // Gehe Array rückwärts durch
  for (int i = charArray.length - 1; i >= 0; i = i - 1) {
    // Gebe Zeichen aus
    print(charArray[i]);
  }

  // Erzeuge Zeilenumbruch
  println();
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  char[] palindrom =
    {'r', 'e', 'i', 'b', 'n', 'i', 'e', 'e', 'i', 'n', 'b', 'i', 'e', 'r'};
  char[] test = {'H', 'a', 'l', 'l', 'o'};

  printBackwards(palindrom);
  printBackwards(test);
}

