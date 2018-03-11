# Klasse zur Realisierung eines Tic-Tac-Toe-Spiels
class TicTacToe:

    # Konstruktor, der das Spielfeld initialisiert
    def __init__(self):
        self.field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.reset()

    # Methode, die alle Felder eines Spielfelds
    # mit 0-Werten initialisiert.
    def reset(self):
        # Lösche Inhalt aller Felder
        self.field = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Setze Startsymbol
        self.mark = 1

    # Methode zum Setzen einer Marke. Die Methode
    # erhält die x,y-Koordinate und setzt die Marke.
    # Wenn die Voraussetzungen dies ermöglichen, wird
    # 'True' zurückgegeben, ansonsten 'False'.
    def setMark(self, x, y):
        # nur gültige Spielfeldgrößen akzeptieren
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False

        # Bestimme Position im Array
        pos = 3 * y + x

        # Feld schon belegt? Dann aus Funktion springen
        if self.field[pos] > 0:
            return False

        # Sonst setze Markierung an Position
        self.field[pos] = self.mark
        # Setze neues Zeichen (O oder X)
        self.mark = (self.mark % 2) + 1
        return True

    # Methode zum Generieren der Ausgabe des Spielfelds.
    # Die Methode erhält keine Parameter übergeben und liefert
    # einen String mit der Repräsentation des Spielfelds zurück.
    def __str__(self):
        temp = ""

        # Elementnummer
        i = 0

        # Gehe Spielfeld durch
        for element in self.field:
            # Python-Dictionary zur Bestimmung des Symbols
            # in Abhängigkeit vom Feldinhalt
            symbol = {0: " ",
                      1: "X",
                      2: "O"}

            # Setze Symbol in Abhängigkeit vom Feldinhalt
            temp += symbol[element]

            # Wenn aktuelle Feldnummer nicht durch 3
            # teilbar ist, Spalte malen
            if (i + 1) % 3 != 0:
                temp += "|"

            # Nach drei Elementen neue Zeile malen
            if (i + 1) % 3 == 0 and i < 6:
                temp += "\n"
                temp += "-+-+-"
                temp += "\n"

            # Erhöhe Elementnummer
            i += 1

        # Gebe Spielfeld mit Zeilenumbruch zurück
        temp += "\n"
        return temp


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.
t = TicTacToe()
println(t)

t.setMark(2, 2)
println(t)

t.setMark(2, 0)
println(t)

t.setMark(1, 1)
println(t)
