// Funktion zum Erzeugen eines umrahmten Texts.
// Die Funktion erhält den Text zeilenweise als Array
// vom Typ String. Der fertig gerahmte Text wird auf
// der Konsole ausgegeben.
public static void frameWordlist(String[] wl) {
  // Maximale Textbreite
  int maxWidth = 0;

  // Bestimme maximale Textbreite
  // Gehe alle Wörter durch
  for (int i = 0; i < wl.length; i++) {
    // Wenn die Länge des Wortes größer als bisheriges Maximum
    // ist, dann überschreiben
    if (wl[i].length() > maxWidth) {
      maxWidth = wl[i].length();
    }
  }

  // Schreibe oberen Rahmenrand
  // 2 Sternchen + 2 Leerzeichen länger als maximale Wortlänge
  for (int i = 0; i < maxWidth + 4; i++) {
    print("*");
  }
  println();

  // Textzeilen
  // Gehe jedes Wort durch
  for (int i = 0; i < wl.length; i++) {
    print("* ");
    print(wl[i]);
    // Schreibe restliche Leerzeichen, je nach Wortlänge
    for (int j = 0; j < maxWidth - wl[i].length(); j++) {
      print(" ");
    }
    println(" *");
  }

  // Schreibe unteren Rahmenrand
  for (int i = 0; i < maxWidth + 4; i++) {
    print("*");
  }
  println();
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  String[] test = {
    "Rahmen",
    "sind",
    "toll!"
  };

  frameWordlist(test);
}

