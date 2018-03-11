// Klasse, die einen Tweet repräsentiert
public class Tweet {
  // Deklaration privater Variablen
  private String username;
  private String text;

  // Öffentlicher Konstruktor, der vorschreibt, dass ein
  // Tweet zwangsläufig aus einem Benutzernamen und dem
  // textuellen Inhalt besteht.
  public Tweet(String username, String text) {
    this.username = username;

    // Beschneide Tweet auf 140 Zeichen,
    // wenn er zu groß ist
    if (text.length() > 140) {
      text = text.substring(0, 140);
    }
    this.text = text;
  }

  // Öffentliche Methode, die den Tweet in geeigneter
  // Weise zurückliefert.
  public String toString() {
    return "\n" + username + ": " + text;
  }
}

// Öffentliche Klasse, die eine Twitterwall repräsentiert
public class TwitterWall {
  // Deklaration privater Variablen
  private Tweet[] tweets;

  // nächste Schreibposition im Array
  private int nextTweet;

  // Konstruktor, der die Anzahl maximal zu verwaltender
  // Tweets erwartet.
  public TwitterWall(int maxTweets) {
    this.tweets = new Tweet[maxTweets];
    this.nextTweet = 0;
  }

  // Öffentliche Methode zum Hinzufügen eines Tweets
  public void addTweet(Tweet tweet) {
    // Wenn kein Platz im Array
    if (nextTweet >= tweets.length) {
      // umkopieren nach vorne
      for (int i = 0; i < tweets.length - 1; i++) {
        tweets[i] = tweets[i + 1];
      }

      // Letzter Eintrag = neuer Tweet
      nextTweet = tweets.length - 1;
    }

    // Füge Tweet hinzu
    tweets[nextTweet] = tweet;

    // erhöhe Zähler
    nextTweet = nextTweet + 1;
  }

  // Öffentliche Methode, die alle Tweets in Form
  // eines Tweet-Arrays in der Reihenfolge der Erzeugung
  // zurückliefert.
  public Tweet[] getTweets() {
    Tweet[] output = new Tweet[nextTweet];
    // Gehe bis letzten Eintrag durch
    for (int i = 0; i < nextTweet; i++) {
      // Kopiere Einträge
      output[i] = tweets[i];
    }

    return output;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  TwitterWall tw = new TwitterWall(2);

  tw.addTweet(new Tweet(
    "Bot1",
    "Dies ist ein Tweet, der so viel Text enthält, dass er über die " +
        "erlaubten 140 Zeichen hinausragen wird. Ehrlich wahr, so " +
        "sollte es sein. #toomuchtext"
  ));
  tw.addTweet(new Tweet("Bot2", "Auch Hallo"));
  tw.addTweet(new Tweet("Bot3", "Wie geht's?"));

  println(tw.getTweets());
}

