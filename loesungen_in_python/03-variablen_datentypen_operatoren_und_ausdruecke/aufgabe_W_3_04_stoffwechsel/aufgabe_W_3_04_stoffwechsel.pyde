# Körpergewicht in kg
m = 58

# Körpergröße in cm
l = 180

# Alter in Jahren
t = 25

# Formel Mann
mr_male = 66.47 + 13.7 * m + 5 * l - 6.8 * t

# Formel Frau
mr_female = 655.1 + 9.6 * m + 1.8 * l - 4.7 * t

print("Mann: " + str(mr_male) + " Kalorien pro Tag")
print("Frau: " + str(mr_female) + " Kalorien pro Tag")
