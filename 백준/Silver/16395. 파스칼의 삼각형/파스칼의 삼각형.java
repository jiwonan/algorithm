import java.util.*;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int k = Integer.parseInt(input[1]);

        int[][] dp = new int[n][n];

        dp[0][0] = 1;
        // System.out.println(Arrays.toString(dp[0]));

        for(int i=1; i<n; i++) {
            for(int j=0; j<=i; j++) {
                if(j == 0 || j == i) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                }
            }
            // System.out.println(Arrays.toString(dp[i]));
        }

        System.out.println(dp[n-1][k-1]);
    }
}