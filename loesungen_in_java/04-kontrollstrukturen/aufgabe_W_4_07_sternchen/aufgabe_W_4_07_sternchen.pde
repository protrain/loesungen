size(400, 400);
background(255);
smooth();

strokeWeight(30);
strokeCap(ROUND);

// Verschiebe Nullpunkt des Koordinatensystems von der Ecke links oben
// des grafischen Ausgabefensters ins Zentrum.
translate(width / 2, height / 2);

for (int i = 0; i < 8; i++) {
  line(0, 60, 0, 100);
  rotate(PI / 4.0);
}

