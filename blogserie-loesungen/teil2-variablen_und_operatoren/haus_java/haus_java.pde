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

// Setze Fenstergröße auf 600x600 Pixel
size(600,600);

// Setze Hintergrund auf weiß
background(weiss);

// Setze Strichfarbe auf Rot
stroke(rot);

// Setze Strichdicke auf 20 Pixel
strokeWeight(2);

// Hausfassade: Rechteck malen
rect(hausX, hausY, hausBreite, hausHoehe);

// Hausdach: Dreieck malen
triangle(hausX, hausY,
  hausX+hausBreite, hausY,
  hausBreite, hausY-dachHoehe);  // Y-Koordinatensystem geht nach unten,
                                 // daher hausY-dachHoehe
