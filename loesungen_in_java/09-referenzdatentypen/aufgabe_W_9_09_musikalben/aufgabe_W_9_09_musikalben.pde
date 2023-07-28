// Öffentliche Klasse, die einen einzelnen Song repräsentiert
public class Song {
  // Deklaration privater Variablen
  private String title,
  duration;

  // Konstruktor, der die Angabe des Titelnamens
  // sowie eine Dauer erwartet
  public Song(String title, String duration) {
    this.title = title;
    this.duration = duration;
  }

  // Öffentliche Methode, die den Titel mit der
  // Angabe der Dauer als String zurückliefert.
  public String toString() {
    return title + " -- " + duration;
  }
}

// Öffentliche Klasse für ein Musikalbum
public class Album {
  // Deklaration privater Variablen
  private String artist,
  country,
  album;

  // Deklaration öffentlicher Variablen
  public Song[] songs;

  // Konstruktor, der die Angabe des Künstlers,
  // das Land sowie den Albumtitel und die einzelnen
  // Songs erwartet
  public Album(String artist, String country, String album, Song[] songs) {
    this.artist = artist;
    this.country = country;
    this.album = album;
    this.songs = songs;
  }

  // Öffentliche Methode, die ein komplettes Album
  // mit allen nötigen Informationen zurückliefert
  public String toString() {
    // Generiere Ausgabe
    String output = "Artist: " + artist + "\n";
    output = output + "Land: " + country + "\n";
    output = output + "Album: " + album + "\n";
    output = output + "---------------------\n";

    // Gehe jeden Song durch
    int tracknumber = 1; // Tracknummer
    for (int i = 0; i < songs.length; i++) {
      output = output + tracknumber + ". " + songs[i] + "\n";

      // Erhöhe Tracknummer um 1
      tracknumber = tracknumber + 1;
    }

    return output;
  }
}

// Öffentliche Klasse zur Verwaltung eines Music Store
public class MusicStore {
  // Deklaration privater Variablen
  private Album[] albums;

  // Standardkonstruktor, der die Initialisierung
  // des Album-Arrays übernimmt.
  public MusicStore() {
    this.albums = new Album[0];
  }

  // Methode zum Hinzufügen eines Albums
  public void addAlbum(Album album) {
    Album[] albumsNew = new Album[albums.length + 1];
    int i = 0;
    for (; i < albums.length; i++) {
      albumsNew[i] = albums[i];
    }
    albumsNew[i] = album;
    albums = albumsNew;
  }

  // Öffentliche Methode zur Ausgabe aller Alben
  // auf der Konsole
  public void printAll() {
    for (int i = 0; i < albums.length; i++) {
      println(albums[i]);
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  // Erstelle Album-Songarray
  Song[] fanta4Songs = {
    new Song("Und Täglich Grüßen Fanta Vier / Romantic Fighters", "1:23"),
    new Song("30 Mark", "0:42"),
    new Song("MfG", "3:35"),
    new Song("Hammer", "4:59"),
    new Song("Die Stadt Die Es Nicht Gibt", "4:29"),
    new Song("0:29", "0:30"),
    new Song("Alles Schon Gesehen", "4:25"),
    new Song("Michi Beck In Hell", "5:12"),
    new Song("Home Again", "0:44")
  };

  // Erstelle Album
  Album fanta4 = new Album(
    "Die Fantastischen Vier",
    "Deutschland",
    "4:99",
    fanta4Songs
  );

  // Erstelle Album-Songarray
  Song[] astleySongs = {
    new Song("Never Gonna Give You Up", "3:36"),
    new Song("Whenever You Need Somebody", "3:56"),
    new Song("Together Forever", "3:29"),
    new Song("It Would Take A Strong Strong Man", "3:44"),
    new Song("The Love Has Gone", "4:20"),
    new Song("Don't Say Goodbye", "4:11"),
    new Song("Slipping Away", "3:56"),
    new Song("No More Looking For Love", "3:15"),
    new Song("You Move Me", "3:45"),
    new Song("When I Fall In Love", "3:03")
  };

  // Erstelle Album
  Album astley = new Album(
    "Rick Astley",
    "England",
    "Whenever You Need Somebody",
    astleySongs
  );

  // Erstelle MusicStore und füge Alben hinzu
  MusicStore ms = new MusicStore();
  ms.addAlbum(fanta4);
  ms.addAlbum(astley);

  // Gebe kompletten Music-Store aus
  ms.printAll();
}

