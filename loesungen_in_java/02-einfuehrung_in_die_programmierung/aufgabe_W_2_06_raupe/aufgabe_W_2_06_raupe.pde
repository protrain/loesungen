size(800, 400);
background(255);

// Alles, was gezeichnet wird, hat eine schwarze Linienumrandung der
// Strichstärke 2.
stroke(0);
strokeWeight(2);

// Kopf
fill(2, 153, 53);
ellipse(100, 100, 150, 150);

// Augen
fill(255);
ellipse(40, 60, 50, 50);
ellipse(80, 60, 50, 50);

// Die Schnittstelle, an der sich die Linienumrandungen beider Augen
// überlappen, muss überzeichnet werden. Damit die Ellipse, mit der dieser
// Bereich überzeichnet wird, nicht sichtbar ist, wird die Linienfarbe
// für die Anweisung auf weiß gesetzt.
stroke(255);
ellipse(60, 60, 25, 28);
stroke(0);

// Pupillen
fill(0);
ellipse(50, 60, 20, 20);
ellipse(70, 60, 20, 20);

// Restlicher Körper
fill(2, 153, 53);
ellipse(175, 210, 150, 150);
ellipse(275, 230, 150, 150);
ellipse(375, 210, 150, 150);
ellipse(475, 230, 150, 150);
ellipse(575, 210, 150, 150);
