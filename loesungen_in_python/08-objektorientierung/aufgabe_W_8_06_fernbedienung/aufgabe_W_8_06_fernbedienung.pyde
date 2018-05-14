class RemoteControl:
    """ Klasse, die eine Fernbedienung realisiert """

    def __init__(self, num_programs):
        """ Initialisierer, der die maximale Anzahl an Programm-
        speicherplätzen zur Initialisierung übergeben
        bekommt. Ohne diese Angabe kann kein Objekt der
        Fernbedienung angelegt werden."""
        self._programs = []

        # Initialisiere angegebene Anzahl an Programmen
        for i in range(1, numPrograms + 1):
            self._programs.append("Programm %s" %i)
         self._current_program_number = 0

    def next_program(self):
        """ Methode zum Wechsel zum nächsten Programm """
        # Gehe um ein Programm nach oben,
        # wenn noch nicht am Ende der Liste
        if self._current_program_number < len(self._programs) - 1:
            self._current_program_number += 1
        # Sonst beim ersten Programm wieder starten
        else:
            self._current_program_number = 0

    # Methode zur Benennung des aktuellen Programms
    def set_program_name(self, name):
        self._programs[self._current_program_number] = name

    # Methode, um aktuelles Programm mit Sendernummer
    # auszugeben
    def print_program_name(self):
        print "Sendernummer: %s" % self._current_program_number
        print "Programm: %s" % self._programs[self._current_program_number]
        print


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Testdurchlauf
rc = RemoteControl(5)
rc.set_program_name("ARD")
rc.print_program_name()

# Gehe drei Sender weiter und gebe jeden aus
for i in range(0, 3):
    rc.next_program()

# Setze Sendername
rc.set_program_name("RTL")
rc.print_program_name()

# Gehe sechs Mal nach vorne
for i in range(0, 6):
    rc.next_program()
    rc.print_program_name()
