// Öffentliche Klasse, die einen ReisendePerson repräsentiert
public class ReisendePerson {
  // Deklaration privater Variablen
  private String firstname;
  private String lastname;
  private String title;
  private boolean checkIn;

  // Ist ReisendePerson am Gate?
  private boolean atGate;

  // Konstruktor, der dafür sorgt, dass Objekte dieser Klasse nur
  // unter Angabe von Vor- und Zunamen sowie Titel angelegt werden
  // können.
  public ReisendePerson(String firstname, String lastname, String title) {
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

  // Öffentliche Methode zur Prüfung, ob ReisendePerson bereits
  // eingecheckt ist
  public boolean isCheckedIn() {
    return checkIn;
  }

  // Öffentliche Methode zum Setzen des Status: ReisendePerson am Gate
  public void onGate() {
    this.atGate = true;
  }

  // Öffentliche Methode zur Ermittlung, ob ReisendePerson am Gate ist
  public boolean isAtGate() {
    return atGate;
  }

  // Öffentliche Methode zum Generieren eines aussagekräftigen
  // Strings zur Repräsentation der reisenden Person.
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
  private ReisendePerson[] passengers;

  // Öffentlicher Konstruktor, der die Daten vorgibt, die für
  // die Erzeugung eines Objekts dieser Klasse notwendig sind.
  public Flug(
    String id,
    String startAirport,
    String endAirport,
    String startTime,
    String gate,
    ReisendePerson[] passengers
  ) {
    this.id = id;
    this.startAirport = startAirport;
    this.endAirport = endAirport;
    this.startTime = startTime;
    this.gate = gate;
    this.passengers = passengers;
  }

  // Öffentliche Methode, die eine reisende Person aufruft, wenn
  // diese nicht am Gate ist.
  public void ausrufen() {
    // Gehe ReisendePersonliste durch
    for (int i = 0; i < passengers.length; i++) {
      // Wenn ReisendePerson eingecheckt und noch
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
  ReisendePerson[] reisende = {
    new ReisendePerson("Martin", "Krause", "Dr."),
    new ReisendePerson("Simone", "Krause", ""),
    new ReisendePerson("Herr", "Kules", ""),
    new ReisendePerson("Frau", "Kules", ""),
    new ReisendePerson("Kranke", "Person", "")
  };

  // Checke alle Fluggäste außer Kranke Person ein
  for (int i = 0; i < reisende.length - 1; i++) {
    reisende[i].checkIn();
    // Außer den Krauses sind davon alle am Gate
    if (i > 1) {
      reisende[i].onGate();
    }
  }

  Flug flug = new Flug(
    "MH123",
    "Köln-Bonn",
    "München",
    "9:10",
    "C12",
    reisende
  );
  flug.ausrufen();
}

