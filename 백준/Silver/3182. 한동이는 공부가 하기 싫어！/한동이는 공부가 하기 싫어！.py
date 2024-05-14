import sys
input = sys.stdin.readline
graph = []
answer = -1
global visited

def solve(start, cnt):
    if visited[start]:
        return cnt
    visited[start] = True
    return solve(graph[start]-1, cnt + 1)

def main():
    cnt = int(input())
    max = 0
    for _ in range(0, cnt):
        graph.append(int(input()))
    
    global visited
    for idx in range(0, cnt):
        visited = [False for _ in range(0, cnt)]
        res = solve(idx, 0)
        if res > max:
            max = res
            answer = idx
    
    print(answer+1)


if __name__ == "__main__":
    main()
