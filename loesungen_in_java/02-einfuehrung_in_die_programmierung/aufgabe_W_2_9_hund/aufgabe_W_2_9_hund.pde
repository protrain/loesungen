size(800, 800);

// Grundeinstellungen für die Linienumrandungen (Blauton in der
// Strichstärke 20 sowie abgerundete Enden)
stroke(40, 71, 124);
strokeWeight(20);
strokeCap(ROUND);
strokeJoin(ROUND);

// Schwanz
fill(40, 71, 124);
triangle(500, 600,  // links
    780, 620,       // unten
    780, 580);      // oben

// Körper (Trapez in der Mitte)
fill(255);
quad(200, 300,      // oben links
    500, 300,       // oben rechts
    600, 700,       // unten rechts
    100, 700);      // unten links

// Kopf (Trapez oben)
quad(100, 10,       // oben links
    500, 10,        // oben rechts
    500, 300,       // unten rechts
    10, 300);       // unten links

// Schlappohr
fill(40, 71, 124);
triangle(500, 10,   // Oben
    700, 500,       // Rechts unten
    500, 500);      // Links unten
fill(255);

// Linke Pfote
quad(200, 670,      // oben links
    300, 660,       // oben rechts
    310, 750,       // unten rechts
    170, 750);      // unten links

// Krallen der linken Pfote
line(220, 730, 220, 760);
line(280, 730, 280, 760);

// Rechte Pfote
quad(400, 670,      // oben links
    520, 660,       // oben rechts
    560, 750,       // unten rechts
    380, 750);      // unten links

// Krallen der rechten Pfote
line(430, 730, 430, 770);
line(500, 730, 500, 760);

// Gesicht
fill(40, 71, 124);
// Mal links
quad(100, 10, 200, 10, 200, 110, 75, 90);
// Mund
rect(150, 175, 125, 50);
// Augenzwinkern
strokeJoin(MITER);
rect(400, 100, 100, 10);

