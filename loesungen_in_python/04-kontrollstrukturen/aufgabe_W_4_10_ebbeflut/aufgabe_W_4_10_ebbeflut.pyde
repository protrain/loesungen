tag = 0
ebbe_stunde = 5

# Bestimme Uhrzeit, zu der Ebbe ist
ebbe_stunde = 4.0
ebbe_minute = 47.0

print("Tag {} - Ebbe: {} Uhr und {} Minuten"
      .format(tag, int(ebbe_stunde), int(ebbe_minute)))


# Berechne Ebbezeit als Kommazahl
ebbe_komma = ebbe_stunde + ebbe_minute/60.0

# Berechne Zeit zwischen Ebbe und Ebbe als Kommazahl
tide_stunde_n = 12.0
tide_minute_n = 25.0
tide_komma = tide_stunde_n + tide_minute_n/60.0

for i in range(0, 5):
    # Berechne daraus Uhrzeit als Kommazahl, zu der Flut ist
    flut_komma = (ebbe_komma + tide_komma / 2.0)

    # Berechne den Tag
    tag += int(flut_komma / 24)

    # Rechne die Uhrzeit auf den Tag um
    flut_komma %= 24

    # Berechne Stunden und Minuten aus der Kommazahl
    flut_stunde = int(flut_komma)
    flut_minute = int(flut_komma % 1 * 60)

    print("Tag {} - Flut: {} Uhr und {} Minuten"
          .format(tag, flut_stunde, flut_minute))

    # Berechne die nächste Ebbe
    ebbe_komma = (ebbe_komma + tide_komma)

    # Berechne den Tag
    tag += int(ebbe_komma / 24)

    # Rechne die Uhrzeit auf den Tag um
    ebbe_komma %= 24

    # Berechne Stunden und Minuten aus der Kommazahl
    ebbe_stunde = int(ebbe_komma)
    ebbe_minute = int(ebbe_komma % 1 * 60)

    print("Tag {} - Ebbe: {} Uhr und {} Minuten"
          .format(tag, int(ebbe_stunde), int(ebbe_minute)))
