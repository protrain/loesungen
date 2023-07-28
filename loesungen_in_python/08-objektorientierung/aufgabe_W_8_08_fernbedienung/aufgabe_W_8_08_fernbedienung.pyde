# Klasse, die eine Fernbedienung realisiert
class RemoteControl:
    # Konstruktor, der die maximale Anzahl an Programm-
    # speicherplätzen zur Initialisierung übergeben
    # bekommt. Ohne diese Angabe kann kein Objekt der
    # Fernbedienung angelegt werden.
    def __init__(self, num_programs):
        self.__programs = []

        # Initialisiere angegebene Anzahl an Programmen
        for i in range(0, num_programs):
            self.__programs += ["Programm " + str(i + 1)]
        self.__current_program_number = 0

    # Methode zum Wechsel zum nächsten Programm
    def next_program(self):
        # Gehe um ein Programm nach oben,
        # wenn noch nicht am Ende der Liste
        if self.__current_program_number < len(self.__programs) - 1:
            self.__current_program_number += 1
        # Sonst beim ersten Programm wieder starten
        else:
            self.__current_program_number = 0

    # Methode zur Benennung des aktuellen Programms
    def set_program_name(self, name):
        self.__programs[self.__current_program_number] = name

    # Methode, um aktuelles Programm mit Sendernummer
    # auszugeben
    def print_program_name(self):
        print("Sendernummer: " + str(self.__current_program_number))
        print("Programm: " + self.__programs[self.__current_program_number])
        print("")


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
