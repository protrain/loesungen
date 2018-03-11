// Funktion zum Filtern von Content-Type- und Content-Length-Werten
// in einer Webserver-Status-Nachricht. Die Status-Nachricht wird in
// einem String-Array an die Funktion übergeben und liefert die
// relevanten Informationen zurück.
String filterContentHeader(String[] response) {
  String type = null;
  String length = null;

  // Gehe jede Response-Zeile durch
  for (int i = 1; i < response.length; i++) {
    // Trenne String nach Zeichenkette ": " in einzelne Array-Elemente auf
    String[] temp = response[i].split(": ");

    // Springe zu nächster For-Iteration, wenn mehr als 2x ": " in einer
    // Zeile (dann kann nichts gefunden werden)
    if (temp.length != 2) {
      continue;
    }

    // Setze Variablen nach Werten
    // Springe aus Schleife, wenn beide Werte schon gesetzt sind
    if (type != null && length != null) {
      break;
    }
    // Setze Content-Type, wenn Wert in Zeile ist
    else if (temp[0].equalsIgnoreCase("Content-Type")) {
      type = temp[1];
    }
    // Setze Content-Length, wenn Wert in Zeile ist
    else if (temp[0].equalsIgnoreCase("Content-Length")) {
      length = temp[1];
    }
  }

  // Erzeuge Ausgabe
  if (type != null && length != null) {
    return "The response contains: " + type + " (" + length + ")";
  }
  else {
    return "The response does not contain any content.";
  }
}


// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  String[] header = {
    "HTTP/1.1 200 OK",
    "Server: Apache",
    "Content-Length: 14188",
    "Connection: close",
    "Content-Type: image/jpg",
    "..."
  };

  println(filterContentHeader(header));
}

