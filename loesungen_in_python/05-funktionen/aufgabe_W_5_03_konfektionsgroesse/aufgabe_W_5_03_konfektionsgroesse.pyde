# Funktion zur Berechnung der Konfektionsgröße in Abhängigkeit des
# Geschlechts, der Körpergröße und des Brustumfangs. Die Werte werden
# an die Methode übergeben. Nach der Berechnung wird das Ergebnis als
# Integer zurückgegeben.
def computeGarmentSize(isFemale, bodyHeight, bustline):
    garmentSize = bustline / 2

    # Sonderfälle für Frauen
    if isFemale: 				# Wird Berechnung für eine Frau?
        garmentSize -= 6	    # Konfektionsgröße um 6 minimieren

        if bodyHeight > 170:    # Ist die Frau größer als 170cm,
            garmentSize *= 2    # Konfektionsgröße verdoppeln
        elif bodyHeight < 164:  # und wenn kleiner als 164cm,
            garmentSize /= 2    # Konfektionsgröße halbieren

    return garmentSize          # Rückgabe der Konfektionsgröße


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

print computeGarmentSize(True, 167, 92)

