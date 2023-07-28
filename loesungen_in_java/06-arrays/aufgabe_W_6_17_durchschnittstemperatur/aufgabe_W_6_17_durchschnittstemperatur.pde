// Funktion, welche prüft, ob wir es bei zwei aufeinander
// folgenden Tageszahlen mit einem neuen Monat zu tun haben.
public boolean isNewMonth(int dayNow, int dayPrevious) {
  if (dayNow < dayPrevious) {
    // Bei einem aufeinanderfolgenden Tag ist der aktuelle
    // Tag nicht kleiner als der vorherige, außer wir haben
    // es mit einem neuen Monat zu tun (wie hier der Fall).
    return true;
  }
  return false;
}

// Funktion, welche die Durchschnittstemperatur berechnet. Als
// Eingabe wird ein Array mit den Tagen und ein Array mit den
// zugehörigen Temperaturen übergeben.
public float[] getMonthlyAverageTemp(int[] days, float[] temps) {
  if (days.length != temps.length) {
    // Beide Arrays sind nicht gleich groß, daher können wir
    // keine Berechnung durchführen
    return null;
  }
  
  // Ausgabearray mit den Durchschnittstemperaturen
  float[] monthlyAverageTemps = new float[12];
  // Aktueller Monat im Array
  int currentMonth = 0;
  
  // Summe der aktuell gesammelten Temperaturen
  float tempsSum = 0.0;
  
  // Anzahl der aktuell gesammelten Temperaturen
  int tempsCount = 0;
  
  int dayPrevious = 0;
  
  // Gehe beide Arrays durch
  for (int i = 0; i < days.length; i++) {
    // Hole Tag und Temperatur
    int day = days[i];
    float temp = temps[i];
      
    // Wenn wir einen neuen Monat haben, dann berechnen wir die
    // Durchschnittswerte und speichern sie in den Ausgabearray
    if (isNewMonth(day, dayPrevious)) {
      float tempAverage = tempsSum / tempsCount;
      monthlyAverageTemps[currentMonth] = tempAverage;
            
      // Setze die Zähler zurück
      tempsCount = 0;
      tempsSum = 0.0;
      
      // Wir sind jetzt im neuen Monat
      currentMonth++;
      
      // Abbruch, wenn wir über 12 Monate sind
      if (currentMonth > 12) {
        break;
      }
    }
    
    // Addiere die Temperaturen auf, aber erst nachdem wir die
    // Tageszahl geprüft haben
    tempsSum += temp;
    tempsCount++;
    
    // Wir speichern vorherigen Tag für die
    // nächste Iteration
    dayPrevious = day;
  }
  
  // Berechne noch den Durchschnitt für die letzte Iteration,
  // sofern noch nicht geschehen
  if (tempsCount > 0) {
      float tempAverage = tempsSum / tempsCount;
      monthlyAverageTemps[currentMonth] = tempAverage;
  }
  
  return monthlyAverageTemps;
} 

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  int daysA[] =  {1, 2, 7, 13, 14, 15, 21, 28, 31, 1, 2, 3, 4, 5};
  float tempsA[] = {11.1, 11.2, 13.3, 15.1, 15.2, 15.3, 16.7, 17.1,
                    18.9, 17.1, 17.0, 16.9, 17.0, 16.9};
                    
  println(getMonthlyAverageTemp(daysA, tempsA));
  println();
                    
  int daysB[] =  {1, 2, 7, 14, 21, 28, 1, 2, 5};
  float tempsB[] = {11, 11, 11, 11, 11, 11, 5, 11, 11};
                    
  println(getMonthlyAverageTemp(daysB, tempsB));
}
