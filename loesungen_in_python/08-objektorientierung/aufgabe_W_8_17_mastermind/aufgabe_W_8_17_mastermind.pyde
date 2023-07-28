# Öffentliche Klasse, die das Spiel Mastermind realisiert
class Mastermind:
    # Konstanten für Farbcodes
    RED = 0
    GREEN = 1
    BLUE = 2
    WHITE = 3
    ORANGE = 4
    GREY = 5

    def __init__(self, c_1, c_2, c_3, c_4):
        # Initialisiere Array
        self.__code = []
        for i in range(0, 4):
            self.__code.append(-1)

        # Setze Farben
        self.__code[0] = c_1
        self.__code[1] = c_2
        self.__code[2] = c_3
        self.__code[3] = c_4

        # Initialisiere Zähler der Spielzüge
        self.__num_move = 0

    # Private Methode, die berechnet, wie viele richtige Farben
    # an den richtigen Positionen liegen. Die Farben werden
    # in der entsprechenden Reihenfolge ausgewertet. Die Anzahl
    # der korrekten Farben an den Positionen wird zurückgeliefert.
    def __correct_colors_and_positions(self, colors):
        # Anzahl richtiger Farben und Positionen
        count = 0
        for i in range(0, len(self.__code)):
            if self.__code[i] == colors[i]:
                count += 1
        return count

    # Private Methode, die berechnet, wie viele Farben korrekt
    # angegeben wurden. Dazu werden die angegebenen Farben
    # auf ihr Vorkommen geprüft und das Ergebnis zurückgeliefert.
    def __correct_colors(self, colors):
        # Anzahl richtiger Farben, die an falscher
        # Position stehen
        count = 0

        # Bereits geprüfte Positionen des Codes
        checked = [False, False, False, False]

        # Hake zunächst alle Farben ab, die die richtige Farbe und
        # Position haben
        for i in range(0, len(self.__code)):
            # Wenn an identischer Position
            if self.__code[i] == colors[i]:
                # Position als geprüft abhaken
                checked[i] = True

        # Zähle jetzt alle Farben
        # Gehe jede Codenummer durch
        for i in range(0, len(self.__code)):
            for j in range(0, len(colors)):
                # Wenn Position mit gleicher Farbe gefunden, die noch
                # nicht abgehakt ist, dann zählen (und abhaken)
                if self.__code[i] == colors[j] and checked[j] is False:
                    checked[j] = True
                    count += 1
                    # Aus Schleife springen
                    break

        return count

    # Öffentliche Methode, die den Spielzug entgegennimmt und
    # auswertet. Als Elemente eines zweidimensionalen Arrays
    # werden die korrekten Farbpositionen und die Anzahl der
    # korrekten Farben zurückgeliefert.
    def guess(self, c_1, c_2, c_3, c_4):
        output = [-1, -1]
        # Baue Spielzug zu Array um
        colors = [c_1, c_2, c_3, c_4]

        # Werte private Methoden für Spielzug aus
        output[0] = self.__correct_colors_and_positions(colors)
        output[1] = self.__correct_colors(colors)

        # Erhöhe Spielzugzähler
        self.__num_move += 1
        return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.
mm = Mastermind(Mastermind.RED, Mastermind.BLUE, Mastermind.GREY,
                Mastermind.BLUE)

guess = mm.guess(Mastermind.GREEN, Mastermind.GREY, Mastermind.BLUE,
                 Mastermind.BLUE)

print("correctColorsAndPositions: \t" + str(guess[0]))
print("correctColors: \t\t" + str(guess[1]))
