// Funktion zur Bestimmung eines Zeichens auf einen Vokal
// Das Zeichen wird an die Funktion übergeben. Die Funktion
// gibt einen Wahrheitswert zurück.
public static boolean isVowel(char c) {
  // Gebe true zurück, wenn Buchstabe ein Vokal ist
  if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
    return true;
  }
  else {
    return false;
  }
}

// Funktion zur Umsetzung des MRA-Algorithmus. Die Funktion
// erhält ein Wort als String und liefert den Match Rating
// Approach
public static String mra(String word) {
  // Wandle Buchstaben in Großbuchstaben um
  word = word.toUpperCase();

  String temp = "";
  char c;

  // Gehe alle Zeichen durch
  for (int i = 0; i < word.length(); i++) {
    c = word.charAt(i);

    // Der erste Buchstabe darf ein Vokal sein,
    // also springe in nächste Schleifeniteration
    if (isVowel(c) && i > 0) {
      continue;
    }

    // Wenn es nicht der erste Buchstabe ist, prüfe,
    // ob es eine Buchstabenwiederholung ist.
    if (i > 0 && c == word.charAt(i - 1)) {
      // Springe in nächste Schleifeniteration
      continue;
    }

    // Übernehme Buchstaben, wenn die
    // beiden Fälle oben nicht zutreffen
    temp = temp + word.charAt(i);
  }

  // Kürzen bei zu langem Wort
  if (temp.length() > 6) {
    // die ersten drei Buchstaben
    String start = temp.substring(0, 3);
    // die letzten drei Buchstaben
    String end = temp.substring(temp.length() - 3);
    temp = start + end;
  }

  return temp;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  //println("Basketball");
  println(mra("Armbanduhr"));
}

