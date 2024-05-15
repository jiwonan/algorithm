import sys
input = sys.stdin.readline

def bfs(arr, start):
    cnt = 0
    visited = [False for _ in range(0, len(arr))]
    queue = []
    queue.append(start)

    while len(queue) != 0:
        idx = queue.pop(0)
        visited[idx] = True
        for i in arr[idx]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)
    
    return cnt


def main():
    n = int(input())
    m = int(input())
    arr = [list() for _ in range(0, n + 1)]
    for _ in range(0, m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    
    cnt = bfs(arr, 1)
    print(cnt)

if __name__ == "__main__":
    main()