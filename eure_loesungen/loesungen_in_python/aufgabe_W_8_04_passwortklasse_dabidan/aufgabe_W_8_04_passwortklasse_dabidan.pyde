###################################################
# Lösung von dabidan (https://github.com/dabidan)
# "Funktion vereinfacht und an PEP8 angeglichen"
###################################################

class Password:
    """ Klasse zur Repräsentation eines Passworts """
    def __init__(self, password):
        """ Initialisierer der Klasse, der die Objektgenerierung
        nur unter Angabe eines Passworts ermöglicht. """
        self._password = password

    @staticmethod
    def is_strong(password):
        """ Öffentliche Methode zur Prüfung auf ein starkes Passwort.
        Die Methode erhält als Eingangsparameter ein Passwort.
        Das Ergebnis der Prüfung wird am Ende zurückgegeben. """
        if len(password) < 8:
            return False

        # Variablen zur Prüfung der nötigen Voraussetzung deklarieren und
        # mit dem Wert 'False' initialisieren.
        lower = upper = figure = special = False

        # Prüfen
        for c in password:
            if 'a' <= c <= 'z':
                lower = True
            elif 'A' <= c <= 'Z':
                upper = True
            elif '0' <= c <= '9':
                figure = True
            elif c == '!' or c == '*':
                special = True

        # Sind alle Voraussetzungen erfüllt, gib True zurück
        return lower and upper and figure and special

    def change(self, old_password, new_password):
        """ Öffentliche Methode zum Ändern eines Passworts. Sowohl
        das bisherige wie auch das neue Passwort werden an die
        Methode als String-Array übergeben. Das Ergebnis der
        Änderung wird am Ende zurückgegeben. """

        # Handelt es sich nicht um ein starkes Passwort,
        # folgt ein Abbruch, und es wird 'False' zurückgegeben.
        if not self.is_strong(new_password):
            return False

        # Entspricht das eingegebene alte Passwort
        # nicht dem im Speicher, erfolgt der Abbruch.
        if old_password != self._password:
            return False

        # Ansonsten wird das neu eingegebene Passwort übernommen
        self._password = new_password
        return True

    # Methode zum Zurücksetzen des Passworts
    def delete(self):
        self._password = None


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

test_password = "PassW15!!"

pw = Password("Passwort123")

# Neues Passwort unsicher -> Passwort nicht geändert
print pw.change("Passwort123",
                  "Passwort1234")

# Altes Passwort falsch -> Passwort nicht geändert
print pw.change("AnderesPasswort",
                  test_password)

# Altes Passwort korrekt -> Ändere Passwort
print pw.change("Passwort123", test_password)
