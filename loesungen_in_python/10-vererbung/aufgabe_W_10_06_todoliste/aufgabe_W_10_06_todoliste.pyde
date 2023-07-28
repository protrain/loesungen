# Öffentliche Klasse zur Repräsentation eines Listeneintrags
class ListItem(object):

    # Öffentlicher Konstruktor, der einen Eintrag als String
    # erwartet und als nicht überprüft voreinstellt
    def __init__(self, entry):
        self.__entry = entry
        self.__checked = False

    # Getter-Methode zur Abfrage des Entry-Strings
    def get_entry(self):
        return self.__entry

    # Getter-Methode zur Abfrage des Überprüfungsstatus
    def get_checked(self):
        return self.__checked

    # Setter-Methode mit dem Status als Parameter
    def set_checked(self, checked):
        self.__checked = checked

    # Öffentliche Methode zur Repräsentation eines
    # beschreibenden ListItem
    def __str__(self):
        return self.get_entry() + " (" + str(self.get_checked()) + ")"


# Öffentliche Klasse zur Verwaltung einer ToDoList
class TodoList:

    # Öffentlicher Konstruktor mit der Initialisierung
    # der internen Liste
    def __init__(self):
        self.__list = []

    # Öffentliche Methode zum Hinzufügen eines neuen
    # ListItems-Objekts
    def add_item(self, item):
        self.__list += [item]

    # Öffentliche Methode zum Setzen des Status eines
    # Listeneintrags
    def check_item(self, entry):
        # Gehe Liste durch
        for item in self.__list:
            # Wenn Eintrag mit Gesuchtem übereinstimmt, dann abhaken.
            if item.get_entry() == entry:
                item.set_checked(True)

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
        return str(self.__amount) + "x " + self.get_entry() + \
            " (" + str(self.get_checked()) + ")"


# Klasse zur Verwaltung einer Shopping-Liste
class ShoppingList:

    # Öffentlicher Konstruktor, der die Liste initialisiert
    def __init__(self):
        self.__list = []

    # Öffentliche Methode, die einen Listeneintrag in Form
    # eines ListItem-Objekts entgegennimmt, um diesen dann
    # in die Einkaufsliste zu setzen.
    def add_item(self, item):
        self.__list += [item]

    # Öffentliche Methode zum Setzen des Status eines
    # Eintrags, der an die Methode übergeben wird
    def check_item(self, entry):
        # Gehe Liste durch
        for item in self.__list:
            # Wenn Eintrag mit Gesuchtem übereinstimmt
            # dann abhaken
            if item.get_entry() == entry:
                item.set_checked(True)
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
tdl.add_item(ListItem("Erster Eintrag"))
tdl.add_item(ListItem("Zweiter Eintrag"))
tdl.check_item("Zweiter Eintrag")
print(tdl)

sl = ShoppingList()
sl.add_item(ShoppingItem("Aepfel", 3))
sl.add_item(ShoppingItem("Birnen", 1))
sl.add_item(ShoppingItem("Toastbrot", 2))
sl.add_item(ShoppingItem("Birnenbaum", 2))
print(sl)
sl.check_item("Birnen")
print(sl)
