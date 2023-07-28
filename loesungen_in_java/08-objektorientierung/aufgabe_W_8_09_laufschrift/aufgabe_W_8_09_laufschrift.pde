// Klasse, welche die Laufschrift realisiert
public class Ticker {
  // Position des Textes
  private int x, y;
  
  // Darzustellender Text
  private String text;
  private int textSize;
  
  // Laufgeschwindigkeit pro Frame
  private int speedPerFrame;
  
  // Konstuktor, welche den Text und die
  // Geschwindigkeit festlegt
  public Ticker(String text, int speedPerFrame) {
    this.text = text;
    this.textSize = height / 4;
    this.speedPerFrame = speedPerFrame;
    
    // Wir starten am Rand des Bildschirmfensters
    this.x = width;
    this.y = height / 2;
  }
  
  // Funktion, welche den Text für den aktuellen Frame
  // nach links bewegt
  public void moveText() {
    // Wir müssen die Breite des Textes wissen, damit
    // wir wissen, wann der Text nicht mehr zu sehen ist.
    textSize(this.textSize);
    int textWidth = int(textWidth(this.text));
    
    if (this.x < -textWidth) {
      // Text ist nicht mehr sichtbar, also bewegen
      // wir ihn wieder an den Anfang
      this.x = width;
    } else {
      this.x -= this.speedPerFrame;
    }
  }
  
  // Funktion, welche den Text auf den Bildschirm zeichnet
  public void drawText() {
    background(255);
    fill(0);
    textSize(this.textSize);
    textAlign(LEFT, CENTER);
    text(this.text, this.x, this.y);
  }
}

Ticker ticker;

public void setup() {
  size(100, 100);
  
  ticker = new Ticker("+++ Kaffee 1 Euro +++", 1);
}

public void draw() {
  ticker.drawText();
  ticker.moveText();
}
