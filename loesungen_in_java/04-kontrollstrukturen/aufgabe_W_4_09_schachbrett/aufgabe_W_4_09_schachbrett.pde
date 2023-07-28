size(800, 800);
noStroke();

// Soll aktueller Kasten schwarz sein?
boolean black = true;

// Größe pro Feldelement
int size = 100;

// Gehe jede Spalte durch
for (int y = 0; y < height / size; y++) {
  // Gehe jede Zeile durch
  for (int x = 0; x < width / size; x++) {
    // Male Farbe abhängig von Variable
    if (black == true) {
      // setze Farbe auf Schwarz
      fill(0);
    }
    else {
      // setze Farbe auf Weiß
      fill(255);
    }

    // Kehre Variable um
    black = !black;

    // Male Element
    rect(0, 0, size, size);

    // "Wandere" ein Feld nach rechts
    translate(size, 0);
  }
  // Ende der Zeile erreicht
  // "Wandere" in nächste Zeile
  translate(-width, size);

  // Kehre Variable nochmals um, da Muster
  // immer mit letzter Farbe anfängt
  black = !black;
}

