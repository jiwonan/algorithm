class Solution {
    int[][] arr;
    
    public int solution(int[][] triangle) {
        int answer = 0;
        arr = triangle;
        
        calc(arr.length - 2);
        return arr[0][0];
    }
    
    private void calc(int r) {
        if(r == -1) return;
        
        for(int i=0;i<arr[r].length;i++) {
            int max = Math.max(arr[r+1][i], arr[r+1][i+1]);
            arr[r][i] = max + arr[r][i];
        }
        
        calc(r-1);
    }
}