# Öffentliche Klasse für die Repräsentation einer Zutat
class Zutat:

    # Konstruktor, der die Angabe der Zutat, Menge und Einheit
    # erwartet
    def __init__(self, name, menge, einheit):
        self.name = name
        self.menge = menge
        self.einheit = einheit

    # Öffentliche Methode zur Generierung eines geeigneten
    # Strings zur Repräsentation der Zutat
    def __str__(self):
        return str(self.menge) + self.einheit + " " + self.name


# Öffentliche Klasse für die Repräsentation einer
# Kochanweisung
class Anweisung:

    # Öffentlicher Konstruktor, der regelt, dass eine Instanz
    # dieser Klasse nur unter Angabe des Anweisungstexts und
    # der Positionsnummer angelegt werden kann
    def __init__(self, text, position):
        self.text = text
        self.position = position

    # Öffentliche Methode zur Generierung eines geeigneten
    # Strings zur Ausgabe
    def __str__(self):
        return str(self.position) + ". " + self.text


# Öffentliche Klasse für ein ganzes Rezept
class Kochrezept:

    # Öffentlicher Konstruktor. Eine Objekt der Klasse kann
    # nur dann instanziiert werden, wenn der Name, die
    # vermeintliche Zeit, die Zutaten, Anweisungen und eine
    # generelle Herdanweisung angegeben werden.
    def __init__(self, name, zeit, zutatenliste, anweisungsliste,
                 herd_anweisung):
        self.name = name
        self.zeit = zeit
        self.anweisungen = anweisungsliste
        self.zutaten = zutatenliste
        self.herd_anweisung = herd_anweisung

    # Öffentliche Methode zum Generieren eines repräsentativen
    # Strings für das Kochrezept
    def __str__(self):
        output = ""
        output += "- " + self.name + \
            " (" + str(self.zeit) + " Minuten) -\n"
        output += "\nZutaten:\n"

        # Alle Zutaten durchgehen
        i = 0
        for zutat in self.zutaten:
            output += "- " + str(zutat) + "\n"
            i += 1

        output += "\nZubereitung:\n"

        # Alle Anweisungen durchgehen
        for anweisung in self.anweisungen:
            output += str(anweisung) + "\n"

        output += str((len(self.anweisungen) + 1)) + \
            ". " + self.herd_anweisung

        return output


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

zutaten = []
zutaten.append(Zutat("Kartoffelmehl", 80, "g"))
zutaten.append(Zutat("Maisstärke", 80, "g"))
zutaten.append(Zutat("Eier", 3, ""))
zutaten.append(Zutat("Milch", 400, "ml"))
zutaten.append(Zutat("Traubenzucker", 5, "EL"))
zutaten.append(Zutat("Pflanzenöl", 5, "EL"))

anweisungen = []
anweisungen.append(Anweisung("Die Mehle vermischen und sieben.", 1))
anweisungen.append(Anweisung("Eier, Zucker und Milch dazugeben.", 2))
anweisungen.append(Anweisung("Alles mit dem Schneebesen gut verquirlen.",
                             3))
anweisungen.append(Anweisung("10 Minuten quellen lassen.", 4))
anweisungen.append(Anweisung("Noch einmal verrühren.", 5))

hinweis_herd = "Pfanne auf hoher Stufe erhitzen und Teig"
hinweis_herd += "portionsweise im heißen Öl ausbacken."

pfannkuchen = Kochrezept("Pfannkuchen", 30, zutaten, anweisungen,
                         hinweis_herd)

print(pfannkuchen)
