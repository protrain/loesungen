// Klasse zur Repräsentation eines Meeting-Protokolls
public class MeetingMinutes {
  // Deklaration privater Variablen
  private String date;
  private String timeframe;
  private String room;
  private String[] participants;
  private Item[] items;

  // Konstruktor, der die benötigten Daten per
  // Vorschrift beim Anlegen eines neuen Objekts
  // erforderlich macht.
  public MeetingMinutes(
    String date,
    String timeframe,
    String room,
    String[] participants
  ) {
    this.date = date;
    this.timeframe = timeframe;
    this.room = room;
    this.participants = participants;

    // Leere Liste erzeugen
    this.items = new Item[0];
  }

  // Methode zum Hinzufügen eines Item-Objekts
  public void add(Item item) {
    // Erzeuge vergrößertes Array
    Item[] newItems = new Item[items.length + 1];

    // Kopiere Elemente rüber
    for (int i = 0; i < items.length; i = i + 1) {
      newItems[i] = items[i];
    }

    // Belege letztes Element mit neuem Item
    newItems[newItems.length - 1] = item;

    // Ersetze alte mit neuer Liste
    items = newItems;
  }

  // Methode zur Repräsentation eines Meetings
  public String toString() {
    String output = "Meeting: " + date + " (" + timeframe + "), " + room + "\n";
    output = output + "Participants: ";

    // Gehe Teilnehmerliste durch
    for (int i = 0; i < participants.length; i = i + 1) {
      output = output + participants[i];

      // Komma bis zum letzten Element setzen
      if (i < participants.length - 1) {
        output = output + ", ";
      }
    }
    output = output + "\n-----------\n";

    // Alle Diskussionspunkte durchgehen
    for (int i = 0; i < items.length; i = i + 1) {
      output = output + items[i].toString() + "\n";
    }

    return output;
  }
}

// Abstrakte Klasse Item
public abstract class Item {
  // Deklaration privater Variablen
  String content;

  // Konstruktor, der den Content verlangt
  public Item(String content) {
    this.content = content;
  }

  // Methode zur Repräsentation des Items
  public String toString() {
    return this.content;
  }
}

// Öffentliche Klasse zur Repräsentation eines Diskussionsbeitrags.
// Es wird von der Klasse Item geerbt.
public class DiscussionItem extends Item {
  // Der Konstruktor erwartet den Inhalt
  public DiscussionItem(String content) {
    // und übergibt diesen an die Basisklasse
    super(content);
  }

  // Überschreiben der Repräsentation mit der spezifischen Version
  // für einen Diskussionsbeitrag.
  public String toString() {
    return "Discussion: " + super.toString();
  }
}

// Klasse, die eine Entscheidung repräsentiert und von der Klasse
// Item erbt.
public class DecisionItem extends Item {
  // Konstruktor, der den Content verlangt
  public DecisionItem(String content) {
    // und die Basisklasse damit aufruft
    super(content);
  }

  // Überschreiben der Repräsentation mit der spezifischen Version
  // für einen Entscheidungsbeitrag.
  public String toString() {
    return "Decision: " + super.toString();
  }
}

// Klasse zur Repräsentation einer Aktion, die von der Klasse
// Item ableitet.
public class ActionItem extends Item {
  // Öffentlicher Konstruktor, der zur Angabe des Inhalts verpflichtet.
  public ActionItem(String content) {
    // und an die Basisklasse weiterleitet
    super(content);
  }

  // Überschreiben der Repräsentation mit der spezifischen Version
  // für einen Aktionsbeitrag.
  public String toString() {
    return "Action: " + super.toString();
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  String[] participants = {
    "Luigi Lo Iacono",
    "Michael Schneider",
    "Stephan Wiefling"
  };

  MeetingMinutes meeting = new MeetingMinutes(
    "10.10.2017",
    "10-12 Uhr",
    "R123",
    participants
  );

  meeting.add(new DiscussionItem("Veröffentlichung Buch"));
  meeting.add(new DecisionItem("Dem Antrag wurde einstimmig zugestimmt."));
  meeting.add(
    new ActionItem("Bis zum nächsten Meeting muss Kapitel 9 fertig gestellt sein.")
  );

  println(meeting);
}
