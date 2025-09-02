/*
 *  Lösung von BinaryDude11100011111 (https://github.com/BinaryDude11100011111)
 *  Hinweis: Der Code ist erst ab Java 11 kompatibel.
 */

public class Main {
    public static void main(String[] args) {
        String indent = "        ";
        int left = 0;
        for (int i = 0; i < 8; i++) {
            System.out.print(indent.repeat(i));
            for (int n = left; n < 7;n++) {
                System.out.printf("(%d | %d) ",left,n);
            }
            System.out.print("\n");
            left++;
        }
    }
}
