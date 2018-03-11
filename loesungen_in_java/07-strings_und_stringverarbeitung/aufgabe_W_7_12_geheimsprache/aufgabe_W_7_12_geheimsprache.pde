// Statische Funktion zum Überführen eines englischen
// Texts in eine Geheimsprache. Der Text wird an die
// Funktion übergeben, und das überführte Ergebnis wird
// am Ende von der Funktion zurückgeliefert.
public static String pigLatin(String text) {
  // Packe jedes Wort in ein Array-Element
  String[] words = text.split(" ");

  // Temporärer String zur Verarbeitung
  String temp = "";

  for (int i = 0; i < words.length; i++) {
    // übernehme Wort ab dem 2. Buchstaben
    temp = temp + words[i].substring(1);

    // Setze 1. Buchstaben ans Ende
    temp = temp + words[i].charAt(0);

    // Füge "ay" hinzu
    temp = temp + "ay ";
  }

  // Gebe Satz ohne letztes Leerzeichen zurück
  return temp.substring(0, temp.length() - 1);
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  println(pigLatin("top secret"));
}

