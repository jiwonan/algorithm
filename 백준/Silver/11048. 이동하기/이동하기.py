import sys
input = sys.stdin.readline

def main():
    N,M = map(int, input().split())

    maze = []
    maze.append(list())
    for _ in range(0, N):
        row = list(map(int, input().split()))
        row.insert(0,0)
        maze.append(row)
    
    dp = [[0 for _ in range(0, M+1)] for _ in range(0, N+1)]

    for r in range(1, N+1):
        for c in range(1, M+1):
            dp[r][c] = maze[r][c] + max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])

    print(dp[N][M])

if __name__ == "__main__":
    main()