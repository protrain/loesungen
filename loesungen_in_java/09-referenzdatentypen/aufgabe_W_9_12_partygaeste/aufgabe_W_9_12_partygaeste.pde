// Öffentliche Klasse zur Repräsentation einer Partyverwaltung
public class PartyInvitation {
  // Deklaration privater Variablen
  private String[] invitations;
  private String[] coming;
  private String[] notComing;

  // Öffentlicher Konstruktor, der vorschreibt, dass Instanzen
  // dieser Klasse nur mit Angabe der Einladungen erfolgen können.
  public PartyInvitation(String[] invitations) {
    this.invitations = invitations;
    this.coming = new String[0];
    this.notComing = new String[0];
  }

  // Öffentliche Methode, die die Teilnahme einer eingeladenen
  // Person vermerkt. Der Name der eingeladenen Person wird
  // an die Funktion übergeben.
  public void coming(String name) {
    // Wenn die Person unter den eingeladenen Personen
    // gefunden wird,
    if (findAndRemove(invitations, name)) {
      // vergrößere das Teilnehmer-Array, speichere
      // diesen Gast als Teilnehmer und ersetze die bisherige
      // Liste durch die um den gerade zugesagten Teilnehmer
      // erweiterte Liste
      coming = growAndAdd(coming, name);
    }
  }

  // Öffentliche Methode, die die Nichtteilnahme einer
  // eingeladenen Person vermerkt. Der Name der eingeladenen
  // Person wird an die Funktion übergeben.
  public void notComing(String name) {
    // Wenn die Person unter den eingeladenen Personen
    // gefunden wird,
    if (findAndRemove(this.invitations, name)) {
      // vergrößere das Nichtteilnehmer-Array, speichere
      // diesen Gast als Nichtteilnehmer und ersetze die
      // bisherige Liste durch die um den gerade zugesagten
      // Teilnehmer erweiterten Liste
      notComing = growAndAdd(notComing, name);
    }
  }

  // Öffentliche Methode, die die Anzahl der Teilnehmer
  // zurückliefert.
  public int numberOfComingGuests() {
    return coming.length;
  }

  // Öffentliche Methode, die die Anzahl der Absager
  // zurückliefert.
  public int numberOfNotComingGuests() {
    return notComing.length;
  }

  // Private Methode, die das übergebene Array um einen Teilnehmer
  // vergrößert und die an die Methode übergebene Person
  // dieser Liste hinzufügt.
  private String[] growAndAdd(String[] arrayIn, String item) {
    String[] arrayOut = new String[arrayIn.length + 1];

    // Kopiere Elemente rüber
    for (int i = 0; i < arrayIn.length; i++) {
      arrayOut[i] = arrayIn[i];
    }

    // Setze neues Element
    arrayOut[arrayOut.length - 1] = item;

    return arrayOut;
  }

  // Private Methode, die in der übergebenen Liste nach dem
  // ebenfalls übergebenen Namen sucht und zurückliefert, ob
  // der Name in der Liste gefunden wurde.
  private boolean findAndRemove(String[] liste, String item) {
    // Gehe Liste durch
    for (int i = 0; i < liste.length; i++) {
      // Wenn Inhalt mit Erwartung übereinstimmt,
      // setze auf null
      if (liste[i] != null && liste[i].equals(item)) {
        liste[i] = null;
        return true;
      }
    }

    // Wenn nichts gefunden, dann false zurückgeben
    return false;
  }

  // Öffentliche Testfunktion, um Array-Inhalt zu testen
  public String[] getInvitationsArray() {
    return this.invitations;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  String[] gaesteliste = {
    "Hinz",
    "Kunz",
    "Dirty",
    "Harry"
  };
  PartyInvitation invitations = new PartyInvitation(gaesteliste);

  // Hinz und Kunz kommen
  invitations.coming("Hinz");
  invitations.coming("Kunz");

  // Harry kommt nicht
  invitations.notComing("Harry");

  // Gebe kommende und nicht kommende Gäste aus
  println(invitations.numberOfComingGuests());
  println(invitations.numberOfNotComingGuests());

  // Kontrolle, ob wirklich alle Elemente außer Dirty
  // mit null ersetzt wurden
  println(invitations.getInvitationsArray());
}

