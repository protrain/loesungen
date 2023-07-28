// Klasse, die einen Social-Media-Post repräsentiert
public class Post {
  // Deklaration privater Variablen
  private String username;
  private String text;

  // Öffentlicher Konstruktor, der vorschreibt, dass ein
  // Post zwangsläufig aus einem Anmeldenamen und dem
  // textuellen Inhalt besteht.
  public Post(String username, String text) {
    this.username = username;

    // Beschneide Post auf 140 Zeichen,
    // wenn er zu groß ist
    if (text.length() > 140) {
      text = text.substring(0, 140);
    }
    this.text = text;
  }

  // Öffentliche Methode, die den Post in geeigneter
  // Weise zurückliefert.
  public String toString() {
    return "\n" + username + ": " + text;
  }
}

// Öffentliche Klasse, die eine Socialwall repräsentiert
public class SocialWall {
  // Deklaration privater Variablen
  private Post[] posts;

  // nächste Schreibposition im Array
  private int nextPost;

  // Konstruktor, der die Anzahl maximal zu verwaltender
  // Posts erwartet.
  public SocialWall(int maxPosts) {
    this.posts = new Post[maxPosts];
    this.nextPost = 0;
  }

  // Öffentliche Methode zum Hinzufügen eines Posts
  public void addPost(Post post) {
    // Wenn kein Platz im Array
    if (nextPost >= posts.length) {
      // umkopieren nach vorne
      for (int i = 0; i < posts.length - 1; i++) {
        posts[i] = posts[i + 1];
      }

      // Letzter Eintrag = neuer Post
      nextPost = posts.length - 1;
    }

    // Füge Post hinzu
    posts[nextPost] = post;

    // erhöhe Zähler
    nextPost = nextPost + 1;
  }

  // Öffentliche Methode, die alle Posts in Form
  // eines Post-Arrays in der Reihenfolge der Erzeugung
  // zurückliefert.
  public Post[] getPosts() {
    Post[] output = new Post[nextPost];
    // Gehe bis letzten Eintrag durch
    for (int i = 0; i < nextPost; i++) {
      // Kopiere Einträge
      output[i] = posts[i];
    }

    return output;
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  SocialWall sw = new SocialWall(2);

  sw.addPost(new Post(
    "Bot1",
    "Dies ist ein Post, der so viel Text enthält, dass er über die " +
        "erlaubten 140 Zeichen hinausragen wird. Ehrlich wahr, so " +
        "sollte es sein. #toomuchtext"
  ));
  sw.addPost(new Post("Bot2", "Auch Hallo"));
  sw.addPost(new Post("Bot3", "Wie geht's?"));

  println(sw.getPosts());
}
