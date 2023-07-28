# Funktion zum Zerteilen eines Eingabestrings, der an
# die Funktion übergeben wird. Als Ergebnis wird ein
# Array mit den Teilstrings zurückgegeben.
def split(input):
    str_len = len(input)
    output = []

    # Aktueller ausgelesener String (bis Semikolon)
    word = ""

    for i in range(0, str_len):
        # Semikolon entdeckt oder Ende des Strings
        if input[i] == ";":
            # Füge Wort hinzu
            output = output + [word]

            # Lösche aktuelles Wort
            word = ""
        # Letztes Element im String -> Wort ergänzen + hinzufügen
        elif i == str_len - 1:
            word = word + input[i]
            output = output + [word]

        # Sonst String um aktuellen Character ergänzen
        else:
            word = word + input[i]

    return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print(split("ab;cde;fghi;jklm"))
