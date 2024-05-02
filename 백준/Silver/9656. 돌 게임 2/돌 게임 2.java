import java.util.*;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        String winner = n % 2 == 0 ? "SK" : "CY";
        System.out.println(winner);
    }
}