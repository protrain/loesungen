# Klasse, die eine Fernbedienung realisiert
class RemoteControl:

    # Konstruktor, der die maximale Anzahl an Programm-
    # speicherplätzen zur Initialisierung übergeben
    # bekommt. Ohne diese Angabe kann kein Objekt der
    # Fernbedienung angelegt werden.
    def __init__(self, numPrograms):
        self.__programs = []

        # Initialisiere angegebene Anzahl an Programmen
        for i in range(0, numPrograms):
            self.__programs += ["Programm " + str(i + 1)]
        self.__currentProgramNumber = 0

    # Methode zum Wechsel zum nächsten Programm
    def nextProgram(self):
        # Gehe um ein Programm nach oben,
        # wenn noch nicht am Ende der Liste
        if self.__currentProgramNumber < len(self.__programs) - 1:
            self.__currentProgramNumber += 1
        # Sonst beim ersten Programm wieder starten
        else:
            self.__currentProgramNumber = 0

    # Methode zur Benennung des aktuellen Programms
    def setProgramName(self, name):
        self.__programs[self.__currentProgramNumber] = name

    # Methode, um aktuelles Programm mit Sendernummer
    # auszugeben
    def printProgramName(self):
        print "Sendernummer: " + str(self.__currentProgramNumber)
        print "Programm: " + self.__programs[self.__currentProgramNumber]
        print


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Testdurchlauf
rc = RemoteControl(5)
rc.setProgramName("ARD")
rc.printProgramName()

# Gehe drei Sender weiter und gebe jeden aus
for i in range(0, 3):
    rc.nextProgram()

# Setze Sendername
rc.setProgramName("RTL")
rc.printProgramName()

# Gehe sechs Mal nach vorne
for i in range(0, 6):
    rc.nextProgram()
    rc.printProgramName()
