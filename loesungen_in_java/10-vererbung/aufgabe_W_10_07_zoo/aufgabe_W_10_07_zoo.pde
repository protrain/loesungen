// Klasse, die einen Besucher repräsentiert
public class Visitor {
  // Deklaration privater Variablen
  private double prize;

  // Konstruktor, der die Angabe eines Preises
  // erforderlich macht
  public Visitor(double prize) {
    this.prize = prize;
  }

  // Getter-Methode zur Abfrage des Preises
  public double getPrize() {
    return prize;
  }

  // Getter-Methode zur Rückgabe der Anzahl von Personen
  public int getCount() {
    return 0;
  }
}

// Öffentliche Klasse, die eine Personengruppe repräsentiert
// und von der Klasse Visitor erbt
public class Group extends Visitor {
  // Deklaration privater Variablen
  private int size;

  // Konstruktor mit der Angabe der Gruppengröße
  public Group(int size) {
    // Aufruf der Basisklasse
    super(50.0);

    // Speichern der Gruppengröße lokal
    this.size = size;
  }

  // Getter-Methode zur Rückgabe der Gruppengröße
  public int getCount() {
    return size;
  }
}

// Öffentliche Klasse, die ein Kind repräsentiert
// und von der Klasse Visitor erbt
public class Child extends Visitor {
  public Child() {
    // Aufruf der Basisklasse
    super(0.0);
  }

  // Getter-Methode zur Rückgabe der Gruppengröße
  public int getCount() {
    return 1;
  }
}


// Öffentliche Klasse, die einen Erwachsenen repräsentiert
// und von der Klasse Visitor erbt
public class Adult extends Visitor {
  public Adult() {
    // Aufruf der Basisklasse
    super(15.0);
  }

  // Getter-Methode zur Rückgabe der Gruppengröße
  public int getCount() {
    return 1;
  }
}

// Öffentliche Klasse, die den Eingang repräsentiert
public class Entrance {
  // Deklaration privater Variablen
  private Visitor[] visitors;
  private int visitorCount;

  // Öffentlicher Konstruktor, der die Gesamtzahl an
  // Gästen erwartet.
  public Entrance(int size) {
    visitors = new Visitor[size];
  }

  // Methode zum Hinzufügen von Besucher(n) vom
  // Typ 'Visitor'. Instanzen aller von Visitor abgeleiteten
  // Klassen können hier übergeben werden.
  public void addVisitor(Visitor v) {
    visitors[visitorCount++] = v;
  }

  // Methode zur Ermittlung der gesamten Einnahmen
  public double computeTurnover() {
    double to = 0.0;

    // Gehe jeden Besucher durch
    for (int i = 0; i < visitorCount; i = i + 1) {
      // Addiere Preis von Besucher zum Gesamtpreis
      to = to + visitors[i].getPrize();
    }

    return to;
  }

  // Methode, die die Gesamtzahl an Besuchern bestimmt
  // sowie zurückliefert.
  public int computeVisitors() {
    int v = 0;

    // Gehe jeden Besucher durch
    for (int i = 0; i < visitorCount; i = i + 1) {
      // Addiere Besucheranzahl zur Gesamtzahl
      v = v + visitors[i].getCount();
    }

    return v;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  Entrance entrance = new Entrance(100);
  entrance.addVisitor(new Group(6));
  entrance.addVisitor(new Adult());
  entrance.addVisitor(new Child());
  entrance.addVisitor(new Child());

  println("Besucher: " + entrance.computeVisitors());
  println("Umsatz: " + entrance.computeTurnover() + " Euro");
}
