// Gebe den angegebenen Tag als julianisches Datum zurück
float getJulianDate(float year, float month, float day) {
  if (month < 2) {
    year = year + 1;
    month = month + 12;
  }

  float b = 2 - (year / 100) + (year / 400);
  return (
    365.25 * (year + 4716) + (30.6001 * (month + 1)) + day + b - 1524.5
  );
}

// Gebe die Mondphase als String zurück
String getMoonPhase(float year, float month, float day) {
  // Definiere den Mondzyklus in Tagen
  float moonCyclus = 29.53;

  // Definiere einen Tag, an dem Neumond war
  // Wir nehmen hier den 28.09.2019
  float newMoon = getJulianDate(2019, 9, 28);

  // Definiere den Tag, für den wir die Mondphase berechnen wollen
  float dateToday = getJulianDate(year, month, day);

  // Berechne die Tage seit dem letzten Neumond
  float daysSinceLastNewMoon = int(dateToday - newMoon);

  // Berechne die Anzahl der Neumonde, die seit dem angegebenen
  // Neumond-Datum waren
  float newMoonCount = daysSinceLastNewMoon / moonCyclus;

  // Nehmen wir die Nachkommastelle, wissen wir, wo wir in
  // der Mondphase stehen
  float moonPosition = newMoonCount % 1;

  // Bei Werten kleiner als 0.5 haben wir einen zunehmenden Mond
  if (moonPosition < 0.5) {
    return "Zunehmender Mond";
  }

  // Andernfalls haben wir einen abnehmenden Mond
  return "Abnehmender Mond";
}

void setup() {
  // Jetzt folgen die Testbedingungen
  println("11.11.2019: " + getMoonPhase(2019, 11, 11));
  println("12.11.2019: Vollmond");
  println("13.11.2019: " + getMoonPhase(2019, 11, 13));
  println("25.11.2019: " + getMoonPhase(2019, 11, 25));
  println("26.11.2019: Neumond");
  println("27.11.2019: " + getMoonPhase(2019, 11, 27));
}
