// Importieren der AWT-Bibliothek
import java.awt.*;

// Klasse, die die Ansteuerung einer LED realisiert
class AmbiLight {
  // Deklaration privater Variablen
  private int h, s, l;

  // Konstruktor, der die Werte für Hue, Saturation und Lightness
  // erwartet.
  public AmbiLight(int h, int s, int l) {
    this.h = h;
    this.s = s;
    this.l = l;
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
  public void increaseLightness() {
    if (l < 100) {
      l = l + 1;
    }
    else {
      l = 100;
    }
  }

  // Öffentliche Methode zum Herabsetzen der Helligkeit
  public void decreaseLightness() {
    if (l > 0) {
      l = l - 1;
    }
    else {
      l = 0;
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
    return hslToRgb(h, s, l);
  }

  // Öffentliche Methode zum Generieren einer Zufallsfarbe
  public int[] getRandomColor() {
    h = int(random(0, 360));
    s = int(random(0, 100));
    l = int(random(0, 100));

    return hslToRgb(h, s, l);
  }

  // Private Funktion zur Umrechnung von HSL nach RGB-Werten
  // An die Funktion werden die Werte für die Farbe, die
  // Sättigung und die Helligkeit übergeben.
  // Die Funktion liefert ein Array mit den RGB-Werten zurück.
  private int[] hslToRgb(int h, int s, int l) {
    // Wandle HSL in RGB um
    // Dividiere die hsl-Werte, damit die Werte zwischen
    // 0 und 1 liegen (notwendig zur Java-Berechnung)
    int rgb = Color.HSBtoRGB(h, s / 100.0, l / 100.0);
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
    al.increaseLightness();
    println(al.getNextColor());
  }
}

