// Öffentliche Klasse zur Repräsentation einer Lampe
public class Lamp {
  // Deklaration interner Variablen
  private int watt;

  // Konstruktor, der die Angabe der Wattzahl verlangt.
  public Lamp(int watt) {
    this.watt = watt;
  }

  // Methode zur Berechnung des jährlichen Energieverbrauchs
  public int annualPowerConsumption(int hoursPerDay) {
    // Formel aus Aufgabe
    return (watt * hoursPerDay * 365) / 1000;
  }

  // Getter-Methode zur Rückgabe der Wattzahl
  public int getWatt() {
    return watt;
  }
}

// Öffentliche Klasse, die von der Klasse Lamp ableitet
public class Bulb extends Lamp {
  // Konstruktor verlangt ebenfalls die Angabe der Wattzahl
  public Bulb(int watt) {
    // Aufruf des Basisklassenkonstruktors
    super(watt);
  }

  // Methode zur Rückgabe eines repräsentativen Strings
  public String toString(int hoursPerDay) {
    return "A bulb consumes " + annualPowerConsumption(hoursPerDay) 
        + " KWh " + "per year.";
  }
}

// Öffentliche Klasse, die von der Klasse Lamp ableitet
public class LEDBulb extends Lamp {
  // Konstruktor verlangt die Angabe der Wattzahl
  public LEDBulb(int watt) {
    // Aufruf des Basisklassenkonstruktors
    super(watt);
  }

  // Methode zur Rückgabe eines repräsentativen Strings
  public String toString(int hoursPerDay) {
    return "A led bulb consumes " +
        annualPowerConsumption(hoursPerDay) + " KWh per year.";
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  Bulb b = new Bulb(60);
  LEDBulb l = new LEDBulb(9);

  println(b.toString(10));
  println(l.toString(10));
}
