# [level 3] 정수 삼각형 - 43105 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43105#qna) 

### 성능 요약

메모리: 61.6 MB, 시간: 7.98 ms

### 구분

코딩테스트 연습 > 동적계획법（Dynamic Programming）

### 채점결과

정확성: 64.3<br/>효율성: 35.7<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 04월 29일 16:39:14

### 문제 설명

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/97ec02cc39/296a0863-a418-431d-9e8c-e57f7a9722ac.png" title="" alt="스크린샷 2018-09-14 오후 5.44.19.png"></p>

<p>위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.</p>

<p>삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한사항</h5>

<ul>
<li>삼각형의 높이는 1 이상 500 이하입니다.</li>
<li>삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>triangle</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]</td>
<td>30</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 풀이 요약
DFS 문제 일 것이라 예상하고 우선 DFS에 대해서 정리했다.

### DFS
깊이 우선 탐색, root에서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 알고리즘.
- 자기 자신을 호출하는 순환 알고리즘 형태를 가지고 있다.
- 모든 노드를 방문해야 하는 경우에 주로 사용된다. (ex 미로찾기)
#### 시간복잡도
인접 행렬 : O(V^2) <br/>
인접 리스트 : O(V+E)

>V: 정점(노드)의 개수<br/>
>E: 간선의 개수

DFS에 대해 알아본 후 다시 문제를 보니 어떻게 적용해야하는지 바로 감이 오지 않아 우선 글로 정리하고 구현해보았다.
```
1. 왼쪽 아니면 오른쪽으로만 갈 수 있다.
2. 함수 진입 시 자기자신을 sum에 더하고 왼쪽, 오른쪽 탐색 진행
3. 마지막 노드에 다다르면 전역의 max 값과 비교 후 더 큰 값으로 max 변경.
4. return

구현 코드
class Solution {
    int max = Integer.MIN_VALUE;
    int[][] arr;
    
    public int solution(int[][] triangle) {
        int answer = 0;
        arr = triangle;
        
        dfs(0,0,0);
        return max;
    }
    
    private void dfs(int r, int c, int sum) {
        sum += arr[r][c];
        
        // 마지막 node
        if(r+1 >= arr.length) {
            if(max < sum) max = sum;
            return;
        }
        
        for(int i=0;i<2;i++) { // 왼쪽 오른쪽 무조건 탐색해야 해서 총 2번
            dfs(r + 1,c + i, sum);
        }
    }
}
```

예시로 주어진 테스트 케이스는 통과했지만, 시간 초과가 떠 반정도를 틀렸다.

불필요한 시점에 로직이 중단되는 로직이 없다는 것을 깨달았지만,
위에서 아래로 내려오는 방식은 max값을 구해야하는 상황에서는 도중에 return 해줘야 할 포인트를 찾기가 어려웠다.

아래에서 위로 더해가며 아래 두 노드와 부모 노드를 더한 값 중 더 큰 값을 더해가는 방식으로 풀어야한다는 결론이 나왔다.
(max값을 구하는 로직 선행)

bottom-up 방식으로 row가 0이 되면 return하는 재귀함수를 구현했다.

+) dynamic programming 문제이다.
