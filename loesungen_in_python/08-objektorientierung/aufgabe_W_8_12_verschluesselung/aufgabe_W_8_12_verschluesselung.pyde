# Klasse, die die Schiebeverschlüsselung realisiert
class ShiftCipher:

    # Konstruktor, der den Schlüssel zur Voraussetzung
    # der Instanziierung eines Objekts macht. Der an die
    # Funktion übergebene Schlüssel wird für die Lebens-
    # dauer intern gespeichert
    def __init__(self, key):
        self.__key = key

    # Öffentliche Methode zum Verschlüsseln eines übergebenen
    # Texts. Das Ergebnis der Verschlüsselung wird von der
    # Methode zurückgeliefert.
    def encipher(self, input):
        # Hier wird verschlüsselter String gespeichert
        output = ""

        # Gehe jeden Buchstaben durch
        for c in input:
            # Bestimme Position
            pos = self.__get_position_in_alphabet(c)

            # Addiere mit Key
            new_pos = pos + self.__key

            # Wenn neue Position größer als Alphabet ist,
            # nehme nur den Rest (= innerhalb von 1 bis 26)
            if new_pos > 26:
                new_pos = new_pos % 26

            # Hole neuen Buchstaben
            new_c = self.__get_letter_in_position(new_pos)

            # Füge dem String hinzu
            output += new_c

        # Gebe verschlüsselten String zurück
        return output


    # Öffentliche Methode zum Entschlüsseln eines Texts, der
    # an die Methode übergeben wird. Mithilfe
    # des intern gespeicherten Schlüssels liefert
    # die Methode das Ergebnis (den Klartext) wieder
    # zurück.
    def decipher(self, input):
        output = ""

        # Gehe jeden Buchstaben durch
        for c in input:
            # Bestimme Position
            pos = self.__get_position_in_alphabet(c)

            # Subtrahiere mit Key
            new_pos = pos - self.__key

            # Wenn neue Position kleiner als Alphabet ist,
            # addiere mit 26 (= innerhalb von 1 bis 26)
            if new_pos < 0:
                new_pos = (new_pos + 26) % 26

            # Sonderfall, wenn Position = Key ist
            elif new_pos == 0:
                new_pos = 26

            # Hole neuen Buchstaben
            new_c = self.__get_letter_in_position(new_pos)

            # Füge dem String hinzu
            output += new_c + " "

        # Gebe entschlüsselten String zurück
        return output

    # Private Methode, die zu einem Buchstaben die Position
    # im Alphabet berechnet und zurückgibt
    def __get_position_in_alphabet(self, letter):
        # Wandle Buchstabe in Kleinbuchstaben um
        letter = letter.lower()

        # Python-Dictionary zur Zuordnung von Buchstaben
        # zu ihrer Alphabetsposition
        letter_position = {"a": 1,
                           "b": 2,
                           "c": 3,
                           "d": 4,
                           "e": 5,
                           "f": 6,
                           "g": 7,
                           "h": 8,
                           "i": 9,
                           "j": 10,
                           "k": 11,
                           "l": 12,
                           "m": 13,
                           "n": 14,
                           "o": 15,
                           "p": 16,
                           "q": 17,
                           "r": 18,
                           "s": 19,
                           "t": 20,
                           "u": 21,
                           "v": 22,
                           "w": 23,
                           "x": 24,
                           "y": 25,
                           "z": 26,
                          }
        # Hole Position im lateinischen Alphabet
        pos_number = letter_position[letter]
        return pos_number

    # Private Methode, um einen Buchstabe von der angegebenen
    # Position des Alphabets zurückzuliefern
    def __get_letter_in_position(self, position):
        # Python-Dictionary zur Zuordnung von
        # Alphabetsposition zu Buchstaben
        alphabet = {1: "a",
                    2: "b",
                    3: "c",
                    4: "d",
                    5: "e",
                    6: "f",
                    7: "g",
                    8: "h",
                    9: "i",
                    10: "j",
                    11: "k",
                    12: "l",
                    13: "m",
                    14: "n",
                    15: "o",
                    16: "p",
                    17: "q",
                    18: "r",
                    19: "s",
                    20: "t",
                    21: "u",
                    22: "v",
                    23: "w",
                    24: "x",
                    25: "y",
                    26: "z",
                   }
        # Gebe Buchstaben zurück
        return alphabet[position]


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.
sc = ShiftCipher(3)
encrypted = sc.encipher("abcdefghijklmnopqrstuvwxyz")
print(encrypted)
print(sc.decipher(encrypted))

sc = ShiftCipher(3)
encrypted = sc.encipher("DieserTextIstVerschluesselt")
print(encrypted)
print(sc.decipher(encrypted))
