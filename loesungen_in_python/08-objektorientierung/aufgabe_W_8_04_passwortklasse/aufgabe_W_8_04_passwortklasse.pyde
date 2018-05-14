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
    def isStrong(password):
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
    def change(self, oldPwd, newPwd):
        # Handelt es sich nicht um ein starkes Passwort,
        # folgt ein Abbruch, und es wird 'false' zurückgegeben.
        if self.isStrong(newPwd) == False:
            return False

        # Entspricht das eingegebene alte Passwort hinsichtlich
        # der Länge nicht dem im Speicher, erfolgt
        # der Abbruch.
        if len(oldPwd) != len(self.__password):
            return False

        # Entspricht das eingegebene alte Passwort (Buchstabe
        # für Buchstabe) nicht dem Passwort aus dem Speicher,
        # erfolgt ebenfalls ein Abbruch
        for i in range(0, len(oldPwd)):
            if self.__password[i] != oldPwd[i]:
                return False

        # Ansonsten wird das neu eingegebene Passwort übernommen
        # und dazu das Char-Array kopiert
        self.__password = []
        for c in newPwd:
            self.__password.append(c)
        return True

    # Methode zum Zurücksetzen des Passworts
    def delete(self):
        self.__password = None


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

testPW = list("PassW15!!")

pw = Password(list("Passwort123"))

# Neues Passwort unsicher -> Passwort nicht geändert
println(pw.change(list("Passwort123"),
                  list("Passwort1234")))

# Altes Passwort falsch -> Passwort nicht geändert
println(pw.change(list("AnderesPasswort"),
                  testPW))

# Altes Passwort korrekt -> Ändere Passwort
println(pw.change(list("Passwort123"), testPW))

# Ändere ein Element im testPW-Array
# Sollte Referenz übergeben worden sein, wird ein Fehler auftreten
testPW[0] = 's'

println(pw.change(list("PassW15!!"), list("NewPW!16")))
