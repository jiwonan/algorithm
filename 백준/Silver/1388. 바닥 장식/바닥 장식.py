import sys
row, col = map(int, input().split())

tiles = []
for r in range(0, row):
    tiles.append(list(sys.stdin.readline()))

def dfs(r, c):
    for y in range(r, row):
        if tiles[y][c] == "|":
            tiles[y][c] = "x"
            continue
        else:
            break

def bfs(r, c):
    for x in range(c, col):
        if tiles[r][x] == "-":
            tiles[r][x] = "x"
            continue
        else:
            break

count = 0

for r in range(0, row):
    for c in range(0, col):
        if tiles[r][c] == "x":
            continue
        elif tiles[r][c] == "|":
            dfs(r,c)
            count += 1
        else:
            bfs(r,c)
            count += 1

print(count)