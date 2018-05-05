def print_backwards(chars):
    """ Funktion zur Ausgabe der Buchstaben in umgekehrter Reihenfolge
    An die Funktion wird ein Array mit char-Werten übergeben """
    # Schreibe umgekehrtes Array in die Konsole und erzeuge Zeilenumbruch
    print ''.join(chars[::-1])


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

palindrom = ['r', 'e', 'i', 'b', 'n', 'i', 'e', 'e', 'i', 'n',
             'b', 'i', 'e', 'r']
test = ['H', 'a', 'l', 'l', 'o']

print_backwards(palindrom)
print_backwards(test)

