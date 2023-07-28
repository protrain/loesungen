# Funktion zur Berechnung des Bogenmaß
# Erhält die Gradzahl als Fließkommazahl und
# liefert das Bogenmaß zurück

# Bei der Ausführung in einer reinen Python-Umgebung, muss die
# Libraries importiert werden
from math import acos, cos, pi as PI, sin


def to_radians(degree):
    radian = degree / 180 * PI
    return radian


# Funktion zur Berechnung der Distanz zwischen zwei GPS-
# Koordinaten. Übergeben werden Breitengrad und Längengrad der
# ersten und der zweiten Koordinate
def gps_distance(lat_1, lon_1, lat_2, lon_2):
    # Umrechnen in Bogenmaß
    lat_1 = to_radians(lat_1)
    lon_1 = to_radians(lon_1)
    lat_2 = to_radians(lat_2)
    lon_2 = to_radians(lon_2)

    # Berechne die Entfernung mithilfe vordefinierter
    # mathematischer Funktionen
    c = acos(sin(lat_1) * sin(lat_2) + cos(lat_1) * cos(lat_2)
             * cos(lon_2 - lon_1))
    d = c * 6378.137

    return d


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    # GPS-Koordinaten Kölner Dom
    kd_lat = 50.94157
    kd_lon = 6.95821

    # GPS-Koordinaten Düsseldorfer Fernsehturm
    ft_lat = 51.21795
    ft_lon = 6.76165

    print(gps_distance(kd_lat, kd_lon, ft_lat, ft_lon))

    # GPS-Koordinaten Hamburger Elbphilharmonie
    hh_lat = 53.54125
    hh_lon = 9.9841

    # GPS-Koordinaten Münchener Frauenkirche
    mu_lat = 48.13663
    mu_lon = 11.57715

    print(gps_distance(hh_lat, hh_lon, mu_lat, mu_lon))

# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
