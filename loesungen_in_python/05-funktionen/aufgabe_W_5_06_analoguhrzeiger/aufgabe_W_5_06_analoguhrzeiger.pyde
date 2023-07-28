# Funktion zur Berechnung des Winkels für den Stundenzeiger
# Die Stunden- und Minutenzahl werden als Integer-Werte an
# die Funktion übergeben, die als Ergebnis den Winkel als
# ganzzahligen Wert zurückgibt
def compute_hour_and_Angle(h, m):
    return (60 * h + m) / 2   # gibt Ergebnis der Berechnung zurück

# Funktion zur Berechnung des Winkels für den Minutenzeiger
# Die Minutenzahl wird als Ganzzahlwert an die Funktion übergeben.
# Die Funktion liefert den Winkel für den Minutenzeiger als
# Integer-Wert zurück.
def compute_minute_and_Angle(m):
    return 6 * m

# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    # Uhrzeit in Stunden und Minuten festlegen
    h = 3
    m = 33

    # Bestimme die beiden Winkel
    hAngle = compute_hour_and_Angle(h, m)
    mAngle = compute_minute_and_Angle(m)

    # Gebe Winkel aus
    zeile = "Der Stundenzeiger steht um " + str(h) + ":" + str(m)
    zeile += " Uhr auf " + str(hAngle) + " Grad."
    print(zeile)
    zeile = "Der Minutenzeiger steht um " + str(h) + ":" + str(m)
    zeile += " Uhr auf " + str(mAngle) + " Grad."
    print(zeile)

    # Zeichne analoge Zeitangabe in grafisches Ausgabefenster
    size(200, 200)
    translate(width / 2, height / 2)
    ellipse(0, 0, 180, 180)
    rotate(radians(hAngle))
    line(0, 0, 0, -60)
    rotate(-radians(hAngle))
    rotate(radians(mAngle))
    line(0, 0, 0, -80)
