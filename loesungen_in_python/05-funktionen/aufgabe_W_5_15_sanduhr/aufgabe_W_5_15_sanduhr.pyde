# Funktion zur Ausgabe einer Sanduhr auf der Konsole
# Die maximale Breite wird als Integer-Wert an die
# Funktion übergeben. Die Funktion hat keinen Rückgabewert
def print_sandglass(s_width):
    if s_width > 2:           # nur wenn die Bereite > 2 ist
        s_height = s_width    # Höhe wird mit Breite initialisiert
        if s_width % 2 == 0:  # ist die Breite eine gerade Zahl,
            s_height -= 1     # muss die Höhe um eins minimiert werden

        # wiederhole für alle Zeilen des oberen Dreiecks
        for i in range(0, int(s_height / 2) + 1):
            output = ""
            # Rücke mit zunehmender Zeilenzahl i ein
            output = " " * i    # Schreibe Leerzeichen in Variable

            # Die Variable width gibt die Anzahl an #-Zeichen an, die
            # mit jeder Zeile i um 2 verringert wird
            # Schreibe Lattenzaun-Zeichen in Variable
            output = output + "#" * (s_width - (2 * i))
            # Gebe Zeile mit der Variable aus und wechsele in nächste
            # Zeile
            print(output)

        # wiederhole für alle Zeilen des unteren Dreiecks
        for i in range(int(s_height / 2) - 1, -1, -1):
            # Rücke mit zunehmender Zeilenzahl i ein            
            output = " " * i  # Schreibe Leerzeichen in Variable
            # Die Variable width gibt die Anzahl an #-Zeichen an, die
            # mit jeder Zeile i um 2 verringert wird
            # Schreibe Lattenzaun-Zeichen in Variable            
            output += "#" * (s_width - (2 * i))
            # Gebe Zeile mit der Variable aus und wechsele in nächste
            # Zeile
            print(output)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

print_sandglass(8)
