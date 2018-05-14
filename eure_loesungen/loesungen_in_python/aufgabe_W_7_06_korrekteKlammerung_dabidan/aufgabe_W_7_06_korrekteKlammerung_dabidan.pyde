###################################################
# Lösung von dabidan (https://github.com/dabidan)
# "Funktion vereinfacht und an PEP8 angeglichen"
###################################################

def check_brackets(input):
    """ Funktion zur Überprüfung eines Strings auf eine gültige
    Klammerung. Der String wird an die Funktion übergeben.
    Diese liefert am Ende einen Wahrheitswert, der angibt,
    ob eine korrekte Klammerung vorliegt.
    """
    # Anzahl der noch geöffneten Klammern
    open_brackets = 0

    # Gehe Zeichen für Zeichen durch
    for char in input:
        # Offene Klammer gefunden
        if char == "(":
            # Offene Klammeranzahl erhöhen
            open_brackets += 1
        # Geschlossene Klammer gefunden
        elif char == ")":
            # gibt es eine geöffnete Klammer hierzu
            if open_brackets > 0:
                # offene Klammeranzahl reduzieren
                open_brackets -= 1
            else:  # sonst ist Klammerung nicht korrekt
                return False

    # Wenn keine offenen Klammern mehr vorhanden sind, wird true zurückgegeben
    return open_brackets == 0


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print check_brackets("(()(a)(()((c))))")
