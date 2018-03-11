// Funktion zur Glättung eines Audiosignals
// Erhält das Signal als double-Array
double[] smoothAudio(double[] signal) {
  // leeres Array erzeugen
  double[] output = new double[signal.length];

  // Für das erste Element wird der Wert
  // als Durchschnitt der ersten beiden Werte berechnet
  double average = (signal[0] + signal[1]) / 2;

  output[0] = average;

  // Für alle weiteren Elemente (bis auf das letzte...)
  for (int n = 1; n < signal.length - 1; n = n + 1) {
    // Durchschnitt berechnen
    average = (signal[n - 1] + signal[n] + signal[n + 1]) / 3;

    // Wert dem Output hinzufügen
    output[n] = average;
  }

  // ... das wird nochmal gesondert berechnet
  average = (signal[signal.length - 2] + signal[signal.length - 1]) / 2;
  output[signal.length - 1] = average;

  return output;
}

// Funktion zum Zeichnen des Signals
// An die Funktion wird das Signal als eindimensionales Array sowie
// der Startpunkt für die Zeichnung (ist Fensterhöhe = unterer Rand)
// übergeben.
void displayAudio(double[] signal, int yStart) {
  int xScale = 8;        // Skalierung der Punkte untereinander
  int yScale = 3;        // Skalierung der Punkte untereinander
  int xSize = 7;         // Punktgröße
  int x = 0;

  for (int i = 0; i < signal.length; i++) {
    float element = (float)signal[i];
    ellipse(x * xScale, -element * yScale + yStart, xSize, xSize);
    x = x + 1;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(500, 500);
  background(255);
  fill(255, 0, 0);

  // Generiere Sinussignal (20 Elemente)
  double[] audio = new double[20];

  for (int i = 0; i < 20; i++) {
    audio[i] = int(sin(2 * PI / 20 * i) * 20);
  }

  // Baue anschließend Störungen im Signal ein
  audio[10] = audio[8] - 8;
  audio[15] = audio[15] - 7;

  double[] audioSmooth = smoothAudio(audio);
  displayAudio(audio, 100);

  fill(0, 255, 0, 255);
  displayAudio(audioSmooth, 300);
}

