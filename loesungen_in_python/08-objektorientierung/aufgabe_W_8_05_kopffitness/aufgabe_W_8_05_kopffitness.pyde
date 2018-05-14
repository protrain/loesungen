from random import randint
# Klasse, die das Quiz realisiert
class MultiplicationQuiz:
    def __init__(self):
        """ Initialisiere Zahlen für Multiplikation """
        self.a = 0
        self.b = 0

    def get_exercise(self):
        """ Generiert neue Aufgabe """
        # Generiere zufällige Zahlen für Multiplikation
        self.a = randint(1, 20)
        self.b = randint(1, 20)

        # Gebe String mit Aufgabe zurück
        return "%s * %s = ?" % (self.a, self.b)
    
    # Gebe Ergebnis zurück
    def get_result(self):
        return self.a * self.b


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Testfunktion
quiz = MultiplicationQuiz()
print quiz.get_exercise()
print "Result: %s" % quiz.get_result()

print quiz.get_exercise()
print "Result: %s" % quiz.get_result()
