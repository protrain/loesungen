# Funktion zur Berechnung des Bogenmaß
# Erhält die Gradzahl als Fließkommazahl und
# liefert das Bogenmaß zurück
def toRadians(degree):
    radian = degree / 180 * PI
    return radian

# Funktion zur Berechnung der Distanz zwischen zwei GPS-
# Koordinaten. Übergeben werden Breitengrad und Längengrad der
# ersten und der zweiten Koordinate
def gpsDistance(lat1, lon1, lat2, lon2):
    # Umrechnen in Bogenmaß
    lat1 = toRadians(lat1)
    lon1 = toRadians(lon1)
    lat2 = toRadians(lat2)
    lon2 = toRadians(lon2)

    # Berechne die Entfernung mithilfe vordefinierter
    # mathematischer Funktionen
    c = acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2)
             * cos(lon2 - lon1))
    d = c * 6378.137

    return d

# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    # GPS-Koordinaten Kölner Dom
    kdLat = 50.94157
    kdLon = 6.95821

    # GPS-Koordinaten Düsseldorfer Fernsehturm
    ftLat = 51.21795
    ftLon = 6.76165

    print gpsDistance(kdLat, kdLon, ftLat, ftLon)

    # GPS-Koordinaten Hamburger Elbphilharmonie
    hhLat = 53.54125
    hhLon = 9.9841

    # GPS-Koordinaten Münchener Frauenkirche
    muLat = 48.13663
    muLon = 11.57715

    print gpsDistance(hhLat, hhLon, muLat, muLon)

