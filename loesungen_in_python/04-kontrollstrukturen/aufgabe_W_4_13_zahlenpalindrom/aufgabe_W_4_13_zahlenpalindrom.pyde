number = 12321
#number = 12345

# Zunächst bestimmen wir die Anzahl der Dezimalstellen der
# Palindrom-Zahl
i = number

# Anzahl der Dezimalstellen
size = 0
while i > 0:
    # Teile durch 10 (nehme letzte Zahl weg)
    i = i / 10

    # Erhöhe Dezimalstellenzahl
    size += 1

# ist Zahl ein Palindrom?
isPalindrom = False

# Gehe size/2-Schritte durch (wenn wir vorne mit hinten vergleichen, sind
# wir ab der Hälfte durch)
for i in range(size, size / 2, -1):
    # Bestimme vordere Zahl
    # Schneide i Stellen vorne weg
    firstDigit = number % int(pow(10, i))

    # Gehe Zahl so lange "hoch" (durch 10 teilen), bis nur noch eine
    # Ziffer da ist
    while firstDigit / 10 != 0:
        firstDigit /= 10

    # Bestimme hintere Zahl
    # Schneide i Stellen vorne weg, hier allerdings in umgekehrter
    # Reihenfolge
    lastDigit = number % int(pow(10, size - i + 1))

    # Gehe Zahl so lange "hoch" (durch 10 teilen), bis nur noch eine
    # Ziffer da ist
    while lastDigit / 10 != 0:
        lastDigit /= 10

    # Prüfe, ob beide Ziffern übereinstimmen
    if firstDigit == lastDigit:
        isPalindrom = True
    else:
        isPalindrom = False
        # Aus Schleife springen, damit Variable
        # nicht verändert werden kann
        break


# Erzeuge Ausgabe je nach Fall
if isPalindrom:
    print "Die Zahl " + str(number) + " ist ein Palindrom"
else:
    print "Die Zahl " + str(number) + " ist kein Palindrom"

