// Setze das Geburtsdatum in Form von drei Integerzahlen
// (Tag, Monat, Jahr)
int day = 21;
int month = 6;
int year = 1970;

// Bestimme Sternzeichen
switch (month) {
  case 1:
    // Entweder Steinbock oder Wassermann
    if (day < 20) {
      println("Steinbock");
    } else {
      println("Wassermann");
    }
    break;
  case 2:
    // Entweder Wassermann oder Fische
    if (day < 19) {
      println("Wassermann");
    } else {
      println("Fische");
    }
    break;
   case 3:
     // Entweder Fische oder Widder
     if (day < 21) {
       println("Fische");
     } else {
       println("Widder");
     }
     break;
   case 4:
     // Entweder Widder oder Stier
     if (day < 21) {
       println("Widder");
     } else {
       println("Stier");
     }
     break;
   case 5:
     // Entweder Stier oder Zwillinge
     if (day < 22) {
       println("Stier");
     } else {
       println("Zwillinge");
     }
     break;
   case 6:
     // Entweder Zwillinge oder Krebs
     if (day < 22) {
       println("Zwillinge");
     } else {
       println("Krebs");
     }
     break;
   case 7:
     // Entweder Krebs oder Löwe
     if (day < 23) {
       println("Krebs");
     } else {
       println("Löwe");
     }
     break;
   case 8:
     // Entweder Löwe oder Jungfrau
     if (day < 23) {
       println("Löwe");
     } else {
       println("Jungfrau");
     }
     break;
   case 9:
     // Entweder Jungfrau oder Waage
     if (day < 23) {
       println("Jungfrau");
     } else {
       println("Waage");
     }
     break;
   case 10:
     // Entweder Waage oder Skorpion
     if (day < 23) {
       println("Waage");
     } else {
       println("Skorpion");
     }
     break;
   case 11:
     // Entweder Skorpion oder Schütze
     if (day < 23) {
       println("Skorpion");
     } else {
       println("Schütze");
     }
     break;
   case 12:
     // Entweder Schütze oder Steinbock
     if (day < 21) {
       println("Schütze");
     } else {
       println("Steinbock");
     }
     break;
   default:
     println("Ungültig");
     break;
}
