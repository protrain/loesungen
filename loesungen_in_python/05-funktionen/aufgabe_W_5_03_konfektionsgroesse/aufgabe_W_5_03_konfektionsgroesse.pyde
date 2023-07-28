# Funktion zur Berechnung der Konfektionsgröße in Abhängigkeit des
# Geschlechts, der Körpergröße und des Brustumfangs. Die Werte werden
# an die Methode übergeben. Nach der Berechnung wird das Ergebnis als
# Integer zurückgegeben.
def compute_garment_size(is_female, body_height, bustline):
    garment_size = bustline / 2

    # Sonderfälle für Frauen
    if is_female:         # Wird Berechnung für eine Frau?
        garment_size -= 6      # Konfektionsgröße um 6 minimieren

        if body_height > 170:    # Ist die Frau größer als 170cm,
            garment_size *= 2    # Konfektionsgröße verdoppeln
        elif body_height < 164:  # und wenn kleiner als 164cm,
            garment_size /= 2    # Konfektionsgröße halbieren

    return garment_size          # Rückgabe der Konfektionsgröße


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

print(compute_garment_size(True, 167, 92))
