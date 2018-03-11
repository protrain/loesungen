# Funktion zur Überprüfung von Übereinstimmungen
# Die Funktion erhält die Werte für Person a und b in einem
# Array mit Wahrheitswerten und gibt die prozentuale
# Überschneidung zurück
def interestsMatch(a, b):
    # Abbruch, wenn beide Profile ungleich groß sind
    if len(a) != len(b):
        return 0

    numMatches = 0

    # Gehe Liste durch
    for i in range(0, len(a)):
        # Erhöhe Zähler, wenn es Übereinstimmung gibt
        if a[i] == b[i]:
            numMatches += 1

    # Prozentzahl: Übereinstimmungen / Gesamtzahl * 100
    return int((numMatches / float(len(a))) * 100)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

personA = [True, True, False, False, False, True]
personB = [True, False, False, False, False, True]
personC = [False, False, True, True, True, False]
personD = [False, False, True, True, True]

print interestsMatch(personA, personA)
print interestsMatch(personA, personB)
print interestsMatch(personA, personC)
print interestsMatch(personA, personD)

