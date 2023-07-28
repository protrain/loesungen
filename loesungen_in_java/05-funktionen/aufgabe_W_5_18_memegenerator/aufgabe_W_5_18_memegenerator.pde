// Funktion, welche die passende Schriftgröße
// für einen Text bestimmt und setzt.
public int getFontSize(
  String text,
  int maxFontSize,
  int imgWidth
) {
  // Starte zunächst bei der maximal gewollten
  // Schriftgröße
  int fontSize = maxFontSize;
  
  // Gehe so lange die Schrifgröße herunter
  // bis die Schrift in das Fenster passt
  textSize(fontSize);
  while (textWidth(text) > imgWidth) {
    if (fontSize <= 0) {
      // Wir brechen ab, wenn da wir eine ungültige
      // Schriftgröße bekommen
      break;
    }
    
    // Reduziere Schriftgröße um 5 Pixel
    fontSize -= 5;
    textSize(fontSize);
  }
  
  return fontSize;
}

public void generateMeme(
  String imagePath,
  String textTop,
  String textBottom
) {
  // Lade Bild
  PImage img = loadImage(imagePath);
  
  // Abmessungen des Eingabebilds
  int imgWidth = img.width;
  int imgHeight = img.height;

  // Lade die Schrift für das Meme
  // Die Schriftart muss noch in den externe_daten-Ordner
  // gestellt werden, damit der Code ausgeführt wird.
  String fontPath = "../../../externe_daten/anton-font/"
    + "data/Anton-Regular.ttf";
  PFont anton = createFont(fontPath, 200);
  
  // Setze Schriftart
  textFont(anton);
  
  // Zentriere Text
  textAlign(CENTER);
  
  // Weiße Schrift
  fill(255);
    
  // Zeichne schwarzen Hintergrund
  background(0);
  
  // Zeichne Bild
  image(img, 0, 0);
  
  // Setze Text oben
  int fontSize = getFontSize(textTop, 80, imgWidth);
  textSize(fontSize);
  text(textTop, imgWidth/2, fontSize);
  
  // Setze Text unten
  fontSize = getFontSize(textBottom, 80, imgWidth);
  textSize(fontSize);
  text(textBottom, imgWidth/2, imgHeight - 10);
  
  // Speichere Bild als JPG-Datei
  save("meme.jpg");
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  // Setze die Fenstergröße
  size(510, 340);

  String imagePath = "./bild.jpg";

  generateMeme(
    imagePath,
    "MY REACTION",
    "WHEN I SEE GOOD JAVA CODE"
  );
  
  /*generateMeme(
    imagePath,
    "WHEN I SEE YOU",
    "I GO NUTS"
  );*/
}
