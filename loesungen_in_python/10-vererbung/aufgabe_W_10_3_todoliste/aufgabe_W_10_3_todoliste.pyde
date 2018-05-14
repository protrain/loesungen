# Öffentliche Klasse zur Repräsentation eines Listeneintrags
class ListItem(object):

    # Öffentlicher Konstruktor, der einen Eintrag als String
    # erwartet und als nicht überprüft voreinstellt
    def __init__(self, entry):
        self.__entry = entry
        self.__checked = False

    # Getter-Methode zur Abfrage des Entry-Strings
    def getEntry(self):
        return self.__entry

    # Getter-Methode zur Abfrage des Überprüfungsstatus
    def getChecked(self):
        return self.__checked

    # Setter-Methode mit dem Status als Parameter
    def setChecked(self, checked):
        self.__checked = checked

    # Öffentliche Methode zur Repräsentation eines
    # beschreibenden ListItem
    def __str__(self):
        return self.getEntry() + " (" + str(self.getChecked()) + ")"


# Öffentliche Klasse zur Verwaltung einer ToDoList
class TodoList:

    # Öffentlicher Konstruktor mit der Initialisierung
    # der internen Liste
    def __init__(self):
        self.__list = []

    # Öffentliche Methode zum Hinzufügen eines neuen
    # ListItems-Objekts
    def addItem(self, item):
        self.__list += [item]

    # Öffentliche Methode zum Setzen des Status eines
    # Listeneintrags
    def checkItem(self, entry):
        # Gehe Liste durch
        for item in self.__list:
            # Wenn Eintrag mit Gesuchtem übereinstimmt, dann abhaken.
            if item.getEntry() == entry:
                item.setChecked(True)

                # Springe aus Schleife
                break

    # Methode zur Repräsentation aller Einträge in der
    # To-do-Liste. Das Ergebnis wird von der Methode zurück-
    # gegeben.
    def __str__(self):
        # Rückgabestring
        output = ""

        # Gehe jedes Element durch.
        for item in self.__list:
            # Packe toString Methode in Rückgabe
            # und füge Zeilenumbruch hinzu
            output += str(item) + "\n"

        return output


# Öffentliche Klasse zur Repräsentation eines Einkaufslisten-
# eintrags. Hierzu wird von der Klasse ListItem abgeleitet, und
# die für einen Einkaufslisteneintrag charakterisierenden Merkmale
# werden hinzugefügt.
class ShoppingItem(ListItem):

    # Öffentlicher Konstruktor, der einen Eintrag als String sowie
    # die Menge dieses Eintrags verlangt
    def __init__(self, entry, amount):
        # Aufruf des Basisklassenkonstruktors
        ListItem.__init__(self, entry)

        # Zusätzlich wird noch die Menge festgehalten.
        self.__amount = amount

    # Öffentliche Methode zur Repräsentation eines
    # aussagekräftigen Strings für einen Einkaufslisteneintrag
    def __str__(self):
        # rufe toString-Methode der Superklasse auf
        return str(self.__amount) + "x " + self.getEntry() + \
            " (" + str(self.getChecked()) + ")"


# Klasse zur Verwaltung einer Shopping-Liste
class ShoppingList:

    # Öffentlicher Konstruktor, der die Liste initialisiert
    def __init__(self):
        self.__list = []

    # Öffentliche Methode, die einen Listeneintrag in Form
    # eines ListItem-Objekts entgegennimmt, um diesen dann
    # in die Einkaufsliste zu setzen.
    def addItem(self, item):
        self.__list += [item]

    # Öffentliche Methode zum Setzen des Status eines
    # Eintrags, der an die Methode übergeben wird
    def checkItem(self, entry):
        # Gehe Liste durch
        for item in self.__list:
            # Wenn Eintrag mit Gesuchtem übereinstimmt
            # dann abhaken
            if item.getEntry() == entry:
                item.setChecked(True)
                # Springe aus Schleife
                break

    # Öffentliche Methode zur Repräsentation der Shopping-Liste.
    def __str__(self):
        # Rückgabestring
        output = ""

        # gehe jedes Element durch
        for item in self.__list:
            # Packe toString-Methode in Rückgabe
            # und füge Zeilenumbruch hinzu
            output += str(item) + "\n"

        return output


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

tdl = TodoList()
tdl.addItem(ListItem("Erster Eintrag"))
tdl.addItem(ListItem("Zweiter Eintrag"))
tdl.checkItem("Zweiter Eintrag")
print tdl

sl = ShoppingList()
sl.addItem(ShoppingItem("Aepfel", 3))
sl.addItem(ShoppingItem("Birnen", 1))
sl.addItem(ShoppingItem("Toastbrot", 2))
sl.addItem(ShoppingItem("Birnenbaum", 2))
print sl
sl.checkItem("Birnen")
print sl
