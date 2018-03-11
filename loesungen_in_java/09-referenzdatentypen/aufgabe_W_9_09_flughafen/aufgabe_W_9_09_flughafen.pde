// Öffentliche Klasse, die einen Passagier repräsentiert
public class Passagier {
  // Deklaration privater Variablen
  private String firstname;
  private String lastname;
  private String title;
  private boolean checkIn;

  // Ist Passagier am Gate?
  private boolean atGate;

  // Konstruktor, der dafür sorgt, dass Objekte dieser Klasse nur
  // unter Angabe von Vor- und Zunamen sowie Titel angelegt werden
  // können.
  public Passagier(String firstname, String lastname, String title) {
    this.firstname = firstname;
    this.lastname = lastname;
    this.title = title;
    this.checkIn = false;
    this.atGate = false;
  }

  // Öffentliche Methode zum Durchführen des Check-ins
  public void checkIn() {
    this.checkIn = true;
  }

  // Öffentliche Methode zur Prüfung, ob dieser Passagier bereits
  // eingecheckt ist
  public boolean isCheckedIn() {
    return checkIn;
  }

  // Öffentliche Methode zum Setzen des Status: Passagier am Gate
  public void onGate() {
    this.atGate = true;
  }

  // Öffentliche Methode zur Ermittlung, ob der Passagier am Gate ist
  public boolean isAtGate() {
    return atGate;
  }

  // Öffentliche Methode zum Generieren eines aussagekräftigen
  // Strings zur Repräsentation des Passagiers.
  public String toString() {
    // Nur Titel ausgeben, wenn auch angegeben
    if (title.equals("")) {
      return firstname + " " + lastname;
    }
    else {
      return title + " " + firstname + " " + lastname;
    }
  }
}

// Öffentliche Klasse, die einen Flug repräsentieren soll
public class Flug {
  // Deklaration privater Variablen
  private String id;
  private String startAirport;
  private String endAirport;
  private String startTime;
  private String gate;
  private Passagier[] passengers;

  // Öffentlicher Konstruktor, der die Daten vorgibt, die für
  // die Erzeugung eines Objekts dieser Klasse notwendig sind.
  public Flug(
    String id,
    String startAirport,
    String endAirport,
    String startTime,
    String gate,
    Passagier[] passengers
  ) {
    this.id = id;
    this.startAirport = startAirport;
    this.endAirport = endAirport;
    this.startTime = startTime;
    this.gate = gate;
    this.passengers = passengers;
  }

  // Öffentliche Methode, die einen Passagier aufruft, wenn
  // dieser nicht am Gate ist.
  public void ausrufen() {
    // Gehe Passagierliste durch
    for (int i = 0; i < passengers.length; i++) {
      // Wenn Passagier eingecheckt und noch
      // nicht am Gate
      if (passengers[i].isCheckedIn() && !passengers[i].isAtGate()) {
        // Ausrufen
        println("Last call for passenger " + passengers[i]);
      }
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  Passagier[] passagiere = {
    new Passagier("Martin", "Krause", "Dr."),
    new Passagier("Simone", "Krause", ""),
    new Passagier("Herr", "Kules", ""),
    new Passagier("Frau", "Kules", ""),
    new Passagier("Kranke", "Person", "")
  };

  // Checke alle Fluggäste außer Kranke Person ein
  for (int i = 0; i < passagiere.length - 1; i++) {
    passagiere[i].checkIn();
    // Außer den Krauses sind davon alle am Gate
    if (i > 1) {
      passagiere[i].onGate();
    }
  }

  Flug flug = new Flug(
    "MH123",
    "Köln-Bonn",
    "München",
    "9:10",
    "C12",
    passagiere
  );
  flug.ausrufen();
}

