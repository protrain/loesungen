// Funktion zum Konvertieren eines JSON-Strings in ein
// Java-Array. Die Funktion erhält den JSON-String in der
// Übergabe und liefert das Ergebnis-Array zurück.
public static String[] toStringArray(String jsonArray) {
  String[] stringArray = new String[0];

  // Alle Leerzeichen entfernen
  jsonArray = jsonArray.replaceAll(" ", "");

  // sind wir gerade mitten in einem JSON-String?
  boolean stringOpen = false;

  String word = "";

  // Gehe jedes Zeichen durch
  for (int i = 0; i < jsonArray.length(); i++) {
    // Sind wir jetzt bei einem Anführungsstrich (ganz wichtig: Backslash
    // vor dem Anführungsstrich, sonst interpretiert Java es als Ende des
    // Strings)
    if (jsonArray.charAt(i) == '\'') {
      // Waren wir in einem String, sind wir jetzt am Ende
      if (stringOpen == true) {
        // Füge hinzu
        // neues Array anlegen (ein Element größer)
        String[] newArray = new String[stringArray.length + 1];

        // Kopiere alle alten Elemente rüber
        for (int j = 0; j < stringArray.length; j++) {
          newArray[j] = stringArray[j];
        }

        // neues Element hinzufügen
        newArray[newArray.length - 1] = word;

        // Setze neues Array zum Ausgabe-Array
        stringArray = newArray;

        // Word resetten
        word = "";
        stringOpen = false;
      }
      else {
        // Jetzt sind wir im JSON-String
        stringOpen = true;
        // Ansonsten Zeichen hinzufügen, solange wir
        // im JSON-String sind
      }
    }

    else if (stringOpen == true) {
      word = word + jsonArray.charAt(i);
    }
  }

  return stringArray;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  String jsonArray = "[ 'Null', 'Eins', 'Zwei', 'Drei', 'Vier' ]";
  String[] stringArray = toStringArray(jsonArray);

  for (int i = 0; i < stringArray.length; i++) {
    println(stringArray[i]);
  }
}

