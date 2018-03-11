// Funktion zur Anwendung eines Medianfilters
// auf ein übergebenes Bild. Das Ergebnisbild
// wird von der Funktion zurückgegeben.
PImage MedianFilter(PImage input) {
  // Bildausschnittsarray mit 9 Werten
  int[] area = new int[9];
  int[] grey = new int[9];

  PImage output = new PImage(input.width, input.height);

  // Gehe für jedes Pixel einzeln durch
  for (int y = 1; y < input.height - 1; y++) {
    for (int x = 1; x < input.width - 1; x++) {
      // Hole Ausschnitt aus Input
      int num = 0;

      // x,y-Zähler für 3x3-Block
      for (int j = -1; j <= 1; j++) {
        for (int k = -1; k <= 1; k++) {
          // speichere die umliegenden Elemente
          // im area-Array
          area[num] = input.get(x + k, y + j);
          num = num + 1;
        }
      }

      // Berechne Grauwerte aus den extrahierten
      // umliegenden Punkten (area-Array)
      for (int i = 0; i < area.length; i++) {
        grey[i] = int(
          red(area[i]) * 0.299
            + green(area[i]) * 0.581
            + blue(area[i]) * 0.114
        );
      }

      // Sortiere Pixel
      grey = sort(grey);

      // Nehme mittleren Wert
      int median = grey[4];

      // Schreibe Median in Ausgangspixel
      output.set(x, y, color(median, median, median));
    }
  }

  return output;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(1000, 1000);

  PImage image = loadImage("image.png");
  PImage imageFiltered = MedianFilter(image);

  image(imageFiltered, 0, 0);
}

