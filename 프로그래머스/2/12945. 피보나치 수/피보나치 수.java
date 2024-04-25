class Solution {
    public int solution(int n) {
        int divideNum = 1234567;
        int[] fibo = new int[n+1];
        
        fibo[0] = 0 % divideNum;
        fibo[1] = 1 % divideNum;
        
        for(int i=2;i<=n;i++) {
            fibo[i] = (fibo[i-2] + fibo[i-1]) % divideNum;
        }
        
        return fibo[n];
    }
    
void test() {
        int[] fibo = new int[1001];
        
        fibo[0] = 0;
        fibo[1] = 1;
        
        for(int i=2;i<=1000;i++) {
            fibo[i] = fibo[i-2] + fibo[i-1];
        }
        
        System.out.println(fibo[1000] % 873876091);
    }
}