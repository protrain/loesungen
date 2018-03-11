size(800, 800)
background(255)
noStroke()

# Startwert für den Kreisradius
# Dieser muss ein Vielfaches von 255 sein, damit alle 255 Farbtöne in den
# Farbverlauf einfließen können.
radius = 510

# Gehe alle Grautöne von Weiß nach Schwarz durch
for c in range(255, 0, -1):
    # Ändere Farbe
    fill(c)

    # Zeichne einen Kreis
    ellipse(400, 400, radius, radius)

    # Verkleinere den Radius
    # Dadurch ergeben sich konzentrische Kreise, die immer kleiner werden
    # und dabei die Grautöne von Weiß (255) nach Schwarz (0) annehmen.
    radius -= 2

