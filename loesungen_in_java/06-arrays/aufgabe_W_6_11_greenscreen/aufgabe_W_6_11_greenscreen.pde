// Funktion zum Verschmelzen zweier Bilder, die
// der Funktion als Parameter übergeben werden
PImage mergeImages(PImage greenscreen, PImage scene) {
  // Erzeuge leeres Ergebnisbild
  PImage resultImage = new PImage(scene.width, scene.height);

  // Lade alle Bilder in den Speicher
  greenscreen.loadPixels();
  scene.loadPixels();
  resultImage.loadPixels();

  // Gehe jedes Pixel einzeln durch
  for (int x = 0; x < scene.width; x++) {
    for (int y = 0; y < scene.height; y++) {
      // Position im Bild als fortlaufenden Index berechnen
      int idx = y * greenscreen.width + x;

      // Wenn Grün im Bild
      if (red(greenscreen.pixels[idx]) == 0 
            && green(greenscreen.pixels[idx]) == 255 
            && blue(greenscreen.pixels[idx]) == 0) {
        resultImage.pixels[idx] = scene.pixels[idx];
      }
      else {
        resultImage.pixels[idx] = greenscreen.pixels[idx];
      }
    }
  }
  resultImage.updatePixels();

  return resultImage;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  size(800, 800);

  // Lade Bild mit Greenscreen
  PImage gs = loadImage("green.png");

  // Lade Bild mit Hintergrund
  PImage sc = loadImage("bg.png");

  // Kombiniere beide Bilder
  PImage result = mergeImages(gs, sc);

  // Gebe kombiniertes Bild im Fenster aus
  image(result, 0, 0);
}

