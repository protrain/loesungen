// Klasse zur Realisierung eines Highscore-Eintrags
class HighscoreEntry {
  // Deklaration privater Variablen
  private String nickname;
  private int points;

  // Konstruktor, der als Eingabewerte den Nickname und
  // die erreichten Punkte erwartet.
  public HighscoreEntry(String nickname, int points) {
    this.nickname = nickname;
    this.points = points;
  }

  // Öffentliche Methode zur Ausgabe eines Strings mit der
  // Angabe von Nickname und der erreichten Punkte.
  public String toString() {
    return this.nickname + " - " + this.points + " Punkte";
  }
}

// Klasse zur Realisierung einer Highscore-Tabelle
class HighscoreTable {
  // Deklaration interner Variablen
  private HighscoreEntry[] entries;

  // Konstruktor der Klasse, der die Initialisierung vornimmt.
  public HighscoreTable() {
    // Lege leere Highscore-Liste mit 10 Platzierungen an
    this.entries = new HighscoreEntry[10];
    for (int i = 0; i < 10; i++) {
      this.entries[i] = new HighscoreEntry("Name" + i, 0);
    }
  }

  // Öffentliche Methode zum Hinzufügen eines neuen Eintrags in die
  // Highscore-Liste. Übergeben werden der Nickname, die erreichten
  // Punkte sowie die Position innerhalb der Liste
  public void addEntry(String nickname, int points, int position) {
    // Nutze die HighscoreEntry-Klasse
    HighscoreEntry entry = new HighscoreEntry(nickname, points);

    // Gehe alte Liste bis zur Position durch
    HighscoreEntry[] entriesTemp = new HighscoreEntry[entries.length + 1];
    for (int i = 0; i < position - 1; i++) {
      // Füge altes Element hinzu
      entriesTemp[i] = entries[i];
    }

    // Füge jetzt neues Element hinzu
    entriesTemp[position - 1] = entry;

    // Gehe Rest der Liste durch
    for (int i = position - 1; i < entries.length; i++) {
      // Füge altes Element hinzu
      entriesTemp[i + 1] = entries[i];
    }

    // Setze temporäre Liste als neue Liste
    this.entries = entriesTemp;
  }

  // Öffentliche Methode zur Ausgabe der Highscore-Liste
  public void printList() {
    int pos = 1;
    for (int i = 0; i < entries.length; i++) {
      println("Platz " + pos + ": " + entries[i]);
      pos = pos + 1;
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  HighscoreTable hs = new HighscoreTable();
  hs.addEntry("Dieter", 666, 1);
  hs.addEntry("Thomas", 12, 6);
  hs.printList();
}

