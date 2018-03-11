// Öffentliche, abstrakte Klasse zur Basisimplementierung eines
// Gewässers. Die Klasse ist nicht instanziierbar; es können also
// keine Objekte dieser Klasse direkt erzeugt werden.
public abstract class Gewaesser {
  // Deklaration privater Variablen
  private String name;
  private boolean schiffbar;
  private float schadstoffbelastung;

  // Öffentlicher Konstruktor, der die Angabe des Namens,
  // der Schiffbarkeit sowie der Schadstoffbelastung erfordert.
  public Gewaesser(
    String name,
    boolean schiffbar,
    float schadstoffbelastung
  ) {
    this.name = name;
    this.schiffbar = schiffbar;
    this.schadstoffbelastung = schadstoffbelastung;
  }

  // Getter-Methode zur Abfrage, in welches andere Gewässer
  // dieses mündet. Diese Methode wird in ableitenden Klassen
  // überschrieben.
  public Gewaesser getMuendetIn() {
    return null;
  }

  // Getter-Methode zur Rückgabe des Gewässernamens
  public String getName() {
    return name;
  }

  // Öffentliche Methode zum Generieren eines repräsentativen
  // Strings.
  public String toString() {
    return name;
  }
}

// Öffentliche Klasse, die ein Meer repräsentiert und dazu von
// der abstrakten Klasse Gewässer ableitet.
public class Meer extends Gewaesser {
  // Deklaration privater Variablen
  private int flaeche;

  // Konstruktor, der Name, Schadstoffbelastung sowie Fläche
  // einfordert
  public Meer(String name, float schadstoffbelastung, int flaeche) {
    // und damit den Konstruktor der Basisklasse (Gewaesser) aufruft.
    // Da ein Meer immer schiffbar ist, wird beim Aufruf des Basisklassen-
    // konstruktors für schiffbar direkt der Wert 'true' gesetzt.
    super(name, true, schadstoffbelastung);

    // und zusätzlich noch die Fläche in der selbst erzeugten Variablen
    // speichert. Denn die Basisklasse hat hierfür keine Variable vor-
    // gesehen.
    this.flaeche = flaeche;
  }
}

// Klasse, die einen Fluss repräsentiert und von der Klasse Gewaesser
// ableitet.
public class Fluss extends Gewaesser {
  // Deklaration privater Variablen, die typisch für einen
  // Fluss sind
  private int laenge;
  private Gewaesser muendetIn;

  // Öffentlicher Konstruktor, der die benötigten Werte
  // entgegennimmt. Ein Fluss mündet in einem anderen
  // Gewässer und wird zusätzlich verlangt.
  public Fluss(
    String name,
    boolean schiffbar,
    float schadstoffbelastung,
    int laenge,
    Gewaesser muendetIn
  ) {
    // Aufruf und Übergabe der Werte an den Konstruktor der
    // Basisklasse Gewaesser
    super(name, schiffbar, schadstoffbelastung);

    // Speichern der zusätzlichen Parameter, die für einen
    // Fluss charakteristisch sind.
    this.laenge = laenge;
    this.muendetIn = muendetIn;
  }

  // Öffentliche Methode, um das nächste erreichbare Meer
  // zu bestimmen.
  public Gewaesser bestimmeMeer() {
    // Gehe ins nächste Gewässer
    Gewaesser gewaesser = this.muendetIn;

    // Solange wir noch weitere Gewässer haben,
    while (gewaesser.getMuendetIn() != null) {
      // gehe Gewässerkette solange durch, bis wir auf Meer stoßen
      // (also kein muendetIn mehr vorhanden ist)
      gewaesser = gewaesser.getMuendetIn();
    }

    return gewaesser;
  }

  // Überschreiben der Basisklassenmethode, die
  // hier aber einen konkreten Wert zurückliefert
  public Gewaesser getMuendetIn() {
    return muendetIn;
  }

  // Öffentliche Methode zur Repräsentation eines Flusses
  public String toString() {
    return super.name + ", mündet in " + getMuendetIn().getName()
        + ", endet" + " in " + bestimmeMeer();
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  Meer nordsee = new Meer("Nordsee", 12.2, 842000);
  Fluss elbe = new Fluss("Elbe", true, 12.3, 1094, nordsee);
  Fluss moldau = new Fluss("Moldau", true, 12.3, 430, elbe);
  Fluss berounka = new Fluss("Berounka", false, 12.3, 138, moldau);
  Fluss havel = new Fluss("Havel", true, 12.3, 334, elbe);

  println(berounka);
  println(moldau);
  println(havel);
}

