###################################################
# Lösung von dabidan (https://github.com/dabidan)
# "Vereinfachung der Klassen und Anpassung an PEP8"
###################################################

class ListItem(object):
    """ Öffentliche Klasse zur Repräsentation eines Listeneintrags """

    def __init__(self, entry):
        """ Öffentlicher Initialisierer, der einen Eintrag als String
        erwartet und als nicht überprüft voreinstellt """
        self.entry = entry
        self.checked = False

    def __str__(self):
        """ Öffentliche Methode zur Repräsentation eines
        beschreibenden ListItem """
        return "%s(%s)" % (self.entry, self.checked)


class TodoList:
    """ Öffentliche Klasse zur Verwaltung einer ToDoList """

    def __init__(self):
        """ Öffentlicher Initialisierer erzeugt leere Liste """
        self.list = []

    def add_item(self, item):
        """ Öffentliche Methode zum Hinzufügen eines neuen
        ListItems-Objekts """
        self.list.append(item)

    def check_item(self, entry):
        """ Öffentliche Methode zum Setzen des Status eines
        Listeneintrags """
        # Gehe Liste durch
        for item in self.list:
            # Wenn Eintrag mit Gesuchtem übereinstimmt, dann abhaken.
            if item.entry == entry:
                item.checked = True

                # Springe aus Schleife
                break

    def __str__(self):
        """ Methode zur Repräsentation aller Einträge in der
        To-do-Liste. Das Ergebnis wird von der Methode zurück-
        gegeben. """
        # Rückgabestring
        return "".join(map("{}\n".format, self.list))


class ShoppingItem(ListItem):
    """ Öffentliche Klasse zur Repräsentation eines Einkaufslisten-
    eintrags. Hierzu wird von der Klasse ListItem abgeleitet, und
    die für einen Einkaufslisteneintrag charakterisierenden Merkmale
    werden hinzugefügt. """

    def __init__(self, entry, amount):
        """ Öffentlicher Konstruktor, der einen Eintrag als String sowie
        die Menge dieses Eintrags verlangt """
        # Aufruf des Basisklassenkonstruktors
        ListItem.__init__(self, entry)

        # Zusätzlich wird noch die Menge festgehalten.
        self.amount = amount

    def __str__(self):
        """ Öffentliche Methode zur Repräsentation eines
        aussagekräftigen Strings für einen Einkaufslisteneintrag """
        # rufe toString-Methode der Superklasse auf
        return "%sx %s(%s)" % (self.amount, self.entry, self.checked)


class ShoppingList:
    """ Klasse zur Verwaltung einer Shopping-Liste """

    def __init__(self):
        """ Öffentlicher Initialisierer erzeugt leere Liste """
        self.list = []

    def add_item(self, item):
        """ Öffentliche Methode zum Hinzufügen eines neuen
        ListItems-Objekts """
        self.list.append(item)

    def check_item(self, entry):
        """ Öffentliche Methode zum Setzen des Status eines
        Listeneintrags """
        # Gehe Liste durch
        for item in self.list:
            # Wenn Eintrag mit Gesuchtem übereinstimmt, dann abhaken.
            if item.entry == entry:
                item.checked = True

                # Springe aus Schleife
                break

    def __str__(self):
        """Öffentliche Methode zur Repräsentation der Shopping-Liste. """
        # Rückgabestring
        return "".join(map("{}\n".format, self.list))

# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

tdl = TodoList()
tdl.add_item(ListItem("Erster Eintrag"))
tdl.add_item(ListItem("Zweiter Eintrag"))
tdl.check_item("Zweiter Eintrag")
print tdl

sl = ShoppingList()
sl.add_item(ShoppingItem("Aepfel", 3))
sl.add_item(ShoppingItem("Birnen", 1))
sl.add_item(ShoppingItem("Toastbrot", 2))
sl.add_item(ShoppingItem("Birnenbaum", 2))
print sl
sl.check_item("Birnen")
print sl
