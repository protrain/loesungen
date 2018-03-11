def setup():
    # Definiere globale Variablen
    # pictureNo: Variable, die später als Zeiger auf das aktuell
    #            zu verwendende Bild verwendet wird
    # animation: Array für die Bilder
    global pictureNo, animation

    # Grafischen Ausgabebereich initialisieren
    size(100, 100)
    background(255)

    # Bilder in Array einlesen
    animation = [loadImage("walk1.jpg"), loadImage("walk2.jpg"),
                 loadImage("walk3.jpg"), loadImage("walk4.jpg"),
                 loadImage("walk5.jpg"), loadImage("walk6.jpg")]

    # Aktuelle Bildnummer
    pictureNo = 0

    # Setze Framerate auf 12 Bilder pro Sekunde
    frameRate(12)


def draw():
    global pictureNo, animation

    # Lösche das vorherige Bild
    background(255)

    # Zeige aktuelles Bild an
    image(animation[pictureNo], 10, 10)

    # Erhöhe Bilderzähler, solange das letzte Bild im Array
    # noch nicht erreicht wurde
    if pictureNo < 5:
        pictureNo += 1

    # sonst Zähler zurücksetzen
    else:
        pictureNo = 0

