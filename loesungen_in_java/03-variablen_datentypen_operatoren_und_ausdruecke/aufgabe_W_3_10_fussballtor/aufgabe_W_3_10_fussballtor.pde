// Variablen setzen

// Farben setzen
color wiese = color(42, 211, 50);
color himmel = color(227, 248, 252);
color torpfosten = color(0, 0, 0);
color torkasten = color(255, 255, 255, 100);

// Höhe und Breite des Tors festlegen
int hoehe = 300;
float breite = 2.5 * hoehe;

// Torposition
int torX = 100;
int torY = 100;

// Oberer linker Eckpunkt des inneren Torkastens
float kastenX = breite * 1 / 8;
float kastenY = hoehe * 1 / 8;
float kastenBreite = breite * 3 / 4;
float kastenHoehe = hoehe * 5 / 8;

size(1000, 500);

// Hintergrund malen

// Hintergrundfarbe auf Himmelfarbe setzen
background(himmel);

// Wiesenfarbe setzen
stroke(wiese);
fill(wiese);

// Wiese ab halber Torhöhe zeichnen
rect(0, torY + hoehe / 2, 1000, 500);


// Tornetz zeichnen

strokeWeight(3);

// Setze volle Transparenz (vierter Parameter Alpha=0)
stroke(torkasten);
fill(torkasten);

// Verschiebe Nullpunkt in den Kasten
translate(torX + kastenX, torY + kastenY);

// Male inneren Torkasten
rect(0, 0, kastenBreite, kastenHoehe);

// Male obere Benetzung
quad(
  0,
  0,
  -kastenX,
  -kastenY,
  breite - kastenX,
  -kastenY,
  kastenBreite,
  0
);

// Male Benetzung links
quad(
  0,
  0,
  -kastenX,
  -kastenY,
  -kastenX,
  hoehe - kastenY,
  0,
  kastenHoehe
);

// Verschiebe Koordinatensystem an den rechten Kasten
translate(kastenBreite, 0);

// Male Benetzung rechts
quad(0, 0, kastenX, -kastenY, kastenX, hoehe - kastenY, 0, kastenHoehe);

translate(-kastenBreite, 0);

// Torpfosten malen

// Linienfarbe auf Pfostenfarbe setzen
stroke(torpfosten);

// Liniendicke auf 10 Pixel setzen
strokeWeight(10);

// Transformiere Koordinatensystem auf Pfosten
translate(-kastenX, -kastenY);

// Pfosten oben
line(0, 0, breite, 0);

// Pfosten links
line(0, 0, 0, hoehe);

// Gehe mit Koordinatensystem die Breite des Pfosten nach rechts
// womit wir an der rechten Pfostenposition sind
translate(breite, 0);

// Pfosten rechts
line(0, 0, 0, hoehe);
