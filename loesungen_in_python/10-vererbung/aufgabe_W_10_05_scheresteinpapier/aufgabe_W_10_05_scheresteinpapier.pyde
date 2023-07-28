# Konstanten zum Ergebnis
UNENTSCHIEDEN = 0
SELF_GEWINNT = 1
SELF_VERLIERT = -1


# Abstrakte Klasse zur Repräsentation einer Hand.
# Von dieser Klasse kann keine Instanz (= Objekt) erzeugt werden.
class Hand(object):
    def __init__(self):
        # Eine Hand alleine kann nicht gewinne, da wir das Spiel nur
        # mit abgeleiteten Instanzen spielen können.
        self.wins_against = None

    # Funktion, welche den Namen der Klasse zurückgibt
    def get_name(self):
        return type(self).__name__

    # Funktion, die angibt, ob die von Hand abgeleitete
    # Klasse gegen die andere Klasse gewinnt.
    # 0: Unentschieden
    # 1: this gewinnt
    # -1: opponent_hand gewinnt
    def get_result(self, opponent_hand):
        # Hole Datentyp-Namen vom aktuellen Objekt
        self_hand_type = self.get_name()

        # Hole Datentyp-Namen vom gegnerischen Objekt
        opponent_hand_type = opponent_hand.get_name()

        # Gleicher Datentyp bring unentschieden
        if self_hand_type == opponent_hand_type:
            return UNENTSCHIEDEN

        if opponent_hand_type == self.wins_against:
            # Wir haben gewonnen
            return SELF_GEWINNT
        else:
            # Wir haben verloren
            return SELF_VERLIERT


# Öffentliche Klasse für Schere leitet
# von der Klasse Hand ab.
class Schere(Hand):
    def __init__(self):
        Hand.__init__(self)
        self.wins_against = "Papier"


# Öffentliche Klasse für Stein leitet
# von der Klasse Hand ab.
class Stein(Hand):
    def __init__(self):
        Hand.__init__(self)
        self.wins_against = "Schere"


# Öffentliche Klasse für Papier leitet
# von der Klasse Hand ab.
class Papier(Hand):
    def __init__(self):
        Hand.__init__(self)
        self.wins_against = "Stein"


# Funktion, welche das Schere-Stein-Papier-Spiel realisiert.
# Die Funktion nimmt abgeleitete Objekte der Hand-Klasse
# entgegen. 
def play_schere_stein_papier(person_a, person_b):
    print("{} vs. {}".format(person_a.get_name(), person_b.get_name()))

    # Berechne Ergebnis
    result = person_a.get_result(person_b)
    if result == UNENTSCHIEDEN:
        __ergebnis = "Unentschieden"
    elif result == SELF_GEWINNT:
        __ergebnis = person_a.get_name() + " gewinnt"
    else:
        __ergebnis = person_b.get_name() + " gewinnt"
    print("Ergebnis: {}".format(__ergebnis))
    print("")


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    play_schere_stein_papier(Schere(), Stein())
    play_schere_stein_papier(Schere(), Papier())
    play_schere_stein_papier(Papier(), Stein())
    play_schere_stein_papier(Papier(), Papier())


# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
