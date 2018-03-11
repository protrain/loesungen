// Wurf und Visualisierung eines 6-seitigen Würfels
int diceNumber = 1; // Würfelzahl, wird hier einmalig initialisiert


// Funktion zum Zeichnen einer gewürfelten Zahl, die als Integer-Wert
// übergeben wird.
void drawDice(int number) {
  // Größe des Würfelpunkts
  int dotSize = 40;

  // Zeichne Punkte in Abhängigkeit der Nummer
  // die Augenzahl
  if (number == 1) {
    ellipse(200, 200, dotSize, dotSize);
  }
  else if (number == 2) {
    ellipse(100, 100, dotSize, dotSize);
    ellipse(300, 300, dotSize, dotSize);
  }
  else if (number == 3) {
    ellipse(100, 100, dotSize, dotSize);
    ellipse(200, 200, dotSize, dotSize);
    ellipse(300, 300, dotSize, dotSize);
  }
  else if (number == 4) {
    ellipse(100, 100, dotSize, dotSize);
    ellipse(300, 300, dotSize, dotSize);
    ellipse(300, 100, dotSize, dotSize);
    ellipse(100, 300, dotSize, dotSize);
  }
  else if (number == 5) {
    ellipse(100, 100, dotSize, dotSize);
    ellipse(300, 300, dotSize, dotSize);
    ellipse(300, 100, dotSize, dotSize);
    ellipse(100, 300, dotSize, dotSize);
    ellipse(200, 200, dotSize, dotSize);
  }
  else if (number == 6) {
    ellipse(100, 100, dotSize, dotSize);
    ellipse(300, 300, dotSize, dotSize);
    ellipse(300, 100, dotSize, dotSize);
    ellipse(100, 300, dotSize, dotSize);
    ellipse(100, 200, dotSize, dotSize);
    ellipse(300, 200, dotSize, dotSize);
  }
}

// Funktion zum Generieren einer Zufallszahl,
// die dann als Integer-Wert zurückgeliefert wird
int throwDice() {
  // Mit dem Zufallszahlgenerator random wird eine
  // Zahl von 1-6 generiert.
  return int(random(1, 7));
}

// Diese Funktion wird ausgeführt, wenn eine Taste
// gedrückt wurde.
void keyPressed() {
  diceNumber = throwDice();
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(400, 400);

  diceNumber = throwDice(); // Zur Initialisierung einmal werfen
}

// Funktion zum Zeichnen
void draw() {
  clear();
  stroke(0);
  fill(0);
  background(255, 255, 255);

  drawDice(diceNumber);
}

