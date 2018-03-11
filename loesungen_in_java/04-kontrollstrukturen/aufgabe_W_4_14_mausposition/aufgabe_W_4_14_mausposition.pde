public void setup() {
  size(800, 800);
}

public void draw() {
  // Position und Größe des Buttons
  int x = 200;
  int y = 300;
  int w = 400;
  int h = 200;

  // Färbe Rechteck von Mausposition ein
  // Wenn Maus direkt über Rechteck -> Grün
  if (mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + h) {
    fill(0, 255, 0);
  }
  // Sonst Blau
  else {
    fill(0, 0, 255);
  }

  // Zeichne Rechteck
  rect(x, y, w, h);
}

