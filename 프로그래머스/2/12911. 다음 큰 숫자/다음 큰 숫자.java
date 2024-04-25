class Solution {
    public int solution(int n) {
        int count = Integer.bitCount(n);
        int answer = n;
        
        while(true) {
            answer++;
            int tempCount = Integer.bitCount(answer);
            if(tempCount == count) break;
        }
        
        return answer;
    }
}