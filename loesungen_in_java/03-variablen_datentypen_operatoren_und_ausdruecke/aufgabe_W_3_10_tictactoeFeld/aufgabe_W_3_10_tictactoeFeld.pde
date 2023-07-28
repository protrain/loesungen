size(170, 170);

// Initiale Startkoordinaten
int x = 10;
int y = 10;

// Breite und Höhe der Rechtecke
int w = 50;
int h = 50;

// Zeichne neun Rechtecke an die jeweiligen Stellen
rect(x, y, w, h);
rect(x, y + h, w, h);
rect(x, y + h * 2, w, h);
rect(x + w, y, w, h);
rect(x + w, y + h, w, h);
rect(x + w, y + h * 2, w, h);
rect(x + w * 2, y, w, h);
rect(x + w * 2, y + h, w, h);
rect(x + w * 2, y + h * 2, w, h);

