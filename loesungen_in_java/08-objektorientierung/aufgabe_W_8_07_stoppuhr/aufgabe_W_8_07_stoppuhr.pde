// Klasse zur Realisierung einer Stoppuhr
class StopWatch {
  // Deklarieren privater Variablen
  // Zeitpunkte zum Messen (Start + Stop)
  private long startTime;
  private long stopTime;

  // Wird gerade Zeit gestoppt
  private boolean running;

  // Konstruktor zur Initialisierung der Member-Variablen
  public StopWatch() {
    this.startTime = 0;
    this.stopTime = 0;
    this.running = false;
  }

  // Methode zum Starten eines Vorgangs.
  // Es werden keine Werte an die Funktion übergeben
  // oder von der Funktion zurückgegeben. Nur interne
  // Member werden gesetzt
  public void start() {
    if (this.running == false) {
      this.startTime = System.currentTimeMillis();
      this.running = true;
    }
  }

  // Methode zum Stoppen eines Vorgangs.
  // Es werden keine Werte an die Funktion übergeben
  // oder von der Funktion zurückgegeben. Nur interne
  // Member werden gesetzt
  public void stop() {
    if (this.running == true) {
      this.stopTime = System.currentTimeMillis();
      this.running = false;
    }
  }

  // Methode zum Berechnen der vergangenen Zeit. Da
  // die Berechnung auf Basis der internen Variablen
  // stattfindet, werden keine Werte an die Methode
  // übergeben. Als Ergebnis wird die vergangene Zeit
  // als String zurückgegeben
  public String elapsedTime() {
    long time;
    if (this.running == true) {
      // Zeit läuft noch
      // nehme aktuelle Zeit
      time = System.currentTimeMillis() - this.startTime;
    }
    else {
      // Zeit läuft nicht (mehr)
      // nehme gestoppte Zeit
      time = this.stopTime - this.startTime;
    }

    // Bestimme Sekunden und Hundertstel
    long seconds = time / 1000;
    long hundreds = time % 1000;

    // Gebe Zeit formatiert aus
    return "" + seconds + "." + hundreds;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.

StopWatch sw = new StopWatch();

void setup() {
  size(400, 50);
}

void draw() {
  background(255);
  textSize(32);
  text(sw.elapsedTime(), 10, 30);
  fill(0, 102, 153);
}

void keyTyped() {
  if (key == '1') {
    sw.start();
  }
  else if (key == '2') {
    sw.stop();
  }
}

