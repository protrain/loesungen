// Farben
color weiss = color(255,255,255);
color rot = color(255, 0, 0);

// Hauseigenschaften
int hausX = 150;
int hausY = 200;

// Höhe und Breite des Hauses
int hausHoehe = 300;
int hausBreite = 300;

// Höhe des Dachs, was auf das Haus gesetzt wird
int dachHoehe = 100;

// Definiere Eigenschaften der Garage
int garagenHoehe = hausHoehe / 2;
int garagenBreite = hausBreite * 5/8;

// Setze Fenstergröße auf 600x600 Pixel
size(800, 800);

// Setze Hintergrund auf weiß
background(weiss);

// Setze Strichfarbe auf Rot
stroke(rot);

// Setze Strichdicke auf 20 Pixel
strokeWeight(2);

// Bewege Nullpunkt an Hauskoordinaten
translate(hausX, hausY);

// Rechteck malen
rect(0 ,0, hausBreite, hausHoehe);

// Dreieck malen
triangle(0, 0,
  hausBreite, 0,
  0.5*hausBreite, -dachHoehe);  // Y-Koordinatensystem geht nach unten,
                                // daher hausY-dachHoehe

// Bewege Nullpunkt weiter zu Garagenkoordinate
translate(hausBreite, hausHoehe - garagenHoehe);

// Male die Garage rechts an das Haus
rect(0, 0, garagenBreite, garagenHoehe);
