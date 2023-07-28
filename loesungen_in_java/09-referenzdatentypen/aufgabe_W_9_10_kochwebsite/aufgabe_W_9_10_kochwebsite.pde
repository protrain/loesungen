// Öffentliche Klasse für die Repräsentation einer Zutat
public class Zutat {
  // Deklaration privater Variablen
  private String name;
  private int menge;
  private String einheit;

  // Konstruktor, der die Angabe der Zutat, Menge und Einheit
  // erwartet
  public Zutat(String name, int menge, String einheit) {
    this.name = name;
    this.menge = menge;
    this.einheit = einheit;
  }

  // Öffentliche Methode zur Generierung eines geeigneten
  // Strings zur Repräsentation der Zutat
  public String toString() {
    return menge + einheit + " " + name;
  }
}

// Öffentliche Klasse für die Repräsentation einer
// Koch-Anweisung
public class Anweisung {
  // Deklaration privater Variablen
  private String text;
  private int position;

  // Öffentlicher Konstruktor, der regelt, dass eine Instanz
  // dieser Klasse nur unter Angabe des Anweisungstexts und
  // der Positionsnummer angelegt werden kann.
  public Anweisung(String text, int position) {
    this.text = text;
    this.position = position;
  }

  // Öffentliche Methode zur Generierung eines geeigneten
  // Strings zur Ausgabe
  public String toString() {
    return position + ". " + text;
  }
}

// Öffentliche Klasse für ein ganzes Rezept
public class Kochrezept {
  // Deklaration interner Variablen
  private String name;
  private int zeit;
  private Anweisung[] anweisungen;
  private Zutat[] zutaten;
  private String anweisungHerd;

  // Öffentlicher Konstruktor. Ein Objekt der Klasse kann
  // nur dann instanziiert werden, wenn der Name, die
  // vermeintliche Zeit, die Zutaten, Anweisungen und eine
  // generelle Herdanweisung angegeben werden.
  public Kochrezept(
    String name,
    int zeit,
    Zutat[] zutaten,
    Anweisung[] anweisungen,
    String anweisungHerd
  ) {
    this.name = name;
    this.zeit = zeit;
    this.anweisungen = anweisungen;
    this.zutaten = zutaten;
    this.anweisungHerd = anweisungHerd;
  }

  // Öffentliche Methode zum Generieren eines repräsentativen
  // Strings für das Kochrezept
  public String toString() {
    String output = "";
    output = output + "- " + name + " (" + zeit + " Minuten) -\n";
    output = output + "\nZutaten:\n";

    // Alle Zutaten durchgehen
    for (int i = 0; i < zutaten.length; i++) {
      output = output + "- " + zutaten[i].toString() + "\n";
    }

    output = output + "\nZubereitung:\n";

    // Alle Anweisungen durchgehen
    for (int i = 0; i < anweisungen.length; i++) {
      output = output + anweisungen[i].toString() + "\n";
    }

    output = output + (anweisungen.length + 1) + ". " +
        anweisungHerd;

    return output;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  Zutat[] zutaten = new Zutat[6];
  zutaten[0] = new Zutat("Kartoffelmehl", 80, "g");
  zutaten[1] = new Zutat("Maisstärke", 80, "g");
  zutaten[2] = new Zutat("Eier", 3, "");
  zutaten[3] = new Zutat("Milch", 400, "ml");
  zutaten[4] = new Zutat("Traubenzucker", 5, "EL");
  zutaten[5] = new Zutat("Pflanzenöl", 5, "EL");

  Anweisung[] anweisungen = new Anweisung[5];
  anweisungen[0] = new Anweisung("Die Mehle vermischen und sieben.", 1);
  anweisungen[1] = new Anweisung("Eier, Zucker und Milch dazugeben.", 2);
  anweisungen[2] = new Anweisung(
    "Alles mit dem Schneebesen gut verquirlen.",
    3
  );
  anweisungen[3] = new Anweisung("10 Minuten quellen lassen.", 4);
  anweisungen[4] = new Anweisung("Noch einmal verrühren.", 5);

  String anweisungHerd = "Pfanne auf hoher Stufe erhitzen und Teig " +
    "portionsweise im heißen Öl ausbacken.";

  Kochrezept pfannkuchen = new Kochrezept(
    "Pfannkuchen",
    30,
    zutaten,
    anweisungen,
    anweisungHerd
  );

  println(pfannkuchen);
}

