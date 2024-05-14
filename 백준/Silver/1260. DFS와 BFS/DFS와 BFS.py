import sys
input = sys.stdin.readline
global arr
global visited

def dfs(start):
    print(start, end=" ")
    visited[start] = True
    for idx in arr[start]:
        if not visited[idx]:
            dfs(idx)

def bfs(start, n):
    queue = []
    queue.append(start)
    visited[start] = True
    while(len(queue) != 0):
        idx = queue.pop(0)
        print(idx, end=" ")
        for v in arr[idx]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)


def main():
    n, m, v = map(int, input().split())
    global arr
    arr = [list() for _ in range(0, n+1)]

    for _ in range(0, m):
        v1, v2 = map(int, input().split())
        arr[v1].append(v2)
        arr[v2].append(v1)
    
    for i in range(0, n + 1):
        arr[i].sort()
    
    global visited
    visited = [False for _ in range(0, n+1)]
    dfs(v)
    print()
    visited = [False for _ in range(0, n+1)]
    bfs(v, n)
    print()

if __name__ == "__main__":
    main()