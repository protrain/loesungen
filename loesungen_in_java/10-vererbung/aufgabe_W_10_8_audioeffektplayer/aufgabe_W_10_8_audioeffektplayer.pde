// Abstrakte Klasse zur Repräsentation eines Audioeffekts.
// Von dieser Klasse kann keine Instanz (= Objekt) erzeugt werden.
public abstract class AudioEffect {
  // Deklaration privater Variablen
  private String filename;

  // Konstruktor, der zur Angabe eines Dateinamens auffordert
  public AudioEffect(String filename) {
    this.filename = filename;
  }

  // Methode zum Abspielen
  public void play() {
    println("Not implemented!");
  }

  // Getter-Methode zur Rückgabe des Dateinamens
  public String getFilename() {
    return filename;
  }
}

// Öffentliche Klasse für den Wave-Effekt leitet
// von der Klasse AudioEffect ab.
public class WAVEffect extends AudioEffect {
  // Konstruktor erwartet ebenfalls den Dateinamen
  public WAVEffect(String filename) {
    // um diesen an die Basisklasse zu übergeben
    super(filename);
  }

  // Methode zum Abspielen
  public void play() {
    println("PlayWAV: " + getFilename());
  }
}

// Öffentliche Klasse für den MP3Effect-Effekt leitet
// von der Klasse AudioEffect ab.
public class MP3Effect extends AudioEffect {
  public MP3Effect(String filename) {
    super(filename);
  }

  // Methode zum Abspielen
  public void play() {
    println("PlayMp3: " + getFilename());
  }
}

// Öffentliche Klasse für den OGGEffect-Effekt leitet
// von der Klasse AudioEffect ab.
public class OGGEffect extends AudioEffect {
  public OGGEffect(String filename) {
    super(filename);
  }

  // Methode zum Abspielen
  public void play() {
    println("PlayOGG: " + getFilename());
  }
}

// Öffentliche Klasse zur Repräsentation des AudioEffectPlayers
public class AudioEffectPlayer {
  // Deklaration privater Variablen
  private AudioEffect[] effects;
  private int indexToAdd;

  // Konstruktor, der keine zusätzlichen Angaben vorschreibt
  // und die Initialisierung vornimmt.
  public AudioEffectPlayer() {
    this.effects = new AudioEffect[100];
    this.indexToAdd = 0;
  }

  // Methode zum Hinzufügen eines neuen Audioeffekts
  // Der Effekt wird übergeben.
  public void addEffect(AudioEffect effect) {
    // Wenn noch Platz frei, dann hinzufügen
    if (indexToAdd < effects.length) {
      effects[indexToAdd] = effect;
      indexToAdd = indexToAdd + 1;
    }
  }

  // Methode zum Entfernen eines übergebenen
  // Audioeffekts
  public void removeEffect(AudioEffect effect) {
    // Gehe Liste durch
    for (int i = 0; i < effects.length; i++) {
      // Wenn gefunden
      if (effects[i] == effect) {
        // Lösche Element
        effects[i] = null;

        // Kopiere dahinter folgende Elemente nach vorne
        for (int j = i; i < indexToAdd; i++) {
          effects[j] = effects[j + 1];
        }

        // Verringere indexToAdd um eins
        indexToAdd = indexToAdd - 1;

        // Springe aus Schleife
        break;
      }
    }
  }

  // Methode zum Abspielen eines Effekts
  public void play(int id) {
    if (id < indexToAdd) {
      effects[id].play();
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier werden die implementierten Klassen zu Demonstrations- und
// Testzwecken instanziiert und verwendet.
public void setup() {
  AudioEffectPlayer player = new AudioEffectPlayer();
  MP3Effect mp3 = new MP3Effect("Testfile");

  player.addEffect(new WAVEffect("Testfile"));
  player.addEffect(mp3);
  player.addEffect(new OGGEffect("Testfile"));
  player.play(0);
  player.play(1);
  player.removeEffect(mp3);
  player.play(1);
}

