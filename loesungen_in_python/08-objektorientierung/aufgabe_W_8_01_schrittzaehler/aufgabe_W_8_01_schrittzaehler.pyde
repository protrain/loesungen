# Klasse, die den Schrittzähler realisiert
class step_counter:
    # Initialisierung
    # Alle Instanzvariablen werden im Konstruktor initialisiert
    # Die Klasse kann nur mit der Angabe eines Schrittzählers
    # initialisiert werden, wenn es sich bei diesem Konstruktor NICHT um
    # einen Standardkonstruktor handelt
    def __init__(self, date):
        self.__date = date
        self.__steps = 0

    # Öffentliche Methode, um den Schrittzähler um 1 zu erhöhen
    def increment_steps(self):
        self.__steps += 1

    # Öffentliche Methode zur Erzeugung einer Statusnachricht, die
    # zurückgegeben wird
    def __str__(self):
        return "Am " + self.__date + " bin ich " + \
            str(self.__steps) + " Schritte gegangen."

# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.


# Objekt der Klasse step_counter durch Konstrukturaufruf erzeugen
# Das Datum wird auf den 11.11.2011 gesetzt
sc = step_counter("11.11.2011")

# Gehe 1111 Schritte
for i in range(0, 1111):
    sc.increment_steps()

# Gebe Schritte aus
print(sc)
