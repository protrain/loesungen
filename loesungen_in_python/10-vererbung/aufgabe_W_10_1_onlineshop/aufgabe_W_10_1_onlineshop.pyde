# Öffentliche Klasse zur Repräsentation eines Artikels
class Article(object):

    # Konstruktor, der die Artikelnummer und den Preis
    # erforderlich macht
    def __init__(self, articleNumber, price):
        self.__articleNumber = articleNumber
        self.__price = price

    # Getter-Methode, die den Preis zurückliefert
    def getPrice(self):
        return self.__price


# Öffentliche Klasse, die ein Buch repräsentiert
# Die Klasse erbt von der Klasse Artikel.
class Book(Article):
    # Der Mehrwertsteuersatz für Bücher (7 %) wird durch die
    # statische Konstante VAT repräsentiert.
    vat = 0.07

    # Öffentlicher Konstruktor mit der Vorschrift
    # zum Anlegen eines Buchobjekts
    def __init__(self, articleNumber, price, author, title, year):
        # Aufruf des Konstruktors der Basisklasse Article
        Article.__init__(self, articleNumber, price)

        # Zusätzlich werden die charakterisierenden
        # Eigenschaften eines Buchs gesetzt.
        self.__author = author
        self.__title = title
        self.__year = year

    # Öffentliche Methode zur Berechnung des Bruttopreises
    def getPrice(self):
        # Rufe für Nettopreis die Methode in der Superklasse auf
        # und addiere die für Bücher geltende Mehrwertsteuer.
        price = super(Book, self).getPrice()
        price += super(Book, self).getPrice() * Book.vat

        return price

    # Öffentliche Methode, die einen geeigneten String generiert
    # und zurückliefert
    def __str__(self):
        output = "Buch - " + self.__author + ": "
        output += self.__title + " (" + str(self.__year) + ")"
        return output


# Klasse, die eine DVD repräsentiert und von der Klasse
# Article ableitet
class DVD(Article):

    # Statische Konstante für Mehrwertsteuersatz für DVDs (19 %)
    vat = 0.19

    # Öffentlicher Konstruktor der Klasse DVD. Zum Generieren eines
    # Objekts der Klasse DVD werden die angegebenen Werte verlangt.
    def __init__(
            self,
            articleNumber,
            price,
            name,
            duration,
            countryCode):
        # Aufruf des Basisklassenkonstruktors
        Article.__init__(self, articleNumber, price)

        # Zusätzliche Daten werden in den internen Variablen abgelegt.
        self.__name = name
        self.__duration = duration
        self.countryCode = countryCode

    # Öffentliche Methode zur Berechnung des Bruttopreises
    def getPrice(self):
        # Rufe für Nettopreis die Methode in der Superklasse auf
        # und addiere die für Bücher geltende Mehrwertsteuer.
        price = super(DVD, self).getPrice()
        price += super(DVD, self).getPrice() * DVD.vat

        return price

    # Öffentliche Methode, die einen DVD-repräsentativen String
    # zurückliefert
    def __str__(self):
        return "DVD - " + self.__name


# Klasse, die einen Warenkorb realisiert
class ShoppingCart:

    # Öffentlicher Konstruktor, der den internen
    # Warenkorb initialisiert.
    def __init__(self):
        # Noch leerer Warenkorb
        self.__cart = []

    # Öffentliche Methode zum Hinzufügen eines Artikels
    # zum Warenkorb. Der Artikel wird in Form eines
    # Article-Objekts realisiert. Da sowohl Bücher als
    # auch DVDs von der Klasse Article erben, sind beide
    # Typen hier erlaubt und werden dafür auf die Basis-
    # Implementierung zurückgecastet.
    def addToCart(self, article):
        self.__cart.append(article)

    # Öffentliche Methode, die eine Rechnung auf der
    # Konsole druckt
    def showBill(self):
        # Gesamtpreis
        sum = 0.0

        # Jeden Artikel durchgehen
        for article in self.__cart:
            # Gebe Namen und Preis aus
            print str(article) + "\t " + str(article.getPrice()) + " Euro"

            # Addiere zu Gesamtpreis
            sum += article.getPrice()

        print "------------------------------------"

        # Gebe Gesamtpreis aus
        print "Gesamtpreis: " + str(sum) + " Euro"


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

book = Book(122767676, 32.71, "Luigi Lo Iacono", "WebSockets", 2015)
dvd1 = DVD(122767676, 14.95, "Spiel mir das Lied vom Tod", "99:12", 1)
dvd2 = DVD(122767676, 8.40, "Casablanca, Classic Collection", "99:12", 1)

wk = ShoppingCart()
wk.addToCart(book)
wk.addToCart(dvd1)
wk.addToCart(dvd2)
wk.showBill()
