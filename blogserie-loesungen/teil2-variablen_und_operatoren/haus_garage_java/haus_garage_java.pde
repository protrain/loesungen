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
int garageX = hausX + hausBreite;
int garageY = hausY + hausHoehe - garagenHoehe;


// Setze Fenstergröße auf 600x600 Pixel
size(800, 800);

// Setze Hintergrund auf weiß
background(weiss);

// Setze Strichfarbe auf Rot
stroke(rot);

// Setze Strichdicke auf 20 Pixel
strokeWeight(2);

// Rechteck malen
rect(hausX, hausY, hausBreite, hausHoehe);

// Dreieck malen
triangle(hausX, hausY,
  hausX+hausBreite, hausY,
  hausBreite, hausY-dachHoehe);  // Y-Koordinatensystem geht nach unten,
                                 // daher hausY-dachHoehe

// Male die Garage rechts an das Haus
rect(garageX, garageY, garagenBreite, garagenHoehe);
