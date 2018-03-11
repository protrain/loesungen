// Basisklasse für alle Fahrzeuge
public class Fahrzeug {
  private float kmSatz;

  // Konstruktor, der vorgibt, dass ein
  // Kilometersatz angegeben werden muss
  public Fahrzeug(float kmSatz) {
    this.kmSatz = kmSatz;
  }

  // Getter zur Rückgabe des Kilometersatzes
  public float getKmSatz() {
    return kmSatz;
  }
}

// Klasse Fahrrad, die von der Klasse Fahrzeug erbt
public class Fahrrad extends Fahrzeug {
  // Rufe Superklasse auf und setze Fahrpreis auf 1,00 EUR fest
  public Fahrrad() {
    super(1.00f);
  }
}

public class Motorroller extends Fahrzeug {
  // Rufe Superklasse auf und setze Fahrpreis auf 2,00 EUR fest
  public Motorroller() {
    super(2.00f);
  }
}

public class Kleintransporter extends Fahrzeug {
  // Rufe Superklasse auf und setze Fahrpreis auf 5,50 EUR fest
  public Kleintransporter() {
    super(5.50);
  }
}


// Klasse, die eine Fahrt repräsentiert
public class Fahrt {
  private Fahrzeug fahrzeug;
  private float km;

  // Konstruktor, der die Angabe eines Fahrzeugs
  // und die gefahrenen Kilometer vorschreibt.
  public Fahrt(Fahrzeug fahrzeug, float km) {
    this.fahrzeug = fahrzeug;
    this.km = km;
  }

  // Methode zur Berechnung des Fahrpreises
  // (Kilometersatz * Kilometer)
  public float getPrice() {
    return fahrzeug.getKmSatz() * km;
  }
}


// Klasse, die ein Fahrtenbuch repräsentiert
public class Fahrtenbuch {
  private Fahrt[] fahrten;

  // Konstruktor, der die Fahrten initialisiert
  public Fahrtenbuch() {
    this.fahrten = new Fahrt[0];
  }

  // Öffentliche Methode zum Hinzufügen einer Fahrt,
  // die als Fahrtobjekt an die Methode übergeben wird
  public void addFahrt(Fahrt fahrt) {
    Fahrt[] fahrtenNew = new Fahrt[fahrten.length + 1];

    for (int i = 0; i < fahrten.length; i++) {
      fahrtenNew[i] = fahrten[i];
    }

    fahrtenNew[fahrtenNew.length - 1] = fahrt;
    fahrten = fahrtenNew;
  }

  // Getter-Methode, die den Preis zurückliefert
  public float getPrice() {
    // Gesamtpreis
    float price = 0.0f;

    // Gehe jede Fahrt durch
    for (int i = 0; i < fahrten.length; i++) {
      // Berechne Preis
      price = price + fahrten[i].getPrice();
    }

    return price;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  // Erstelle Fahrtenbuch
  Fahrtenbuch fb = new Fahrtenbuch();

  // Füge Fahrten hinzu
  fb.addFahrt(new Fahrt(new Fahrrad(), 3));
  fb.addFahrt(new Fahrt(new Motorroller(), 7.12));
  fb.addFahrt(new Fahrt(new Kleintransporter(), 56.11));

  // Berechne Gesamtpreis
  println(fb.getPrice());
}

