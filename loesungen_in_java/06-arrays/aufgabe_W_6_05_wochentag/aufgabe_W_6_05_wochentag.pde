// Funktion zur Berechnung des Wochentags
// Erhält als Eingabeparameter ganzzahlige Werte für
// den Tag, den Montag und das Jahr
void calcDayOfWeek(int inputDay, int inputMonth, int inputYear) {
  // Letzten zwei Ziffern bestimmen, indem der Modulo-Operator ein-
  // gesetzt wird um den Rest zu berechnen.
  int dayOfWeek = inputYear % 100;

  // Ganzzahligen Anteil eines Viertels hinzuaddieren
  // Das Ergebnis einer Division mit Integer-Zahlen liefert
  // den ganzzahligen Wert der Division.
  dayOfWeek = dayOfWeek + (dayOfWeek / 4);

  // Zuweisung Additionswerte für Monat
  // Erster Wert = 0, um Zuweisung einfacher zu machen
  // Erster Monat ist also in monthAdd[1] gespeichert
  int[] monthAdd = { 0, 1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6 };


  // Werte entsprechend des Monats addieren
  dayOfWeek = dayOfWeek + monthAdd[inputMonth];

  // Tag addieren
  dayOfWeek = dayOfWeek + inputDay;

  // Zuweisung Jahrzehnt zu Offset
  int centuryAdd = 0;
  int century = inputYear / 100;
  switch (century) {
    case 18:
      centuryAdd = 2;
      break;
    case 19:
      centuryAdd = 0;
      break;
    case 20:
      centuryAdd = 6;
      break;
    case 21:
      centuryAdd = 4;
      break;
  }

  // Addiere Offset
  dayOfWeek = dayOfWeek + centuryAdd;

  // Bei Schaltjahr wird für Januar und Februar 1 subtrahiert
  if (checkLeapYear(inputYear)) {
    if (inputMonth == 1 || inputMonth == 2) { // Monat = 1 oder 2?
      dayOfWeek = dayOfWeek - 1;
    }
  }

  // Wochentag ergibt sich aus Reduzieren Modulo 7
  dayOfWeek = dayOfWeek % 7;

  // Array mit Wochentagen
  String[] dayOfWeekNames = {
    "Samstag",
    "Sonntag",
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag"
  };

  // Gebe Wochentag aus
  println(dayOfWeekNames[dayOfWeek]);
}

// Funktion zur Schaltjahrprüfung (aus vorheriger Aufgabe)
boolean checkLeapYear(int yearInput) {
  // Ist Jahreszahl durch 400 teilbar?
  if (yearInput % 400 == 0) {
    return true;
  }
  else { // sonst prüfe,
    // ob Jahreszahl durch 4, aber nicht durch 100 teilbar ist
    if ((yearInput % 4 == 0) && (yearInput % 100 != 0)) {
      return true;
    }
  }
  // Wenn keine Bedingung zutrifft
  return false;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  calcDayOfWeek(1, 1, 1817);
}

