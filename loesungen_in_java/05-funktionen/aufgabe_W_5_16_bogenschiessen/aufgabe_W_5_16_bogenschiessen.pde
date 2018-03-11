// Konstanten
float g = 9.81;
int soilY = 520;            // Position, an dem der Boden beginnt
int grassY = 500;           // Position, an dem die Wiese beginnt

// Pfeilstartposition
int startX = 60;
int startY = grassY - 40;

int aimWidth = 30;
int aimHeight = 70;

// Globale Variablen setzen
int speed = 90;
float angle = 45;
float arrowX = startX;
float arrowY = startY;
float arrowDegrees = angle;
boolean arrowFire = false;  // Wurde Pfeil abgefeuert?
float arrowTime = 1;
int aimX = 0;
int aimY = 0;

// Funktion zum (Re-)Initialisieren von globalen Variablen
// Benötigt keinen Eingabewert und gibt auch keinen Wert
// zurück
public void reset() {
  speed = 90;
  angle = 45;
  arrowX = startX;
  arrowY = startY;
  arrowDegrees = angle;
  arrowFire = false;        // Wurde Pfeil abgefeuert?
  arrowTime = 1;
  aimX = int(random(width - 300, width));
  aimY = grassY - aimHeight;
}

// Funktion zur Ausgabe von Koordinaten der Wurfparabel zum
// angeforderten Zeitpunkt.
// An die Funktion wird die Geschwindigkeit als Integer-Wert
// sowie der Winkel und den Zeitpunkt je als Fließkommazahl
// gegeben. Die Rückgabe erfolgt als Fließkomma-Array
float[] getTrajectory(int v0, float beta, float t) {
  beta = radians(beta);
  float x = v0 * t * cos(beta);
  float y = v0 * t * sin(beta) - (g / 2) * t * t;
  float[] output = {
    x,
    y
  };
  return output;
}

// Funktion zur Berechnung des Steigungswinkels des Pfeils
// (1. Ableitung) als Fließkommazahl zurück
float getDegrees(int v0, float beta, float t) {
  beta = radians(beta);
  float x1 = v0 * cos(beta);
  float y1 = v0 * sin(beta) - g * t;
  float winkel = atan(y1 / x1);
  return degrees(winkel);
}

// Funktion, die die Reaktion auf Tastatureingaben
// verarbeitet. Der keyCode ist in einer globalen
// Variable enthalten.
void keyPressed() {
  if (keyCode == RIGHT) {
    increaseSpeed();
  }
  else if (keyCode == LEFT) {
    decreaseSpeed();
  }
  else if (keyCode == UP) {
    increaseAngle();
  }
  else if (keyCode == DOWN) {
    decreaseAngle();
  }
  else if (keyCode == 10) {
    arrowFire = true;
  }
  else if (key == 'r') {
    reset();
  }
}

// Funktion zum Erhöhen der Geschwindigkeit ohne
// Ein- oder Ausgabeparameter
void increaseSpeed() {
  if (arrowFire == false) {
    speed = speed + 1;
  }
}

// Funktion zum Verringern der Geschwindigkeit ohne
// Ein- oder Ausgabeparameter
void decreaseSpeed() {
  if (speed > 0 && arrowFire == false) {
    speed = speed - 1;
  }
}

// Funktion zum Erhöhen des Winkels ohne
// Ein- oder Ausgabeparameter
void increaseAngle() {
  if (angle < 90 && arrowFire == false) {
    angle = angle + 1;
    arrowDegrees = angle;
  }
}
// Funktion zum Verringern der Winkels ohne
// Ein- oder Ausgabeparameter
void decreaseAngle() {
  if (angle > -90 && arrowFire == false) {
    angle = angle - 1;
    arrowDegrees = angle;
  }
}

// Funktion zum Aktualisieren der Pfeilposition
// Keine Ein- oder Ausgabeparameter, da die Funktion
// auf den globalen Variablen rechnet.
void updateArrow() {
  // Nur aktualisieren, wenn Pfeil abgefeuert wurde
  if (arrowFire == true) {
    // Hole Wurfparabel
    float[] newPos = getTrajectory(speed, angle, arrowTime);
    arrowDegrees = getDegrees(speed, angle, arrowTime);

    // Berechne neue Pfeilposition mit Wurfparabel
    arrowX = startX + newPos[0];
    arrowY = startY - newPos[1];

    // Erhöhe Berechnungszeit der Wurfparabel
    arrowTime = arrowTime + 0.1;
    checkCollision();
  }
}

// Funktion zur simplen Kollisionserkennung
// ohne Ein- und Ausgabeparameter
void checkCollision() {
  if (isInBounds(arrowX, arrowY)) {
    arrowFire = false;
  }
}

// Funktion zur Bestimmung, ob die aktuelle Koordinate
// im Kollisionsbereich liegt
boolean isInBounds(float x, float y) {
  if (y > soilY || x > aimX 
    && x < aimX + aimWidth 
    && y < aimY + aimHeight 
    && y > aimY) {
    return true;
  }
  else {
    return false;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(1200, 600);
  reset();
}


// Funktion, die immer wieder zum (Neu-)Zeichnen des
// Bildschirminhalts aufgerufen wird
void draw() {
  // zunächst Löschen des Bildschirms
  clear();
  // Hintergrundfarbe setzen
  background(255);
  // mit gesetzter Farbe füllen
  fill(0);
  // Textgröße setzen
  textSize(20);
  // zeichne Variablenangaben
  text("speed: " + speed, 5, 25);
  text("angle: " + angle, 5, 50);

  // Auf Kollision prüfen
  checkCollision();

  // Pfeil aktualisieren
  updateArrow();

  // Zeichne Wiese
  stroke(76, 178, 33);
  fill(76, 178, 33);
  rect(0, grassY, width, soilY - grassY);

  // Zeichne Boden
  stroke(125, 67, 22);
  fill(125, 67, 22);
  rect(0, soilY, width, width - soilY);

  // Zeichne Zielscheibe
  stroke(125, 0, 0);
  fill(125, 0, 0);
  rect(aimX, aimY, aimWidth, aimHeight);

  // Zeichne Pfeil
  stroke(125);
  fill(125);
  int radius = 80;
  float archW = cos(radians(arrowDegrees)) * radius;
  float archH = sin(radians(arrowDegrees)) * radius;
  line(arrowX, arrowY, arrowX - archW, arrowY + archH);
}

