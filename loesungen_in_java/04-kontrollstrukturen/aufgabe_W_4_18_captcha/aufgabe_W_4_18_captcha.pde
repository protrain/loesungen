// Konstanten für die Antwort
int NOSOLUTION = -1;
// Richtige Antwort
int CORRECT = 1;
// Falsche Antwort
int WRONG = 0;

// Noch keine Lösung angeklickt
int solution = NOSOLUTION;

PImage imgLeft, imgMiddle, imgRight;
int imgWidth;
int correctX1, correctY1, correctX2, correctY2;

void setup() {
  // Definiere Fenstergröße
  size(600, 200);
  
  // Setze Hintergrundfarbe auf weiß
  background(255);
  
  // Lade CAPTCHA-Bild mit korrekter Lösung
  PImage dog0 = loadImage("./dog0.png");
  PImage dog90 = loadImage("./dog90.png");
  PImage dog180 = loadImage("./dog180.png");
  PImage dog270 = loadImage("./dog270.png");

  
  // Leite Höhe und Breite des Bildes ab
  imgWidth = dog0.width;
  int imgHeight = dog0.height;
  
  // Wähle zufällig Bildposition (Stellen 0-2) aus
  // welche die Richtige ist
  int correctImage = int(random(0, 3));
  
  // Berechne den Klickbereich, an dem wir mit einem
  // korrekt geratenen Bild rechnen
  
  // Oben links
  correctX1 = imgWidth * correctImage;
  correctY1 = 0;
  // Unten rechts
  correctX2 = imgWidth * (correctImage + 1);
  correctY2 = imgHeight;
  
  // Setze die Bilder für die entsprechenden Positionen.
  if (correctImage == 0) {
    imgLeft = dog0;
  } else {
    // Wähle Zufallszahl und bestimme danach zufälliges
    // "falsches" Bild
    int randomInt = int(random(0, 3));
    switch (randomInt) {
      case 0:
        imgLeft = dog90;
        break;
      case 1:
        imgLeft = dog180;
        break;
      default:
        imgLeft = dog270;
        break;
    }
  }
  
  if (correctImage == 1) {
    imgMiddle = dog0;
  } else {
    // Wähle Zufallszahl und bestimme danach zufälliges
    // "falsches" Bild
    int randomInt = int(random(0, 3));
    switch (randomInt) {
      case 0:
        imgMiddle = dog90;
        break;
      case 1:
        imgMiddle = dog180;
        break;
      default:
        imgMiddle = dog270;
        break;
    }
  }
  
  if (correctImage == 2) {
    imgRight = dog0;
  } else {
    // Wähle Zufallszahl und bestimme danach zufälliges
    // "falsches" Bild
    int randomInt = int(random(0, 3));
    switch (randomInt) {
      case 0:
        imgRight = dog90;
        break;
      case 1:
        imgRight = dog180;
        break;
      default:
        imgRight = dog270;
        break;
    }
  }  
}

void draw() {
  if (solution == WRONG) {
    // Falsche Antwort
    // Zeichne roten Hintergrund
    background(255, 0, 0);
  } else if(solution == CORRECT) {
    // Richtige Antwort
    // Zeichne blauen Hintergrund
    background(0, 0, 255);
  } else {
    // Es wurde noch kein Bild angeklickt
    // Zeichne Bild
    image(imgLeft, 0, 0);
    image(imgMiddle, imgWidth, 0); 
    image(imgRight, imgWidth*2, 0);
  }
}

// Funktion, welche Mausklicks verarbeitet
public void mouseClicked() {
  // Prüfe, ob Position der Maus im korrekten
  // Klickbereich liegt
  if (
    mouseX > correctX1 && mouseX < correctX2
    && mouseY > correctY1 && mouseY < correctY2
  ) {
      solution = CORRECT;
    } else {
      solution = WRONG;
    }
}
