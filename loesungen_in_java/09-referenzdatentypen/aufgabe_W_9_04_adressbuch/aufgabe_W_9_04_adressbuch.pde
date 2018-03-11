// Klasse zur Repräsentation eines Kontakts
public class Contact {
  // Deklaration interner Variablen
  private int id;
  private String name;
  private String email;
  private String phone;
  private String twitter;

  // Konstruktor der zur Initialisierung der Klassen-
  // variablen die Id, Name, E-Mail-Adresse, Telefonnummer
  // und Twitter-Adresse vorschreibt.
  public Contact(
    int id,
    String name,
    String email,
    String phone,
    String twitter
  ) {
    this.name = name;
    this.email = email;
    this.phone = phone;
    this.twitter = twitter;
    this.id = id;
  }

  // Öffentliche Methode zur Generierung eines
  // Strings mit den Kontaktdaten. Der generierte String
  // wird von der Methode zurückgeliefert.
  public String toString() {
    return id + " { " + name + "\t" + email + "\t" + phone + "\t" +
        twitter;
  }

  // Öffentliche Methode zur Rückgabe des Namens
  public String getName() {
    return name;
  }

  // Öffentliche Methode zur Rückgabe der Id
  public int getID() {
    return id;
  }
}


// Öffentliche Klasse, die ein Adressbuch realisiert
public class Adressbook {
  // Deklaration interner Variablen
  private String name;
  private Contact[] contacts;

  // Konstruktor, der für die Instanziierung den
  // Namen erfordert.
  public Adressbook(String name) {
    this.name = name;
    this.contacts = new Contact[0];
  }

  // Öffentliche Methode zur Generierung eines Strings
  // mit allen Adressbucheinträgen. Der String wird von
  // der Methode zurückgeliefert.
  public String showAll() {
    String output = "Adressbuch { " + name + "\n";

    // Gehe jeden Kontakt durch
    for (int i = 0; i < contacts.length; i++) {
      // Schreibe Inhalt der toString-Methode in
      // Ausgabe-Variable mit Zeilenumbruch
      output = output + contacts[i].toString() + "\n";
    }
    return output;
  }

  // Öffentliche Methode zur Suche und Rückgabe des
  // Kontakts. Der Name der zu suchenden Person
  // wird an die Methode übergeben. Der generierte
  // String des Kontakts wird im Erfolgsfall zurück-
  // geliefert, ansonsten ein leerer String.
  public String showByName(String name) {
    // Gehe Kontaktliste durch und suche den Namen
    for (int i = 0; i < contacts.length; i++) {
      // Stimmt der Name überein
      if (contacts[i].getName() == name) {
        // Gebe den Eintrag als String zurück und
        // springe aus Funktion
        return contacts[i].toString();
      }
    }
    return "";
  }

  // Öffentliche Methode zum Hinzufügen eines Kontakts.
  // Der Kontakt muss als Contact-Objekt an die Methode
  // übergeben werden.
  public void addContact(Contact contact) {
    // Vergrößertes Array anlegen
    Contact[] contactsNew = new Contact[contacts.length + 1];
    // Elemente kopieren
    for (int i = 0; i < contacts.length; i++) {
      contactsNew[i] = contacts[i];
    }
    // Neues Element hinzufügen
    contactsNew[contactsNew.length - 1] = contact;
    // Neues Array übernehmen
    contacts = contactsNew;
  }

  // Öffentliche Methode zum Suchen eines Kontakts nach
  // der Id. Diese muss an die Funktion übergeben werden.
  // Der Kontakt wird im Erfolgsfall zurückgeliefert -
  // ansonsten wird null zurückgeliefert.
  public Contact getContact(int id) {
    // Gehe Kontaktliste durch und suche die ID
    for (int i = 0; i < contacts.length; i++) {
      // Stimmt die ID überein
      if (contacts[i].getID() == id) {
        // Gebe den Eintrag zurück und
        // springe aus Funktion
        return contacts[i];
      }
    }
    return null;
  }

  // Methode zum Entfernen eines Kontakts aus dem Adressbuch.
  // An die Methode muss die eindeutige Id übergeben werden.
  public void removeContact(int id) {
    // Lege Rückgabeliste an
    Contact[] contactsCopy = new Contact[0];
    // Gehe Kontaktliste durch und suche die ID
    for (int i = 0; i < contacts.length; i++) {
      // Stimmt die ID nicht überein
      if (contacts[i].getID() != id) {
        // füge Kontakt hinzu
        // neue Liste erzeugen und Elemente rüberkopieren
        Contact[] contactsCopyNew = new Contact[contactsCopy.length + 1];
        // Kopiere alte Inhalte rüber
        for (int j = 0; j < contactsCopy.length; j++) {
          contactsCopyNew[j] = contactsCopy[j];
        }
        contactsCopyNew[contactsCopyNew.length - 1] = contacts[i];
        contactsCopy = contactsCopyNew;
        // Wenn ID übereinstimmt, wird Kontakt
        // nicht hinzugefügt (= gelöscht)
      }
    }
    // Übernehme neue Liste
    this.contacts = contactsCopy;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  // Privates Adressbuch
  Adressbook privat = new Adressbook("Privat");
  privat.addContact(new Contact(1, "Ken Tern", "ken.tern@mail.de",
            "+49 221 3982781", "@kentern"));
  privat.addContact(new Contact(2, "Bill Iger", "bill.iger@gmx.de",
            "+49 211 9821348", "@billiger"));
  privat.addContact(new Contact(3, "Flo Kati", "flo.kati@web.de",
            "+49 251 9346441", "@flokati"));
  privat.addContact(new Contact(4, "Ingeborg Mirwas", "inge.mirwas@post.de",
            "+49 228 4663289", "@borgmirwas"));
  privat.addContact(new Contact(5, "Ann Schweigen", "ann.schweigen@gmx.de",
            "+49 231 6740921", "@annschweigen"));
  privat.addContact(new Contact(6, "Mark Enschuh", "mark.enschuh@gmail.com",
            "+49 234 4565657", "@markenschuh"));
  privat.addContact(new Contact(7, "Lee Köhr", "lee.koehr@mail.de",
            "+49 561 8976761", "@leekoehr"));
  privat.addContact(new Contact(8, "Pit Schnass", "pit.schnass@post.de",
            "+49 721 4545754", "@pitschnass"));

  // Geschäftliches Adressbuch
  Adressbook arbeit = new Adressbook("Arbeit");
  arbeit.addContact(new Contact(1, "Phil Tertüte", "phil.tertuete@company.de",
            "+49 177 1786756", "@philtertuete"));
  arbeit.addContact(new Contact(2, "Flo Kati", "flo.kati@laden.com",
            "+49 161 2336541", "@ibm.kati"));
  arbeit.addContact(new Contact(3, "Andreas Kreuz", "andreas.kreuz@bazaar.de",
            "+49 163 3442889", "@asbazaar"));
  arbeit.addContact(new Contact(4, "Erkan Alles", "erkan.alles@solver.de",
            "+49 171 1442553", "@easolver"));
  arbeit.addContact(new Contact(5, "Mark Reele", "mark.reele@media.de",
            "+49 151 5345612", "@mrmedia"));
  arbeit.addContact(new Contact(6, "Roy Bär", "roy.baer@media.de",
            "+49 151 5477889", "@rbmedia"));
  arbeit.addContact(new Contact(7, "Mario Nette", "mario.nette@media.de",
            "+49 151 5113341", "@mnmedia"));
  arbeit.addContact(new Contact(8, "Klaus Uhr", "klaus.uhr@media.de",
            "+49 151 6743431", "@kumedia"));

  println(privat.showAll());
  println(privat.getContact(5));
  privat.removeContact(5);
  println(privat.showAll());

  println(arbeit.showByName("Flo Kati"));
}

