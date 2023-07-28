// Setze Fenstergröße
size(600, 750);

// Setze Hintergrundfarbe
background(80);

// Zeichnungsparameter für Maske
strokeWeight(0);
stroke(230);
fill(230);

// Maske
// Oben links
triangle(50, 250, 200, 250, 200, 50);
// Oben rechts
triangle(200, 50, 400, 300, 200, 300);
// Mitte links
rect(50, 250, 150, 250);
// Mitte rechts
rect(200, 300, 200, 150);
// Unten links
triangle(50, 500, 200, 500, 200, 700);
// Unten rechts
triangle(200, 450, 400, 450, 200, 700);

// Zeichnungsparameter für Befestigung
strokeWeight(0);
stroke(255);
fill(255);

// Befestigung
// Oben
rect(300, 250, 250, 50);
// Mitte
rect(500, 300, 50, 150);
// Unten
rect(300, 450, 250, 50);
