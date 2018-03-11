// Klasse, die eine Zwischenablage repräsentiert
public class Clipboard {
  // Deklaration privater Variablen
  private String[] clipboard;
  private int position;

  // Konstruktor, der die internen Werte initialisiert
  // Um eine Instanz dieser Klasse erzeugen zu können, muss
  // die Größe angegeben werden.
  public Clipboard(int size) {
    // Initialisiere mit n Speicherplätzen
    this.clipboard = new String[size];
    // Aktuelle Schreibposition
    // Mit erster Erhöhung wird an Position 0 gestartet, daher -1
    this.position = -1;
  }

  // Öffentliche Methode zum Hinzufügen einer Zeichenkette
  // in die Zwischenablage. Die Zeichenkette wird an die
  // Methode übergeben.
  public void copy(String string) {
    // Wenn Schreibposition noch innerhalb der
    // Speichergröße
    if (position < clipboard.length - 1) {
      // Erhöhe Positionszähler
      position = position + 1;
      // Schreibe String an aktuelle Position
      clipboard[position] = string;
    }
    // Wenn keine freie Stelle gefunden
    else {
      // Lösche ältesten Eintrag (= erster Eintrag)
      clipboard[0] = null;
      // Kopiere die Einträge im Array um
      // gehe Einträge von 1 bis Ende durch
      for (int i = 1; i < clipboard.length; i++) {
        // Kopiere Eintrag eine Stelle nach vorne
        clipboard[i - 1] = clipboard[i];
      }
      // setze String ans Ende
      clipboard[position] = string;
    }
  }

  // Methode zum Einfügen (Rückgabe) des letzten Eintrags
  // aus der Zwischenablage. Die Methode benötigt keine
  // Parametereingabe und gibt den letzten Eintrag wieder
  // zurück.
  public String paste() {
    // Nehme Eintrag von letzter Schreibposition
    String string = clipboard[position];
    // Lösche Eintrag an der Stelle
    clipboard[position] = null;
    // Reduziere Zähler
    if (this.position > 0) {
      position = position - 1;
    }
    // Wenn negative Position, dann wieder zurücksetzen
    else {
      position = 0;
    }
    return string;
  }

  // Methode zur Ausgabe der aktuellen Zwischenablage
  public String toString() {
    String output = "[";
    int i = 0;
    for (; i < clipboard.length - 1; i++) {
      output = output + clipboard[i] + ", ";
    }
    output = output + clipboard[i] + "]";
    return output;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  Clipboard cb = new Clipboard(2);

  // Schreibe in Zwischenablage absichtlich mehr Inhalt als möglich
  cb.copy("Hallo");
  cb.copy("Wie");
  cb.copy("Geht");
  cb.copy("Es");

  // Leere Zwischenablageninhalt
  println(cb.paste());
  println(cb.paste());
  println(cb.paste());
  println(cb.paste());

  println(cb);
}

