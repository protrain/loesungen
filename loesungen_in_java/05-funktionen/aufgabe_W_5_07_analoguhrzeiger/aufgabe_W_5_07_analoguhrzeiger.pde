// Funktion zur Berechnung des Winkels für den Stundenzeiger
// Die Stunden- und Minutenzahl werden als Integer-Werte an
// die Funktion übergeben, die als Ergebnis den Winkel als
// ganzzahligen Wert zurückgibt
int computeHourHandAngle(int h, int m) {
  return (60 * h + m) / 2; // gibt Ergebnis der Berechnung zurück
}

// Funktion zur Berechnung des Winkels für den Minutenzeiger
// Die Minutenzahl wird als Ganzzahlwert an die Funktion übergeben.
// Die Funktion liefert den Winkel für den Minutenzeiger als
// Integer-Wert zurück.
int computeMinuteHandAngle(int m) {
  return 6 * m;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  // Uhrzeit in Stunden und Minuten festlegen
  int h = 3;
  int m = 33;

  // Bestimme die beiden Winkel
  int hAngle = computeHourHandAngle(h, m);
  int mAngle = computeMinuteHandAngle(m);

  // Gebe Winkel aus
  println(
    "Der Stundenzeiger steht um " + h + ":" + m + " Uhr auf " + hAngle +
    " Grad."
  );
  println(
    "Der Minutenzeiger steht um " + h + ":" + m + " Uhr auf " + mAngle +
    " Grad."
  );

  // Zeichne analoge Zeitangabe in grafisches Ausgabefenster
  size(200, 200);
  translate(width / 2, height / 2);
  ellipse(0, 0, 180, 180);
  rotate(radians(hAngle));
  line(0, 0, 0, -60);
  rotate(-radians(hAngle));
  rotate(radians(mAngle));
  line(0, 0, 0, -80);
}

