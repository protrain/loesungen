// Körpergewicht in kg
int m = 58;

// Körpergröße in cm
int bodyHeight = 180;

// Alter in Jahren
int t = 25;

// Formel Mann
float mrMale = 66.47 + 13.7 * m + 5 * bodyHeight - 6.8 * t;

// Formel Frau
float mrFemale = 655.1 + 9.6 * m + 1.8 * bodyHeight - 4.7 * t;

println("Mann: " + mrMale + " Kalorien pro Tag");
println("Frau: " + mrFemale + " Kalorien pro Tag");
