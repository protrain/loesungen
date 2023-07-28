// Funktion zum Konvertieren eines IMDB-Texteintrags
// in eine tabellarische String-Array-Darstellung.
// An die Funktion wird ein eindimensionales String-Array
// mit den zeilenweisen IMDB-Einträgen übergeben. Als
// Ergebnis wird ein zweidimensionales Array mit Zeilen und
// Spalten für die Einträge generiert und zurückgegeben.
String[][] toTable(String[] imdbList) {
  // Leere Tabelle erzeugen mit
  // so vielen Zeilen wie im Eingabe-Array und mit je drei Spalten
  // für die Werte <Score><Filmtitel>(<Erscheinungsjahr>)
  String[][] t = new String[imdbList.length][3];

  // Jede Zeile der Liste durchgehen
  for (int i = 0; i < imdbList.length; i++) {
    // Zeile aus IMDB-Liste auslesen
    String s = imdbList[i];

    // Inhalte auslesen
    // das erste Leerzeichen trennt <Score> und <Filmtitel>
    String score = s.substring(0, s.indexOf(' '));

    // Die letzten 7 Zeichen eines IMDB-Eintrags bestehen aus
    // Leerzeichen + (<Erscheinungsjahr). Damit können wir den
    // <Filmtitel> ausschneiden, wenn wir bedenken, dass der Titel
    // nach dem <Score> angegeben wird:
    String title = s.substring(s.indexOf(' ') + 1, s.length() - 7);

    // Ausschneiden des <Erscheinungsjahr>s ohne Klammern. Da der
    // IMDB-String zuletzt aus der Jahreszahl und einer schließenden
    // Klammer besteht...
    String year = s.substring(s.length() - 5, s.length() - 1);

    // Reihen der Zeile hinzufügen
    t[i][0] = score;
    t[i][1] = title;
    t[i][2] = year;
  }

  return t;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  String[] liste = {
    "8.7 The Lord of the Rings: The Fellowship of the Ring (2001)"
  };

  String[][] listeConverted = toTable(liste);

  for (int y = 0; y < listeConverted.length; y++) {
    for (int x = 0; x < listeConverted[0].length; x++) {
      print(listeConverted[y][x] + "\t");
    }

    println();
  }
}

