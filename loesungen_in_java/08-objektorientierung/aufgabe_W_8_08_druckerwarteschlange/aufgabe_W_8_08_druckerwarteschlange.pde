// Klasse zur Realisierung einer Druckerwarteschlange
public class PrinterQueue {
  // Deklaration privater Variablen
  private String[] jobs;
  private int nextSlot;
  private int nextJob;
  private int numJobs;
  private int maxJobs;

  // Konstruktor mit der Angabe der maximalen Warte-
  // schlangengröße. Ohne diese Angabe kann später keine
  // Instanz (= Objekt) erzeugt werden.
  // Die internen Werte werden initialisiert
  public PrinterQueue(int maxJobs) {
    jobs = new String[maxJobs];
    nextSlot = 0;
    nextJob = 0;
    numJobs = 0;
    this.maxJobs = maxJobs;
  }

  // Methode, um einen Druckauftrag der Warteschlange
  // hinzuzufügen. Der Job wird als String übergeben.
  // Die Methode hat keinen Rückgabewert, kann aber eine
  // Exception auslösen, wenn die Anzahl der Jobs überschritten
  // wird
  public void addJob(String job)throws Exception {
    // Wenn voll besetzt, gebe Fehler zurück
    // und springe damit aus der Funktion
    if (numJobs >= maxJobs) {
      throw new Exception("Exception: Number of Jobs exceeded");
    }

    jobs[nextSlot] = job;

    // Sorge dafür, dass nächste Position immer im Array-Bereich bleibt
    nextSlot = (nextSlot + 1) % maxJobs;
    numJobs = numJobs + 1;
  }

  // Methode, die den nächsten Job zurückliefert, sofern noch
  // einer in der Pipe steht. Es wird kein Parameter an die Funktion
  // übergeben. Als Ergebnis wird der Job als String zurückgeliefert.
  public String nextJob() {
    String job = null;
    if (numJobs > 0) {
      numJobs = numJobs - 1;
      job = jobs[nextJob];
      // bestimme nächste Jobnummer
      nextJob = (nextJob + 1) % maxJobs;
    }
    return job;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  PrinterQueue pq = new PrinterQueue(1);

  try {
    pq.addJob("Hallo");
    // Warteschlange voll. Jetzt sollte Exception kommen
    pq.addJob("Weiter");
  } catch (Exception e) {
    e.printStackTrace();
  }

  // Arbeite Warteschlange ab
  println(pq.nextJob());
  println(pq.nextJob());
  try {
    // Jetzt ist Speicher leer, sollte also wieder gehen
    pq.addJob("Weiter");
  } catch (Exception e) {
    e.printStackTrace();
  }

  println(pq.nextJob());
}

