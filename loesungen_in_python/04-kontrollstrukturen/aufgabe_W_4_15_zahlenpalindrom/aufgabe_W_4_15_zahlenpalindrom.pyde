number = 12321
# number = 12345

# Zunächst bestimmen wir die Anzahl der Dezimalstellen der
# Palindrom-Zahl
i = number

# Anzahl der Dezimalstellen
size = 0
while int(i) > 0:
    # Teile durch 10 (nehme letzte Zahl weg)
    i = i / 10

    # Erhöhe Dezimalstellenzahl
    size += 1

# ist Zahl ein Palindrom?
is_palindrom = False

# Gehe size/2-Schritte durch (wenn wir vorne mit hinten vergleichen, sind
# wir ab der Hälfte durch)

for i in range(size, int(size / 2), -1):
    # Bestimme vordere Zahl
    # Schneide i Stellen vorne weg
    first_digit = number % pow(10, i)

    # Gehe Zahl so lange "hoch" (durch 10 teilen), bis nur noch eine
    # Ziffer da ist
    while int(first_digit / 10) > 0:
        first_digit = int(first_digit / 10)

    # Bestimme hintere Zahl
    # Schneide i Stellen vorne weg, hier allerdings in umgekehrter
    # Reihenfolge
    last_digit = number % pow(10, size - i + 1)

    # Gehe Zahl so lange "hoch" (durch 10 teilen), bis nur noch eine
    # Ziffer da ist
    while int(last_digit / 10) != 0:
        last_digit = int(last_digit / 10)

    # Prüfe, ob beide Ziffern übereinstimmen
    if first_digit == last_digit:
        is_palindrom = True
    else:
        is_palindrom = False
        # Aus Schleife springen, damit Variable
        # nicht verändert werden kann
        break

# Erzeuge Ausgabe je nach Fall
if is_palindrom:
    print("Die Zahl " + str(number) + " ist ein Palindrom")
else:
    print("Die Zahl " + str(number) + " ist kein Palindrom")
