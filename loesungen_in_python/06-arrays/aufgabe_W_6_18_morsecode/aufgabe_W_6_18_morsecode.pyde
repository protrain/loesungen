# Funktion zur Ausgabe des Morsecodes für einen Eingabetext
# Übergeben wird der Eingabetext
def print_morse_code(input_data):
    # Setze Eingabe auf Lowercase
    input_data = input_data.lower()

    # Entferne alle Leerzeichen aus dem String
    input_data = input_data.replace(" ", "")

    # Entferne Punkt und Komma aus dem String
    input_data = input_data.replace(",", "")
    input_data = input_data.replace(".", "")

    output = ""
    # Lexikon für Morsezeichen (von Zeichen A bis 0)
    morsecode = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----"
    }

    # Gib den zu "morsenden" Text zunächst als Text aus
    print(input_data)

    # Lese Zeichen für Zeichen aus
    for index in input_data:
        # Hole Morsezeichen aus Lexikon und schreibe in Ergebnis
        output += morsecode[index] + " "

    # gebe Zeichen aus
    print(output)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
print_morse_code("Wozu Worte drucken, es gibt doch Schreiber")
