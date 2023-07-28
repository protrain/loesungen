// Klasse, die das Quiz realisiert
public class MultiplicationQuiz {
  // private Variablen deklarieren
  private int a, b;

  // Konstruktor der Klasse
  public MultiplicationQuiz() {
    // Initialisiere Zahlen für Multiplikation
    this.a = 0;
    this.b = 0;
  }

  // Generiert neue Aufgabe
  public String getExercise() {
    // Generiere zufällige Zahlen für Multiplikation
    a = int(random(1, 20));
    b = int(random(1, 20));

    // Gebe String mit Aufgabe zurück
    return a + " * " + b + " = ?";
  }

  // Gebe Ergebnis zurück
  public int getResult() {
    return a * b;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  // Testfunktion
  MultiplicationQuiz quiz = new MultiplicationQuiz();
  println(quiz.getExercise());
  println("Result: " + quiz.getResult());

  println(quiz.getExercise());
  println("Result: " + quiz.getResult());
}

