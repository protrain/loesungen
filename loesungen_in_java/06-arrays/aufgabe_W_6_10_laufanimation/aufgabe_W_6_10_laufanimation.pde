// Array für die Bilder deklarieren und initialisieren
PImage[] animation = new PImage[6];

// Variable, die später als Zeiger auf das aktuell
// zu verwendende Bild verwendet wird
int pictureNo;

void setup() {
  // Grafischen Ausgabebereich initialisieren
  size(100, 100);
  background(255);

  // Bilder in Array einlesen
  animation[0] = loadImage("walk1.jpg");
  animation[1] = loadImage("walk2.jpg");
  animation[2] = loadImage("walk3.jpg");
  animation[3] = loadImage("walk4.jpg");
  animation[4] = loadImage("walk5.jpg");
  animation[5] = loadImage("walk6.jpg");

  // Aktuelle Bildnummer
  pictureNo = 0;

  // Setze Framerate auf 12 Bilder pro Sekunde
  frameRate(12);
}

void draw() {
  // Lösche das vorherige Bild
  background(255);

  // Zeige aktuelles Bild an
  image(animation[pictureNo], 10, 10);

  // Erhöhe Bilderzähler, solange das letzte Bild im Array
  // noch nicht erreicht wurde
  if (pictureNo < 5)
    pictureNo += 1;
  // sonst Zähler zurücksetzen
  else
    pictureNo = 0;
}

