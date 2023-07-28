// Funktion, welche ein Bild in Pixelart umwandelt
public void generatePixelart(String imagePath, int scaleFactor) {
  // Lade Bild in das Fenster
  PImage img = loadImage(imagePath);
  image(img, 0, 0);
  
  // Bestimme Bildhöhe und -breite
  int imgHeight = img.height;
  int imgWidth = img.width;
    
  // Für jeden Pixel nach der Skalierschrittweite
  for (int y = 0; y < imgHeight; y += scaleFactor) {
    for (int x = 0; x < imgWidth; x += scaleFactor) {
      // Hole Pixelfarbe an Stelle (x, y)
      color pixelColor = get(x, y);
            
      // Male Viereck der Größe scaleFactor x scaleFactor
      fill(pixelColor);
      // Deaktiviere 
      noStroke();
      rect(x, y, scaleFactor, scaleFactor);
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  // Setze die Fenstergröße
  size(510, 340);

  // Lade Bild
  generatePixelart("./bild.jpg", 10);
  //generatePixelart("./bild.jpg", 20);
}
