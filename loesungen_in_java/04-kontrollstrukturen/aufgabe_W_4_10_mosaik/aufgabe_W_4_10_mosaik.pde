size(800, 800);
background(255);
noStroke();

// Größe pro Kästchen
int size = 20;

// Gehe alle Spalten durch
for (int y = 0; y < height / size; y++) {
  // Gehe alle Zeilen durch
  for (int x = 0; x < width / size; x++) {
    // Zufällige Füllfarbe
    fill(random(0, 255), random(0, 255), random(0, 255));

    // Zufälliger Rotationswinkel
    float angle = random(-PI / 32, PI / 32);

    // Rotiere hin
    rotate(angle);

    // Zeichne Rechteck
    rect(0, 0, size, size);

    // Rotiere zurück
    rotate(-angle);

    // Bewege Koordinatensystem nach rechts
    translate(size, 0);
  }

  // Bewege Koordinatensystem nach unten und ganz nach links
  translate(-height, size);
}

