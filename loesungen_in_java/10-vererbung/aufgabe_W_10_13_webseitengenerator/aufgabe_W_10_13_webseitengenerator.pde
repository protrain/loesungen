// Konstanten, mit denen wir die Wetterlage beschreiben
static final int SONNE = 0,
BEWOELKT = 1,
REGEN = 2;

// Abstrakte Klasse zur Repräsentation einer Stadt.
// Von dieser Klasse kann keine Instanz (= Objekt) erzeugt werden.
public abstract class Stadt {
  // Deklaration privater Variablen
  private String name;
  private int wetter;

  // Konstruktor, der zur Angabe eines Städtenamens und des
  // Wetters auffordert
  public Stadt(String name, int wetter) {
    this.name = name;
    this.wetter = wetter;
  }

  // Getter-Methode zur Rückgabe des Städtenamens
  public String getName() {
    return this.name;
  }

  // Getter-Methode zur Rückgabe des Wetters als String
  public String getWetter() {
    if (this.wetter == REGEN) {
      return "regnerisch";
    }
    else if (this.wetter == BEWOELKT) {
      return "bewölkt";
    }
    else if (this.wetter == SONNE) {
      return "sonnig";
    }

    // Unbekannter Wert
    return "Unbekannt";
  }

  // Getter-Methode zur Rückgabe des Webseiten-Inhalts
  // für den Webseiten-Generator.
  public String getContent() {
    return "<p>In " + this.getName() + " ist es " + this.getWetter() +
        ".</p>";
  }

  // Getter-Methode zur Rückgabe der URL zur Wetterseite
  public String getURL() {
    // Wandle Namen in Kleinbuchstaben um
    String name = this
      .getName()
      .toLowerCase();

    // Wandle Leerzeichen im Namen in Bindestriche um
    name = name.replace(" ", "-");

    // Wandle Umlaute um
    name = name.replace("ä", "ae");
    name = name.replace("ü", "ue");
    name = name.replace("ö", "oe");

    // Gebe umgewandelte URL zurück
    return name + ".html";
  }
}

// Öffentliche Klasse für die Großstadt leitet
// von der Klasse Stadt ab.
public class Grossstadt extends Stadt {
  private String[] stadtteile;

  // Konstruktor erwartet ebenfalls einen Städtenamen und das
  // Wetter, aber zusätzlich noch Stadtteile
  public Grossstadt(String name, int wetter, String[] stadtteile) {
    // Städtename und Wetter werden an die Basisklasse
    // übergeben
    super(name, wetter);

    // Stadtteile werden noch gesetzt
    this.stadtteile = stadtteile;
  }

  // Getter-Methode zur Rückgabe des Webseiten-Inhalts
  // für den Webseiten-Generator
  public String getContent() {
    // Hier speichern wir unsere Webseite als HTML-Code.
    // Wir übernehmen zunächst den Code von der Überklasse.
    String output = super.getContent();

    String stadtteile = "";
    // Gehe die Stadtteile durch
    for (int i = 0; i < this.stadtteile.length; i = i + 1) {
      if (i == (this.stadtteile.length - 1)) {
        // Wir sind beim letzten Eintrag:
        // Füge "und" vor dem Stadtteilnamen hinzu
        stadtteile = stadtteile + " und ";
      }

      // Füge Namen des Stadtteils hinzu
      stadtteile = stadtteile + this.stadtteile[i];

      // Wenn wir noch nicht am Ende sind
      if (i < (this.stadtteile.length - 2)) {
        // Füge Komma und Leerzeichen hinzu
        stadtteile = stadtteile + ", ";
      }
    }

    // Füge den Hinweis zu den Stadtteilen hinzu
    output = output + "<p>Dies trifft auch für die Stadtteile " +
        stadtteile + " zu.</p>";

    // Gebe generierten HTML-Code zurück
    return output;
  }

  // Getter-Methode zur Rückgabe der URL zur Wetterseite
  public String getURL() {
    // Generiere URL und gebe sie zurück.
    // Rufe dabei die URL-Generierungsmethode aus der
    // Oberklasse auf.
    return "wetter_grossstadt_" + super.getURL();
  }
}

// Öffentliche Klasse für die Großstadt leitet
// von der Klasse Stadt ab.
public class Kleinstadt extends Stadt {
  // Konstruktor erwartet ebenfalls einen Städtenamen und das
  // Wetter
  public Kleinstadt(String name, int wetter) {
    // Städtename und Wetter werden an die Basisklasse
    // übergeben
    super(name, wetter);
  }

  // Getter-Methode zur Rückgabe des Webseiten-Inhalts
  // für den Webseiten-Generator
  public String getContent() {
    return super.getContent();
  }

  // Getter-Methode zur Rückgabe der URL zur Wetterseite
  public String getURL() {
    // Generiere URL und gebe sie zurück.
    // Rufe dabei die URL-Generierungsmethode aus der
    // Oberklasse auf.
    return "wetter_kleinstadt_" + super.getURL();
  }
}

// Öffentliche Klasse für den Webseitengenerator
public class WebseitenGenerator {
  // Deklaration privater Variablen
  private Stadt[] staedte;

  // Anzahl der Einträge im Array
  private int numEntries = 0;

  public WebseitenGenerator() {
    this.staedte = new Stadt[0];
  }

  // Methode zum Hinzufügen einer Stadt
  public void addStadt(Stadt stadt) {
    // Erzeuge temporären Array mit einem Eintrag mehr
    Stadt[] staedteTemp = new Stadt[numEntries + 1];

    // Kopiere die alten Werte in den neuen Array
    for (int i = 0; i < numEntries; i = i + 1) {
      staedteTemp[i] = this.staedte[i];
    }

    // Füge den neuen Eintrag an der letzten Position hinzu
    staedteTemp[numEntries] = stadt;

    // Setze die neue Liste
    staedte = staedteTemp;

    // Erhöhe die Anzahl der Einträge um eins
    numEntries = numEntries + 1;
  }

  // Methode zum Erstellen und Ausgeben der Navigationsleiste
  // unserer Wetterwebseite
  public String getNavigation() {
    // Hier speichern wir unsere Navigationsleiste als HTML-Code.
    // Wir beginnen mit dem Paragrafen-HTML-Tag
    String output = "<h1>Die Wetter-Webseite</h1><p>";

    // Gehe alle Städte durch
    for (int i = 0; i < this.staedte.length; i = i + 1) {
      // Hole die URL zur Datei
      String url = this
        .staedte[i]
        .getURL();

      // Hole den Städtenamen
      String name = this
        .staedte[i]
        .getName();

      // Füge HTML-Link zur Ausgabe hinzu
      output = output + "<a href='" + url + "'>" + name + "</a>";

      // Füge Trenner hinzu, wenn wir noch nicht am Ende der
      // Liste sind
      if (i < this.staedte.length - 1) {
        output = output + " | ";
      }
    }

    // Schließe den Paragrafen-Tag
    output = output + "</p>";

    // Gebe generierte Navigationsleiste zurück
    return output;
  }

  // Methode zum Erstellen und Ausgeben der HTML-Seite
  // für eine bestimmte Stadt
  public String generatePage(int index) {
    // Hole die Stadt aus dem Array
    Stadt stadt = this.staedte[index];

    // Hier speichern wir unsere Webseite als HTML-Code
    // Setze HTML-Kopf
    String output = "<html><body>";

    // Füge Navigationsleiste hinzu
    output = output + this.getNavigation();

    // Füge Überschrift hinzu
    output = output + "<h2>Das Wetter für " + stadt.getName() + "</h2>";

    output = output + stadt.getContent();

    // Füge HTML-Fußzeile hinzu
    output = output + "</body></html>";

    // Gebe HTML-Code zurück
    return output;
  }

  // Methode zum Erstellen und Ausgeben der Wetterwebseite
  // mit allen Webseiten
  public void generateWebsites() {
    // Generiere Index-Dokument
    // Öffne Datei für die Hauptseite
    PrintWriter output = createWriter("index.html");

    // Generiere HTML-Code für Datei, in der Hauptseite nehmen
    // wir nur die Navigationsleiste
    String htmlCode = this.getNavigation();

    // Speichere HTML-Code in Datei
    output.print(htmlCode);

    // Schließe Datei
    output.close();

    // Gehe alle Städte durch
    for (int i = 0; i < this.staedte.length; i = i + 1) {
      // Öffne Datei mit URL-Dateinamen
      output = createWriter(this.staedte[i].getURL());

      // Generiere HTML-Code für Datei
      htmlCode = this.generatePage(i);

      // Speichere HTML-Code in Datei
      output.print(htmlCode);

      // Schließe Datei
      output.close();
    }

    println("Webseiten generiert");
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  // Definiere Köln
  String[] stadtteileKoeln = {
    "Ehrenfeld",
    "Raderthal",
    "Nippes",
    "Poll",
    "Esch",
    "Pesch",
    "Kalk"
  };
  Grossstadt koeln = new Grossstadt("Köln", SONNE, stadtteileKoeln);

  // Definiere Daaden
  Kleinstadt daaden = new Kleinstadt("Daaden", BEWOELKT);

  // Definiere Bonn
  String[] stadtteileBonn = {
    "Poppelsdorf",
    "Südstadt",
    "Beuel",
    "Duisdorf",
    "Graurheindorf"
  };
  Grossstadt bonn = new Grossstadt("Bonn", REGEN, stadtteileBonn);

  // Initialisiere den Webseitengenerator
  WebseitenGenerator generator = new WebseitenGenerator();

  // Füge die Städte hinzu
  generator.addStadt(koeln);
  generator.addStadt(daaden);
  generator.addStadt(bonn);

  // Generiere die Webseiten
  generator.generateWebsites();
}
