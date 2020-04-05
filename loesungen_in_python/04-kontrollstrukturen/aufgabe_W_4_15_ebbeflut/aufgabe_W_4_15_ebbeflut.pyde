tag = 0

# Bestimme Uhrzeit, zu der Ebbe ist
ebbeStunde = 4.0
ebbeMinute = 47.0

println("Tag {} - Ebbe: {} Uhr und {} Minuten"
        .format(tag, int(ebbeStunde), int(ebbeMinute)))

# Berechne Ebbezeit als Kommazahl
ebbeKomma = ebbeStunde + ebbeMinute / 60.0

# Berechne Zeit zwischen Ebbe und Ebbe als Kommazahl
tideStunden = 12.0
tideMinuten = 25.0
tideKomma = tideStunden + tideMinuten / 60.0

for i in range(0, 5):
    # Berechne daraus Uhrzeit als Kommazahl, zu der Flut ist
    flutKomma = (ebbeKomma + tideKomma / 2.0)

    # Berechne den Tag
    tag += int(flutKomma) / 24

    # Rechne die Uhrzeit auf den Tag um
    flutKomma %= 24

    # Berechne Stunden und Minuten aus der Kommazahl
    flutStunde = int(flutKomma)
    flutMinute = int(flutKomma % 1 * 60)

    println("Tag {} - Flut: {} Uhr und {} Minuten"
            .format(tag, flutStunde, flutMinute))

    # Berechne die nächste Ebbe
    ebbeKomma = (ebbeKomma + tideKomma)

    # Berechne den Tag
    tag += int(ebbeKomma) / 24

    # Rechne die Uhrzeit auf den Tag um
    ebbeKomma %= 24

    # Berechne Stunden und Minuten aus der Kommazahl
    ebbeStunde = int(ebbeKomma)
    ebbeMinute = int(ebbeKomma % 1 * 60)

    println("Tag {} - Ebbe: {} Uhr und {} Minuten"
            .format(tag, int(ebbeStunde), int(ebbeMinute)))
