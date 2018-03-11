// Funktion zum Durchführen eines URL-Encodings.
// An die Funktion wird der Originalstring eingegeben.
// Der konvertierte String wird von der Funktion
// zurückgeliefert.
static String urlEncode(String s) {
  String encoded = "";

  // Alle Zeichen im String durchgehen
  for (int i = 0; i < s.length(); i++) {
    char c = s.charAt(i);
    // Schreibe Zeichen in Ausgabestring
    if (c == ' ') {
      encoded = encoded + "%20";
    }
    else if (c == '*') {
      encoded = encoded + "%2A";
    }
    else if (c == '+') {
      encoded = encoded + "%2B";
    }
    else if (c == ',') {
      encoded = encoded + "%2C";
    }
    else if (c == '/') {
      encoded = encoded + "%2F";
    }
    else if (c == ':') {
      encoded = encoded + "%3A";
    }
    else if (c == ';') {
      encoded = encoded + "%3B";
    }
    else if (c == '=') {
      encoded = encoded + "%3D";
    }
    else if (c == '?') {
      encoded = encoded + "%3F";
    }
    else {
      encoded = encoded + c;
    }
  }

  return encoded;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  println(
    urlEncode("http://www.hanser-fachbuch.de/buch/WebSockets/9783446443716")
  );
}

