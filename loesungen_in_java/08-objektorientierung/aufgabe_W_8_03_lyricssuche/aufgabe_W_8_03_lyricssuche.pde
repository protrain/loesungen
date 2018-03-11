// Statische Klasse, die nur aus statischen Methoden besteht
public static class Lyrics {
  // Statische Methode, die die URL zu einem Songtext aufbaut.
  // Als Eingabewerte werden Musiker und Titel an die Methode
  // übergeben. Als Ergebnis wird der generierte URL zurückgegeben
  public static String getLyricsURL(String artist, String title) {
    // Konvertiere artist und title in Kleinschreibung
    artist = artist.toLowerCase();
    title = title.toLowerCase();

    // Ersetze Leerzeichen mit Unterstrich
    artist = artist.replaceAll(" ", "_");
    title = title.replaceAll(" ", "_");

    // Baue URL
    String url = "http://lyrics.wikia.com/api.php?func=getSong&artist=";
    url = url + artist + "&song=" + title;

    // Gebe URL zurück
    return url;
  }
}

// Startpunkt des Hauptprogramms
// Zu Demonstrations- und Testzwecken werden die oben programmierten
// statischen Klassenmethoden verwendet.
public void setup() {
  // Lese Interpret und Titel ein
  String interpret = "Die Fantastischen Vier";
  String titel = "MFG";

  println(Lyrics.getLyricsURL(interpret, titel));
}

