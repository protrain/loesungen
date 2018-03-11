def setup():
    size(800, 800)


def draw():
    # Position, Breite und Höhe des Buttons
    x = 200
    y = 300
    w = 400
    h = 200

    # Färbe Rechteck von Mausposition ein
    # Wenn Maus direkt über Rechteck -> Grün
    if mouseX > x and mouseX < x + w and mouseY > y and mouseY < y + h:
        fill(0, 255, 0)
    # Sonst Blau
    else:
        fill(0, 0, 255)

    # Zeichne Rechteck
    rect(x, y, w, h)

