// Funktion zum Verkleinern eines quadratischen
// Arrays. Das zu verkleinernde Array wird an die
// Funktion übergeben. Als Ergebnis wird das
// verkleinerte Array zurückgegeben.
boolean[][] shrink(boolean[][] in) {
  // Nur gültige Größen (gerade Anzahl an Feldern
  // und quadratisch) akzeptieren
  if ( in.length % 2 != 0 && in.length != in[0].length) {
    return null;
  }

  // Ausgabe-Array anlegen (halb so groß wie die Eingabe)
  boolean[][] out = new boolean[in.length / 2][in.length / 2];

  // Zähler, wie viele Schwarzwerte in dem 2x2-Element sind
  int numBlack = 0;

  // Für jedes Feld im Ausgabe-Array
  for (int i = 0; i < out.length; i++) {
    for (int j = 0; j < out.length; j++) {
      // Analyse: Gehe in Form von 2x2-Elementen das
      // Eingabe-Array durch und bestimme die Anzahl
      // an Schwarzwerten
      for (int k = 0; k < 2; k++) {
        for (int l = 0; l < 2; l++) {
          // Wenn kein Weißwert vorliegt,
          // dann Schwarzzähler erhöhen
          if (! in[k + i * 2][l + j * 2]) {
            numBlack = numBlack + 1;
          }
        }
      }

      // Wenn mindestens zweimal Schwarz vorkommt
      // schwarz im Ausgabe-Array speichern
      if (numBlack > 1)
        out[i][j] = false; // sonst weiß
      else
        out[i][j] = true;
        
      // Zähler resetten für nächstes 2x2-Element
      numBlack = 0;
    }
  }

  return out;
}

// Funktion zur grafischen Darstellung eines
// zweidimensionalen Arrays, welches an die
// Funktion übergeben wird
void displayArray(boolean[][] input) {
  // Höhe und Breite des Arrays bestimmen
  int iWidth = input[0].length;
  int iHeight = input.length;

  // Größe pro Rechteck, abhängig vom Bildschirmfenster
  int xSize = width / iWidth;
  int ySize = height / iHeight;

  // Gehe jede Zeile und Spalte durch
  for (int y = 0; y < iHeight; y++) {
    for (int x = 0; x < iWidth; x++) {
      // Bestimme Farbe
      // true = Setze Farbe auf Weiß
      if (input[y][x] == true)
        fill(255);
      // Sonst setze Farbe auf Grau
      else
        fill(125);
       
      // Male Kasten auf Bildschirm
      rect(x * xSize, y * ySize, xSize, ySize);
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(800, 800);

  boolean[][] bwImage =
    {
      {false, true,  false, false, true,  false},
      {true,  true,  false, false, true,  true},
      {true,  false, true,  true,  false, true},
      {true,  true,  true,  true,  true,  true},
      {false, true,  false, false, true,  false},
      {true,  false, false, false, false, true}
    };

  //displayArray(bwImage);
  displayArray(shrink(bwImage));
}

