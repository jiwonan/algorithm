import sys

total = int(input())
countByLvl = list(map(int, input().split()))

probArr = [list(),list(),list(),list(),list()]

sum = 0

for idx in range(0, total):
    level, time = map(int, sys.stdin.readline().split())
    probArr[level - 1].append(time)

for i in range(0, len(probArr)):
    probArr[i].sort()
    for j in range(0, countByLvl[i]):
        sum += probArr[i][j]
        if j > 0:
            sum += probArr[i][j] - probArr[i][j - 1]
    if i < len(probArr) - 1: sum += 60

print(sum)