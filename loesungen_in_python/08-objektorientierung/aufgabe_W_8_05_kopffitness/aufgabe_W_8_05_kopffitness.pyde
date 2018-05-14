# Klasse, die das Quiz realisiert
class MultiplicationQuiz:
    # Konstruktor der Klasse
    def __init__(self):
        # Initialisiere Zahlen für Multiplikation
        self.__a = 0
        self.__b = 0

    # Generiert neue Aufgabe
    def getExercise(self):
        # Generiere zufällige Zahlen für Multiplikation
        self.__a = int(random(1, 20))
        self.__b = int(random(1, 20))

        # Gebe String mit Aufgabe zurück
        return str(self.__a) + " * " + str(self.__b) + " = ?"

    # Gebe Ergebnis zurück
    def getResult(self):
        return self.__a * self.__b


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Testfunktion
quiz = MultiplicationQuiz()
print quiz.getExercise()
print "Result: " + str(quiz.getResult())

print quiz.getExercise()
print "Result: " + str(quiz.getResult())
