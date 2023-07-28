# Klasse zur Repräsentation eines Passworts
class Password:
    # Konstruktor der Klasse, der die Objektgenerierung
    # nur unter Angabe eines Passworts in Form eines Char-Arrays
    # ermöglicht.
    def __init__(self, password):
        self.__password = []

        # Kopiere Char-Array in den separaten Speicher
        # der internen Variablen
        for i in range(0, len(password)):
            self.__password.append(password[i])

    # Öffentliche Methode zur Prüfung auf ein starkes Passwort. Die Methode
    # erhält als Eingangsparameter ein Passwort als Char-Array.
    # Das Ergebnis der Prüfung wird am Ende zurückgegeben.
    @staticmethod
    def is_strong(password):
        if len(password) < 8:
            return False

        # Variablen zur Prüfung der nötigen Voraussetzung deklarieren und
        # mit dem Wert 'False' initialisieren.
        lower = False
        upper = False
        figure = False
        special = False

        # Prüfen
        for c in password:
            if c >= 'a' and c <= 'z':
                lower = True
            elif c >= 'A' and c <= 'Z':
                upper = True
            elif c >= '0' and c <= '9':
                figure = True
            elif c == '!' or c == '*':
                special = True

        # Sind alle Voraussetzungen erfüllt, gib das Ergebnis zurück
        if lower and upper and figure and special:
            return True
        else:
            return False


    # Öffentliche Methode zum Ändern eines Passworts. Sowohl
    # das bisherige wie auch das neue Passwort werden an die
    # Methode als String-Array übergeben. Das Ergebnis der
    # Änderung wird am Ende zurückgegeben.
    def change(self, old_pwd, new_pwd):
        # Handelt es sich nicht um ein starkes Passwort,
        # folgt ein Abbruch, und es wird 'false' zurückgegeben.
        if self.is_strong(new_pwd) is False:
            return False

        # Entspricht das eingegebene alte Passwort hinsichtlich
        # der Länge nicht dem im Speicher, erfolgt
        # der Abbruch.
        if len(old_pwd) != len(self.__password):
            return False

        # Entspricht das eingegebene alte Passwort (Buchstabe
        # für Buchstabe) nicht dem Passwort aus dem Speicher,
        # erfolgt ebenfalls ein Abbruch
        for i in range(0, len(old_pwd)):
            if self.__password[i] != old_pwd[i]:
                return False

        # Ansonsten wird das neu eingegebene Passwort übernommen
        # und dazu das Char-Array kopiert
        self.__password = []
        for c in new_pwd:
            self.__password.append(c)
        return True

    # Methode zum Zurücksetzen des Passworts
    def delete(self):
        self.__password = None


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

test_pw = list("PassW15!!")

pw = Password(list("Passwort123"))

# Neues Passwort unsicher -> Passwort nicht geändert
print(pw.change(list("Passwort123"),
                list("Passwort1234")))

# Altes Passwort falsch -> Passwort nicht geändert
print(pw.change(list("AnderesPasswort"),
                test_pw))

# Altes Passwort korrekt -> Ändere Passwort
print(pw.change(list("Passwort123"), test_pw))

# Ändere ein Element im test_pw-Array
# Sollte Referenz übergeben worden sein, wird ein Fehler auftreten
test_pw[0] = 's'

print(pw.change(list("PassW15!!"), list("NewPW!16")))
