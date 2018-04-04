/*gibt einen Weihnachtsbaum aus, indem mehrere for-Schleifen durchlaufen werden*/

public class Weihnachtsbaum2 {
	
	public static void main(String args[]) {
		
		System.out.print("       *      "); 	//Spitze
		
		for (int j = 0; j < 8; j++) {
			
			for (int i = j; i < 7; i++) {
				System.out.print(' ');			//Leerzeichen links
			}
		
			for (int i = j; i > 0; i--) {
				System.out.print('*');			//linke Baumhaelfte
			}
			
			for (int i = j; i > 0; i--) {
				System.out.print('*');			//rechte Baumhaelfte
			}		
			
			System.out.println();				//neue Zeile
		}
		
		System.out.print("     ***     "); 		//Baumstamm
	}
}
