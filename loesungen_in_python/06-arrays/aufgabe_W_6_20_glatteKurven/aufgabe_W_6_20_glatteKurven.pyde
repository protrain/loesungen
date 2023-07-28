# Funktion zur Glättung eines Audiosignals
# Erhält das Signal als double-Array
def smooth_audio(signal):
    # leeres Array erzeugen
    output = []

    # Für das erste Element wird der Wert
    # als Durchschnitt der ersten beiden Werte berechnet.
    average = (signal[0] + signal[1]) / 2
    output = output + [average]

    # Restliche Elemente
    for n in range(1, len(signal) - 1):
        # Durchschnitt berechnen
        average = (signal[n - 1] + signal[n] + signal[n + 1]) / 3

        # Wert dem Output hinzufügen
        output = output + [average]

    # ... das wird nochmal gesondert berechnet
    average = (signal[len(signal) - 2] + signal[len(signal) - 1]) / 2
    output = output + [average]

    return output


# Funktion zum Zeichnen des Signals
# An die Funktion wird das Signal als eindimensionales Array sowie
# der Startpunkt für die Zeichnung (ist Fensterhöhe = Unterer Rand)
# übergeben.
def display_audio(signal, y_start):
    x_scale = 8     # Skalierung der Punkte untereinander
    y_scale = 3     # Skalierung der Punkte untereinander
    x_size = 7      # Punktgröße
    x = 0

    for element in signal:
        ellipse(x * x_scale, -element * y_scale + y_start, x_size, x_size)
        x = x + 1


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
size(500, 500)
background(255)
fill(255, 0, 0)

# Generiere Sinus-Signal (20 Elemente)
audio = []
for i in range(0, 20):
    audio += [sin(2 * PI / 20 * i) * 20]

# Baue anschließend Störungen im Signal ein
audio[10] = audio[8] - 8
audio[15] = audio[15] - 7

audioSmooth = smooth_audio(audio)
display_audio(audio, 100)

fill(0, 255, 0, 255)
display_audio(audioSmooth, 300)
