public class ps_eight {
    public static void main(String[] args) {
        int number = 0;
        while (number < 100000000) {
            System.out.println(String.format("%08d", number++));
        }
    }
}
