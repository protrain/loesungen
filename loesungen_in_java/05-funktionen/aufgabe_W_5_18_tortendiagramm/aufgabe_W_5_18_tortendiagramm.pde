// Funktion zum Zeichnen eines Tortendiagramms mit den abgegebenen
// Stimmen und den Farben als Eingabe
public void drawPieChart(int[] numbers, color[] colors) {
  // Berechne zunächst die Summe der Einzelelemente
  float sum = 0 f;
  for (int i = 0; i < numbers.length; i = i + 1) {
    sum = sum + numbers[i];
  }

  // Berechne danach die Prozente
  float percentages[] = new float[numbers.length];
  for (int i = 0; i < numbers.length; i = i + 1) {
    percentages[i] = numbers[i] / sum * 100;
  }

  // Setze Startposition im Kreis. Wir beginnen am Anfang.
  float start = 0 f;

  // Gehe nun die Prozente durch
  for (int i = 0; i < percentages.length; i = i + 1) {
    float percent = percentages[i];

    // Bestimme Endposition in Abhängigkeit vom Prozentsatz
    float end = start + 2 * PI / 100 * percent;

    // Setze neue Füllfarbe
    fill(colors[i]);

    // Male Tortenabschnitt in vordefinierter Farbe
    arc(width / 2, height / 2, 300, 300, start, end);

    // Setze Füllfarbe für den Text
    fill(0);

    // Setze Textgröße
    textSize(30);

    // Setze neue Startposition ans Ende
    start = end;
  }
}

// Funktion zum Zeichnen eines Tortendiagramms mit den abgegebenen
// Stimmen als Eingabe. Die Farben werden zufällig generiert
public void drawPieChart(int[] numbers) {
  // Array, in dem wir die Farben für das Tortendiagramm
  // speichern
  color[] colors = new color[numbers.length];

  // Generiere Farben
  for (int i = 0; i < numbers.length; i = i + 1) {
    // Generiere die Farben für Rot, Grün und Blau.
    int r = int(random(0, 255));
    int g = int(random(0, 255));
    int b = int(random(0, 255));

    // Setze die Farben für Rot, Grün und Blau.
    colors[i] = color(r, g, b);
  }

  // Rufe die drawPieChart-Funktion mit den Farben auf
  drawPieChart(numbers, colors);
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  // Setze die Fenstergröße auf 400x400 Pixel
  size(400, 400);

  // Setze weißen Hintergrund
  background(255);

  // Array, in dem wir die absoluten Zahlen für unser
  // Tortendiagramm speichern
  int[] numbers = {
    900,
    1200,
    122,
    567
  };

  // Array, in dem wir die Farben für das Tortendiagramm
  // speichern
  color[] colors = {
    color(32, 39, 56),
    color(75, 101, 0),
    color(185, 104, 47),
    color(172, 58, 82)
  };

  // Zeichne Tortendiagramm mit Farben als Parameter
  drawPieChart(numbers, colors);

  // Zeichne Tortendiagramm ohne Farben als Parameter
  //drawPieChart(numbers);
}