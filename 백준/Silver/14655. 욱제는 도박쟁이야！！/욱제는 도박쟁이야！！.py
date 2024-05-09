import sys

coinCount = int(input())
firstRound = list(map(int, sys.stdin.readline().split()))
secondRound = list(map(int, sys.stdin.readline().split()))

for idx in range(0, len(firstRound)):
    firstRound[idx] = abs(firstRound[idx])
    secondRound[idx] = abs(secondRound[idx])

print(sum(firstRound) + sum(secondRound))
