// Klasse die ein klickbares Puzzleteil repräsentiert
public class PuzzlePiece {
  private PImage image;
  private int x, y, rotation;
  private int imgSize;
  
  // Konstruktor, der ein Bild, die
  // Koordinaten und die Rotation erwartet
  public PuzzlePiece(
    PImage image,
    int x,
    int y,
    int rotation,
    int imgSize
  ) {
    this.image = image;
    this.x = x;
    this.y = y;
    this.rotation = rotation;
    this.imgSize = image.width;
  }
  
  // Funktion, welches das Bild auf den Bildschirm zeichnet
  public void render() {    
    // Bestimme den Mittelpunkt des Bildes
    int xCenter = this.x + this.imgSize / 2;
    int yCenter = this.y + this.imgSize / 2;
    
    // Bewege Mittelpunkt des Koordinatensystems in
    // die Mitte des Bildes. Wir müssen das machen,
    // damit wir das Bild in der Mitte drehen können.
    translate(xCenter, yCenter);
    
    // Drehe Koordinatensystem um angegebenen Rotationswinkel
    rotate(radians(this.rotation));

    // Setze das Koordinatensystem des Bildes auf die
    // Mitte, damit wir das Bild an der geplanten
    // Stelle malen können.
    imageMode(CENTER);
    
    // Male das Bild
    image(this.image, 0, 0, imgSize, imgSize);
    
    // Rotiere und bewege das Koordinatensystem zurück,
    // damit wir andere Elemente wieder malen können.
    rotate(radians(-this.rotation));
    translate(-xCenter, -yCenter);
  }
  
  // Funktion, welche prüft, ob das Bild geklickt wurde
  private boolean imageClicked(int x, int y) {
     // Berechne den Bildbereich oben links und unten rechts.
    int topLeftX = this.x;
    int topLeftY = this.y;
    int bottomRightX = this.x + this.imgSize;
    int bottomRightY = this.y + this.imgSize;
    
    // Prüfe, ob Klick im Bildbereich erfolgt ist
    return
      x > topLeftX && x < bottomRightX
      && y > topLeftY && y < bottomRightY;
  }
  
  // Funktion, welche das Bild um 90 Grad nach rechts dreht
  private void rotateRight() {
    this.rotation = (this.rotation + 90) % 360;
  }
  
  // Funktion, welche eine Klickaktion verarbeitet.
  public void handleClick() {
    if (this.imageClicked(mouseX, mouseY)) {
      // Rotiere Bild um 90 Grad
      this.rotateRight();
    }
  }
  
  // Funktion, welche die Bildrotation zurückgibt
  public int getRotation() {
    return this.rotation;
  }
}

public class RotationPuzzleGame {
  PuzzlePiece[][] puzzleField;
  PImage mainImage;
  boolean solved;
  
  // Konstruktor, der die Puzzlegröße als Integer erwartet
  public RotationPuzzleGame(int puzzleSize) {
    // Initialisiere das Spielfeld
    puzzleField = new PuzzlePiece[puzzleSize][puzzleSize];
    
    // Puzzle ist noch nicht gelöst
    this.solved = false;
    
    // Lade das Hauptbild
    PImage mainImage = loadImage("dog.png");
    this.mainImage = mainImage;
    
    // Bestimme Größe der Bild-Einzelteile
    int imgSplitSizeX = mainImage.width / puzzleSize;
    int imgSplitSizeY = mainImage.height / puzzleSize;
    
    // Splitte das Bild in Einzelteile
    for (int y = 0; y < puzzleSize; y++) {
      for (int x = 0; x < puzzleSize; x++) {
        // Erstelle neues Bildobjekt für Puzzleteil
        PImage puzzlePiece = createImage(
          imgSplitSizeX,
          imgSplitSizeY,
          RGB  
        );
        
        // Startposition des Bildschnipsels im Hauptbild
        int splitStartPosX = imgSplitSizeX * x;
        int splitStartPosY = imgSplitSizeY * y;
        
        // Kopiere Bildbereich von großem Bild in das Puzzleteil
        puzzlePiece = mainImage.get(
          splitStartPosX,
          splitStartPosY,
          imgSplitSizeX,
          imgSplitSizeY
        );
                
        // Packe Puzzleteil in das Spielfeld
        puzzleField[y][x] = new PuzzlePiece(
          puzzlePiece,
          splitStartPosX,
          splitStartPosY,
          getRandomRotation(),
          imgSplitSizeX
        );
      }
    }
  }
 
  
  // Funktion, welche das Spielfeld darstellt
  public void render() {
    // Gehe alle Elemente des Spielfeldes einzeln durch
    for (int y = 0; y < this.puzzleField.length; y++) {
      for (int x = 0; x < this.puzzleField[0].length; x++) {
        // Male Einzelbild auf Bildschirm
        puzzleField[y][x].render();
      }
    }
    
    // Prüfen, ob Puzzle gelöst ist
    this.checkStatus();
  }
  
  // Funktion, welche die Clicks verarbeitet
  public void handleClick() {
    // Gehe alle Elemente des Spielfeldes einzeln durch
    for (int y = 0; y < this.puzzleField.length; y++) {
      for (int x = 0; x < this.puzzleField[0].length; x++) {
        // Male Einzelbild auf Bildschirm
        puzzleField[y][x].handleClick();
      }
    }
  }
  
  // Funktion, welche eine zufälligen Bildrotation in 90-Grad-
  // Winkeln zurückgibt
  private int getRandomRotation() {
    int[] rotations = {0, 90, 180, 270};
    
    // Bestimme Zufallszahl zwischen 0 und 3
    int randomNumber = int(random(0, 4));
    
    return rotations[randomNumber];
  }
  
  // Funktion, welche prüft, ob das Spiel geschafft wurde
  private void checkStatus() {
    // Gehe alle Elemente des Spielfeldes einzeln durch
    for (int y = 0; y < this.puzzleField.length; y++) {
      for (int x = 0; x < this.puzzleField[0].length; x++) {
        // Hole Rotation des Puzzleteils
        int rotation = puzzleField[y][x].getRotation();
        
        // Wir brechen ab, sofern nicht alle Spielfelder die
        // richtige Rotation von 0 Grad haben
        if (rotation != 0) {
          return;
        }
      }
    }
    
    // Wenn wir hier landen, ist das Puzzle gelöst. Nun können die
    // Puzzleteile nicht mehr bewegt werden.
    this.solved = true;

    int fontSize = 39;
    int imgCenterX = this.mainImage.width / 2;
    int imgCenterY = this.mainImage.height + fontSize;
    
    fill(0, 0, 255);
    textAlign(CENTER);
    textSize(fontSize);
    text("Puzzle gelöst!",imgCenterX, imgCenterY);
  }
}


RotationPuzzleGame game;

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  size(300, 350);
  
  game = new RotationPuzzleGame(4);
}

public void mouseClicked() {
  game.handleClick();
}

public void draw() {
  if (game.solved == false ) {
     game.render();
  } 
}
