// Öffentliche Klasse, die das Spiel Mastermind realisiert
public class Mastermind {
  // Konstanten für Farbcodes
  public static final int RED = 0;
  public static final int GREEN = 1;
  public static final int BLUE = 2;
  public static final int WHITE = 3;
  public static final int ORANGE = 4;
  public static final int GREY = 5;

  // Deklaration der internen Variablen
  private int[] code;
  private int numMove;

  // Öffentlicher Konstruktor, der den aktuellen Farbcode
  // als Übergabeparameter erwartet
  public Mastermind(int c1, int c2, int c3, int c4) {
    // Initialisiere Array
    this.code = new int[4];

    // Setze Farben
    code[0] = c1;
    code[1] = c2;
    code[2] = c3;
    code[3] = c4;

    // Initialisiere Zähler der Spielzüge
    this.numMove = 0;
  }

  // Private Methode, die berechnet, wie viele richtige Farben
  // an den richtigen Positionen liegen. Die Farben werden
  // in der entsprechenden Reihenfolge ausgewertet. Die Anzahl
  // der korrekten Farben an den Positionen wird zurückgeliefert.
  private int correctColorsAndPositions(int[] colors) {
    // Anzahl richtiger Farben und Positionen
    int count = 0;
    for (int i = 0; i < code.length; i++) {
      if (code[i] == colors[i]) {
        count = count + 1;
      }
    }

    return count;
  }

  // Private Methode, die berechnet, wie viele Farben korrekt
  // angegeben wurden. Dazu werden die angegebenen Farben
  // auf ihr Vorkommen geprüft und das Ergebnis zurückgeliefert.
  private int correctColors(int[] colors) {
    // Anzahl richtiger Farben, die an falscher
    // Position stehen
    int count = 0;

    // Bereits geprüfte Positionen des Codes
    boolean[] checked = { false, false, false, false };

    // Hake zunächst alle Farben ab, die die richtige Farbe und
    // Position haben
    for (int i = 0; i < code.length; i++) {
      // Wenn an identischer Position
      if (code[i] == colors[i]) {
        // Position als geprüft abhaken
        checked[i] = true;
      }
    }

    // Zähle jetzt alle Farben
    // Gehe jede Codenummer durch
    for (int i = 0; i < code.length; i++) {
      for (int j = 0; j < colors.length; j++) {
        // Wenn Position mit gleicher Farbe gefunden, die noch
        // nicht abgehakt ist, dann zählen (und abhaken)
        if (code[i] == colors[j] && checked[j] == false) {
          checked[j] = true;
          count = count + 1;
          // Aus Schleife springen
          break;
        }
      }
    }

    return count;
  }

  // Öffentliche Methode, die den Spielzug entgegennimmt und
  // auswertet. Als Elemente eines zweidimensionalen Arrays
  // werden die korrekten Farbpositionen und die Anzahl der
  // korrekten Farben zurückgeliefert.
  public int[] guess(int c1, int c2, int c3, int c4) {
    int[] output = new int[2];
    // Baue Spielzug zu Array um
    int[] colors = { c1, c2, c3, c4 };

    // Werte private Methoden für Spielzug aus
    output[0] = correctColorsAndPositions(colors);
    output[1] = correctColors(colors);

    // Erhöhe Spielzugzähler
    numMove = numMove + 1;
    return output;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  Mastermind mm = new Mastermind(
    Mastermind.RED,
    Mastermind.BLUE,
    Mastermind.GREY,
    Mastermind.BLUE
  );

  int[] guess = mm.guess(
    Mastermind.GREEN,
    Mastermind.GREY,
    Mastermind.BLUE,
    Mastermind.BLUE
  );

  println("correctColorsAndPositions: \t" + guess[0]);
  println("correctColors: \t\t" + guess[1]);
}

