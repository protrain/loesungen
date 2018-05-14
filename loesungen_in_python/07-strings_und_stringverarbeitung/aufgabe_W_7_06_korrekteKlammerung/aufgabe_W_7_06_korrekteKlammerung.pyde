# Funktion zur Überprüfung eines Strings auf eine gültige
# Klammerung. Der String wird an die Funktion übergeben.
# Diese liefert am Ende einen Wahrheitswert, der angibt,
# ob eine korrekte Klammerung vorliegt.
def checkBrackets(input):
    # Anzahl der noch geöffneten Klammern
    openBrackets = 0

    # Ist die letzte Klammer eine geschlossene?
    lastBracketClosed = True

    # Gehe Zeichen für Zeichen durch
    for c in input:
        # Offene Klammer gefunden
        if c == "(":
            # Offene Klammeranzahl erhöhen
            openBrackets += 1

            # Letzte Klammer ist somit nicht geschlossen
            lastBracketClosed = False

        # Geschlossene Klammer gefunden
        if c == ")":
            # gibt es eine geöffnete Klammer hierzu
            if openBrackets > 0:
                # offene Klammeranzahl reduzieren
                openBrackets -= 1
            else:  # sonst ist Klammerung nicht korrekt
                return False

            # Letzte Klammer ist damit geschlossen
            lastBracketClosed = True

    # Wenn keine offenen Klammern mehr vorhanden sind und die
    # letzte Klammer geschlossen ist, wird true zurückgegeben
    return openBrackets == 0 and lastBracketClosed


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print checkBrackets("(()(a)(()((c))))")

