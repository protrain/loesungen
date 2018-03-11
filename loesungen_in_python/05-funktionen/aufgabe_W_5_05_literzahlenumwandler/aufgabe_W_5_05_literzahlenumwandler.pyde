# Funktion zur Umrechnung von Volumenangaben
# Erhält das Volumen als Fließkommazahl und gibt den berechneten
# Wert mit der Einheit als String zurück


def volumeConverter(volume):
    # ist das Volumen größer oder gleich 1.0
    if volume >= 1.0:
        return str(volume) + " l"  # dann Rückgabe Wert mit Einheit "l"

    # sonst prüfe, ob Volumen größer oder gleich 0.1
    elif volume >= 0.1:
        # Umrechnen Wert auf cl
        result = int(volume * 100) / 1
        return str(result) + " cl"      # Rückgabe Wert mit Einheit "cl"

    # ansonsten prüfe, ob Volumen größer oder gleich 0.001
    elif volume >= 0.001:
        # Umrechnen Wert auf ml
        result = int(volume * 1000) / 1
        return str(result) + " ml"      # Rückgabe Wert mit Einheit "ml"

    # ansonsten gib Fehlermeldung als Wert der Umwandlung zurück
    else:
        return "Number too small!"


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

print volumeConverter(1.0)
print volumeConverter(0.42)
print volumeConverter(0.023)
print volumeConverter(0.00023)

