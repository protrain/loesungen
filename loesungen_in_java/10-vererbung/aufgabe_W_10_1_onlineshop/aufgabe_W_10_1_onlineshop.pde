// Öffentliche Klasse zur Repräsentation eines Artikels
public class Article {
  // Deklaration privater Variablen
  private int articleNumber;
  private float price;

  // Konstruktor, der die Artikelnummer und den Preis
  // erforderlich macht.
  public Article(int articleNumber, float price) {
    this.articleNumber = articleNumber;
    this.price = price;
  }

  // Getter-Methode, die den Preis zurückliefert.
  public float getPrice() {
    return price;
  }
}

// Öffentliche Klasse, die ein Buch repräsentiert.
// Die Klasse erbt von der Klasse Artikel
public class Book extends Article {
  // Deklaration eigener privater Variablen
  private String author;
  private String title;
  private int year;

  // Der Mehrwertsteuersatz für Bücher (7 %) wird durch die
  // statische Konstante VAT repräsentiert.
  public static final float VAT = 0.07f;

  // Öffentlicher Konstruktor mit der Vorschrift
  // zum Anlegen eines Buchobjekts.
  public Book(
    int articleNumber,
    float price,
    String author,
    String title,
    int year
  ) {
    // Aufruf des Konstruktors der Basisklasse Article
    super(articleNumber, price);

    // Zusätzlich werden die charakterisierenden
    // Eigenschaften eines Buchs gesetzt.
    this.author = author;
    this.title = title;
    this.year = year;
  }

  // Öffentliche Methode zur Berechnung des Bruttopreises
  public float getPrice() {
    // Rufe für Nettopreis die Methode in der Superklasse auf
    // und addiere die für Bücher geltende Mehrwertsteuer
    return super.getPrice() + super.getPrice() * Book.VAT;
  }

  // Öffentliche Methode, die einen geeigneten String generiert
  // und zurückliefert.
  public String toString() {
    return "Buch - " + author + ": " + title + " (" + year + ")";
  }
}

// Klasse, die eine DVD repräsentiert und von der Klasse
// Article ableitet.
class DVD extends Article {
  // Deklaration privater Variablen, die spezifisch für eine
  // DVD sind
  private String name;
  private String duration;
  private int countryCode;

  // Statische Konstante für Mehrwertsteuersatz für DVDs (19 %)
  public static final float VAT = 0.19f;

  // Öffentlicher Konstruktor der Klasse DVD. Zum Generieren eines
  // Objekts der Klasse DVD werden die angegebenen Werte verlangt.
  public DVD(
    int articleNumber,
    float price,
    String name,
    String duration,
    int countryCode
  ) {
    // Aufruf des Basisklassenkonstruktors
    super(articleNumber, price);

    // Zusätzliche Daten werden in den internen Variablen abgelegt.
    this.name = name;
    this.duration = duration;
    this.countryCode = countryCode;
  }

  // Öffentliche Methode zur Berechnung des Bruttopreises
  public float getPrice() {
    // Rufe für Nettopreis die Methode in der Superklasse auf
    // und addiere die für Bücher geltende Mehrwertsteuer
    return super.getPrice() + super.getPrice() * DVD.VAT;
  }

  // Öffentliche Methode, die einen DVD-repräsentativen String
  // zurückliefert.
  public String toString() {
    return "DVD - " + name;
  }
}

// Klasse, die einen Warenkorb realisiert
public class ShoppingCart {
  // Deklaration privater Variablen
  private Article[] cart;

  // Öffentlicher Konstruktor, der den internen
  // Warenkorb initialisiert
  public ShoppingCart() {
    // Noch leerer Warenkorb
    this.cart = new Article[0];
  }

  // Öffentliche Methode zum Hinzufügen eines Artikels
  // zum Warenkorb. Der Artikel wird in Form eines
  // Article-Objekts realisiert. Da sowohl Bücher als
  // auch DVDs von der Klasse Article erben, sind beide
  // Typen hier erlaubt und werden dafür auf die Basis-
  // implementierung zurückgecastet.
  public void addToCart(Article article) {
    // Vergrößere Array um ein Element
    Article[] cartNew = new Article[cart.length + 1];

    // Kopiere alle Artikel rüber
    for (int i = 0; i < cart.length; i++) {
      cartNew[i] = cart[i];
    }

    // Setze neuen Artikel ans Ende der Liste
    cartNew[cartNew.length - 1] = article;

    // Übernehme neue Liste
    cart = cartNew;
  }

  // Öffentliche Methode, die eine Rechnung auf der
  // Konsole druckt
  public void showBill() {
    // Gesamtpreis
    float sum = 0.0f;

    // Jeden Artikel durchgehen
    for (int i = 0; i < cart.length; i++) {
      Article article = cart[i];

      // Gebe Namen und Preis aus
      println(article + "\t " + article.getPrice() + " Euro");

      // Addiere zu Gesamtpreis
      sum = sum + article.getPrice();
    }
    println("------------------------------------");

    // Gebe Gesamtpreis aus
    println("Gesamtpreis: " + str(sum) + " Euro");
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  Book book = new Book(
    122767676,
    32.71,
    "Luigi Lo Iacono",
    "WebSockets",
    2015
  );

  DVD dvd1 = new DVD(
    122767676,
    14.95,
    "Spiel mir das Lied vom Tod",
    "99:12",
    1
  );
  DVD dvd2 = new DVD(
    122767676,
    8.40,
    "Casablanca, Classic Collection",
    "99:12",
    1
  );

  ShoppingCart wk = new ShoppingCart();
  wk.addToCart(book);
  wk.addToCart(dvd1);
  wk.addToCart(dvd2);
  wk.showBill();
}

