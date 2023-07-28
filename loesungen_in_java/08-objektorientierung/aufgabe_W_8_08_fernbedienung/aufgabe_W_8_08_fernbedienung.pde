// Klasse, die eine Fernbedienung realisiert
public class RemoteControl {
  // private Variablen deklarieren
  private String[] programs;
  private int currentProgramNumber;

  // Konstruktor, der die maximale Anzahl an Programm-
  // speicherplätzen zur Initialisierung übergeben
  // bekommt. Ohne diese Angabe kann kein Objekt der
  // Fernbedienung angelegt werden.
  public RemoteControl(int numPrograms) {
    this.programs = new String[numPrograms];

    // Initialisiere angegebene Anzahl an Programmen
    for (int i = 0; i < numPrograms; i++) {
      this.programs[i] = "Programm " + (i + 1);
    }
    this.currentProgramNumber = 0;
  }

  // Methode zum Wechsel zum nächsten Programm
  public void nextProgram() {
    // Gehe um ein Programm nach oben,
    // wenn noch nicht am Ende der Liste
    if (currentProgramNumber < programs.length - 1) {
      this.currentProgramNumber += 1; 
    }
    // Sonst beim ersten Programm wieder starten
    else {
      this.currentProgramNumber = 0;
    }
  }

  // Methode zur Benennung des aktuellen Programms
  public void setProgramName(String name) {
    programs[currentProgramNumber] = name;
  }

  // Methode, um aktuelles Programm mit Sendernummer
  // auszugeben
  public void printProgramName() {
    println("Sendernummer: " + currentProgramNumber);
    println("Programm: " + programs[currentProgramNumber]);
    println();
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  // Testdurchlauf
  RemoteControl rc = new RemoteControl(5);
  rc.setProgramName("ARD");
  rc.printProgramName();

  // Gehe drei Sender weiter und gebe jeden aus
  for (int i = 0; i < 3; i++) {
    rc.nextProgram();
  }

  // Setze Sendername
  rc.setProgramName("RTL");
  rc.printProgramName();

  // Gehe sechs Mal nach vorne
  for (int i = 0; i < 6; i++) {
    rc.nextProgram();
    rc.printProgramName();
  }
}

