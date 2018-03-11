// Klasse, die den Schrittzähler realisiert
public class StepCounter {
  // private Variablen deklarieren
  private String date;
  private int steps;

  // Initialisierung
  // Alle Instanzvariablen werden im Konstruktor initialisiert
  // Die Klasse kann nur mit der Angabe eines Schrittzählers initialisiert
  // werden, wenn es sich bei diesem Konstruktor NICHT um einen Standardkonstruktor
  // handelt
  public StepCounter(String date) {
    this.date = date;
    this.steps = 0;
  }

  // Öffentliche Methode, um den Schrittzähler um 1 zu erhöhen
  public void incrementSteps() {
    this.steps = this.steps + 1;
  }

  // Öffentliche Methode zur Erzeugung einer Statusnachricht, die
  // zurückgegeben wird
  public String toString() {
    return "Am " + this.date + " bin ich " + this.steps + 
      " Schritte gegangen";
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  // Objekt der Klasse StepCounter durch Konstruktoraufruf erzeugen
  // Das Datum wird auf den 11.11.2011 gesetzt
  StepCounter sc = new StepCounter("11.11.2011");

  // Gehe 1111 Schritte
  for (int i = 0; i < 1111; i++) {
    sc.incrementSteps();
  }

  // Gebe Schritte aus
  println(sc);
}

