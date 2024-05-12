import sys

num = int(sys.stdin.readline())
heightList = list(map(int, sys.stdin.readline().split()))
heightList.sort()
heightMap = dict()

for height in heightList:
    if height in heightMap:
        heightMap[height] = heightMap[height] + 1
    else:
        heightMap[height] = 1

cnt = 0
left = 0

for key in heightMap:
    cnt += 1
    if heightMap[key] > 1:
        cnt += 1

print(cnt)