// Klasse, die eine Webseite repräsentiert
public class Website {
  private String url;
  private ArrayList<Website> linkedByWebsites;
  
  // Konstruktor, welcher die Webseiten-URL erwartet
  public Website(String url) {
    this.url = url;
    this.linkedByWebsites = new ArrayList<Website>();
  }
  
  public ArrayList<Website> getLinkedByWebsites() {
    return this.linkedByWebsites;
  }
  
  public String getURL() {
    return this.url;
  }
  
  // Funktion, welche eine verlinkte Webseite hinzufügt 
  public void addLink(Website website) {
    this.linkedByWebsites.add(website);
  }
  
  // Funktion, welche die Gesamtanzahl an Links zu dieser
  // Webseite zurückliefert
  public int getTotalLinks() {
    // Warteschlange an Links, die wir noch durchgehen müssen
    ArrayList<Website> queue = new ArrayList<Website>();
    
    // Füge Webseiten zu Warteschlange hinzu
    for (Website linkedByWebsite : this.getLinkedByWebsites()) {
      queue.add(linkedByWebsite);
    }
    
    int linkCount = 0;
    
    // Gehe alle Webseiten durch, bis die Warteschlange leer ist
    while (queue.isEmpty() == false) {
      // Hole erste Webseite aus der Warteschlange
      Website website = queue.get(0);
      
      // Entferne Webseite aus der Warteschlange
      queue.remove(0);
      
      // Erhöhe Linkzähler
      linkCount += 1;
      
      // Füge Webseiten zu Warteschlange hinzu
      for (Website linkedByWebsite : website.getLinkedByWebsites()) {
        queue.add(linkedByWebsite);
      }
    }
    
    return linkCount;
  }
}

// Klasse, die ein Suchmaschinenranking realisiert
public class SearchRanking {
  private Website[] websites;
  
  // Konstruktor, welcher einen Array der zu rankenden
  // Webseiten erwartet.
  public SearchRanking(Website[] websites) {
    this.websites = websites;
  }
  
  // Funktion, welche das erste Suchergebnis bestimmt und ausgibt
  public void printNumberOne() {
    // Speichere das größte Ergebnis
    int numberOneCount = -1;
    Website numberOne = null;
    
    // Gehe alle Webseiten durch
    for (Website website : websites) {
      int numLinks = website.getTotalLinks();
      
      // Wenn der aktuelle Wert größer ist
      if (numLinks > numberOneCount) {
        // Setze Webseite an Spitze
        numberOne = website;
        numberOneCount = numLinks;
      }
    }
    
    println(numberOne.getURL() + " (" + numberOneCount + " Links)");
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  // Baue Webseiten und füge Verlinkungen hinzu
  Website ergebnis1 = new Website("https://erste.website");
  Website ergebnis2 = new Website("https://protrain.github.io");
  Website ergebnis3 = new Website("https://dritte.website");
  
  Website link1 = new Website("https://hilfe.programmieren");
  ergebnis1.addLink(link1);
  ergebnis2.addLink(link1);
  
  Website link2 = new Website("https://mega.influencer");
  ergebnis2.addLink(link2);

  link2.addLink(new Website("https://website1"));
  link2.addLink(new Website("https://website2"));
  Website link3 = new Website("https://website3");
  link2.addLink(link3);
  
  Website link4 = new Website("https://website4");
  link3.addLink(link4);
  
  // Baue Testranking Nummer 1
  Website[] websites = {ergebnis1, ergebnis3};
  SearchRanking ranking = new SearchRanking(websites);
  ranking.printNumberOne();
  
  // Baue Testranking Nummer 2
  Website[] websites2 = {ergebnis1, ergebnis2, ergebnis3};
  ranking = new SearchRanking(websites2);
  ranking.printNumberOne();
}
