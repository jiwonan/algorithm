import sys
input = sys.stdin.readline

global arr
global visited
global t2
global answer

def dfs(start, cnt):
    global answer
    visited[start] = True
    if start == t2: 
        answer = cnt
        return

    for i in arr[start]:
        if answer == -1 and not visited[i]:
            dfs(i, cnt+1)

def main():
    n = int(input())
    global t2
    t1, t2 = map(int, input().split())
    m = int(input())
    global arr
    arr = [list() for _ in range(0, n+1)]

    for _ in range(0,m):
        a,b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    
    global visited
    visited = [False for _ in range(0,n+1)]

    global answer
    answer = -1

    dfs(t1, 0)
    print(answer)

if __name__ == '__main__':
    main()