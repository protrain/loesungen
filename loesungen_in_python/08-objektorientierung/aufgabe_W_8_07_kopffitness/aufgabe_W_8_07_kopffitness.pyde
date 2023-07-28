# Bei der Ausführung in einer reinen Python-Umgebung, muss die
# Library importiert werden
#from random import randrange as random


# Klasse, die das Quiz realisiert
class MultiplicationQuiz:
    # Konstruktor der Klasse
    def __init__(self):
        # Initialisiere Zahlen für Multiplikation
        self.__a = 0
        self.__b = 0

    # Generiert neue Aufgabe
    def get_exercise(self):
        # Generiere zufällige Zahlen für Multiplikation
        self.__a = int(random(1, 20))
        self.__b = int(random(1, 20))

        # Gebe String mit Aufgabe zurück
        return str(self.__a) + " * " + str(self.__b) + " = ?"

    # Gebe Ergebnis zurück
    def get_result(self):
        return self.__a * self.__b


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Testfunktion
quiz = MultiplicationQuiz()
print(quiz.get_exercise())
print("Result: " + str(quiz.get_result()))

print(quiz.get_exercise())
print("Result: " + str(quiz.get_result()))
