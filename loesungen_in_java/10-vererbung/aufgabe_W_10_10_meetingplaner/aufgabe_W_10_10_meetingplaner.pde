// Import einer ArrayListe, welche das Hinzufügen von Elementen
// ähnlich wie einer Liste in Python erlaubt.
import java.util.ArrayList;

// Abstrakte Klasse zur Repräsentation eines Meetings.
// Von dieser Klasse kann keine Instanz (= Objekt) erzeugt werden.
public abstract class Meeting {  
  // Deklaration privater Variablen
  private String title;
  private ArrayList<String> agenda;
  private ArrayList<String> participants;
  private String start;
  private String end;

  // Konstruktor, der zur Angabe eines Meetingtitels und des
  // Wetters auffordert
  public Meeting(String title, String start, String end) {
    this.title = title;
    this.agenda = new ArrayList<String>();
    this.participants = new ArrayList<String>();
    this.start = start;
    this.end = end;
  }
  
  public void addToAgenda(String element) {
    this.agenda.add(element);
  }
  
  // Gibt die Agenda als String mit Bulletinpoint-Liste zurück
  public String getAgendaAsString() {
    if (this.agenda.size() > 0) {
      String agendaString = "\n";
      
      // Gehe jedes Element in der Agenda durch
      for (String agendaElement : this.agenda) {
        // Füge neue Zeile mit Bulletinpoint hinzu
        agendaString += "- "+ agendaElement + "\n";
      }
      
      return agendaString;
    }
    
    // Keine Elemente vorhanden
    return "None\n";
  }
  
  public void addParticipant(String name) {
    this.participants.add(name);
  }
  
  // Gibt die Teilnehmendenliste als String zurück
  public String getParticipantsAsString() {
    if (this.participants.size() > 0) {
       String participantsString = "";

      // Gehe Liste der Teilnehmenden durch
      for (String participant : this.participants) {
        // Füge Eintrag hinzu
        participantsString += participant + ", ";
      }
      
      // Entferne die letzten zwei Zeichen nach der letzten Iteration
      return participantsString.substring(
        0,
        participantsString.length() - 2
      );
    }
    
    // Keine Elemente vorhanden
    return "None";
  }

  public String toString() {
     return this.title + " (" + this.start + " - " + this.end + ")\n"
       + "Agenda: " + this.getAgendaAsString()
       + "Participants: " + this.getParticipantsAsString(); 
  }
}

// Öffentliche Klasse für ein physisches Meeting leitet
// von der Klasse Meeting ab.
public class PhysicalMeeting extends Meeting {
  private String roomName;

  // Konstruktor erwartet die Werte aus der abstrakten Klasse und dazu
  // noch den Raumnamen
  public PhysicalMeeting(
    String title,
    String start,
    String end,
    String roomName
  ) {
    // Titel, sowie Start- und Endzeitpunkt werden an die
    // überliegende Funktion übergeben.
    super(title, start, end);
    
    this.roomName = roomName;
  }
  
  public String toString() {
    return super.toString() + "\n" + "Room: "+this.roomName;
  }
}

// Öffentliche Klasse für ein digitales Meeting leitet
// von der Klasse Meeting ab.
public class DigitalMeeting extends Meeting {
  private String URL;

  // Konstruktor erwartet die Werte aus der abstrakten Klasse und dazu
  // noch den Einwahllink
  public DigitalMeeting(
    String title,
    String start,
    String end,
    String URL
  ) {
    // Titel, sowie Start- und Endzeitpunkt werden an die
    // überliegende Funktion übergeben.
    super(title, start, end);
    
    this.URL = URL;
  }
  
  public String toString() {
    return super.toString() + "\n" + "Link: "+this.URL;
  }
}

// Öffentliche Klasse für ein hybrides Meeting leitet
// von der Klasse Meeting ab.
public class HybridMeeting extends Meeting {
  private String roomName;
  private String URL;

  // Konstruktor erwartet die Werte aus der abstrakten Klasse und dazu
  // noch den Raumnamen und den Einwahllink
  public HybridMeeting(
    String title,
    String start,
    String end,
    String roomName,
    String URL
  ) {
    // Titel, sowie Start- und Endzeitpunkt werden an die
    // überliegende Funktion übergeben.
    super(title, start, end);
    
    this.roomName = roomName;
    this.URL = URL;
  }
  
  public String toString() {
    return super.toString() 
      + "\n" + "Room: "+this.roomName
      + "\n" + "Link: "+this.URL;
  }
}


// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  PhysicalMeeting physicalMeeting = new PhysicalMeeting(
    "Physical Testmeeting",
    "01.01.2023, 14:00",
    "01.01.2023, 15:00",
    "C121"
  );
  
  physicalMeeting.addToAgenda("Neues Tool besprechen");
  physicalMeeting.addToAgenda("Feedback von Stakeholdern");
  
  physicalMeeting.addParticipant("Rolf");
  physicalMeeting.addParticipant("Birgit");
  physicalMeeting.addParticipant("Dieter");
  physicalMeeting.addParticipant("Sandra");
  physicalMeeting.addParticipant("Manfred");
  
  println(physicalMeeting);
  println();
  
  DigitalMeeting digitalMeeting = new DigitalMeeting(
    "Digital Testmeeting",
    "02.01.2023, 11:15",
    "02.01.2023, 15:00",
    "https://protrain.github.io/conf?abcdefu"
  );
  
  digitalMeeting.addToAgenda("Digitalisierung");
  digitalMeeting.addToAgenda("Ausprobieren Telko");
  digitalMeeting.addToAgenda("Sonstiges");
  
  digitalMeeting.addParticipant("Luigi");
  digitalMeeting.addParticipant("Mario");
  digitalMeeting.addParticipant("Giuliana");
  digitalMeeting.addParticipant("Pietro");
  
  println(digitalMeeting);
  println();
  
  HybridMeeting hybridMeeting = new HybridMeeting(
    "Hybrid Testmeeting",
    "12.01.2023, 17:00",
    "12.01.2023, 18:00",
    "D181",
    "https://protrain.github.io/conf?abcdefu"
  );
    
  println(hybridMeeting);
}
