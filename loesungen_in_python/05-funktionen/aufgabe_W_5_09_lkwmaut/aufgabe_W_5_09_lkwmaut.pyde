# Funktion zur Berechnung der LKW-Maut in Abhängigkeit der
# Schadstoffklasse, der Anzahl an Achsen und der gefahrenen Kilometer.
# Die Werte werden an die Funktion übergeben. Das Ergebnis der
# Berechnung wird als Fließkommazahl in Euro-Cent zurückgegeben
def lkw_maut(schadstoffklasse, num_achsen, km):
    # Lege Python-Dictionary zur Bestimmung des Preises an
    preis_tabelle = [{"A": 12.5,    # Wenn die Anzahl der Achsen <= 3
                      "B": 14.6,
                      "C": 15.7,
                      "D": 18.8,
                      "E": 19.8,
                      "F": 20.8},
                     {"A": 13.1,    # ab vier Achsen
                      "B": 15.2,
                      "C": 16.3,
                      "D": 19.4,
                      "E": 20.4,
                      "F": 21.4}]

    # Bestimme Km-Preis
    # Wenn die Anzahl der Achsen <= 3
    if num_achsen <= 3:
        # Schadstoffklasse aus Dictionary holen
        km_preis = preis_tabelle[0][schadstoffklasse]
    # Sonst ab 4 Achsen
    else:
        # Schadstoffklasse aus Dictionary holen
        km_preis = preis_tabelle[1][schadstoffklasse]

    # gebe die berechnete LKW-Maut zurück
    return km_preis * km


# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

zeile = "LKW-Maut für 13 km eines 2-Achsers der Schadstoffklasse A: "
zeile += str(lkw_maut("A", 2, 13)) + " Euro-Cent"
print(zeile)

zeile = "LKW-Maut für 13 km eines 5-Achsers der Schadstoffklasse D: "
zeile += str(lkw_maut("D", 5, 13)) + " Euro-Cent"
print(zeile)
