// Klasse zur Repräsentation eines Passworts
public class Password {
  // private Variablen
  private char[] password;

  // Konstruktor der Klasse, der die Objektgenerierung
  // nur unter Angabe eines Passworts in Form eines Char-Arrays
  // ermöglicht.
  public Password(char[] password) {
    // Reservieren des nötigen Speicherbereichs
    this.password = new char[password.length];

    // Kopiere Char-Array in den separaten Speicher
    // der internen Variablen
    for (int i = 0; i < password.length; i++) {
      this.password[i] = password[i];
    }
  }

  // Öffentliche Methode zur Prüfung auf ein starkes Passwort. Die Methode
  // erhält als Eingangsparameter ein Passwort als Char-Array.
  // Das Ergebnis der Prüfung wird am Ende zurückgegeben.
  public boolean isStrong(char[] password) {
    if (password.length < 8) {
      return false;
    }

    // Variablen zur Prüfung der nötigen Voraussetzung deklarieren und
    // mit dem Wert 'false' initialisieren.
    boolean lower = false,
    upper = false,
    figure = false,
    special = false;

    // Prüfen
    for (int i = 0; i < password.length; i++) {
      if (password[i] >= 'a' && password[i] <= 'z') {
        lower = true;
      }
      else if (password[i] >= 'A' && password[i] <= 'Z') {
        upper = true;
      }
      else if (password[i] >= '0' && password[i] <= '9') {
        figure = true;
      }
      else if (password[i] == '!' || password[i] == '*') {
        special = true;
      }
    }

    // Sind alle Voraussetzungen erfüllt, gib das Ergebnis zurück
    if (lower && upper && figure && special) {
      return true;
    }
    else {
      return false;
    }
  }

  // Öffentliche Methode zum Ändern eines Passworts. Sowohl
  // das bisherige wie auch das neue Passwort werden an die
  // Methode als String-Array übergeben. Das Ergebnis der
  // Änderung wird am Ende zurückgegeben
  public boolean change(char[] oldPwd, char[] newPwd) {
    // Handelt es sich nicht um ein starkes Passwort,
    // folgt ein Abbruch, und es wird 'false' zurückgegeben
    if (!isStrong(newPwd)) {
      return false;
    }

    // Entspricht das eingegebene alte Passwort hinsichtlich
    // der Länge nicht dem im Speicher, erfolgt
    // der Abbruch.
    if (oldPwd.length != password.length) {
      return false;
    }

    // Entspricht das eingegebene alte Passwort (Buchstabe
    // für Buchstabe) nicht dem Passwort aus dem Speicher,
    // erfolgt ebenfalls ein Abbruch.
    for (int i = 0; i < oldPwd.length; i++) {
      if (password[i] != oldPwd[i]) {
        return false;
      }
    }

    // Ansonsten wird das neu eingegebene Passwort übernommen
    // und dazu das Char-Array kopiert
    this.password = new char[newPwd.length];
    for (int i = 0; i < newPwd.length; i++) {
      password[i] = newPwd[i];
    }
    return true;
  }

  // Methode zum Zurücksetzen des Passworts
  public void delete() {
    password = null;
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  char[] testPW = "PassW15!!".toCharArray();

  Password pw = new Password("Passwort123".toCharArray());

  // Neues Passwort unsicher -> Passwort nicht geändert
  println(
    pw.change("Passwort123".toCharArray(), "Passwort1234".toCharArray())
  );

  // Altes Passwort falsch -> Passwort nicht geändert
  println(pw.change("AnderesPasswort".toCharArray(), testPW));

  // Altes Passwort korrekt -> Ändere Passwort
  println(pw.change("Passwort123".toCharArray(), testPW));

  // Ändere ein Element im testPW-Array
  // Sollte Referenz übergeben worden sein, wird ein Fehler auftreten
  testPW[0] = 's';

  println(pw.change("PassW15!!".toCharArray(), "NewPW!16".toCharArray()));
}

