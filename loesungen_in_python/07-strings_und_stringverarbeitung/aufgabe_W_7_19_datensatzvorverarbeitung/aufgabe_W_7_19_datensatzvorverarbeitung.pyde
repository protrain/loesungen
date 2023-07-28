# Bei der Ausführung in einer reinen Python-Umgebung, kann die
# folgende Funktion die Processing-Funktion loadStrings ersetzen
# def load_strings(filename):
#     with open(filename, mode="r", encoding="utf-8", ) as f:
#         return f.read().splitlines()


# Funktion, welche den Emotionsdatensatz importiert und für die
# weitere Nutzung vorverarbeitet
def import_emotions(filepath):
    output = {}

    # Lese die Datensatzdatei als String-Array ein
    lines = loadStrings(filepath)

    # Gehe jede Zeile einzeln durch
    for line in lines:
        # Trenne die Zeile mittels Tabulatorzeichen in die 
        # einzelnen Spalten auf
        columns = line.split("\t")

        # Wir lesen nur Zeilen mit mindestens zwei Spalten aus
        if len(columns) < 2:
            continue

        # Lese Wort ein und entferne das Kürzel am Ende
        word = columns[0]
        stop_position = word.index("|")
        word = word[0:stop_position]

        # Lese Emotionsbewertung als Float ein
        emotion_score = float(columns[1])

        # Füge Hauptwort hinzu
        output[word] = emotion_score

        if len(columns) == 2:
            # Wort hat keine Variationen, daher gehen wir in
            # die nächste Iteration
            continue

        # Lese Wortvariationen als einzelne Arrayelemente ein.
        # Die Einträge sind hier mit Komma getrennt, daher
        # brauchen wir die split-Funktion.
        word_variations = columns[2].split(",")

        # Füge Wortvariationen hinzu
        for word_variation in word_variations:
            output[word_variation] = emotion_score

    return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    # Lade Testtabelle im TSV-Format
    emotions = import_emotions("testdata.txt")

    print(emotions["erster"])
    print(emotions["zweit"])
    print(emotions["Dritter"])


# Ohne Processing
#setup()
