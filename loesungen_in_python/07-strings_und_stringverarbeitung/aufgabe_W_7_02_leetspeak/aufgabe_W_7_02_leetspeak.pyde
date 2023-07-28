# Funktion, welches einen Buchstaben entgegennimmt
# und die Leetspeak-Variante davon zurückliefert.
# Sofern keine Leetspeak-Variante existiert,
# wird der gleiche Buchstabe zurückgeliefert.
def get_leet_char(input_char):
    # Wandle Buchstaben in Großbuchstaben um
    input_char_upper = input_char.upper()

    # Generiere Zuordnung von Buchstaben zu Leet
    leet_dict = {
                "A": "4",
                "E": "3",
                "G": "6",
                "H": "#",
                "I": "1",
                "S": "$",
                "O": "0",
                "T": "7",
                "Z": "2",
                }

    if input_char_upper in leet_dict:
        # Leet-Eintrag gefunden
        return leet_dict[input_char_upper]

    # Kein Eintrag gefunden
    return input_char


# Funktion, welche einen Text als String entgegennimmt
# und dann die Leetspeak-Variante zurückliefert
def get_leetspeak(input_string):
    output_string = ""

    # Gehe jeden Buchstaben der Eingabestrings durch
    for input_char in input_string:
        # Wandle Buchstaben in Leetspeak um
        output_string += get_leet_char(input_char)

    return output_string


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    print(get_leetspeak("It's my job to keep punkrock elite"))
    print(get_leetspeak("An apple a day keeps hunger away"))
    print(get_leetspeak("abcdefghijklmnopqrstuvwxyz"))


# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
