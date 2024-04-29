import java.util.*;

// https://www.acmicpc.net/problem/1463

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        if(n==1) {
            System.out.println(0);
            return;
        }

        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[n] = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(n);

        while(!queue.isEmpty()) {
            int v = queue.poll();
            int count = dp[v] + 1;

            if(v % 2 == 0 && dp[v / 2] == Integer.MAX_VALUE) {
                dp[v / 2] = count;
                queue.offer(v/2);
            }

            if(v % 3==0 && dp[v / 3] == Integer.MAX_VALUE) {
                dp[v / 3] = count;
                queue.offer(v/3);
            }

            if(dp[v - 1] == Integer.MAX_VALUE) {
                dp[v - 1] = count;
                queue.offer(v - 1);
            }

            if(dp[1] != Integer.MAX_VALUE) {
                break;
            }
        }

        System.out.println(dp[1]);
    }
}