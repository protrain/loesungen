# Funktion zur Überprüfung von Übereinstimmungen
# Die Funktion erhält die Werte für Person a und b in einem
# Array mit Wahrheitswerten und gibt die prozentuale
# Überschneidung zurück
def interests_match(a, b):
    # Abbruch, wenn beide Profile ungleich groß sind
    if len(a) != len(b):
        return 0

    num_matches = 0

    # Gehe Liste durch
    for i in range(0, len(a)): 
        # Erhöhe Zähler, wenn es Übereinstimmung gibt
        if a[i] == b[i]:
            num_matches += 1

    # Prozentzahl: Übereinstimmungen / Gesamtzahl * 100
    return int((num_matches / float(len(a))) * 100)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

personA = [True, True, False, False, False, True]
personB = [True, False, False, False, False, True]
personC = [False, False, True, True, True, False]
personD = [False, False, True, True, True]

print(interests_match(personA, personA))
print(interests_match(personA, personB))
print(interests_match(personA, personC))
print(interests_match(personA, personD))
