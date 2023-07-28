// Öffentliche Klasse, die einen Punkt im Koordinatensystem
// repräsentiert
public class Point {
  // Deklaration privater Variablen
  private int x;
  private int y;

  // Konstruktor, der die Angabe von x und y bei der Objekt-
  // generierung vorschreibt.
  public Point(int x, int y) {
    this.x = x;
    this.y = y;
  }

  // Getter-Methode zur Rückgabe des X-Werts
  public int getX() {
    return x;
  }

  // Getter-Methode zur Rückgabe des Y-Werts
  public int getY() {
    return y;
  }
}


// Öffentliche Klasse, die einen Polygonzug repräsentiert
public class PolyLine {
  // Deklaration privater Variablen
  private Point[] points;
  private int nextFree;

  // Öffentlicher Konstruktor, der bei der Objekterzeugung
  // zur Angabe der Größe des Polygonzugs benötigt wird
  public PolyLine(int size) {
    points = new Point[size];
    nextFree = 0;
  }

  // Öffentliche Methode zum Hinzufügen eines weiteren
  // Punkts in Form eines x- und  y-Werts
  public void append(int x, int y) {
    if (nextFree < points.length) {
      points[nextFree] = new Point(x, y);
      nextFree = nextFree + 1;
    }
  }

  // Öffentliche Methode zum Hinzufügen eines weiteren
  // Punkts, der durch ein Point-Objekt repräsentiert
  // wird
  public void append(Point p) {
    append(p.getX(), p.getY());
  }

  // Öffentliche Methode, die den Polygonzug in einem
  // String repräsentiert. Der erzeugte String wird
  // am Ende der Funktion zurückgegeben.
  public String toString() {
    String temp = "{ ";

    for (int i = 0; i < nextFree; i++) {
      temp = temp + "(" + points[i].getX() + "," + points[i].getY() + ")";
    }

    return temp + " }";
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  // Neuen Polygonzug erzeugen
  PolyLine poly = new PolyLine(3);
  println(poly);

  // Füge Punkt hinzu
  poly.append(2, 4);
  println(poly);

  // Füge Punkt hinzu (andere Methode)
  poly.append(new Point(10, 5));
  poly.append(4, 4);
  println(poly);

  // Füge ein Element zu viel hinzu
  poly.append(1, 1);
  println(poly);
}

