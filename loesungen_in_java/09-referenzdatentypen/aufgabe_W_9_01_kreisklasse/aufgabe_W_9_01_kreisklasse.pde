// Öffentliche Klasse zur Repräsentation eines Kreises
public class Circle {
  // Deklaration privater Variablen
  private Coordinate position;
  private int radius;

  // Konstruktor, der die Position im Koordinatensystem
  // sowie den Radius erwartet
  public Circle(int x, int y, int radius) {
    // Die Position wird als Koordinate gespeichert.
    this.position = new Coordinate(x, y);
    this.radius = radius;
  }

  // Öffentliche Methode zur Berechnung des Flächeninhalts
  public float area() {
    // PI*r^2
    return PI * radius * radius;
  }

  // Methode zur Ausgabe
  public void toConsole() {
    float area = this.area();
    println(
      "Ich stehe bei " + this.position + " und bin " + area + " gross."
    );
  }
}

// Interne Klasse zur Repräsentation einer Koordinate
class Coordinate {
  // Deklaration interner Variablen
  private int x;
  private int y;

  // Konstruktor, der die Angabe von x- und y-Werten
  // übernimmt und intern speichert
  public Coordinate(int x, int y) {
    this.x = x;
    this.y = y;
  }

  // Öffentliche Methode zur Rückgabe einer generierten
  // Koordinatenangabe
  public String toString() {
    return "(" + x + ", " + y + ")";
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  // Testfunktion
  Circle kreis = new Circle(10, 43, 4);
  kreis.toConsole();
}

