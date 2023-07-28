class Partei {
  String name;
  double stimmenAktuell;
  double stimmenVorher;

  // Konstruktor der Klasse, der die Objektgenerierung
  // nur unter der Angabe des Parteinamens als String,
  // der aktuellen Stimmenanzahl als Integer und der
  // vorherigen Stimmenanzahl als Integer ermöglicht
  public Partei(String name, double stimmenVorher, double stimmenAktuell) {
    this.name = name;
    this.stimmenAktuell = stimmenAktuell;
    this.stimmenVorher = stimmenVorher;
  }

  // Berechnet, um wie viel Prozent sich die Parteistimmen
  // von der vorherigen zur aktuellen Wahl entwickelt haben
  public double bestimmeEntwicklung() {
    // Berechne zunächst als absolute Zahl, wie sehr sich
    // die Stimmen verändert haben
    double entwicklungAbsolut = this.stimmenAktuell - this.stimmenVorher;

    // Berechne jetzt in Prozent, wie sich Zuwachs/Abnahme
    // im Vergleich zur vorherigen Wahl entwickelt haben
    double entwicklungProzent = entwicklungAbsolut / this.stimmenVorher * 100;

    return entwicklungProzent;
  }

  // Ermittle, ob Partei einen Zuwachs zur vorherigen Wahl
  // bekommen hat
  public boolean istZuwachs() {
    // Liegt die Prozentzahl über 0, haben wir einen Zuwachs
    return this.bestimmeEntwicklung() > 0;
  }

  public String toString() {
    // In diesem String speichern wir die Ausgabe
    String output = "Die Partei '" + this.name + "' hat einen";

    // Variiere den Text je nach Zuwachs oder Verlust
    if (this.istZuwachs()) {
      output = output + " Zuwachs ";
    }
    else {
      output = output + " Verlust ";
    }

    // Füge den Rest vom Text an
    output = output + "von " + this.bestimmeEntwicklung() + "% bekommen";

    // Gebe diesen String nun aus
    return output;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
public void setup() {
  // Erstelle Parteien
  Partei gewinnerPartei = new Partei("Gewinnerpartei", 500, 600);
  Partei verliererPartei = new Partei("Verliererpartei", 600, 300);

  // Gebe die Statistik aus
  println(gewinnerPartei);
  println(verliererPartei);
}
