# Körpergewicht in kg
m = 58

# Körpergröße in cm
l = 180

# Alter in Jahren
t = 25

# Formel Mann
mrMale = 66.47 + 13.7 * m + 5 * l - 6.8 * t

# Formel Frau
mrFemale = 655.1 + 9.6 * m + 1.8 * l - 4.7 * t

print "Mann: " + str(mrMale) + " Kalorien pro Tag"
print "Frau: " + str(mrFemale) + " Kalorien pro Tag"

