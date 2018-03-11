# Funktion zur Ausgabe einer Sanduhr auf der Konsole
# Die maximale Breite wird als Integer-Wert an die
# Funktion übergeben. Die Funktion hat keinen Rückgabewert
def printSandglass(sWidth):
    if(sWidth > 2):         # nur wenn die Bereite > 2 ist
        sHeight = sWidth    # Höhe wird mit Breite initialisiert
        if sWidth % 2 == 0:   # ist die Breite eine gerade Zahl,
            sHeight -= 1    # muss die Höhe um eins minimiert werden

        # wiederhole für alle Zeilen des oberen Dreiecks
        for i in range(0, sHeight / 2 + 1):
            output = ""
            # Rücke mit zunehmender Zeilenzahl i ein
            for j in range(0, i):
                output += " "  # Schreibe Leerzeichen in Variable

            # Die Variable width gibt die Anzahl an #-Zeichen an, die
            # mit jeder Zeile i um 2 verringert wird
            for j in range(0, sWidth - (2 * i)):
                output += "#"  # Schreibe Lattenzaun-Zeichen in Variable
            # Gebe Zeile mit der Variable aus und wechsele in nächste
            # Zeile
            print output

        # wiederhole für alle Zeilen des unteren Dreiecks
        for i in range(sHeight / 2 - 1, -1, -1):
            # Rücke mit zunehmender Zeilenzahl i ein
            output = ""
            for j in range(0, i):
                output += " "  # Schreibe Leerzeichen in Variable

            # Die Variable width gibt die Anzahl an #-Zeichen an, die
            # mit jeder Zeile i um 2 verringert wird
            for j in range(0, sWidth - (2 * i)):
                output += "#"  # Schreibe Lattenzaun-Zeichen in Variable
            # Gebe Zeile mit der Variable aus und wechsele in nächste
            # Zeile
            print output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

printSandglass(8)

