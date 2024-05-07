import sys

count, snakeLen = map(int, sys.stdin.readline().split())
apples = list(map(int, sys.stdin.readline().split()))
apples.sort()

for apple in apples:
    if apple > snakeLen:
        break
    snakeLen += 1

print(snakeLen)