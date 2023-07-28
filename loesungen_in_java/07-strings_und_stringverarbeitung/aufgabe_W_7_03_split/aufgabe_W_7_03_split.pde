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
      // Da Arrays nicht dynamisch vergrößert werden können, muss
      // eine eigene Funktion diese Anforderung ermöglichen
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
  println(split("ab;cde;fghi;jklm"));
}

