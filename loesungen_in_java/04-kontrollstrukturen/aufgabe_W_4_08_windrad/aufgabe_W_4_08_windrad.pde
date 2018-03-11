size(800, 800);
background(255);
smooth();

fill(86, 135, 174, 175);
noStroke();

// Verschiebe Nullpunkt des Koordinatensystems von der Ecke links oben
// des grafischen Ausgabefensters ins Zentrum.
translate(width / 2, height / 2);

float radius = 350.0;
for (int i = 0; i < 8; i++) {
  arc(radius / 2, 0.0, radius, radius, 0, PI);
  rotate(PI / 4.0);
}

