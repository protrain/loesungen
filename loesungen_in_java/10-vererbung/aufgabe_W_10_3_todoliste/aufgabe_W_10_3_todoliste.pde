// Öffentliche Klasse zur Repräsentation eines Listeneintrags
public class ListItem {
  // Deklaration privater Variablen
  private String entry;
  private boolean checked;

  // Öffentlicher Konstruktor, der einen Eintrag als String
  // erwartet und als nicht überprüft voreinstellt.
  public ListItem(String entry) {
    this.entry = entry;
    this.checked = false;
  }

  // Getter-Methode zur Abfrage des Entry-Strings
  public String getEntry() {
    return entry;
  }

  // Getter-Methode zur Abfrage des Überprüfungsstatus
  public boolean getChecked() {
    return checked;
  }

  // Setter-Methode mit dem Status als Parameter
  public void setChecked(boolean checked) {
    this.checked = checked;
  }

  // Öffentliche Methode zur Repräsentation eines
  // beschreibenden ListItem
  public String toString() {
    return getEntry() + " (" + getChecked() + ")";
  }
}


// Öffentliche Klasse zur Verwaltung einer To-do-Liste
public class TodoList {
  // Deklaration privater Variablen
  private ListItem[] list;

  // Öffentlicher Konstruktor mit der Initialisierung
  // der internen Liste.
  public TodoList() {
    this.list = new ListItem[0];
  }

  // Öffentliche Methode zum Hinzufügen eines neuen
  // ListItems-Objekts.
  public void addItem(ListItem item) {
    // Array vergrößern
    ListItem[] listNew = new ListItem[list.length + 1];

    // Elemente kopieren
    for (int i = 0; i < list.length; i++) {
      listNew[i] = list[i];
    }

    // letztes Element setzen
    listNew[listNew.length - 1] = item;

    // Liste übernehmen
    this.list = listNew;
  }

  // Öffentliche Methode zum Setzen des Status eines
  // Listeneintrags
  public void checkItem(String entry) {
    // Gehe Liste durch
    for (int i = 0; i < list.length; i++) {
      // Wenn Eintrag mit Gesuchtem übereinstimmt, dann abhaken.
      if (list[i].getEntry().equals(entry)) {
        list[i].setChecked(true);

        // Springe aus Schleife
        break;
      }
    }
  }

  // Methode zur Repräsentation aller Einträge in der
  // To-do-Liste. Das Ergebnis wird von der Methode zurück-
  // gegeben.
  public String toString() {
    // Rückgabestring
    String output = "";

    // Gehe jedes Element durch
    for (int i = 0; i < list.length; i++) {
      // Packe toString-Methode in Rückgabe
      // und füge Zeilenumbruch hinzu
      output = output + list[i].toString() + "\n";
    }
    return output;
  }
}

// Öffentliche Klasse zur Repräsentation eines Einkaufslisten-
// eintrags. Hierzu wird von der Klasse ListItem abgeleitet und
// die für einen Einkaufslisteneintrag charakterisierenden Merkmale
// hinzugefügt.
public class ShoppingItem extends ListItem {
  // Deklaration privater Variablen
  private String entry;
  private int amount;

  // Öffentlicher Konstruktor, der einen Eintrag als String sowie
  // die Menge dieses Eintrags verlangt
  public ShoppingItem(String entry, int amount) {
    // Aufruf des Basisklassenkonstruktors
    super(entry);

    // zusätzlich wird noch die Menge festgehalten
    this.amount = amount;
  }

  // Öffentliche Methode zur Repräsentation eines
  // aussagekräftigen Strings für einen Einkaufslisteneintrag
  public String toString() {
    // rufe toString-Methode der Superklasse auf
    return amount + "x " + getEntry() + " (" + getChecked() + ")";
  }
}

// Klasse zur Verwaltung einer Shoppingliste
public class ShoppingList {
  // Deklaration der privaten Variablen
  private ListItem[] list;

  // Öffentlicher Konstruktor, der die Liste initialisiert
  public ShoppingList() {
    this.list = new ListItem[0];
  }

  // Öffentliche Methode, die einen Listeneintrag in Form
  // eines ListItem-Objekts entgegennimmt, um diesen dann
  // in die Einkaufsliste zu setzen
  public void addItem(ListItem item) {
    // Array vergrößern
    ListItem[] listNew = new ListItem[list.length + 1];

    // Elemente kopieren
    for (int i = 0; i < list.length; i++) {
      listNew[i] = list[i];
    }

    // letztes Element setzen
    listNew[listNew.length - 1] = item;

    // Liste übernehmen
    this.list = listNew;
  }

  // Öffentliche Methode zum Setzen des Status eines
  // Eintrags, der an die Methode übergeben wird.
  public void checkItem(String entry) {
    // Gehe Liste durch
    for (int i = 0; i < list.length; i++) {
      // Wenn Eintrag mit Gesuchtem übereinstimmt,
      // dann abhaken
      if (list[i].getEntry().equals(entry)) {
        list[i].setChecked(true);

        // Springe aus Schleife
        break;
      }
    }
  }

  // Öffentliche Methode zur Repräsentation der Shoppingliste.
  public String toString() {
    // Rückgabestring
    String output = "";

    // gehe jedes Element durch
    for (int i = 0; i < list.length; i++) {
      // Packe toString Methode in Rückgabe
      // und füge Zeilenumbruch hinzu
      output = output + list[i].toString() + "\n";
    }
    return output;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  TodoList tdl = new TodoList();
  tdl.addItem(new ListItem("Erster Eintrag"));
  tdl.addItem(new ListItem("Zweiter Eintrag"));
  tdl.checkItem("Zweiter Eintrag");
  println(tdl);

  ShoppingList sl = new ShoppingList();
  sl.addItem(new ShoppingItem("Aepfel", 3));
  sl.addItem(new ShoppingItem("Birnen", 1));
  sl.addItem(new ShoppingItem("Toastbrot", 2));
  sl.addItem(new ShoppingItem("Birnenbaum", 2));
  println(sl);
  sl.checkItem("Birnen");
  println(sl);
}

