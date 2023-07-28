// Klasse, die einen digitalen Bilderrahmen darstellt
public class DigitalPictureFrame {
  // Deklaration privater Variablen
  private Picture[] pics;
  private int amount;
  private int current;

  // Konstruktor, der dafür sorgt, dass ein Objekt dieses
  // Typs (Klasse) nur mit der Angabe der maximal zu
  // verwaltenden Bilder erzeugt werden kann.
  public DigitalPictureFrame(int size) {
    // Initialisierung
    pics = new Picture[size];
    amount = 0;
    current = 0;
  }

  // Öffentliche Methode zum Hinzufügen eines neuen Bilds.
  // Das Bild wird der Methode übergeben.
  public void addPicture(Picture pic) {
    // Sind noch Speicherplätze frei, dann hinzufügen
    if (amount < pics.length) {
      pics[amount] = pic;

      // Erhöhe Zähler
      amount = amount + 1;
    }
  }

  // Methode zum Löschen eines Bilds aus dem Bilderrahmen.
  // Der Index des Bilds im Rahmen wird der Methode über-
  // geben.
  public void deletePicture(int index) {
    // Nur arbeiten, wenn angegebener Index im
    // gültigen Bereich
    if (index >= 0 && index <= amount) {
      // Kopiere nachfolgende Bilder nach vorne
      for (int i = index; i < amount - 1; i++) {
        pics[i] = pics[i + 1];
      }
      // Reduziere Zähler, da Bild gelöscht
      amount = amount - 1;
    }
  }

  // Öffentliche Methode zum Abholen des nächsten Bilds
  public Picture getNext() {
    int pos = current;

    // Sorge mit Modulo dafür, dass maximale Anzahl nicht über-
    // schritten werden kann (erspart if-else-Anweisungen)
    current = (current + 1) % amount;
    return pics[pos];
  }

  // Öffentliche Methode, die ein Zufallsbild aus der
  // Menge der im Rahmen enthaltenen Bilder auswählt
  // und zurückliefert.
  public Picture getNextRandom() {
    return pics[(int)(Math.random() * amount)];
  }
}

// Öffentliche Klasse Picture, die ein Bild repräsentiert.
public class Picture {
  // Deklaration privater Variable
  private String name;

  // Konstruktor, der erzwingt, dass bei der Objektgenerierung
  // der Name des Bilds angegeben werden muss.
  public Picture(String name) {
    this.name = name;
  }

  // Öffentliche Methode, die einen String (in diesem Fall
  // den intern gespeicherten Namen) zurückliefert.
  public String toString() {
    return this.name;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  DigitalPictureFrame dpf = new DigitalPictureFrame(3);
  dpf.addPicture(new Picture("Bild 1"));
  dpf.addPicture(new Picture("Bild 2"));
  dpf.addPicture(new Picture("Bild 3"));

  // Gebe alle Bilder aus
  println(dpf.getNext());
  println(dpf.getNext());
  println(dpf.getNext());
  println();
  println(dpf.getNextRandom());
  dpf.deletePicture(3);

  // Hier darf kein Bild 3 auftauchen
  println(dpf.getNextRandom());
}

