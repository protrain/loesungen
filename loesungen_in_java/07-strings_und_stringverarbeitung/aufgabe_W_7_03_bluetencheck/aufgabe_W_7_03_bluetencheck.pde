// Funktion, die die Position eines Buchstabens im Alphabet
// zurückliefert. An die Funktion wird der Buchstabe übergeben,
// für den die Position bestimmt und am Ende der Funktion
// zurückgeliefert wird.
int getPositionInAlphabet(char letter) {
  // String mit dem Alphabet
  String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  // Hole Position aus Alphabet
  // (Position im String + 1, da von 0 losgezählt wird)
  int pos = alphabet.indexOf(letter) + 1;
  return pos;
}

// Funktion zur Berechnung der Prüfsumme einer Seriennummer
// eines Euro-Geldscheins. Die Funktion erhält die Serien-
// nummer als String und liefert die Prüfzahl zurück.
int computeCheckDigit(String serialnumber) {
  char letter = serialnumber.charAt(0);
  // Hole Position im lateinischen Alphabet
  int posNumber = getPositionInAlphabet(letter);

  // Berechne Summe
  int sum = 0;

  // Addiere Quersumme
  while (posNumber != 0) {
    sum = sum + posNumber % 10;
    posNumber = posNumber / 10;
  }

  // Addiere restliche Ziffern
  // Wandle dabei die Ziffern in Integer-Werte um
  for (int i = 1; i < 11; i++) {
    sum = sum + Integer.parseInt("" + serialnumber.charAt(i));
  }

  // Ganzzahligen Rest der Division durch 9 bestimmen (Modulo)
  int rest = sum % 9;

  // Berechne Prüfziffer
  // Subtrahiere Rest von 8
  int checkDigit = 8 - rest;

  // Wenn Ergebnis = 0, dann ist Prüfziffer = 9
  if (rest == 0) {
    checkDigit = 9;
  }
  return checkDigit;
}

// Funktion, die die Prüfziffer einer Seriennummer
// eines Geldscheins zurückliefert. Die Seriennummer
// wird an die Funktion übergeben. Die Funktion liefert
// die Prüfziffer der Seriennummer zurück.
int getCheckDigit(String serialnumber) {
  return Integer.parseInt("" + serialnumber.charAt(11));
}

// Funktion zur Überprüfung der Gültigkeit einer Seriennummer
// eines Geldscheins. Die Seriennummer wird als String an die
// Funktion übergeben und liefert einen Wahrheitswert zurück.
boolean isCheckDigitValid(String serialnumber) {
  return getCheckDigit(serialnumber) == computeCheckDigit(serialnumber);
}

// Funktion zum Zerteilen eines Eingabestrings, der an
// die Funktion übergeben wird. Als Ergebnis wird ein
// Array mit den Teilstrings zurückgegeben.
String[] split(String input) {
  int stringLength = input.length();
  String[] output = new String[2];

  // Aktueller ausgelesener String (bis Semikolon)
  String word = "";

  for (int i = 0; i < stringLength; i++) {
    // Semikolon entdeckt oder Ende des Strings
    if (input.charAt(i) == ';') {
      // Füge Wort hinzu
      output = addToArray(word, output);

      // Lösche aktuelles Wort
      word = "";
    }
    // Letztes Element im String -> Wort ergänzen + hinzufügen
    else if (i == stringLength - 1) {
      word = word + input.charAt(i);
      output = addToArray(word, output);
    }
    // Sonst String um aktuellen Character ergänzen
    else {
      word = word + input.charAt(i);
    }
  }

  return output;
}

// Funktion zum Hinzufügen eines neuen Stringteils an ein Array.
// Die Funktion erhält den hinzuzufügenden String sowie das Array,
// an das der String angefügt werden soll.
String[] addToArray(String element, String[] array) {
  // Position, an der Element hinzugefügt werden soll
  int addPos = -1;

  // Finde leere Stelle
  // Gehe Array von vorne durch
  for (int i = 0; i < array.length; i++) {
    if (array[i] == null) {
      // leere Stelle gefunden
      addPos = i;

      // Springe aus Schleife
      break;
    }
  }

  // Wenn nichts gefunden -> Erweitern
  if (addPos == -1) {
    String[] arrayTemp = new String[array.length + 1];

    // Kopiere alle Elemente
    for (int i = 0; i < array.length; i++) {
      arrayTemp[i] = array[i];
    }

    // Setze kopiertes, vergrößertes Array als
    // neues Array
    array = arrayTemp;

    // Hinzufügeposition ist letzte Stelle
    addPos = array.length - 1;
  }

  // Füge Element hinzu
  array[addPos] = element;
  return array;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  println(isCheckDigitValid("S00630387745"));
}

