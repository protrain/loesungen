// Öffentliche Klasse zur Repräsentation eines Bruchs
public class Fraction {
  // Deklaration interner Variablen
  private int numerator;
  private int denominator;

  // Konstruktor, der Zähler und Nenner eines Bruchs
  // anfordert
  public Fraction(int numerator, int denominator) {
    this.numerator = numerator;
    this.denominator = denominator;
  }

  // Öffentliche Methode zum Addieren eines Bruchs.
  // Zum aktuellen Bruch wird der an die Methode über-
  // gebene Bruch addiert und als eigenständiges Objekt
  // zurückgegeben.
  public Fraction add(Fraction f) {
    int z1 = numerator * f.getDenominator();
    int z2 = denominator * f.getNumerator();
    return new Fraction(z1 + z2, denominator * f.getDenominator());
  }

  // Öffentliche Methode zum Multiplizieren eines Bruchs.
  // Der aktuelle Bruch wird mit dem an die Methode über-
  // gebenen Bruch multipliziert und als eigenständiges
  // Objekt zurückgegeben.
  public Fraction multiply(Fraction f) {
    return new Fraction(
      numerator * f.getNumerator(),
      denominator * f.getDenominator()
    );
  }

  // Öffentliche Methode, die den Zähler zurückliefert
  public int getNumerator() {
    return numerator;
  }

  // Öffentliche Methode, die den Nenner zurückliefert
  public int getDenominator() {
    return denominator;
  }

  // Öffentliche Methode zur Ausgabe eines Bruchs
  public String toString() {
    return numerator + "/" + denominator;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  // 1/2
  Fraction f1 = new Fraction(1, 2);

  // 1/4
  Fraction f2 = new Fraction(1, 4);

  // 1/2 + 1/4 = 6/8
  Fraction sum = f1.add(f2);
  println(f1 + " + " + f2 + " = " + sum);

  // 1/2 + 1/4 = 1/8
  Fraction mult = f1.multiply(f2);
  println(f1 + " * " + f2 + " = " + mult);
}

