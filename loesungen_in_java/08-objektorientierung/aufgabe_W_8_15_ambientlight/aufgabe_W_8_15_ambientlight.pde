// Importieren der AWT-Bibliothek
import java.awt.*;

// Klasse, die die Ansteuerung einer LED realisiert
class AmbiLight {
  // Deklaration privater Variablen
  private int h, s, b;

  // Konstruktor, der die Werte für Hue, Saturation und Brightness
  // erwartet.
  public AmbiLight(int h, int s, int b) {
    this.h = h;
    this.s = s;
    this.b = b;
  }

  // Öffentliche Methode zum Erhöhen der Farbsättigung
  public void increaseSaturation() {
    if (s < 100) {
      s = s + 1;
    }
    else {
      s = 100;
    }
  }

  // Öffentliche Methode zum Herabsetzen der Farbsättigung
  public void decreaseSaturation() {
    if (s > 0) {
      s = s - 1;
    }
    else {
      s = 0;
    }
  }

  // Öffentliche Methode zur Erhöhung der Helligkeit
  public void increaseBrightness() {
    if (b < 100) {
      b = b + 1;
    }
    else {
      b = 100;
    }
  }

  // Öffentliche Methode zum Herabsetzen der Helligkeit
  public void decreaseBrightness() {
    if (b > 0) {
      b = b - 1;
    }
    else {
      b = 0;
    }
  }

  // Öffentliche Methode, um die Werte für die nächstmögliche
  // Farbe zu generieren
  public int[] getNextColor() {
    // Erhöhe Farbwert
    h = h + 1;

    // Wenn Hue den maximalen Farbwert (360 Grad) überschreitet,
    // beginne bei 0 Grad
    if (h > 360) {
      h = 0;
    }

    // gebe Farbe als RGB-Farbwert zurück
    return hsbToRgb(h, s, b);
  }

  // Öffentliche Methode zum Generieren einer Zufallsfarbe
  public int[] getRandomColor() {
    h = int(random(0, 360));
    s = int(random(0, 100));
    b = int(random(0, 100));

    return hsbToRgb(h, s, b);
  }

  // Private Funktion zur Umrechnung von HSB nach RGB-Werten
  // An die Funktion werden die Werte für die Farbe, die
  // Sättigung und die Helligkeit übergeben.
  // Die Funktion liefert ein Array mit den RGB-Werten zurück.
  private int[] hsbToRgb(int h, int s, int b) {
    // Wandle HSB in RGB um
    // Dividiere die HSB-Werte, damit die Werte zwischen
    // 0 und 1 liegen (notwendig zur Java-Berechnung)
    int rgb = Color.HSBtoRGB(h, s / 100.0, b / 100.0);
    // Erzeuge Color-Objekt
    Color c = new Color(rgb);
    // Gebe Farbbestandteile zurück
    int[] output = {
      c.getRed(),
      c.getGreen(),
      c.getBlue()
    };
    return output;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  AmbiLight al = new AmbiLight(0, 0, 50);

  for (int i = 0; i < 50; i++) {
    al.increaseBrightness();
    println(al.getNextColor());
  }
}
