// Klasse zur Berechnung des BMI
public static class Health {
  // Statische Methode zur Berechnung der Kategorie in
  // Abhängigkeit des BMI, der an die Methode übergeben wird
  // Die Kategorie wird als Text zurückgegeben
  public static String getCategory(float bmi) {
    // Gebe Kategorie in Abhängigkeit zum Wert zurück
    if (bmi < 18.5) {
      return "untergewichtig";
    }
    else if (bmi >= 18.5 && bmi <= 25) {
      return "normalgewichtig";
    }
    else if (bmi > 25 && bmi <= 30) {
      return "übergewichtig";
    }
    else {
      return "fettleibig";
    }
  }

  // Statische Methode zur Berechnung des BMI.
  // Die Methode erhält die Körpergröße sowie das Gewicht
  // als Eingabe und gibt den berechneten BMI als
  // Fließkommazahl zurück
  public static float computeBMI(int weight, float height) {
    return weight / (height * height);
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  // Testwerte
  int tWeight = 57;
  float tHeight = 1.80;

  // Werte berechnen
  float bmi = Health.computeBMI(tWeight, tHeight);
  String category = Health.getCategory(bmi);

  println("Mit einem BMI von " + bmi + " sind Sie " + category + ".");
}

