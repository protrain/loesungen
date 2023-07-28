// Konstanten zum Ergebnis
int UNENTSCHIEDEN = 0;
int THIS_GEWINNT = 1;
int THIS_VERLIERT = -1;

// Abstrakte Klasse zur Repräsentation einer Hand.
// Von dieser Klasse kann keine Instanz (= Objekt) erzeugt werden.
abstract class Hand {
  // Klassenname, gegen die das Objekt gewinnen würde
  String winsAgainst;
  
  public Hand() {
    // Eine Hand alleine kann nicht gewinne, da wir das Spiel nur
    // mit abgeleiteten Instanzen spielen können.
    this.winsAgainst = null;
  };
  
  // Funktion, welche den Namen der Klasse zurückgibt
  public String getName() {
    return this.getClass().getSimpleName();
  }
  
  // Funktion, die angibt, ob die von Hand abgeleitete
  // Klasse gegen die andere Klasse gewinnt.
  // 0: Unentschieden
  // 1: this gewinnt
  // -1: opponentHand gewinnt
  public int getResult(Hand opponentHand) {
    // Hole Datentyp-Namen vom aktuellen Objekt
    String thisHandType =  this.getName();
    
    // Hole Datentyp-Namen vom gegnerischen Objekt
    String opponentHandType = opponentHand.getName();
        
    // Gleicher Datentyp bring unentschieden
    if (thisHandType.equals(opponentHandType)) {
      return UNENTSCHIEDEN;
    }
    
    if (opponentHandType.equals(winsAgainst)) {
      // Wir haben gewonnen
      return THIS_GEWINNT;
    } else {
      // Wir haben verloren
      return THIS_VERLIERT;
    }
  }
}

// Öffentliche Klasse für Schere leitet
// von der Klasse Hand ab.
final class Schere extends Hand {
  public Schere() {
    this.winsAgainst = "Papier";
  }
}

// Öffentliche Klasse für Stein leitet
// von der Klasse Hand ab.
final class Stein extends Hand {
  public Stein() {
    this.winsAgainst = "Schere";
  }
}

// Öffentliche Klasse für Papier leitet
// von der Klasse Hand ab.
final class Papier extends Hand {
  public Papier() {
    this.winsAgainst = "Stein";
  }
}

// Funktion, welche das Schere-Stein-Papier-Spiel realisiert.
// Die Funktion nimmt abgeleitete Objekte der Hand-Klasse
// entgegen. 
public void playSchereSteinPapier(Hand personA, Hand personB) {
  println(personA.getName() + " vs. " + personB.getName());
  
  // Berechne Ergebnis
  int result = personA.getResult(personB);
  print("Ergebnis: ");
  if (result == UNENTSCHIEDEN) {
    println("Unentschieden");
  } else if (result == THIS_GEWINNT) {
    println(personA.getName() + " gewinnt");
  } else {
    println(personB.getName() + " gewinnt");
  }
  println();
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  playSchereSteinPapier(new Schere(), new Stein());
  playSchereSteinPapier(new Schere(), new Papier());
  playSchereSteinPapier(new Papier(), new Stein());
  playSchereSteinPapier(new Papier(), new Papier());
}
