// Importieren der AWT-Bibliothek
import java.awt.*;

// Klasse, die die Ansteuerung einer LED realisiert
// Fixes für https://raw.githubusercontent.com/protrain/loesungen/master/loesungen_in_java/08-objektorientierung/aufgabe_W_8_12_ambientlight/aufgabe_W_8_12_ambientlight.pde:
// - Randomzahlen inkl. Upper Bound
// - Hue Wert in Color.HSBtoRGB korrekt berechnet
// - Da Color.HSBtoRGB eine Umwandlung von HSB/HSV (nicht HSL) vornimmt, Variablen/Kommentare angepasst

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
    // FIX siehe https://processing.org/reference/random_.html
    // FIX random(-5, 10.2) returns values starting at -5 and up to (but not including) 10.2.
    // FIX um Zufallszahlen im ganzen Intervall zu erhalten --> Upper Bound + 1
    h = int(random(0, 360 + 1));
    s = int(random(0, 100 + 1));
    b = int(random(0, 100 + 1));

    return hsbToRgb(h, s, b);
  }

  // Private Funktion zur Umrechnung von HSB nach RGB-Werten
  // An die Funktion werden die Werte für die Farbe, die
  // Sättigung und die Helligkeit übergeben.
  // Die Funktion liefert ein Array mit den RGB-Werten zurück.
  private int[] hsbToRgb(int h, int s, int b) {
    // Wandle HSB in RGB um
    // Dividiere die hsb-Werte, damit die Werte zwischen
    // 0 und 1 liegen (notwendig zur Java-Berechnung)
    // FIX h muss durch 360.0f dividiert werden
    int rgb = Color.HSBtoRGB(h / 360.0f, s / 100.0f, b / 100.0f);
    // Erzeuge Color-Objekt
    Color c = new Color(rgb);
    // Gebe Farbbestandteile zurück
    return new int[] {
      c.getRed(),
      c.getGreen(),
      c.getBlue()
    };
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

