# Funktion zur Überprüfung eines Strings auf eine gültige
# Klammerung. Der String wird an die Funktion übergeben.
# Diese liefert am Ende einen Wahrheitswert, der angibt,
# ob eine korrekte Klammerung vorliegt.
def check_brackets(input_data):
    # Anzahl der noch geöffneten Klammern
    open_brackets = 0

    # Ist die letzte Klammer eine geschlossene?
    last_bracket_closed = True

    # Gehe Zeichen für Zeichen durch
    for c in input_data:
        # Offene Klammer gefunden
        if c == "(":
            # Offene Klammeranzahl erhöhen
            open_brackets += 1

            # Letzte Klammer ist somit nicht geschlossen
            last_bracket_closed = False

        # Geschlossene Klammer gefunden
        if c == ")":
            # gibt es eine geöffnete Klammer hierzu
            if open_brackets > 0:
                # offene Klammeranzahl reduzieren
                open_brackets -= 1
            else:  # sonst ist Klammerung nicht korrekt
                return False

            # Letzte Klammer ist damit geschlossen
            last_bracket_closed = True

    # Wenn keine offenen Klammern mehr vorhanden sind und die
    # letzte Klammer geschlossen ist, wird true zurückgegeben
    return open_brackets == 0 and last_bracket_closed


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print(check_brackets("(()(a)(()((c))))"))
