// Öffentliche Klasse zur Repräsentation eines Hotelzimmers
public class Room {
  // Deklaration privater Variablen
  private int number;
  private boolean available;

  // Konstruktor, der vorschreibt, dass die Zimmer-
  // nummer angegeben wird
  public Room(int number) {
    this.number = number;
    this.available = true;
  }

  // Öffentliche Methode zur Prüfung, ob das Zimmer
  // noch frei ist.
  public boolean isAvailable() {
    return this.available;
  }

  // Öffentliche Methode, um den Status der Zimmer-
  // belegung zu ändern. Der zu setzende Status
  // wird der Methode übergeben.
  public void setAvailable(boolean available) {
    this.available = available;
  }

  // Methode, die die Zimmernummer zurückliefert.
  public int getNumber() {
    return this.number;
  }
}

// Öffentliche Klasse zur Zimmerverwaltung eines Hotels
public class Hotel {
  // Deklaration interner Variablen
  private Room[] rooms;
  private String name;
  private int stars;

  // Öffentlicher Konstruktor, der den Hotelnamen, die
  // Anzahl der Sterne sowie die Räume übergeben bekommt
  public Hotel(String name, int stars, Room[] rooms) {
    this.rooms = rooms;
    this.name = name;
    this.stars = stars;
  }

  // Öffentliche Methode, die den Index des nächsten freien Raums
  // zurückliefert
  public int checkIn() {
    // Gehe Räume nacheinander durch
    for (int i = 0; i < rooms.length; i++) {
      // Sobald ein Raum frei ist
      if (rooms[i].isAvailable()) {
        // Raum belegen
        rooms[i].setAvailable(false);
        // Aus der Funktion mit Nummer springen
        return rooms[i].getNumber();
      }
    }

    return 0;
  }

  // Öffentliche Methode, die einen Checkout-Vorgang simuliert. Die
  // Zimmernummer, für die der Checkout-Vorgang durchgeführt werden
  // soll wird an die Methode übergeben.
  public void checkOut(int number) {
    // Zähler außerhalb von for-Schleife definieren,
    // da wir sie danach noch brauchen könnten
    int i = 0;

    // Gehe Räume nacheinander durch
    for (; i < rooms.length; i++) {
      // Stimmt Raumnummer überein und ist Raum noch belegt
      if (rooms[i].getNumber() == number && !rooms[i].isAvailable()) {
        // Aus Schleife springen
        break;
      }
    }

    // Sollten wir vor Array-Ende aus Schleife
    // gesprungen sein (= Raum gefunden + belegt),
    // dann Raum auf verfügbar stellen
    if (i < rooms.length) {
      rooms[i].setAvailable(true);
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  Room[] rooms = new Room[9];
  rooms[0] = new Room(101);
  rooms[1] = new Room(102);
  rooms[2] = new Room(103);
  rooms[3] = new Room(201);
  rooms[4] = new Room(202);
  rooms[5] = new Room(203);
  rooms[6] = new Room(301);
  rooms[7] = new Room(302);
  rooms[8] = new Room(303);

  Hotel hotel = new Hotel("Seeblick", 4, rooms);

  println(hotel.checkIn());
  println(hotel.checkIn());
  println(hotel.checkIn());
  hotel.checkOut(102);
  println(hotel.checkIn());
  println(hotel.checkIn());
}

