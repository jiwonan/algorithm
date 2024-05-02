import java.util.*;

class Main {
    static int fun = 0;

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        addFun(n);
        System.out.println(fun);
    }

    private static void addFun(int n) {
        if(n == 1) return;

        int a = n / 2;
        int b = a;

        if(n % 2 != 0) {
            b++;
        }

        fun += (a * b);
        addFun(a);
        addFun(b);
    }
}