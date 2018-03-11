// Funktion zur einfachen Komprimierung von Strings
// Als Eingabeparameter wird der zu komprimierende String
// übergeben. Die Funktion liefert das Ergebnis der Komprimierung
// zurück.
String simpleCompression(String input) {
  int cCount = 0; // Gezählte gleiche Zeichen
  char lastChar = input.charAt(0); // Letztes Zeichen
  String output = ""; // Komprimierter String

  // Gehe alle Zeichen im String durch
  for (int i = 0; i < input.length(); i++) {
    // Bestimmen des aktuellen Zeichens
    char currentChar = input.charAt(i);

    // Wenn Zeichen übereinstimmen
    if (currentChar == lastChar) {
      // Erhöhe Zähler
      cCount = cCount + 1;
    }
    else {
      // Anzahl + Zeichen an Ausgabestring schreiben
      output = output + "" + cCount + lastChar;

      // Zeichenzähler zurücksetzen
      cCount = 1;
    }

    // Letztes Zeichen aktualisieren
    lastChar = currentChar;
  }

  // Letztes Zeichen noch hinzufügen (wurde in Schleife nicht
  // verarbeitet)
  output = output + "" + cCount + lastChar;

  return output;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  String bwImageStringA = "WWWWBBBWBBBBBBWW"; // compressed: "4W3B1W6B2W"
  String bwImageStringB = "BBBBWWWWWWWWWB";   // compressed: "4B9W1B"
  String bwImageStringC = "WBBBBWWWWWWB";     // compressed: "1W4B6W1B"

  println(simpleCompression(bwImageStringA));
  println(simpleCompression(bwImageStringB));
  println(simpleCompression(bwImageStringC));
}

