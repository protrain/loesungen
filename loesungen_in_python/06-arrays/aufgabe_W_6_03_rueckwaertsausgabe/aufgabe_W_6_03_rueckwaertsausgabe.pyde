# Funktion zur Ausgabe der Buchstaben in umgekehrter Reihenfolge
# An die Funktion wird ein Array mit char-Werten übergeben
def printBackwards(charArray):
    # Ausgabestring
    # in Python notwendig, da print immer einen
    # Zeilenumbruch setzt
    output = ""

    # Gehe jedes Zeichen durch
    for element in charArray:
        # Schreibe Zeichen an erste Stelle des Arrays
        output = element + output

    # Schreibe umgekehrtes Array in die Konsole und erzeuge Zeilenumbruch
    print output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

palindrom = ['r', 'e', 'i', 'b', 'n', 'i', 'e', 'e', 'i', 'n',
             'b', 'i', 'e', 'r']
test = ['H', 'a', 'l', 'l', 'o']

printBackwards(palindrom)
printBackwards(test)

