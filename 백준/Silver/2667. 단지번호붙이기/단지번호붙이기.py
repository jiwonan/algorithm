import sys
input = sys.stdin.readline

n = int(input())
apartment = []

for _ in range(0, n):
    str = input().replace("\n", "")
    apartment.append([int(d) for d in str])

visited = [[False for _ in range(0, n)] for _ in range(0, n)]

def count(row, col):
    queue = []
    queue.append([row, col])
    visited[row][col] = True

    cnt = 0

    while len(queue) > 0:
        cnt += 1
        q = queue.pop(0)
        r = q[0]
        c = q[1]

        # 상
        if r >= 1 and not visited[r - 1][c] and apartment[r-1][c] == 1:
            visited[r-1][c] = True
            queue.append([r-1,c])
        
        # 하
        if r < n-1 and not visited[r+1][c] and apartment[r+1][c] == 1:
            visited[r+1][c] = True
            queue.append([r+1, c])
        
        # 좌
        if c >= 1 and not visited[r][c-1] and apartment[r][c-1] == 1:
            visited[r][c-1] = True
            queue.append([r, c-1])

        # 우
        if c < n-1 and not visited[r][c+1] and apartment[r][c+1] == 1:
            visited[r][c+1] = True
            queue.append([r, c+1])

    return cnt

def main():
    result = []

    for i in range(0, n):
        for j in range(0, n):
            if visited[i][j]:
                continue

            if apartment[i][j] == 1:
                result.append(count(i, j))
            else:
                visited[i][j] = True
    
    result.sort()

    print(len(result))

    for r in result:
        print(r)

if __name__ == '__main__':
    main()