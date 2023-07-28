# Klasse zur Repräsentation eines Kontakts
class Contact:

    # Konstruktor, der zur Initialisierung der Klassen-
    # variablen die Id, Name, E-Mail-Adresse, Telefonnummer
    # und Twitter-Adresse vorschreibt.
    def __init__(self, contact_id, name, email, phone, social):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__social = social
        self.__id = contact_id

    # Öffentliche Methode zur Generierung eines
    # Strings mit den Kontaktdaten. Der generierte String
    # wird von der Methode zurückgeliefert.
    def __str__(self):
        output = str(self.__id) + ": " + self.__name + "\t"
        output += self.__email + "\t" + self.__phone + "\t" + self.__social
        return output

    # Öffentliche Methode zur Rückgabe des Namens
    def get_name(self):
        return self.__name

    # Öffentliche Methode zur Rückgabe der Id
    def get_id(self):
        return self.__id

# Öffentliche Klasse, die ein Adressbuch realisiert


class Adressbook:

    # Konstruktor, der für die Instanziierung den
    # Namen erfordert.
    def __init__(self, name):
        self.__name = name
        self.__contacts = []

    # Öffentliche Methode zur Generierung eines Strings
    # mit allen Adressbucheinträgen. Der String wird von
    # der Methode zurückgeliefert.
    def show_all(self):
        output = "Adressbuch: " + self.__name + "\n"

        # Gehe jeden Kontakt durch
        for contact in self.__contacts:
            # Schreibe Inhalt der toString-Methode in
            # Ausgabe-Variable mit Zeilenumbruch
            output += str(contact) + "\n"

        return output

    # Öffentliche Methode zur Suche und Rückgabe des
    # Kontakts. Der Name der zu suchenden Person
    # wird an die Methode übergeben. Der generierte
    # String des Kontakts wird im Erfolgsfall zurück-
    # geliefert, ansonsten ein leerer String.
    def show_by_name(self, name):
        # Gehe Kontaktliste durch und suche den Namen
        for contact in self.__contacts:
            # Stimmt der Name überein
            if contact.get_name() == name:
                # Gebe den Eintrag als String zurück und
                # springe aus Funktion
                return str(contact)

    # Öffentliche Methode zum Hinzufügen eines Kontakts.
    # Der Kontakt muss als Contact-Objekt an die Methode
    # übergeben werden.
    def add_contact(self, contact):
        self.__contacts.append(contact)

    # Öffentliche Methode zum Suchen eines Kontakts nach
    # der Id. Diese muss an die Funktion übergeben werden.
    # Der Kontakt wird im Erfolgsfall zurückgeliefert -
    # ansonsten wird null zurückgeliefert.
    def get_contact(self, contact_id):
        # Gehe Kontaktliste durch und suche die ID
        for contact in self.__contacts:
            # Stimmt die ID überein
            if contact.get_id() == contact_id:
                # Gebe den Eintrag zurück und
                # springe aus Funktion
                return contact

    # Methode zum Entfernen eines Kontakts aus dem Adressbuch.
    # An die Methode muss die eindeutige Id übergeben werden.
    def remove_contact(self, contact_id):
        # Lege Kopie der Liste an
        contacts_copy = []
        # Gehe Kontaktliste durch und suche die ID
        for contact in self.__contacts:
            # Stimmt die ID nicht überein
            if contact.get_id() != contact_id:
                # füge Kontakt hinzu
                contacts_copy.append(contact)

            # Wenn ID übereinstimmt, wird Kontakt
            # nicht hinzugefügt (= gelöscht)

        # Übernehme neue Liste
        self.__contacts = contacts_copy


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

# Privates Adressbuch
privat = Adressbook("Privat")
privat.add_contact(Contact(1, "Ken Tern", "ken.tern@mail.de",
                           "+49 221 3982781", "@kentern"))
privat.add_contact(Contact(2, "Bill Iger", "bill.iger@gmx.de",
                           "+49 211 9821348", "@billiger"))
privat.add_contact(Contact(3, "Flo Kati", "flo.kati@web.de",
                           "+49 251 9346441", "@flokati"))
privat.add_contact(Contact(4, "Ingeborg Mirwas", "inge.mirwas@post.de",
                           "+49 228 4663289", "@borgmirwas"))
privat.add_contact(Contact(5, "Ann Schweigen", "ann.schweigen@gmx.de",
                           "+49 231 6740921", "@annschweigen"))
privat.add_contact(Contact(6, "Mark Enschuh", "mark.enschuh@gmail.com",
                           "+49 234 4565657", "@markenschuh"))
privat.add_contact(Contact(7, "Lee Köhr", "lee.koehr@mail.de",
                           "+49 561 8976761", "@leekoehr"))
privat.add_contact(Contact(8, "Pit Schnass", "pit.schnass@post.de",
                           "+49 721 4545754", "@pitschnass"))

# Geschäftliches Adressbuch
arbeit = Adressbook("Arbeit")
arbeit.add_contact(Contact(1, "Phil Tertüte", "phil.tertuete@company.de",
                           "+49 177 1786756", "@philtertuete"))
arbeit.add_contact(Contact(2, "Flo Kati", "flo.kati@laden.com",
                           "+49 161 2336541", "@ibm.kati"))
arbeit.add_contact(Contact(3, "Andreas Kreuz", "andreas.kreuz@bazaar.de",
                           "+49 163 3442889", "@asbazaar"))
arbeit.add_contact(Contact(4, "Erkan Alles", "erkan.alles@solver.de",
                           "+49 171 1442553", "@easolver"))
arbeit.add_contact(Contact(5, "Mark Reele", "mark.reele@media.de",
                           "+49 151 5345612", "@mrmedia"))
arbeit.add_contact(Contact(6, "Roy Bär", "roy.baer@media.de",
                           "+49 151 5477889", "@rbmedia"))
arbeit.add_contact(Contact(7, "Mario Nette", "mario.nette@media.de",
                           "+49 151 5113341", "@mnmedia"))
arbeit.add_contact(Contact(8, "Klaus Uhr", "klaus.uhr@media.de",
                           "+49 151 6743431", "@kumedia"))

print(privat.show_all())
print(privat.get_contact(5))
print(privat.remove_contact(5))
print(privat.show_all())

print(arbeit.show_by_name("Flo Kati"))
