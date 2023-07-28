public class Room {
  private String name;
  private String number;
  private int seats;

  // Konstruktor, der den Namen des Raumes, die Nummer und
  // Anzahl der Sitze erwartet
  public Room(String name, String number, int seats) {
    this.name = name;
    this.number = number;
    this.seats = seats;
  }

  public String getName() {
    return this.name;
  }

  public String getNumber() {
    return this.number;
  }

  public String toString() {
    return "Raum " + this.number + " (" + this.name + ", " + this.seats + " " +
        "Sitze)";
  }
}

public class Occupancy {
  private Room room;
  private String reason;
  private String from;
  private String to;

  // Konstruktor, der den Raum, den Grund zur Raumbelegung sowie das
  // Start- und Enddatum erwartet
  public Occupancy(Room room, String reason, String from, String to) {
    this.reason = reason;
    this.room = room;
    this.from = from;
    this.to = to;
  }

  public Room getRoom() {
    return this.room;
  }

  public String getFrom() {
    return this.from;
  }

  public String toString() {
    return this.from + " - " + this.to + " (" + this.reason + ")";
  }
}

public class RoomOccupancyPlan {
  private Occupancy[] occupancies;

  // Konstruktor, der den Raumbelegungsplan initialisiert
  public RoomOccupancyPlan() {
    // Initialisiere neue Belegungsliste
    this.occupancies = new Occupancy[0];
  }

  // Zeige den Belegungsplan an
  public String toString() {
    String output = "";

    // Der Raum aus der letzten Iteration
    Room lastRoom = new Room("", "", -1);
    for (int i = 0; i < occupancies.length; i = i + 1) {
      // Aktueller Raum
      Room currentRoom = occupancies[i].getRoom();

      // Sollte der letzte Raum nicht identisch sein
      if (!lastRoom.equals(currentRoom)) {
        // Gebe die Titelzeile für den neuen Raum aus
        output = output + currentRoom + ":\n";
      }

      // Gebe den Termin aus
      output = output + "* " + occupancies[i] + "\n";

      // Speichere Raum aus aktueller Iteration für
      // nächste Iteration
      lastRoom = currentRoom;
    }

    return output;
  }

  // Füge Eintrag hinzu, sortiert nach Raum
  public void addOccupancy(
    Room room,
    String reason,
    String from,
    String to
  ) {
    // Erzeuge neue Raumbelegung basierend auf den Eingaben
    Occupancy occupancy = new Occupancy(room, reason, from, to);

    // Erstelle neuen temporären Array, der um ein Element größer ist
    Occupancy[] occupanciesTemp = new Occupancy[occupancies.length + 1];

    // Position im neuen Array
    int pos = 0;

    // Füge den ersten Listeneintrag ohne Schleife hinzu
    if (occupanciesTemp.length == 1) {
      occupanciesTemp[pos] = occupancy;
    }
    else {
      // Gehe Einträge durch
      int i = 0;
      for (; i < occupancies.length; i = i + 1) {
        // Raumnummer des neuen Eintrags
        String numberNew = occupancy
          .getRoom()
          .getNumber();

        // Belegungsbeginn des neuen Eintrags
        String fromNew = occupancy.getFrom();

        // Raumnummer des Eintrags an der aktuellen Position
        String numberCurrent = occupancies[i]
          .getRoom()
          .getNumber();

        // Belegungsbeginn des Eintrags an der aktuellen Position
        String fromCurrent = occupancies[i].getFrom();

        // Wenn aktueller Eintrag alphabetisch größer oder gleich
        // dem hinzufügenden Eintrag ist
        if (numberCurrent.compareTo(numberNew) >= 0 && fromCurrent.compareTo(fromNew) >= 0) {
          // Haben Stelle gefunden
          // Füge neuen Eintrag an dieser Stelle hinzu
          occupanciesTemp[pos] = occupancy;

          // Erhöhe Position um 1
          pos = pos + 1;
        }

        // Füge aktuellen Eintrag an dieser Stelle hinzu
        occupanciesTemp[pos] = occupancies[i];

        // Erhöhe Position um 1
        pos = pos + 1;
      }

      // Haben wir das neue Element immer noch nicht hinzugefügt,
      // da es an die letzte Stelle hinzugefügt werden muss,
      // fügen wir dieses noch hinzu
      if (i == pos) {
        occupanciesTemp[pos] = occupancy;
      }
    }

    // Setze temporären Array als neuen Array der Liste
    this.occupancies = occupanciesTemp;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  // Definiere Räume
  Room usabilitylab = new Room("Usability Lab", "A-W42", 2);
  Room besprechungsraum = new Room("Besprechungsraum", "A-C33", 10);
  Room vorlesungssaal = new Room("Vorlesungssaal", "A-T44", 140);

  // Erstelle Raumbelegungsplan
  RoomOccupancyPlan plan = new RoomOccupancyPlan();

  // Füge Einträge hinzu
  plan.addOccupancy(
    usabilitylab,
    "Studie zu Buchprojekt",
    "2019-02-03",
    "2019-02-04"
  );
  plan.addOccupancy(
    besprechungsraum,
    "Lagebesprechung zu den Programmieraufgaben",
    "2019-02-03",
    "2019-02-04"
  );
  plan.addOccupancy(
    vorlesungssaal,
    "Vorlesung Informatik",
    "2019-02-03",
    "2019-02-04"
  );
  plan.addOccupancy(
    usabilitylab,
    "Studie zu risikobasierter Authentifizierung",
    "2019-02-05",
    "2019-02-06"
  );
  plan.addOccupancy(
    usabilitylab,
    "Testen der Programmieraufgaben",
    "2019-02-04",
    "2019-02-05"
  );

  // Gebe Belegungsplan aus
  println(plan);
}
