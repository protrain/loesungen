// Klasse zur Realisierung eines Tic-Tac-Toe-Spiels
public class TicTacToe {
  // Deklaration interner Variablen
  private int[] field;
  private int mark;

  // Konstruktor, der das Spielfeld initialisiert
  public TicTacToe() {
    field = new int[9];
    reset();
  }

  // Methode, die alle Felder eines Spielfelds
  // mit 0-Werten initialisiert.
  public void reset() {
    // Gehe alle Felder durch und lösche Inhalt
    for (int i = 0; i < field.length; i++) {
      field[i] = 0;
    }

    // Setze Startsymbol
    mark = 1;
  }

  // Methode zum Setzen einer Marke. Die Methode
  // erhält die x,y-Koordinate und setzt die Marke.
  // Wenn die Voraussetzungen dies ermöglichen, wird
  // 'true' zurückgegeben, ansonsten 'false'.
  public boolean setMark(int x, int y) {
    // nur gültige Spielfeldgrößen akzeptieren
    if (x < 0 || x > 2 || y < 0 || y > 2) {
      return false;
    }

    // Bestimme Position im Array
    int pos = 3 * y + x;

    // Feld schon belegt? Dann aus Funktion springen
    if (field[pos] > 0) {
      return false;
    }

    // Sonst setze Markierung an Position
    field[pos] = mark;

    // Setze neues Zeichen (O oder X)
    mark = (mark % 2) + 1;

    return true;
  }

  // Methode zum Generieren der Ausgabe des Spielfelds.
  // Die Methode bekommt keine Parameter übergeben und liefert
  // einen String mit der Repräsentation des Spielfelds zurück.
  public String toString() {
    String temp = "";

    // Gehe Spielfeld durch
    for (int i = 0; i < field.length; i++) {
      // Setze Symbol in Abhängigkeit vom Feldinhalt
      switch (field[i]) {
        case 0:
          temp = temp + " ";
          break;
        case 1:
          temp = temp + "X";
          break;
        case 2:
          temp = temp + "O";
          break;
        default:
          temp = temp + " ";
      }

      // Wenn aktuelle Feldnummer nicht durch 3
      // teilbar ist, Spalte malen
      if ((i + 1) % 3 != 0) {
        temp = temp + "|";
      }

      // nach drei Elementen neue Zeile malen
      if ((i + 1) % 3 == 0 && i < 6) {
        temp = temp + "\n";
        temp = temp + "-+-+-";
        temp = temp + "\n";
      }
    }

    // Gebe Spielfeld mit Zeilenumbruch zurück
    return temp = temp + "\n";
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  TicTacToe t = new TicTacToe();

  println(t);

  t.setMark(2, 2);
  println(t);

  t.setMark(2, 0);
  println(t);

  t.setMark(1, 1);
  println(t);
}

