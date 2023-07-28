static class Gender {
  // Definiere Konstanten für das Geschlecht
  static int FEMALE = 1;
  static int NONBINARY = 0;
  static int MALE = -1;
}

// Klasse, welche eine Person repräsentiert
class Person {
  private String name;
  private int gender;
  private int expression;
  private int upperHips;
  private int hipSwing;
  private int stability;
  
  // Konstruktor für die Person
  public Person(
    String name,
    int gender,
    int expression,
    int upperHips,
    int hipSwing,
    int stability
  ) {
    this.name = name;
    this.gender = gender;
    this.expression = expression;
    this.upperHips = upperHips;
    this.hipSwing = hipSwing;
    this.stability = stability;
  }
  
  public int getExpression() {
    return this.expression;
  }
  
  public int getUpperHips() {
    return this.upperHips;
  }
  
  public int getHipSwing() {
    return this.hipSwing;
  }
  
  public int getStability() {
    return this.stability;
  }
}

// Abstrakte Klasse, welche einen Tanz repräsentiert
abstract class Dance {
  private Person personA;
  private Person personB;

  // Konstruktor, welcher die beiden involvierten Personen
  // erwartet
  public Dance(Person personA, Person personB) {
    this.personA = personA;
    this.personB = personB;
  }
  
  public Person getPersonA() {
    return this.personA;
  }
  
  public Person getPersonB() {
    return this.personB;
  }
  
  // Private Funktion, welche die Paarharmonie in einer
  // Kategorie berechnet
  private int getHarmonySubscore(
    int scorePersonA,
    int scorePersonB
  ) {
    // Berechne positive Differenz
    int minScore = min(scorePersonA, scorePersonB);
    int maxScore = max(scorePersonA, scorePersonB);
    int difference = maxScore - minScore;
    
    // Ziehe Differenz von Maximalpunktzahl ab
    return 10 - difference;
  }
  
  // Methode zur Bestimmung der Paarharmonie
  public int getHarmonyScore() {
    // Gesamtsumme aller Wertungen
    int scoreSum = 0;
    
    // Gehe alle Wertungen durch
    scoreSum += getHarmonySubscore(
      this.personA.getExpression(),
      this.personB.getExpression()
    );
    
    int[] relevantScores = this.getRelevantCriteriaScores();
    int relevantScorePersonA = relevantScores[0];
    int relevantScorePersonB = relevantScores[1];
    scoreSum += getHarmonySubscore(
      relevantScorePersonA,
      relevantScorePersonB
    );
   
    return scoreSum / 2;
  }
  
  // Methode zur Bestimmung des Paarausdrucks
  public int getExpressionScore() {
    int scorePersonA = this.personA.getExpression();
    int scorePersonB = this.personB.getExpression();
    
    return Math.max(scorePersonA, scorePersonB);
  }
  
  // Methode zur Bestimmung der Körperhaltungswertung.
  public int getPostureScore() {
    int scorePersonA = getRelevantCriteriaScores()[0];
    int scorePersonB = getRelevantCriteriaScores()[1];

    return (scorePersonA + scorePersonB) / 2;
  }
  
  // Methode zur Rückgabe der für Tanz relevanten Kriterums-
  // werte. Da diese in jedem Tanz anders ist, müssen wir sie
  // in den Unterklassen ausformulieren.
  abstract int[] getRelevantCriteriaScores();
  
  // Methode, welche die Wertung der Jury zurückgibt
  public int getJuryScore() {
    return this.getHarmonyScore() 
      + this.getExpressionScore()
      + this.getPostureScore();
  }
}

class StandardDance extends Dance {
  public StandardDance(Person personA, Person personB) {
    // Rufe die Superklasse zur Initialisierung auf
    super(personA, personB);
  }
  
  public int[] getRelevantCriteriaScores() {
    int[] scores = new int[2];
    scores[0] = this.getPersonA().getStability();
    scores[1] = this.getPersonB().getStability();
    
    return scores;
  }
}

class LatinDance extends Dance {
  public LatinDance(Person personA, Person personB) {
    // Rufe die Superklasse zur Initialisierung auf
    super(personA, personB);
  }
  
  public int[] getRelevantCriteriaScores() {
    int[] scores = new int[2];
    scores[0] = this.getPersonA().getHipSwing();
    scores[1] = this.getPersonB().getHipSwing();
    
    return scores;
  }
}

class SwingDance extends Dance {
  public SwingDance(Person personA, Person personB) {
    // Rufe die Superklasse zur Initialisierung auf
    super(personA, personB);
  }
  
  public int[] getRelevantCriteriaScores() {
    int[] scores = new int[2];
    scores[0] = this.getPersonA().getUpperHips();
    scores[1] = this.getPersonB().getUpperHips();
    
    return scores;
  }
}


// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  Person pA = new Person(
    "Francis",
    Gender.NONBINARY,
    7,
    10,
    5,
    5
  );
  
  Person pB = new Person(
    "Tom",
    Gender.MALE,
    4,
    7,
    6,
    7
  );
  
  
  println("LatinDance " + new LatinDance(pA, pB).getJuryScore());
  println("StandardDance " + new StandardDance(pA, pB).getJuryScore());
  println("SwingDance " + new SwingDance(pA, pB).getJuryScore());
}
