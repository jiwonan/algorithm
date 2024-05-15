import sys
input = sys.stdin.readline

def bfs(n,m,visited):
    queue = []
    queue.append([0,0])

    while len(queue) != 0:
        p = queue.pop(0)
        r = p[0]
        c = p[1]
        cnt = visited[r][c]

        # 위로 이동
        if r-1 >= 0 and visited[r-1][c] == 1:
            if not (r-1 == 0 and c == 0):
                visited[r-1][c] = cnt+1
                queue.append([r-1,c])
        # 아래로 이동
        if r+1 < n and visited[r+1][c] == 1:
            visited[r+1][c] = cnt+1
            queue.append([r+1,c])
        # 왼쪽으로 이동
        if c-1 >= 0 and visited[r][c-1] == 1:
            if not (r == 0 and c-1 == 0):
                visited[r][c-1] = cnt+1
                queue.append([r,c-1])
        # 오른쪽으로 이동
        if c+1 < m and visited[r][c+1] == 1:
            visited[r][c+1] = cnt+1
            queue.append([r,c+1])

    return visited[n-1][m-1]

def main():
    n,m = map(int, input().split())
    visited = [list() for _ in range(0, n)]

    for i in range(0, n):
        str = input().replace("\n", "")
        visited[i] = list(int(n) for n in str)
    
    print(bfs(n,m,visited))

if __name__ == "__main__":
    main()