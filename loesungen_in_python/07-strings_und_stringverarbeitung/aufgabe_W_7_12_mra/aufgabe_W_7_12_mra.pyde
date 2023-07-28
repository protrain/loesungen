# Funktion zur Bestimmung eines Zeichens auf einen Vokal
# Das Zeichen wird an die Funktion übergeben. Die Funktion
# gibt einen Wahrheitswert zurück.
def is_vowel(c):
    # Gebe True zurück, wenn Buchstabe ein Vokal ist
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        return True
    else:
        return False


# Funktion zur Umsetzung des MRA-Algorithmus. Die Funktion
# erhält ein Wort als String und liefert den Match Rating
# Approach zurück
def mra(word):
    # Wandle in Großbuchstaben um
    word = word.upper()

    temp = ""

    # Gehe alle Zeichen durch
    for i in range(0, len(word)):
        c = word[i]

        # Der erste Buchstabe darf ein Vokal sein,
        # also springe in nächste Schleifeniteration
        if is_vowel(c) and i > 0:
            continue

        # Wenn es nicht der erste Buchstabe ist, prüfe,
        # ob es eine Buchstabenwiederholung ist.
        if i > 0 and c == word[i - 1]:
            # Springe in nächste Schleifeniteration
            continue

        # Übernehme Buchstaben, wenn die
        # beiden Fälle oben nicht zutreffen
        temp += word[i]

    # Kürzen bei zu langem Wort
    if len(temp) > 6:
        # die ersten drei Buchstaben
        start = temp[0:3]
        # die letzten drei Buchstaben
        end = temp[len(temp) - 3:]
        temp = start + end

    return temp


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
def setup():
    print(mra("Algorithmusschreiber"))


# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
