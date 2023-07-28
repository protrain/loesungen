# Bei der Ausführung in einer reinen Python-Umgebung, kann die
# folgende Funktion die Processing-Funktion loadStrings ersetzen
# def load_strings(filename):
#     with open(filename, mode="r", encoding="utf-8", ) as f:
#         return f.read().splitlines()

# Dateipfade zu den SentiWS-Datensatz-Dateien. Diese ggf.
# anpassen. Der Datensatz muss noch heruntergeladen werden,
# bevor das Programm ausgeführt werden kann.
# Siehe: https://github.com/protrain/loesungen
base_path = "../../../externe_daten/sentiws/data/"
path_positive = base_path+"SentiWS_v2.0_Positive.txt"
path_negative = base_path+"SentiWS_v2.0_Negative.txt"

# Wir speichern die HashMap als globale Variable, damit wir sie
# nur einmal zur Laufzeit berechnen müssen. Andernfalls geht
# wertvolle Rechenzeit verloren.
emotions = None
    
# Funktion, welche den Emotionsdatensatz importiert und für die
# weitere Nutzung vorverarbeitet
# Diese Funktionsvariation nutzt dabei das übergebene HashMap-
# Objekt weiter.
def import_emotions(filepath, dictionary):
    # Lese die Datensatzdatei als String-Array ein
    lines = loadStrings(filepath)
    
    # Gehe jede Zeile einzeln durch
    for line in lines:
        # Trenne die Zeile mittels Tabulatorzeichen in die einzelnen
        # Spalten auf
        columns = line.split("\t")
    
        # Wir lesen nur Zeilen mit mindestens zwei Spalten aus
        if len(columns) < 2:
            continue
        
        # Lese Wort ein und entferne das Kürzel am Ende
        word = columns[0]
        stop_position = word.find("|")
        word = word[0:stop_position]
    
        # Lese Emotionsbewertung als Float ein
        emotion_score = float(columns[1])
    
        # Füge Hauptwort hinzu
        dictionary[word] = emotion_score
    
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
            dictionary[word_variation] = emotion_score
        
    return dictionary

# Funktion, welche die Datenbanken importiert
def import_emotions_dataset():
    global emotions
    
    # Wir generieren die HashMap nur, wenn sie noch nicht vorher
    # erstellt wurde.
    if emotions == None:
        # Lade Tabellen im TSV-Format
        emotions = {}
        emotions = import_emotions(path_positive, emotions)
        import_emotions(path_negative, emotions)

# Funktion, welche die Satzzeichen aus einem Wort entfernt
def remove_punctuation(word):
    if len(word) <= 1:
        return word
  
    # Liste alle Satzzeichen auf, die wir entfernen wollen
    # Diese dürfen aber nur an vorderer oder hinterer Stelle
    # sein.
    punctuations = ['.', ',', '-', '!', ':', '']
    
    # Entferne zunächst Leerzeichen an vorderer und hinterer
    # Stelle
    word = word.strip()
    
    # Entnehme vorderstes und hinterstes Zeichen
    word_first_char = word[0]
    word_last_char = word[-1]
    
    # Wir prüfen zunächst das Ende des Wortes
    if word_last_char in punctuations:
        # Zeichen gefunden, wird entfernt
        word = word[0:-1]

    # Jetzt prüfen wir den Anfang des Wortes
    if word_first_char in punctuations:
        # Zeichen gefunden, wird entfernt
        word = word[1:]
    
    return word

# Funktion, welche die Emotionsbewertung zurückliefert
def get_emotion_score(word):
    # Da die Datenbank noch nicht initalisiert wurde, machen
    # wir das einmal
    if emotions == None:
        import_emotions()
  
    # Entferne Satzzeichen am Anfang und Ende des Wortes.
    word = remove_punctuation(word)
    
    # Schaue nach, ob das Wort in Datensatz existiert
    emotion_score = 0.0
    try:
        emotion_score = emotions[word]
    except KeyError:
        # Prüfe, ob das Wort nicht noch in Kleinschreibung
        # vorhanden ist
        try:
            emotion_score = emotions[word.lower()]
        except:
            # Wort wurde nicht gefunden
            emotion_score = 0.0

    return emotion_score

# Funktion, welche aus einem Text die Grundstimmung
def determine_sentiment(text):
    # Trenne den Text nach Leerzeichen auf
    words = text.split(" ")
    
    # Emotionsbewertung aller Wörter
    emotion_score = 0.0
    
    # Gehe alle Wörter durch
    for word in words:
        # Füge Emotionsbewertung hinzu
        emotion_score = emotion_score + get_emotion_score(word)
    
    if emotion_score == 0.0:
        return "Keine Tendenz: {}".format(emotion_score)
    elif emotion_score < 0.0:
        return "Negative Tendenz: {}".format(emotion_score)
    else:
        return "Positive Tendenz: {}".format(emotion_score)

# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    import_emotions_dataset()
    
    satz1 = "Die Schreiberlinge brillieren mit "
    satz1 += "hervorragenden Einfällen! War sehr "
    satz1 += "hilfreich für mich!"
    
    satz2 = "Unverantwortlich, dass diese Autoren meinen , "
    satz2 += "sie könnten meinen Hass mit Zahlen messen."
    
    print(satz1)
    print(determine_sentiment(satz1))
    print("")
    print(satz2)
    print(determine_sentiment(satz2))


# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
