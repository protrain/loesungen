# Import spezieller Python-Funktionalitäten, damit abstrakte Methoden
# definiert werden können
from abc import ABCMeta, abstractmethod

# Abstrakte Klasse zur Repräsentation eines Audioeffekts.
# Von dieser Klasse kann keine Instanz (= Objekt) erzeugt werden.
class AudioEffect(object):

    # Definiere diese Klasse als abstrakte Klasse. Danach können
    # wir abstrakte Funktionen in dieser Klasse definieren (mit
    # @abstractclass).
    __metaclass__ = ABCMeta

    # Konstruktor, der zur Angabe eines Dateinamens auffordert
    @abstractmethod
    def __init__(self, filename):
        self.__filename = filename

    # Methode zum Abspielen
    @abstractmethod
    def play(self):
        pass

    # Getter-Methode zur Rückgabe des Dateinamens
    def get_filename(self):
        return self.__filename


# Öffentliche Klasse für den Wave-Effekt leitet
# von der Klasse AudioEffect ab.
class WAVEffect(AudioEffect):

    # Konstruktor erwartet ebenfalls den Dateinamen,
    def __init__(self, filename):
        # um diesen an die Basisklasse zu übergeben.
        AudioEffect.__init__(self, filename)

    # Methode zum Abspielen
    def play(self):
        print("PlayWAV: " + self.get_filename())


# Öffentliche Klasse für den MP3Effect-Effekt leitet
# von der Klasse AudioEffect ab.
class MP3Effect(AudioEffect):

    def __init__(self, filename):
        AudioEffect.__init__(self, filename)

    def play(self):
        print("PlayMp3: " + self.get_filename())


# Öffentliche Klasse für den OGGEffect-Effekt leitet
# von der Klasse AudioEffect ab.
class OGGEffect(AudioEffect):

    def __init__(self, filename):
        AudioEffect.__init__(self, filename)

    # Methode zum Abspielen
    def play(self):
        print("PlayOGG: " + self.get_filename())


# Öffentliche Klasse zur Repräsentation des AudioEffectPlayer
class AudioEffectPlayer:

    # Konstruktor, der keine zusätzlichen Angaben vorschreibt
    # und die Initialisierung vornimmt
    def __init__(self):
        self.__effects = []
        for i in range(0, 100):
            self.__effects.append(None)
        self.__index_to_add = 0

    # Methode zum Hinzufügen eines neuen Audioeffekts
    # Der Effekt wird übergeben.
    def add_effect(self, effect):
        # Wenn noch Platz frei, dann hinzufügen.
        if self.__index_to_add < len(self.__effects):
            self.__effects[self.__index_to_add] = effect
            self.__index_to_add += 1

    # Methode zum Entfernen eines übergebenen
    # Audioeffekts
    def remove_effect(self, effect):
        # Gehe Liste durch
        for i in range(0, len(self.__effects)):
            # Wenn gefunden
            if self.__effects[i] == effect:
                # Lösche Element
                self.__effects[i] = None

                # Kopiere dahinter folgende Elemente nach vorne
                for j in range(i, self.__index_to_add):
                    self.__effects[j] = self.__effects[j + 1]

                # Verringere indexToAdd um eins
                self.__index_to_add -= 1

                # Springe aus Schleife
                break

    # Methode zum Abspielen eines Effekts
    def play(self, id_no):
        if id_no < self.__index_to_add:
            self.__effects[id_no].play()


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

player = AudioEffectPlayer()
mp3 = MP3Effect("Testfile")

player.add_effect(WAVEffect("Testfile"))
player.add_effect(mp3)
player.add_effect(OGGEffect("Testfile"))
player.play(0)
player.play(1)
player.remove_effect(mp3)
player.play(1)
