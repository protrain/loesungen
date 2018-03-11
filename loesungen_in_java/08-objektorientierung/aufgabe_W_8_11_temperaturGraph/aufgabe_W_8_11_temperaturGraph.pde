// Klasse zur Realisierung eines Temperaturgraphen
public class TemperatureGraph {
  // Deklaration interner Variablen
  private int year;
  private int[] temperatures;

  // Konstruktor, der vorschreibt, dass Instanzen dieser
  // Klasse nur mit Angabe der Jahreszahl generiert werden
  // können.
  public TemperatureGraph(int year) {
    this.year = year;
    temperatures = new int[12];

    // Initialisiere alle Monate mit unmöglichen
    // Temperaturen (für Vollständigkeitscheck)
    for (int i = 0; i < temperatures.length; i++) {
      temperatures[i] = -1000;
    }
  }

  // Methode, die das Hinzufügen einer Temperatur in
  // Verbindung mit dem Monat ermöglicht.
  // Dazu werden Monat und Wert an die Methode übergeben.
  public void addTemperature(int month, int value) {
    // Nur arbeiten, wenn gültiger Monat angegeben wurde
    if (month > 0 && month < 13) {
      // Füge Temperatur hinzu
      temperatures[month - 1] = value;
    }
  }

  // Funktion zur Ausgabe des Graphen. Die Ausgabe erfolgt
  // direkt auf der Konsole.
  public void plotGraph() {
    // Nur arbeiten, wenn alle Monate ausgefüllt sind
    if (isComplete()) {
      // Hole minimale und maximale Temperaturwerte
      // zur Höhenbestimmung
      int maxTemperature = getMaxTemperature();
      int minTemperature = getMinTemperature();

      // Nutze i zum Temperaturvergleich und Balkenzeichnen.
      // Beginne mit höchster Temperatur (oberste Raute) bis
      // zur niedrigsten (unterster Balkenwert)
      for (int i = maxTemperature; i >= minTemperature; i = i - 1) {
        // Gehe alle Monate durch
        for (int j = 0; j < temperatures.length; j++) {
          // Wenn Temperatur über den Vergleichswert,
          // dann Balken zeichnen
          if (temperatures[j] >= i)
            print(" #");
            // Sonst nur Leerzeile zeichnen
          else
            print("  ");
        }
        // Nach Monatsvergleich Zeilenumbruch für
        // nächstniedrigere Temperaturstufe
        println();
      }
    }
  }

  // Methode zur Prüfung auf Vollzähligkeit der Werte
  // Als Ergebnis wird ein 'true' oder 'false' ausgegeben.
  private boolean isComplete() {
    // Prüfe, ob alle Monatswerte über dem
    // Initialwert -1000 liegen
    for (int i = 0; i < temperatures.length; i++) {
      if (temperatures[i] == -1000) {
        return false;
      }
    }
    return true;
  }

  // Methode zur Bestimmung und Rückgabe der maximalen
  // Temperatur
  private int getMaxTemperature() {
    int max = -1000;
    // Gehe alle Monate durch
    for (int i = 0; i < temperatures.length; i++) {
      // Liegt aktuelle Temperatur über dem aktuellen
      // Maximum, ist es das neue Maximum
      if (temperatures[i] > max) {
        max = temperatures[i];
      }
    }
    // Am Ende liegt das Maximum vor
    return max;
  }

  // Methode zur Bestimmung und Rückgabe der minimalen
  // Temperatur
  private int getMinTemperature() {
    // Wähle unrealistischen Startwert, der immer
    // unterboten werden kann
    int min = 1000;
    // Gehe alle Monate durch
    for (int i = 0; i < temperatures.length; i++) {
      // Liegt aktuelle Temperatur über dem aktuellen
      // Minimum, ist es das neue Minimum
      if (temperatures[i] < min) {
        min = temperatures[i];
      }
    }
    // Am Ende liegt das Minimum vor
    return min;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  // Erzeuge Temperaturanzeige
  TemperatureGraph tg = new TemperatureGraph(2017);

  // Füge Werte aus Beispiel hinzu
  tg.addTemperature(1, 2);
  tg.addTemperature(2, -3);
  tg.addTemperature(3, 7);
  tg.addTemperature(4, 8);
  tg.addTemperature(5, 14);
  tg.addTemperature(6, 16);
  tg.addTemperature(7, 17);
  tg.addTemperature(8, 18);
  tg.addTemperature(9, 14);
  tg.addTemperature(10, 9);
  tg.addTemperature(11, 5);
  tg.addTemperature(12, 2);

  // Zeichne Graphen
  tg.plotGraph();
}

