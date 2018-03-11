// Öffentliche Klasse zur Repräsentation eines E-Books
public class Ebook {
  // Deklaration privater Variablen
  private MediaAsset[] assets;
  private String author;
  private int year;

  // Öffentlicher Konstruktor, der zur Angabe von
  // Autor und Jahreszahl verpflichtet
  public Ebook(String author, int year) {
    this.assets = new MediaAsset[100];
    this.author = author;
    this.year = year;
  }

  // Getter-Methode zur Rückgabe der Seitenanzahl
  public int numPages() {
    float sum = 0.0f;

    // Gehe Assets-Array durch
    for (int i = 0; i < assets.length; i++) {
      // Ist Eintrag in Array vorhanden, dann Summe errechnen
      if (assets[i] != null) {
        sum = sum + assets[i].numPages();
      }
    }

    return Math.round(sum);
  }

  // Methode, über die ein MediaAsset hinzugefügt werden kann
  // Das Asset muss an die Methode übergeben werden.
  public void addAsset(MediaAsset asset) {
    // Gehe Assets-Array durch
    for (int i = 0; i < assets.length; i++) {
      // Ist kein Eintrag in Array vorhanden, dann einmal hinzufügen
      if (assets[i] == null) {
        assets[i] = asset;

        // Springe aus Schleife
        break;
      }
    }
  }

  // Methode, die eine String-Repräsentation dieses
  // E-Books zurückliefert.
  public String toString() {
    String output = "Ebook: " + author + " (" + year + ")\nSeiten: " +
        numPages() + "\n-------\n";

    // Gehe Array-Inhalte durch
    for (int i = 0; i < assets.length; i++) {
      // Füge toString-Ausgabe hinzu
      if (assets[i] != null) {
        output = output + assets[i].toString();
      }
    }

    return output;
  }
}

// Klasse zur Beschreibung eines MediaAsset
public class MediaAsset {
  // Deklaration privater Variablen
  private String file;
  private int size;
  private String language;

  // Konstruktor, der zur Angabe diverser Informationen verpflichtet
  public MediaAsset(String file, int size, String language) {
    this.file = file;
    this.size = size;
    this.language = language;
  }

  // Methode zur Rückgabe der Seitenanzahl ist hierbei nicht möglich
  public float numPages() {
    // Ein undefiniertes Asset trägt nicht zur Seitenzahl bei
    return 0.0f;
  }

  // Methode zur Repräsentation des Assets
  public String toString() {
    return file + " (" + numPages() + " Seiten)\n";
  }
}

// Öffentliche Klasse zur Repräsentation eines TextAssets, die
// von der Klasse MediaAsset ableitet.
public class TextAsset extends MediaAsset {
  // Deklaration privater Variablen
  private int numChars;

  // Konstruktor, der zur Angabe von Werten für Dateinamen, -größe,
  // Sprache sowie Anzahl an Zeichen verpflichtet
  public TextAsset(String file, int size, String language, int numChars) {
    // Aufruf der Basisklasse und Übergabe der Werte
    super(file, size, language);

    // Spezifische Werte werden lokal gespeichert
    this.numChars = numChars;
  }

  // Methode zur Abfrage der Anzahl an Seiten
  public float numPages() {
    return numChars / 2000.0f;
  }
}

// Öffentliche Klasse zur Repräsentation eines PictureAssets, die
// von der Klasse MediaAsset ableitet.
public class PictureAsset extends MediaAsset {
  // Deklaration privater Variablen
  private int w;
  private int h;

  // Öffentlicher Konstruktor, der zur Angabe der folgenden Werte
  // verpflichtet
  public PictureAsset(
    String file,
    int size,
    String language,
    int w,
    int h
  ) {
    // Aufruf und Übergabe der von der Basisklasse verwalteten Werte
    super(file, size, language);

    // Übrige Werte werden lokal festgehalten
    this.w = w;
    this.h = h;
  }

  // Methode zur Berechnung und Rückgabe der Anzahl von Seiten
  public float numPages() {
    float height = h * (960 / (float)w);
    if (height > 600) {
      return 1.0f;
    }
    else {
      return 0.5f;
    }
  }
}


// Öffentliche Klasse zur Repräsentation eines PictureAssets, die
// von der Klasse MediaAsset ableitet.
public class AudioAsset extends MediaAsset {
  // Deklaration privater Variablen
  private int duration;

  // Öffentlicher Konstruktor, der zur Angabe der folgenden Werte
  // verpflichtet
  public AudioAsset(String file, int size, String language, int duration) {
    // Aufruf und Übergabe der von der Basisklasse verwalteten Werte
    super(file, size, language);

    // Übrige Werte werden lokal festgehalten
    this.duration = duration;
  }

  // Methode zur Berechnung und Rückgabe der Anzahl von Seiten
  public float numPages() {
    return 0.0f;
  }
}


// Öffentliche Klasse zur Repräsentation eines VideoAssets, die
// von der Klasse MediaAsset ableitet.
public class VideoAsset extends MediaAsset {
  // Deklaration privater Variablen
  private int duration;
  private int w;
  private int h;

  // Konstruktor, der zur Angabe der folgenden Werte verpflichtet
  public VideoAsset(
    String file,
    int size,
    String language,
    int duration,
    int w,
    int h
  ) {
    // Aufruf und Übergabe der von der Basisklasse verwalteten Werte
    super(file, size, language);

    // Übrige Werte werden lokal festgehalten
    this.duration = duration;
    this.w = w;
    this.h = h;
  }

  // Methode zur Berechnung und Rückgabe der Anzahl von Seiten
  public float numPages() {
    float height = h * (960 / (float)w);
    if (height > 600) {
      return 1.0f;
    }
    else {
      return 0.5f;
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  Ebook testBook = new Ebook("Stephan Wiefling", 2017);
  testBook.addAsset(new TextAsset("Aufgabe 1", 12, "Deutsch", 3444));
  testBook.addAsset(new AudioAsset("Audio 1", 12, "Deutsch", 95));
  testBook.addAsset(
    new VideoAsset("Video 1", 12, "Deutsch", 95, 800, 800)
  );
  testBook.addAsset(new PictureAsset("Bild 1", 12, "Deutsch", 2000, 600));
  testBook.addAsset(new TextAsset("Aufgabe 2", 12, "Deutsch", 7655));
  println(testBook);
}

