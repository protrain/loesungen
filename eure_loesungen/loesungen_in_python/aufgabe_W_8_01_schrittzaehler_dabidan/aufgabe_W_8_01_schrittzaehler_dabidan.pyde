###################################################
# Lösung von dabidan (https://github.com/dabidan)
# "Anpassungen an PEP8"
###################################################

# Klasse, die den Schrittzähler realisiert
class StepCounter:
    # Alle Instanzvariablen werden im Initialisierer gesetzt.
    def __init__(self, date):
        self._date = date
        self._steps = 0

    # Öffentliche Methode, um den Schrittzähler um 1 zu erhöhen
    def increment_steps(self):
        self._steps += 1

    # Öffentliche Methode zur Erzeugung einer Statusnachricht, die
    # zurückgegeben wird
    def __str__(self):
        return "Am %s bin ich %s Schritte gegangen." % (self._date, self._steps)

# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Objekt der Klasse StepCounter durch Konstrukturaufruf erzeugen
# Das Datum wird auf den 11.11.2011 gesetzt
sc = StepCounter("11.11.2011")

# Gehe 1111 Schritte
for i in range(0, 1111):
    sc.increment_steps()

# Gebe Schritte aus
print sc
