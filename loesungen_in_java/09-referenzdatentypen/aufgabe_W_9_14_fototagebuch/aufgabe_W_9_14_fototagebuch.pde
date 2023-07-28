// Import von Bibliotheksfunktionen für den Umgang
// mit dem Datum
import java.util.Date;

// Öffentliche Klasse, die ein Foto repräsentiert
public class Photo {
  // Deklaration privater Variablen
  private String name;

  // Konstruktor, der vorschreibt, dass ein Foto
  // einen Namen haben muss.
  public Photo(String name) {
    this.name = name;
  }

  // Öffentliche Methode zum Generieren einer
  // geeigneten String-basierten Ausgabe
  public String toString() {
    return name;
  }
}

// Öffentliche Klasse, die ein Fototagebuch repräsentiert
public class PhotoDiary {
  // Deklaration privater Variablen
  private Photo[] photos;
  private Date[] dates;

  // Standardkonstruktor, der keine Angaben benötigt
  // und die internen Variablen initialisiert
  public PhotoDiary() {
    photos = new Photo[0];
    dates = new Date[0];
  }

  // Öffentliche Methode zum Hinzufügen eines Fotos,
  // das an die Methode übergeben wird.
  public void addPhoto(Photo p) {
    // Erzeuge um ein Element größeres Array
    Photo[] tPhotos = new Photo[photos.length + 1];
    Date[] tDates = new Date[dates.length + 1];

    // Kopiere bestehende Einträge in das gerade generierte
    // Array rüber
    for (int i = 0; i < photos.length; i++) {
      tPhotos[i] = photos[i];
      tDates[i] = dates[i];
    }

    // Setze letztes Photo mit neuem Foto
    tPhotos[photos.length] = p;

    // Setze letztes Datum mit aktueller Zeit
    tDates[dates.length] = new Date();

    // Übernehme neue Arrays
    photos = tPhotos;
    dates = tDates;
  }

  // Öffentliche Methode, die alle Fotos eines Tages zurückliefert.
  public Photo[] getPhotosByDay(Date day) {
    int count = 0;
    for (int i = 0; i < dates.length; i++) {
      if (DateUtils.isSameDay(dates[i], day)) {
        count = count + 1;
      }
    }

    if (count > 0) {
      Photo[] tPhotos = new Photo[count];
      count = 0;

      for (int i = 0; i < dates.length; i++) {
        if (DateUtils.isSameDay(dates[i], day)) {
          tPhotos[count++] = photos[i];
        }
      }
      return tPhotos;
    }
    else {
      return null;
    }
  }
}

// Öffentliche Hilfsklasse, die eine statische Methode
// enthält.
public static class DateUtils {
  // Methode zur Überprüfung auf Gleichheit eines Tags
  public static boolean isSameDay(Date a, Date b) {
    // Stimmen Tag, Jahr und Monat überein, ist es der gleiche Tag
    if (a.getDay() == b.getDay() && a.getMonth() == b.getMonth()
          && a.getYear() == b.getYear()) {
      return true;
    }
    else {
      return false;
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  PhotoDiary pd = new PhotoDiary();
  pd.addPhoto(new Photo("Foto 1"));
  pd.addPhoto(new Photo("Foto 2"));

  // Heutiges Datum
  Date today = new Date();
  println(pd.getPhotosByDay(today));
}

