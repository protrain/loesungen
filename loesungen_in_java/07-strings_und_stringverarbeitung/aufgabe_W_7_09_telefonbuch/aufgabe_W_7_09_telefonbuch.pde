// Funktion zum Einlesen eines Telefonbuchs in Form einer CSV-Datei
// Als Parameter wird die Angabe des Pfades zur Datei an die Funktion
// übergeben. Diese liefert den Inhalt der Datei als String-Array zurück.
String[] readPhonebook(String filename) {
  String[] phonebook = loadStrings(filename);
  String[][] output = new String[phonebook.length][5];

  // Telefonbuch einlesen
  for (int i = 0; i < phonebook.length; i++) {
    // Trenne CSV-Einträge
    String[] entryArray = split(phonebook[i]);

    // Ergänze Festnetznummer, wenn erste Ziffer = "0"

    // Wurde eine Nummer angegeben
    if (!entryArray[2].equals("")) {
      // Beginnt die Nummer mit einer '0'
      if (entryArray[2].charAt(0) == '0') {
        // Tauschen
        entryArray[2] = "+49" + entryArray[2].substring(1);
      }
    }

    // Ergänze Handynummer, wenn erste Nummer "0"

    // Wurde eine Nummer angegeben
    if (!entryArray[3].equals("")) {
      // Beginnt die Nummer mit einer '0'
      if (entryArray[3].charAt(0) == '0') {
        // Tauschen
        entryArray[3] = "+49" + entryArray[3].substring(1);
      }
    }
    // Füge Array an Ausgabe an
    output[i] = entryArray;
  }

  return combine(output);
}


// Funktion zum Zerteilen eines Eingabestrings, der an
// die Funktion übergeben wird. Als Ergebnis wird ein
// Array mit den Teilstrings zurückgegeben.
String[] split(String input) {
  int stringLength = input.length();
  String[] output = new String[2];
  String word = ""; // Aktueller ausgelesener String (bis Semikolon)
  for (int i = 0; i < stringLength; i++) {
    // Semikolon entdeckt oder Ende des Strings
    if (input.charAt(i) == ';') {
      // Füge Wort hinzu
      output = addToArray(word, output);
      // Lösche aktuelles Wort
      word =// Letztes Element im String -> Wort ergänzen + hinzufügen
      "";
    }
    else if (i == stringLength - 1) {
      word = word + input.charAt(i);
      output = addToArray(
        word,
        output// Sonst String um aktuellen Character ergänzen
      );
    }
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

    // Setze kopiertes, vergrößertes Array als neues Array
    array = arrayTemp;

    // Hinzufügeposition ist letzte Stelle
    addPos = array.length - 1;
  }

  // Füge Element hinzu
  array[addPos] = element;
  return array;
}

// Funktion zum Zusammensetzen eines zweidimensionalen Arrays
// zurück in ein String-Array mit kommaseparierten Werten
String[] combine(String[][] inputArray) {
  String[] output = new String[inputArray.length];

  // Gehe jede Zeile durch
  for (int i = 0; i < inputArray.length; i++) {
    String[] element = inputArray[i];

    // Erstes Element bereits übernehmen
    String row = element[0];

    // Jedes Element in der Zeile durchgehen
    for (int j = 1; j < element.length; j++) {
      // Füge restlichen Elemente der Zeile hinzu
      row = row + ";" + element[j];
    }

    // Spalte hinzufügen
    output[i] = row;
  }
  return output;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  // Array ausgeben. Datei telefonbuch.csv im Projektordner wird
  // dabei eingelesen.
  String[] phonebook = readPhonebook("telefonbuch.csv");

  for (int i = 0; i < phonebook.length; i++) {
    println(phonebook[i]);
  }
}

