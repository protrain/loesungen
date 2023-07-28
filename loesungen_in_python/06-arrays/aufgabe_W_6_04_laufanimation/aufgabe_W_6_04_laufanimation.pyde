def setup():
    # Definiere globale Variablen
    # picture_no: Variable, die später als Zeiger auf das aktuell
    #            zu verwendende Bild verwendet wird
    # animation: Array für die Bilder
    global picture_no, animation

    # Grafischen Ausgabebereich initialisieren
    size(100, 100)
    background(255)

    # Bilder in Array einlesen
    animation = [loadImage("walk1.jpg"), loadImage("walk2.jpg"),
                 loadImage("walk3.jpg"), loadImage("walk4.jpg"),
                 loadImage("walk5.jpg"), loadImage("walk6.jpg")]

    # Aktuelle Bildnummer
    picture_no = 0

    # Setze Framerate auf 12 Bilder pro Sekunde
    frameRate(12)


def draw():
    global picture_no, animation

    # Lösche das vorherige Bild
    background(255)

    # Zeige aktuelles Bild an
    image(animation[picture_no], 10, 10)

    # Erhöhe Bilderzähler, solange das letzte Bild im Array
    # noch nicht erreicht wurde
    if picture_no < 5:
        picture_no += 1

    # sonst Zähler zurücksetzen
    else:
        picture_no = 0
