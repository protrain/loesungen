# Abstrakte Klasse zur Repräsentation eines Meetings.
# Von dieser Klasse kann keine Instanz (= Objekt) erzeugt werden.
class Meeting(object):
    # Konstruktor, der zur Angabe eines Meetingtitels und des
    # Wetters auffordert
    def __init__(self, title, meeting_start, meeting_end):
        self.__title = title
        self.__agenda = []
        self.__participants = []
        self.__start = meeting_start
        self.__end = meeting_end

    def add_to_agenda(self, element):
        self.__agenda.append(element)
    
    # Gibt die Agenda als mit Bulletinpoint-Liste zurück
    def get_agenda_as_string(self):
        if len(self.__agenda) > 0:
            agenda_string = "\n"
            
            # Gehe jedes Element in der Agenda durch
            for __agendaElement in self.__agenda:
                # Füge neue Zeile mit Bulletinpoint hinzu
                agenda_string += "- " + __agendaElement + "\n"
            return agenda_string
        
        # Keine Elemente vorhanden
        return "None\n"
    
    def add_participant(self, name):
        self.__participants.append(name)
        
    # Gibt die Teilnehmendenliste als String zurück
    def get_participants_as_string(self):
        if len(self.__participants) > 0:
            participants_string = ""
        
            # Gehe Liste der Teilnehmenden durch
            for participant in self.__participants:
                # Füge Eintrag hinzu
                participants_string += participant + ", "
            
            # Entferne die letzten zwei Zeichen nach der
            # letzten Iteration
            return participants_string[:-2]
        return "None"
  
    def __str__(self):
        output = ""
        output += "{} ({} - {})\n".format(self.__title, self.__start, self.__end)
        output += "Agenda: {}".format(self.get_agenda_as_string())
        output += "Participants: {}".format(self.get_participants_as_string())
        return output
  

# Öffentliche Klasse für ein physisches Meeting leitet
# von der Klasse Meeting ab.
class PhysicalMeeting(Meeting):
    # Konstruktor erwartet die Werte aus der abstrakten Klasse und dazu
    # noch den Raumnamen
    def __init__(self, title, meeting_start, meeting_end, room_name):
        # Titel, sowie Start- und Endzeitpunkt werden an die
        # überliegende Funktion übergeben.
        Meeting.__init__(self, title, meeting_start, meeting_end)

        self.room_name = room_name

    def __str__(self):
        return "{}\n Room:{}".format(Meeting.__str__(self), self.room_name)


# Öffentliche Klasse für ein digitales Meeting leitet
# von der Klasse Meeting ab.
class DigitalMeeting(Meeting):
    # Konstruktor erwartet die Werte aus der abstrakten Klasse und dazu
    # noch den Einwahllink
    def __init__(self, title, meeting_start, meeting_end, url):
        # Titel, sowie Start- und Endzeitpunkt werden an die
        # überliegende Funktion übergeben.
        Meeting.__init__(self, title, meeting_start, meeting_end)

        self.url = url

    def __str__(self):
        return "{}\nLink: {}".format(Meeting.__str__(self), self.url)


# Öffentliche Klasse für ein hybrides Meeting leitet
# von der Klasse Meeting ab.
class HybridMeeting(Meeting):
    # Konstruktor erwartet die Werte aus der abstrakten Klasse und dazu
    # noch den Raumnamen und den Einwahllink
    def __init__(self, title, meeting_start, meeting_end, room_name, url):
        # Titel, sowie Start- und Endzeitpunkt werden an die
        # überliegende Funktion übergeben.
        Meeting.__init__(self, title, meeting_start, meeting_end)

        self.room_name = room_name
        self.url = url

    def __str__(self):
        output = ""
        output += "{}\n".format(Meeting.__str__(self))
        output += "Room: {}\n".format(self.room_name)
        output += "Link: {}".format(self.url)
        return output


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    parameters = ["Physical Testmeeting",
                  "01.01.2023, 14:00",
                  "01.01.2023, 15:00",
                  "C121"]
    pm = PhysicalMeeting(*parameters)

    pm.add_to_agenda("Neues Tool besprechen")
    pm.add_to_agenda("Feedback von Stakeholdern")

    pm.add_participant("Rolf")
    pm.add_participant("Birgit")
    pm.add_participant("Dieter")
    pm.add_participant("Sandra")
    pm.add_participant("Manfred")

    print(pm)
    print("")

    parameters = ["Digital Textmeeting",
                  "02.01.2023, 11:15",
                  "02.01.2023, 15:00",
                  "https://protrain.github.io/conf?abcdefu"]
    dm = DigitalMeeting(*parameters)

    dm.add_to_agenda("Digitalisierung")
    dm.add_to_agenda("Ausprobieren Telko")
    dm.add_to_agenda("Sonstiges")

    dm.add_participant("Luigi")
    dm.add_participant("Mario")
    dm.add_participant("Giuliana")
    dm.add_participant("Pietro")

    print(dm)
    print("")

    parameters = [
        "Hybrid Testmeeting",
        "12.01.2023, 17:00",
        "12.01.2023, 18:00",
        "D181",
        "https://protrain.github.io/conf?abcdefu"]
    hm = HybridMeeting(*parameters)

    print(hm)


# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
