// Importiere die Kennzeichen
String[][] importLicensePlates() {
  // Lade CSV-Datei mit allen Kennzeichen
  String[] licensePlatesCSV = loadStrings("kennzeichen.csv");

  // Erstelle daraus zweispaltiges Array
  String[][] licensePlates = new String[licensePlatesCSV.length][licensePlatesCSV.length];

  // Gehe alle Reihen der CSV-Datei durch
  for (int i = 0; i < licensePlatesCSV.length; i = i + 1) {
    // Unterteile Semikolons in Array-Elements
    licensePlates[i] = split(licensePlatesCSV[i], ";");
  }

  // Jetzt haben wir Liste mit allen KFZ-Kennzeichen importiert
  // Gebe diese Liste zurück
  return licensePlates;
}

// Bestimme Stadt/Landkreis basierend auf dem Kennzeichen
String getLocation(String identifier) {
  // Extrahiere Ortskürzel aus Kennzeichen
  identifier = identifier.split("-")[0];

  // Importiere Liste der Autokennzeichen
  String[][] licensePlates = importLicensePlates();

  // Binäre Suche

  // Beginne bei gesamtem Array
  int left = 0;
  int right = licensePlates.length - 1;

  // Wiederhole solange, bis wir alle Werte im Array abgesucht haben
  while (left <= right) {
    // Bilde die Mitte zwischen den Bereichen links und rechts
    int middle = left + ((right - left) / 2);

    // Haben wir das richtige Kennzeichenkürzel in der Mitte?
    if (licensePlates[middle][0].equals(identifier)) {
      // Gebe die Ortsbezeichnung zurück
      return licensePlates[middle][1];
    }
    else {
      // Kennzeichen ist nicht in der Mitte, daher prüfen wir jetzt
      // anhand der Buchstaben, in welchem Bereich wir weitersuchen
      // sollten

      // Wenn das gesuchte Kennzeichen alphabetisch größer ist
      if (identifier.compareTo(licensePlates[middle][0]) > 0) {
        // Suche rechts weiter
        left = middle + 1;
      }
      else {
        // Sonst auf der linken Seite
        right = middle - 1;
      }
    }
  }

  // Wir sind am Ende angekommen, also haben wir leider nichts
  // gefunden
  return "KENNZEICHEN NICHT GEFUNDEN";
}


void setup() {
  println(getLocation("K-TH-666"));
  println(getLocation("AB-CD-123"));
  println(getLocation("SRO-LI-7326"));
  println(getLocation("NON-EX-157"));
}
