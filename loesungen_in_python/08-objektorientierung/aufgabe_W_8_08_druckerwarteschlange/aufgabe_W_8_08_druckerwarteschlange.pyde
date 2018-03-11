# Klasse zur Realisierung einer Druckerwarteschlange
class PrinterQueue:

    # Konstruktor mit der Angabe der maximalen Warte-
    # schlangengröße. Ohne diese Angabe kann später keine
    # Instanz (= Objekt) erzeugt werden.
    # Die internen Werte werden initialisiert.
    def __init__(self, maxJobs):
        self.__jobs = []
        self.__maxJobs = maxJobs

    # Methode, um einen Druckauftrag der Warteschlange
    # hinzuzufügen. Der Job wird als String übergeben.
    # Die Methode hat keinen Rückgabewert, kann aber eine
    # Exception auslösen, wenn die Anzahl der Jobs überschritten
    # wird.
    def addJob(self, job):
        # Füge hinzu, solange noch nicht voll besetzt
        if len(self.__jobs) < self.__maxJobs:
            self.__jobs += [job]
        else:
            # Voll besetzt, gebe Fehler zurück
            print "Exception: Number of Jobs exceeded"

    # Methode, die den nächsten Job zurückliefert, sofern noch
    # einer in der Pipe steht. Es wird kein Parameter an die Funktion
    # übergeben. Als Ergebnis wird der Job als String zurückgeliefert.
    def nextJob(self):
        # Wenn Auftrag in der Liste existiert
        if len(self.__jobs) > 0:
            # Nehme erstes Element
            job = self.__jobs[0]

            # Sortiere Array um, um erstes zu löschen
            self.__jobs = self.__jobs[1:]

            return job
        else:
            return None


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.
pq = PrinterQueue(1)

pq.addJob("Hallo")

# Warteschlange voll. Jetzt sollte Fehler kommen
pq.addJob("Weiter")

# Arbeite Warteschlange ab
print pq.nextJob()
print pq.nextJob()
print pq.nextJob()

# Jetzt ist Speicher leer,
# sollte also wieder gehen
pq.addJob("Weiter")
